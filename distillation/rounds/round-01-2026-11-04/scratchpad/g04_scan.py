#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""附录 B 十一类扫描（B.1 原文正则，逐类打印命中数与命中行）。含注入型正控制。"""
import re, os, sys, glob

DIRS = {
    "04": "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04/output/genre-fiction-craft/references/04-wuxia-xianxia-fantasy",
}
PATS = [
    ("#1 书名号", [r"《[^》]+》"]),
    ("#2 来源编号残片", [r"PG[ -]?[0-9]+", r"(^|[^A-Za-z0-9])-[0-9]{3,5}([^0-9]|$)"]),
    ("#3 来源数量与年代", [r"[0-9]+ ?本(材料|书|手册)", r"材料标称",
        r"(1[5-9]|20)[0-9]{2} ?年(代)?.{0,8}(市场|手册|杂志|出版|建议)"]),
    ("#4 指向学习材料", [r"书内|书里|同书|该书|此书|原书|来源是|出自|引自|据称|这批材料|学习材料|原文库|批次"]),
    ("#5 作者与名人", [r"作家|小说家|评论家|大师|名著|经典作品", r"[A-Z][a-z]+ [A-Z][a-z]+"]),
    ("#6 英文原句", [r'"[A-Z][a-z]+( [a-z]+){4,}']),
    ("#7 包外路径", [r"notes/|results/|/home/|materials/|rounds/"]),
    ("#8 改动痕迹", [r"旧版|本版|更正|早先的版本|融合版|上一版"]),
    ("#9 审计词", [r"NOT_PROVEN|VERIFIED|NOT_RUN|STATIC_CHECKED|DESIGN_EXAMPLE|OBSERVED|F/H/P|GQ[1-5]|R1[78]"]),
    ("#10 删除残迹", [r"（\s*）", r"\(\s*\)", r"见\s*[，。；]", r"据\s*[，。；]", r"与\s*同"]),
    ("#11 禁用说法", [r"夯|拉完了|硬规则|用户明确要求"]),
]

def scan(files, tag):
    texts = {f: open(f, encoding="utf-8").read().split("\n") for f in files}
    total = 0
    print("\n===== %s (%d 文件) =====" % (tag, len(files)))
    for name, pats in PATS:
        hits = []
        for p in pats:
            rx = re.compile(p)
            for f, lines in texts.items():
                for i, ln in enumerate(lines, 1):
                    for m in rx.finditer(ln):
                        hits.append("%s:%d [%s] %s" % (os.path.basename(f), i, p[:14], m.group(0)[:26]))
        total += len(hits)
        print("%-18s 命中 %3d" % (name, len(hits)))
        for h in hits[:6]:
            print("      " + h)
        if len(hits) > 6:
            print("      …另 %d 条" % (len(hits) - 6))
    print("---- %s 合计命中 %d ----" % (tag, total))
    return total

CTL = "/tmp/g04scan_ctl"
os.makedirs(CTL, exist_ok=True)
open(CTL + "/control.md", "w", encoding="utf-8").write(
    "《某书》里 PG123 提到 1920 年代的杂志市场；这批材料出自原书，硬规则；NOT_PROVEN；（）；见，\n")
ctl = scan([CTL + "/control.md"], "正控制（必须非零）")
real = scan(sorted(glob.glob(DIRS["04"] + "/*.md")), "04 目录盘上现状（补丁后）")
print("\n[判定] 正控制命中 %d（>0 才有效）；04 目录命中 %d" % (ctl, real))
