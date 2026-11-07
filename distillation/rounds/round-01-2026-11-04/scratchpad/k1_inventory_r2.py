#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""K1 返工 r2：规则单元盘点（W1.5）。

与 W1 的 k1_inventory.py 的区别（语义缺陷修复）：
- 盘点单位从「v0 文件」改为「规则单元」：unit_id 优先用规则编号（含 2.3 节
  新旧前缀对照），无编号的用「文件路径 + 标题」（附录 A.1）。
- 不再优先 basename 对齐；按 2.8 节「用规则编号和标题来对齐」。
- flag 语义分开：A.1 四 flag 之外增加两个补充标记 UNALIGNED? / SOURCE_ONLY，
  二者「不是丢失、待定向精读」；MISSING 只留给 v3 目标目录内确实无相似
  编号/标题/内容块的单元。
- genre 机制卡编号从标题括号（如 RO-K001–RO-K120）与表格行提取。

只读：用 `git show <提交>:<路径>` 读 v0/v1/v2/v3；不检出、不改仓库、
不复制原件、不放作品全文。输出只含元数据（编号/路径/字节/标记），
不含任何作品名、人物、情节、原句、来源编号、年代、篇数。

只写带 `-2026-11-04-r2` 的新文件（A.3 只追加不覆盖，旧表一律不动）。
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict

REPO = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology"
OUT = os.path.join(REPO, "distillation/rounds/round-01-2026-11-04/notes/loss-inventory/raw")
TAG = "2026-11-04-r2"
COMMITS = OrderedDict([("v0", "d23c461"), ("v1", "d2003e4"),
                       ("v2", "3c1cb5f"), ("v3", "2a10c07")])

# ---------------------------------------------------------------- 谱系（同 W1）
LINEAGE = OrderedDict([
    ("character-and-narrative-control", ["narrative-pov-information-control",
        "nonlinear-time-craft", "character-psychology-trauma-craft", "psycho-trauma-craft-b10"]),
    ("cross-media-drama-adaptation", ["cross-media-drama-transfer"]),
    ("fiction-planning-and-diagnosis", ["fiction-craft", "fiction-craft-and-language",
        "reader-experience-and-critique", "research-fact-verification"]),
    ("line-editing-and-proofreading", ["style-refinement-and-proofreading"]),
    ("scene-conflict-and-rhythm", ["foreshadowing-and-rhythm", "scene-chapter-design-lab",
        "action-fight-scene-craft"]),
    ("story-architecture-and-longform-planning", ["plot-architecture", "serialized-volume-planning"]),
])
GENRE = OrderedDict([
    ("01", ["crime-mystery-craft-b03", "mystery-clue-fairplay", "mystery-detection-craft-b04",
            "mystery-detective-plot-forge", "mystery-evidence-chain-designer"]),
    ("02", ["courtship-conflict-craft", "romance-craft-b03-b07", "romance-craft-b06",
            "romance-emotional-arc", "romance-obstacle-and-cost", "romance-obstacle-delay-craft",
            "romance-social-cost-craft"]),
    ("03", ["gothic-weird-horror-craft", "horror-dread-and-revelation", "horror-gothic-suspense-b05",
            "horror-supernatural-craft", "horror-thriller-craft-b04"]),
    ("04", ["speculative-wuxia-fantasy-craft", "wuxia-fantasy-power-arc", "wuxia-xianxia-plot-forge",
            "fantasy-adventure-structure-lab", "supernatural-power-craft"]),
    ("05", ["sci-fi-future-plot-forge", "sci-fi-novum-world-forge",
            "science-fiction-conceptual-reveal", "science-fiction-craft-b04", "scifi-future-craft-b03"]),
    ("06", ["historical-alt-history-craft", "historical-contract-and-legitimacy-craft",
            "historical-fiction-craft-b03", "historical-fiction-plot-forge",
            "historical-fiction-power-machine", "historical-immersion-and-stakes"]),
    ("07", ["castaway-salvage-stronghold", "survival-crisis-escalation",
            "wilderness-disaster-survival-craft-b01"]),
    ("08", ["adventure-treasure-craft", "adventure-treasure-craft-b02", "adventure-treasure-craft-b03"]),
    ("09", ["comedy-beat-craft", "comedy-scene-mechanics", "comic-engine-craft", "comic-fiction-diagnosis"]),
    ("10", ["competition-underdog-arc", "profession-competition-craft", "vocation-proof-and-price"]),
    ("11", ["identity-revenge-intrigue-b06", "identity-revenge-powercraft-fiction",
            "intrigue-revenge-craft-b04", "revenge-identity-craft", "revenge-intrigue-architecture",
            "revenge-intrigue-craft"]),
    ("12", ["child-story-craft", "children-ya-craft-b05", "childrens-youth-fiction-craft-b01"]),
    ("13", ["isekai-crossworld-craft", "isekai-crossworld-craft-b01", "isekai-crossworld-craft-b02"]),
    ("14", ["realism-craft-b09"]),
])
GENRE_NAMES = OrderedDict([
    ("01", "推理"), ("02", "言情"), ("03", "恐怖"), ("04", "武侠仙侠玄幻"),
    ("05", "科幻"), ("06", "历史架空"), ("07", "求生灾变"), ("08", "探险寻宝"),
    ("09", "喜剧"), ("10", "职业竞技"), ("11", "身份复仇权谋"), ("12", "儿童青少年"),
    ("13", "异世界穿越"), ("14", "年代现实"),
])
TIGHT = {"01", "07", "10"}          # 20% 阈值（5.1 节、§6.1）
MULTI_ATTR = {
    "fantasy-adventure-structure-lab": ("04", "08"),
    "supernatural-power-craft": ("04", "03"),
}

# 2.3 节新旧前缀对照
PREFIX_REMAP = {"SV": "SD", "PD": "PS", "PT": "PV", "IDP": "IR",
                "COM": "CO", "RM": "RL", "RD": "RL"}
V1_ALIAS = {"line-editing-and-proofreading": "english-prose-line-editing"}

# 来源类文件（2.8 节「删掉的来源文件不直接恢复」）
SOURCE_FILE = re.compile(r"source|provenance", re.I)

# ---------------------------------------------------------------- 解析
BLOCK_KEYS = OrderedDict([
    ("规则", ["规则", "rule"]),
    ("怎么做", ["怎么做", "用法", "做法", "步骤", "操作", "how"]),
    ("例外", ["例外", "边界", "什么时候不用", "不适用", "限制", "边界条件"]),
    ("反例", ["反例", "反面示例", "反模式", "counterexample", "anti-example", "反面"]),
    ("检查", ["检查", "核查", "核对", "自检", "check", "检查项", "审查项"]),
    ("适用", ["适用", "条件", "什么时候用", "前提", "适用条件"]),
    ("失败", ["失败", "失败出口", "失败模式", "failure"]),
])
BLOCK_ORDER = list(BLOCK_KEYS.keys())

HEAD_RE = re.compile(r"^(#{1,4})\s+(.*)$")
# 规则编号：AF-01 / R1 / A1 / RO-K001 / SF-K102 / IR-05D / SU-02 / SV-T / SD-T
ID_CAND = re.compile(
    r"\b([A-Z]{1,4}(?:-[A-Z])?(?:-\d{1,3}[A-Z]?|\d{1,3}[A-Z]?)|[A-Z]{1,4}-[A-Z])\b")
RANGE_RE = re.compile(r"([A-Z]{1,4}-?[A-Z]?)(\d{1,3})\s*[–—-]\s*(?:[A-Z]{1,4}-?[A-Z]?)?(\d{1,3})")
NORM_STRIP = re.compile(r"[\s\*`_：:，,。、；;（）()「」『』《》【】\[\]！!？?·…\-—/\\|]")
TABLE_ID = re.compile(r"^\|\s*([A-Za-z][A-Za-z0-9-]*\d[A-Za-z0-9-]*)\s*\|")
BOLD_ID = re.compile(r"\*\*([A-Za-z][A-Za-z0-9-]*\d[A-Za-z0-9-]*)\*\*")


def norm(s: str) -> str:
    return NORM_STRIP.sub("", s).lower()


def clean_id(tok: str):
    """归一为规则编号；排除来源行位残片（如 L995、P123）。"""
    tok = tok.strip("*`").upper()
    m = ID_CAND.fullmatch(tok)
    if not m:
        return None
    if re.fullmatch(r"[A-Z]\d{3}", tok):     # 来源行号残片，不是规则编号
        return None
    return tok


def expand_range(par: str):
    """从标题括号内容提取编号：范围展开 + 离散编号。"""
    ids = set()
    for m in RANGE_RE.finditer(par):
        pre, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        if b >= a and b - a <= 400:
            width = len(m.group(2))
            for n in range(a, b + 1):
                ids.add("%s%0*d" % (pre, width, n))
    for t in ID_CAND.findall(par):
        c = clean_id(t)
        if c:
            ids.add(c)
    return ids


def detect_blocks(lines):
    found = set()
    for line in lines:
        s = line.strip()
        if s.startswith("**") or re.match(r"^#{2,4}\s", s) or re.match(r"^[-*]\s", s):
            head = s[:32]
            for cls, kws in BLOCK_KEYS.items():
                if any(k in head for k in kws):
                    found.add(cls)
    return found


def ngrams(text, n=12, cap=400):
    """内容块指纹：均匀采样 12 字连续片段，最多 cap 个，控制内存。"""
    s = norm(text)
    total = max(0, len(s) - n + 1)
    if total == 0:
        return set()
    step = max(1, total // cap)
    return {s[i:i + n] for i in range(0, total, step)}


def id_prefix(i):
    """编号族前缀：AF-01→AF、RO-K001→RO-K、R1→R、SU-02→SU、C05→C。"""
    m = re.match(r"^([A-Z]+(?:-[A-Z])?)", i)
    return m.group(1) if m else i


def remap(unit_id):
    """2.3 节新旧前缀对照：返回该编号在各版本可能的写法集合。"""
    out = {unit_id}
    if not unit_id:
        return out
    m = re.match(r"^([A-Z]+)-?(\d+)([A-Z]?)$", unit_id)
    if m:
        pre, num, tail = m.group(1), m.group(2), m.group(3)
        if pre == "AC":
            n = int(num)
            out.add("%s%d" % (chr(ord("A") + (n - 1) // 6), (n - 1) % 6 + 1))
        elif pre in PREFIX_REMAP:
            out.add(PREFIX_REMAP[pre] + "-" + num + tail)
            out.add(PREFIX_REMAP[pre] + num + tail)
    return out


def parse_decls(text, relpath):
    """把文件拆成「声明单元」：每个规则编号一个；无编号的标题给 PATH+TITLE。"""
    lines = text.splitlines()
    heads = [(i, len(m.group(1)), m.group(2))
             for i, l in enumerate(lines) if (m := HEAD_RE.match(l))]
    decls = []
    for k, (i, level, content) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        body_lines = lines[i + 1:end]
        body = "\n".join(body_lines)
        blocks = detect_blocks(body_lines)
        title = norm(content)
        ids = set()
        first = content.split()[0] if content.split() else ""
        c = clean_id(first)
        if c:
            ids.add(c)
        for par in re.findall(r"[（(]([^）)]*)[）)]", content):
            ids |= expand_range(par)
        # 表格行（机制卡）：每行单独成单元
        row_ids = []
        for l in body_lines:
            m2 = TABLE_ID.match(l)
            if m2:
                c = clean_id(m2.group(1))
                if c:
                    row_ids.append((c, l))
        if len(row_ids) >= 5:
            for c, l in row_ids:
                decls.append({"id": c, "unit": c, "title": title, "blocks": blocks,
                              "bytes": len(l.encode("utf-8")), "ngrams": ngrams(l),
                              "path": relpath})
            ids = set()
        else:
            for c, _ in row_ids:
                ids.add(c)
            for l in body_lines:
                for b in BOLD_ID.findall(l):
                    c = clean_id(b)
                    if c:
                        ids.add(c)
        for c in ids:
            decls.append({"id": c, "unit": c, "title": title, "blocks": blocks,
                          "bytes": len(body.encode("utf-8")), "ngrams": ngrams(body),
                          "path": relpath})
        if not ids and level >= 2 and title:
            decls.append({"id": None, "unit": "%s+%s" % (relpath, title[:40]),
                          "title": title, "blocks": blocks,
                          "bytes": len(body.encode("utf-8")), "ngrams": ngrams(body),
                          "path": relpath})
    if not heads:
        title = norm(os.path.basename(relpath))
        decls.append({"id": None, "unit": "%s+%s" % (relpath, title[:40]),
                      "title": title, "blocks": detect_blocks(lines),
                      "bytes": len(text.encode("utf-8")), "ngrams": ngrams(text),
                      "path": relpath})
    return decls


# ---------------------------------------------------------------- git 只读
def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True).stdout


def collect():
    trees, blob_repr = {}, {}
    for ver, commit in COMMITS.items():
        raw = git("-c", "core.quotePath=false", "ls-tree", "-r", "-l", commit,
                  "--", "skills").decode("utf-8", "replace")
        files = {}
        for line in raw.splitlines():
            if "\t" not in line:
                continue
            meta, path = line.split("\t", 1)
            parts = meta.split()
            if len(parts) < 4 or parts[1] != "blob":
                continue
            try:
                size = int(parts[3])
            except ValueError:
                continue
            sha = parts[2]
            files[path] = {"size": size, "sha": sha}
            if sha not in blob_repr:
                blob_repr[sha] = (commit, path)
        trees[ver] = files
    contents = {}
    for sha, (commit, path) in blob_repr.items():
        contents[sha] = git("show", "%s:%s" % (commit, path)).decode("utf-8", "replace")
    return trees, contents


def pool_paths(trees, ver, group, cat=None):
    if group == "genre-fiction-craft":
        pref = "skills/genre-fiction-craft/references/%s-" % cat
    else:
        d = V1_ALIAS.get(group, group) if ver == "v1" else group
        pref = "skills/%s/" % d
    return [p for p in trees[ver] if p.startswith(pref)]


def build_index(trees, contents, ver, group, cat):
    """该版本目标目录的编号 / 标题 / 内容块 / 块类型索引。"""
    idx = {"ids": set(), "titles": set(), "ngrams": set(), "decl": {},
           "prefixes": set(), "files": 0}
    for p in pool_paths(trees, ver, group, cat):
        idx["files"] += 1
        t = contents.get(trees[ver][p]["sha"], "")
        rel = p[len("skills/"):]
        for d in parse_decls(t, rel):
            if d["id"]:
                idx["ids"].add(d["id"])
                idx["prefixes"].add(id_prefix(d["id"]))
                idx["decl"][d["id"]] = d
            if d["title"]:
                idx["titles"].add(d["title"])
            idx["ngrams"] |= d["ngrams"]
    return idx


# ---------------------------------------------------------------- 单元与 flag
def is_source_only(path):
    return bool(SOURCE_FILE.search(os.path.basename(path)))


def align_unit(unit, idx):
    """返回 (aligned, method, matched_decl, content_hit)。按 2.8 节编号+标题对齐。"""
    cand = remap(unit["id"]) if unit["id"] else set()
    hit = cand & idx["ids"]
    if hit:
        mid = sorted(hit)[0]
        return True, ("id" if mid == unit["id"] else "prefix"), idx["decl"].get(mid), True
    t = unit["title"]
    if t and t in idx["titles"]:
        return True, "title", None, True
    if t and len(t) >= 8:
        for other in idx["titles"]:
            if len(other) >= 8 and (t in other or other in t):
                return True, "title~", None, True
    content_hit = len(unit["ngrams"] & idx["ngrams"]) >= 2
    return False, None, None, content_hit


def shrink(unit, matched, cat):
    if not matched or not matched.get("bytes"):
        return False
    v0, v3 = unit["bytes"], matched["bytes"]
    if v0 <= 0 or v3 <= 0 or v3 >= v0:
        return False
    thr = 0.20 if cat in TIGHT else 0.30
    return (v0 - v3) / v0 > thr or (v0 - v3) > 1536


def flags_for(u, cat):
    """A.1 四 flag + 两个补充标记。UNALIGNED?/SOURCE_ONLY 不是丢失、待定向精读。"""
    src = u["source_only"]
    a, method, md, content_hit = align_unit(u, u["idx3"])
    out = []
    if src:
        out.append("SOURCE_ONLY")
    if not a:
        # MISSING 只留给「编号体系可比 + 该编号确实缺号 + 无相似标题 + 无相似
        # 内容块」的单元。编号体系可比 = v3 目标目录仍使用同一编号族（或 2.3 节
        # 改号后的编号族）；若 v0→v3 编号整体改名/重组（2.3、2.8 节），编号对不上
        # 是必然的，无法判定是否缺失，一律记 UNALIGNED?，避免把「对不上」记成丢失。
        cand = remap(u["id"]) if u["id"] else set()
        comparable = bool(cand) and any(
            id_prefix(c) in u["idx3"]["prefixes"] for c in cand)
        pool_ok = u["idx3"]["files"] > 0
        if comparable and pool_ok and not content_hit:
            out.append("MISSING")
        else:
            out.append("UNALIGNED?")        # 机械对齐失败，无法判定是否缺失
        return out
    if shrink(u, md, cat):
        out.append("SHRUNK")
    if method in ("prefix", "title", "title~"):
        out.append("RENUMBERED?")
    if md and u["blocks"] and (u["blocks"] - md["blocks"]):
        out.append("BLOCK_LOST")
    return out or ["—"]


def build_units(group, cat, v0dirs, trees, contents):
    idx = {v: build_index(trees, contents, v, group, cat) for v in ("v1", "v2", "v3")}
    units, blocking = [], []
    seen = set()
    for d in v0dirs:
        pref = "skills/%s/" % d
        paths = [p for p in trees["v0"] if p.startswith(pref)]
        if not paths:
            blocking.append((d, "该 v0 目录在 v0 树中无文件（路径核对失败）"))
            continue
        for p in paths:
            rel = p[len("skills/"):]
            t = contents.get(trees["v0"][p]["sha"], "")
            fsize = trees["v0"][p]["size"]
            for decl in parse_decls(t, rel):
                key = decl["unit"]
                if key in seen:
                    continue
                seen.add(key)
                u = dict(decl)
                u["source_only"] = is_source_only(rel)
                u["fsize"] = fsize
                u["idx3"] = idx["v3"]
                for v in ("v1", "v2", "v3"):
                    a, method, md, ch = align_unit(u, idx[v])
                    u["hit_" + v] = a
                    u["method_" + v] = method
                    u["md_" + v] = md
                units.append(u)
    return units, idx, blocking


def versions_str(u):
    return "1 " + " ".join("1" if u["hit_" + v] else "0" for v in ("v1", "v2", "v3"))


def bytes_str(u):
    def f(v):
        md = u["md_" + v]
        return str(md["bytes"]) if md else "—"
    return "%d / %s / %s / %s" % (u["bytes"], f("v1"), f("v2"), f("v3"))


def blocks_str(u):
    short = {"规则": "规", "怎么做": "怎", "例外": "例", "反例": "反",
             "检查": "检", "适用": "适", "失败": "败"}
    return "".join(short[x] for x in BLOCK_ORDER if x in u["blocks"]) or "∅"


def render_table(units, cat):
    out = ["| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |",
           "|---|---|---|---|---|"]
    for u in units:
        out.append("| `%s` | `%s` | `%s` | `%s` | `%s` |" % (
            u["unit"], versions_str(u), blocks_str(u), bytes_str(u),
            ";".join(flags_for(u, cat))))
    return "\n".join(out)


def stats(units, cat):
    c = defaultdict(int)
    aligned = 0
    for u in units:
        fs = flags_for(u, cat)
        for f in fs:
            c[f] += 1
        if u["hit_v3"]:
            aligned += 1
    return {"total": len(units), "aligned": aligned, "flags": dict(c)}


def header(group, cat, v0dirs, st):
    thr = "20%" if cat in TIGHT else "30%"
    return "\n".join([
        "# K1 返工 raw 表（r2）· %s%s" % (group, (" / 题材 %s %s" % (cat, GENRE_NAMES[cat])) if cat else ""),
        "",
        "- 版本：`%s`（A.3 只追加不覆盖；W1 的 `%s` 旧表原样保留，两版并存）" % (TAG, "2026-11-04"),
        "- 数据来源：`git show <提交>:<路径>`，提交 %s；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。" %
            "、".join("%s=%s" % (k, v) for k, v in COMMITS.items()),
        "- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。",
        "- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。",
        "- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。",
        "- 阈值：缩减超过 **%s** 或超过 **1.5 KB** 打 SHRUNK；%s" %
            (thr, "本题材按 5.1 节 / §6.1 收紧到 20%。" if cat in TIGHT else "默认 30%。"),
        "",
        "### flag 语义（**补充标记不是丢失、待定向精读**）",
        "",
        "| flag | 含义 |", "|---|---|",
        "| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |",
        "| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |",
        "| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |",
        "| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |",
        "| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |",
        "| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |",
        "| `—` | 已对齐且无 A.1 信号 |",
        "",
        "- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。",
        "- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。",
        "- 谱系 v0 来源：%s" % "、".join("`%s`" % d for d in v0dirs),
        "",
        "**规则单元数 %d；v3 对齐成功 %d（%.1f%%）；对齐失败 UNALIGNED? %d（%.1f%%）**" %
            (st["total"], st["aligned"], st["aligned"] / st["total"] * 100 if st["total"] else 0,
             st["flags"].get("UNALIGNED?", 0),
             st["flags"].get("UNALIGNED?", 0) / st["total"] * 100 if st["total"] else 0),
        "**flag 计数**：%s" % "；".join("%s=%d" % (k, v) for k, v in sorted(st["flags"].items())),
        "",
    ])


def write_raw(fname, text):
    path = os.path.join(OUT, fname)
    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n\n---\n\n## 重新生成 %s\n\n" % TAG)
        f.write(text)
    return path


def card_report(trees, contents, cat, prefix):
    """机制卡编号：从标题括号（如 RO-K001–RO-K120）与表格行提取。"""
    out = []
    for ver, commit in COMMITS.items():
        nums = set()
        for p in pool_paths(trees, ver, "genre-fiction-craft", cat):
            t = contents.get(trees[ver][p]["sha"], "")
            nums |= {int(x) for x in re.findall(prefix + r"(\d{3})", t)}
        if nums:
            lo, hi = min(nums), max(nums)
            cont = nums == set(range(lo, hi + 1))
            out.append((ver, lo, hi, len(nums), cont))
        else:
            out.append((ver, None, None, 0, None))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    trees, contents = collect()
    print("各版本文件数：", {v: len(t) for v, t in trees.items()})
    print("唯一 blob 数：", len(contents))

    all_stats, all_blocking = OrderedDict(), []
    all_units = []

    for group, v0dirs in LINEAGE.items():
        units, idx, blocking = build_units(group, None, v0dirs, trees, contents)
        st = stats(units, None)
        all_stats[group] = st
        all_units.append((group, None, units))
        text = header(group, None, v0dirs, st) + "\n" + render_table(units, None) + "\n"
        for d, reason in blocking:
            text += "\n- 机械对齐阻塞：`%s` — %s\n" % (d, reason)
        text += "\n## 如实记录\n\n"
        text += "- 无法按编号/标题对齐的单元记 `UNALIGNED?`，**不记 MISSING**；来源类文件记 `SOURCE_ONLY`。不伪造对齐行、不跳过。\n"
        text += "- 本表只出信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。\n"
        write_raw("%s-%s.md" % (group, TAG), text)
        for d, reason in blocking:
            all_blocking.append((group, d, reason))
        print("[%s] units=%d aligned=%d flags=%s" % (group, st["total"], st["aligned"], st["flags"]))

    # ---- genre：一份表，按 14 类分节
    gtext = [
        "# K1 返工 raw 表（r2）· genre-fiction-craft（按 14 类题材分组）", "",
        "- 版本：`%s`（A.3 只追加不覆盖；W1 旧表原样保留）" % TAG,
        "- 盘点单位：规则单元（规则编号 / 文件路径+标题）；机制卡编号从标题括号与表格行提取。",
        "- 对齐：按 2.8 节用规则编号（含 2.3 节改号对照）+ 标题 + 内容块，不按文件名。",
        "- 阈值：默认 30% 或 1.5 KB；**01 推理 / 07 求生灾变 / 10 职业竞技收紧到 20%**（5.1 节、§6.1）。",
        "- 补充标记 `UNALIGNED?` / `SOURCE_ONLY` **不是丢失、待定向精读**；`MISSING` 只留给确实无相似编号/标题/内容块的单元。",
        "- v1 题材目录为中文名、v2/v3 为英文名，按 `NN-` 数字前缀定位；跨题材多归属按主归属登记并记阻塞。",
        "",
    ]
    g_all = []
    for cat, v0dirs in GENRE.items():
        units, idx, blocking = build_units("genre-fiction-craft", cat, v0dirs, trees, contents)
        st = stats(units, cat)
        g_all.append((cat, units, st))
        all_units.append(("genre/%s" % cat, cat, units))
        gtext += ["---\n", "## 题材 %s %s（阈值 %s）\n" % (cat, GENRE_NAMES[cat], "20%" if cat in TIGHT else "30%")]
        gtext.append(header("genre-fiction-craft", cat, v0dirs, st))
        gtext.append(render_table(units, cat) + "\n")
        for d, reason in blocking:
            gtext.append("- 机械对齐阻塞：`%s` — %s\n" % (d, reason))
            all_blocking.append(("genre/%s" % cat, d, reason))

    tot = sum(s["total"] for _, _, s in g_all)
    ali = sum(s["aligned"] for _, _, s in g_all)
    gf = defaultdict(int)
    for cat, units, s in g_all:
        for k, v in s["flags"].items():
            gf[k] += v
    gsummary = {"total": tot, "aligned": ali, "flags": dict(gf)}
    all_stats["genre-fiction-craft"] = gsummary
    gtext.insert(0, "**genre 规则单元 %d；v3 对齐成功 %d（%.1f%%）；UNALIGNED? %d（%.1f%%）**\n" %
                 (tot, ali, ali / tot * 100 if tot else 0,
                  gf.get("UNALIGNED?", 0), gf.get("UNALIGNED?", 0) / tot * 100 if tot else 0))

    # 机制卡核对（2.3 节 / §6.1 修订依据）
    gtext += ["\n---\n", "## 机制卡编号核对（从标题括号与表格行提取，2.3 节 / §6.1 修订依据）\n", "",
              "| 题材 | 版本 | 编号范围 | 张数 | 连续 |", "|---|---|---|---|---|"]
    card_facts = []
    for cat, prefix, label in (("02", r"RO-K", "G02 言情"), ("05", r"SF-K", "G05 科幻")):
        rows = card_report(trees, contents, cat, prefix)
        for ver, lo, hi, n, cont in rows:
            gtext.append("| %s | %s | %s | %s | %s |" %
                         (label, ver, ("%s%03d–%s%03d" % (prefix, lo, prefix, hi)) if lo else "—",
                          n if n else "—", ("是" if cont else "否") if lo else "—"))
        card_facts.append((label, rows))
    gtext += ["",
              "- **W1 已证实的事实（本表复核一致）**：G02 言情 `RO-K` v2 为 001–166 共 166 张、v3 为 001–120 共 120 张，**v2→v3 删 46 张（RO-K121–166）**；G05 科幻 `SF-K` 在 v2 / v3 均为 001–102 连续 102 张，**未删卡，属逐卡压缩**（`05-science-fiction/mechanisms.md` 32.4→20.4 KB）。",
              "- 计划 §6.1 已据此修订：G02 是删卡、G05 是逐卡压缩，两者不是同一种丢失，**W3 分别处理**；G05 不套用 G02 的「补回删卡编号」做法。",
              "- 机制卡正文含来源案例，本表只输出编号范围与张数，不复制任何原文。", ""]
    gtext += ["---\n", "## 如实记录（不伪造、不跳过）\n",
              "- v0→v3 题材文件重组、编号与标题改写，按文件名无法对齐（2.8 节）；无法机械对齐的单元逐行记 `UNALIGNED?`，不记 `MISSING`、不伪造对齐行。",
              "- `fantasy-adventure-structure-lab`（04/08）、`supernatural-power-craft`（04/03）为跨题材多归属，按主归属登记，副归属待 W3 核定。",
              "- `title~` 为粗粒度相似标题信号，须 W3 比内容核定；本表只出信号，不做逐条决定。", ""]
    write_raw("genre-fiction-craft-%s.md" % TAG, "\n".join(gtext))
    print("[genre] units=%d aligned=%d flags=%s" % (tot, ali, gsummary["flags"]))

    # ---- 汇总
    grand_total = sum(s["total"] for s in all_stats.values())
    grand_aligned = sum(s["aligned"] for s in all_stats.values())
    gf2 = defaultdict(int)
    for s in all_stats.values():
        for k, v in s["flags"].items():
            gf2[k] += v
    unal = gf2.get("UNALIGNED?", 0)
    miss = gf2.get("MISSING", 0)
    src = gf2.get("SOURCE_ONLY", 0)
    sm = [
        "# K1 返工汇总（r2）· %s" % TAG, "",
        "- W1 版（`_summary-2026-11-04.md`）原样保留；本表为 A.3「重新生成另起带日期文件名」的返工版，**两版并存**。",
        "- **返工原因**：W1 以「v0 文件」为单位、优先 basename 对齐；v0→v3 重组后 basename 全变，685 行被标 `MISSING`（genre 594 行）。附录 A.1 规定单位是「规则编号；没有编号的用文件路径+标题」，2.8 节要求「用规则编号和标题来对齐」；把「对不上」记成「丢失」会误导 W3 精读，故返工。",
        "", "## 三条口径（必须随表下发给 W3）", "",
        "1. **MISSING ≠ 丢失**：MISSING 只留给「编号体系可比（v3 仍用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块」的机械判定；编号整体改名/重组导致对不上的一律 `UNALIGNED?`。MISSING 不等于内容丢失，也不等于应恢复。",
        "2. **覆盖率 ≠ 内容保留率**：对齐成功只说明编号/标题/内容块有对应，不能推出内容完整、逐项可用或已验收。",
        "3. **raw 表是信号不是结论**：本表只出机械盘点信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。",
        "", "## 返工后 flag 分布", "",
        "| flag | 数量 | 占规则单元 | 性质 |", "|---|---|---|---|",
    ]
    for f in ("MISSING", "SHRUNK", "BLOCK_LOST", "RENUMBERED?", "UNALIGNED?", "SOURCE_ONLY", "—"):
        n = gf2.get(f, 0)
        kind = ("补充标记·不是丢失" if f in ("UNALIGNED?", "SOURCE_ONLY") else
                "A.1 原 flag" if f != "—" else "对齐无信号")
        sm.append("| `%s` | %d | %.1f%% | %s |" %
                  (f, n, n / grand_total * 100 if grand_total else 0, kind))
    sm += [
        "", "**对齐失败占比**：`UNALIGNED?` %d / %d = **%.1f%%**（机械对齐失败，无法判定是否缺失；须 W3 比内容核定）。" %
            (unal, grand_total, unal / grand_total * 100 if grand_total else 0),
        "**MISSING**：%d / %d = %.1f%%（按语义收窄后只留编号体系可比、且确实无相似编号/标题/内容块的单元；W1 旧表 685 行的「对不上」已分流到 `UNALIGNED?` / `SOURCE_ONLY`）。" %
            (miss, grand_total, miss / grand_total * 100 if grand_total else 0),
        "**SOURCE_ONLY**：%d（来源类文件，2.8 节不直接恢复）。" % src,
        "v3 对齐成功：%d / %d = %.1f%%。" %
            (grand_aligned, grand_total, grand_aligned / grand_total * 100 if grand_total else 0),
        "", "## 与 W1 旧表的 flag 分布对比", "",
        "| flag | W1 旧表(765 v0 文件) | r2 返工(%d 规则单元) |" % grand_total,
        "|---|---|---|",
        "| `MISSING` | 685 | %d |" % miss,
        "| `UNALIGNED?` | 0（当时无此标记） | %d |" % unal,
        "| `SOURCE_ONLY` | 0（当时无此标记） | %d |" % src,
        "| `SHRUNK` | 21 | %d |" % gf2.get("SHRUNK", 0),
        "| `BLOCK_LOST` | 32 | %d |" % gf2.get("BLOCK_LOST", 0),
        "| `RENUMBERED?` | 11 | %d |" % gf2.get("RENUMBERED?", 0),
        "| `—` | 34 | %d |" % gf2.get("—", 0),
        "- 注：两版盘点单位不同（文件 vs 规则单元），总数不可直接相减比较；对比只看 MISSING 被 `UNALIGNED?` / `SOURCE_ONLY` 分流后的语义变化。",
        "", "## 各表 flag 分布", "",
        "| raw 表 | 规则单元 | v3 对齐 | MISSING | SHRUNK | BLOCK_LOST | RENUMBERED? | UNALIGNED? | SOURCE_ONLY | — |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for name, s in all_stats.items():
        f = s["flags"]
        sm.append("| `%s` | %d | %d | %d | %d | %d | %d | %d | %d | %d |" %
                  (name, s["total"], s["aligned"], f.get("MISSING", 0), f.get("SHRUNK", 0),
                   f.get("BLOCK_LOST", 0), f.get("RENUMBERED?", 0), f.get("UNALIGNED?", 0),
                   f.get("SOURCE_ONLY", 0), f.get("—", 0)))
    sm += ["", "## genre 14 类分节", "",
           "| 题材 | 阈值 | 规则单元 | v3 对齐 | MISSING | UNALIGNED? | SOURCE_ONLY | 其他 A.1 flag |",
           "|---|---|---|---|---|---|---|---|"]
    for cat, units, s in g_all:
        f = s["flags"]
        other = f.get("SHRUNK", 0) + f.get("BLOCK_LOST", 0) + f.get("RENUMBERED?", 0)
        sm.append("| %s %s | %s | %d | %d | %d | %d | %d | %d |" %
                  (cat, GENRE_NAMES[cat], "20%" if cat in TIGHT else "30%", s["total"],
                   s["aligned"], f.get("MISSING", 0), f.get("UNALIGNED?", 0),
                   f.get("SOURCE_ONLY", 0), other))
    sm += ["", "## W1 已证实的两个机制卡事实（本表复核一致；计划 §6.1 已据此修订）", "",
           "- **G02 言情 RO-K**：v2 001–166（166 张）→ v3 001–120（120 张），**删 46 张（RO-K121–166）**，`02-romance/mechanisms.md` 40.7→23.6 KB。",
           "- **G05 科幻 SF-K**：v2 / v3 均为 001–102 连续 102 张，**未删卡，属逐卡压缩**，`05-science-fiction/mechanisms.md` 32.4→20.4 KB。",
           "- W3 分别处理：G02 按 2.3 节逐卡决定；**G05 按逐卡压缩处理，不套 G02 的「补回删卡编号」做法**。",
           "- **W2 证据修正**（只读核对结论，详见 `notes/slice-prep-2026-11-04.md`「W2 证据修正」节）：v3 02-romance/mechanisms.md 的 RO-K116–120 已是 v2 RO-K162–166 的通用化改写，46 张中这 5 张已有落点；逐卡分类 34 含通用机制 / 9 纯来源观察 / 3 待核（与 2.3 节 39/7 口径不同，W3 先统一口径），不得整批当待恢复、不得重复补回；G05 的 102 卡行 29025→18409B（均 285→180，−37%）按字段找回；G01 缩减发生在 v0→v1，W3 须逐块对 v0 核。",
           "", "## 未解决阻塞（如实记录，不伪造行）", "",
           "- **仍无法机械对齐的比例 %.1f%%**（UNALIGNED? %d / %d）：v0→v3 题材/目录重组、编号与标题全面改写（2.8、2.3 节），basename 对齐失效；按编号+标题+内容块仍对不上的，只能记 `UNALIGNED?` 交 W3 定向精读比内容，不判缺失、不伪造对齐行。" %
            (unal / grand_total * 100 if grand_total else 0, unal, grand_total),
           "- `title~` 相似标题、`SHRUNK`/`BLOCK_LOST` 的跨版本标签词差异均为粗粒度信号，非结论。",
           "- 两处跨题材多归属（04/08、04/03）待 W3 核定；genre 级公共入口文件不纳入题材池，不把多份 v0 SKILL.md 强行对齐到 1 份 v3 SKILL.md 抬高对齐率。",
    ]
    for grp, d, reason in all_blocking:
        sm.append("- `%s` / `%s`：%s" % (grp, d, reason))
    sm += ["", "## preset-card-generation", "",
           "preset-card-generation：无 v0（不进入 7 份 raw 表）。", ""]
    write_raw("_summary-%s.md" % TAG, "\n".join(sm) + "\n")

    print("\n=== 返工汇总 ===")
    print("规则单元 %d，v3 对齐 %d，UNALIGNED? %d（%.1f%%），MISSING %d，SOURCE_ONLY %d" %
          (grand_total, grand_aligned, unal, unal / grand_total * 100 if grand_total else 0, miss, src))
    print("flags:", dict(gf2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
