# K1 机械盘点 raw 表 · fiction-planning-and-diagnosis

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`fiction-craft`、`fiction-craft-and-language`、`reader-experience-and-critique`、`research-fact-verification`

**覆盖率**：已对齐 20 / v0 文件 44 = **45.5%**（v1/v2/v3 各版本有对应：14 / 20 / 20）

**flag 计数**：BLOCK_LOST=5；MISSING=24；RENUMBERED?=2；SHRUNK=4；—=13

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `fiction-craft/SKILL.md [P4]` | `1 1 1 1` | `规例检败` | `17104 / 4086 / 29101 / 32772` | `BLOCK_LOST` |
| `fiction-craft/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `152 / 174 / 715 / 715` | `—` |
| `fiction-craft/references/diagnosis.md [无编号]` | `1 0 1 1` | `规检适败` | `19417 / — / 19650 / 22163` | `—` |
| `fiction-craft/references/drafting.md [无编号]` | `1 0 1 1` | `规检适败` | `16449 / — / 16881 / 16881` | `BLOCK_LOST` |
| `fiction-craft/references/examples.md [无编号]` | `1 0 0 0` | `怎适败` | `21235 / — / — / —` | `MISSING` |
| `fiction-craft/references/p4-field-guide.md [无编号]` | `1 0 0 0` | `∅` | `2705 / — / — / —` | `MISSING` |
| `fiction-craft/references/planning.md [无编号]` | `1 0 1 1` | `规例反检败` | `17761 / — / 17413 / 17521` | `—` |
| `fiction-craft/references/revision.md [无编号]` | `1 0 1 1` | `规例适败` | `14153 / — / 14008 / 13987` | `—` |
| `fiction-craft/references/rule-examples.md [RC-01,RC-02… 共21]` | `1 1 1 1` | `规怎例反检适败` | `16809 / 20260 / 16588 / 16581` | `SHRUNK;BLOCK_LOST` |
| `fiction-craft/references/rules.md [RC-01,RC-02… 共21]` | `1 1 1 1` | `规怎例反检适败` | `101960 / 20260 / 16588 / 16581` | `SHRUNK;RENUMBERED?` |
| `fiction-craft/references/scope-and-conflicts.md [无编号]` | `1 0 1 1` | `规例适` | `19044 / — / 18706 / 18371` | `—` |
| `fiction-craft/references/source-index.md [无编号]` | `1 0 0 0` | `规怎例适` | `17449 / — / — / —` | `MISSING` |
| `fiction-craft/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `规` | `4637 / — / — / —` | `MISSING` |
| `fiction-craft/templates/diagnosis-report.md [无编号]` | `1 0 1 1` | `∅` | `3414 / — / 3523 / 3756` | `—` |
| `fiction-craft/templates/novel-plan.md [无编号]` | `1 0 1 1` | `∅` | `4406 / — / 4462 / 4478` | `—` |
| `fiction-craft/templates/revision-sheet.md [无编号]` | `1 0 1 1` | `∅` | `3943 / — / 3987 / 4107` | `—` |
| `fiction-craft/templates/scene-plan.md [无编号]` | `1 0 1 1` | `∅` | `3277 / — / 3484 / 3484` | `—` |
| `fiction-craft-and-language/SKILL.md [无编号]` | `1 1 1 1` | `规怎例检适` | `21990 / 4086 / 29101 / 32772` | `—` |
| `fiction-craft-and-language/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `5772 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/character-and-experience.md [无编号]` | `1 0 0 0` | `规例适败` | `9657 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/contract-and-morality.md [无编号]` | `1 0 0 0` | `规例适` | `6098 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/diagnosis.md [无编号]` | `1 0 1 1` | `检` | `5702 / — / 19650 / 22163` | `—` |
| `fiction-craft-and-language/references/language-and-revision.md [无编号]` | `1 0 0 0` | `∅` | `4659 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/modern-and-zh.md [无编号]` | `1 0 0 0` | `∅` | `3588 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/scene-selection-and-story.md [无编号]` | `1 0 0 0` | `例适` | `6624 / — / — / —` | `MISSING` |
| `fiction-craft-and-language/references/source-index.md [无编号]` | `1 0 0 0` | `规` | `8560 / — / — / —` | `MISSING` |
| `reader-experience-and-critique/SKILL.md [无编号]` | `1 1 1 1` | `怎` | `5625 / 4086 / 29101 / 32772` | `—` |
| `reader-experience-and-critique/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `192 / 174 / 715 / 715` | `—` |
| `reader-experience-and-critique/examples/worked-example.md [C-08]` | `1 1 0 0` | `∅` | `2636 / 2681 / — / —` | `MISSING` |
| `reader-experience-and-critique/references/01-reader-contract-and-effect.md [无编号]` | `1 0 0 0` | `反` | `2254 / — / — / —` | `MISSING` |
| `reader-experience-and-critique/references/02-criticism-and-market-bias.md [无编号]` | `1 0 0 0` | `反` | `1994 / — / — / —` | `MISSING` |
| `reader-experience-and-critique/references/03-voice-sincerity-and-characters.md [无编号]` | `1 0 0 0` | `反检` | `2234 / — / — / —` | `MISSING` |
| `reader-experience-and-critique/references/04-workflow-and-decisions.md [R10,R11,R12]` | `1 1 0 0` | `规适` | `2358 / 10435 / — / —` | `MISSING` |
| `reader-experience-and-critique/references/05-source-index.md [C-08]` | `1 1 0 0` | `∅` | `3644 / 2681 / — / —` | `MISSING` |
| `research-fact-verification/SKILL.md [无编号]` | `1 1 1 1` | `怎例检败` | `8821 / 4086 / 29101 / 32772` | `BLOCK_LOST` |
| `research-fact-verification/agents/openai.yaml [无编号]` | `1 1 1 1` | `败` | `1579 / 174 / 715 / 715` | `SHRUNK;BLOCK_LOST` |
| `research-fact-verification/references/conflict-and-versions.md [无编号]` | `1 0 0 0` | `∅` | `4152 / — / — / —` | `MISSING` |
| `research-fact-verification/references/examples.md [A1,A10… 共16]` | `1 1 0 0` | `例反` | `8649 / 9857 / — / —` | `MISSING` |
| `research-fact-verification/references/failure-modes.md [无编号]` | `1 0 0 0` | `∅` | `3006 / — / — / —` | `MISSING` |
| `research-fact-verification/references/research-protocol.md [无编号]` | `1 0 0 0` | `∅` | `5101 / — / — / —` | `MISSING` |
| `research-fact-verification/references/source-boundaries.md [无编号]` | `1 0 0 0` | `规` | `4323 / — / — / —` | `MISSING` |
| `research-fact-verification/references/source-derived-checks.md [R06,R07… 共14]` | `1 1 1 1` | `怎检` | `13464 / 27916 / 23854 / 22461` | `SHRUNK;RENUMBERED?` |
| `research-fact-verification/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `4267 / — / — / —` | `MISSING` |
| `research-fact-verification/references/templates.md [无编号]` | `1 0 0 0` | `检` | `2095 / — / — / —` | `MISSING` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
