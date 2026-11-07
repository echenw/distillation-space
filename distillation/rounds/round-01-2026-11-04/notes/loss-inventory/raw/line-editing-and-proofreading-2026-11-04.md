# K1 机械盘点 raw 表 · line-editing-and-proofreading

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
- 谱系 v0 来源：`style-refinement-and-proofreading`

**覆盖率**：已对齐 9 / v0 文件 10 = **90.0%**（v1/v2/v3 各版本有对应：6 / 9 / 9）

**flag 计数**：BLOCK_LOST=4；MISSING=1；SHRUNK=5；—=4

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `style-refinement-and-proofreading/SKILL.md [无编号]` | `1 1 1 1` | `规怎检适` | `12051 / 4753 / 12573 / 13488` | `—` |
| `style-refinement-and-proofreading/examples/worked-example.md [无编号]` | `1 1 1 1` | `∅` | `4457 / 14068 / 4463 / 5028` | `SHRUNK` |
| `style-refinement-and-proofreading/references/en-mechanics-and-punctuation.md [C01,C02… 共10]` | `1 1 1 1` | `规怎例反检适` | `12268 / 12708 / 11334 / 5903` | `SHRUNK;BLOCK_LOST` |
| `style-refinement-and-proofreading/references/en-paragraph-and-emphasis.md [C20,C21,C22,C23,C24]` | `1 1 1 1` | `规例反适` | `6547 / 6473 / 6161 / 2413` | `SHRUNK;BLOCK_LOST` |
| `style-refinement-and-proofreading/references/en-sentence-revision.md [C11,C12… 共9]` | `1 1 1 1` | `规例反适` | `12532 / 12173 / 11409 / 4978` | `SHRUNK;BLOCK_LOST` |
| `style-refinement-and-proofreading/references/en-word-choice-and-concision.md [C25,C26,C27,C28,C29]` | `1 1 1 1` | `规怎例反适` | `8444 / 8150 / 7488 / 2494` | `SHRUNK;BLOCK_LOST` |
| `style-refinement-and-proofreading/references/source-index.md [无编号]` | `1 0 0 0` | `规怎检` | `8537 / — / — / —` | `MISSING` |
| `style-refinement-and-proofreading/references/workflow.md [无编号]` | `1 0 1 1` | `∅` | `6582 / — / 7145 / 7596` | `—` |
| `style-refinement-and-proofreading/references/zh-mechanics.md [SR-13,SR-15]` | `1 0 1 1` | `∅` | `9664 / — / 9625 / 9964` | `—` |
| `style-refinement-and-proofreading/references/zh-sentence-and-wording.md [SR-01,SR-02… 共13]` | `1 0 1 1` | `规怎例反检适` | `12212 / — / 12282 / 12710` | `—` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
