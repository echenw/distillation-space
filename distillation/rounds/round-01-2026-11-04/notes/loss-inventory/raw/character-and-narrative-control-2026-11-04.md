# K1 机械盘点 raw 表 · character-and-narrative-control

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
- 谱系 v0 来源：`narrative-pov-information-control`、`nonlinear-time-craft`、`character-psychology-trauma-craft`、`psycho-trauma-craft-b10`

**覆盖率**：已对齐 12 / v0 文件 38 = **31.6%**（v1/v2/v3 各版本有对应：14 / 12 / 12）

**flag 计数**：BLOCK_LOST=5；MISSING=26；—=7

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `narrative-pov-information-control/SKILL.md [无编号]` | `1 1 1 1` | `规怎例检适` | `20329 / 4858 / 25431 / 26400` | `BLOCK_LOST` |
| `narrative-pov-information-control/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `6346 / — / — / —` | `MISSING` |
| `narrative-pov-information-control/references/diagnosis.md [无编号]` | `1 0 1 1` | `规例` | `8678 / — / 12770 / 14363` | `—` |
| `narrative-pov-information-control/references/information-control.md [无编号]` | `1 0 1 1` | `∅` | `7046 / — / 8848 / 9193` | `—` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md [无编号]` | `1 0 1 1` | `怎例检` | `11390 / — / 12415 / 12691` | `—` |
| `narrative-pov-information-control/references/scene-summary-and-time.md [无编号]` | `1 0 1 1` | `例检` | `6694 / — / 8309 / 8734` | `BLOCK_LOST` |
| `narrative-pov-information-control/references/source-index.md [无编号]` | `1 0 0 0` | `规` | `8653 / — / — / —` | `MISSING` |
| `narrative-pov-information-control/references/zh-and-serial.md [无编号]` | `1 0 1 1` | `规怎检` | `5396 / — / 5411 / 5563` | `—` |
| `nonlinear-time-craft/SKILL.md [P4]` | `1 1 1 1` | `规例检适败` | `9675 / 4858 / 25431 / 26400` | `BLOCK_LOST` |
| `nonlinear-time-craft/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `202 / 309 / 730 / 730` | `—` |
| `nonlinear-time-craft/references/01-loops.md [无编号]` | `1 0 0 0` | `规` | `3468 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/02-flickers.md [无编号]` | `1 0 0 0` | `规` | `2887 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/03-viewers.md [无编号]` | `1 0 0 0` | `例` | `2494 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `规例反` | `8597 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/05-exchanges.md [无编号]` | `1 0 0 0` | `怎` | `5798 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/06-temporal-protocol.md [无编号]` | `1 0 0 0` | `怎反适败` | `4870 / — / — / —` | `MISSING` |
| `nonlinear-time-craft/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `393 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/SKILL.md [无编号]` | `1 1 1 1` | `例适败` | `8828 / 4858 / 25431 / 26400` | `BLOCK_LOST` |
| `character-psychology-trauma-craft/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `636 / 309 / 730 / 730` | `—` |
| `character-psychology-trauma-craft/references/counterexamples.md [无编号]` | `1 0 0 0` | `∅` | `1776 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/references/examples.md [无编号]` | `1 0 0 0` | `例` | `3426 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md [C09-P01,C09-P02… 共12]` | `1 1 0 0` | `∅` | `12168 / 14552 / — / —` | `MISSING` |
| `character-psychology-trauma-craft/references/scene-revision.md [无编号]` | `1 0 0 0` | `∅` | `3152 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `4960 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/references/trauma-boundaries.md [无编号]` | `1 0 0 0` | `∅` | `2886 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/templates/character-state-card.md [无编号]` | `1 0 0 0` | `∅` | `2298 / — / — / —` | `MISSING` |
| `character-psychology-trauma-craft/templates/revision-check.md [无编号]` | `1 0 0 0` | `∅` | `1093 / — / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/SKILL.md [无编号]` | `1 1 1 1` | `规例适败` | `9486 / 4858 / 25431 / 26400` | `BLOCK_LOST` |
| `psycho-trauma-craft-b10/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `525 / 309 / 730 / 730` | `—` |
| `psycho-trauma-craft-b10/examples/scene-examples.md [无编号]` | `1 0 0 0` | `规例反` | `6004 / — / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/72-source-differences.md [B-10]` | `1 1 0 0` | `∅` | `20768 / 10471 / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/rules.md [B-10,RT-01… 共19]` | `1 1 0 0` | `规例反检适` | `24410 / 14552 / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `例适` | `3694 / — / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/source-index.md [B-10]` | `1 1 0 0` | `∅` | `16925 / 10471 / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/techniques.md [无编号]` | `1 0 0 0` | `反` | `3940 / — / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/references/version-and-license.md [B-10]` | `1 1 0 0` | `规适` | `3036 / 10471 / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/templates/psycho-trauma-designer.md [PT-01–PT-14]` | `1 1 0 0` | `∅` | `2839 / 10471 / — / —` | `MISSING` |
| `psycho-trauma-craft-b10/templates/psycho-trauma-diagnosis.md [PD-01–PD-10]` | `1 1 0 0` | `∅` | `2187 / 10471 / — / —` | `MISSING` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
