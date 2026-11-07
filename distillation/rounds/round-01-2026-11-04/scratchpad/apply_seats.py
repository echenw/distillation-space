#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""席位补丁统一落笔器（通用版：跨多题材目录、任意席名、单一写入者）。
用法：python3 apply_seats.py --seats G06-a1,G11-b1 [--declared G06-a1=14,...] [--write] [--merge /tmp/x.json] [--ctl]
"""
import re, os, sys, glob, shutil, collections, json

ROUND = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
LI = os.path.join(ROUND, "notes/loss-inventory")
REFROOT = os.path.join(ROUND, "output/genre-fiction-craft/references")
HDR = re.compile(r"^补丁\s+(?:\*\*)?([A-Za-z0-9_-]+)(?:\*\*)?")
FLD = re.compile(r"^(?:[-*]\s*|\s{2,})(落点文件|定位锚|动作|新文)\s*[：:；]\s?(.*)$")
LABEL = re.compile(r"^(?:[-*]\s*|\s{2,})\**[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z0-9／\s]{1,9}\**\s*[：:；]")
DIRRX = re.compile(r"references/([^/\s`）)]+)/([A-Za-z0-9_-]+\.md)")

def clean(s):
    return s.strip().strip("`").strip()

def anchor_of(raw):
    raw = (raw or "").strip()
    m = re.search(r"`([^`\n]+)`", raw)
    if m:
        return m.group(1).strip()
    return re.sub(r"（[^（）]*(末句|行末|注意|例子|交付|段|行)[^（）]*）\s*$", "", raw).strip().strip("`")

def parse(seat):
    lines = open(os.path.join(LI, "genre-fiction-craft-%s.md" % seat), encoding="utf-8").read().split("\n")
    out, cur, field = [], None, None
    for ln in lines:
        m = HDR.match(ln)
        if m and not ln.startswith("#"):
            if cur:
                out.append(cur)
            cur, field = {"seat": seat, "id": m.group(1)}, None
            continue
        if cur is None:
            continue
        if ln.startswith("## ") or ln.startswith(">") or ln.startswith("```") or ln.strip() == "---":
            field = None
            continue
        f = FLD.match(ln)
        if f:
            key, val = f.group(1), f.group(2)
            cur[key] = val
            field = key if (key == "新文" and "新增小节" in (cur.get("动作") or "")) else None
            continue
        if LABEL.match(ln):
            field = None
            continue
        if field == "新文":
            cur["新文"] = cur.get("新文", "") + "\n" + ln
    if cur:
        out.append(cur)
    res = []
    for p in out:
        for k in list(p):
            if isinstance(p[k], str):
                p[k] = p[k].strip()
        if "定位锚" in p and ("落点文件" in p or "新文" in p):
            res.append(p)
    return res

def resolve(p, prev):
    raw = (p.get("落点文件") or "") + " " + (p.get("定位锚") or "") + " " + (p.get("动作") or "")
    m = DIRRX.search(raw.replace("…", "x/"))
    if m:
        return m.group(1), m.group(2)
    m2 = re.search(r"([A-Za-z0-9_-]+\.md)", p.get("落点文件") or "")
    if m2 and prev:
        nm = m2.group(1)
        if os.path.exists(os.path.join(REFROOT, prev[0], nm)):
            return prev[0], nm
        hits = [d for d in os.listdir(REFROOT) if os.path.exists(os.path.join(REFROOT, d, nm))]
        if len(hits) == 1:
            return hits[0], nm
        if len(hits) > 1:
            return None, "AMBIG:" + nm
    return None, "NOFILE:" + (p.get("落点文件") or "")[:40]

def main():
    a = sys.argv[1:]
    get = lambda k, d=None: (a[a.index(k) + 1] if k in a else d)
    write = "--write" in a
    ctl = get("--ctl")
    seats = (get("--seats") or "").split(",")
    declared = {}
    for kv in (get("--declared") or "").split(","):
        if "=" in kv:
            k, v = kv.split("="); declared[k] = int(v)
    merge_path = get("--merge")
    rootbase = REFROOT if not ctl else ctl
    texts, KNOWN = {}, set()
    patches, problems = [], []
    for s in seats:
        ps = parse(s)
        tag = "" if (s not in declared or declared[s] == len(ps)) else "  ⚠自报=%s" % declared[s]
        print("[parse] %-10s 解析=%s%s" % (s, len(ps), tag))
        prev = None
        for p in ps:
            d, nm = resolve(p, prev)
            if d is None:
                problems.append((s, p["id"], nm)); continue
            fp = os.path.join(rootbase, d, nm)
            if not os.path.exists(fp):
                problems.append((s, p["id"], "MISSING_TARGET:" + d + "/" + nm)); continue
            prev = (d, nm)
            act = p.get("动作", "")
            a_ = ("行内追加" if "行内追加" in act else "精确替换整行" if ("精确替换" in act and "整行" in act)
                  else "精确替换子串" if "精确替换" in act else "新增小节" if "新增小节" in act else "OTHER:" + act[:26])
            new = p.get("新文", "").strip("\n") if a_ == "新增小节" else clean(p.get("新文", ""))
            anch = anchor_of(p.get("定位锚", ""))
            if not anch or not new or a_.startswith("OTHER"):
                problems.append((s, p["id"], "FIELD/ACT:" + a_)); continue
            if d not in texts:
                texts[d] = {f: open(os.path.join(rootbase, d, f), encoding="utf-8").read() for f in os.listdir(os.path.join(rootbase, d)) if f.endswith(".md")}
            KNOWN.add(d)
            p.update(dir=d, file=nm, act=a_, anchor=anch, new=new,
                     hits=texts[d][nm].count(anch))
            if p["hits"] == 1:
                p["line"] = (d, nm, texts[d][nm][:texts[d][nm].index(anch)].count("\n"))
            patches.append(p)

    claims = collections.defaultdict(list)
    for p in patches:
        if p["hits"] == 1:
            claims[p["line"]].append("%s:%s" % (p["seat"], p["id"]))
    collide = {k: v for k, v in claims.items() if len(v) > 1}
    merged_keys = set()
    if merge_path and os.path.exists(merge_path):
        for key, spec in json.load(open(merge_path, encoding="utf-8")).items():
            dirnm, rest = key.split("/", 1)
            fn, ln = rest.rsplit("|", 1)
            k = (dirnm, fn, int(ln) - 1)
            if k not in collide:
                print("[merge] ⚠ 不在冲突组：%s" % key); continue
            for p in patches:
                if p.get("line") == k:
                    p["merged_away"] = True
            patches.append({"seat": "MAIN", "id": "M" + ln, "dir": dirnm, "file": fn,
                            "act": spec.get("act", "行内追加"), "anchor": spec.get("anchor", ""),
                            "new": spec["text"], "hits": 1, "line": k, "do": True,
                            "merge_replaces": [c for c in collide[k]]})
            merged_keys.add(k)
    print("\n[同点冲突组] %d 组" % len(collide))
    for k, v in sorted(collide.items()):
        print("   %s/%s L%d ← %s%s" % (k[0], k[1], k[2] + 1, " / ".join(v), "  【已合并】" if k in merged_keys else ""))

    stat = collections.Counter(); held = []
    for p in patches:
        if p.get("merged_away"):
            stat["merged_away"] += 1; continue
        if p["seat"] == "MAIN":
            continue
        if p["hits"] != 1:
            stat["skip_anchor_%d" % min(p["hits"], 9)] += 1; held.append((p, "锚命中 %d" % p["hits"]))
        elif p["line"] in collide and any(q["act"] in ("精确替换整行", "新增小节") for q in patches if q.get("line") == p["line"]) and p["line"] not in merged_keys:
            stat["hold_collide"] += 1; held.append((p, "同点含整行/新增小节 " + ",".join(collide[p["line"]])))
        else:
            stat["apply_" + p["act"]] += 1; p["do"] = True
    byfile = collections.defaultdict(list)
    for p in patches:
        if p.get("do"):
            byfile[(p["dir"], p["file"])].append(p)
    order = [s for s in seats]
    for (d, fn), plist in byfile.items():
        for p in sorted(plist, key=lambda x: (-x["line"][2], order.index(x["seat"]) if x["seat"] in order else 99,
                                              (0, int(x["id"])) if str(x["id"]).isdigit() else (1, str(x["id"])))):
            lines = texts[d][fn].split("\n"); i = p["line"][2]
            if p["act"] == "行内追加":
                if lines[i].rstrip().endswith("|") and p["anchor"] in lines[i]:
                    k = lines[i].index(p["anchor"]) + len(p["anchor"]); lines[i] = lines[i][:k] + p["new"] + lines[i][k:]
                else:
                    lines[i] = lines[i].rstrip() + p["new"]
            elif p["act"] == "精确替换子串":
                if p["anchor"] not in lines[i]:
                    print("!! %s:%s 锚不在行内，跳过" % (p["seat"], p["id"])); continue
                lines[i] = lines[i].replace(p["anchor"], p["new"], 1)
            elif p["act"] == "精确替换整行":
                lines[i] = p["new"]
            elif p["act"] == "新增小节":
                lines = lines[:i + 1] + [""] + p["new"].split("\n") + lines[i + 1:]
            texts[d][fn] = "\n".join(lines)
        print("[apply] %-12s %-30s %d 条" % (d, fn, len(plist)))
    struct = []
    for (d, fn), plist in byfile.items():
        o = open(os.path.join(REFROOT, d, fn), encoding="utf-8").read().split("\n")
        n = texts[d][fn].split("\n")
        if len(o) != len(n) and not any(p["act"] == "新增小节" for p in plist):
            struct.append("%s/%s 行数 %d->%d" % (d, fn, len(o), len(n)))
        for i, (x, y) in enumerate(zip(o, n)):
            if x.rstrip().endswith("|") and not y.rstrip().endswith("|"):
                struct.append("%s/%s L%d 表格行尾破损" % (d, fn, i + 1))
            if len(y) < len(x) and x.count("|") >= 2:
                struct.append("%s/%s L%d 表格行变短 %d->%d" % (d, fn, i + 1, len(x), len(y)))
    print("[结构检查] 异常 %d 条 %s" % (len(struct), struct[:6]))
    print("[统计] " + "  ".join("%s=%d" % (k, v) for k, v in sorted(stat.items())) +
          "  席位补丁合计=%d" % (sum(stat.values())))
    if held:
        print("[挂起明细] %d 条" % len(held))
        for p, why in held:
            print("   %s:%s %s/%s ← %s" % (p["seat"], p["id"], p["dir"], p["file"], why))
    print("[解析异常] %d %s" % (len(problems), problems[:8]))
    if write:
        os.makedirs("/tmp/prepatch", exist_ok=True); n = 0
        for (d, fn) in byfile:
            fp = os.path.join(REFROOT, d, fn)
            shutil.copy(fp, "/tmp/prepatch/" + d + "__" + fn)
            open(fp, "w", encoding="utf-8").write(texts[d][fn]); n += 1
        print("[WRITE] 已落盘 %d 文件，写前副本在 /tmp/prepatch/" % n)
    else:
        print("[DRY] 未写盘")

main()
