#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 delivery-preflight-spec：逐模板文件取「首列独立行的编号全集」，
并列出该 skill 包内出现但未成模板独立行的编号（缺口候选）。
两种取词法并列跑（裸 AD-01 与 `AD-01` 反引号式），并打印差额。"""
import os, re, glob, json, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/spec-out"
os.makedirs(OUT, exist_ok=True)
ROOT = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
PKGS = ["story-architecture-and-longform-planning", "character-and-narrative-control",
        "fiction-planning-and-diagnosis", "scene-conflict-and-rhythm",
        "cross-media-drama-adaptation", "line-editing-and-proofreading",
        "preset-card-generation", "genre-fiction-craft"]

ID = re.compile(r"\b([A-Z]{2,3})-([0-9]{1,3})\b")
ROW = re.compile(r"^\|\s*`?([A-Z]{2,3}-[0-9]{1,3})`?\s*(?:\||：|:)")
HEAD = re.compile(r"^#{2,6}\s*.*?\b([A-Z]{2,3}-[0-9]{1,3})\b")

spec = {"version": 1, "templates": []}
matrix = []

for pkg in PKGS:
    d = os.path.join(ROOT, "output", pkg)
    if not os.path.isdir(d):
        continue
    tpl_files = sorted(glob.glob(os.path.join(d, "templates", "*.md")))
    if pkg == "genre-fiction-craft":
        tpl_files = sorted(glob.glob(os.path.join(d, "references", "*", "templates*.md")))
    # 包内全部 ID（任意形态）
    allids = set()
    for f in glob.glob(os.path.join(d, "**", "*.md"), recursive=True):
        for m in ID.finditer(open(f, encoding="utf-8").read()):
            allids.add(m.group(0))
    fams = {}
    for i in allids:
        fams.setdefault(i.split("-")[0], set()).add(i)
    matrix.append("\n## %s" % pkg)
    matrix.append("- 包内编号唯一集（任意形态）=%d，族分布：%s" % (
        len(allids), ", ".join("%s:%d" % (k, len(v)) for k, v in sorted(fams.items()))))
    if not tpl_files:
        matrix.append("- **无 `templates/*.md`**：按 R18 §6 不建 spec 条目；若编号需在交付时逐项可填，另立项补模板。")
        continue
    for f in tpl_files:
        txt = open(f, encoding="utf-8").read()
        rows = [m.group(1) for ln in txt.split("\n") for m in [ROW.match(ln)] if m]
        heads = [m.group(1) for ln in txt.split("\n") for m in [HEAD.match(ln)] if m]
        uniq = sorted(set(rows), key=lambda x: (x.split("-")[0], int(x.split("-")[1])))
        matrix.append("- 模板 `%s`：首列独立行 %d 个（标题式 %d 个）%s" % (
            os.path.relpath(f, d), len(set(rows)), len(set(heads)),
            "；样例 " + ",".join(uniq[:6]) if uniq else ""))
        if uniq:
            spec["templates"].append({"path": "output/%s/%s" % (pkg, os.path.relpath(f, d)),
                                      "format": "markdown-table",
                                      "field_ids": uniq})
    # 缺口候选：包内出现但没有任何 templates 首列行的族
    covered = set()
    for t in spec["templates"]:
        if t["path"].startswith("output/%s/" % pkg):
            covered |= set(t["field_ids"])
    gap = {}
    for i in sorted(allids - covered):
        gap.setdefault(i.split("-")[0], []).append(i)
    matrix.append("- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：%s" % (
        "；".join("%s 缺 %d 个（%s…）" % (k, len(v), v[0]) for k, v in sorted(gap.items())) if gap else "无"))

open(os.path.join(OUT, "field-id-matrix.md"), "w", encoding="utf-8").write(
    "# delivery-preflight-spec 取数矩阵（主代理机械实测，2026-11-05）\n\n性质：**spec 的取数准备，不是已冻结的 spec**。R18 §6 要求 `field_ids` 必须来自已确认真实需求并已冻结的唯一 ID；本表只回答「哪些编号已经在模板里独占一行、哪些没有」，不判定哪些需求要求逐项可填。判定归 W4 由非作者按 requirements 做。\n"
    "\n取词两法并列：首列独立行 `^\\|\\s*`?ID`?\\s*\\|`，标题式 `^#{2,6} …ID`。两者计数都打印，不以单档下结论。\n"
    + "\n".join(matrix) + "\n")
json.dump(spec, open(os.path.join(OUT, "delivery-preflight-spec.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("templates 条目:", len(spec["templates"]), "| 全部 field_ids 合计:",
      sum(len(t["field_ids"]) for t in spec["templates"]))
print("输出:", OUT)
