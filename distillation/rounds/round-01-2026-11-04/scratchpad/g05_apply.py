#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G04 六席补丁统一落笔器（单一写入者＝主代理）。
默认 dry；--write 才落盘；--root 指向目标 04 目录（正控制用临时副本）。
"""
import re, os, sys, glob, shutil, collections

ROUND = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
RECDIR = os.path.join(ROUND, "notes/loss-inventory")
REAL04 = os.path.join(ROUND, "output/genre-fiction-craft/references/05-science-fiction")
SEATS = ["a1", "a2", "a3", "a4"]
DECLARED = {"a1": 26, "a2": 27, "a3": 21, "a4": 20}
KNOWN = {os.path.basename(p) for p in glob.glob(os.path.join(REAL04, "*.md"))}

HDR = re.compile(r"^补丁\s+(\*\*)?([A-Za-z0-9]+)(\*\*)?")
FLD = re.compile(r"^(?:[-*]\s*|\s{2,})(落点文件|定位锚|动作|新文)\s*[：:；]\s?(.*)$")
LABEL = re.compile(r"^(?:[-*]\s*|\s{2,})\**[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z0-9／\s]{1,9}\**\s*[：:；]")

def clean(s):
    return s.strip().strip("`").strip()

def anchor_of(raw):
    """锚点取词：带反引号的取首个反引号内文本；否则剥掉尾部括注（末句／行末／注意／例子／交付／段）。"""
    raw = (raw or "").strip()
    m = re.search(r"`([^`\n]+)`", raw)
    if m:
        return m.group(1).strip()
    s = re.sub(r"（[^（）]*(末句|行末|注意|例子|交付|段|行)[^（）]*）\s*$", "", raw).strip()
    return s.strip("`").strip()

def parse(seat):
    path = os.path.join(RECDIR, "genre-fiction-craft-G05-%s.md" % seat)
    lines = open(path, encoding="utf-8").read().split("\n")
    out, cur, field = [], None, None
    for ln in lines:
        if HDR.match(ln) and not ln.startswith("#"):
            if cur:
                out.append(cur)
            cur = {"seat": seat, "id": HDR.match(ln).group(2)}
            field = None
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
            # 只有「新增小节」需要多段新文；其余一律单行，避免吞掉后文段落
            field = key if (key == "新文" and "新增小节" in (cur.get("动作") or "")) else None
            continue
        if LABEL.match(ln):                             # 可能同点／对应记账 等非目标字段：不并入
            field = None
            continue
        if field == "新文":
            cur["新文"] = cur.get("新文", "") + ("\n" if cur.get("新文_multi", True) else "") + ln
    if cur:
        out.append(cur)
    res = []
    for p in out:
        for k in ("定位锚", "新文", "动作", "落点文件"):
            if k in p:
                p[k] = p[k].strip() if isinstance(p[k], str) else p[k]
                p[k] = re.sub(r"\n{3,}", "\n\n", p[k]).strip("\n") if k == "新文" else p[k].strip()
        if "定位锚" in p and "落点文件" in p:
            res.append(p)
    return res

def resolve_file(p, prev):
    raw = (p.get("落点文件") or "").strip()
    hit = re.search(r"([A-Za-z0-9][A-Za-z0-9_-]*\.md)", raw)
    if "同上" in raw and prev:
        return prev, None
    if not hit:
        return None, "NOFILE:" + raw[:40]
    nm = hit.group(1)
    if nm not in KNOWN:
        return None, "UNKNOWN_TARGET:" + nm
    return nm, None

def main():
    args = sys.argv[1:]
    write = "--write" in args
    root = REAL04
    for i, a in enumerate(args):
        if a == "--root":
            root = args[i + 1]
    texts = {n: open(os.path.join(root, n), encoding="utf-8").read() for n in KNOWN}
    patches, problems = [], []
    prev = {}
    for s in SEATS:
        ps = parse(s)
        n = len(ps)
        print("[parse] %s 解析=%s 自报=%s%s" % (s, n, DECLARED[s], "  ⚠差额" if n != DECLARED[s] else ""))
        for p in ps:
            nm, err = resolve_file(p, prev.get(s))
            if err:
                problems.append((s, p["id"], err)); continue
            prev[s] = nm
            p["file"] = nm
            p["anchor"] = anchor_of(p.get("定位锚", ""))
            p["act"] = ("行内追加" if "行内追加" in p.get("动作", "")
                        else "精确替换整行" if ("精确替换" in p.get("动作", "") and "整行" in p.get("动作", ""))
                        else "精确替换子串" if "精确替换" in p.get("动作", "")
                        else "新增小节" if "新增小节" in p.get("动作", "")
                        else "OTHER:" + p.get("动作", "")[:30])
            p["new"] = clean(p.get("新文", "")) if p["act"] != "新增小节" else p.get("新文", "").strip("\n")
            if not p["anchor"] or not p["new"]:
                problems.append((s, p["id"], "EMPTY_FIELD")); continue
            patches.append(p)

    # 锚点命中与同点检测（在原始盘上文本上做，不用中途被改写的文本）
    claims = collections.defaultdict(list)
    for p in patches:
        t = texts[p["file"]]
        c = t.count(p["anchor"])
        p["hits"] = c
        if c == 1:
            line_no = t[:t.index(p["anchor"])].count("\n")
            p["line"] = (p["file"], line_no)
            claims[(p["file"], line_no)].append("%s:%s" % (p["seat"], p["id"]))
        else:
            p["line"] = None

    collide = {k: v for k, v in claims.items() if len(v) > 1}

    # 主代理合并裁决：/tmp/g04_merge.json = {"<file>|<1-based 行号>": "合并后的成品句"}
    MERGE = "/tmp/g05_merge.json"
    merged_keys = set()
    if os.path.exists(MERGE):
        import json as _json
        mm = _json.load(open(MERGE, encoding="utf-8"))
        for key, spec in mm.items():
            fn, ln = key.rsplit("|", 1)
            k = (fn, int(ln) - 1)
            act, txt = (spec["act"], spec["text"]) if isinstance(spec, dict) else ("行内追加", spec)
            anch = spec.get("anchor") if isinstance(spec, dict) else None
            if k not in collide:
                print("[merge] ⚠ 该键当前不在冲突组：%s" % key); continue
            for p in patches:
                if p.get("line") == k:
                    p["merged_away"] = True
            patches.append({"seat": "MAIN", "id": "merge-" + ln,
                            "file": fn, "anchor": anch or txt[:0], "act": act, "new": txt,
                            "hits": 1, "line": k, "do": True})
            merged_keys.add(key)

    stat = collections.Counter()
    held = []
    def destructive(gid):
        return any(q["act"] in ("精确替换整行", "新增小节") for q in patches if q.get("line") == gid)
    for p in patches:
        if p.get("merged_away"):
            stat["merged_away"] += 1; continue
        if p.get("seat") == "MAIN":
            continue
        if p["hits"] != 1:
            stat["skip_anchor_%d" % min(p["hits"], 9)] += 1; held.append((p, "锚点命中 %d 次" % p["hits"]))
        elif p["line"] in collide and len(collide[p["line"]]) > 1 and destructive(p["line"]) and p["line"] not in merged_keys:
            stat["hold_collide"] += 1; held.append((p, "同点冲突（含整行替换）" + ",".join(collide[p["line"]])))
        elif p["act"].startswith("OTHER"):
            stat["hold_action"] += 1; held.append((p, "动作未识别"))
        else:
            stat["apply_" + p["act"]] += 1; p["do"] = True

    print("\n[同点冲突组] %d 组" % len(collide))
    for k, v in sorted(collide.items()):
        print("   %s L%d ← %s" % (k[0], k[1] + 1, " / ".join(v)))
    if "--show-collide" in args:
        for k, v in sorted(collide.items()):
            print("\n=== 组 %s|%d （%d 条）===" % (k[0], k[1] + 1, len(v)))
            for p in patches:
                if p.get("line") == k and p.get("seat") != "MAIN":
                    print("[--]%s:%s %s" % (p["seat"], p["id"], p["act"]))
                    print("   锚：%s" % p["anchor"][:90])
                    print("   文：%s" % p["new"][:400])

    # 落笔：同文件按行号倒序，避免行号漂移
    byfile = collections.defaultdict(list)
    for p in patches:
        if p.get("do"):
            byfile[p["file"]].append(p)
    for fn, plist in byfile.items():
        for p in sorted(plist, key=lambda x: (-x["line"][1],
                                              SEATS.index(x["seat"]) if x["seat"] in SEATS else 99,
                                              (0, int(x["id"])) if str(x["id"]).isdigit() else (1, str(x["id"])))):
            lines = texts[fn].split("\n")
            i = p["line"][1]
            if p["act"] == "行内追加":
                if lines[i].rstrip().endswith("|") and p["anchor"] in lines[i]:
                    k = lines[i].index(p["anchor"]) + len(p["anchor"])
                    lines[i] = lines[i][:k] + p["new"] + lines[i][k:]
                    p["cell_insert"] = True
                else:
                    lines[i] = lines[i].rstrip() + p["new"]
            elif p["act"] == "精确替换子串":
                if p["anchor"] not in lines[i]:
                    print("!! %s:%s 锚不在行内（可能被他席改写），跳过" % (p["seat"], p["id"])); continue
                lines[i] = lines[i].replace(p["anchor"], p["new"], 1)
            elif p["act"] == "精确替换整行":
                lines[i] = p["new"]
            elif p["act"] == "新增小节":
                lines = lines[:i + 1] + [""] + p["new"].split("\n") + lines[i + 1:]
            texts[fn] = "\n".join(lines)
        print("[apply] %-30s %d 条" % (fn, len(plist)))

    pipebad = []
    for fn in byfile:
        o = open(os.path.join(root if False else REAL04, fn), encoding="utf-8").read().split("\n")
        o = open(os.path.join(REAL04, fn), encoding="utf-8").read().split("\n")
        for i, l in enumerate(texts[fn].split("\n")):
            if i < len(o) and l.count("|") != o[i].count("|") and (o[i].count("|") >= 2):
                pipebad.append("%s L%d %d->%d" % (fn, i + 1, o[i].count("|"), l.count("|")))
    print("[表格结构检查] 竖线数变化行 %d 条 %s" % (len(pipebad), pipebad[:6]))
    print("\n[统计] " + "  ".join("%s=%d" % (k, v) for k, v in sorted(stat.items())) + "  合计=%d" % sum(stat.values()))
    print("[挂起明细] %d 条" % len(held))
    for p, why in held:
        print("   %s:%s %s ← %s" % (p["seat"], p["id"], p["file"], why))
    print("[解析异常] %d" % len(problems), problems[:8])

    if write:
        for fn in byfile:
            p = os.path.join(root, fn)
            shutil.copy(p, p + ".preg04")
            open(p, "w", encoding="utf-8").write(texts[fn])
        print("[WRITE] 已落盘 %d 文件，备份后缀 .preg04" % len(byfile))
    else:
        print("[DRY] 未写盘")

main()
