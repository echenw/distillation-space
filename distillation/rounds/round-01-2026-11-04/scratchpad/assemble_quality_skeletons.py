#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""W3 第 1 批：为 8 个 skill 装配 notes/quality/<skill>/{brief.json,review.json} 骨架。

用例逐字取自 notes/suite-contract.md 第六节（附录 E 装配，全部自创）。
骨架不编造任何 SHA / 树摘要 / 通过结论；GQ1–GQ4 待填，GQ5 NOT_PROVEN。
若目标文件已存在则跳过（只追加不覆盖，不改动 W2 已有的 quality 文件）。
"""
from __future__ import annotations

import json
import os

R = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
Q = os.path.join(R, "notes/quality")
DATE = "2026-11-04"

# 附录 E 用例（notes/suite-contract.md 第六节），id / kind / scenario / expected 原样
CASES = {
    "line-editing-and-proofreading": [
        {"id": "LE-T1", "kind": "positive", "scenario": "一段约 800 字的中文小说正文，要求精修句子和标点，保留口吻", "expected": "先定第 0 轮的三件事，再按层次改，交付改后文本和逐条说明"},
        {"id": "LE-T2", "kind": "missing", "scenario": "只有一句「帮我润色」，不说用途、体例和读者", "expected": "先问；用户不答时按最小改动处理，并列出所做的假设"},
        {"id": "LE-T3", "kind": "conflict", "scenario": "要求「每句都更有力」，同时要求保留方言口语和意识流段落", "expected": "先判负触发：口语和意识流段不改，冲突列给作者选"},
        {"id": "LE-T4", "kind": "boundary", "scenario": "英文对白稿，只要拼写和标点校对", "expected": "只做机械层，不碰风格"},
    ],
    "cross-media-drama-adaptation": [
        {"id": "CM-T1", "kind": "positive", "scenario": "3 万字中篇改编成 90 分钟舞台剧", "expected": "给改编合同、分场表和信息载体方案"},
        {"id": "CM-T2", "kind": "missing", "scenario": "只有梗概，没有原作文本", "expected": "只出方案草稿，依赖原文的部分标明「未能核实」"},
        {"id": "CM-T3", "kind": "conflict", "scenario": "要保留全部内心独白，又不许用旁白", "expected": "列出冲突和替代载体，由作者选"},
        {"id": "CM-T4", "kind": "boundary", "scenario": "改成多结局的互动音频", "expected": "走互动改编分支，交付分支表"},
    ],
    "scene-conflict-and-rhythm": [
        {"id": "SC-T1", "kind": "positive", "scenario": "设计一场两人谈判戏", "expected": "写明进场和离场各变了什么、约束从哪来、知情差"},
        {"id": "SC-T2", "kind": "missing", "scenario": "只说「这一章节奏慢」，不给正文", "expected": "先要正文；先给检查清单，不臆断原因"},
        {"id": "SC-T3", "kind": "conflict", "scenario": "作者把高潮定在第 10 章，但第 6 章已有更强的对决", "expected": "给「降级前文」和「重定峰值」两条路，由作者裁决"},
        {"id": "SC-T4", "kind": "boundary", "scenario": "几十人的群战", "expected": "走群战与转述规则，不逐人写打斗"},
    ],
    "character-and-narrative-control": [
        {"id": "CH-T1", "kind": "positive", "scenario": "双视点悬疑", "expected": "交付视角合同和统一信息表"},
        {"id": "CH-T2", "kind": "missing", "scenario": "人物还没有任何台词样本", "expected": "走「声口待定」的出口，不编造口吻"},
        {"id": "CH-T3", "kind": "conflict", "scenario": "坚持第一人称，又要读者知道主角不知道的阴谋", "expected": "列出补光、换视点、事后叙述等选项和各自代价"},
        {"id": "CH-T4", "kind": "boundary", "scenario": "叙述者不是人（例如一栋房子）", "expected": "说明视角合同哪些项不适用、哪些要改写"},
    ],
    "story-architecture-and-longform-planning": [
        {"id": "ST-T1", "kind": "positive", "scenario": "12 万字单本", "expected": "交付主行动、终点、中点、高潮时点"},
        {"id": "ST-T2", "kind": "missing", "scenario": "连载已发 80 章，只给后续想法，没给已发大纲", "expected": "先要已发内容的状态账，再规划"},
        {"id": "ST-T3", "kind": "conflict", "scenario": "已发布章节锁定，新卷设定与已发内容矛盾", "expected": "只改未发部分，列出最小冲突集合，由作者裁决"},
        {"id": "ST-T4", "kind": "boundary", "scenario": "每篇独立、共享人物的系列短篇", "expected": "说明篇幅容器和分卷规则哪些适用"},
    ],
    "fiction-planning-and-diagnosis": [
        {"id": "FP-T1", "kind": "positive", "scenario": "从一个点子做新作计划", "expected": "定赛道，交付骨架和场景表"},
        {"id": "FP-T2", "kind": "missing", "scenario": "要诊断，只给了梗概", "expected": "只做梗概层的诊断，列出还需要哪些正文"},
        {"id": "FP-T3", "kind": "conflict", "scenario": "读者反馈要求加感情线，作者的契约是纯推理", "expected": "给反馈分级，说明对契约的影响，由作者决定"},
        {"id": "FP-T4", "kind": "boundary", "scenario": "半纪实作品里的统计数字", "expected": "走事实核验流程，核实不了的标「未能核实」"},
    ],
    "genre-fiction-craft": [
        {"id": "GE-T1", "kind": "positive", "scenario": "仙侠长篇设计功法代价体系", "expected": "题材规则加机制，交付代价账"},
        {"id": "GE-T2", "kind": "missing", "scenario": "只说「写个言情」，没有人物和阻碍", "expected": "先问；先给几种阻碍类型供选"},
        {"id": "GE-T3", "kind": "conflict", "scenario": "推理要求线索先给，作者却想最后一章才让凶手出场", "expected": "列出冲突，给「早出场但不显眼」这类折中方案"},
        {"id": "GE-T4", "kind": "boundary", "scenario": "科幻、言情、悬疑混合", "expected": "按混合题材规则确定主次"},
    ],
    "preset-card-generation": [
        {"id": "PC-T1", "kind": "positive", "scenario": "为一部都市异能连载生成推进模式卡", "expected": "交付推进卡，并通过交付前检查"},
        {"id": "PC-T2", "kind": "missing", "scenario": "要文风卡，但没给样文，也没描述", "expected": "先要样文；先给几种候选文风让作者选"},
        {"id": "PC-T3", "kind": "conflict", "scenario": "已锁定的文风卡要求短句，新的表达约束卡写「不要碎句」", "expected": "走版本和锁定内容的冲突出口，不擅自覆盖已锁定的卡"},
        {"id": "PC-T4", "kind": "boundary", "scenario": "要给图片生成模型写提示词卡（不是小说）", "expected": "判为负触发，说明不适用"},
    ],
}

KIND_NOTE = {"positive": "正常", "missing": "缺料", "conflict": "冲突", "boundary": "边界"}

BRIEF_NOTE = (
    "W3 第 1 批骨架，未冻结。cases 已按 notes/suite-contract.md 第六节（附录 E 用例装配，"
    "全部自创）装配；requirements / capabilities / interfaces / applicability 由 W4 依最终 "
    "Skill 承诺完整盘点后补齐，不得留空冻结、不得删难实现需求制造全绿（R09 §6.1）。"
)

REVIEW_NOTE = (
    "W3 第 1 批骨架，未冻结。GQ1–GQ4 只放待填状态与证据位，状态一律 not_proven，"
    "未填任何通过；GQ5 = NOT_PROVEN（无真实任务测试）。本文件不得用于 "
    "kd_artifact_quality.py 预检，也不构成独立 review。W4 须由独立于作者的只读审查"
    "子代理（D3-C）按真实产物重做，绑定实际 brief/Skill 树 SHA 与真实回执。"
)

GQ_TODO = [
    ("GQ1", "功能真实性", "逐项列能力 ID，核对可区分分支、反证/排除条件、修后复验与真实 reference；区分 workflow/automation/external"),
    ("GQ2", "语义自洽", "独立逐节检查 SKILL.md 与所有 reference/模板的跨文件规则，逐组登记 A/B 原文、冲突或解释、反例及复验"),
    ("GQ3", "跨 Skill 接口", "核实 Owner、provider/consumer、字段/类型/版本/路径、缺字段分支、仲裁与双方实际引用；绑定两份 Skill 当前树 SHA"),
    ("GQ4", "适用性与反例", "每个重要规则/阈值记录适用条件、限制、反例及采纳/改写理由；成品不提来源、例子自创"),
]

SECTIONS_TODO = (
    "W4 须把 brief 五组 ID（requirements/capabilities/interfaces/applicability/cases）逐一列全；"
    "每行状态只允许 pass/fail/not_proven；semantics[] 至少一项，引用两处不同真实文本 refs[] 与 record_ref；"
    "interfaces[] 含 provider_ref/consumer_ref 与 peer_tree_sha256 中 provider/consumer 的真实树摘要、record_ref；"
    "applicability[] 含 scope/limitation/counterexample/ref/record_ref；cases[] 有 mode:host/manual/synthetic 与 record_ref。"
    "所有回执形如 {\"path\":\"<真实文件>\",\"sha256\":\"<实际文件摘要>\"}，不得填自造值。"
)


def brief_doc(skill, cases):
    return {
        "version": 1,
        "skill": skill,
        "status": "skeleton",
        "assembled_by": "Agent 1（W3 第 1 批，规范维护）",
        "assembled_at": DATE,
        "case_source": "notes/suite-contract.md 第六节（附录 E 用例装配，全部自创）",
        "kind_mapping": KIND_NOTE,
        "note": BRIEF_NOTE,
        "requirements": [],
        "capabilities": [],
        "interfaces": [],
        "applicability": [],
        "cases": cases,
        "gq5": {"status": "NOT_PROVEN", "note": "无真实任务测试（GQ5 未授权）"},
    }


def review_doc(skill):
    gq = []
    for gid, name, todo in GQ_TODO:
        gq.append({"id": gid, "name": name, "status": "not_proven",
                   "evidence_ref": None, "todo": todo})
    gq.append({"id": "GQ5", "name": "最终版真实任务", "status": "NOT_PROVEN",
               "note": "无真实任务测试（GQ5 未授权）", "evidence_ref": None})
    return {
        "version": 1,
        "skill": skill,
        "status": "skeleton_not_frozen",
        "assembled_by": "Agent 1（W3 第 1 批，规范维护）",
        "assembled_at": DATE,
        "brief_sha256": None,
        "skill_tree_sha256": None,
        "producer": None,
        "reviewer": None,
        "note": REVIEW_NOTE,
        "sha_placeholders": {
            "brief_sha256": "待 W4 按实际 brief.json 原始字节计算（不得自造）",
            "skill_tree_sha256": "待 W4 按最终 output/<skill>/ 整树计算（R09 §6.1，不得自造）",
            "producer": "待填：该 skill 的作者 Worker",
            "reviewer": "待 W4 另派只读审查子代理（独立于作者，D3-C）",
        },
        "gq": gq,
        "sections": {
            "requirements": [], "capabilities": [], "interfaces": [],
            "applicability": [], "cases": [], "semantics": [],
        },
        "sections_todo": SECTIONS_TODO,
        "static_only": True,
        "static_only_note": "静态交付可达成本轮约定；GQ5 与效果仍 NOT_PROVEN，不得写成通过。",
    }


def main():
    created, skipped = [], []
    for skill, cases in CASES.items():
        d = os.path.join(Q, skill)
        os.makedirs(d, exist_ok=True)
        for name, doc in (("brief.json", brief_doc(skill, cases)),
                          ("review.json", review_doc(skill))):
            p = os.path.join(d, name)
            if os.path.exists(p):
                skipped.append(p)
                continue
            with open(p, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=2)
                f.write("\n")
            created.append(p)
    print("新建 %d 个文件：" % len(created))
    for p in created:
        print("  ", p)
    if skipped:
        print("已存在、跳过（不覆盖）：%d 个" % len(skipped))
        for p in skipped:
            print("  ", p)
    # 合法性回读校验
    for skill in CASES:
        for name in ("brief.json", "review.json"):
            with open(os.path.join(Q, skill, name), encoding="utf-8") as f:
                json.load(f)
    print("JSON 合法性回读：全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
