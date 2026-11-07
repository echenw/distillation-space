# K1 机械盘点 raw 表 · cross-media-drama-adaptation

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
- 谱系 v0 来源：`cross-media-drama-transfer`

**覆盖率**：已对齐 2 / v0 文件 11 = **18.2%**（v1/v2/v3 各版本有对应：10 / 2 / 2）

**flag 计数**：BLOCK_LOST=1；MISSING=9；SHRUNK=1；—=1

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `cross-media-drama-transfer/SKILL.md [CROSS-MEDIA]` | `1 1 1 1` | `怎检败` | `10123 / 5763 / 16162 / 13987` | `SHRUNK;BLOCK_LOST` |
| `cross-media-drama-transfer/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `331 / 254 / 754 / 754` | `—` |
| `cross-media-drama-transfer/examples/worked-example.md [无编号]` | `1 1 0 0` | `规` | `3725 / 4269 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/01-transferability.md [R1]` | `1 1 0 0` | `例反` | `3099 / 3674 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md [R2]` | `1 1 0 0` | `例反检` | `3780 / 4316 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/03-information-carriers.md [R3]` | `1 1 0 0` | `反` | `3888 / 4224 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md [R4]` | `1 1 0 0` | `例反适` | `4526 / 4826 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/05-stage-realization.md [R5]` | `1 1 0 0` | `例检` | `4698 / 4864 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md [R6]` | `1 1 0 0` | `规例检` | `4771 / 4881 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md [R7]` | `1 1 0 0` | `规检` | `3334 / 4388 / — / —` | `MISSING` |
| `cross-media-drama-transfer/references/08-source-index.md [R8]` | `1 0 0 0` | `规例` | `12794 / — / — / —` | `MISSING` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
