# K1 机械盘点 raw 表 · scene-conflict-and-rhythm

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
- 谱系 v0 来源：`foreshadowing-and-rhythm`、`scene-chapter-design-lab`、`action-fight-scene-craft`

**覆盖率**：已对齐 12 / v0 文件 24 = **50.0%**（v1/v2/v3 各版本有对应：13 / 12 / 12）

**flag 计数**：BLOCK_LOST=6；MISSING=12；RENUMBERED?=1；SHRUNK=6；—=3

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `foreshadowing-and-rhythm/SKILL.md [无编号]` | `1 1 1 1` | `规例检适` | `14243 / 5499 / 26408 / 25589` | `BLOCK_LOST` |
| `foreshadowing-and-rhythm/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `4605 / — / — / —` | `MISSING` |
| `foreshadowing-and-rhythm/references/chapter-ends-and-endings.md [SU-15,SU-16,SU-17,SU-18]` | `1 0 1 1` | `规怎例反检` | `8236 / — / 8669 / 7669` | `—` |
| `foreshadowing-and-rhythm/references/diagnosis.md [无编号]` | `1 0 0 0` | `∅` | `4342 / — / — / —` | `MISSING` |
| `foreshadowing-and-rhythm/references/intensity-and-rhythm.md [SU-02,SU-10,SU-11,SU-12,SU-13,SU-14]` | `1 0 1 1` | `规怎例反检` | `8915 / — / 12011 / 5152` | `SHRUNK;BLOCK_LOST` |
| `foreshadowing-and-rhythm/references/setup-and-payoff.md [SU-01,SU-06,SU-07,SU-08]` | `1 0 1 1` | `规怎例反检` | `7768 / — / 9140 / 4186` | `SHRUNK;BLOCK_LOST` |
| `foreshadowing-and-rhythm/references/source-index.md [无编号]` | `1 0 0 0` | `规` | `6073 / — / — / —` | `MISSING` |
| `foreshadowing-and-rhythm/references/suspense-and-reveal.md [SU-03,SU-04,SU-05,SU-09]` | `1 0 1 1` | `规怎例反检` | `7185 / — / 8352 / 5869` | `SHRUNK` |
| `scene-chapter-design-lab/SKILL.md [无编号]` | `1 1 1 1` | `规怎例检适败` | `10960 / 5499 / 26408 / 25589` | `BLOCK_LOST` |
| `scene-chapter-design-lab/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `1008 / 255 / 670 / 670` | `SHRUNK` |
| `scene-chapter-design-lab/examples/worked-example.md [无编号]` | `1 0 0 0` | `规怎例适` | `6089 / — / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/chapter-continuity.md [S7,S8,S9]` | `1 1 0 0` | `例反检适` | `6070 / 12423 / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/conflicts-and-exceptions.md [K1,K2,K3,K4,K5,K6]` | `1 1 0 0` | `例适` | `6258 / 14206 / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/diagnosis-revision.md [S0,S10,S11,S12]` | `1 1 0 0` | `规例适败` | `5631 / 17609 / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/information-dialogue.md [S5,S6,S6A]` | `1 1 0 0` | `例反` | `6356 / 13847 / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/scene-design.md [S1,S2,S3,S4]` | `1 1 0 0` | `例反适` | `7026 / 12423 / — / —` | `MISSING` |
| `scene-chapter-design-lab/references/source-index.md [无编号]` | `1 0 0 0` | `怎例` | `5359 / — / — / —` | `MISSING` |
| `action-fight-scene-craft/SKILL.md [无编号]` | `1 1 1 1` | `规怎例检败` | `12183 / 5499 / 26408 / 25589` | `BLOCK_LOST` |
| `action-fight-scene-craft/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `754 / 255 / 670 / 670` | `—` |
| `action-fight-scene-craft/references/diagnosis.md [S1,S2… 共8]` | `1 1 0 0` | `规怎反检适` | `6587 / 17609 / — / —` | `MISSING` |
| `action-fight-scene-craft/references/rules.md [AF-01,AF-01–AF-18… 共19]` | `1 1 1 1` | `规怎例反检适` | `19611 / 13847 / 17345 / 12452` | `SHRUNK;RENUMBERED?` |
| `action-fight-scene-craft/references/scope-and-conflicts.md [无编号]` | `1 0 1 1` | `规例` | `6078 / — / 10207 / 7384` | `SHRUNK;BLOCK_LOST` |
| `action-fight-scene-craft/references/source-index.md [无编号]` | `1 0 0 0` | `规` | `8757 / — / — / —` | `MISSING` |
| `action-fight-scene-craft/templates/action-checklist.md [无编号]` | `1 1 1 1` | `∅` | `2267 / 2967 / 3073 / 3073` | `—` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
