# K1 机械盘点 raw 表 · story-architecture-and-longform-planning

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
- 谱系 v0 来源：`plot-architecture`、`serialized-volume-planning`

**覆盖率**：已对齐 9 / v0 文件 28 = **32.1%**（v1/v2/v3 各版本有对应：4 / 9 / 9）

**flag 计数**：MISSING=19；RENUMBERED?=4；SHRUNK=1；—=5

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `plot-architecture/SKILL.md [P4]` | `1 1 1 1` | `规例检适败` | `15838 / 4148 / 31396 / 35201` | `—` |
| `plot-architecture/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `663 / 348 / 646 / 646` | `—` |
| `plot-architecture/references/decision-rework.md [无编号]` | `1 0 0 0` | `规怎例检` | `4485 / — / — / —` | `MISSING` |
| `plot-architecture/references/diagnosis.md [D0,D1,D2,D3,D4,D5]` | `1 0 1 1` | `规检适败` | `21678 / — / 21802 / 23689` | `RENUMBERED?` |
| `plot-architecture/references/examples.md [E1,E2,E3,E4,E5]` | `1 0 1 1` | `规怎例反检适败` | `24761 / — / 24634 / 25157` | `RENUMBERED?` |
| `plot-architecture/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `661 / — / — / —` | `MISSING` |
| `plot-architecture/references/planning.md [无编号]` | `1 0 0 0` | `规检适败` | `14979 / — / — / —` | `MISSING` |
| `plot-architecture/references/revision.md [RC-06,RC-13,RC-15]` | `1 0 1 1` | `规怎检败` | `14862 / — / 14963 / 15126` | `RENUMBERED?` |
| `plot-architecture/references/rules.md [RC-01,RC-02… 共16]` | `1 0 1 1` | `规怎例反检适` | `63537 / — / 46515 / 47755` | `SHRUNK;RENUMBERED?` |
| `plot-architecture/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `规例适` | `17509 / — / — / —` | `MISSING` |
| `plot-architecture/references/source-index.md [PG11483,PG14525… 共19]` | `1 0 0 0` | `规怎例适` | `26357 / — / — / —` | `MISSING` |
| `plot-architecture/templates/diagnosis-report.md [无编号]` | `1 0 0 0` | `怎检` | `5743 / — / — / —` | `MISSING` |
| `plot-architecture/templates/plot-canvas.md [无编号]` | `1 0 1 1` | `怎检` | `5282 / — / 5316 / 5388` | `—` |
| `plot-architecture/templates/scene-table.md [无编号]` | `1 0 0 0` | `怎检` | `6421 / — / — / —` | `MISSING` |
| `serialized-volume-planning/SKILL.md [R04,WAVE4]` | `1 1 1 1` | `规例检败` | `22717 / 4148 / 31396 / 35201` | `—` |
| `serialized-volume-planning/agents/openai.yaml [无编号]` | `1 1 1 1` | `∅` | `519 / 348 / 646 / 646` | `—` |
| `serialized-volume-planning/examples/wave4-casebook.md [B-01]` | `1 0 0 0` | `例败` | `1855 / — / — / —` | `MISSING` |
| `serialized-volume-planning/examples/worked-example.md [WAVE4]` | `1 0 0 0` | `规例检败` | `12325 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/01-volume-architecture.md [R04]` | `1 0 0 0` | `规怎例反检适败` | `15787 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/02-chapter-hooks.md [R04]` | `1 0 0 0` | `怎例反检适败` | `12673 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/03-continuity-and-reset.md [无编号]` | `1 0 0 0` | `例反检适败` | `13056 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/04-formula-and-variation.md [无编号]` | `1 0 0 0` | `规怎例反适败` | `11837 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/05-production-constraints.md [无编号]` | `1 0 0 0` | `规例反检适败` | `19702 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/06-source-index.md [R04]` | `1 0 0 0` | `规例反检败` | `47820 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/07-production-discipline.md [无编号]` | `1 0 0 0` | `规例反检` | `11167 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/08-cross-volume-dependencies.md [无编号]` | `1 0 0 0` | `反检败` | `5409 / — / — / —` | `MISSING` |
| `serialized-volume-planning/references/legacy-metadata.md [R04]` | `1 0 0 0` | `∅` | `1743 / — / — / —` | `MISSING` |
| `serialized-volume-planning/templates/series-volume-dependency.md [无编号]` | `1 0 0 0` | `∅` | `1294 / — / — / —` | `MISSING` |

## 机械对齐阻塞与如实记录

- 未对齐（v3 无对应）的 v0 文件逐行见上表 `MISSING`，不伪造行、不跳过。
- 版本重组后内容可能并入他文件；`title~` 为粗粒度相似标题信号，须 W2 定向精读确认，不作逐条决定。
- v1→v2 题材/目录改名按「新旧前缀 + 标题」对齐，不按文件名。
