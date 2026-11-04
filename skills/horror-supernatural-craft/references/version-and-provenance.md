# 版本、来源覆盖与许可

历史版 Skill 的 YAML 原始元数据（只读保留，当前 ChatGPT frontmatter 只允许 name/description）：


name: horror-supernatural-craft
description: 以 1886–1916 恐怖/怪谈/哥特正典 26 部（23 来源族，约 212 万 o200k tok 全文实读）为证据的恐怖小说创作方法——超自然机制与誓约诅咒设计、恐惧感技术、物证对账、叙事框架与收束谱系，带条件、反例、路线选择表与证据行号回指。
metadata:
  source: "26 sources / 23 families (PG3268, PG3781, PG43, PG10002, PG10624, PG10659, PG45964, PG11610, PG1190, PG1210, PG14168, PG1710, PG18508, PG19750, PG23220, PG24879, PG35517, PG5083, PG5164, PG5182, PG6781, PG72421, PG79427, PG9909, PG46363, PG459)"
  evidence_family: "23"
  source_coverage: "100% o200k tok（26/26 FULL；PG18508 于 2026-10-25 补读至 EOF 升 FULL，见 references/06-source-index.md）"
  modern_applicability: "NOT_PROVEN"
  runtime_tests: "NOT_PROVEN"

本文件记录 Agent2 最终消费者包的版本、来源覆盖和许可边界；历史 Round 的 ZIP/receipt 不作为 Skill 运行时依赖。P6 正式冻结不在本轮 P4 收口范围。
原文 SHA-256：26/26 与批次来源一致；历史覆盖总账 26/26 连续区间，且每本独立内容卡有带行号的具体 F 观察。此为可信 P2 审计，不是本轮再次通读 26 本。
原来 23 来源族（Blackwood 系列等按族合并），不得用同系列多个 PG 伪称独立证据。
许可证：旧 Skill 未明确声明的权利条件一律 LICENSE_NOT_DECLARED；不继承或虚构公共领域许可，引用短片段并保留 PG 身份。
runtime_tests=NOT_RUN；P5/GQ5=NOT_PROVEN；P6/P7=NOT_DONE。
决策优先级：本轮改正的主 references > 简版 p4-field-guide；原作品发生的事件是 F，跨作品归纳是 H，具体执行是 P。

## 逐来源作用索引

| PG | 可信阅读状态 | P3 规则关联 | 作用 |
|---|---|---|---|
| PG10002 | TRUSTED_FULL | M01, M02, M06, M12, M16, M17, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG10624 | TRUSTED_FULL | M04, M08, M10, M11 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG10659 | TRUSTED_FULL | M01, M02, M03, M05, M07, M08, M10, M11, M12, M16, M18, M21, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG11610 | TRUSTED_FULL | M02, M05, M12, M13, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG1190 | TRUSTED_FULL | M05, M08, M21 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG1210 | TRUSTED_FULL | M04, M08, M11, M14, M16, M17, M18, M21, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG14168 | TRUSTED_FULL | M03, M17, M21 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG1710 | TRUSTED_FULL | M01, M13, M14, M19, M21 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG18508 | TRUSTED_FULL | M04, M09, M15, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG19750 | TRUSTED_FULL | M11, M14, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG23220 | TRUSTED_FULL | M13, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG24879 | TRUSTED_FULL | M06, M07, M11, M13, M14, M17, M18, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG3268 | TRUSTED_FULL | M02, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG35517 | TRUSTED_FULL | M01, M06, M09, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG3781 | TRUSTED_FULL | - | 上下文，不充当多来源正向证据 |
| PG43 | TRUSTED_FULL | M01, M02, M03, M05, M06, M07, M08, M09, M10, M11, M16, M20, M21, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG459 | TRUSTED_FULL | - | 上下文，不充当多来源正向证据 |
| PG45964 | TRUSTED_FULL | M14, M16 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG46363 | TRUSTED_FULL | M05, M15, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG5083 | TRUSTED_FULL | M06, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG5164 | TRUSTED_FULL | M01, M09, M11, M12, M15, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG5182 | TRUSTED_FULL | M02, M05, M06, M13, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG6781 | TRUSTED_FULL | M01, M14 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG72421 | TRUSTED_FULL | M02, M04, M05, M11, M12, M17, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG79427 | TRUSTED_FULL | M05, M13, M15, M18, M19, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
| PG9909 | TRUSTED_FULL | M07, M18, M22 | F 事实/限定/反例，以对应 M 逐条裁决 |
