#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""K1 机械盘点：只读脚本，用 `git show <提交>:<路径>` 读 v0/v1/v2/v3。

不检出、不改仓库、不复制原件、不放作品全文。
产出 7 份 raw 表（附录 A.1 字段）+ 1 份汇总，文件名带日期，只追加不覆盖。
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict

REPO = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology"
OUT = os.path.join(REPO, "distillation/rounds/round-01-2026-11-04/notes/loss-inventory/raw")
DATE = "2026-11-04"
COMMITS = OrderedDict([("v0", "d23c461"), ("v1", "d2003e4"),
                       ("v2", "3c1cb5f"), ("v3", "2a10c07")])

# ---------------------------------------------------------------- 谱系映射
# 第 5 节表；v0 目录名已用 git ls-tree 核实全部存在。
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
# 收紧到 20% 的三类（第 5.1 节、附录 A.1）
TIGHT = {"01", "07", "10"}
# 跨题材多归属（第 5 节注明「部分进」），机械对齐只记主归属 + 阻塞说明
MULTI_ATTR = {
    "fantasy-adventure-structure-lab": ("04", "08"),
    "supernatural-power-craft": ("04", "03"),
}

# 编号改号对照（2.3 节）
PREFIX_REMAP = {"AC": "A", "SV": "SD", "PD": "PS", "PT": "PV",
                "IDP": "IR", "COM": "CO", "RM": "RL", "RD": "RL"}

# v1 的 line-editing 目录名不同
V1_ALIAS = {"line-editing-and-proofreading": "english-prose-line-editing"}

# ---------------------------------------------------------------- blocks
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

HEAD_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*$")
NORM_STRIP = re.compile(r"[\s\*`_：:，,。、；;（）()「」『』《》【】\[\]！!？?·…\-—/\\]")


def norm(s: str) -> str:
    return NORM_STRIP.sub("", s).lower()


def parse(text: str):
    """返回 (id 集合, 标题集合, blocks 集合)。纯机械，不精读。"""
    ids, titles, blocks = set(), set(), set()
    for line in text.splitlines():
        stripped = line.strip()
        # blocks：只认标签行（**加粗** / 标题 / 列表项）的前段关键词
        if stripped.startswith("**") or re.match(r"^#{2,4}\s", stripped) or re.match(r"^[-*]\s", stripped):
            head = stripped[:32]
            for cls, kws in BLOCK_KEYS.items():
                if any(k in head for k in kws):
                    blocks.add(cls)
        m = HEAD_RE.match(line)
        if not m:
            continue
        body = m.group(2).strip()
        toks = body.split()
        if not toks:
            continue
        first = toks[0].strip("*`")
        if ID_RE.match(first) and len(first) <= 14 and (any(c.isdigit() for c in first) or "-" in first or "–" in first):
            ids.add(first.upper())
            rest = body[len(toks[0]):].strip(" :：-–*")
            if rest:
                titles.add(norm(rest))
    return ids, titles, blocks


def remapped(ids):
    out = set()
    for i in ids:
        out.add(i)
        base = i.split("-")[0]
        if base in PREFIX_REMAP:
            out.add(PREFIX_REMAP[base] + i[len(base):])
    return out


def id_summary(ids):
    if not ids:
        return "无编号"
    ids = sorted(ids)
    if len(ids) <= 6:
        return ",".join(ids)
    return "%s… 共%d" % (",".join(ids[:2]), len(ids))


# ---------------------------------------------------------------- git 只读
def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True).stdout


def collect():
    """每个版本 -> {path: {size, sha}}；内容按 blob SHA 去重只读一次。"""
    trees = {}
    blob_repr = {}
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


def info(trees, contents, ver, path):
    d = trees[ver].get(path)
    if not d:
        return None
    return {"size": d["size"], "text": contents.get(d["sha"], "")}


def precompute(trees, contents):
    """每个版本每个文件预解析 (ids, titles, blocks, size)。"""
    parsed = {}
    for ver, files in trees.items():
        parsed[ver] = {}
        for path, d in files.items():
            ids, titles, blocks = parse(contents.get(d["sha"], ""))
            parsed[ver][path] = {"ids": ids, "titles": titles, "blocks": blocks,
                                 "size": d["size"], "bn": os.path.basename(path)}
    return parsed


def pool(trees, parsed, ver, group, cat=None):
    """候选文件池：该版本目标 skill 目录（genre 限 NN- 题材目录）。"""
    if group == "genre-fiction-craft":
        pref = "skills/genre-fiction-craft/references/%s-" % cat
    else:
        d = V1_ALIAS.get(group, group) if ver == "v1" else group
        pref = "skills/%s/" % d
    return [(p, m) for p, m in parsed[ver].items() if p.startswith(pref)]


def align(v0meta, candidates):
    """返回 (matched_path, meta, method)。优先级：basename > 标题 > 改号前缀 > 原编号。"""
    bn = v0meta["bn"]
    for p, m in candidates:
        if m["bn"] == bn:
            return p, m, "basename"
    t0, i0 = v0meta["titles"], remapped(v0meta["ids"])
    for p, m in candidates:
        if t0 & m["titles"]:
            return p, m, "title"
        # 「相似标题」：长度≥8 的互相包含，仅作机械信号
        for a in t0:
            if len(a) < 8:
                continue
            if any((a in b or b in a) and len(b) >= 8 for b in m["titles"]):
                return p, m, "title~"
    for p, m in candidates:
        if i0 & m["ids"]:
            return p, m, "prefix"
    for p, m in candidates:
        if v0meta["ids"] & m["ids"]:
            return p, m, "id"
    return None, None, None


def shrink_flag(row, cat):
    """任一更早版本(v0/v1/v2) → v3 缩减超阈值即打 SHRUNK（覆盖 2.3 节的 v2→v3 删除）。"""
    v3 = row["v3size"]
    if v3 is None or v3 <= 0:
        return False
    thr = 0.20 if cat in TIGHT else 0.30
    for v in ("v0", "v1", "v2"):
        s = row.get(v + "size")
        if s is None or s <= 0 or s <= v3:
            continue
        if (s - v3) / s > thr or (s - v3) > 1536:
            return True
    return False


def build_rows(group, cat, v0dirs, trees, parsed):
    rows, blocking = [], []
    for d in v0dirs:
        pref = "skills/%s/" % d
        units = [(p, m) for p, m in parsed["v0"].items() if p.startswith(pref)]
        if not units:
            blocking.append((d, "该 v0 目录在 v0 树中无文件（路径核对失败）"))
            continue
        for p, m in units:
            rel = p[len("skills/"):]
            row = {"unit": "%s [%s]" % (rel, id_summary(m["ids"])),
                   "v0size": m["size"], "matches": {}, "methods": {}, "blocks0": m["blocks"]}
            for ver in ("v1", "v2", "v3"):
                mp, mm, method = align(m, pool(trees, parsed, ver, group, cat))
                row["matches"][ver] = mp
                row["methods"][ver] = method
                row[ver + "size"] = mm["size"] if mm else None
                row[ver + "blocks"] = mm["blocks"] if mm else set()
            rows.append(row)
    return rows, blocking


def flags_for(row, cat):
    v3 = row["matches"]["v3"]
    if v3 is None:
        return ["MISSING"]
    out = []
    if shrink_flag(row, cat):
        out.append("SHRUNK")
    method = row["methods"]["v3"]
    if method in ("title", "title~", "prefix"):
        out.append("RENUMBERED?")
    if method == "basename" and row["blocks0"] and (row["blocks0"] - row["v3blocks"]):
        out.append("BLOCK_LOST")
    return out if out else ["—"]


def versions_str(row):
    return "1 " + " ".join("1" if row["matches"][v] else "0" for v in ("v1", "v2", "v3"))


def bytes_str(row):
    def f(v):
        s = row.get(v + "size")
        return str(s) if s is not None else "—"
    return "%d / %s / %s / %s" % (row["v0size"], f("v1"), f("v2"), f("v3"))


def blocks_str(row):
    b = row["blocks0"]
    short = {"规则": "规", "怎么做": "怎", "例外": "例", "反例": "反",
             "检查": "检", "适用": "适", "失败": "败"}
    return "".join(short[x] for x in BLOCK_ORDER if x in b) or "∅"


def render_table(rows, cat):
    out = ["| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |",
           "|---|---|---|---|---|"]
    for r in rows:
        out.append("| `%s` | `%s` | `%s` | `%s` | `%s` |" % (
            r["unit"], versions_str(r), blocks_str(r), bytes_str(r), ";".join(flags_for(r, cat))))
    return "\n".join(out)


def stats(rows, cat):
    total = len(rows)
    aligned = sum(1 for r in rows if r["matches"]["v3"])
    c = defaultdict(int)
    for r in rows:
        for f in flags_for(r, cat):
            c[f] += 1
    present = {v: sum(1 for r in rows if r["matches"][v]) for v in ("v1", "v2", "v3")}
    return {"total": total, "aligned": aligned,
            "coverage": (aligned / total * 100) if total else 0.0,
            "flags": dict(c), "present": present}


def header(group, cat, v0dirs, st):
    thr = "20%" if cat in TIGHT else "30%"
    lines = [
        "# K1 机械盘点 raw 表 · %s%s" % (group, (" / 题材 %s %s" % (cat, GENRE_NAMES[cat])) if cat else ""),
        "",
        "- 生成日期：%s（只追加不覆盖；重生成另起带日期文件）" % DATE,
        "- 数据来源：`git show <提交>:<路径>`，提交 %s；不检出、不改仓库、不复制原件、不放作品全文。" %
            "、".join("%s=%s" % (k, v) for k, v in COMMITS.items()),
        "- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。",
        "- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **%s** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；%s" %
            (thr, "本题材按第 5.1 节收紧到 20%。" if cat in TIGHT else "默认 30%。"),
        "- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。",
        "- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。",
        "- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。",
        "- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。",
        "- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。",
        "- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。",
        "- 谱系 v0 来源：%s" % "、".join("`%s`" % d for d in v0dirs),
        "",
        "**覆盖率**：已对齐 %d / v0 文件 %d = **%.1f%%**（v1/v2/v3 各版本有对应：%d / %d / %d）" %
            (st["aligned"], st["total"], st["coverage"],
             st["present"]["v1"], st["present"]["v2"], st["present"]["v3"]),
        "",
        "**flag 计数**：%s" % "；".join("%s=%d" % (k, v) for k, v in sorted(st["flags"].items())),
        "",
    ]
    return "\n".join(lines)


def write_raw(fname, text):
    path = os.path.join(OUT, fname)
    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n\n---\n\n## 重新生成 %s\n\n" % DATE)
        f.write(text)
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    trees, contents = collect()
    parsed = precompute(trees, contents)
    print("各版本文件数：", {v: len(t) for v, t in trees.items()})
    print("唯一 blob 数：", len(contents))

    all_stats = OrderedDict()
    all_blocking = []

    # 6 个非 genre
    for group, v0dirs in LINEAGE.items():
        rows, blocking = build_rows(group, None, v0dirs, trees, parsed)
        st = stats(rows, None)
        all_stats[group] = st
        text = header(group, None, v0dirs, st) + "\n" + render_table(rows, None) + "\n"
        for d, reason in blocking:
            text += "\n- 机械对齐阻塞：`%s` — %s\n" % (d, reason)
        text += "\n## 机械对齐阻塞与如实记录\n\n"
        text += "- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。\n"
        text += "- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。\n"
        text += "- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。\n"
        write_raw("%s-%s.md" % (group, DATE), text)
        for d, reason in blocking:
            all_blocking.append((group, d, reason))
        print("[%s] total=%d aligned=%d cov=%.1f%% flags=%s" %
              (group, st["total"], st["aligned"], st["coverage"], st["flags"]))

    # genre：一份 raw 表，按 14 类题材分节
    gtext = [
        "# K1 机械盘点 raw 表 · genre-fiction-craft（按 14 类题材分组）",
        "",
        "- 生成日期：%s（只追加不覆盖；重生成另起带日期文件）" % DATE,
        "- 数据来源：`git show <提交>:<路径>`，提交 %s；不检出、不改仓库、不复制原件、不放作品全文。" %
            "、".join("%s=%s" % (k, v) for k, v in COMMITS.items()),
        "- 按 D4-A：14 类全部机械盘点；**热门三类 04 武侠仙侠玄幻 / 02 言情 / 05 科幻** 与 v0 全文对照由 W2 起定向精读执行，本表只出机械盘点信号。",
        "- 阈值：默认缩减 >30% 或 >1.5 KB；**01 推理 / 07 求生灾变 / 10 职业竞技收紧到 20%**（第 5.1 节、附录 A.1）。",
        "- v1 题材目录为中文名、v2/v3 为英文名，均按 `NN-` 数字前缀定位对应题材目录。",
        "- 字段与 flag 含义见各分节表头；`blocks` 简写：规/怎/例/反/检/适/败/∅。",
        "- 编号改号对照：`IDP→IR`、`COM→CO`、`RM/RD→RL` 等按 2.3 节，用「新旧前缀 + 标题」对齐。",
        "",
    ]
    g_all = []
    for cat, v0dirs in GENRE.items():
        rows, blocking = build_rows("genre-fiction-craft", cat, v0dirs, trees, parsed)
        st = stats(rows, cat)
        g_all.append((cat, rows, st))
        gtext.append("---\n")
        gtext.append("## 题材 %s %s（阈值 %s）\n" % (cat, GENRE_NAMES[cat], "20%" if cat in TIGHT else "30%"))
        gtext.append(header("genre-fiction-craft", cat, v0dirs, st))
        gtext.append(render_table(rows, cat) + "\n")
        for d, reason in blocking:
            gtext.append("- 机械对齐阻塞：`%s` — %s\n" % (d, reason))
            all_blocking.append(("genre/%s" % cat, d, reason))
    # genre 汇总
    tot = sum(s["total"] for _, _, s in g_all)
    ali = sum(s["aligned"] for _, _, s in g_all)
    gf = defaultdict(int)
    for cat, rows, s in g_all:
        for r in rows:
            for f in flags_for(r, cat):
                gf[f] += 1
    gsummary = {"total": tot, "aligned": ali,
                "coverage": ali / tot * 100 if tot else 0.0, "flags": dict(gf)}
    all_stats["genre-fiction-craft"] = gsummary
    gtext.insert(0, "**genre 全表覆盖率**：已对齐 %d / %d = **%.1f%%**；flag 计数：%s\n" %
                 (ali, tot, gsummary["coverage"],
                  "；".join("%s=%d" % (k, v) for k, v in sorted(gf.items()))))
    gtext.append("\n---\n\n## genre 机械对齐阻塞（如实记录）\n\n")
    gtext.append("- **genre 覆盖率偏低是机械对齐的真实结果，不是跳过**：v0 题材文件名为「编号 + 描述」（如 `01-information-and-clues.md`），v3 重组为英文名（如 `fairness-and-format.md`），basename 几乎不重叠；v0 规则编号（`R1`、`CM-xx` 等）与标题在 v3 改为题材前缀编号（如 `MY-xx`）且标题重写，按「新旧前缀 + 标题」也难以对齐。依据第 2.8 节「v1→v2 题材目录改英文名，文件也重组了，没有办法按文件名对齐」与第 2.3 节，机械盘点只能出这些信号；逐条用规则编号和标题对齐是 W2 定向精读的任务。\n")
    gtext.append("- 已对齐的多为跨版本保留同名的 `examples.md` / 机制卡类文件；`MISSING` 行逐条列出，不伪造行、不跳过。\n")
    gtext.append("- `fantasy-adventure-structure-lab`（第 5 节注「部分进 08」）、`supernatural-power-craft`（「部分进 03」）为**跨题材多归属**：机械盘点按主归属 04 登记，不强行拆成两份对齐；08/03 的归属待 W2 定向精读核定。\n")
    gtext.append("- v1→v2 题材目录由中文名改英文名，按 `NN-` 数字前缀定位对应题材目录；genre 级公共入口文件不纳入题材池，不把 59 份 v0 SKILL.md 强行对齐到 1 份 v3 SKILL.md 来抬高覆盖率。\n")
    gtext.append("- **编号内嵌标题的解析限制**：v3 机制卡编号写在标题括号内（如 `# 关系机制卡（RO-K001–RO-K120）`），不是标准 `## 编号 标题` 形式，机械解析提不出这类 ID；2.3 节的 `RO-K121–166`（v2→v3 删除）、`05-science-fiction/mechanisms.md` 32.4→20.4 KB 等，须 W2 定向精读逐卡/逐文件核定，本表不据此伪造对齐行。\n")
    write_raw("genre-fiction-craft-%s.md" % DATE, "\n".join(gtext))
    print("[genre-fiction-craft] total=%d aligned=%d cov=%.1f%% flags=%s" %
          (tot, ali, gsummary["coverage"], gsummary["flags"]))

    # ---- 汇总文件（含 preset-card「无 v0」单列）
    grand_total = sum(s["total"] for s in all_stats.values())
    grand_aligned = sum(s["aligned"] for s in all_stats.values())
    gf2 = defaultdict(int)
    for s in all_stats.values():
        for k, v in s["flags"].items():
            gf2[k] += v
    sm = ["# K1 机械盘点汇总 · %s" % DATE, "",
          "- 7 份 raw 表（6 个非 genre skill + 1 份 genre 按 14 类分组）；只出表，不精读、不做逐条决定。",
          "- 覆盖率定义：已对齐的 v0 文件数 / 该组 v0 文件总数。",
          "", "## 各表覆盖率与 flag 统计", "",
          "| raw 表 | v0 文件数 | 已对齐 | 覆盖率 | MISSING | SHRUNK | BLOCK_LOST | RENUMBERED? | — |",
          "|---|---|---|---|---|---|---|---|---|"]
    for name, s in all_stats.items():
        f = s["flags"]
        sm.append("| `%s` | %d | %d | %.1f%% | %d | %d | %d | %d | %d |" %
                  (name, s["total"], s["aligned"], s["coverage"],
                   f.get("MISSING", 0), f.get("SHRUNK", 0), f.get("BLOCK_LOST", 0),
                   f.get("RENUMBERED?", 0), f.get("—", 0)))
    sm.append("| **合计** | %d | %d | %.1f%% | %d | %d | %d | %d | %d |" %
              (grand_total, grand_aligned,
               grand_aligned / grand_total * 100 if grand_total else 0,
               gf2.get("MISSING", 0), gf2.get("SHRUNK", 0), gf2.get("BLOCK_LOST", 0),
               gf2.get("RENUMBERED?", 0), gf2.get("—", 0)))
    sm += ["", "## genre 14 类分节覆盖率", "",
           "| 题材 | 阈值 | v0 文件数 | 已对齐 | 覆盖率 | MISSING | SHRUNK | BLOCK_LOST | RENUMBERED? |",
           "|---|---|---|---|---|---|---|---|---|"]
    for cat, rows, s in g_all:
        f = s["flags"]
        sm.append("| %s %s | %s | %d | %d | %.1f%% | %d | %d | %d | %d |" %
                  (cat, GENRE_NAMES[cat], "20%" if cat in TIGHT else "30%",
                   s["total"], s["aligned"], s["coverage"],
                   f.get("MISSING", 0), f.get("SHRUNK", 0), f.get("BLOCK_LOST", 0),
                   f.get("RENUMBERED?", 0)))
    sm += ["", "## 未解决阻塞（如实记录，不伪造、不跳过）", ""]
    sm.append("- 版本重组（v0 74 个独立 skill → v3 7 个合并 skill）后，v0 文件内容常合并/拆分到多个 v3 文件；机械盘点只能出「有无对应 + 缩减信号」，**覆盖率不是内容保留率**，逐条决定待 W2 定向精读。")
    sm.append("- **genre 覆盖率 2.6% 为机械对齐上限**：v0 题材文件名/规则编号/标题在 v3 全面重组改写（第 2.8、2.3 节），basename 与标题均难对齐；未对齐项逐行记 `MISSING`，须 W2 定向精读按规则编号与标题逐条核定，不伪造行。")
    sm.append("- **编号内嵌标题**：v3 机制卡编号写在标题括号内（如 `# 关系机制卡（RO-K001–RO-K120）`），机械解析提不出；2.3 节的 RO-K121–166（v2→v3 删除）、科幻 mechanisms.md 缩减等须 W2 定向精读逐卡核定，本表不据此伪造对齐行。")
    sm.append("- `title~` 粗粒度相似标题、`SHRUNK`/`BLOCK_LOST` 跨版本标签词不同带来的噪声，均为信号非结论。")
    for grp, d, reason in all_blocking:
        sm.append("- `%s` / `%s`：%s" % (grp, d, reason))
    sm += ["", "## preset-card-generation", "",
           "preset-card-generation：无 v0（不进入 7 份 raw 表）。", ""]
    write_raw("_summary-%s.md" % DATE, "\n".join(sm) + "\n")

    print("\n=== 汇总 ===")
    print("总 v0 文件数 %d，已对齐 %d，覆盖率 %.1f%%" %
          (grand_total, grand_aligned, grand_aligned / grand_total * 100 if grand_total else 0))
    print("flag 合计：", dict(gf2))
    print("输出目录：", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
