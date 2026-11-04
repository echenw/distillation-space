---
name: horror-gothic-suspense-b05
description: "恐怖/哥特/怪谈写作与修订技能（来源：27 份 1764–1921 年恐怖文学材料，当前 P2 为 27/27 TRUSTED_FULL，批次 A-04-B05）。当用户要写、诊断或修订恐怖、哥特、怪谈、灵异、心理惊悚类小说或短篇，需要设计恐惧结构、超自然机制、证词体系、恐惧剂量与怪谈式结局时使用。不用于非虚构灵异纪实、纯血腥场面调度或儿童向怪谈照搬。"
---


# Horror-Gothic-Suspense（恐怖惊悚怪谈写作技能 · 批次 B05）

## P4 专项操作入口（Agent B 静态修订）

本轮直接修正原有 rules/techniques/templates，再提供 [精简条件规则](references/p4-field-guide.md)。按用户任务选择主分支，只加载该分支所需参考资料；原始叙事实例是 **F（作品现象）**，提炼为作者可以采用的流程属于 **H/P（设计推断/建议）**，不能写成原作者明确教过的方法。

**必须先获得**任务（写作/策划/诊断/改写）、目标受众与媒介、已知人物/事件/规则及原稿（诊断时必需），并确定允许改写的范围。输出合同：`任务路由 → 输入事实/缺口 → 选择的规则ID → 有位置的文本证据或来源 → 可执行方案（含反方案） → 交付物 → 尚未验证的风险`。当用户没给原稿时不能虚构段落位置；要求改稿时默认只给方案或非覆盖的新稿；涉及权利、历史真实或危险现实建议时，划清故事创作与现实事实边界。

**退出方式**：缺关键剧情信息，给最小补料清单和两条可选方向；用户目标相互冲突，保留两个条件分支和取舍，不捏造统一结论；超出本 Skill 的类型/年代/媒介/读者条件，说明不能支持的结论，必要时只提供明确标为推断的结构类比；效果与真实用户任务未验证时标 `NOT_PROVEN`。这不是自动触发、自动运行或保证创作效果的程序。


从 27 份 Project Gutenberg 恐怖文学（Dickens、Le Fanu、Gaskell、Kipling、M.R. James、Henry James、Stoker、Wilde、Bierce、Blackwood、Marryat 等）与文论/证词材料归纳；当前 P2 为 27/27 `TRUSTED_FULL`。每条规则的来源事实仍须按 PG ID+行号回读，FULL 不等于跨书效果已经验证。

## 触发
- 用户要写/起草恐怖、哥特、怪谈、灵异、心理惊悚小说或短篇。
- 用户要诊断、修订既有恐怖稿件（结构、剂量、证词、结局问题）。
- 用户要为故事设计超自然机制、诅咒系统、闹鬼规则。
- 用户询问"如何营造恐惧/悬念/怪谈氛围"类写作问题。

## 负触发（不使用本技能）
- 非虚构灵异纪实、超自然调查报告的"真实性"咨询（本技能的证词工程是叙事装置，见 references/scope-and-conflicts.md §3 C5）。
- 纯血腥/血浆恐怖的场面调度（本批来源以氛围与心理恐怖为主）。
- 儿童向怪谈的直接照搬（来源含时代伦理框架，必须重构）。
- 科幻恐怖的核心机制（来源时代前置于科幻）。

## 输入权限
- 需要：稿件文本或故事设定（可空=从零构思）、目标篇幅（缺失时可给创作假设）、道德机制偏好（复仇/悲剧/混合；未指定时按用户构思合理尝试，不擅自默认悲剧）。
- 不需要：原来源文本（引用已内置）；不需要修改任何原始材料。

## 工作分支
1. **从零构思** → 读 references/techniques.md 分域 A、B → 用 templates/haunting-designer.md 定机制 → 用 templates/dread-scene-planner.md 排场景。
2. **起草中咨询** → 按问题域路由 references/rules.md 对应规则（RG-01..RG-20），规则含失效条件。
3. **诊断修订** → 用 templates/manuscript-diagnosis.md 逐项审计 → 按 MD-12 开 RG 编号处方 → 必要时对照 references/examples.md 的正反例。
4. **冲突与边界问题** → references/scope-and-conflicts.md（5 项裁决 CONDITIONAL/UNRESOLVED + 时代重构点）。

## 输出
- 构思：机制设计表（HD 全字段）+ 场景规划表（DS 全字段）+ 规则遵循说明。
- 诊断：诊断表（MD 全字段）+ 处方清单（RG 编号+改法）。
- 所有有原始来源依据的建议附规则编号与核对过的来源锚点（PG+行号），用户可要求回读原文核验。

## 失败出口
- 用户故事的核心冲突与全部 20 条规则不兼容（如纯幽默鬼故事无怪谈核）→ 如实告知本技能不适用，不硬套。
- 道德宇宙论选择与用户要求冲突 → 列出 C3 裁决（UNRESOLVED）交用户决定，不代选。
- 来源引文与用户持有的版本行号不一致 → 以 PG 整本阅读版.txt 为准并提供原句，不猜行号。
- 真实性边界：本技能产出一律为虚构创作辅助；若用户拟以"真实事件"名义发布，提示核实与伦理义务，不代为认证。

## 来源与核验
- 27 份来源、当前 P2 可信全文状态、旧版本和许可声明：references/version-and-provenance.md；来源行号：references/source-index.md。
- 规则库（20 条，全部带锚点）：references/rules.md。
- 适用范围、冲突裁决、时代重构：references/scope-and-conflicts.md。
- 正反例：references/examples.md。
- 模板：templates/haunting-designer.md、templates/dread-scene-planner.md、templates/manuscript-diagnosis.md。
