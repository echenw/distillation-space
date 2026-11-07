**genre 规则单元 4584；v3 对齐成功 37（0.8%）；UNALIGNED? 4547（99.2%）**

# K1 返工 raw 表（r2）· genre-fiction-craft（按 14 类题材分组）

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 旧表原样保留）
- 盘点单位：规则单元（规则编号 / 文件路径+标题）；机制卡编号从标题括号与表格行提取。
- 对齐：按 2.8 节用规则编号（含 2.3 节改号对照）+ 标题 + 内容块，不按文件名。
- 阈值：默认 30% 或 1.5 KB；**01 推理 / 07 求生灾变 / 10 职业竞技收紧到 20%**（5.1 节、§6.1）。
- 补充标记 `UNALIGNED?` / `SOURCE_ONLY` **不是丢失、待定向精读**；`MISSING` 只留给确实无相似编号/标题/内容块的单元。
- v1 题材目录为中文名、v2/v3 为英文名，按 `NN-` 数字前缀定位；跨题材多归属按主归属登记并记阻塞。

---

## 题材 01 推理（阈值 20%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 01 推理

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK；本题材按 5.1 节 / §6.1 收紧到 20%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`crime-mystery-craft-b03`、`mystery-clue-fairplay`、`mystery-detection-craft-b04`、`mystery-detective-plot-forge`、`mystery-evidence-chain-designer`

**规则单元数 379；v3 对齐成功 2（0.5%）；对齐失败 UNALIGNED? 377（99.5%）**
**flag 计数**：RENUMBERED?=2；SOURCE_ONLY=34；UNALIGNED?=377

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `crime-mystery-craft-b03/SKILL.md+0.这是什么` | `1 0 0 0` | `∅` | `611 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+证据边界先读这一条否则后面的规则会被误用` | `1 0 0 0` | `规` | `1809 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+1.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+触发` | `1 0 0 0` | `反` | `425 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+负触发不要用本skill` | `1 0 0 0` | `例` | `641 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+2.任务路由` | `1 0 0 0` | `∅` | `991 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+3.最短执行路径3个门按顺序过` | `1 0 0 0` | `∅` | `1230 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `211 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `236 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `207 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `150 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `128 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `195 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `149 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `145 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `201 / — / — / —` | `UNALIGNED?` |
| `R11A` | `1 0 0 0` | `∅` | `158 / — / — / —` | `UNALIGNED?` |
| `R11B` | `1 0 0 0` | `∅` | `145 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `219 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `289 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+4.规则索引14条canonical正文在各reference文件` | `1 0 0 0` | `∅` | `3254 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+5.执行步骤拿到一个真实请求时照做` | `1 0 0 0` | `∅` | `937 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `699 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+7.模板案件设计表` | `1 0 0 0` | `例适` | `1251 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `873 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/SKILL.md+9.结构` | `1 0 0 0` | `∅` | `893 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规适` | `2851 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+请求` | `1 0 0 0` | `∅` | `163 / — / — / —` | `UNALIGNED?` |
| `G1` | `1 0 0 0` | `∅` | `487 / — / — / —` | `UNALIGNED?` |
| `G2` | `1 0 0 0` | `∅` | `487 / — / — / —` | `UNALIGNED?` |
| `G3` | `1 0 0 0` | `∅` | `487 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+第2步命中规则` | `1 0 0 0` | `∅` | `594 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+第3步输出四块` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+1判定` | `1 0 0 0` | `∅` | `80 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+2案件设计表填完的关键格` | `1 0 0 0` | `∅` | `828 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+3线索记账表节选` | `1 0 0 0` | `∅` | `585 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+4动作清单` | `1 0 0 0` | `∅` | `916 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/examples/worked-example.md+第4步自检` | `1 0 0 0` | `规` | `373 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/references/03-resolution-and-conflicts.md+收束装置清单三种可互换的做法` | `1 0 0 0` | `∅` | `776 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/references/03-resolution-and-conflicts.md+§6时代局限必须标注不得作为技法迁移` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/references/03-resolution-and-conflicts.md+§7拒收清单不得把单本情节设计升为通则` | `1 0 0 0` | `∅` | `1020 / — / — / —` | `UNALIGNED?` |
| `PG108` | `1 0 0 0` | `∅` | `5679 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG807` | `1 0 0 0` | `∅` | `5679 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `crime-mystery-craft-b03/references/05-source-index.md+证据族去重` | `1 0 0 0` | `∅` | `423 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `crime-mystery-craft-b03/references/05-source-index.md+本轮补写补读的部分` | `1 0 0 0` | `∅` | `559 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A1` | `1 0 0 0` | `∅` | `264 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `∅` | `193 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `∅` | `275 / — / — / —` | `UNALIGNED?` |
| `A4` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `A5` | `1 0 0 0` | `∅` | `194 / — / — / —` | `UNALIGNED?` |
| `A6` | `1 0 0 0` | `∅` | `258 / — / — / —` | `UNALIGNED?` |
| `A7` | `1 0 0 0` | `∅` | `270 / — / — / —` | `UNALIGNED?` |
| `A8` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `A9` | `1 0 0 0` | `∅` | `230 / — / — / —` | `UNALIGNED?` |
| `A10` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `A11` | `1 0 0 0` | `∅` | `213 / — / — / —` | `UNALIGNED?` |
| `A12` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `A13` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `A14` | `1 0 0 0` | `∅` | `154 / — / — / —` | `UNALIGNED?` |
| `A15` | `1 0 0 0` | `∅` | `264 / — / — / —` | `UNALIGNED?` |
| `A16` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `A17` | `1 0 0 0` | `∅` | `238 / — / — / —` | `UNALIGNED?` |
| `A18` | `1 0 0 0` | `∅` | `139 / — / — / —` | `UNALIGNED?` |
| `A19` | `1 0 0 0` | `∅` | `222 / — / — / —` | `UNALIGNED?` |
| `A20` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/references/06-adjudication-log.md+拒收reject一览同时见03末节` | `1 0 0 0` | `∅` | `524 / — / — / —` | `UNALIGNED?` |
| `crime-mystery-craft-b03/references/06-adjudication-log.md+本轮notproven出口` | `1 0 0 0` | `∅` | `600 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+1.先定解谜契约` | `1 0 0 0` | `∅` | `634 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+2.三个核心不变量` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+a.信息披露时点` | `1 0 0 0` | `∅` | `172 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+b.证据与推断分层` | `1 0 0 0` | `∅` | `258 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+c.候选空间与信息来源` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+3.执行流程` | `1 0 0 0` | `∅` | `1308 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+4.12条规则导航` | `1 0 0 0` | `规例适` | `664 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+5.默认输出` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+解答证据矩阵` | `1 0 0 0` | `∅` | `132 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+嫌疑假设矩阵` | `1 0 0 0` | `∅` | `82 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/SKILL.md+公平性finding` | `1 0 0 1` | `∅` | `347 / — / — / —` | `RENUMBERED?` |
| `mystery-clue-fairplay/SKILL.md+6.失败出口` | `1 0 0 0` | `例` | `762 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+设定` | `1 0 0 0` | `∅` | `370 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+1.答案命题` | `1 0 0 0` | `∅` | `264 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+2.必要事实与披露` | `1 0 0 0` | `∅` | `564 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+3.证据链` | `1 0 0 0` | `∅` | `276 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+4.合法误导` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+5.揭示` | `1 0 0 0` | `∅` | `296 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/examples/worked-example.md+6.冲突版检查` | `1 0 0 0` | `∅` | `360 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/anti-patterns.md+f反例边界` | `1 0 0 0` | `∅` | `478 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/anti-patterns.md+五类高风险作弊` | `1 0 0 0` | `∅` | `512 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/anti-patterns.md+修法优先级` | `1 0 0 0` | `规` | `336 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/anti-patterns.md+时代与现实边界` | `1 0 0 0` | `∅` | `226 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/clue-placement.md+f` | `1 0 0 0` | `∅` | `535 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/clue-placement.md+h→p` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/clue-placement.md+不是r1fail的情况` | `1 0 0 0` | `∅` | `182 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/clue-placement.md+检查` | `1 0 0 0` | `∅` | `288 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+1.支持公平性更像信息权利不像固定线索配方` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+观察→推断分层` | `1 0 0 0` | `∅` | `671 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+叙事知识边界` | `1 0 0 0` | `例检` | `389 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+专业规则应先成为读者可用规则` | `1 0 0 0` | `∅` | `505 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+2.反例有线索不等于读者拥有解法` | `1 0 0 0` | `∅` | `629 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+3.差异不同子类型需要不同公平契约` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+短篇杂志侦探` | `1 0 0 0` | `∅` | `148 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+长篇证词多pov` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+封闭候选黄金时代式多假设` | `1 0 0 0` | `∅` | `152 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+科幻超自然非现实机制` | `1 0 0 0` | `∅` | `204 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/corpus-synthesis.md+4.不提升为p的内容` | `1 0 0 0` | `怎` | `413 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/evidence-design.md+f` | `1 0 0 0` | `∅` | `315 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/evidence-design.md+p` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/misdirection-frames.md+f` | `1 0 0 0` | `∅` | `421 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/misdirection-frames.md+p` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/misdirection-frames.md+边界` | `1 0 0 0` | `∅` | `293 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/misdirection-frames.md+最小审计` | `1 0 0 0` | `∅` | `229 / — / — / —` | `UNALIGNED?` |
| `PG223` | `1 0 0 0` | `∅` | `5406 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P4` | `1 0 0 0` | `∅` | `5406 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG583` | `1 0 0 0` | `∅` | `5406 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-clue-fairplay/references/source-index.md+使用边界` | `1 0 0 1` | `例` | `679 / — / — / —` | `SOURCE_ONLY;RENUMBERED?` |
| `mystery-clue-fairplay/references/structure-and-narration.md+f` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/structure-and-narration.md+p` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `301 / — / — / —` | `UNALIGNED?` |
| `mystery-clue-fairplay/references/version-and-provenance.md+历史污染处置` | `1 0 0 0` | `∅` | `458 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-clue-fairplay/references/version-and-provenance.md+证据语义` | `1 0 0 0` | `反适` | `301 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-clue-fairplay/references/version-and-provenance.md+现实专业事实边界` | `1 0 0 0` | `∅` | `300 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-clue-fairplay/references/version-and-provenance.md+许可` | `1 0 0 0` | `∅` | `307 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-clue-fairplay/references/version-and-provenance.md+验证边界` | `1 0 0 0` | `∅` | `206 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+0.一句话与边界` | `1 0 0 0` | `∅` | `623 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+1.触发负触发` | `1 0 0 0` | `例适` | `1172 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+2.输入缺一项就先问不要猜` | `1 0 0 0` | `∅` | `653 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+3.证据底座必须随产物一起声明` | `1 0 0 0` | `∅` | `1280 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `1256 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+5.执行步骤按顺序做不要跳` | `1 0 0 0` | `怎检` | `3811 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+5b.完整走查示例` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `P5` | `1 0 0 0` | `∅` | `1553 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `921 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/SKILL.md+9.红线` | `1 0 0 0` | `规` | `593 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规怎例` | `1759 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+输入` | `1 0 0 0` | `∅` | `302 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+步骤0契约承诺可解→全套做` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+步骤1物证路线选路线a量化` | `1 0 0 0` | `∅` | `496 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+步骤2三条线` | `1 0 0 0` | `∅` | `172 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+步骤7揭示前审计` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/examples/worked-example.md+输出四张表` | `1 0 0 0` | `∅` | `141 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/clue-identity-misdirection.md+r1′线索发现即描写判据＝"对读者可见"` | `1 0 0 0` | `规例检适` | `2373 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/clue-identity-misdirection.md+r2′识别链分级≥2条且≥1条不可临时改变` | `1 0 0 0` | `规检` | `2196 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/clue-identity-misdirection.md+r3′错误权威框架正当性来自方法论的不确定区间` | `1 0 0 0` | `规怎反检适` | `2244 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/clue-identity-misdirection.md+r9′多证人契约与盲区` | `1 0 0 0` | `规怎例检适` | `2178 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+r7′物证路线先声明二选一` | `1 0 0 0` | `规` | `173 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+路线a｜量化给"可复算的量"` | `1 0 0 0` | `∅` | `712 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+路线b｜经验社会经验与常识类比` | `1 0 0 0` | `∅` | `573 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+失效条件本批新证据必须写进设计文档` | `1 0 0 0` | `∅` | `666 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+操作排序本批最有用的一条` | `1 0 0 0` | `∅` | `328 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+r6′作案窗口三类窗口解释"没人看见"不解释"谁做的"` | `1 0 0 0` | `∅` | `984 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+时间与不在场证明` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+时间伪造的两种用途先声明再写` | `1 0 0 0` | `∅` | `571 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+把口头线索升级为书面可核` | `1 0 0 0` | `∅` | `265 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+不在场证明的量化与误判来源` | `1 0 0 0` | `∅` | `307 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+时间锚的读者可核对` | `1 0 0 0` | `∅` | `189 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+r8′封闭名单+等权怀疑+不得因身份豁免` | `1 0 0 0` | `怎例` | `2059 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+r10′副文本可承担谜题与核对工具但不得点名凶手` | `1 0 0 0` | `∅` | `811 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md+r11′程序是决策不是压力` | `1 0 0 0` | `规反检` | `2106 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+1.定罪缺口检查p5本skill独有必做` | `1 0 0 0` | `检` | `1472 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+2.密室与不可能犯罪三种解法互不通用` | `1 0 0 0` | `∅` | `115 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+解法a｜机关未被启动／被误用` | `1 0 0 0` | `∅` | `695 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+解法b｜身份错位` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+解法c｜解答完成但需另设陷阱取证` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+密室条件的铺设空间即条件` | `1 0 0 0` | `反` | `983 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+3.揭晓形式五种选一种并匹配契约` | `1 0 0 0` | `∅` | `709 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+4.r12特殊能力与"非公平"标注` | `1 0 0 0` | `规例` | `1402 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+5.明确保留的冲突不得伪造共识` | `1 0 0 0` | `∅` | `1100 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md+6.反模式速查本批确实出现的` | `1 0 0 0` | `∅` | `1301 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/rule-adjudication.md+裁决汇总` | `1 0 0 0` | `∅` | `381 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/rule-adjudication.md+revise明细改什么为什么` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/rule-adjudication.md+reject6→允许"有意悬空"` | `1 0 0 0` | `反适` | `351 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/rule-adjudication.md+keep明细本批新证据` | `1 0 0 0` | `∅` | `1766 / — / — / —` | `UNALIGNED?` |
| `mystery-detection-craft-b04/references/rule-adjudication.md+notproven明细` | `1 0 0 0` | `∅` | `465 / — / — / —` | `UNALIGNED?` |
| `A-04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A-03` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detection-craft-b04/references/source-index-and-evidence-tiers.md+1.三档证据等级引用前必看` | `1 0 0 0` | `∅` | `815 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detection-craft-b04/references/source-index-and-evidence-tiers.md+2.29本来源索引族去重后23族` | `1 0 0 0` | `∅` | `4607 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detection-craft-b04/references/source-index-and-evidence-tiers.md+3.本批未验证项` | `1 0 0 0` | `∅` | `462 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+返工后的强制证据叙事决策优先` | `1 0 0 0` | `∅` | `509 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+输入权限何时可用不可用` | `1 0 0 0` | `∅` | `605 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+快速决策表先选型再查规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+表1灵异因果的最终兑现三档谜面可以误导最终解释须自洽` | `1 0 0 0` | `∅` | `403 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+表2核心诡计选型按谜面选族` | `1 0 0 0` | `∅` | `593 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+表3动机与伦理风险选型“同情度”不作客观评分` | `1 0 0 0` | `∅` | `362 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+表4结案方式选型` | `1 0 0 0` | `∅` | `347 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+触发与负触发` | `1 0 0 0` | `∅` | `563 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+分支路由按任务类型` | `1 0 0 0` | `∅` | `715 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+输出契约` | `1 0 0 0` | `规` | `321 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+失败出口` | `1 0 0 0` | `规例` | `584 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/SKILL.md+文件路由` | `1 0 0 0` | `∅` | `1040 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `184 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+1.灵异档位不可混档硬约束` | `1 0 0 0` | `∅` | `532 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+2."民间侦探抓捕"的程序越界` | `1 0 0 0` | `∅` | `502 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+3.天罚收束的巧合红线` | `1 0 0 0` | `∅` | `358 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+4.目击反推的适用边界` | `1 0 0 0` | `∅` | `238 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+5.时代偏见不迁移硬约束` | `1 0 0 0` | `∅` | `434 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+6.单源规则清单引用时必须标注单源` | `1 0 0 0` | `∅` | `539 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/counterexamples.md+7.结构性失效形态对照速查` | `1 0 0 0` | `∅` | `502 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/examples.md+示例1规划型为一部1908年伦敦背景长篇设计核心谜题` | `1 0 0 0` | `规` | `2219 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/examples.md+示例2诊断型"中段塌陷"修法` | `1 0 0 0` | `败` | `1428 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/failure-modes.md+诊断六问对任何"没劲的推理稿"逐问` | `1 0 0 0` | `∅` | `899 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/failure-modes.md+六类类型病与修法索引` | `1 0 0 0` | `∅` | `886 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/failure-modes.md+失败出口按序执行` | `1 0 0 0` | `∅` | `1125 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/atmosphere-and-cast.md+p族灵异与伪超自然真伪光谱` | `1 0 0 0` | `规` | `453 / — / — / —` | `UNALIGNED?` |
| `P1` | `1 0 0 0` | `怎` | `638 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `怎` | `489 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `怎` | `389 / — / — / —` | `UNALIGNED?` |
| `P6` | `1 0 0 0` | `怎` | `327 / — / — / —` | `UNALIGNED?` |
| `P7` | `1 0 0 0` | `怎` | `527 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/atmosphere-and-cast.md+q族女性角色功能谱系` | `1 0 0 0` | `∅` | `244 / — / — / —` | `UNALIGNED?` |
| `Q1` | `1 0 0 0` | `怎` | `578 / — / — / —` | `UNALIGNED?` |
| `Q2` | `1 0 0 0` | `怎` | `433 / — / — / —` | `UNALIGNED?` |
| `Q3` | `1 0 0 0` | `怎` | `493 / — / — / —` | `UNALIGNED?` |
| `Q4` | `1 0 0 0` | `怎` | `417 / — / — / —` | `UNALIGNED?` |
| `Q5` | `1 0 0 0` | `怎` | `353 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/atmosphere-and-cast.md+r族藏匿与逃亡` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/atmosphere-and-cast.md+s族情感线与收束` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `S1` | `1 0 0 0` | `怎` | `368 / — / — / —` | `UNALIGNED?` |
| `S2` | `1 0 0 0` | `怎` | `387 / — / — / —` | `UNALIGNED?` |
| `S3` | `1 0 0 0` | `怎` | `420 / — / — / —` | `UNALIGNED?` |
| `S4` | `1 0 0 0` | `怎` | `461 / — / — / —` | `UNALIGNED?` |
| `S5` | `1 0 0 0` | `怎` | `485 / — / — / —` | `UNALIGNED?` |
| `S6` | `1 0 0 0` | `怎` | `409 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/detection-and-process.md+i族侦探方法论` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `I1` | `1 0 0 0` | `怎` | `486 / — / — / —` | `UNALIGNED?` |
| `I2` | `1 0 0 0` | `怎` | `596 / — / — / —` | `UNALIGNED?` |
| `I3` | `1 0 0 0` | `怎` | `417 / — / — / —` | `UNALIGNED?` |
| `I4` | `1 0 0 0` | `怎` | `439 / — / — / —` | `UNALIGNED?` |
| `I5` | `1 0 0 0` | `怎反` | `507 / — / — / —` | `UNALIGNED?` |
| `I6` | `1 0 0 0` | `怎` | `529 / — / — / —` | `UNALIGNED?` |
| `I7` | `1 0 0 0` | `怎` | `382 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/detection-and-process.md+j族程序与收网` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `J1` | `1 0 0 0` | `怎` | `667 / — / — / —` | `UNALIGNED?` |
| `J2` | `1 0 0 0` | `怎` | `429 / — / — / —` | `UNALIGNED?` |
| `J3` | `1 0 0 0` | `怎` | `610 / — / — / —` | `UNALIGNED?` |
| `J4` | `1 0 0 0` | `怎` | `403 / — / — / —` | `UNALIGNED?` |
| `J5` | `1 0 0 0` | `怎` | `577 / — / — / —` | `UNALIGNED?` |
| `J6` | `1 0 0 0` | `怎` | `420 / — / — / —` | `UNALIGNED?` |
| `J7` | `1 0 0 0` | `怎` | `437 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/detection-and-process.md+k族媒体与信息生态` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `K1` | `1 0 0 0` | `怎` | `491 / — / — / —` | `UNALIGNED?` |
| `K2` | `1 0 0 0` | `怎` | `448 / — / — / —` | `UNALIGNED?` |
| `K3` | `1 0 0 0` | `怎` | `462 / — / — / —` | `UNALIGNED?` |
| `K4` | `1 0 0 0` | `怎` | `419 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/examples.md+示例a设计“证言与钟声不同步”的虚构谜题` | `1 0 0 0` | `怎败` | `821 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/examples.md+示例b诊断三次重复讯问` | `1 0 0 0` | `适` | `542 / — / — / —` | `UNALIGNED?` |
| `B05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `A-05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/failure-modes.md+入口与输入` | `1 0 0 0` | `∅` | `338 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/failure-modes.md+六类诊断逐格填写不可跳到“诡计库”代替推理` | `1 0 0 0` | `∅` | `1639 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/failure-modes.md+紧凑的证据公平性测试` | `1 0 0 0` | `∅` | `641 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/failure-modes.md+参考对抗案例均是合成输入不是读者实测` | `1 0 0 0` | `例` | `809 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/failure-modes.md+来源性质` | `1 0 0 0` | `∅` | `227 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `91 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `76 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/references/historical-provenance.md+历史freeze.md旧产物` | `1 0 0 0` | `∅` | `163 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/references/identity-and-mastermind.md+f族身份诡计与顶替` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `F1` | `1 0 0 0` | `怎` | `621 / — / — / —` | `UNALIGNED?` |
| `F2` | `1 0 0 0` | `怎` | `563 / — / — / —` | `UNALIGNED?` |
| `F3` | `1 0 0 0` | `怎` | `508 / — / — / —` | `UNALIGNED?` |
| `F4` | `1 0 0 0` | `怎` | `471 / — / — / —` | `UNALIGNED?` |
| `F5` | `1 0 0 0` | `怎` | `592 / — / — / —` | `UNALIGNED?` |
| `F6` | `1 0 0 0` | `怎` | `501 / — / — / —` | `UNALIGNED?` |
| `F7` | `1 0 0 0` | `怎` | `560 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/identity-and-mastermind.md+g族反派伪装与反侦查` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `G4` | `1 0 0 0` | `怎` | `459 / — / — / —` | `UNALIGNED?` |
| `G5` | `1 0 0 0` | `怎` | `514 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/identity-and-mastermind.md+h族布局者与智力收网` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `H1` | `1 0 0 0` | `怎` | `430 / — / — / —` | `UNALIGNED?` |
| `H2` | `1 0 0 0` | `怎` | `534 / — / — / —` | `UNALIGNED?` |
| `H3` | `1 0 0 0` | `怎` | `512 / — / — / —` | `UNALIGNED?` |
| `H4` | `1 0 0 0` | `怎` | `418 / — / — / —` | `UNALIGNED?` |
| `H5` | `1 0 0 0` | `怎` | `452 / — / — / —` | `UNALIGNED?` |
| `H6` | `1 0 0 0` | `怎适` | `486 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/impossible-crime.md+a族密室与不可能现场` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/impossible-crime.md+b族凶器物证与法证毒杀` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `怎` | `665 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `怎` | `531 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `怎` | `369 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `怎` | `527 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `怎` | `612 / — / — / —` | `UNALIGNED?` |
| `B6` | `1 0 0 0` | `怎` | `633 / — / — / —` | `UNALIGNED?` |
| `B7` | `1 0 0 0` | `怎` | `546 / — / — / —` | `UNALIGNED?` |
| `B8` | `1 0 0 0` | `规怎` | `529 / — / — / —` | `UNALIGNED?` |
| `B9` | `1 0 0 0` | `怎` | `513 / — / — / —` | `UNALIGNED?` |
| `B10` | `1 0 0 0` | `怎` | `551 / — / — / —` | `UNALIGNED?` |
| `B11` | `1 0 0 0` | `怎` | `548 / — / — / —` | `UNALIGNED?` |
| `B12` | `1 0 0 0` | `怎适` | `566 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/motive-and-justice.md+l族经济与家庭动机` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `L1` | `1 0 0 0` | `怎适` | `569 / — / — / —` | `UNALIGNED?` |
| `L2` | `1 0 0 0` | `怎` | `559 / — / — / —` | `UNALIGNED?` |
| `L3` | `1 0 0 0` | `怎适` | `518 / — / — / —` | `UNALIGNED?` |
| `L4` | `1 0 0 0` | `怎` | `400 / — / — / —` | `UNALIGNED?` |
| `L5` | `1 0 0 0` | `怎` | `475 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/motive-and-justice.md+m族复仇与私了` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M1` | `1 0 0 0` | `怎` | `508 / — / — / —` | `UNALIGNED?` |
| `M2` | `1 0 0 0` | `怎` | `707 / — / — / —` | `UNALIGNED?` |
| `M3` | `1 0 0 0` | `规怎` | `487 / — / — / —` | `UNALIGNED?` |
| `M4` | `1 0 0 0` | `怎` | `456 / — / — / —` | `UNALIGNED?` |
| `M5` | `1 0 0 0` | `怎` | `489 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `怎` | `543 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/motive-and-justice.md+n族赌局竞技罪案` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `N1` | `1 0 0 0` | `怎` | `480 / — / — / —` | `UNALIGNED?` |
| `N2` | `1 0 0 0` | `怎` | `470 / — / — / —` | `UNALIGNED?` |
| `N3` | `1 0 0 0` | `怎` | `552 / — / — / —` | `UNALIGNED?` |
| `N4` | `1 0 0 0` | `怎` | `426 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/motive-and-justice.md+o族罪案结构句法` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `O1` | `1 0 0 0` | `怎` | `474 / — / — / —` | `UNALIGNED?` |
| `O2` | `1 0 0 0` | `怎` | `449 / — / — / —` | `UNALIGNED?` |
| `O3` | `1 0 0 0` | `规怎` | `491 / — / — / —` | `UNALIGNED?` |
| `O4` | `1 0 0 0` | `怎` | `430 / — / — / —` | `UNALIGNED?` |
| `O5` | `1 0 0 0` | `怎例` | `514 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/source-index.md+代表性可核验原文定位` | `1 0 0 0` | `∅` | `933 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/references/source-index.md+可迁移边界` | `1 0 0 0` | `∅` | `253 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/references/timeline-and-evidence.md+c族时间与不在场证明` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `怎` | `403 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `怎` | `540 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/timeline-and-evidence.md+d族匿名信与通讯操纵` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `D1` | `1 0 0 0` | `怎` | `600 / — / — / —` | `UNALIGNED?` |
| `D2` | `1 0 0 0` | `怎` | `401 / — / — / —` | `UNALIGNED?` |
| `D3` | `1 0 0 0` | `怎` | `578 / — / — / —` | `UNALIGNED?` |
| `D4` | `1 0 0 0` | `怎` | `487 / — / — / —` | `UNALIGNED?` |
| `D5` | `1 0 0 0` | `怎` | `567 / — / — / —` | `UNALIGNED?` |
| `mystery-detective-plot-forge/references/timeline-and-evidence.md+e族目击与证人操纵` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `怎` | `496 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `怎例` | `450 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `怎` | `560 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `怎` | `504 / — / — / —` | `UNALIGNED?` |
| `E5` | `1 0 0 0` | `怎` | `579 / — / — / —` | `UNALIGNED?` |
| `E6` | `1 0 0 0` | `怎` | `516 / — / — / —` | `UNALIGNED?` |
| `PG170` | `1 0 0 0` | `∅` | `235 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG204` | `1 0 0 0` | `∅` | `166 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG244` | `1 0 0 0` | `∅` | `141 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG330` | `1 0 0 0` | `∅` | `131 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG434` | `1 0 0 0` | `∅` | `147 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/sources-index.md+阅读覆盖声明` | `1 0 0 0` | `∅` | `589 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-detective-plot-forge/sources-index.md+时代与语域声明` | `1 0 0 0` | `∅` | `409 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+1.触发负触发` | `1 0 0 0` | `检` | `1009 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+2.输入先收齐缺一项就问一项` | `1 0 0 0` | `∅` | `789 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+3.任务路由读哪份reference` | `1 0 0 0` | `∅` | `1472 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+4.执行步骤按顺序不要跳` | `1 0 0 0` | `∅` | `953 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+5.适用边界写在动手之前` | `1 0 0 0` | `规` | `1024 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+6.输出合同每次交付固定六段` | `1 0 0 0` | `∅` | `657 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+7.失败出口` | `1 0 0 0` | `例检适` | `718 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/SKILL.md+8.元信息保留与迁移勿删` | `1 0 0 0` | `∅` | `1175 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规反检适` | `1553 / — / — / —` | `UNALIGNED?` |
| `L6` | `1 0 0 0` | `∅` | `544 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md+1.各规则的失效速查` | `1 0 0 0` | `∅` | `2652 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md+2.明确被拒的候选不要在建议里复活` | `1 0 0 0` | `∅` | `1196 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md+3.未证明notproven不要写成规则` | `1 0 0 0` | `怎` | `597 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md+4.四处保留的冲突不做调和` | `1 0 0 0` | `∅` | `873 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md+5.时代与体裁边界写作前先确认` | `1 0 0 0` | `∅` | `794 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+样例一｜设计乡村宅邸密室割喉第一发现人是护士` | `1 0 0 0` | `∅` | `276 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+1.判定` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+2.检查清单结果` | `1 0 0 0` | `∅` | `1209 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+3.改写方案按优先级` | `1 0 0 0` | `∅` | `667 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+4.来源锚点` | `1 0 0 0` | `∅` | `319 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+5.风险与反例` | `1 0 0 0` | `∅` | `465 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+6.未决项` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+样例二｜修改第一人称助手叙述读者说"早就猜到凶手"` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/examples.md+3.改写方案` | `1 0 0 0` | `∅` | `813 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§a现场与时序` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§b时间锚` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§c密室与无侵入` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§d死因定性自杀事故他杀` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§e毒物` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§f证词与视角` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§g物证` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `mystery-evidence-chain-designer/references/rules-core.md+§h对手异常与失败` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `PG155` | `1 0 0 0` | `∅` | `7882 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-evidence-chain-designer/references/source-ledger.md+2.按技法族查书跨书规则按"族"计权重不按"本"计` | `1 0 0 0` | `∅` | `627 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `mystery-evidence-chain-designer/references/source-ledger.md+3.覆盖与核验` | `1 0 0 0` | `∅` | `546 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 02 言情（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 02 言情

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`courtship-conflict-craft`、`romance-craft-b03-b07`、`romance-craft-b06`、`romance-emotional-arc`、`romance-obstacle-and-cost`、`romance-obstacle-delay-craft`、`romance-social-cost-craft`

**规则单元数 430；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 430（100.0%）**
**flag 计数**：SOURCE_ONLY=49；UNALIGNED?=430

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `courtship-conflict-craft/SKILL.md+1.这是什么能力边界` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+2.证据底座先读再决定信多少` | `1 0 0 0` | `∅` | `1058 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+3.触发负触发` | `1 0 0 0` | `∅` | `940 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+4.需要的输入缺什么先问什么` | `1 0 0 0` | `∅` | `584 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+5.最短判断路径五个门按顺序过` | `1 0 0 0` | `∅` | `1625 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+6.执行步骤7步逐项落表` | `1 0 0 0` | `∅` | `1446 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+7.输出合同` | `1 0 0 0` | `∅` | `936 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `929 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+9.任务路由首读补读交付` | `1 0 0 0` | `∅` | `1292 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+10.硬边界不得违反` | `1 0 0 0` | `规` | `539 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+11.文件地图与自检` | `1 0 0 0` | `适` | `1002 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/SKILL.md+12.变更记录本轮roundp4final20261030` | `1 0 0 0` | `适` | `739 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/examples/worked-example.md+示例a保留婚姻与土地申诉不能互相替代` | `1 0 0 0` | `∅` | `1377 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/examples/worked-example.md+示例b本轮新增当争议受理方不中立把"澄清"换成"让有权的人亲耳听到"` | `1 0 0 0` | `∅` | `2621 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/examples/worked-example.md+缺料版两个示例共用` | `1 0 0 0` | `∅` | `624 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `反` | `2142 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `反` | `1573 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `反` | `1044 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `反` | `1328 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `反` | `1450 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `反` | `1271 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/references/01-courtship-engines.md+具体回归检查` | `1 0 0 0` | `∅` | `529 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `反` | `1839 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `反` | `1873 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `例反` | `1349 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/references/02-settlement-and-closure.md+互相排斥的结局分支` | `1 0 0 0` | `∅` | `959 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `反` | `928 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/references/03-derivative-and-formats.md+版权与责任声明与工艺分开` | `1 0 0 0` | `∅` | `486 / — / — / —` | `UNALIGNED?` |
| `courtship-conflict-craft/references/03-derivative-and-formats.md+分卷诊断表` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `PG524` | `1 0 0 0` | `∅` | `2357 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG158` | `1 0 0 0` | `∅` | `2357 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG619` | `1 0 0 0` | `∅` | `2357 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/04-source-index.md+证据族去重19本≠19个独立证据` | `1 0 0 0` | `∅` | `709 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/04-source-index.md+重点规则引用定位` | `1 0 0 0` | `例` | `1154 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/04-source-index.md+阅读与授权边界` | `1 0 0 0` | `∅` | `794 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md+1.逐条裁决含本轮roundp4final的复议` | `1 0 0 0` | `∅` | `3899 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md+2.新旧关系与否决理由` | `1 0 0 0` | `∅` | `925 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md+3.信息反例与缺料检查` | `1 0 0 0` | `例适` | `746 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md+4.本轮保留的未决冲突不伪造共识` | `1 0 0 0` | `∅` | `735 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md+5.证据等级与使用限制` | `1 0 0 0` | `∅` | `659 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+0.这个skill的证据边界先读再决定要不要用` | `1 0 0 0` | `∅` | `669 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+1.触发负触发` | `1 0 0 0` | `规` | `899 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+2.输入合同缺什么先问什么` | `1 0 0 0` | `∅` | `574 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `461 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+4.执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `P1` | `1 0 0 0` | `∅` | `402 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `∅` | `823 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `1199 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+步骤4信息差必须握在有权改变它的人手里` | `1 0 0 0` | `∅` | `368 / — / — / —` | `UNALIGNED?` |
| `P4` | `1 0 0 0` | `∅` | `475 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+步骤6结局在三种形态里显式选一种不选默认` | `1 0 0 0` | `∅` | `766 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+5.输出合同` | `1 0 0 0` | `∅` | `744 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+6.反面清单本批证伪的约定` | `1 0 0 0` | `∅` | `661 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+7.失败出口` | `1 0 0 0` | `例适` | `762 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/SKILL.md+8.参考文件按需加载不要一次全读` | `1 0 0 0` | `∅` | `586 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `3991 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+一四个刻意保留的冲突` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+冲突1牺牲是高尚还是控制` | `1 0 0 0` | `∅` | `813 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+冲突2中间人促成了好事还是造成了伤害` | `1 0 0 0` | `∅` | `540 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+冲突3结局要不要交代所有人` | `1 0 0 0` | `∅` | `609 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+冲突4欺骗的代价何时到` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+二反面清单本批证伪的六条通用约定` | `1 0 0 0` | `∅` | `934 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+三替代规则用来替换被reject的约定` | `1 0 0 0` | `∅` | `603 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md+四notproven清单不要回答直接声明` | `1 0 0 0` | `规` | `370 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/evidence-index.md+skill.md→行号映射` | `1 0 0 0` | `∅` | `2802 / — / — / —` | `UNALIGNED?` |
| `PG805` | `1 0 0 0` | `∅` | `1736 / — / — / —` | `UNALIGNED?` |
| `PG177` | `1 0 0 0` | `∅` | `1736 / — / — / —` | `UNALIGNED?` |
| `PG700` | `1 0 0 0` | `∅` | `1736 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+一阻挡力清单至少配两条一条外部一条内在` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+外部阻挡力制度身份家族法律` | `1 0 0 0` | `∅` | `620 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+内在阻挡力主角自身的取舍性格自我评估` | `1 0 0 0` | `∅` | `723 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+反对者必须自洽` | `1 0 0 0` | `∅` | `555 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+二追求场景两种开场都是可选` | `1 0 0 0` | `∅` | `481 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+三拒绝场景三层输出` | `1 0 0 0` | `∅` | `55 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+第1层礼节层拒绝先从礼节做起不先谈感情` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+第2层理由层给出可检验的标准不是"我感觉不合适"` | `1 0 0 0` | `∅` | `209 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+第3层动机自陈层拒绝者承认自己也不干净` | `1 0 0 0` | `∅` | `184 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+可直接复用的两个动作` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+四追问这条拒绝成立吗` | `1 0 0 0` | `∅` | `310 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md+五信息差必须握在有权改变它的人手里` | `1 0 0 0` | `∅` | `664 / — / — / —` | `UNALIGNED?` |
| `B-07` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B-05` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B07` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B-03` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B-04` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B-06` | `1 0 0 0` | `∅` | `4520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-craft-b03-b07/references/source-roles-b03b07.md+三条使用禁令` | `1 0 0 0` | `∅` | `593 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P6` | `1 0 0 0` | `∅` | `736 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+0.输入权限与边界` | `1 0 0 0` | `规` | `1083 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+1.主轴判定写作前3问` | `1 0 0 0` | `∅` | `765 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+2.快速决策表选型` | `1 0 0 0` | `∅` | `1231 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+3.规则族正文` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R01` | `1 0 0 0` | `规怎例适` | `2227 / — / — / —` | `UNALIGNED?` |
| `R02` | `1 0 0 0` | `规怎例适` | `1273 / — / — / —` | `UNALIGNED?` |
| `R03` | `1 0 0 0` | `规怎适` | `1209 / — / — / —` | `UNALIGNED?` |
| `R04` | `1 0 0 0` | `规怎适` | `1222 / — / — / —` | `UNALIGNED?` |
| `R05` | `1 0 0 0` | `规怎适` | `1088 / — / — / —` | `UNALIGNED?` |
| `R06` | `1 0 0 0` | `规怎适` | `962 / — / — / —` | `UNALIGNED?` |
| `R07` | `1 0 0 0` | `规怎适` | `1002 / — / — / —` | `UNALIGNED?` |
| `R08` | `1 0 0 0` | `规怎适` | `955 / — / — / —` | `UNALIGNED?` |
| `R09` | `1 0 0 0` | `规怎适` | `954 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `规怎适` | `1652 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `规怎适` | `1074 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `规怎适` | `1111 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `规怎例检适` | `1628 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `规怎适` | `1509 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `规怎例适` | `1268 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+4.反例与失败出口` | `1 0 0 0` | `规` | `866 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+5.references导航` | `1 0 0 0` | `∅` | `959 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+6.覆盖与限制必读` | `1 0 0 0` | `例` | `917 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/SKILL.md+7.溯源` | `1 0 0 0` | `规` | `398 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `155 / — / — / —` | `UNALIGNED?` |
| `CE-01` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `CE-02` | `1 0 0 0` | `∅` | `127 / — / — / —` | `UNALIGNED?` |
| `CE-03` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `CE-04` | `1 0 0 0` | `∅` | `104 / — / — / —` | `UNALIGNED?` |
| `CE-05` | `1 0 0 0` | `∅` | `122 / — / — / —` | `UNALIGNED?` |
| `CE-06` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `CE-07` | `1 0 0 0` | `∅` | `81 / — / — / —` | `UNALIGNED?` |
| `CE-08` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `CE-09` | `1 0 0 0` | `∅` | `155 / — / — / —` | `UNALIGNED?` |
| `CE-10` | `1 0 0 0` | `∅` | `111 / — / — / —` | `UNALIGNED?` |
| `CE-11` | `1 0 0 0` | `∅` | `122 / — / — / —` | `UNALIGNED?` |
| `CE-12` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `CE-13` | `1 0 0 0` | `∅` | `173 / — / — / —` | `UNALIGNED?` |
| `CE-14` | `1 0 0 0` | `∅` | `140 / — / — / —` | `UNALIGNED?` |
| `CE-15` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `CE-16` | `1 0 0 0` | `∅` | `121 / — / — / —` | `UNALIGNED?` |
| `CE-17` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `CE-18` | `1 0 0 0` | `∅` | `130 / — / — / —` | `UNALIGNED?` |
| `CE-19` | `1 0 0 0` | `∅` | `148 / — / — / —` | `UNALIGNED?` |
| `CE-20` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `CE-21` | `1 0 0 0` | `∅` | `137 / — / — / —` | `UNALIGNED?` |
| `CE-22` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/counterexamples.md+一价值不可迁移只登记禁止采纳` | `1 0 0 0` | `∅` | `3123 / — / — / —` | `UNALIGNED?` |
| `CE-23` | `1 0 0 0` | `∅` | `139 / — / — / —` | `UNALIGNED?` |
| `CE-24` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `CE-25` | `1 0 0 0` | `∅` | `150 / — / — / —` | `UNALIGNED?` |
| `CE-26` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `CE-27` | `1 0 0 0` | `∅` | `189 / — / — / —` | `UNALIGNED?` |
| `CE-28` | `1 0 0 0` | `∅` | `207 / — / — / —` | `UNALIGNED?` |
| `CE-29` | `1 0 0 0` | `∅` | `132 / — / — / —` | `UNALIGNED?` |
| `CE-30` | `1 0 0 0` | `∅` | `183 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/counterexamples.md+二技法有效但代价过高慎用` | `1 0 0 0` | `∅` | `1339 / — / — / —` | `UNALIGNED?` |
| `CE-31` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `CE-32` | `1 0 0 0` | `∅` | `140 / — / — / —` | `UNALIGNED?` |
| `CE-33` | `1 0 0 0` | `∅` | `117 / — / — / —` | `UNALIGNED?` |
| `CE-34` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `CE-35` | `1 0 0 0` | `∅` | `129 / — / — / —` | `UNALIGNED?` |
| `CE-36` | `1 0 0 0` | `∅` | `136 / — / — / —` | `UNALIGNED?` |
| `CE-37` | `1 0 0 0` | `∅` | `202 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/counterexamples.md+三技法本身失败反面教材` | `1 0 0 0` | `∅` | `1139 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/counterexamples.md+四同族降权说明` | `1 0 0 0` | `∅` | `643 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/examples.md+使用说明` | `1 0 0 0` | `规` | `488 / — / — / —` | `UNALIGNED?` |
| `FM01` | `1 0 0 0` | `∅` | `183 / — / — / —` | `UNALIGNED?` |
| `FM02` | `1 0 0 0` | `∅` | `212 / — / — / —` | `UNALIGNED?` |
| `FM03` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `FM04` | `1 0 0 0` | `∅` | `213 / — / — / —` | `UNALIGNED?` |
| `FM05` | `1 0 0 0` | `∅` | `154 / — / — / —` | `UNALIGNED?` |
| `FM06` | `1 0 0 0` | `∅` | `202 / — / — / —` | `UNALIGNED?` |
| `FM07` | `1 0 0 0` | `∅` | `195 / — / — / —` | `UNALIGNED?` |
| `FM08` | `1 0 0 0` | `∅` | `152 / — / — / —` | `UNALIGNED?` |
| `FM09` | `1 0 0 0` | `∅` | `175 / — / — / —` | `UNALIGNED?` |
| `FM10` | `1 0 0 0` | `∅` | `173 / — / — / —` | `UNALIGNED?` |
| `FM11` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `FM12` | `1 0 0 0` | `∅` | `182 / — / — / —` | `UNALIGNED?` |
| `FM13` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `FM14` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `FM15` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `FM16` | `1 0 0 0` | `∅` | `183 / — / — / —` | `UNALIGNED?` |
| `FM17` | `1 0 0 0` | `∅` | `223 / — / — / —` | `UNALIGNED?` |
| `FM18` | `1 0 0 0` | `∅` | `254 / — / — / —` | `UNALIGNED?` |
| `FM19` | `1 0 0 0` | `∅` | `219 / — / — / —` | `UNALIGNED?` |
| `FM20` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/failure-modes.md+返工顺序建议` | `1 0 0 0` | `∅` | `329 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/failure-modes.md+不可修复项应放弃而非修补` | `1 0 0 0` | `规` | `369 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.五型相遇的完整参数` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.1拾物型` | `1 0 0 0` | `∅` | `791 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.2羞辱型` | `1 0 0 0` | `例` | `774 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.3窥见型` | `1 0 0 0` | `例` | `561 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.4共读型` | `1 0 0 0` | `∅` | `666 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+1.5"我认识你"型` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+2.场景检查清单写完自检` | `1 0 0 0` | `∅` | `522 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+3.障碍地图模板` | `1 0 0 0` | `∅` | `354 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+3.1空间障碍的四种强度` | `1 0 0 0` | `∅` | `606 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+4.1三级信息差身世继承型` | `1 0 0 0` | `∅` | `453 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md+5.锚点表` | `1 0 0 0` | `∅` | `1354 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+1.物件信号选择与回收` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+1.1四种可用的信号物` | `1 0 0 0` | `∅` | `680 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+1.2回收规则` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+1.3珍珠眼泪型信物` | `1 0 0 0` | `怎` | `334 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+2.延迟装置让延迟有真实约束或人物边界` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+2.1五种可信延迟` | `1 0 0 0` | `∅` | `769 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+2.2不可信延迟失败出口` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+3.情感节拍表可直接套用` | `1 0 0 0` | `∅` | `1224 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+4.一封信的物理旅程模板` | `1 0 0 0` | `∅` | `631 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r2-beats-and-delay.md+5.锚点表` | `1 0 0 0` | `∅` | `1030 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+1.阶层财产阻力资源身份与制度三种观察面` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+1.1数字可见化仅当金额真的改变选择` | `1 0 0 0` | `∅` | `401 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+1.2命令化` | `1 0 0 0` | `∅` | `371 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+1.3出身血统` | `1 0 0 0` | `∅` | `527 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+2.家族执行者资源条件清单` | `1 0 0 0` | `∅` | `743 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+2.1写法顺序` | `1 0 0 0` | `∅` | `467 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+3.身份过去风险三种历史样本与现代边界` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+3.1身世羞耻` | `1 0 0 0` | `规` | `231 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+3.2恩情混淆` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+3.3疾病过去` | `1 0 0 0` | `∅` | `250 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+4.竞争者历史样本与独立目标` | `1 0 0 0` | `∅` | `577 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+4.1三角检查` | `1 0 0 0` | `∅` | `403 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+5.舆论与嫉妒四级升级` | `1 0 0 0` | `∅` | `693 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+5.1写作规则` | `1 0 0 0` | `∅` | `341 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+6.资源婚配契约场景模板仅在制度交易真实存在时` | `1 0 0 0` | `∅` | `700 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r3-rivals-and-market.md+7.锚点表` | `1 0 0 0` | `∅` | `1595 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.告白与承诺先判同意状态再选形式` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.1私密低声型` | `1 0 0 0` | `∅` | `318 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.2压迫式长篇告白作为冲突反例读取` | `1 0 0 0` | `∅` | `348 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.3权力差问答不得把职位变成同意` | `1 0 0 0` | `检` | `352 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.4书信异地型` | `1 0 0 0` | `∅` | `293 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+1.5形式意图错位型` | `1 0 0 0` | `∅` | `446 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+2.形式意图与同意状态对照` | `1 0 0 0` | `∅` | `676 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+3.牺牲自污只在自主选择成立时使用` | `1 0 0 0` | `∅` | `842 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+4.结局不是婚配考试` | `1 0 0 0` | `∅` | `1129 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+4.1关系后的现实四个可选观察面` | `1 0 0 0` | `∅` | `453 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+5.反讽收尾的边界` | `1 0 0 0` | `败` | `483 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r4-confession-and-endings.md+6.锚点表` | `1 0 0 0` | `∅` | `1639 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.视角选择树按信息差不按性别` | `1 0 0 0` | `∅` | `427 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.1双视角并置` | `1 0 0 0` | `怎` | `288 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.2单方限知+读者多知` | `1 0 0 0` | `怎` | `376 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.3日记书信接笔` | `1 0 0 0` | `怎` | `284 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.4全知叙述者插话` | `1 0 0 0` | `怎` | `347 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+1.5第一人称“低承诺”` | `1 0 0 0` | `怎` | `231 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+2.内心戏服务选择不要求每段都改变行动` | `1 0 0 0` | `∅` | `429 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+2.1内心戏检查` | `1 0 0 0` | `∅` | `300 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+3.照护疾病接触不是同意照护不是债务` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+3.1照护场景` | `1 0 0 0` | `适` | `500 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+3.2病弱残障精神异常第三方的主权` | `1 0 0 0` | `∅` | `303 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+4.职业经济自主不是求婚附加条款` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+4.1自主目标` | `1 0 0 0` | `∅` | `493 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+4.2职业作为尊严或冲突来源` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `romance-craft-b06/references/r5-pov-and-interiority.md+5.锚点表` | `1 0 0 0` | `∅` | `1272 / — / — / —` | `UNALIGNED?` |
| `PG121` | `1 0 0 0` | `∅` | `2011 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG544` | `1 0 0 0` | `∅` | `2011 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG141` | `1 0 0 0` | `∅` | `2011 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-craft-b06/sources-index.md+当前复核状态` | `1 0 0 0` | `∅` | `348 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+1.输入与判断` | `1 0 0 0` | `∅` | `946 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+2.执行流程` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+a.建立关系基线` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+b.选择真实阻力` | `1 0 0 0` | `∅` | `203 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+c.管理信息与接近` | `1 0 0 0` | `∅` | `213 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+d.让关系通过选择推进` | `1 0 0 0` | `∅` | `231 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+e.表达与确认` | `1 0 0 0` | `∅` | `191 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+f.结局与后果` | `1 0 0 0` | `∅` | `195 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+3.输出合同` | `1 0 0 0` | `例` | `571 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+4.规则导航` | `1 0 0 0` | `例` | `394 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/SKILL.md+5.失败出口` | `1 0 0 0` | `规适` | `643 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `165 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/examples/worked-example.md+输入` | `1 0 0 0` | `∅` | `256 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/examples/worked-example.md+先判关系状态` | `1 0 0 0` | `∅` | `454 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/examples/worked-example.md+两个都成立的结局` | `1 0 0 0` | `∅` | `370 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/examples/worked-example.md+冲突场景自检` | `1 0 0 0` | `∅` | `390 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/01-refusal-and-vow.md+f证据` | `1 0 0 0` | `∅` | `564 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/01-refusal-and-vow.md+h→p` | `1 0 0 0` | `例` | `231 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/01-refusal-and-vow.md+失效与反例` | `1 0 0 0` | `∅` | `325 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/01-refusal-and-vow.md+自检` | `1 0 0 0` | `例` | `393 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/02-obstacle-carriers.md+f证据` | `1 0 0 0` | `∅` | `509 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/02-obstacle-carriers.md+h→p` | `1 0 0 0` | `∅` | `260 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/02-obstacle-carriers.md+常见真实阻力` | `1 0 0 0` | `例` | `552 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/02-obstacle-carriers.md+失效` | `1 0 0 0` | `∅` | `271 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/03-reversal-and-vacancy.md+f证据` | `1 0 0 0` | `∅` | `467 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/03-reversal-and-vacancy.md+h→p` | `1 0 0 0` | `∅` | `319 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/03-reversal-and-vacancy.md+最小检查` | `1 0 0 0` | `∅` | `311 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/03-reversal-and-vacancy.md+失效` | `1 0 0 0` | `∅` | `295 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/04-confession-scenes.md+f与边界证据` | `1 0 0 0` | `∅` | `707 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/04-confession-scenes.md+f证据` | `1 0 0 0` | `∅` | `678 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/04-confession-scenes.md+h→p` | `1 0 0 0` | `∅` | `273 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/05-ending-and-cost.md+f证据` | `1 0 0 0` | `∅` | `1028 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/05-ending-and-cost.md+结局清单` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `romance-emotional-arc/references/05-ending-and-cost.md+红线与冲突裁决` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `418 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `243 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `∅` | `371 / — / — / —` | `UNALIGNED?` |
| `C6` | `1 0 0 0` | `∅` | `322 / — / — / —` | `UNALIGNED?` |
| `PG945` | `1 0 0 0` | `∅` | `3663 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG768` | `1 0 0 0` | `∅` | `3663 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG145` | `1 0 0 0` | `∅` | `3663 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG27` | `1 0 0 0` | `∅` | `3663 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-emotional-arc/references/source-index.md+使用边界` | `1 0 0 0` | `规例` | `528 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-emotional-arc/references/version-and-provenance.md+证据语义` | `1 0 0 0` | `规怎反适` | `375 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-emotional-arc/references/version-and-provenance.md+许可与引用` | `1 0 0 0` | `∅` | `357 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-emotional-arc/references/version-and-provenance.md+版本限制` | `1 0 0 0` | `∅` | `241 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+0.这是什么` | `1 0 0 0` | `规` | `441 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+1.证据底座诚实口径` | `1 0 0 0` | `适` | `1086 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+触发` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+负触发` | `1 0 0 0` | `例` | `366 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+3.明确输入缺什么就问什么不猜` | `1 0 0 0` | `∅` | `597 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `731 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+5.最短执行路径2个门` | `1 0 0 0` | `∅` | `995 / — / — / —` | `UNALIGNED?` |
| `O1` | `1 0 0 0` | `∅` | `143 / — / — / —` | `UNALIGNED?` |
| `O2` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `O3` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `O4` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `O5` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `175 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `S1` | `1 0 0 0` | `∅` | `156 / — / — / —` | `UNALIGNED?` |
| `S2` | `1 0 0 0` | `∅` | `166 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+6.规则索引10条canonical在各reference` | `1 0 0 0` | `∅` | `1703 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+7.两张最小模板` | `1 0 0 0` | `∅` | `377 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+8.禁止项` | `1 0 0 0` | `∅` | `730 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+9.失败出口` | `1 0 0 0` | `∅` | `667 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/SKILL.md+10.文件地图与自检` | `1 0 0 0` | `∅` | `804 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md+§1o1+o2障碍必须挂在"能解除它的人"名下+硬障碍五型` | `1 0 0 0` | `反` | `1988 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md+§2o4承诺的解除必须由持有人本人执行` | `1 0 0 0` | `反` | `1573 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md+§3o3持续延迟用硬障碍误会降级为一次性转折器` | `1 0 0 0` | `∅` | `1532 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md+§4o5误认型障碍要重写解释不要制造笑料` | `1 0 0 0` | `∅` | `835 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md+§5快速检查清单无稿时用` | `1 0 0 0` | `适` | `384 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+§1e1退让型结局=障碍清零→主动不动→一个可观察的小动作` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+fpg541theageofinnocence本批最完整的样本本轮实读l1126` | `1 0 0 0` | `∅` | `984 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+fpg283thereef退让想做成不可逆动作却落空` | `1 0 0 0` | `∅` | `405 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+fpg6688themillonthefloss退让写成焚信结局是死` | `1 0 0 0` | `∅` | `293 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+p` | `1 0 0 0` | `∅` | `470 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+§2e2代价账本结合不等于结算完成` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f三种代价` | `1 0 0 0` | `∅` | `738 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f"赢了但没付代价"在本批没有市场` | `1 0 0 0` | `∅` | `310 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+p代价账本三行结局前必须填完` | `1 0 0 0` | `∅` | `369 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+§3e3财产的方向由归属决定有反例冲突保留` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f断裂财产写在资格条款名下` | `1 0 0 0` | `∅` | `318 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f促成财产是拉平装置` | `1 0 0 0` | `∅` | `324 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f无碍贫穷不妨碍结合` | `1 0 0 0` | `∅` | `145 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f财产被当成择偶的全部理由本批的负面样本` | `1 0 0 0` | `∅` | `379 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+§4婚后线结合之后继续记账补充规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+f` | `1 0 0 0` | `∅` | `457 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+h` | `1 0 0 0` | `∅` | `82 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md+§5快速检查清单` | `1 0 0 0` | `适` | `476 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+§1s1舆论按"一句闲话→一次行动改变"的粒度工作` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `PG541` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `PG161` | `1 0 0 0` | `∅` | `127 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+f可计量的闲话不是氛围` | `1 0 0 0` | `∅` | `1396 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+f舆论的无力面反例别把舆论写成万能` | `1 0 0 0` | `∅` | `277 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+p闲话→行动对照表` | `1 0 0 0` | `∅` | `296 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+§2s2多视角同一事件每个视角必须有不同利害关系` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+fpg5066thewholefamily十二作者合集howells领衔` | `1 0 0 0` | `∅` | `445 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+p` | `1 0 0 0` | `∅` | `316 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+§3视角与内心戏的边界本批的有限证据` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+f` | `1 0 0 0` | `∅` | `586 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+h` | `1 0 0 0` | `∅` | `112 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md+§4快速检查清单` | `1 0 0 0` | `∅` | `349 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/04-source-index.md+1.任务与路径` | `1 0 0 0` | `∅` | `569 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG283` | `1 0 0 0` | `∅` | `3408 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-and-cost/references/04-source-index.md+3.族去重19本→15个独立来源族` | `1 0 0 0` | `∅` | `641 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-and-cost/references/04-source-index.md+4.覆盖与回源可复现` | `1 0 0 0` | `∅` | `763 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-and-cost/references/04-source-index.md+6.边界声明` | `1 0 0 0` | `∅` | `331 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+0.裁决对象从哪来` | `1 0 0 0` | `∅` | `582 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+1.逐条裁决` | `1 0 0 0` | `∅` | `3878 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+2.保留的三条冲突不伪造共识` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+冲突a财产是障碍还是解药` | `1 0 0 0` | `适` | `430 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+冲突b退让是美德还是损失` | `1 0 0 0` | `∅` | `482 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+冲突c训诫文本vs小说实践` | `1 0 0 0` | `规` | `387 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md+3.未解决notproven` | `1 0 0 0` | `∅` | `575 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+1.触发与负触发` | `1 0 0 0` | `规例适` | `1156 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+2.输入` | `1 0 0 0` | `∅` | `488 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1156 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+4.执行步骤` | `1 0 0 0` | `∅` | `1285 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+5.输出合同` | `1 0 0 0` | `∅` | `678 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+6.失败出口` | `1 0 0 0` | `规` | `1287 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/SKILL.md+7.证据边界必须随交付一起说明` | `1 0 0 0` | `检` | `508 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `2465 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/coercion-and-consent.md+f｜真实情节顺序ethelm.delltetherstonespg59181` | `1 0 0 0` | `∅` | `949 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/coercion-and-consent.md+h｜叙事解释不是现实法医法律结论` | `1 0 0 0` | `∅` | `484 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/coercion-and-consent.md+p｜创作检查` | `1 0 0 0` | `败` | `577 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/coercion-and-consent.md+本轮阅读回执` | `1 0 0 0` | `∅` | `272 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§1障碍的可克服性可谈判vs不可谈判` | `1 0 0 0` | `例适` | `726 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§2贫穷是不是障碍真实冲突不统一` | `1 0 0 0` | `∅` | `539 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§3误解的来源不同→修法不同` | `1 0 0 0` | `∅` | `414 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§4迟到的表白同一机制两种结局保留冲突` | `1 0 0 0` | `∅` | `665 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§5时间轴婚前vs婚后不做通则` | `1 0 0 0` | `∅` | `318 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§6牺牲本批的共识与它的边界` | `1 0 0 0` | `规例` | `374 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§7明确notproven的部分` | `1 0 0 0` | `规` | `706 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md+§8胁迫的知情性与自由同意` | `1 0 0 0` | `适` | `778 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/rules-obstacle-delay.md+r7可选方言口音转写只用于制造信息不对称` | `1 0 0 0` | `∅` | `608 / — / — / —` | `UNALIGNED?` |
| `romance-obstacle-delay-craft/references/rules-obstacle-delay.md+20261031补齐run新增pg59181l720112000独立第二台账8块` | `1 0 0 0` | `反` | `1477 / — / — / —` | `UNALIGNED?` |
| `PG482` | `1 0 0 0` | `∅` | `3666 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG550` | `1 0 0 0` | `∅` | `3666 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG507` | `1 0 0 0` | `∅` | `3666 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG361` | `1 0 0 0` | `∅` | `3666 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG380` | `1 0 0 0` | `∅` | `739 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-obstacle-delay-craft/references/source-index.md+索引使用规则` | `1 0 0 0` | `规` | `430 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+1.何时用何时不用` | `1 0 0 0` | `∅` | `1621 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+2.证据底座输出时必须随` | `1 0 0 0` | `例` | `903 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+3.任务路由先判型再读对应reference` | `1 0 0 0` | `∅` | `1089 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+4.最短执行路径7步从零搭一条有社会成本的婚姻线` | `1 0 0 0` | `∅` | `1148 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+5.输出合同每次任务交付什么` | `1 0 0 0` | `∅` | `781 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+6.红线不可协商` | `1 0 0 0` | `∅` | `1233 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+7.规则索引与限制` | `1 0 0 0` | `∅` | `1463 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `776 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/SKILL.md+9.引用格式输出时强制` | `1 0 0 0` | `∅` | `326 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `814 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/examples/worked-example.md+0.用户给的材料虚构` | `1 0 0 0` | `∅` | `230 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/examples/worked-example.md+1.诊断` | `1 0 0 0` | `∅` | `627 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/examples/worked-example.md+2.改法按执行顺序` | `1 0 0 0` | `∅` | `1823 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/examples/worked-example.md+3.交付物` | `1 0 0 0` | `∅` | `419 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/examples/worked-example.md+4.这次没有用到的规则` | `1 0 0 0` | `例适` | `200 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/references/01-source-roles.md+怎么读` | `1 0 0 0` | `反` | `410 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG969` | `1 0 0 0` | `∅` | `4495 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG821` | `1 0 0 0` | `∅` | `4495 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG471` | `1 0 0 0` | `∅` | `4495 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-social-cost-craft/references/01-source-roles.md+不能当证据的子集` | `1 0 0 0` | `∅` | `461 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-social-cost-craft/references/01-source-roles.md+引用写法` | `1 0 0 0` | `例适` | `550 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `RP1` | `1 0 0 0` | `例` | `1136 / — / — / —` | `UNALIGNED?` |
| `RP2` | `1 0 0 0` | `∅` | `1037 / — / — / —` | `UNALIGNED?` |
| `RP3` | `1 0 0 0` | `例` | `947 / — / — / —` | `UNALIGNED?` |
| `RP6` | `1 0 0 0` | `例` | `899 / — / — / —` | `UNALIGNED?` |
| `RP9` | `1 0 0 0` | `∅` | `688 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `825 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `RP5` | `1 0 0 0` | `例` | `1344 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/references/03-stigma-and-boundaries.md+写作检查清单输出前自查` | `1 0 0 0` | `∅` | `306 / — / — / —` | `UNALIGNED?` |
| `RP4` | `1 0 0 0` | `怎例` | `1058 / — / — / —` | `UNALIGNED?` |
| `RP7` | `1 0 0 0` | `反` | `1239 / — / — / —` | `UNALIGNED?` |
| `RP8` | `1 0 0 0` | `例` | `764 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `564 / — / — / —` | `UNALIGNED?` |
| `romance-social-cost-craft/references/04-confession-documents-ending.md+结局类型速查本批19本实际出现过的` | `1 0 0 0` | `∅` | `538 / — / — / —` | `UNALIGNED?` |
| `SHA-256` | `1 0 0 0` | `∅` | `4199 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `romance-social-cost-craft/references/05-source-index.md+引用格式` | `1 0 0 0` | `∅` | `198 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 03 恐怖（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 03 恐怖

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`gothic-weird-horror-craft`、`horror-dread-and-revelation`、`horror-gothic-suspense-b05`、`horror-supernatural-craft`、`horror-thriller-craft-b04`

**规则单元数 454；v3 对齐成功 1（0.2%）；对齐失败 UNALIGNED? 453（99.8%）**
**flag 计数**：RENUMBERED?=1；SOURCE_ONLY=39；UNALIGNED?=453

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `gothic-weird-horror-craft/SKILL.md+1.何时使用触发` | `1 0 0 0` | `检` | `464 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+2.负触发不要用本skill` | `1 0 0 0` | `∅` | `639 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+3.最短路径四步定档其余都是分支` | `1 0 0 0` | `∅` | `391 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+4.输入必须拿到才动手` | `1 0 0 0` | `∅` | `530 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+5.任务路由` | `1 0 0 0` | `∅` | `610 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+6.执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+6.1定归因档互斥先选` | `1 0 0 0` | `反` | `681 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+6.2定恐惧对象六档决定高潮形态` | `1 0 0 0` | `∅` | `662 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+6.3定三份契约各三选一全篇一致` | `1 0 0 0` | `∅` | `987 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+6.4选信息压制手段三选一见references03` | `1 0 0 0` | `∅` | `286 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `检` | `387 / — / — / —` | `UNALIGNED?` |
| `H4` | `1 0 0 0` | `检` | `387 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `799 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+7.输出合同` | `1 0 0 0` | `∅` | `754 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `适` | `496 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+9.本包不是什么` | `1 0 0 0` | `∅` | `233 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/SKILL.md+10.references` | `1 0 0 0` | `∅` | `672 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `189 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `A4` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `F4` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `F1` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `F3` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `F5` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `F6` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `F2` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/01-attribution-and-fear-objects.md+三组合禁忌h` | `1 0 0 0` | `∅` | `439 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `检` | `913 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `1149 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `872 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/02-contracts-and-switches.md+信息压制手段三选一对同一事件不可并用` | `1 0 0 0` | `∅` | `646 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/02-contracts-and-switches.md+切换代价表p` | `1 0 0 0` | `∅` | `450 / — / — / —` | `UNALIGNED?` |
| `T1` | `1 0 0 0` | `检` | `556 / — / — / —` | `UNALIGNED?` |
| `T2` | `1 0 0 0` | `规` | `1243 / — / — / —` | `UNALIGNED?` |
| `T3` | `1 0 0 0` | `∅` | `811 / — / — / —` | `UNALIGNED?` |
| `T4` | `1 0 0 0` | `∅` | `459 / — / — / —` | `UNALIGNED?` |
| `T5` | `1 0 0 0` | `∅` | `445 / — / — / —` | `UNALIGNED?` |
| `T6` | `1 0 0 0` | `∅` | `419 / — / — / —` | `UNALIGNED?` |
| `T7` | `1 0 0 0` | `∅` | `441 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `699 / — / — / —` | `UNALIGNED?` |
| `T8` | `1 0 0 0` | `∅` | `699 / — / — / —` | `UNALIGNED?` |
| `T9` | `1 0 0 0` | `∅` | `410 / — / — / —` | `UNALIGNED?` |
| `T10` | `1 0 0 0` | `∅` | `448 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§0明令禁止的推导方式写任何输出前先读` | `1 0 0 0` | `∅` | `721 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§1冲突轴1解释vs悬置` | `1 0 0 0` | `∅` | `543 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§2冲突轴2异类有无道德` | `1 0 0 0` | `∅` | `539 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§3冲突轴3素材选址古堡vs本土` | `1 0 0 0` | `∅` | `400 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§4冲突轴4调性气氛冷报道怪诞` | `1 0 0 0` | `∅` | `303 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§5冲突轴5恐怖来源宇宙尺度vs家族社会` | `1 0 0 0` | `∅` | `377 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§6反例清单专门用于推翻通则` | `1 0 0 0` | `∅` | `719 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md+§7部分不适用未证明不要引用它们来支撑规则` | `1 0 0 0` | `∅` | `813 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md+§1先把档位反推出来不知道作者意图时也能做` | `1 0 0 0` | `∅` | `579 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md+§2硬检查项每条都要能指出位置` | `1 0 0 0` | `∅` | `850 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md+§3判分口径粗筛用不是质量总分` | `1 0 0 0` | `∅` | `775 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md+§4常见处方` | `1 0 0 0` | `∅` | `687 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md+§5本表的边界` | `1 0 0 0` | `∅` | `308 / — / — / —` | `UNALIGNED?` |
| `gothic-weird-horror-craft/references/06-source-index.md+§1任务与版本元数据必须随包保留` | `1 0 0 0` | `∅` | `1706 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG389` | `1 0 0 0` | `∅` | `4478 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG696` | `1 0 0 0` | `∅` | `4478 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG84` | `1 0 0 0` | `∅` | `4478 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `gothic-weird-horror-craft/references/06-source-index.md+§3行号口径关键避免引用错位` | `1 0 0 0` | `∅` | `442 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P1` | `1 0 0 0` | `∅` | `1834 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `gothic-weird-horror-craft/references/06-source-index.md+§5权利与许可如实声明不做法律意见` | `1 0 0 0` | `规` | `684 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `gothic-weird-horror-craft/references/06-source-index.md+§6证据边界必须随结论一起说` | `1 0 0 0` | `∅` | `748 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+1.这个skill解决什么` | `1 0 0 0` | `∅` | `686 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+2.触发与负触发` | `1 0 0 0` | `规例` | `848 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+3.输入明确要求` | `1 0 0 0` | `∅` | `590 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `规` | `1878 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+5.条件化恐怖工作模型可选不是固定配方` | `1 0 0 0` | `规检` | `1167 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+6.任务路由` | `1 0 0 0` | `∅` | `1632 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+7.最短执行路径7步` | `1 0 0 0` | `∅` | `1283 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+8.输出合同` | `1 0 0 0` | `∅` | `1083 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `90 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `71 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `96 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `78 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `65 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `72 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `75 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `97 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `∅` | `90 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `R17` | `1 0 0 0` | `∅` | `80 / — / — / —` | `UNALIGNED?` |
| `R18` | `1 0 0 0` | `∅` | `86 / — / — / —` | `UNALIGNED?` |
| `R19` | `1 0 0 0` | `∅` | `83 / — / — / —` | `UNALIGNED?` |
| `R20` | `1 0 0 0` | `∅` | `77 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+9.规则索引` | `1 0 0 0` | `∅` | `2706 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+10.失败出口` | `1 0 0 0` | `规怎检` | `1240 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+11.边界与禁止` | `1 0 0 0` | `规怎` | `701 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+12.fhp标注` | `1 0 0 0` | `∅` | `494 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/SKILL.md+13.版本与迁移` | `1 0 0 0` | `∅` | `1853 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/examples/worked-example.md+例1正常写一篇"夜里有人在楼下说话"的怪谈短篇` | `1 0 0 0` | `∅` | `1606 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/examples/worked-example.md+例2边界用户要"鬼其实是活人"的反转` | `1 0 0 0` | `检` | `651 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/examples/worked-example.md+例3失败出口规则型诅咒写崩` | `1 0 0 0` | `规` | `555 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/examples/worked-example.md+例4负触发用户要"让读者真的害怕的惊吓点子"` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/examples/worked-example.md+例5新增20261031补齐run用户要写"许愿忘掉创伤"的交易型怪谈` | `1 0 0 0` | `∅` | `1593 / — / — / —` | `UNALIGNED?` |
| `R21` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `PG792` | `1 0 0 0` | `怎反检` | `2834 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/01-frames-and-witnesses.md+证据准入与来源边界20261031` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `R22` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `PG345` | `1 0 0 1` | `规怎反适败` | `3279 / — / — / —` | `RENUMBERED?` |
| `R30` | `1 0 0 0` | `∅` | `1716 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/02-dread-staging.md+证据准入与来源边界20261031` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `R23` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `R28` | `1 0 0 0` | `∅` | `1737 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/03-revelation-positions.md+证据准入与来源边界20261031` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `R24` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `R25` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `R29` | `1 0 0 0` | `规适` | `1628 / — / — / —` | `UNALIGNED?` |
| `PG644` | `1 0 0 0` | `规适` | `1628 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/04-rules-and-rituals.md+证据准入与来源边界20261031` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `R27` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `R26` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/05-endings-and-ethics.md+证据准入与来源边界20261031` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+f1｜pg23172thedamnedthing官方不采信异常因果` | `1 0 0 0` | `∅` | `962 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+f2｜pg11438thewillows环境恐惧的归属没有被直接证明` | `1 0 0 0` | `∅` | `520 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+f3｜pg19337achristmascarol不同子类的收束目标不同` | `1 0 0 0` | `∅` | `385 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+f4｜pg10832carnackitheghostfinder同一卷内"人祸"` | `1 0 0 0` | `∅` | `831 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+f5｜pg78605talesoftheuneasy证词各按常理文本不裁决202` | `1 0 0 0` | `∅` | `462 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+h｜五部来源的非同一性` | `1 0 0 0` | `∅` | `509 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+p｜任务路由与失败出口` | `1 0 0 0` | `∅` | `698 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md+证据责任` | `1 0 0 0` | `反适` | `689 / — / — / —` | `UNALIGNED?` |
| `horror-dread-and-revelation/references/source-index.md+重要的证据分层` | `1 0 0 0` | `∅` | `1718 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-dread-and-revelation/references/source-index.md+对0.2.00.3.0旧规则的最终关系` | `1 0 0 0` | `适` | `1347 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-dread-and-revelation/references/source-index.md+p5gq5与版权边界` | `1 0 0 0` | `∅` | `340 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `P4` | `1 0 0 0` | `∅` | `1715 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+触发` | `1 0 0 0` | `规` | `329 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+负触发不使用本技能` | `1 0 0 0` | `∅` | `404 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+输入权限` | `1 0 0 0` | `∅` | `318 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+工作分支` | `1 0 0 0` | `∅` | `589 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+输出` | `1 0 0 0` | `规检` | `316 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+失败出口` | `1 1 0 0` | `规例` | `544 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/SKILL.md+来源与核验` | `1 0 0 0` | `规反适` | `465 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `RG-03` | `1 0 0 0` | `∅` | `372 / — / — / —` | `UNALIGNED?` |
| `RG-02` | `1 0 0 0` | `∅` | `372 / — / — / —` | `UNALIGNED?` |
| `RG-01` | `1 0 0 0` | `∅` | `326 / — / — / —` | `UNALIGNED?` |
| `RG-05` | `1 0 0 0` | `∅` | `353 / — / — / —` | `UNALIGNED?` |
| `RG-06` | `1 0 0 0` | `∅` | `441 / — / — / —` | `UNALIGNED?` |
| `RG-08` | `1 0 0 0` | `∅` | `492 / — / — / —` | `UNALIGNED?` |
| `RG-09` | `1 0 0 0` | `∅` | `390 / — / — / —` | `UNALIGNED?` |
| `RG-14` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `RG-15` | `1 0 0 0` | `∅` | `473 / — / — / —` | `UNALIGNED?` |
| `RG-18` | `1 0 0 0` | `∅` | `352 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/examples.md+反例集失效条件实证` | `1 0 0 0` | `∅` | `880 / — / — / —` | `UNALIGNED?` |
| `RG-04` | `1 0 0 0` | `规怎例反适` | `643 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `RG-07` | `1 0 0 0` | `怎` | `492 / — / — / —` | `UNALIGNED?` |
| `RG-10` | `1 0 0 0` | `怎` | `650 / — / — / —` | `UNALIGNED?` |
| `RG-11` | `1 0 0 0` | `怎` | `589 / — / — / —` | `UNALIGNED?` |
| `RG-12` | `1 0 0 0` | `怎` | `645 / — / — / —` | `UNALIGNED?` |
| `RG-13` | `1 0 0 0` | `怎` | `502 / — / — / —` | `UNALIGNED?` |
| `RG-16` | `1 0 0 0` | `怎` | `544 / — / — / —` | `UNALIGNED?` |
| `RG-17` | `1 0 0 0` | `怎` | `523 / — / — / —` | `UNALIGNED?` |
| `RG-19` | `1 0 0 0` | `怎检` | `623 / — / — / —` | `UNALIGNED?` |
| `RG-20` | `1 0 0 0` | `怎` | `522 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md+1.适用范围` | `1 0 0 0` | `∅` | `873 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md+2.来源族去重同源技法不双计` | `1 0 0 0` | `∅` | `549 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md+3.冲突裁决消费者版` | `1 0 0 0` | `∅` | `70 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `∅` | `298 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md+4.时代局限与当代改写点诚实声明` | `1 0 0 0` | `∅` | `680 / — / — / —` | `UNALIGNED?` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md+5.证据不足不立条如实记录` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `PG924` | `1 0 0 0` | `∅` | `1911 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `S1` | `1 0 0 0` | `∅` | `1911 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG355` | `1 0 0 0` | `∅` | `1722 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG174` | `1 0 0 0` | `∅` | `1722 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `S2` | `1 0 0 0` | `∅` | `1722 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG209` | `1 0 0 0` | `∅` | `1722 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-gothic-suspense-b05/references/source-index.md+阅读覆盖声明` | `1 0 0 0` | `∅` | `591 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-gothic-suspense-b05/references/techniques.md+g.修订自查清单快速` | `1 0 0 0` | `适` | `520 / — / — / —` | `UNALIGNED?` |
| `DS-01` | `1 0 0 0` | `∅` | `66 / — / — / —` | `UNALIGNED?` |
| `DS-02` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `DS-03` | `1 0 0 0` | `∅` | `75 / — / — / —` | `UNALIGNED?` |
| `DS-04` | `1 0 0 0` | `∅` | `77 / — / — / —` | `UNALIGNED?` |
| `DS-05` | `1 0 0 0` | `∅` | `69 / — / — / —` | `UNALIGNED?` |
| `DS-06` | `1 0 0 0` | `∅` | `76 / — / — / —` | `UNALIGNED?` |
| `DS-07` | `1 0 0 0` | `∅` | `64 / — / — / —` | `UNALIGNED?` |
| `DS-08` | `1 0 0 0` | `∅` | `73 / — / — / —` | `UNALIGNED?` |
| `DS-09` | `1 0 0 0` | `∅` | `68 / — / — / —` | `UNALIGNED?` |
| `DS-10` | `1 0 0 0` | `∅` | `87 / — / — / —` | `UNALIGNED?` |
| `DS-11` | `1 0 0 0` | `∅` | `71 / — / — / —` | `UNALIGNED?` |
| `DS-12` | `1 0 0 0` | `∅` | `68 / — / — / —` | `UNALIGNED?` |
| `DS-13` | `1 0 0 0` | `∅` | `67 / — / — / —` | `UNALIGNED?` |
| `DS-14` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `HD-01` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `HD-02` | `1 0 0 0` | `∅` | `52 / — / — / —` | `UNALIGNED?` |
| `HD-03` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `HD-04` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `HD-05` | `1 0 0 0` | `∅` | `77 / — / — / —` | `UNALIGNED?` |
| `HD-06` | `1 0 0 0` | `∅` | `63 / — / — / —` | `UNALIGNED?` |
| `HD-07` | `1 0 0 0` | `∅` | `83 / — / — / —` | `UNALIGNED?` |
| `HD-08` | `1 0 0 0` | `∅` | `57 / — / — / —` | `UNALIGNED?` |
| `HD-09` | `1 0 0 0` | `∅` | `76 / — / — / —` | `UNALIGNED?` |
| `HD-10` | `1 0 0 0` | `∅` | `69 / — / — / —` | `UNALIGNED?` |
| `HD-11` | `1 0 0 0` | `∅` | `68 / — / — / —` | `UNALIGNED?` |
| `HD-12` | `1 0 0 0` | `∅` | `72 / — / — / —` | `UNALIGNED?` |
| `HD-13` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `HD-14` | `1 0 0 0` | `∅` | `38 / — / — / —` | `UNALIGNED?` |
| `HD-15` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `HD-16` | `1 0 0 0` | `∅` | `62 / — / — / —` | `UNALIGNED?` |
| `MD-01` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `MD-02` | `1 0 0 0` | `∅` | `89 / — / — / —` | `UNALIGNED?` |
| `MD-03` | `1 0 0 0` | `∅` | `86 / — / — / —` | `UNALIGNED?` |
| `MD-04` | `1 0 0 0` | `∅` | `89 / — / — / —` | `UNALIGNED?` |
| `MD-05` | `1 0 0 0` | `∅` | `65 / — / — / —` | `UNALIGNED?` |
| `MD-06` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `MD-07` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `MD-08` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `MD-09` | `1 0 0 0` | `∅` | `73 / — / — / —` | `UNALIGNED?` |
| `MD-10` | `1 0 0 0` | `∅` | `71 / — / — / —` | `UNALIGNED?` |
| `MD-11` | `1 0 0 0` | `∅` | `38 / — / — / —` | `UNALIGNED?` |
| `MD-12` | `1 0 0 0` | `∅` | `66 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+1.何时使用` | `1 0 0 0` | `例检` | `587 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+2.负触发不要用本skill` | `1 0 0 0` | `规` | `707 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+3.最短路径` | `1 0 0 0` | `∅` | `1218 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `1079 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+5.证据声明` | `1 0 0 0` | `∅` | `1035 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `428 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+7.失败出口` | `1 0 0 0` | `例` | `620 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/SKILL.md+8.语料边界最重要的三句话` | `1 0 0 0` | `∅` | `603 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+示例a语料复盘pg43"thelastnight"的破门场景拆解` | `1 0 0 0` | `规` | `1873 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+示例b合成设计示范"继承的斗篷"短篇约6000词` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+第1步机制设定单references01` | `1 0 0 0` | `∅` | `538 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+第2步誓约三要素表01§3` | `1 0 0 0` | `∅` | `433 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+第3步物证对账单03§1` | `1 0 0 0` | `∅` | `495 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+第4步入场与憋蓄02§1§5` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+第5步收束对账03§305§2` | `1 0 0 0` | `∅` | `389 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+示例b的自我风险标注` | `1 0 0 0` | `规` | `327 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/examples/worked-example.md+使用提醒` | `1 0 0 0` | `∅` | `356 / — / — / —` | `UNALIGNED?` |
| `M11` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `M14` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `M15` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `M02` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `M12` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/01-mechanics-and-curses.md+7.本文件规则速查` | `1 0 0 0` | `∅` | `637 / — / — / —` | `UNALIGNED?` |
| `M21` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `M03` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `M01` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `M04` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `M16` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `M07` | `1 0 0 0` | `∅` | `1074 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/02-dread-and-atmosphere.md+7.场景自查清单` | `1 0 0 0` | `∅` | `580 / — / — / —` | `UNALIGNED?` |
| `M08` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `M05` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `M06` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/03-evidence-and-revelation.md+5.证据自查清单` | `1 0 0 0` | `∅` | `574 / — / — / —` | `UNALIGNED?` |
| `M17` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M09` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M10` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/04-structure-and-narrators.md+1.框架选择需要多层信息时采用非强制起草前置` | `1 0 0 0` | `∅` | `802 / — / — / —` | `UNALIGNED?` |
| `C-05` | `1 0 0 0` | `∅` | `1595 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/04-structure-and-narrators.md+5.临终装置组跨框架可复用` | `1 0 0 0` | `∅` | `1145 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/04-structure-and-narrators.md+6.框架自查清单` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `M18` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M20` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M19` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M13` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-supernatural-craft/references/05-negative-space-and-tone.md+5.全稿调性审计表` | `1 0 0 0` | `∅` | `496 / — / — / —` | `UNALIGNED?` |
| `PG43` | `1 0 0 0` | `∅` | `3840 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `SHA-256` | `1 0 0 0` | `∅` | `3840 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG459` | `1 0 0 0` | `∅` | `3840 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-supernatural-craft/references/06-source-index.md+2.规则编号约定重要` | `1 0 0 0` | `∅` | `769 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-supernatural-craft/references/06-source-index.md+3.融合决策摘要` | `1 0 0 0` | `∅` | `743 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-supernatural-craft/references/06-source-index.md+4.跨skill接口` | `1 0 0 0` | `∅` | `691 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-supernatural-craft/references/06-source-index.md+5.引用与验证路径` | `1 0 0 0` | `∅` | `464 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-supernatural-craft/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `B04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+本轮p3p4返工后的强制分支` | `1 0 0 0` | `∅` | `508 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+0.这份skill是什么` | `1 0 0 0` | `规` | `600 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+0.1与v1.0.0的差异必读` | `1 0 0 0` | `∅` | `906 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+1.先做三问类型判定必做` | `1 0 0 0` | `怎例` | `720 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+2.选恐怖来源三选一为主再选伪装` | `1 0 0 0` | `∅` | `1136 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+3.七步工作流` | `1 0 0 0` | `∅` | `1402 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+4.规则族速查完整锚点见references` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `A7` | `1 0 0 0` | `例` | `1413 / — / — / —` | `UNALIGNED?` |
| `A6` | `1 0 0 0` | `例` | `1413 / — / — / —` | `UNALIGNED?` |
| `A5` | `1 0 0 0` | `例` | `1413 / — / — / —` | `UNALIGNED?` |
| `B7` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `∅` | `1077 / — / — / —` | `UNALIGNED?` |
| `C7` | `1 0 0 0` | `规` | `1111 / — / — / —` | `UNALIGNED?` |
| `D1` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `D2` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `D3` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `D7` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `D5` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `D4` | `1 0 0 0` | `∅` | `1116 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `1433 / — / — / —` | `UNALIGNED?` |
| `E6` | `1 0 0 0` | `∅` | `1433 / — / — / —` | `UNALIGNED?` |
| `E7` | `1 0 0 0` | `∅` | `1433 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `1433 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `∅` | `1433 / — / — / —` | `UNALIGNED?` |
| `G5` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `G4` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `G1` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `G2` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `G3` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `G6` | `1 0 0 0` | `∅` | `742 / — / — / —` | `UNALIGNED?` |
| `H3` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `H1` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `H2` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `I3` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `I1` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `I2` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `J4` | `1 0 0 0` | `∅` | `585 / — / — / —` | `UNALIGNED?` |
| `J1` | `1 0 0 0` | `∅` | `585 / — / — / —` | `UNALIGNED?` |
| `J3` | `1 0 0 0` | `∅` | `585 / — / — / —` | `UNALIGNED?` |
| `J2` | `1 0 0 0` | `∅` | `585 / — / — / —` | `UNALIGNED?` |
| `K3` | `1 0 0 0` | `∅` | `1039 / — / — / —` | `UNALIGNED?` |
| `K2` | `1 0 0 0` | `∅` | `1039 / — / — / —` | `UNALIGNED?` |
| `K1` | `1 0 0 0` | `∅` | `1039 / — / — / —` | `UNALIGNED?` |
| `L1B` | `1 0 0 0` | `∅` | `617 / — / — / —` | `UNALIGNED?` |
| `L1` | `1 0 0 0` | `∅` | `617 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+5.决策表按情境选规则` | `1 0 0 0` | `∅` | `1887 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+6.最小改稿检查12项` | `1 0 0 0` | `∅` | `915 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+7.references导航` | `1 0 0 0` | `规例反败` | `1059 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+8.证据与限制本版修正` | `1 0 0 0` | `∅` | `1009 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/SKILL.md+9.本版取代声明` | `1 0 0 0` | `∅` | `555 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+1.道具结算配对表装置迁移` | `1 0 0 0` | `规` | `2646 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.九个边界样本逐条` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.1pg13314barfordabbey感伤书信体非恐怖` | `1 0 0 0` | `适` | `576 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.2pg269beastsandsuperbeasts讽刺集` | `1 0 0 0` | `∅` | `307 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.3pg9964thecentaur自然神秘` | `1 0 0 0` | `∅` | `328 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.4pg6761ferdinandcountfathom流浪汉小说` | `1 0 0 0` | `∅` | `260 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.5pg9468annast.ives雅各宾书信体混合` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.6pg30729stevenson文集卷三mixed本版重写` | `1 0 0 0` | `怎` | `1372 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.7pg35153pg78106machen自传性文论非虚构` | `1 0 0 0` | `规` | `248 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.8pg14099证言汇编非虚构` | `1 0 0 0` | `∅` | `268 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+2.9四个非虚构源的关系说明` | `1 0 0 0` | `∅` | `571 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/counterexamples.md+3.迁移检查清单` | `1 0 0 0` | `∅` | `494 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架1pg175thephantomoftheopera全解释型长篇` | `1 0 0 0` | `∅` | `62 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+可迁移步骤` | `1 0 0 0` | `∅` | `544 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+失效条件` | `1 0 0 0` | `∅` | `220 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架2pg68569thewyvernmystery家族哥特长篇` | `1 0 0 0` | `∅` | `63 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+结构拆解` | `1 0 0 0` | `∅` | `698 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架3pg932thefallofthehouseofusher短篇同构` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架4pg12828twoghostlymysteries伪文献+痕迹反证` | `1 0 0 0` | `∅` | `67 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架5pg23535theinvaders短篇密度型` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+骨架6pg30729thebodysnatcher+批评卷双载体示范本版新增` | `1 0 0 0` | `∅` | `185 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+6a短篇部分carrier=fiction共犯与物流` | `1 0 0 0` | `怎适` | `1626 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+6b批评部分carrier=nonfiction六个可迁移装置` | `1 0 0 0` | `怎` | `2268 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/examples.md+6c本骨架的禁止事项` | `1 0 0 0` | `怎` | `338 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+1.notproven不得写进规则` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+2.时代伤害只登记不采纳` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+2.1残疾疾病作为"恶的标记"` | `1 0 0 0` | `∅` | `571 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+2.2性别暴力与"浪漫化胁迫"` | `1 0 0 0` | `∅` | `513 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+2.3阶级种族国族刻板` | `1 0 0 0` | `∅` | `210 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+2.4pg30729的时代立场本版新增必须单列` | `1 0 0 0` | `∅` | `982 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.可复现的结构性失败` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.1解释焦虑收束阶段倒空` | `1 0 0 0` | `∅` | `293 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.2巧合过量` | `1 0 0 0` | `∅` | `182 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.3感伤洗白` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.4规则自相矛盾` | `1 0 0 0` | `规` | `222 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.5效果饥渴本版新增制造阶段加料规则l1` | `1 0 0 0` | `规` | `773 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+3.6载体误用本版新增pg30729专项` | `1 0 0 0` | `∅` | `494 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/failure-modes.md+4.使用本skill的禁止清单` | `1 0 0 0` | `∅` | `529 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/freeze-manifest.json+freezemanifest.json` | `1 0 0 0` | `∅` | `2232 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+h.怪谈集选本结构` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+规则h1恐怖篇+换气篇carrier=fiction` | `1 0 0 0` | `检` | `218 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+规则h2统一框架把异构篇目缝成书carrier=fiction` | `1 0 0 0` | `检` | `137 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+规则h3选本导论给类型学并承认偏差carrier=fiction` | `1 0 0 0` | `检` | `188 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+l.写作纪律本版新增族cond` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+规则l1反"效果饥渴"condcarrier=nonfiction主张+fict` | `1 0 0 0` | `规怎检败` | `1442 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+边界样本九个控制组` | `1 0 0 0` | `∅` | `105 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+1.pg13314barfordabbey感伤书信体` | `1 0 0 0` | `怎` | `213 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+2.pg269beastsandsuperbeasts讽刺集` | `1 0 0 0` | `∅` | `273 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+3.pg9964thecentaur自然神秘` | `1 0 0 0` | `∅` | `202 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+4.pg6761ferdinandcountfathom流浪汉小说` | `1 0 0 0` | `∅` | `182 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+5.pg9468annast.ives雅各宾书信体混合` | `1 0 0 0` | `∅` | `421 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+6.pg30729stevenson文集卷三mixed本版重写` | `1 0 0 0` | `怎` | `2097 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+7.pg35153pg78106machen自传性文论非虚构` | `1 0 0 0` | `规` | `247 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+8.pg14099证言汇编非虚构` | `1 0 0 0` | `∅` | `267 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+9.pg30729批评部分与上述三者的关系说明` | `1 0 0 0` | `∅` | `253 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+作者自述的处理硬规则` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+四用法登记pg30729的落位` | `1 0 0 0` | `∅` | `476 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md+本册的最小检查` | `1 0 0 0` | `∅` | `427 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+b.可信度工程` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则b1证言链+一件只有当事人知道的琐物corecarrier=fiction` | `1 0 0 0` | `规怎` | `523 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则b2让官方给出"最合理的错误答案"corecarrier=fiction` | `1 0 0 0` | `规` | `474 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则b4多层叙述者各见一部分corecarrier=fiction` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则b5让读者先于叙述者知道corecarrier=fiction` | `1 0 0 0` | `怎` | `237 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则b7量化细节降温本版新增condcarrier=nonfiction主张+f` | `1 0 0 0` | `规怎` | `966 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+e.视角与不可靠` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则e1不信者被迫信corecarrier=fiction` | `1 0 0 0` | `∅` | `146 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则e2日记史书=自我治疗或自我辩护corecarrier=fiction` | `1 0 0 0` | `∅` | `427 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则e3信息扣留必须有后文兑现corecarrier=fiction` | `1 0 0 0` | `∅` | `268 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则e6自白+压回本版新增corecarrier=nonfiction机制最完整` | `1 0 0 0` | `规怎` | `1411 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+规则e7公私反差即可信度装置本版新增condcarrier=nonfiction` | `1 0 0 0` | `规怎` | `1022 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md+本册的最小检查` | `1 0 0 0` | `∅` | `430 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+f.升级引擎` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+引擎f1三异常一结论密度型carrier=fiction` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+引擎f2延迟永不发生耗损型carrier=fiction` | `1 0 0 0` | `∅` | `330 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+引擎f3身体功能背叛强度型carrier=fiction` | `1 0 0 0` | `∅` | `328 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+引擎f4短恐怖+长日常长篇节奏carrier=fiction` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+补充引擎cond来自k族详见rulescontractsandspace.md` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+g.收束与余数` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g1一行一句冷收束carrier=fiction` | `1 0 0 0` | `∅` | `525 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g2冷档案新闻纪实体carrier=fiction` | `1 0 0 0` | `∅` | `353 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g3解释核心危险可选择留一项有作用的余数carrier=fiction` | `1 0 0 0` | `规适` | `430 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g4反高潮否认心理型carrier=fiction` | `1 0 0 0` | `∅` | `144 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g5感伤婚礼秩序恢复carrier=fiction` | `1 0 0 0` | `∅` | `206 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+收束g6留下不解释的凶兆线carrier=fiction` | `1 0 0 0` | `∅` | `125 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+冲突裁决与收束直接相关` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md+本册的最小检查` | `1 0 0 0` | `∅` | `449 / — / — / —` | `UNALIGNED?` |
| `PG269` | `1 0 0 0` | `规败` | `1369 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `S4` | `1 0 0 0` | `怎` | `1368 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/fear-source-and-type.md+6.规则a7非人程序恐怖本版新增condcarrier=nonfiction主张` | `1 0 0 0` | `规怎例适` | `1388 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/fear-source-and-type.md+7.类型判定速查表` | `1 0 0 0` | `∅` | `559 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/fear-source-and-type.md+8.本册不采用的来源` | `1 0 0 0` | `∅` | `272 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/fear-source-and-type.md+9.本册的最小检查` | `1 0 0 0` | `∅` | `331 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `378 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `16 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/historical-provenance.md+历史freeze.md旧产物` | `1 0 0 0` | `∅` | `163 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/references/rework-decision.md+输入合同` | `1 0 0 0` | `∅` | `407 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `1552 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rework-decision.md+l1l2边界同卷必须拆开` | `1 0 0 0` | `反` | `883 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rework-decision.md+场景修订与失败出口` | `1 0 0 0` | `∅` | `694 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+c.规则禁令与契约` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c1聚焦一条可记忆禁令有条件的默认corecarrier=fiction` | `1 0 0 0` | `∅` | `230 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c2把抽象恐惧换成可结算的契约corecarrier=fiction` | `1 0 0 0` | `∅` | `97 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c3规则要"日常到可笑"corecarrier=fiction` | `1 0 0 0` | `∅` | `172 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c4反制先由"失效"建立corecarrier=fiction` | `1 0 0 0` | `∅` | `140 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c5代价必须具体且可执行corecarrier=fiction` | `1 0 0 0` | `∅` | `144 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则c7代价单位化本版新增corecarrier=nonfiction主张+3个` | `1 0 0 0` | `规怎例适` | `1157 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+d.空间与物证` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d1建筑即凶器通道要预埋corecarrier=fiction` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d2局部先行每次只开一个感官corecarrier=fiction` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d3一件可携带的实物corecarrier=fiction` | `1 0 0 0` | `∅` | `136 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d4痕迹反证corecarrier=fiction` | `1 0 0 0` | `∅` | `105 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d5日常物件的背叛corecarrier=fiction` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则d7以熟为奇本版新增condcarrier=nonfiction主张+fic` | `1 0 0 0` | `规怎` | `1285 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+k.团伙与程序本版新增族三条全部cond` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则k1团伙退场表condcarrier=nonfiction主+fiction` | `1 0 0 0` | `规怎` | `892 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则k2程序化作案condcarrier=nonfiction主+fiction` | `1 0 0 0` | `规怎` | `1218 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+规则k3囚禁对照法仅非虚构主例condcarrier=nonfiction主+f` | `1 0 0 0` | `规怎` | `902 / — / — / —` | `UNALIGNED?` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md+本册的最小检查` | `1 0 0 0` | `∅` | `546 / — / — / —` | `UNALIGNED?` |
| `PG175` | `1 0 0 0` | `∅` | `3981 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG537` | `1 0 0 0` | `∅` | `3981 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG932` | `1 0 0 0` | `∅` | `3981 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/sources-index.md+族权重说明` | `1 0 0 0` | `∅` | `775 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `horror-thriller-craft-b04/sources-index.md+引用约定` | `1 0 0 0` | `∅` | `513 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 04 武侠仙侠玄幻（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 04 武侠仙侠玄幻

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`speculative-wuxia-fantasy-craft`、`wuxia-fantasy-power-arc`、`wuxia-xianxia-plot-forge`、`fantasy-adventure-structure-lab`、`supernatural-power-craft`

**规则单元数 627；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 627（100.0%）**
**flag 计数**：SOURCE_ONLY=44；UNALIGNED?=627

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `P4` | `1 0 0 0` | `规` | `985 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+0.适用范围与诚实声明先读` | `1 0 0 0` | `∅` | `1142 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+1.触发与负触发` | `1 0 0 0` | `规例检适` | `1237 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+2.证据底座` | `1 0 0 0` | `∅` | `686 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `459 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+4.规则族索引22族` | `1 0 0 0` | `∅` | `3209 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+5.最短执行路径` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+a.从零设计奇境约30–60分钟` | `1 0 0 0` | `∅` | `496 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+b.设计法宝禁忌试炼升级约40–90分钟` | `1 0 0 0` | `∅` | `588 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+c.设计代价身份替身名号约30–60分钟` | `1 0 0 0` | `∅` | `436 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+d.设计制度组织传闻反派约30–60分钟` | `1 0 0 0` | `∅` | `504 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+e.设计预言契约收束约20–40分钟` | `1 0 0 0` | `∅` | `302 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+f.审稿诊断约15–30分钟` | `1 0 0 0` | `∅` | `268 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+6.输出模板按需裁剪` | `1 0 0 0` | `∅` | `858 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+7.失败出口何时停` | `1 0 0 0` | `规适` | `1099 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+8.文件清单` | `1 0 0 0` | `反败` | `1001 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/SKILL.md+9.交付状态如实` | `1 0 0 0` | `规` | `345 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `196 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/counterexamples.md+1.来源内失败原著自己暴露的坑` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C-01` | `1 0 0 0` | `规怎反适` | `526 / — / — / —` | `UNALIGNED?` |
| `C-02` | `1 0 0 0` | `规怎反` | `482 / — / — / —` | `UNALIGNED?` |
| `C-03` | `1 0 0 0` | `规怎反` | `548 / — / — / —` | `UNALIGNED?` |
| `C-04` | `1 0 0 0` | `规怎反适` | `487 / — / — / —` | `UNALIGNED?` |
| `C-05` | `1 0 0 0` | `规怎反适` | `399 / — / — / —` | `UNALIGNED?` |
| `C-06` | `1 0 0 0` | `规怎反` | `485 / — / — / —` | `UNALIGNED?` |
| `C-07` | `1 0 0 0` | `规怎反适` | `443 / — / — / —` | `UNALIGNED?` |
| `C-08` | `1 0 0 0` | `规怎反` | `529 / — / — / —` | `UNALIGNED?` |
| `C-09` | `1 0 0 0` | `规怎反适` | `396 / — / — / —` | `UNALIGNED?` |
| `C-10` | `1 0 0 0` | `规怎反` | `521 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/counterexamples.md+2.现代误用把单源时代局限当规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M-01` | `1 0 0 0` | `∅` | `358 / — / — / —` | `UNALIGNED?` |
| `M-02` | `1 0 0 0` | `∅` | `605 / — / — / —` | `UNALIGNED?` |
| `M-03` | `1 0 0 0` | `∅` | `349 / — / — / —` | `UNALIGNED?` |
| `M-04` | `1 0 0 0` | `∅` | `273 / — / — / —` | `UNALIGNED?` |
| `M-05` | `1 0 0 0` | `适` | `249 / — / — / —` | `UNALIGNED?` |
| `M-06` | `1 0 0 0` | `规` | `230 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/counterexamples.md+3.证据边界本批不能证明` | `1 0 0 0` | `∅` | `735 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/counterexamples.md+4.使用反例的正确姿势` | `1 0 0 0` | `∅` | `405 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/examples.md+例1雾港长篇奇境+圣物+群体转变` | `1 0 0 0` | `规` | `226 / — / — / —` | `UNALIGNED?` |
| `F01` | `1 1 0 0` | `∅` | `746 / 627 / — / —` | `UNALIGNED?` |
| `F02` | `1 1 0 0` | `例` | `854 / 531 / — / —` | `UNALIGNED?` |
| `F03` | `1 1 0 0` | `∅` | `776 / 580 / — / —` | `UNALIGNED?` |
| `F13` | `1 1 0 0` | `∅` | `462 / 501 / — / —` | `UNALIGNED?` |
| `F18` | `1 1 0 0` | `检` | `296 / 520 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/examples.md+例2假王子身份+替身+传闻` | `1 0 0 0` | `规` | `249 / — / — / —` | `UNALIGNED?` |
| `F08` | `1 1 0 0` | `∅` | `667 / 530 / — / —` | `UNALIGNED?` |
| `F09` | `1 1 0 0` | `∅` | `769 / 505 / — / —` | `UNALIGNED?` |
| `F14` | `1 1 0 0` | `∅` | `282 / 487 / — / —` | `UNALIGNED?` |
| `F15` | `1 1 0 0` | `检` | `433 / 447 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/examples.md+例3移动客栈制度讽刺+条文漏洞+收束` | `1 0 0 0` | `规` | `232 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `436 / — / — / —` | `UNALIGNED?` |
| `F04` | `1 1 0 0` | `∅` | `436 / 604 / — / —` | `UNALIGNED?` |
| `F12` | `1 1 0 0` | `∅` | `471 / 537 / — / —` | `UNALIGNED?` |
| `F17` | `1 1 0 0` | `检` | `229 / 485 / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `检` | `229 / — / — / —` | `UNALIGNED?` |
| `F20` | `1 1 0 0` | `∅` | `451 / 511 / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `451 / — / — / —` | `UNALIGNED?` |
| `F19` | `1 1 0 0` | `检` | `409 / 488 / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `检` | `409 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/examples.md+组合原则三例共用` | `1 0 0 0` | `∅` | `488 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/failure-modes.md+1.快速判断表` | `1 0 0 0` | `∅` | `1314 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/failure-modes.md+2.逐类失败出口` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `FM-01` | `1 0 0 0` | `例` | `524 / — / — / —` | `UNALIGNED?` |
| `FM-02` | `1 0 0 0` | `例` | `423 / — / — / —` | `UNALIGNED?` |
| `FM-03` | `1 0 0 0` | `规败` | `506 / — / — / —` | `UNALIGNED?` |
| `FM-04` | `1 0 0 0` | `∅` | `501 / — / — / —` | `UNALIGNED?` |
| `FM-05` | `1 0 0 0` | `∅` | `428 / — / — / —` | `UNALIGNED?` |
| `FM-06` | `1 0 0 0` | `∅` | `381 / — / — / —` | `UNALIGNED?` |
| `FM-07` | `1 0 0 0` | `规` | `448 / — / — / —` | `UNALIGNED?` |
| `FM-08` | `1 0 0 0` | `∅` | `559 / — / — / —` | `UNALIGNED?` |
| `FM-09` | `1 0 0 0` | `适` | `430 / — / — / —` | `UNALIGNED?` |
| `FM-10` | `1 0 0 0` | `∅` | `435 / — / — / —` | `UNALIGNED?` |
| `FM-11` | `1 0 0 0` | `例` | `463 / — / — / —` | `UNALIGNED?` |
| `FM-12` | `1 0 0 0` | `∅` | `338 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/failure-modes.md+3.停写信号出现即停不要硬写` | `1 0 0 0` | `∅` | `554 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/failure-modes.md+4.降级路径不能停时` | `1 0 0 0` | `败` | `638 / — / — / —` | `UNALIGNED?` |
| `F22` | `1 1 0 0` | `∅` | `219 / 468 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f01r1门槛可用时间或权限表示非所有异界都适用` | `1 0 0 0` | `规怎` | `1012 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f01r2若有“回返”戏剧压力明确一次具体代价` | `1 0 0 0` | `怎` | `781 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f01r3入口要有“社会面”` | `1 0 0 0` | `怎` | `701 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f02r1一条法则先推演日常` | `1 0 0 0` | `规怎例适` | `630 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f02r2边界补丁让法则可信` | `1 0 0 0` | `怎例` | `796 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f02r3对承重的超凡法则明确可见限制或后果` | `1 0 0 0` | `怎` | `951 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f18r1时间膨胀要有比例` | `1 0 0 0` | `怎例适` | `609 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f18r2反向时间差异境很久现实一瞬` | `1 0 0 0` | `怎例适` | `520 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f18r3可携带空间与跨世界信物` | `1 0 0 0` | `规怎` | `664 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f22r1入侵靠合谋伪装不靠战斗` | `1 0 0 0` | `怎` | `746 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md+f22r2规则例外先演示后解释` | `1 0 0 0` | `怎例` | `582 / — / — / —` | `UNALIGNED?` |
| `F05` | `1 1 0 0` | `∅` | `151 / 526 / — / —` | `UNALIGNED?` |
| `F06` | `1 1 0 0` | `∅` | `151 / 459 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f03r1单一功能+有限无限` | `1 0 0 0` | `怎例` | `765 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f03r2持有凭证与失去条件` | `1 0 0 0` | `怎适` | `779 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f03r3公开验证与来源排他` | `1 0 0 0` | `怎` | `841 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f03r4移动领地立起即生效singlesource仅pg59239` | `1 0 0 0` | `规怎适` | `716 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f04r1禁令少而具体先由长者说清` | `1 0 0 0` | `规怎` | `786 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f04r2违规的不同代价3次只是pg某故事示范非规定` | `1 0 0 0` | `怎` | `825 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f04r3违规留下可观察痕迹` | `1 0 0 0` | `怎` | `694 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f05r1出发前交底成败条件` | `1 0 0 0` | `规怎败` | `835 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f05r2若作者承诺公平闯关任务链应给可追溯的终局条件神话荒诞可刻意失明` | `1 0 0 0` | `规怎` | `901 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f05r3伪证拆穿靠物证工匠公开验证` | `1 0 0 0` | `怎` | `656 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f06r1同路线换靶代价递增` | `1 0 0 0` | `怎` | `794 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md+f06r2愿望阶梯每次兑现生成下一关最终归零反噬` | `1 0 0 0` | `怎` | `890 / — / — / —` | `UNALIGNED?` |
| `F07` | `1 1 0 0` | `∅` | `163 / 498 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f07r1资产递减每件对应一个受助者` | `1 0 0 0` | `怎` | `652 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f07r2自愿条款把牺牲变成谈判` | `1 0 0 0` | `规怎适` | `813 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f07r3诱惑按具体缺口定制` | `1 0 0 0` | `怎` | `621 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f08r1物证三层独特材质+公开匹配+成对证明` | `1 0 0 0` | `怎` | `716 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f08r2知识史验证只有真身知道的路线口令称呼` | `1 0 0 0` | `怎` | `692 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f08r3公共仪式认亲让当事人自己认` | `1 0 0 0` | `怎` | `664 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f09r1先让凭证失效再让冒充者上位` | `1 0 0 0` | `怎` | `906 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f09r2知识缺口无心话败露` | `1 0 0 0` | `规怎` | `540 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f09r3双误认登场先以敌人形态出现再以行为纠正` | `1 0 0 0` | `怎例适` | `664 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f09r4替身夺舍恐怖在“比你更称职”` | `1 0 0 0` | `怎` | `719 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f14r1名字由事件产生` | `1 0 0 0` | `怎` | `794 / — / — / —` | `UNALIGNED?` |
| `PG96` | `1 0 0 0` | `怎` | `610 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md+f14r3结尾改名完成主题闭环` | `1 0 0 0` | `怎` | `592 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f12r1制度质感四件套日期+程序+工具+费用` | `1 0 0 0` | `怎` | `789 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f12r2定义战先重定义关键词再由受害者证词反打` | `1 0 0 0` | `怎` | `807 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f12r3条文漏洞用字面解释反制` | `1 0 0 0` | `怎` | `663 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f13r1四环行为链劳动→环境→交谈→互助` | `1 0 0 0` | `怎` | `752 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f13r2意图等价给弱者一个替代出口` | `1 0 0 0` | `规怎败` | `651 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f15r1怪物由不可靠描述生成` | `1 0 0 0` | `怎` | `732 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f15r2权力来自可见密谈` | `1 0 0 0` | `怎` | `664 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f15r3舆论包装报纸学术把无法解释的事变成定论` | `1 0 0 0` | `怎` | `823 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f17r1定义暴力优先攻击“你是什么”不是“你能打多少”` | `1 0 0 0` | `怎` | `674 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f17r2识人判词让反派的评价暴露自己的匮乏` | `1 0 0 0` | `怎` | `585 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md+f17r3真诚反派三件套真信仰+真勇气+真守约+抽象盲点` | `1 0 0 0` | `怎` | `702 / — / — / —` | `UNALIGNED?` |
| `F16` | `1 1 0 0` | `∅` | `175 / 501 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f16r1规则已知选择未知` | `1 0 0 0` | `规怎` | `909 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f16r2字面漏洞用不可能的小任务破契约` | `1 0 0 0` | `规怎` | `670 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f16r3灵魂分身三条款仪式回归周期不可逆` | `1 0 0 0` | `规怎` | `643 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f19r1入门三要素口令+数字+时辰` | `1 0 0 0` | `怎` | `664 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f19r2规章可以荒诞但必须当众宣布并执行` | `1 0 0 0` | `怎` | `824 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f19r3家用物入会用日常物制造神圣喜剧` | `1 0 0 0` | `怎` | `618 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f20r1愿望偏移以主题满足替代字面满足` | `1 0 0 0` | `怎` | `719 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f20r2反圆满复位即死恶人继位` | `1 0 0 0` | `怎例适` | `594 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f20r3假圣物不必揭穿让实务者因社会效果沉默singlesource仅pg67` | `1 0 0 0` | `怎` | `637 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md+f20r4价值重估最珍贵的是被弃之物` | `1 0 0 0` | `怎` | `642 / — / — / —` | `UNALIGNED?` |
| `F21` | `1 1 0 0` | `∅` | `194 / 485 / — / —` | `UNALIGNED?` |
| `F10` | `1 1 0 0` | `∅` | `194 / 512 / — / —` | `UNALIGNED?` |
| `F11` | `1 1 0 0` | `∅` | `194 / 491 / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f10r1固定位置主角+自由代理` | `1 0 0 0` | `怎` | `857 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f10r2往返节拍每次回来带一个新信息` | `1 0 0 0` | `怎` | `598 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f11r1多证词+拒证者+遗物收尾` | `1 0 0 0` | `怎` | `825 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f11r2伪文献套层声明来源只改人名` | `1 0 0 0` | `怎` | `653 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f11r3痕迹替代尸体凹痕涟漪声音` | `1 0 0 0` | `怎` | `858 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f21r1留白三件套声音+痕迹+见证分裂` | `1 0 0 0` | `怎` | `755 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+f21r2档案句只记录不解释` | `1 0 0 0` | `怎` | `591 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md+类型边界与证据限制必读` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `∅` | `700 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `规` | `345 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `规` | `382 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `306 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `∅` | `239 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `16 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B01` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `A-05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/rework-decision.md+角色与输入` | `1 0 0 0` | `∅` | `450 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/rework-decision.md+四个决策器` | `1 0 0 0` | `∅` | `1476 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/rework-decision.md+案例动作与失败出口` | `1 0 0 0` | `规例` | `811 / — / — / —` | `UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/references/rework-decision.md+输出表p` | `1 0 0 0` | `∅` | `262 / — / — / —` | `UNALIGNED?` |
| `PG128` | `1 0 0 0` | `∅` | `178 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG149` | `1 0 0 0` | `∅` | `168 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG540` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG697` | `1 0 0 0` | `∅` | `163 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG701` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG873` | `1 0 0 0` | `∅` | `169 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG897` | `1 0 0 0` | `∅` | `193 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG902` | `1 0 0 0` | `∅` | `179 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/sources-index.md+1.逐源表25本` | `1 0 0 0` | `∅` | `4839 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/sources-index.md+2.来源族去重20族` | `1 0 0 0` | `规` | `1423 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/sources-index.md+3.引用与回读规则` | `1 0 0 0` | `规例` | `619 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `speculative-wuxia-fantasy-craft/sources-index.md+4.逐本sha256完整` | `1 0 0 0` | `∅` | `2053 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/SKILL.md+触发不触发` | `1 0 0 0` | `∅` | `282 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/SKILL.md+输入和权威` | `1 0 0 0` | `∅` | `533 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/SKILL.md+任务路由与关键决策` | `1 0 0 0` | `∅` | `1899 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/SKILL.md+缺料或冲突` | `1 0 0 0` | `∅` | `380 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/SKILL.md+输出证据与许可` | `1 0 0 0` | `∅` | `643 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `286 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/01-power-source-and-price.md+r1｜keep行为判断` | `1 0 0 0` | `规例反适` | `1110 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/01-power-source-and-price.md+r2｜revise行为判断` | `1 0 0 0` | `规例反` | `1031 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/01-power-source-and-price.md+r3｜revise行为判断` | `1 0 0 0` | `规例反` | `1071 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/01-power-source-and-price.md+r4｜revise行为判断` | `1 0 0 0` | `规例反适` | `1076 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/02-escalation-ladder.md+r5｜reject行为判断` | `1 0 0 0` | `规例反败` | `1049 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/02-escalation-ladder.md+r6｜revise行为判断` | `1 0 0 0` | `规例反` | `1013 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/02-escalation-ladder.md+r9｜reject行为判断` | `1 0 0 0` | `规例反` | `1043 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/03-legitimacy-and-institution.md+r7｜keep行为判断` | `1 0 0 0` | `规例反适` | `971 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/03-legitimacy-and-institution.md+r8｜revise行为判断` | `1 0 0 0` | `规例反` | `992 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/03-legitimacy-and-institution.md+r11｜reject行为判断` | `1 0 0 0` | `规例反` | `1024 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/04-information-and-reveal.md+r10｜revise行为判断` | `1 0 0 0` | `规例反` | `1030 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md+r12｜keep行为判断` | `1 0 0 0` | `规例反适` | `1025 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md+类型边界与旧反例重判` | `1 0 0 0` | `规` | `626 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md+r13｜新增角色真身与假身须靠可核证据而不是名号自动转让` | `1 0 0 0` | `反` | `662 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md+r14｜新增同一词“魔法”可能指真实机制或情感隐喻` | `1 0 0 0` | `反` | `643 / — / — / —` | `UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md+r15｜新增翻译来的神谱旧时代偏见不能当中国仙侠世界观来源` | `1 0 0 0` | `反` | `637 / — / — / —` | `UNALIGNED?` |
| `PG106` | `1 0 0 0` | `∅` | `214 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG12` | `1 0 0 0` | `∅` | `209 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG557` | `1 0 0 0` | `∅` | `206 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG57` | `1 0 0 0` | `∅` | `191 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG605` | `1 0 0 0` | `∅` | `202 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG81` | `1 0 0 0` | `∅` | `204 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-fantasy-power-arc/references/source-index.md+本轮最终来源修复与非同源边界` | `1 0 0 0` | `∅` | `927 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+返工后优先协议` | `1 0 0 0` | `∅` | `509 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+快速决策表先选型再查规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+表1超自然兑现度五档全篇只能占一档中途换档=失信` | `1 0 0 0` | `∅` | `594 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+表2禁忌双支按叙事功能选` | `1 0 0 0` | `∅` | `346 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+表3预言三型×命运知情度` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+核心规则60条精选细则见references` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+一英雄成长m族→referencesheroesandbosses.md` | `1 0 0 0` | `∅` | `1261 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+二boss与攻略be族→referencesheroesandbosses.md` | `1 0 0 0` | `∅` | `1041 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+三信物与道具af族→referencestokensanditems.md` | `1 0 0 0` | `∅` | `1012 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+四骗局与身份cjk族→referencesdeceptionandidentit` | `1 0 0 0` | `∅` | `1598 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+五命运与禁忌dhil族→referencesfateandtaboo.md` | `1 0 0 0` | `∅` | `846 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+六世界与社群go压迫族→referencesworldandsociety.md` | `1 0 0 0` | `∅` | `1184 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+七情感与收束qrn族→referencesemotionandcraft.md` | `1 0 0 0` | `∅` | `595 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+使用流程` | `1 0 0 0` | `∅` | `290 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+反面清单negativetriggers` | `1 0 0 0` | `∅` | `312 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/SKILL.md+文件清单` | `1 0 0 0` | `例反败` | `711 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/counterexamples.md+体裁级反例整条规则不适用` | `1 0 0 0` | `∅` | `1022 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/counterexamples.md+场景级失效条件规则适用但有边界` | `1 0 0 0` | `∅` | `1388 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/counterexamples.md+源内显式反例文本自证` | `1 0 0 0` | `∅` | `741 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/counterexamples.md+使用纪律` | `1 0 0 0` | `∅` | `297 / — / — / —` | `UNALIGNED?` |
| `M3` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `M2` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `M8` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `M1` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `∅` | `468 / — / — / —` | `UNALIGNED?` |
| `H1` | `1 0 0 0` | `∅` | `468 / — / — / —` | `UNALIGNED?` |
| `I1` | `1 0 0 0` | `∅` | `468 / — / — / —` | `UNALIGNED?` |
| `J2` | `1 0 0 0` | `∅` | `540 / — / — / —` | `UNALIGNED?` |
| `J1` | `1 0 0 0` | `∅` | `540 / — / — / —` | `UNALIGNED?` |
| `Q7` | `1 0 0 0` | `∅` | `540 / — / — / —` | `UNALIGNED?` |
| `J5` | `1 0 0 0` | `∅` | `540 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/examples.md+用例4档2低魔长篇的兑现度管理d表1` | `1 0 0 0` | `∅` | `347 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `L2` | `1 0 0 0` | `∅` | `377 / — / — / —` | `UNALIGNED?` |
| `L1` | `1 0 0 0` | `∅` | `377 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/examples.md+用例7收束选型对照n族` | `1 0 0 0` | `∅` | `395 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/examples.md+组合原则` | `1 0 0 0` | `∅` | `314 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+失败现象→诊断→出口` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+1.金手指开太早中期无力` | `1 0 0 0` | `∅` | `345 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+2.boss秒杀或拖成流水账` | `1 0 0 0` | `∅` | `258 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+3.骗局被读者提前看穿` | `1 0 0 0` | `∅` | `269 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+4.骗局穿帮太快剧情需要多撑几章` | `1 0 0 0` | `∅` | `243 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+5.禁忌违反显得蠢` | `1 0 0 0` | `规怎` | `240 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+6.预言线变成说明文` | `1 0 0 0` | `∅` | `214 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+7.超自然分寸失控读者说"都行了还装神秘"` | `1 0 0 0` | `∅` | `256 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+8.信物变成麦高芬读者不在乎它去哪` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+9.动物伙伴工具化` | `1 0 0 0` | `∅` | `173 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+10.恐惧供能反派被读者嘲笑` | `1 0 0 0` | `∅` | `185 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+11.英雄成长跳级新人突然无敌` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+12.收尾泄气` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+13.双主角同质化` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+14.誓言约定线无张力` | `1 0 0 0` | `∅` | `254 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+全局降级策略` | `1 0 0 0` | `规反` | `377 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/failure-modes.md+覆盖边界声明` | `1 0 0 0` | `∅` | `282 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/deception-and-identity.md+j族骗局与真相工程` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `J3` | `1 0 0 0` | `怎` | `443 / — / — / —` | `UNALIGNED?` |
| `J4` | `1 0 0 0` | `怎` | `438 / — / — / —` | `UNALIGNED?` |
| `J6` | `1 0 0 0` | `∅` | `306 / — / — / —` | `UNALIGNED?` |
| `J7` | `1 0 0 0` | `怎` | `449 / — / — / —` | `UNALIGNED?` |
| `J8` | `1 0 0 0` | `怎` | `384 / — / — / —` | `UNALIGNED?` |
| `J9` | `1 0 0 0` | `∅` | `211 / — / — / —` | `UNALIGNED?` |
| `J10` | `1 0 0 0` | `∅` | `201 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/deception-and-identity.md+c族识别与验证` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `规怎` | `703 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `239 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `179 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/deception-and-identity.md+k族冒名双身变形` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `K1` | `1 0 0 0` | `∅` | `220 / — / — / —` | `UNALIGNED?` |
| `K2` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `K3` | `1 0 0 0` | `∅` | `221 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/deception-and-identity.md+使用检查单` | `1 0 0 0` | `败` | `262 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/emotion-and-craft.md+q族情感结构` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `Q1` | `1 0 0 0` | `怎` | `381 / — / — / —` | `UNALIGNED?` |
| `Q2` | `1 0 0 0` | `怎反` | `414 / — / — / —` | `UNALIGNED?` |
| `Q3` | `1 0 0 0` | `怎` | `440 / — / — / —` | `UNALIGNED?` |
| `Q4` | `1 0 0 0` | `∅` | `237 / — / — / —` | `UNALIGNED?` |
| `Q5` | `1 0 0 0` | `∅` | `206 / — / — / —` | `UNALIGNED?` |
| `Q6` | `1 0 0 0` | `∅` | `226 / — / — / —` | `UNALIGNED?` |
| `Q8` | `1 0 0 0` | `∅` | `198 / — / — / —` | `UNALIGNED?` |
| `Q9` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `Q10` | `1 0 0 0` | `∅` | `201 / — / — / —` | `UNALIGNED?` |
| `Q11` | `1 0 0 0` | `∅` | `238 / — / — / —` | `UNALIGNED?` |
| `Q12` | `1 0 0 0` | `∅` | `252 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/emotion-and-craft.md+r族感知与留白工艺` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `25 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `∅` | `25 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `204 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/emotion-and-craft.md+n族收束术五式` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `N1` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `N2` | `1 0 0 0` | `∅` | `165 / — / — / —` | `UNALIGNED?` |
| `N3` | `1 0 0 0` | `∅` | `218 / — / — / —` | `UNALIGNED?` |
| `N4` | `1 0 0 0` | `∅` | `195 / — / — / —` | `UNALIGNED?` |
| `N5` | `1 0 0 0` | `∅` | `130 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/emotion-and-craft.md+使用检查单` | `1 0 0 0` | `∅` | `263 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+d族超自然兑现度谱系五档` | `1 0 0 0` | `∅` | `1431 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+h族禁忌gestabu双支` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `H2` | `1 0 0 0` | `怎` | `375 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+i族不可能任务` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `I2` | `1 0 0 0` | `怎例适` | `361 / — / — / —` | `UNALIGNED?` |
| `I3` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+l族预言与命运治理` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `L3` | `1 0 0 0` | `∅` | `198 / — / — / —` | `UNALIGNED?` |
| `L4` | `1 0 0 0` | `∅` | `367 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+配套誓言体系` | `1 0 0 0` | `∅` | `533 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md+使用检查单` | `1 0 0 0` | `∅` | `292 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/heroes-and-bosses.md+m族英雄成长公式` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M4` | `1 0 0 0` | `怎` | `415 / — / — / —` | `UNALIGNED?` |
| `M5` | `1 0 0 0` | `怎` | `277 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `怎` | `399 / — / — / —` | `UNALIGNED?` |
| `M7` | `1 0 0 0` | `怎` | `376 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/heroes-and-bosses.md+m9m10首尾同型+命运预付` | `1 0 0 0` | `怎` | `263 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/heroes-and-bosses.md+b族boss无敌怪弱点` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/heroes-and-bosses.md+e族攻略参观结构` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `91 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/rework-decision.md+何时调用及必须输入` | `1 0 0 0` | `∅` | `428 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/rework-decision.md+四个不同冲突点不允许混作“神器坏了”` | `1 0 0 0` | `∅` | `1768 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/rework-decision.md+冲突处置` | `1 0 0 0` | `∅` | `834 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/rework-decision.md+p输出合同` | `1 0 0 0` | `∅` | `313 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/tokens-and-items.md+a族信物经济学` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `怎` | `525 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `怎` | `468 / — / — / —` | `UNALIGNED?` |
| `A4` | `1 0 0 0` | `怎` | `392 / — / — / —` | `UNALIGNED?` |
| `A5` | `1 0 0 0` | `怎` | `490 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/tokens-and-items.md+f族强力道具时机学` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `F1` | `1 0 0 0` | `规怎` | `574 / — / — / —` | `UNALIGNED?` |
| `F2` | `1 0 0 0` | `怎` | `508 / — / — / —` | `UNALIGNED?` |
| `F3` | `1 0 0 0` | `怎` | `321 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/tokens-and-items.md+使用检查单` | `1 0 0 0` | `∅` | `296 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+g族恩义网络` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `G1` | `1 0 0 0` | `怎检` | `571 / — / — / —` | `UNALIGNED?` |
| `G2` | `1 0 0 0` | `规怎适` | `460 / — / — / —` | `UNALIGNED?` |
| `G3` | `1 0 0 0` | `怎` | `430 / — / — / —` | `UNALIGNED?` |
| `G4` | `1 0 0 0` | `∅` | `253 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+o族世界构筑` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `O1` | `1 0 0 0` | `怎` | `368 / — / — / —` | `UNALIGNED?` |
| `O2` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `O3` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `O4` | `1 0 0 0` | `∅` | `239 / — / — / —` | `UNALIGNED?` |
| `O5` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `O6` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `O7` | `1 0 0 0` | `∅` | `210 / — / — / —` | `UNALIGNED?` |
| `O8` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `O9` | `1 0 0 0` | `∅` | `152 / — / — / —` | `UNALIGNED?` |
| `O10` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压迫族恐惧权力与迷信战` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压1恐惧权力三步破解` | `1 0 0 0` | `怎例适` | `479 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压2迷信心理战四件套` | `1 0 0 0` | `∅` | `374 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压3革命循环讽刺收尾` | `1 0 0 0` | `∅` | `240 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压4疯狂科学家四件套` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+压5群众羞辱经济` | `1 0 0 0` | `∅` | `214 / — / — / —` | `UNALIGNED?` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md+使用检查单` | `1 0 0 0` | `∅` | `264 / — / — / —` | `UNALIGNED?` |
| `PG123` | `1 0 0 0` | `∅` | `134 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG503` | `1 0 0 0` | `∅` | `179 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG640` | `1 0 0 0` | `∅` | `186 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG85` | `1 0 0 0` | `∅` | `149 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG90` | `1 0 0 0` | `∅` | `145 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-xianxia-plot-forge/sources-index.md+去重声明` | `1 0 0 0` | `∅` | `326 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wuxia-xianxia-plot-forge/sources-index.md+完整sha256冻结用` | `1 0 0 0` | `∅` | `143 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+0.这个skill是什么不是什么` | `1 0 0 0` | `例` | `1373 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+1.触发条件什么时候用这个skill` | `1 0 0 0` | `∅` | `837 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+2.负触发什么时候不要用这个skill` | `1 0 0 0` | `规例适` | `986 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+4.分支判断路由到references` | `1 0 0 0` | `∅` | `1817 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+5.输出格式` | `1 0 0 0` | `∅` | `69 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+判定` | `1 0 0 0` | `规适` | `162 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+依据逐字引文+锚点` | `1 0 0 0` | `∅` | `162 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+操作` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+边界与反例` | `1 0 0 0` | `适` | `85 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+未决需你补充` | `1 0 0 0` | `规适` | `282 / — / — / —` | `UNALIGNED?` |
| `F4` | `1 0 0 0` | `∅` | `1051 / — / — / —` | `UNALIGNED?` |
| `F5` | `1 0 0 0` | `∅` | `1051 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+7.质量状态必须随答案附带不得省略` | `1 0 0 0` | `∅` | `539 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+8a.规则总数与分布如实` | `1 0 0 0` | `规适` | `566 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/SKILL.md+8.来源与覆盖如实` | `1 0 0 0` | `∅` | `537 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `166 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r001给超自然能力配一份"边界声明"边界写在角色自己的台词里` | `1 0 0 0` | `规怎例反适` | `1558 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r002能力授予写成"三件套书面条款+代价+破功面"` | `1 0 0 0` | `规怎反适` | `1654 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r003让条款的字面漏洞由主角当场发现并在后文第三次使用时兑现` | `1 0 0 0` | `规怎反适` | `1166 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r004把"能力的收益"主要写在信息与行动上武力干预全书限一次且必须短` | `1 0 0 0` | `规怎反适` | `1406 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r005能力与代价同源升级的通道就是毁灭的通道` | `1 0 0 0` | `规怎反适` | `1336 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r006统治型强者写"威慑经济学"不写高频暴力` | `1 0 0 0` | `规怎反适败` | `1354 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r007通灵窥探类能力用"成瘾模型"写不用"天赋模型"` | `1 0 0 0` | `规怎反适` | `1428 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r008为不可能任务写一份"荒谬但可执行"的操作手册并在高潮让其中一条失效` | `1 0 0 0` | `怎反适` | `850 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r009命运名册类装置必须"界面化"落成可操作的物件与工序` | `1 0 0 0` | `规怎反适` | `1463 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r010护佑恩赐必须写"可失效条款"并配一个可观察的失效信号` | `1 0 0 0` | `规怎反适` | `1246 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r011名号由伤痕身体变化授予不由战功授予` | `1 0 0 0` | `怎反适` | `856 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+r012低心智异心智角色能力边界=教学边界用"未被想到"写心智阶段` | `1 0 0 0` | `怎反适` | `1149 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md+本节红线仅记录不蒸馏为技法` | `1 0 0 0` | `∅` | `634 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r020把"恶"行政化阴谋以公文推进暴力被程序稀释` | `1 0 0 0` | `规怎反适` | `1052 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r021官方死亡先行先让假死成为公文再让生者露面` | `1 0 0 0` | `怎适` | `576 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r022把群体写成"会换挡的角色"每次换挡必须有具体触发事件` | `1 0 0 0` | `规怎反适` | `1256 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r023让位拒冕按三段完成当众拒绝→当场提名→附公开条件` | `1 0 0 0` | `规怎反适` | `1066 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r024政治承诺写成"可当场验证的交付物"不写空头保证` | `1 0 0 0` | `怎适败` | `696 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r025制度条文进入异族异心视角时被"重译"为其可观察的行为类别` | `1 0 0 0` | `规怎适` | `995 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r026权威可以恐惧可以承认无知但决策链与执行链不中断` | `1 0 0 0` | `怎适` | `683 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r027用"语言符号上限"解释"为什么不起义"结构性解释优于道德解释` | `1 0 0 0` | `怎反适` | `946 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r028让一次失败的集体行动意外产出节奏合唱把政治失败转化为艺术起源` | `1 0 0 0` | `怎适败` | `624 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r029异界秘境的守门人也要给"失职即死"的动机` | `1 0 0 0` | `怎适` | `725 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r030司法审判写成"奇观"空间表决器举证困境都要可视化` | `1 0 0 0` | `怎适` | `954 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r031以"改革敕令"替代复仇作为暴力体系的收束` | `1 0 0 0` | `规怎反适` | `1027 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r032用系统内个体选择显示“制度”与“所有人”不是一回事` | `1 0 0 0` | `规怎适` | `1292 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+r033门派部族的"准入测试"判定"不伤害"而非"赢"` | `1 0 0 0` | `怎适败` | `704 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md+本节红线仅记录` | `1 0 0 0` | `∅` | `1033 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r040先写“为什么会认错”再让错认持续` | `1 0 0 0` | `规怎适` | `981 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r041身份证据按“可伪造性与取得成本”排序而不是固定媒介排序` | `1 0 0 0` | `规怎适` | `1070 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r042让关键身份信物有可追踪的“持有与用途状态”` | `1 0 0 0` | `规怎检适` | `1054 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r043把“自称否认”当人物行为不当真伪判据` | `1 0 0 0` | `规怎适` | `1001 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r044敌口认证关键身份节点让敌人说出口` | `1 0 0 0` | `怎适` | `497 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r045当身份会被制度事件“固化”时用明确时间窗制造压力` | `1 0 0 0` | `规怎适` | `923 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r046用先前可复核的差异完成“公平穿帮”` | `1 0 0 0` | `规怎适` | `1112 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r047档案链五级递进日记→照片画像→信物→旧证人→时代最新技术` | `1 0 0 0` | `规怎适` | `1074 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r048名字三层用法真名破阵秘名请愿官方改名作史笔` | `1 0 0 0` | `怎适` | `788 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r049化名被"登记册旧称当众试名"戳穿不靠供词` | `1 0 0 0` | `怎适` | `493 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r050唯一不信者律反派阵营中必有一位识破者` | `1 0 0 0` | `规怎适` | `936 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r051双画像法同一人由情人与情敌分别描画视角即肖像学` | `1 0 0 0` | `怎适` | `476 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r052显像写成"自混沌排列成形"并让施术者自陈代价` | `1 0 0 0` | `怎适` | `1091 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r053保留对超自然解释不利的证据是"可能为真"的最高级装置` | `1 0 0 0` | `怎适` | `758 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r054镜的功能在本批三书互不相同融合时不可合并` | `1 0 0 0` | `规怎反适` | `1058 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+r055绰号由"身体特征+众人称呼"生成触发词以三次为最低引爆阈值` | `1 0 0 0` | `怎适` | `1529 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md+本节红线仅记录` | `1 0 0 0` | `∅` | `957 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r060契约条款写到"字面可钻"的精度双向罚则+镜像条款` | `1 0 0 0` | `规怎适` | `1788 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r061惩罚与罪同器同地同式镜像度=正义感强度` | `1 0 0 0` | `规怎反适` | `1587 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r062誓言条款字面兑现报应不可商谈` | `1 0 0 0` | `规怎适` | `1023 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r063禁语任务以"不许笑哭说"作任务核心破誓即归零重来` | `1 0 0 0` | `怎适` | `835 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r064破戒由主角的优点触发而非疏忽` | `1 0 0 0` | `规怎适败` | `790 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r065资质内化到身体比外挂器物更耐读器物可失资质不可失` | `1 0 0 0` | `规怎适` | `902 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r066让主角以"自残通过字面考验"再让血迹暴露手段` | `1 0 0 0` | `怎适` | `720 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r067契约陷阱靠"对方命名己方不解其义"即可成立无需欺骗` | `1 0 0 0` | `规怎适` | `925 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r068面对更强索取者先做管辖权转移而不是对抗` | `1 0 0 0` | `怎适` | `490 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r069保护写成"消失"并把回归条件写进同一句话` | `1 0 0 0` | `怎反适` | `998 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r070禁令由被爱者以"同一性句式"说出且必须来自对方之口` | `1 0 0 0` | `怎适` | `760 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r071契约的履行在本批给出相反裁决不可写成跨书共识` | `1 0 0 0` | `规怎适` | `1096 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r072誓言绑定在"可失去之物"上羊群灵魂前途国土丰饶` | `1 0 0 0` | `怎适` | `561 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r073以"物品未被想到"写阶段或让主角做出半成品再看敌方成品` | `1 0 0 0` | `怎适` | `500 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+r074迟到的赦免把时间差本身写成悲剧引擎` | `1 0 0 0` | `怎适` | `677 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md+本节红线仅记录` | `1 0 0 0` | `∅` | `976 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r080引荐链每一环帮助者只知道下一环不给全知向导` | `1 0 0 0` | `规怎适` | `1081 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r081恩义回报三件套施救→致谢→反问需求` | `1 0 0 0` | `怎适` | `533 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r082恩义债务链写"四级对账"救命→债务宣言→生命偿付→财物偿付` | `1 0 0 0` | `规怎适` | `837 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r083撒径计退行时以抛洒物改变追击成本并在镜像人物间变奏` | `1 0 0 0` | `怎适` | `612 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r084藏身处先报硬指标出口数补给态勘探过程"三出口"为经典配置` | `1 0 0 0` | `规怎适` | `646 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r085混乱即窗口把越狱刺杀夺权安排在系统注意力被单一事件吸走的时刻` | `1 0 0 0` | `怎适` | `930 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r086夺获攻方兵器并反用完成攻防势能翻转` | `1 0 0 0` | `怎适` | `617 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r087分线叙事用"硬机制"交接不用巧合擦肩剪辑给读者全知痛感` | `1 0 0 0` | `规怎适` | `997 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r088求援链逐级上升并在顶端以"过罚比例"为赦免理由` | `1 0 0 0` | `怎适` | `784 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r089指引物以"张力"回报正确以消失惩戒回头` | `1 0 0 0` | `规怎适` | `766 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r090逃跑道具随身藏"耳中"一耳一物分段使用` | `1 0 0 0` | `规怎适` | `729 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r091怪物反派以其"家宅"写体貌睡处伙食建材配方作息表` | `1 0 0 0` | `怎适` | `544 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r092反派老妇妖婆的攻防写足日常细节职衔沉睡针口味对证故事拖延` | `1 0 0 0` | `怎适` | `552 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r093以劳役作学费肯做工者得道嫌低贱者被"假装无知"挡回` | `1 0 0 0` | `怎适` | `572 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r094声纹识人远距离身份识别用战吼号角母语对答不依赖视力` | `1 0 0 0` | `怎反适` | `645 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r095以"身体计时"替代钟表且时间焦虑随文明度递减` | `1 0 0 0` | `怎适` | `1080 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r096双计时器竞速让"手慢"与"月快"同时可见` | `1 0 0 0` | `怎适` | `469 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+r097影子四幕获影→统治→人形化→卸影内心恶的外化弧线` | `1 0 0 0` | `怎适` | `1306 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md+本节红线仅记录` | `1 0 0 0` | `∅` | `439 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r100先拆穿一次伪超自然读者才会相信后面的真超自然` | `1 0 0 0` | `规怎例适` | `894 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r101给讲述者一个瑕疵可信度反而上升` | `1 0 0 0` | `怎适` | `593 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r102机制灵异每种超自然存在至少配一条可执行破解法并在终局兑现` | `1 0 0 0` | `规怎适` | `1041 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r103把武器写成"可耗弹药"现编的韵获胜卡壳与库存都是节拍` | `1 0 0 0` | `怎适` | `553 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r104反派的憎恨写成"恨其所无"` | `1 0 0 0` | `怎适` | `412 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r105物证灵异超自然必留可检视可存档的实物` | `1 0 0 0` | `规怎适` | `1106 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r106以生物学结构性错位定义压迫者使其无需动机且无法被说服` | `1 0 0 0` | `怎适` | `793 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r107恐惧是知识与想象的函数同一场景给两个视角各写一遍` | `1 0 0 0` | `怎适` | `650 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r108恐怖周期化节律间隙让被压者重燃侥幸` | `1 0 0 0` | `规怎适` | `787 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r109不可见者以"二手痕迹"显形并以三重验证立足` | `1 0 0 0` | `规怎适` | `789 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r110结尾保留"可能真可能假"的双重解释把类型升为本体论悬置` | `1 0 0 0` | `规怎适` | `1253 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r111沉迷写成"系统空转"不写主角憔悴` | `1 0 0 0` | `怎适` | `525 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r112信念作为准入条件"欲见者须先信"并让它随注意力衰减` | `1 0 0 0` | `规怎反适` | `952 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r113不信的社会机制让权威覆盖亲眼所见并让未学习者作最后证人` | `1 0 0 0` | `怎适` | `631 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r114恐惧必须被"逻辑的醒悟"打破` | `1 0 0 0` | `怎适` | `520 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r115反派也在受规则约束威胁才可信` | `1 0 0 0` | `怎适` | `604 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r116解放不是普遍解让一个被释放者拒绝自由` | `1 0 0 0` | `怎反适` | `692 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r118恶的饥饿洞把反派动机写成"填不满的空洞"而非目标` | `1 0 0 0` | `怎适` | `836 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+r117语言排版可承载音量与停顿体裁限定` | `1 0 0 0` | `怎适` | `605 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md+本节红线仅记录` | `1 0 0 0` | `∅` | `1069 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r130官方叙事三件套报纸讣告+纪念碑+大众遗忘与真相三线并行` | `1 0 0 0` | `规怎适` | `859 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r131系列续作缝合约按四级提及→概要→人物共享→规则共享` | `1 0 0 0` | `规怎适` | `845 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r132元小说终局让角色读不到自己的故事自我抹除即永生` | `1 0 0 0` | `怎适` | `784 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r133收束软化律战败族迁走或归化为家神不留死敌` | `1 0 0 0` | `规怎适` | `821 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r134推源论收束把故事焊到一个自然特征上` | `1 0 0 0` | `怎适` | `521 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r135代价物在结尾原样归还把交易闭合成圆` | `1 0 0 0` | `怎适` | `506 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r136让反派按自己的本质受罚爱美者毁容并在惩罚中保持其本质` | `1 0 0 0` | `怎适` | `500 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r137功绩不被承认时用"对称的两段驱逐"写尽` | `1 0 0 0` | `怎适` | `448 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r138赦免先于请求发生且当事人不知道` | `1 0 0 0` | `怎适` | `384 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r139判词分出"自锁"与"他锁"并给出例外条款` | `1 0 0 0` | `怎适` | `705 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r140守护者看向被留下者而不是离场者` | `1 0 0 0` | `怎适` | `503 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r141环形收束结尾落回开篇的同一意象但状态反转` | `1 0 0 0` | `规怎适` | `725 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r142用"有主题的歌vs无主题的音乐"解释"为什么必须离开"` | `1 0 0 0` | `怎适` | `575 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r143收束于省略以"蒙面的真理"拒绝描写终局` | `1 0 0 0` | `怎适` | `645 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r144反高潮宣言在正文前声明"结尾只指示真正的开始"` | `1 0 0 0` | `怎适` | `549 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r145清算清单收尾反派按罪配刑功臣按功配赏一段话道德结算` | `1 0 0 0` | `怎适` | `491 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r146世代循环条件句收尾` | `1 0 0 0` | `怎适` | `626 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r147信念衰减律飞行失效的原因不是生疏而是不再相信` | `1 0 0 0` | `怎适` | `604 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r148变形惩罚的可撤销性在本批给出相反裁决` | `1 0 0 0` | `怎适` | `1186 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r149儿童低龄视角的道德试炼把诱惑外化为一个对话者` | `1 0 0 0` | `怎适` | `707 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+r150谎言与改正的双向物理规则长鼻标记类` | `1 0 0 0` | `规怎适` | `864 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md+本节红线仅记录` | `1 0 0 0` | `∅` | `832 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/08-conflicts-and-redlines.md+u系列未裁决冲突相反裁决不要把任一分支强定为全体规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `U-01` | `1 0 0 0` | `规` | `576 / — / — / —` | `UNALIGNED?` |
| `U-02` | `1 0 0 0` | `∅` | `331 / — / — / —` | `UNALIGNED?` |
| `U-03` | `1 0 0 0` | `规适` | `593 / — / — / —` | `UNALIGNED?` |
| `U-04` | `1 0 0 0` | `规反` | `467 / — / — / —` | `UNALIGNED?` |
| `U-05` | `1 0 0 0` | `规` | `564 / — / — / —` | `UNALIGNED?` |
| `U-06` | `1 0 0 0` | `∅` | `517 / — / — / —` | `UNALIGNED?` |
| `U-07` | `1 0 0 0` | `∅` | `378 / — / — / —` | `UNALIGNED?` |
| `U-08` | `1 0 0 0` | `规反` | `294 / — / — / —` | `UNALIGNED?` |
| `U-09` | `1 0 0 0` | `规` | `521 / — / — / —` | `UNALIGNED?` |
| `U-10` | `1 0 0 0` | `∅` | `573 / — / — / —` | `UNALIGNED?` |
| `U-11` | `1 0 0 0` | `规` | `514 / — / — / —` | `UNALIGNED?` |
| `U-12` | `1 0 0 0` | `规反` | `383 / — / — / —` | `UNALIGNED?` |
| `U-13` | `1 0 0 0` | `∅` | `307 / — / — / —` | `UNALIGNED?` |
| `U-14` | `1 0 0 0` | `规反` | `331 / — / — / —` | `UNALIGNED?` |
| `U-15` | `1 0 0 0` | `∅` | `347 / — / — / —` | `UNALIGNED?` |
| `U-16` | `1 0 0 0` | `∅` | `254 / — / — / —` | `UNALIGNED?` |
| `U-17` | `1 0 0 0` | `∅` | `248 / — / — / —` | `UNALIGNED?` |
| `U-18` | `1 0 0 0` | `∅` | `201 / — / — / —` | `UNALIGNED?` |
| `U-19` | `1 0 0 0` | `∅` | `242 / — / — / —` | `UNALIGNED?` |
| `U-20` | `1 0 0 0` | `∅` | `276 / — / — / —` | `UNALIGNED?` |
| `U-21` | `1 0 0 0` | `∅` | `414 / — / — / —` | `UNALIGNED?` |
| `U-22` | `1 0 0 0` | `规` | `418 / — / — / —` | `UNALIGNED?` |
| `U-23` | `1 0 0 0` | `∅` | `271 / — / — / —` | `UNALIGNED?` |
| `U-24` | `1 0 0 0` | `∅` | `246 / — / — / —` | `UNALIGNED?` |
| `U-25` | `1 0 0 0` | `规` | `181 / — / — / —` | `UNALIGNED?` |
| `U-26` | `1 0 0 0` | `∅` | `290 / — / — / —` | `UNALIGNED?` |
| `PG78` | `1 0 0 0` | `∅` | `291 / — / — / —` | `UNALIGNED?` |
| `PG364` | `1 0 0 0` | `∅` | `271 / — / — / —` | `UNALIGNED?` |
| `PG310` | `1 0 0 0` | `∅` | `316 / — / — / —` | `UNALIGNED?` |
| `PG592` | `1 0 0 0` | `∅` | `243 / — / — / —` | `UNALIGNED?` |
| `PG16` | `1 0 0 0` | `∅` | `215 / — / — / —` | `UNALIGNED?` |
| `PG500` | `1 0 0 0` | `∅` | `207 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/08-conflicts-and-redlines.md+红线清单仅作历史记录不蒸馏为技法` | `1 0 0 0` | `∅` | `4579 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/08-conflicts-and-redlines.md+计数口径供manifest的fusion字段核对` | `1 0 0 0` | `规` | `491 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r001能力边界可兑现` | `1 0 0 0` | `怎例反适` | `535 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r020制度性恶意` | `1 0 0 0` | `怎例反适` | `537 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r046身份穿帮靠预置证据` | `1 0 0 0` | `怎例反检适` | `662 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r060契约可被角色钻字面` | `1 0 0 0` | `怎例反适` | `553 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r080求助链的下一环` | `1 0 0 0` | `怎例反适` | `548 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r100伪怪谈去魅先行` | `1 0 0 0` | `怎例反适` | `537 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r130记忆权与官方叙事` | `1 0 0 0` | `怎例反适` | `556 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+r145清算与开放结尾取舍` | `1 0 0 0` | `怎例反适` | `652 / — / — / —` | `UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `B02` | `1 0 0 0` | `∅` | `443 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/source-index.md+汇总` | `1 0 0 0` | `∅` | `934 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/source-index.md+逐书索引` | `1 0 0 0` | `∅` | `5606 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/source-index.md+去重说明来源族` | `1 0 0 0` | `∅` | `1578 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG325` | `1 0 0 0` | `∅` | `99 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG708` | `1 0 0 0` | `∅` | `123 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `fantasy-adventure-structure-lab/references/version-and-provenance.md+全部来源与作用` | `1 0 0 0` | `∅` | `3697 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+0.这是什么` | `1 0 0 0` | `∅` | `1165 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+1.触发负触发` | `1 0 0 0` | `∅` | `282 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+触发满足任一` | `1 0 0 0` | `败` | `793 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+负触发不要用` | `1 0 0 0` | `规` | `672 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+2.输入权限` | `1 0 0 0` | `检` | `864 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `例` | `1491 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+4.最小工作流3步内开始` | `1 0 0 0` | `∅` | `609 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+5.输出与owner` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+本skill负责` | `1 0 0 0` | `例检` | `573 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+本skill不负责交回用户其他流程` | `1 0 0 0` | `∅` | `619 / — / — / —` | `UNALIGNED?` |
| `RC-04` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-06` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-08` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-10` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-01` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-03` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-05` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-02` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-07` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `RC-09` | `1 0 0 0` | `∅` | `999 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+7.失败退出` | `1 0 0 0` | `∅` | `1333 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+8.证据边界与验证状态` | `1 0 0 0` | `例适` | `1378 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/SKILL.md+9.文件地图` | `1 0 0 0` | `规` | `919 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+0.通用preamble三条都要做` | `1 0 0 0` | `∅` | `308 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+1.边界判断不到1分钟` | `1 0 0 0` | `∅` | `678 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+2.规划还没有稿` | `1 0 0 0` | `∅` | `1322 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+3.诊断有稿有成稿设定` | `1 0 0 0` | `∅` | `1699 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+4.核账前有承诺后未兑现` | `1 0 0 0` | `∅` | `977 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/design-and-diagnosis.md+5.三条共用的收尾` | `1 0 0 0` | `规检` | `273 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/rules.md+0.读法` | `1 0 0 0` | `规检` | `1616 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/rules.md+1.规则索引` | `1 0 0 0` | `∅` | `1705 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+1.适用不适用` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+1.1适用本skill能处理` | `1 0 0 0` | `例` | `318 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+1.2不适用本书本skill都不处理` | `1 0 0 0` | `∅` | `838 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+1.3本批内不适用的几本书几条线明确列出避免误用` | `1 0 0 0` | `∅` | `811 / — / — / —` | `UNALIGNED?` |
| `CC-01` | `1 0 0 0` | `∅` | `1445 / — / — / —` | `UNALIGNED?` |
| `CC-04` | `1 0 0 0` | `∅` | `1445 / — / — / —` | `UNALIGNED?` |
| `CC-03` | `1 0 0 0` | `∅` | `1445 / — / — / —` | `UNALIGNED?` |
| `CC-02` | `1 0 0 0` | `∅` | `1445 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+3.不可调和的冲突并列保留不伪造共识` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+3.2冲突二违反后果能否免除` | `1 0 0 0` | `∅` | `177 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+4.单来源参数清单只作可选项不作硬门` | `1 0 0 0` | `∅` | `708 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/scope-and-conflicts.md+5.验证状态` | `1 0 0 0` | `∅` | `355 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/references/source-index.md+2.规则→来源覆盖与关键行号` | `1 0 0 0` | `∅` | `1939 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `supernatural-power-craft/references/source-index.md+3.不适用清单重复强调` | `1 0 0 0` | `例` | `308 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `supernatural-power-craft/references/source-index.md+4.引文回源方式` | `1 0 0 0` | `∅` | `507 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `DR-01` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-02` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-10` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-09` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-05` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-06` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-04` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-03` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-07` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `DR-08` | `1 0 0 0` | `∅` | `1802 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/templates/diagnosis-report.md+输出纪律` | `1 0 0 0` | `规检` | `361 / — / — / —` | `UNALIGNED?` |
| `PS-11` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-02` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-04` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-10` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-08` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-05` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-07` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-12` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-06` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-01` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-03` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `PS-09` | `1 0 0 0` | `例适` | `2220 / — / — / —` | `UNALIGNED?` |
| `supernatural-power-craft/templates/power-system-canvas.md+缺口清单自动汇总` | `1 0 0 0` | `∅` | `282 / — / — / —` | `UNALIGNED?` |

---

## 题材 05 科幻（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 05 科幻

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`sci-fi-future-plot-forge`、`sci-fi-novum-world-forge`、`science-fiction-conceptual-reveal`、`science-fiction-craft-b04`、`scifi-future-craft-b03`

**规则单元数 412；v3 对齐成功 8（1.9%）；对齐失败 UNALIGNED? 404（98.1%）**
**flag 计数**：BLOCK_LOST=8；SHRUNK=1；SOURCE_ONLY=29；UNALIGNED?=404

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `P4` | `1 0 0 0` | `∅` | `1847 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+使用须知先读` | `1 0 0 0` | `∅` | `756 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+主决策表` | `1 0 0 0` | `∅` | `1118 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+六域导航` | `1 0 0 0` | `∅` | `1367 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+三个诊断问题不是全域铁律` | `1 0 0 0` | `∅` | `1166 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+失败出口` | `1 0 0 0` | `∅` | `398 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/SKILL.md+来源与审计` | `1 0 0 0` | `反` | `383 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `例` | `476 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `∅` | `450 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `∅` | `434 / — / — / —` | `UNALIGNED?` |
| `A4` | `1 0 0 0` | `检` | `447 / — / — / —` | `UNALIGNED?` |
| `A5` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/anti-examples.md+附两条结构性提醒` | `1 0 0 0` | `例` | `529 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `规` | `547 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `规` | `488 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `规` | `444 / — / — / —` | `UNALIGNED?` |
| `E5` | `1 0 0 0` | `规` | `452 / — / — / —` | `UNALIGNED?` |
| `E6` | `1 0 0 0` | `∅` | `616 / — / — / —` | `UNALIGNED?` |
| `E7` | `1 0 0 0` | `∅` | `588 / — / — / —` | `UNALIGNED?` |
| `E8` | `1 0 0 0` | `规适` | `603 / — / — / —` | `UNALIGNED?` |
| `E9` | `1 0 0 0` | `规` | `399 / — / — / —` | `UNALIGNED?` |
| `E10` | `1 0 0 0` | `规` | `441 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+自检顺序四查` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+第一查是否真的需要显式代价外部性` | `1 0 0 0` | `例` | `720 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+第二查冲突是否需要可反制边界` | `1 0 0 0` | `适` | `665 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+第三查能力限制采用什么形式` | `1 0 0 0` | `规败` | `560 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+第四查收束选式` | `1 0 0 0` | `败` | `523 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+五类死法速查详表见antiexamples.md` | `1 0 0 0` | `∅` | `667 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/failure-modes.md+终极出口` | `1 0 0 0` | `∅` | `430 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `规适` | `1601 / — / — / —` | `UNALIGNED?` |
| `CB-01` | `1 0 0 0` | `规适` | `1601 / — / — / —` | `UNALIGNED?` |
| `CB-02` | `1 0 0 0` | `规适` | `1624 / — / — / —` | `UNALIGNED?` |
| `CB-03` | `1 0 0 0` | `规适` | `1340 / — / — / —` | `UNALIGNED?` |
| `CB-04` | `1 0 0 0` | `规适` | `1474 / — / — / —` | `UNALIGNED?` |
| `CB-05` | `1 0 0 0` | `规适` | `1095 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/created-beings.md+收束技法族12` | `1 0 0 0` | `∅` | `460 / — / — / —` | `UNALIGNED?` |
| `EC-01` | `1 0 0 0` | `规适` | `1410 / — / — / —` | `UNALIGNED?` |
| `PG72` | `1 0 0 0` | `规适` | `1410 / — / — / —` | `UNALIGNED?` |
| `EC-02` | `1 0 0 0` | `规适` | `1439 / — / — / —` | `UNALIGNED?` |
| `F-17` | `1 0 0 0` | `规适` | `1649 / — / — / —` | `UNALIGNED?` |
| `EC-03` | `1 0 0 0` | `规适` | `1649 / — / — / —` | `UNALIGNED?` |
| `P-09` | `1 0 0 0` | `规适` | `1649 / — / — / —` | `UNALIGNED?` |
| `EC-04` | `1 0 0 0` | `规适` | `1127 / — / — / —` | `UNALIGNED?` |
| `EC-05` | `1 0 0 0` | `规适` | `1136 / — / — / —` | `UNALIGNED?` |
| `PG83` | `1 0 0 0` | `规适` | `1136 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/expedition-combat.md+收束技法族12` | `1 0 0 0` | `∅` | `467 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `规适` | `1782 / — / — / —` | `UNALIGNED?` |
| `HT-01` | `1 0 0 0` | `规适` | `1782 / — / — / —` | `UNALIGNED?` |
| `HT-02` | `1 0 0 0` | `规适` | `1566 / — / — / —` | `UNALIGNED?` |
| `HT-03` | `1 0 0 0` | `规适` | `1282 / — / — / —` | `UNALIGNED?` |
| `HT-04` | `1 0 0 0` | `规适` | `1356 / — / — / —` | `UNALIGNED?` |
| `HT-05` | `1 0 0 0` | `∅` | `709 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/history-time.md+收束技法族12` | `1 0 0 0` | `∅` | `421 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `规适` | `1322 / — / — / —` | `UNALIGNED?` |
| `II-01` | `1 0 0 0` | `规适` | `1322 / — / — / —` | `UNALIGNED?` |
| `II-02` | `1 0 0 0` | `规适` | `1160 / — / — / —` | `UNALIGNED?` |
| `II-03` | `1 0 0 0` | `规适` | `1889 / — / — / —` | `UNALIGNED?` |
| `II-04` | `1 0 0 0` | `规适` | `1146 / — / — / —` | `UNALIGNED?` |
| `II-05` | `1 0 0 0` | `∅` | `532 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/identity-infiltration.md+收束技法族12` | `1 0 0 0` | `∅` | `410 / — / — / —` | `UNALIGNED?` |
| `MW-01` | `1 0 0 0` | `规适` | `1748 / — / — / —` | `UNALIGNED?` |
| `MW-02` | `1 0 0 0` | `规适` | `914 / — / — / —` | `UNALIGNED?` |
| `MW-03` | `1 0 0 0` | `规适` | `1916 / — / — / —` | `UNALIGNED?` |
| `MW-04` | `1 0 0 0` | `∅` | `396 / — / — / —` | `UNALIGNED?` |
| `MW-05` | `1 0 0 0` | `规适` | `1083 / — / — / —` | `UNALIGNED?` |
| `MW-06` | `1 0 0 0` | `∅` | `716 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `∅` | `716 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/mind-war.md+收束技法族12` | `1 0 0 0` | `∅` | `417 / — / — / —` | `UNALIGNED?` |
| `SF-01` | `1 0 1 1` | `怎例反检适` | `531 / — / 454 / 454` | `BLOCK_LOST` |
| `SF-02` | `1 0 1 1` | `怎例反适` | `580 / — / 392 / 392` | `SHRUNK;BLOCK_LOST` |
| `SF-03` | `1 0 1 1` | `怎例反适` | `549 / — / 545 / 545` | `BLOCK_LOST` |
| `SF-04` | `1 0 1 1` | `怎例反适` | `518 / — / 461 / 461` | `BLOCK_LOST` |
| `SF-05` | `1 0 1 1` | `怎例反适` | `555 / — / 464 / 464` | `BLOCK_LOST` |
| `SF-06` | `1 0 1 1` | `怎例反适` | `552 / — / 461 / 461` | `BLOCK_LOST` |
| `SF-07` | `1 0 1 1` | `怎例反适` | `543 / — / 455 / 455` | `BLOCK_LOST` |
| `SF-08` | `1 0 1 1` | `怎例反检适` | `553 / — / 434 / 434` | `BLOCK_LOST` |
| `sci-fi-future-plot-forge/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `SL-01` | `1 0 0 0` | `规适` | `1418 / — / — / —` | `UNALIGNED?` |
| `SL-02` | `1 0 0 0` | `规适` | `1179 / — / — / —` | `UNALIGNED?` |
| `SL-03` | `1 0 0 0` | `规适` | `1649 / — / — / —` | `UNALIGNED?` |
| `SL-04` | `1 0 0 0` | `规适` | `1254 / — / — / —` | `UNALIGNED?` |
| `SL-05` | `1 0 0 0` | `规适` | `1456 / — / — / —` | `UNALIGNED?` |
| `SL-06` | `1 0 0 0` | `规适` | `1301 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/references/society-love-craft.md+收束技法族12` | `1 0 0 0` | `∅` | `412 / — / — / —` | `UNALIGNED?` |
| `sci-fi-future-plot-forge/sources.md+token账目核对` | `1 0 0 0` | `∅` | `574 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-future-plot-forge/sources.md+审计链` | `1 0 0 0` | `∅` | `366 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+触发负触发` | `1 0 0 0` | `∅` | `1025 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+输入契约先拿全再动手` | `1 0 0 0` | `∅` | `748 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+任务路由先选主簇只加载该簇的参考资料` | `1 0 0 0` | `规` | `1114 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+执行步骤` | `1 0 0 0` | `∅` | `859 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+输出合同每次必交七项` | `1 0 0 0` | `∅` | `567 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+失败出口` | `1 0 0 0` | `规适败` | `681 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/SKILL.md+边界与元数据` | `1 0 0 0` | `∅` | `635 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `272 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+适用不适用` | `1 0 0 0` | `例适` | `207 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c41接触要有一套"可被对方拒绝"的程序而不是一次善意` | `1 0 0 0` | `∅` | `794 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c42沟通阶梯具体名词→动词→抽象名词逐级变难` | `1 0 0 0` | `∅` | `668 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c43体量误判要由设备"正常"来背书` | `1 0 0 0` | `∅` | `554 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c44接触的前提是承认对方有理智且这个判断要可证伪` | `1 0 0 0` | `∅` | `396 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c45动机质询比技术交换更能撑住接触场面` | `1 0 0 0` | `∅` | `527 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+c46反向证明当全体用心感不能心感者即劣等` | `1 0 0 0` | `∅` | `500 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+冲突与边界` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/alien-contact.md+检查清单` | `1 0 0 0` | `∅` | `321 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+适用不适用` | `1 0 0 0` | `例适` | `229 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c31反噬来自"授权方式"不来自"机器存在"` | `1 0 0 0` | `反适` | `964 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c32能力边界当悬念依赖"能否被击败"时才必须明写` | `1 0 0 0` | `例适` | `959 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c33识别可以是必要条件绝不能写成充分条件` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c34人格证据必须至少有一种可被对方角色核对` | `1 0 0 0` | `∅` | `446 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c35机器也要有物理损耗曲线` | `1 0 0 0` | `∅` | `342 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+c36弱点可以是"技术文盲"不一定是可被攻击的端口` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+反例与冲突` | `1 0 0 0` | `例` | `322 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/created-beings.md+检查清单` | `1 0 0 0` | `∅` | `328 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+1.什么时候必须停下来要料` | `1 0 0 0` | `∅` | `565 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+2.目标冲突时保留分支不伪造共识` | `1 0 0 0` | `适` | `519 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+3.覆盖不到时怎么说` | `1 0 0 0` | `例适` | `356 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+4.孤证不许升级为定律元规则` | `1 0 0 0` | `∅` | `710 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+5.已拒绝的旧铁律见到就改不要套` | `1 0 0 0` | `∅` | `588 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+6.notproven的标注义务` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/failure-exit.md+7.时代语料处理硬性` | `1 0 0 0` | `∅` | `376 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+适用不适用` | `1 0 0 0` | `例适败` | `235 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+c51失败必须有一个可指认的物理原因且该原因在失败前已隐含在读者可获取的信息里` | `1 0 0 0` | `败` | `968 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+c52工程对抗要落在物性上不落在勇气上` | `1 0 0 0` | `∅` | `577 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+c53把计算过程写成角色的行为不写成说明文` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+c54专家型冲突冲劲vs.经验且由技术真相完成和解` | `1 0 0 0` | `∅` | `379 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+c55资源运力的算术先行` | `1 0 0 0` | `∅` | `407 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+反例与冲突` | `1 0 0 0` | `∅` | `516 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md+检查清单` | `1 0 0 0` | `∅` | `249 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+适用不适用` | `1 0 0 0` | `规例适` | `246 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+c21一次只翻一个制度轴并让它在第一段日常场景里就产生后果` | `1 0 0 0` | `例适` | `1012 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+c22翻转要写成可观察的生理器物后果不只是观念` | `1 0 0 0` | `适` | `564 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+c23给异质社会一条"我们为什么这样"的自辩` | `1 0 0 0` | `∅` | `281 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+c24把"少数派"的定义权交给制度而不是主角` | `1 0 0 0` | `∅` | `410 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+时代语料处理必须遵守` | `1 0 0 0` | `∅` | `338 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+反例与冲突` | `1 0 0 0` | `例适` | `267 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md+检查清单` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+适用不适用` | `1 0 0 0` | `例适` | `206 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c71压迫要写成可执行的流程不是形容词` | `1 0 0 0` | `∅` | `1174 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c72把压迫写在"福利"的口径里` | `1 0 0 0` | `∅` | `412 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c73系统性做局要写出蝴蝶效应而不是一个大老板` | `1 0 0 0` | `∅` | `499 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c74代价的形式不限但必须可追踪` | `1 0 0 0` | `∅` | `589 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c75最狠的惩罚是孤独不是死亡` | `1 0 0 0` | `∅` | `265 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+c76制度恐惧的暴露路径要选对舆论vs.法律` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+反例与冲突` | `1 0 0 0` | `∅` | `383 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/institution-detail.md+检查清单` | `1 0 0 0` | `∅` | `310 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+适用不适用` | `1 0 0 0` | `例适` | `278 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+c11先给可计算的量再倒推世界` | `1 0 0 0` | `例适` | `984 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+c12一次只推进一环并把那一环写成可观察物` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+c13为制度自辩配一条生理直觉的反声道` | `1 0 0 0` | `例适` | `575 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+c14"完美计划"的自反装置可选` | `1 0 0 0` | `例适` | `462 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+反例与冲突` | `1 0 0 0` | `∅` | `629 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md+检查清单诊断用` | `1 0 0 0` | `∅` | `315 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+适用不适用` | `1 0 0 0` | `例适` | `229 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+条件规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c61反转的可信度取决于前文是否留了可复核的物` | `1 0 0 0` | `∅` | `959 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c62延后解释必须给出"为什么现在才说"的理由` | `1 0 0 0` | `∅` | `406 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c63框架必须承认证据缺口` | `1 0 0 0` | `∅` | `534 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c64尺度揭晓优先于身份揭晓` | `1 0 0 0` | `∅` | `384 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c65末世不必靠暴力高潮收束` | `1 0 0 0` | `∅` | `504 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+c66结局必须兑现前文承诺` | `1 0 0 0` | `∅` | `368 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+反例与冲突` | `1 0 0 0` | `∅` | `395 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md+检查清单` | `1 0 0 0` | `∅` | `223 / — / — / —` | `UNALIGNED?` |
| `A6` | `1 0 0 0` | `∅` | `204 / — / — / —` | `UNALIGNED?` |
| `A7` | `1 0 0 0` | `∅` | `227 / — / — / —` | `UNALIGNED?` |
| `A8` | `1 0 0 0` | `∅` | `264 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/rule-adjudication.md+a类来自兄弟批次skill的候选规则` | `1 0 0 0` | `∅` | `2577 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `∅` | `226 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `∅` | `281 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `∅` | `333 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `321 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `∅` | `265 / — / — / —` | `UNALIGNED?` |
| `B6` | `1 0 0 0` | `∅` | `225 / — / — / —` | `UNALIGNED?` |
| `B7` | `1 0 0 0` | `∅` | `203 / — / — / —` | `UNALIGNED?` |
| `B8` | `1 0 0 0` | `∅` | `266 / — / — / —` | `UNALIGNED?` |
| `B9` | `1 0 0 0` | `∅` | `229 / — / — / —` | `UNALIGNED?` |
| `B10` | `1 0 0 0` | `∅` | `233 / — / — / —` | `UNALIGNED?` |
| `B11` | `1 0 0 0` | `∅` | `136 / — / — / —` | `UNALIGNED?` |
| `B12` | `1 0 0 0` | `∅` | `230 / — / — / —` | `UNALIGNED?` |
| `B13` | `1 0 0 0` | `∅` | `301 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/rule-adjudication.md+b类通用铁律候选` | `1 0 0 0` | `∅` | `3330 / — / — / —` | `UNALIGNED?` |
| `sci-fi-novum-world-forge/references/rule-adjudication.md+已丢弃的旧铁律不要再套` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `B02` | `1 0 0 0` | `∅` | `508 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A-06` | `1 0 0 0` | `∅` | `508 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG68` | `1 0 0 0` | `∅` | `9729 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG775` | `1 0 0 0` | `∅` | `9729 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/sources.md+知识角色一句话详见notessourcesynthesis.md§1` | `1 0 0 0` | `∅` | `481 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+身份` | `1 0 0 0` | `∅` | `452 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+来源账` | `1 0 0 0` | `∅` | `470 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+证据链` | `1 0 0 0` | `∅` | `837 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+版本与替代关系` | `1 0 0 0` | `规` | `563 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+许可与版权` | `1 0 0 0` | `∅` | `364 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md+打包与哈希` | `1 0 0 0` | `检` | `1016 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P5` | `1 0 0 0` | `∅` | `674 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+这个skill解决什么` | `1 0 0 0` | `∅` | `340 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+触发` | `1 0 0 0` | `∅` | `456 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+负触发不要用` | `1 0 0 0` | `∅` | `399 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+证据底座与覆盖率必须随结论一起说明` | `1 0 0 0` | `规` | `997 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+任务路由` | `1 0 0 0` | `∅` | `734 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+最短执行路径6步` | `1 0 0 0` | `∅` | `1183 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+输出物表` | `1 0 0 0` | `∅` | `899 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+规则索引` | `1 0 0 0` | `反检` | `772 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+硬约束写作时不可越过` | `1 0 0 0` | `适` | `353 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/SKILL.md+失败出口` | `1 0 0 0` | `∅` | `881 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/examples/worked-example.md+0.起点` | `1 0 0 0` | `∅` | `364 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `449 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `377 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `369 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `383 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `238 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `716 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/examples/worked-example.md+9.这个演示用了哪些证据` | `1 0 0 0` | `反` | `652 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+f证据` | `1 0 0 0` | `∅` | `1267 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+怎么用p` | `1 0 0 0` | `∅` | `613 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+适用` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+不适用` | `1 0 0 0` | `∅` | `242 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+反例` | `1 0 0 0` | `败` | `543 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md+自检` | `1 0 0 0` | `∅` | `270 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+f证据前置型` | `1 0 0 0` | `∅` | `937 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+f证据后置型` | `1 0 0 0` | `∅` | `684 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+f证据弥散型两型都不适用` | `1 0 0 0` | `∅` | `319 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+怎么用p` | `1 0 0 0` | `∅` | `617 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+适用` | `1 0 0 0` | `∅` | `108 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+不适用` | `1 0 0 0` | `例` | `484 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+反例` | `1 0 0 0` | `败` | `514 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md+自检` | `1 0 0 0` | `规` | `297 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+f证据` | `1 0 0 0` | `∅` | `1226 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+机制拆解h` | `1 0 0 0` | `∅` | `448 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+怎么用p` | `1 0 0 0` | `∅` | `509 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+适用` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+不适用` | `1 0 0 0` | `∅` | `268 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+反例` | `1 0 0 0` | `败` | `477 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md+自检` | `1 0 0 0` | `∅` | `325 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+r4认知冲击来自“词不够用”不是来自“形容词很猛”` | `1 0 0 0` | `规` | `289 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+f证据` | `1 0 0 0` | `∅` | `784 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+怎么用p` | `1 0 0 0` | `∅` | `533 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+适用不适用` | `1 0 0 0` | `例适` | `249 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+反例` | `1 0 0 0` | `败` | `256 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md+r5见证框架先借出信任再让读者发现信任被用在哪` | `1 0 0 0` | `规适` | `535 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+f证据多维证据组合的正例` | `1 0 0 0` | `∅` | `807 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+f证据裁决式收束不解释只裁定` | `1 0 0 0` | `∅` | `423 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+怎么用p` | `1 0 0 0` | `∅` | `723 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+适用` | `1 0 0 0` | `∅` | `185 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+不适用` | `1 0 0 0` | `规` | `223 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+反例` | `1 0 0 0` | `败` | `464 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md+自检` | `1 0 0 0` | `∅` | `333 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+五类失败模式` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+1.解释段补丁解释替代了揭示` | `1 0 0 0` | `∅` | `473 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+2.原地循环重复没有位移` | `1 0 0 0` | `检` | `467 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+3.讲座式对话概念被讲懂而非撞上` | `1 0 0 0` | `例` | `327 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+4.巧合式翻转揭示不来自前文` | `1 0 0 0` | `适` | `373 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+5.导语剧透把首读惊讶提前花掉` | `1 0 0 0` | `规` | `284 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+审稿检查表逐项写“通过不适用需修”` | `1 0 0 0` | `∅` | `1045 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md+使用边界` | `1 0 0 0` | `反` | `244 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/source-index.md+覆盖统计` | `1 0 0 0` | `规` | `711 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-conceptual-reveal/references/source-index.md+引用与核验` | `1 0 0 0` | `规检` | `405 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG829` | `1 0 0 0` | `∅` | `2633 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG32` | `1 0 0 0` | `∅` | `2633 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+输入权限` | `1 0 0 0` | `怎例` | `940 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+快速决策表先选型再查规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+表1novum四型先判断你的核心装置属于哪型` | `1 0 0 0` | `∅` | `783 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+表2信息释放四档全篇主档只能选一个中途换档=失信` | `1 0 0 0` | `∅` | `691 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+表3社会推演四模式反派可以不是人` | `1 0 0 0` | `∅` | `503 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+表4收束五型` | `1 0 0 0` | `∅` | `485 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+触发与负触发` | `1 0 0 0` | `检` | `746 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+分支路由按任务类型` | `1 0 0 0` | `∅` | `784 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+输出契约` | `1 0 0 0` | `∅` | `605 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+失败出口` | `1 0 0 0` | `规例` | `794 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/SKILL.md+文件路由` | `1 0 0 0` | `∅` | `1139 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `196 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.冲突裁决源文本互相矛盾时怎么选` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.1技术乐观vs技术恐怖` | `1 0 0 0` | `规` | `504 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.2个人英雄vs系统解决` | `1 0 0 0` | `∅` | `347 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.3爱情线的位置` | `1 0 0 0` | `∅` | `391 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.4暴力与复仇` | `1 0 0 0` | `∅` | `343 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+1.5真相与共谋` | `1 0 0 0` | `∅` | `337 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+2.单源清单使用时必须标单源` | `1 0 0 0` | `∅` | `1015 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.时代红线只登记不采纳` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.1反犹与族裔阴谋论` | `1 0 0 0` | `∅` | `305 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.2殖民与"无主之地"` | `1 0 0 0` | `∅` | `461 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.3种族本质论` | `1 0 0 0` | `∅` | `338 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.4性别本质论与工具化` | `1 0 0 0` | `∅` | `401 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.5优生与"完美标本"` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+3.6殉葬浪漫化` | `1 0 0 0` | `∅` | `178 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+4.不可迁移的"科学"装置` | `1 0 0 0` | `∅` | `668 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `362 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/counterexamples.md+6.一条unresolved不要假装有答案` | `1 0 0 0` | `∅` | `381 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+示例1规划型从零搭一部长篇的"设定论证"` | `1 0 0 0` | `∅` | `170 / — / — / —` | `UNALIGNED?` |
| `R19` | `1 0 0 0` | `规` | `764 / — / — / —` | `UNALIGNED?` |
| `R28` | `1 0 0 0` | `∅` | `462 / — / — / —` | `UNALIGNED?` |
| `R21` | `1 0 0 0` | `∅` | `535 / — / — / —` | `UNALIGNED?` |
| `R22` | `1 0 0 0` | `∅` | `535 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第4步r20加限制r01加倒计时` | `1 0 0 0` | `例` | `493 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第5步r14埋反转r17道具三用` | `1 0 0 0` | `检` | `341 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第6步r30收束如果结尾要写"更好的监管制度"` | `1 0 0 0` | `∅` | `330 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+输出契约本示例的交付物` | `1 0 0 0` | `∅` | `443 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+示例2诊断型一份"设定很酷但读不下去"的初稿` | `1 0 0 0` | `∅` | `281 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第1步跑failuremodes七问` | `1 0 0 0` | `∅` | `611 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第2步按规则改不改故事只改因果` | `1 0 0 0` | `例败` | `1343 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+第3步回归清单改完必须逐条过` | `1 0 0 0` | `∅` | `590 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/examples.md+输出契约诊断型交付物` | `1 0 0 0` | `规败` | `388 / — / — / —` | `UNALIGNED?` |
| `M1` | `1 0 0 0` | `规例` | `787 / — / — / —` | `UNALIGNED?` |
| `M2` | `1 0 0 0` | `规` | `904 / — / — / —` | `UNALIGNED?` |
| `M3` | `1 0 0 0` | `∅` | `889 / — / — / —` | `UNALIGNED?` |
| `M4` | `1 0 0 0` | `∅` | `1138 / — / — / —` | `UNALIGNED?` |
| `M5` | `1 0 0 0` | `∅` | `903 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `∅` | `971 / — / — / —` | `UNALIGNED?` |
| `M7` | `1 0 0 0` | `∅` | `1008 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/failure-modes.md+附诊断顺序与出口` | `1 0 0 0` | `∅` | `545 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/contact-and-otherness.md+目录` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `R02` | `1 0 0 0` | `怎` | `1530 / — / — / —` | `UNALIGNED?` |
| `R03` | `1 0 0 0` | `怎` | `1323 / — / — / —` | `UNALIGNED?` |
| `R04` | `1 0 0 0` | `怎` | `1925 / — / — / —` | `UNALIGNED?` |
| `R07` | `1 0 0 0` | `怎` | `1627 / — / — / —` | `UNALIGNED?` |
| `R27` | `1 0 0 0` | `怎` | `1783 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `91 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/references/information-and-pov.md+目录` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `怎` | `1493 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `怎` | `1349 / — / — / —` | `UNALIGNED?` |
| `R24` | `1 0 0 0` | `怎` | `1956 / — / — / —` | `UNALIGNED?` |
| `R25` | `1 0 0 0` | `怎反` | `1582 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/novum-and-rules.md+目录` | `1 0 0 0` | `规例` | `170 / — / — / —` | `UNALIGNED?` |
| `R01` | `1 0 0 0` | `怎适` | `1584 / — / — / —` | `UNALIGNED?` |
| `R20` | `1 0 0 0` | `怎例` | `2046 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `怎` | `1470 / — / — / —` | `UNALIGNED?` |
| `R17` | `1 0 0 0` | `怎` | `1330 / — / — / —` | `UNALIGNED?` |
| `B04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/rework-decision.md+确定目标不把三个验证混在一起` | `1 0 0 0` | `例检` | `668 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/rework-decision.md+选择条件分支` | `1 0 0 0` | `∅` | `1497 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/rework-decision.md+结尾不强迫一类答案` | `1 0 0 0` | `规适败` | `680 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/rework-decision.md+输出合同` | `1 1 0 0` | `∅` | `307 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/structure-and-endings.md+目录` | `1 0 0 0` | `规` | `253 / — / — / —` | `UNALIGNED?` |
| `R08` | `1 0 0 0` | `怎` | `1209 / — / — / —` | `UNALIGNED?` |
| `R09` | `1 0 0 0` | `规怎` | `1731 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `怎` | `1497 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `规怎` | `1476 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `规怎` | `1322 / — / — / —` | `UNALIGNED?` |
| `R23` | `1 0 0 0` | `怎` | `1586 / — / — / —` | `UNALIGNED?` |
| `R26` | `1 0 0 0` | `怎` | `1804 / — / — / —` | `UNALIGNED?` |
| `R29` | `1 0 0 0` | `怎` | `1354 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/references/world-and-institutions.md+目录` | `1 0 0 0` | `∅` | `327 / — / — / —` | `UNALIGNED?` |
| `R05` | `1 0 0 0` | `怎` | `1461 / — / — / —` | `UNALIGNED?` |
| `R06` | `1 0 0 0` | `怎` | `1407 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `怎败` | `1619 / — / — / —` | `UNALIGNED?` |
| `R18` | `1 0 0 0` | `怎` | `1804 / — / — / —` | `UNALIGNED?` |
| `R30` | `1 0 0 0` | `怎` | `2270 / — / — / —` | `UNALIGNED?` |
| `science-fiction-craft-b04/sources-index.md+1.索引表` | `1 0 0 0` | `∅` | `4874 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/sources-index.md+2.完整sha256读前核验值` | `1 0 0 0` | `∅` | `2287 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/sources-index.md+3.来源族与去重说明` | `1 0 0 0` | `规` | `1331 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `science-fiction-craft-b04/sources-index.md+4.时代与体裁分布` | `1 0 0 0` | `∅` | `591 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+1.这个skill解决什么` | `1 0 0 0` | `∅` | `1140 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+2.触发负触发` | `1 0 0 0` | `怎` | `924 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+3.证据底座与硬边界` | `1 0 0 0` | `∅` | `1275 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+4.七条硬规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+5.体裁六分叉先选一类参数完全不同` | `1 0 0 0` | `∅` | `1084 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+6.任务路由` | `1 0 0 0` | `∅` | `1097 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+7.最短执行路径默认7步` | `1 0 0 0` | `∅` | `752 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+8.输出合同` | `1 0 0 0` | `∅` | `807 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/SKILL.md+9.明确不做明确禁止` | `1 0 0 0` | `∅` | `803 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `541 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/examples/worked-example.md+用户请求样例` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/examples/worked-example.md+step0先做核账不做不往下走` | `1 0 0 0` | `规` | `278 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/examples/worked-example.md+step2定体裁分叉§5` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/examples/worked-example.md+输出给用户的四张表` | `1 0 0 0` | `∅` | `304 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/examples/worked-example.md+如果用户的请求超出了证据` | `1 0 0 0` | `∅` | `334 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md+为什么"前置说明"会失败h` | `1 0 0 0` | `∅` | `329 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md+三种可核验的投放姿势f` | `1 0 0 0` | `∅` | `977 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md+延迟的三种合法理由h` | `1 0 0 0` | `∅` | `412 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md+p设定回答表模板` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md+常见病的处方` | `1 0 0 0` | `∅` | `415 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md+证据f` | `1 0 0 0` | `∅` | `1111 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md+h三联为什么比形容词有效跨3组支持pg4340pg21873pg51623` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md+p三联表模板每条机制三格必须填满` | `1 0 0 0` | `∅` | `630 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md+三条边界` | `1 0 0 0` | `∅` | `571 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md+常见病的处方` | `1 0 0 0` | `∅` | `460 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/03-single-variable-world.md+一单一变量推到底ab分叉的核心` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `PG624` | `1 0 0 0` | `∅` | `724 / — / — / —` | `UNALIGNED?` |
| `PG35` | `1 0 0 0` | `∅` | `724 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/03-single-variable-world.md+h跨3组支持bellamyjefferieswells` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/03-single-variable-world.md+p反驳章清单论证线必填` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/03-single-variable-world.md+p口味声明写在封面页两行` | `1 0 0 0` | `∅` | `123 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/03-single-variable-world.md+三体裁分叉速查与skill§5对应` | `1 0 0 0` | `∅` | `527 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/04-rules-costs-and-paperwork.md+证据f` | `1 0 0 0` | `∅` | `1187 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/04-rules-costs-and-paperwork.md+h真正的装置不是"一台坏机器"而是"走不通的救济路径"` | `1 0 0 0` | `∅` | `708 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/04-rules-costs-and-paperwork.md+p不可修制度卡模板` | `1 0 0 0` | `∅` | `623 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/04-rules-costs-and-paperwork.md+常见病的处方` | `1 0 0 0` | `∅` | `465 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/05-time-and-mechanism-ledger.md+h跨3组支持stuartfarrellmerwin` | `1 0 0 0` | `∅` | `215 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/05-time-and-mechanism-ledger.md+p机制账本模板每行四项` | `1 0 0 0` | `∅` | `613 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/05-time-and-mechanism-ledger.md+三种合法拒止防止"想怎么用就怎么用"` | `1 0 0 0` | `∅` | `364 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/05-time-and-mechanism-ledger.md+常见病的处方` | `1 0 0 0` | `∅` | `459 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+一结局落点代价被承认不是胜利被结算` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `PG36` | `1 0 0 0` | `∅` | `777 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+h跨4组支持wellsnoursemerwinboren` | `1 0 0 0` | `∅` | `156 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+p代价清单模板` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+二本批保留的未决冲突不得伪造共识` | `1 0 0 0` | `∅` | `675 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+三负例与禁止项` | `1 0 0 0` | `∅` | `663 / — / — / —` | `UNALIGNED?` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md+四notproven本轮不写规则` | `1 0 0 0` | `∅` | `398 / — / — / —` | `UNALIGNED?` |
| `B03` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scifi-future-craft-b03/references/source-index.md+基线` | `1 0 0 0` | `∅` | `545 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scifi-future-craft-b03/references/source-index.md+降权纪律引用前必读` | `1 0 0 0` | `∅` | `396 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scifi-future-craft-b03/references/source-index.md+已知证据缺陷引用时必须同时说明` | `1 0 0 0` | `∅` | `887 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scifi-future-craft-b03/references/source-index.md+引用格式` | `1 0 0 0` | `∅` | `256 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 06 历史架空（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 06 历史架空

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`historical-alt-history-craft`、`historical-contract-and-legitimacy-craft`、`historical-fiction-craft-b03`、`historical-fiction-plot-forge`、`historical-fiction-power-machine`、`historical-immersion-and-stakes`

**规则单元数 444；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 444（100.0%）**
**flag 计数**：SOURCE_ONLY=55；UNALIGNED?=444

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `P4` | `1 0 0 0` | `∅` | `1065 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+本轮返工的优先证据分流` | `1 0 0 0` | `∅` | `664 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+1.触发条件when与负触发whennot` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+1.1when什么情况下该用本skill` | `1 0 0 0` | `∅` | `1733 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+1.2whennot什么情况下不要用触发即走失败出口不要硬套` | `1 0 0 0` | `∅` | `1494 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+2.输入要求用之前必须拿到什么` | `1 0 0 0` | `∅` | `1053 / — / — / —` | `UNALIGNED?` |
| `F1` | `1 0 0 0` | `∅` | `217 / — / — / —` | `UNALIGNED?` |
| `F2` | `1 0 0 0` | `∅` | `210 / — / — / —` | `UNALIGNED?` |
| `F3` | `1 0 0 0` | `∅` | `199 / — / — / —` | `UNALIGNED?` |
| `F4` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `F5` | `1 0 0 0` | `∅` | `163 / — / — / —` | `UNALIGNED?` |
| `F6` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `F7` | `1 0 0 0` | `∅` | `158 / — / — / —` | `UNALIGNED?` |
| `F8` | `1 0 0 0` | `∅` | `170 / — / — / —` | `UNALIGNED?` |
| `F9` | `1 0 0 0` | `∅` | `182 / — / — / —` | `UNALIGNED?` |
| `F10` | `1 0 0 0` | `∅` | `191 / — / — / —` | `UNALIGNED?` |
| `F11` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `F12` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `F13` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `F14` | `1 0 0 0` | `∅` | `165 / — / — / —` | `UNALIGNED?` |
| `F15` | `1 0 0 0` | `∅` | `141 / — / — / —` | `UNALIGNED?` |
| `F16` | `1 0 0 0` | `∅` | `206 / — / — / —` | `UNALIGNED?` |
| `F17` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `F18` | `1 0 0 0` | `∅` | `174 / — / — / —` | `UNALIGNED?` |
| `F19` | `1 0 0 0` | `∅` | `194 / — / — / —` | `UNALIGNED?` |
| `F20` | `1 0 0 0` | `∅` | `176 / — / — / —` | `UNALIGNED?` |
| `F21` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `F22` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `F23` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+3.规则族总表f1–f23` | `1 0 0 0` | `∅` | `4793 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.分支判断branching` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.1分支a从头规划` | `1 0 0 0` | `∅` | `356 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.2分支b诊断已有稿` | `1 0 0 0` | `∅` | `334 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.3分支c单点设计一场戏一个装置` | `1 0 0 0` | `∅` | `148 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.4分支d真实人物敏感题材` | `1 0 0 0` | `∅` | `109 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.5表1按写作阶段选族` | `1 0 0 0` | `∅` | `689 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.6表2按素材类型选族` | `1 0 0 0` | `∅` | `740 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+4.7表3按症状直接跳转` | `1 0 0 0` | `∅` | `495 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+5.输出格式outputcontract` | `1 0 0 0` | `规怎` | `825 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+6.失败出口failureexit` | `1 0 0 0` | `∅` | `924 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+7.文件路由` | `1 0 0 0` | `∅` | `1111 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+8.notproven声明不得改写为pass` | `1 0 0 0` | `∅` | `747 / — / — / —` | `UNALIGNED?` |
| `P5` | `1 0 0 0` | `∅` | `2157 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+9.1本轮修正记录核验中真实发现并回读改正的缺陷` | `1 0 0 0` | `∅` | `1803 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+9.2本轮20261028额外补验的锚点` | `1 0 0 0` | `∅` | `2961 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+9.3引文缺陷修复20261028门禁复跑` | `1 0 0 0` | `∅` | `1094 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/SKILL.md+10.来源与来源族` | `1 0 0 0` | `∅` | `686 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `400 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `310 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `339 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `370 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/counterexamples.md+1.rejectr1–r5不采纳的做法` | `1 0 0 0` | `∅` | `2056 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/counterexamples.md+r1–r5的共性判别式` | `1 0 0 0` | `∅` | `191 / — / — / —` | `UNALIGNED?` |
| `C6` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C7` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `∅` | `2663 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/counterexamples.md+3.singlesource登记只有1个来源族不升普适规则` | `1 0 0 0` | `∅` | `2061 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/counterexamples.md+singlesource使用规则` | `1 0 0 0` | `∅` | `269 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/counterexamples.md+4.失败出口遇到这些情况停下来而不是硬套` | `1 0 0 0` | `∅` | `1230 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+示例a规划型1685年英格兰虚构信使嵌入monmouth叛乱` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+1.选用规则id` | `1 0 0 0` | `∅` | `61 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+2.每条规则在本作的具体化` | `1 0 0 0` | `∅` | `3004 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+3.失效条件核对` | `1 0 0 0` | `∅` | `904 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+4.证据锚点逐字回读命中` | `1 0 0 0` | `∅` | `1030 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+5.边界声明` | `1 0 0 0` | `败` | `297 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+示例b诊断型一部已成稿的唐代架空长篇` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+1.先用表3定位` | `1 0 0 0` | `败` | `141 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/examples.md+2.诊断步骤` | `1 0 0 0` | `例败` | `2012 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/failure-modes.md+八问速筛` | `1 0 0 0` | `∅` | `676 / — / — / —` | `UNALIGNED?` |
| `M1` | `1 0 0 0` | `∅` | `770 / — / — / —` | `UNALIGNED?` |
| `M2` | `1 0 0 0` | `例败` | `1034 / — / — / —` | `UNALIGNED?` |
| `M3` | `1 0 0 0` | `∅` | `802 / — / — / —` | `UNALIGNED?` |
| `M4` | `1 0 0 0` | `∅` | `770 / — / — / —` | `UNALIGNED?` |
| `M5` | `1 0 0 0` | `败` | `944 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `∅` | `856 / — / — / —` | `UNALIGNED?` |
| `M7` | `1 0 0 0` | `∅` | `969 / — / — / —` | `UNALIGNED?` |
| `M8` | `1 0 0 0` | `∅` | `767 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/failure-modes.md+修法优先级不要跳步` | `1 0 0 0` | `∅` | `342 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/failure-modes.md+诊断记录模板每次用本文件后填写` | `1 0 0 0` | `∅` | `237 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/01-source-contract-and-anchors.md+开篇检查清单可直接执行` | `1 0 0 0` | `∅` | `463 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-alt-history-craft/references/02-gap-agents-and-institutions.md+中段检查清单` | `1 0 0 0` | `适败` | `512 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/03-prophecy-relics-and-ritual.md+命运线检查清单` | `1 0 0 0` | `∅` | `461 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/04-scene-voice-and-space.md+场景检查清单` | `1 0 0 0` | `∅` | `404 / — / — / —` | `UNALIGNED?` |
| `U4` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `U3` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `U2` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `U5` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `U1` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/05-bias-violence-and-limits.md+rejectr1–r5不采纳的做法只进诊断与反例` | `1 0 0 0` | `∅` | `1501 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/05-bias-violence-and-limits.md+unresolvedu1–u5未决问题不写成规则只作"待验证"` | `1 0 0 0` | `∅` | `740 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/05-bias-violence-and-limits.md+singlesource登记本reference涉及部分` | `1 0 0 0` | `∅` | `375 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/05-bias-violence-and-limits.md+伦理红线自查清单` | `1 0 0 0` | `败` | `367 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `418 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-alt-history-craft/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B06` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `A-07` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/rework-decision.md+先判历史合同` | `1 0 0 0` | `∅` | `621 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/rework-decision.md+分支图决策会实质改变输出` | `1 0 0 0` | `∅` | `1023 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/rework-decision.md+五个领域分流与反例` | `1 0 0 0` | `∅` | `1446 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/references/rework-decision.md+可执行输出与停止` | `1 0 0 0` | `∅` | `441 / — / — / —` | `UNALIGNED?` |
| `historical-alt-history-craft/sources-index.md+族→成员` | `1 0 0 0` | `∅` | `611 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-alt-history-craft/sources-index.md+版本与排除不作技法证据` | `1 0 0 0` | `∅` | `571 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-alt-history-craft/sources-index.md+读取路径` | `1 0 0 0` | `∅` | `183 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B05` | `1 0 0 0` | `∅` | `1804 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+1.何时使用when何时不要用whennot` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+1.1when` | `1 0 0 0` | `∅` | `1318 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+1.2whennot触发即走失败出口不要硬套` | `1 0 0 0` | `∅` | `1450 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+2.输入要求用之前必须拿到什么` | `1 0 0 0` | `∅` | `775 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+3.执行步骤五步主流程` | `1 0 0 0` | `怎` | `2077 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.任务路由与分支` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.1分支a从头规划` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.2分支b诊断已有稿` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.3分支c单点设计一场戏一个装置` | `1 0 0 0` | `∅` | `112 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.4分支d真实人物敏感题材` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.5表1按写作阶段选族` | `1 0 0 0` | `∅` | `569 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.6表2按素材类型选族` | `1 0 0 0` | `∅` | `754 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+4.7表3按症状直接跳转` | `1 0 0 0` | `∅` | `500 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+5.输出合同每次应用须交付五项` | `1 0 0 0` | `怎` | `750 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+6.失败出口failureexit` | `1 0 0 0` | `∅` | `959 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+7.文件路由` | `1 0 0 0` | `∅` | `829 / — / — / —` | `UNALIGNED?` |
| `NP5` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `NP2` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `NP4` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `NP6` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `NP3` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `NP1` | `1 0 0 0` | `∅` | `961 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/SKILL.md+9.来源与来源族` | `1 0 0 0` | `∅` | `500 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `212 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A9` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A3` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B3` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A7` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A6` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B2` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B5` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A5` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A2` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B1` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A4` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `A8` | `1 0 0 0` | `∅` | `171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X1` | `1 0 0 0` | `∅` | `518 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X2` | `1 0 0 0` | `∅` | `518 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X5` | `1 0 0 0` | `∅` | `518 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `K4` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `J1` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `K1` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D1` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D2` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D3` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D7` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D5` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `K3` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `J2` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `K2` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D6` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `D4` | `1 0 0 0` | `∅` | `208 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/03-real-figures-and-symmetry.md+冲突x4真实姓名vs虚构人物两个相反方向` | `1 0 0 0` | `败` | `662 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `H3` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `I4` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `E6` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `E5` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `G4` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `H1` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `H2` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `I1` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `G1` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `G2` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `G3` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `I2` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `I3` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `∅` | `5 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/04-space-supernatural-and-period.md+冲突x3超自然的三种写法不统一` | `1 0 0 0` | `∅` | `537 / — / — / —` | `UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/05-source-index-and-adjudication.md+1.18源索引pg作品作者行数sha知识角色贡献族` | `1 0 0 0` | `∅` | `3159 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/05-source-index-and-adjudication.md+2.对历史规则的逐条裁决对象是同父任务的既有skill` | `1 0 0 0` | `∅` | `4826 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X3` | `1 0 0 0` | `∅` | `185 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X4` | `1 0 0 0` | `∅` | `237 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `X6` | `1 0 0 0` | `∅` | `155 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/05-source-index-and-adjudication.md+3.冲突总表x1–x6不伪造共识` | `1 0 0 0` | `∅` | `1171 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-contract-and-legitimacy-craft/references/05-source-index-and-adjudication.md+6.引文核验方法与结果` | `1 0 0 0` | `∅` | `1468 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B03` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+触发` | `1 0 0 0` | `∅` | `300 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+负触发` | `1 0 0 0` | `∅` | `257 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+输入权限` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+工作分支` | `1 0 0 0` | `∅` | `372 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+输出` | `1 0 0 0` | `规` | `163 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+失败出口` | `1 1 0 0` | `∅` | `357 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/SKILL.md+来源与核验` | `1 0 0 0` | `规` | `206 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `166 / — / — / —` | `UNALIGNED?` |
| `RH-01` | `1 0 0 0` | `∅` | `248 / — / — / —` | `UNALIGNED?` |
| `RH-02` | `1 0 0 0` | `∅` | `397 / — / — / —` | `UNALIGNED?` |
| `RH-04` | `1 0 0 0` | `∅` | `397 / — / — / —` | `UNALIGNED?` |
| `RH-08` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `RH-05` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `RH-06` | `1 0 0 0` | `∅` | `323 / — / — / —` | `UNALIGNED?` |
| `RH-10` | `1 0 0 0` | `∅` | `288 / — / — / —` | `UNALIGNED?` |
| `RH-12` | `1 0 0 0` | `∅` | `202 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/examples.md+反例集` | `1 0 0 0` | `∅` | `408 / — / — / —` | `UNALIGNED?` |
| `RH-03` | `1 0 0 0` | `怎例反适` | `581 / — / — / —` | `UNALIGNED?` |
| `RH-07` | `1 0 0 0` | `怎例反适` | `529 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `425 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/p4-field-guide.md+史料声明不是独立史证` | `1 0 0 0` | `∅` | `524 / — / — / —` | `UNALIGNED?` |
| `RH-09` | `1 0 0 0` | `规怎例适` | `589 / — / — / —` | `UNALIGNED?` |
| `RH-11` | `1 0 0 0` | `规怎适` | `589 / — / — / —` | `UNALIGNED?` |
| `RH-13` | `1 0 0 0` | `规怎` | `627 / — / — / —` | `UNALIGNED?` |
| `RH-14` | `1 0 0 0` | `规怎适` | `649 / — / — / —` | `UNALIGNED?` |
| `RH-15` | `1 0 0 0` | `规怎适` | `535 / — / — / —` | `UNALIGNED?` |
| `RH-16` | `1 0 0 0` | `规怎` | `702 / — / — / —` | `UNALIGNED?` |
| `RH-17` | `1 0 0 0` | `规怎` | `601 / — / — / —` | `UNALIGNED?` |
| `RH-18` | `1 0 0 0` | `规怎适` | `739 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+1.适用范围` | `1 0 0 0` | `∅` | `468 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+2.来源族去重` | `1 0 0 0` | `∅` | `317 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+3.冲突裁决消费者版` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C8` | `1 0 0 0` | `∅` | `261 / — / — / —` | `UNALIGNED?` |
| `C9` | `1 0 0 0` | `∅` | `420 / — / — / —` | `UNALIGNED?` |
| `C10` | `1 1 0 0` | `∅` | `304 / 603 / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+4.历史悬案与史料引用门禁` | `1 0 0 0` | `∅` | `480 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+5.真实人物审计` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+6.时代局限重构点` | `1 0 0 0` | `∅` | `483 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md+7.证据不足不立硬律` | `1 0 0 0` | `∅` | `169 / — / — / —` | `UNALIGNED?` |
| `PG966` | `1 0 0 0` | `∅` | `1572 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG848` | `1 0 0 0` | `∅` | `1572 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG421` | `1 0 0 0` | `∅` | `1572 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG357` | `1 0 0 0` | `∅` | `1572 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-craft-b03/references/source-index.md+阅读覆盖声明` | `1 0 0 0` | `∅` | `464 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-craft-b03/references/techniques.md+h.修订自查清单` | `1 0 0 0` | `例` | `441 / — / — / —` | `UNALIGNED?` |
| `HD-01` | `1 0 0 0` | `∅` | `44 / — / — / —` | `UNALIGNED?` |
| `HD-02` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `HD-03` | `1 0 0 0` | `∅` | `97 / — / — / —` | `UNALIGNED?` |
| `HD-04` | `1 0 0 0` | `∅` | `60 / — / — / —` | `UNALIGNED?` |
| `HD-05` | `1 0 0 0` | `∅` | `77 / — / — / —` | `UNALIGNED?` |
| `HD-06` | `1 0 0 0` | `∅` | `62 / — / — / —` | `UNALIGNED?` |
| `HD-07` | `1 0 0 0` | `∅` | `39 / — / — / —` | `UNALIGNED?` |
| `HD-08` | `1 0 0 0` | `∅` | `32 / — / — / —` | `UNALIGNED?` |
| `HD-09` | `1 0 0 0` | `∅` | `67 / — / — / —` | `UNALIGNED?` |
| `HD-10` | `1 0 0 0` | `∅` | `54 / — / — / —` | `UNALIGNED?` |
| `HD-11` | `1 0 0 0` | `∅` | `76 / — / — / —` | `UNALIGNED?` |
| `HD-12` | `1 0 0 0` | `∅` | `57 / — / — / —` | `UNALIGNED?` |
| `HF-01` | `1 0 0 0` | `∅` | `50 / — / — / —` | `UNALIGNED?` |
| `HF-02` | `1 0 0 0` | `∅` | `95 / — / — / —` | `UNALIGNED?` |
| `HF-03` | `1 0 0 0` | `∅` | `89 / — / — / —` | `UNALIGNED?` |
| `HF-04` | `1 0 0 0` | `∅` | `60 / — / — / —` | `UNALIGNED?` |
| `HF-05` | `1 0 0 0` | `∅` | `53 / — / — / —` | `UNALIGNED?` |
| `HF-06` | `1 0 0 0` | `∅` | `92 / — / — / —` | `UNALIGNED?` |
| `HF-07` | `1 0 0 0` | `∅` | `80 / — / — / —` | `UNALIGNED?` |
| `HF-08` | `1 0 0 0` | `∅` | `65 / — / — / —` | `UNALIGNED?` |
| `HF-09` | `1 0 0 0` | `∅` | `73 / — / — / —` | `UNALIGNED?` |
| `HF-10` | `1 0 0 0` | `∅` | `51 / — / — / —` | `UNALIGNED?` |
| `HF-11` | `1 0 0 0` | `∅` | `44 / — / — / —` | `UNALIGNED?` |
| `HF-12` | `1 0 0 0` | `∅` | `61 / — / — / —` | `UNALIGNED?` |
| `HF-13` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `HF-14` | `1 0 0 0` | `∅` | `54 / — / — / —` | `UNALIGNED?` |
| `RF-01` | `1 0 0 0` | `∅` | `42 / — / — / —` | `UNALIGNED?` |
| `RF-02` | `1 0 0 0` | `∅` | `52 / — / — / —` | `UNALIGNED?` |
| `RF-03` | `1 0 0 0` | `∅` | `70 / — / — / —` | `UNALIGNED?` |
| `RF-04` | `1 0 0 0` | `∅` | `94 / — / — / —` | `UNALIGNED?` |
| `RF-05` | `1 0 0 0` | `∅` | `64 / — / — / —` | `UNALIGNED?` |
| `RF-06` | `1 0 0 0` | `∅` | `50 / — / — / —` | `UNALIGNED?` |
| `RF-07` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `RF-08` | `1 0 0 0` | `∅` | `62 / — / — / —` | `UNALIGNED?` |
| `RF-09` | `1 0 0 0` | `∅` | `90 / — / — / —` | `UNALIGNED?` |
| `RF-10` | `1 0 0 0` | `∅` | `54 / — / — / —` | `UNALIGNED?` |
| `RF-11` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `RF-12` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+返工后的优先证据与叙事分流` | `1 0 0 0` | `∅` | `580 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+使用须知先读` | `1 0 0 0` | `∅` | `753 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+主决策表` | `1 0 0 0` | `∅` | `954 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+六域导航` | `1 0 0 0` | `∅` | `1341 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+三条铁律全域通用违反即回到本表` | `1 0 0 0` | `∅` | `1155 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+失败出口` | `1 1 0 0` | `∅` | `296 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/SKILL.md+来源与审计` | `1 0 0 0` | `反` | `449 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/anti-examples.md+1.机械应验谶语违反误读原则` | `1 0 0 0` | `反` | `616 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/anti-examples.md+2.无价忠诚违反代价原则` | `1 0 0 0` | `反` | `669 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/anti-examples.md+3.裸告白求婚违反求婚力学` | `1 0 0 0` | `反` | `572 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/anti-examples.md+4.掉书袋判词违反最短判词律` | `1 0 0 0` | `反` | `473 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/anti-examples.md+5.无规map逃亡违反地形规则引擎` | `1 0 0 0` | `反` | `612 / — / — / —` | `UNALIGNED?` |
| `RE-22` | `1 0 0 0` | `反` | `514 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/document-plot.md+1.构陷的文书链` | `1 0 0 0` | `∅` | `1270 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/document-plot.md+2.真相的释放与判词` | `1 0 0 0` | `∅` | `1198 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/document-plot.md+3.史料接口历史小说专用` | `1 0 0 0` | `∅` | `1285 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/document-plot.md+4.文书的美学` | `1 0 0 0` | `∅` | `817 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/document-plot.md+收束技法` | `1 0 0 0` | `∅` | `607 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+oathtoken域` | `1 0 0 0` | `∅` | `948 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+prophecysong域` | `1 0 0 0` | `∅` | `654 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+madnessmind域` | `1 0 0 0` | `∅` | `779 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+documentplot域` | `1 0 0 0` | `∅` | `676 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+terrainsignal域` | `1 0 0 0` | `∅` | `701 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+kinshiplove域` | `1 0 0 0` | `∅` | `704 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/examples.md+三条铁律的反例警示见antiexamples.md` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+自检顺序四步逐级往下` | `1 0 0 0` | `∅` | `674 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+五类常见死法与修复` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+死法一机械应验谶语` | `1 0 0 0` | `∅` | `162 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+死法二无价忠诚` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+死法三裸告白求婚` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+死法四掉书袋判词` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+死法五无规map逃亡` | `1 0 0 0` | `规` | `196 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+快速诊断问答` | `1 0 0 0` | `∅` | `867 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/failure-modes.md+与三条铁律的对应` | `1 0 0 0` | `∅` | `229 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+1.求婚力学四式` | `1 0 0 0` | `∅` | `1493 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+2.保护性驱逐` | `1 0 0 0` | `∅` | `981 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+3.血亲妒杀线` | `1 0 0 0` | `∅` | `1222 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+4.动物与物作道德参照` | `1 0 0 0` | `∅` | `1023 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+5.死亡收束的形式实验` | `1 0 0 0` | `∅` | `1122 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/kinship-love.md+收束技法` | `1 0 0 0` | `∅` | `641 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/madness-mind.md+1.历史文本中“疯”标签的叙事功能不是医学分型` | `1 0 0 0` | `∅` | `1381 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/madness-mind.md+2.虚构毒杀线的证言误导与取证不提供现实技术` | `1 0 0 0` | `∅` | `1396 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/madness-mind.md+3.义举反噬律` | `1 0 0 0` | `∅` | `886 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/madness-mind.md+4.攻心与守心` | `1 0 0 0` | `∅` | `1442 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/madness-mind.md+收束技法` | `1 0 0 0` | `∅` | `539 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/oath-token.md+1.忠诚票据化` | `1 0 0 0` | `∅` | `1256 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/oath-token.md+2.换名与换装的分工` | `1 0 0 0` | `∅` | `1601 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/oath-token.md+3.双重承诺的化解` | `1 0 0 0` | `∅` | `575 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/oath-token.md+4.信号工程四件套` | `1 0 0 0` | `怎` | `1026 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/oath-token.md+收束技法` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/prophecy-song.md+1.谶语即提纲` | `1 0 0 0` | `∅` | `1393 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/prophecy-song.md+2.歌谣五职` | `1 0 0 0` | `∅` | `1101 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/prophecy-song.md+3.预兆与物候` | `1 0 0 0` | `∅` | `876 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/prophecy-song.md+4.禁忌与反用` | `1 0 0 0` | `∅` | `771 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/prophecy-song.md+收束技法` | `1 0 0 0` | `∅` | `716 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `16 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B02` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/references/source-contract-and-decisions.md+首先判真实历史还是虚构历史` | `1 0 0 0` | `∅` | `520 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/references/source-contract-and-decisions.md+六域按实际矛盾选ab不必全部执行` | `1 0 0 0` | `∅` | `2117 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/references/source-contract-and-decisions.md+公共历史语言的风险` | `1 0 0 0` | `败` | `555 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/references/source-contract-and-decisions.md+最小交付` | `1 0 0 0` | `∅` | `199 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG324` | `1 0 0 0` | `∅` | `2880 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG271` | `1 0 0 0` | `∅` | `2880 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-plot-forge/terrain-signal.md+1.地形规则引擎` | `1 0 0 0` | `∅` | `1459 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/terrain-signal.md+2.账房声部` | `1 0 0 0` | `∅` | `1176 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/terrain-signal.md+3.换锁与潜入工程` | `1 0 0 0` | `∅` | `1150 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/terrain-signal.md+4.单景配角与行进群像` | `1 0 0 0` | `∅` | `1008 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-plot-forge/terrain-signal.md+收束技法` | `1 0 0 0` | `∅` | `671 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+触发` | `1 0 0 0` | `∅` | `242 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+负触发不要加载` | `1 0 0 0` | `∅` | `576 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+输入` | `1 0 0 0` | `∅` | `289 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+执行步骤` | `1 0 0 0` | `∅` | `967 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+输出合同` | `1 0 0 0` | `规检` | `359 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+失败出口` | `1 1 0 0` | `∅` | `353 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/SKILL.md+来源与审计` | `1 0 0 0` | `规` | `731 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `238 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md+冲突组1凭证能否闭合结局` | `1 0 0 0` | `∅` | `519 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md+冲突组2伪装的代价落在哪个规范上` | `1 0 0 0` | `∅` | `351 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md+冲突组3敌人要名声还是要命` | `1 0 0 0` | `∅` | `237 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md+例外与反例保留区不得被吸收为规则` | `1 0 0 0` | `∅` | `983 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md+交叉禁令来源层面` | `1 0 0 0` | `规反` | `317 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/disguise-cost.md+核心主张h由三部作品的对照得出` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/disguise-cost.md+三种已观察到的规范单位f` | `1 0 0 0` | `∅` | `932 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/disguise-cost.md+必做检查` | `1 0 0 0` | `∅` | `498 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/disguise-cost.md+可执行动作p` | `1 0 0 0` | `规` | `537 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/disguise-cost.md+诊断用` | `1 0 0 0` | `∅` | `280 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/era-sensitivity.md+已识别的具体风险点f` | `1 0 0 0` | `∅` | `842 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/era-sensitivity.md+使用规则p` | `1 0 0 0` | `∅` | `817 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/era-sensitivity.md+与其他域的关系` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+五类死法与修复路径` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+死法1结局押在凭证上却没人真正看过凭证` | `1 0 0 0` | `∅` | `445 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+死法2敌人的动机只写"他恨主角"` | `1 0 0 0` | `∅` | `212 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+死法3一句誓言解决了所有问题` | `1 0 0 0` | `∅` | `249 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+死法4谣言传遍全城却无发源人` | `1 0 0 0` | `∅` | `232 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+死法5伪装的代价写错了规范` | `1 0 0 0` | `∅` | `307 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/failure-modes.md+停止点什么时候该停手并交给用户` | `1 0 0 0` | `规` | `545 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/finance-and-instrument.md+必做检查` | `1 0 0 0` | `∅` | `489 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/finance-and-instrument.md+三条来源支持的用法不许混为一谈` | `1 0 0 0` | `∅` | `986 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/finance-and-instrument.md+可掉包凭证的三种写法p` | `1 0 0 0` | `∅` | `328 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/finance-and-instrument.md+反向限制凭证不一定能定案` | `1 0 0 0` | `∅` | `405 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/finance-and-instrument.md+常见错诊断用` | `1 0 0 0` | `∅` | `337 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/history-interface.md+档a纯架空虚拟王国／虚拟政体` | `1 0 0 0` | `规` | `612 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/history-interface.md+档b可核对年代／人物／事件` | `1 0 0 0` | `检` | `738 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/history-interface.md+有明确底本声明的改编` | `1 0 0 0` | `∅` | `364 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/history-interface.md+边缘情况的处理` | `1 0 0 0` | `规` | `516 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/history-interface.md+交叉禁令` | `1 0 0 0` | `∅` | `397 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/hunt-and-pursuit.md+必做检查` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/hunt-and-pursuit.md+来源观察f` | `1 0 0 0` | `败` | `1139 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/hunt-and-pursuit.md+可执行动作p` | `1 0 0 0` | `败` | `569 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/hunt-and-pursuit.md+常见错诊断用` | `1 0 0 0` | `∅` | `442 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/justice-without-forensics.md+候选写法f单源` | `1 0 0 0` | `∅` | `1265 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/justice-without-forensics.md+必做检查若选用本域` | `1 0 0 0` | `∅` | `397 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/justice-without-forensics.md+诊断用` | `1 0 0 0` | `∅` | `241 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/justice-without-forensics.md+为什么不定为本包的承重规则` | `1 0 0 0` | `∅` | `290 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/oath-marriage-inheritance.md+必做检查` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/oath-marriage-inheritance.md+来源观察f` | `1 0 0 0` | `∅` | `1362 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/oath-marriage-inheritance.md+可执行动作p` | `1 0 0 0` | `∅` | `520 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/oath-marriage-inheritance.md+反向提示不许伪造共识` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/performance-and-scapegoat.md+必做检查` | `1 0 0 0` | `∅` | `578 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/performance-and-scapegoat.md+来源观察f` | `1 0 0 0` | `∅` | `1338 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/performance-and-scapegoat.md+可执行动作p` | `1 0 0 0` | `∅` | `502 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/performance-and-scapegoat.md+诊断用` | `1 0 0 0` | `怎` | `379 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/reputation-target.md+三种目标函数本批观察到的全部` | `1 0 0 0` | `∅` | `1213 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/reputation-target.md+必做检查` | `1 0 0 0` | `∅` | `475 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/reputation-target.md+可执行动作p` | `1 0 0 0` | `∅` | `483 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/reputation-target.md+冲突警示` | `1 0 0 0` | `∅` | `277 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/rumor-and-narrative.md+必做检查` | `1 0 0 0` | `∅` | `593 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/rumor-and-narrative.md+来源观察f` | `1 0 0 0` | `∅` | `1138 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/rumor-and-narrative.md+可执行动作p` | `1 0 0 0` | `∅` | `443 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/rumor-and-narrative.md+诊断用` | `1 0 0 0` | `∅` | `353 / — / — / —` | `UNALIGNED?` |
| `historical-fiction-power-machine/references/source-decisions.md+本skill的身份` | `1 0 0 0` | `∅` | `814 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG135` | `1 0 0 0` | `∅` | `1539 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG411` | `1 0 0 0` | `∅` | `1539 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-power-machine/references/source-decisions.md+阅读证据状态` | `1 0 0 0` | `∅` | `674 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-power-machine/references/source-decisions.md+规则裁决对照本类别既有核心规则用本批15源重审` | `1 0 0 0` | `∅` | `1623 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-power-machine/references/source-decisions.md+单源与未证明不得误用` | `1 0 0 0` | `∅` | `397 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-fiction-power-machine/references/source-decisions.md+许可与替代关系` | `1 0 0 0` | `∅` | `351 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+任务路由` | `1 0 0 0` | `∅` | `1011 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+输入权威` | `1 0 0 0` | `∅` | `484 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+可执行流程` | `1 0 0 0` | `∅` | `1037 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+冲突与失败出口` | `1 0 0 0` | `∅` | `543 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+交付格式与provenance` | `1 0 0 0` | `∅` | `436 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/SKILL.md+本批来源与许可边界` | `1 0 0 0` | `∅` | `650 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `297 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/01-time-institution-and-power.md+h01｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `924 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/01-time-institution-and-power.md+h02｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `871 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/01-time-institution-and-power.md+h04｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `848 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/01-time-institution-and-power.md+h05｜keep｜条件规则` | `1 0 0 0` | `规例反败` | `874 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/02-space-objects-and-livelihood.md+h03｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `855 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/02-space-objects-and-livelihood.md+h06｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `845 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/02-space-objects-and-livelihood.md+h07｜keep｜条件规则` | `1 0 0 0` | `规例反败` | `821 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/02-space-objects-and-livelihood.md+h12｜reject｜条件规则` | `1 0 0 0` | `规例反适败` | `777 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/03-blood-identity-and-unreliable-eyes.md+h08｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `844 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/03-blood-identity-and-unreliable-eyes.md+h09｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `836 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/03-blood-identity-and-unreliable-eyes.md+h11｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `794 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/03-blood-identity-and-unreliable-eyes.md+h14｜keep｜条件规则` | `1 0 0 0` | `规例反败` | `870 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/04-voice-frame-and-settlement.md+h10｜keep｜条件规则` | `1 0 0 0` | `规例反败` | `836 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/04-voice-frame-and-settlement.md+h13｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `842 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/04-voice-frame-and-settlement.md+h15｜revise｜条件规则` | `1 0 0 0` | `规例反适败` | `815 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md+旧模式拒绝边界` | `1 0 0 0` | `∅` | `797 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md+历史真实性与虚构推演三层` | `1 0 0 0` | `∅` | `773 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md+修订回归` | `1 0 0 0` | `∅` | `362 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md+a07h16｜带有赦免复仇裁判的历史文本必须标三种层级新增来源补证` | `1 0 0 0` | `反` | `792 / — / — / —` | `UNALIGNED?` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md+a07h17｜作品分组不改变原书题材新增来源补证` | `1 0 0 0` | `例反适` | `623 / — / — / —` | `UNALIGNED?` |
| `PG840` | `1 0 0 0` | `∅` | `4583 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG864` | `1 0 0 0` | `∅` | `4583 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG388` | `1 0 0 0` | `∅` | `4583 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `historical-immersion-and-stakes/references/source-index.md+本轮17书可信阅读与史实边界归档记录不构成运行依赖` | `1 0 0 0` | `∅` | `885 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 07 求生灾变（阈值 20%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 07 求生灾变

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK；本题材按 5.1 节 / §6.1 收紧到 20%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`castaway-salvage-stronghold`、`survival-crisis-escalation`、`wilderness-disaster-survival-craft-b01`

**规则单元数 174；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 174（100.0%）**
**flag 计数**：SOURCE_ONLY=25；UNALIGNED?=174

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `castaway-salvage-stronghold/SKILL.md+1.这个skill解决什么` | `1 0 0 0` | `∅` | `606 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+2.触发负触发` | `1 0 0 0` | `怎` | `893 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+3.证据底座与硬边界` | `1 0 0 0` | `∅` | `984 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+4.体裁三分叉先选这一类参数完全不同` | `1 0 0 0` | `∅` | `783 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+5.任务路由` | `1 0 0 0` | `∅` | `1009 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+6.最短执行路径默认7步` | `1 0 0 0` | `∅` | `1019 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+7.输出物表` | `1 0 0 0` | `∅` | `1058 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+8.规则索引` | `1 0 0 0` | `∅` | `1513 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+9.失败出口` | `1 0 0 0` | `∅` | `634 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/SKILL.md+10.已知冲突不得强行统一` | `1 0 0 0` | `规` | `1219 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `222 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/examples/worked-example.md+用户问题示例` | `1 0 0 0` | `∅` | `111 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/examples/worked-example.md+诊断按skill.md第6节7步` | `1 0 0 0` | `∅` | `155 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/examples/worked-example.md+应用规则` | `1 0 0 0` | `怎` | `1755 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/examples/worked-example.md+改写前后对照` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/examples/worked-example.md+检查` | `1 0 0 0` | `规` | `371 / — / — / —` | `UNALIGNED?` |
| `B02` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/01-inventory-and-measurement.md+b02r1清点建档在第一次取舍前完成并让一项在中段被证伪` | `1 0 0 0` | `规例适` | `2312 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/01-inventory-and-measurement.md+b02r2度量重建先造读数工具再谈配给与排程` | `1 0 0 0` | `规例适` | `1440 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/01-inventory-and-measurement.md+b02r3医学卫生约束入账且至少一次改变决策` | `1 0 0 0` | `规例反` | `1642 / — / — / —` | `UNALIGNED?` |
| `B04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B03` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/02-shelter-engineering.md+b02r4据点写成有入口规则有弱点有后门的资产` | `1 0 0 0` | `规` | `1225 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/02-shelter-engineering.md+b02r5后门可被对手反向利用必须写失守条件` | `1 0 0 0` | `规例反适` | `2074 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B06` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/03-salvage-refit-chain.md+b02r6回收物≥2用途其一延迟兑现` | `1 0 0 0` | `规` | `1316 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/03-salvage-refit-chain.md+b02r7替代链必带明示失效点不做万能装置` | `1 0 0 0` | `规` | `2022 / — / — / —` | `UNALIGNED?` |
| `B08` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B07` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/04-contact-and-signal.md+b02r8接触协议试探示强允许开第一枪的条件` | `1 0 0 0` | `规例适` | `1687 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/04-contact-and-signal.md+b02r9信号载体≥2射程可见性须被论证且有回执或延迟兑现` | `1 0 0 0` | `规败` | `2965 / — / — / —` | `UNALIGNED?` |
| `B09` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B10` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/05-group-governance.md+b02r10权威程序化任命配给权异议渠道与代价继任` | `1 0 0 0` | `规` | `1657 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/05-group-governance.md+b02r11配给可复核+环境补给公开保密按体裁二选一并写代价` | `1 0 0 0` | `规例适` | `2598 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B11` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B12` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/06-cost-and-aftermath.md+b02r12仪式锚点与命名契约可禁名可拒名可被他者命名` | `1 0 0 0` | `规` | `1851 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/06-cost-and-aftermath.md+b02r13结局保留损失清单关系后遗症与被清零的身份` | `1 0 0 0` | `规反` | `2127 / — / — / —` | `UNALIGNED?` |
| `castaway-salvage-stronghold/references/06-cost-and-aftermath.md+附本批次的三条"不得通用化"清单` | `1 0 0 0` | `∅` | `349 / — / — / —` | `UNALIGNED?` |
| `A-08` | `1 0 0 0` | `∅` | `737 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `castaway-salvage-stronghold/references/source-index.md+逐本索引角色覆盖关键行号` | `1 0 0 0` | `∅` | `3652 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `castaway-salvage-stronghold/references/source-index.md+引用纪律` | `1 0 0 0` | `∅` | `444 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+1.这个skill解决什么` | `1 0 0 0` | `∅` | `322 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+2.触发负触发` | `1 0 0 0` | `怎检` | `624 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `反检` | `2665 / — / — / —` | `UNALIGNED?` |
| `P1` | `1 0 0 0` | `反检` | `2665 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `1076 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+5.最短执行路径默认6步` | `1 0 0 0` | `∅` | `1179 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+6.输出物表` | `1 0 0 0` | `∅` | `1013 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `76 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `∅` | `105 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+7.规则索引含本轮裁决` | `1 0 0 0` | `∅` | `2354 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `568 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+9.证据与核验` | `1 0 0 0` | `规` | `569 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+10.agent30.2.0环境资源伦理与任务分流保留` | `1 0 0 0` | `∅` | `1282 / — / — / —` | `UNALIGNED?` |
| `P4` | `1 0 0 0` | `∅` | `1364 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `1364 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/SKILL.md+13.0.3.220261031台账知识融合第二批` | `1 0 0 0` | `∅` | `2190 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `787 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/examples/worked-example.md+场景` | `1 0 0 0` | `∅` | `184 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/examples/worked-example.md+自检` | `1 0 0 0` | `∅` | `198 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/examples/worked-example.md+agent3正常工作流暴风雨后的海岛与合作` | `1 0 0 0` | `∅` | `1241 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/examples/worked-example.md+agent3边界输入没有灾难的乡村生活` | `1 0 0 0` | `适` | `526 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+agent3p3复核revise` | `1 0 0 0` | `怎反适` | `424 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+本轮复核roundp4final20261030裁决revise保留主干收紧机理` | `1 0 0 0` | `例适` | `1580 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+台账融合补充20261031台账补齐run13本全本实读门禁pass` | `1 0 0 0` | `∅` | `796 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+agent3p3复核conditional` | `1 0 0 0` | `怎反适` | `352 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+本轮复核roundp4final20261030裁决keep由condition` | `1 0 0 0` | `例` | `1107 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/01-resource-ledger.md+台账融合补充20261031` | `1 0 0 0` | `规` | `858 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/02-escalation-ladder.md+agent3p3复核revise` | `1 0 0 0` | `怎例反适` | `388 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/02-escalation-ladder.md+本轮复核roundp4final20261030裁决revise撤销pg5874` | `1 0 0 0` | `规例适` | `1508 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/02-escalation-ladder.md+台账融合补充20261031台账补齐run13本全本实读门禁pass` | `1 0 0 0` | `∅` | `584 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/02-escalation-ladder.md+本轮复核roundp4final20261030裁决keep` | `1 0 0 0` | `反` | `1317 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/02-escalation-ladder.md+台账融合补充20261031` | `1 0 0 0` | `反` | `641 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/03-group-governance.md+agent3p3复核revise` | `1 0 0 0` | `怎反适` | `349 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/03-group-governance.md+本轮复核roundp4final20261030裁决revise拆成正例反例边界` | `1 0 0 0` | `例反` | `1682 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/03-group-governance.md+台账融合补充20261031台账补齐run13本全本实读门禁pass` | `1 0 0 0` | `∅` | `1092 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/03-group-governance.md+本轮复核roundp4final20261030裁决keep并降级未重读的行号` | `1 0 0 0` | `反` | `1016 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/03-group-governance.md+本轮复核roundp4final20261030裁决keep冲突不调和` | `1 0 0 0` | `∅` | `1630 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/04-shelter-salvage.md+agent3p3复核conditional` | `1 0 0 0` | `规怎例反适` | `372 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/04-shelter-salvage.md+本轮复核roundp4final20261030裁决keep` | `1 0 0 0` | `规反` | `1201 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/04-shelter-salvage.md+台账融合补充20261031台账补齐run13本全本实读门禁pass` | `1 0 0 0` | `∅` | `1309 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/04-shelter-salvage.md+agent3p3复核revise` | `1 0 0 0` | `怎反适` | `366 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/04-shelter-salvage.md+本轮复核roundp4final20261030裁决revise补强正例改写pg` | `1 0 0 0` | `例反适` | `1552 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+agent3p3复核conditional` | `1 0 0 0` | `怎反适` | `348 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+本轮复核roundp4final20261030裁决revise由conditi` | `1 0 0 0` | `适` | `1290 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+台账融合补充20261031台账补齐run13本全本实读门禁pass` | `1 0 0 0` | `∅` | `1154 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+本轮复核roundp4final20261030裁决keep双向不合并` | `1 0 0 0` | `∅` | `1271 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+agent3p3复核revise` | `1 0 0 0` | `怎反适败` | `422 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+本轮复核roundp4final20261030裁决revise补入同书反例` | `1 0 0 0` | `反` | `1485 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+agent3p3复核keep` | `1 0 0 0` | `怎反检适` | `359 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+本轮复核roundp4final20261030裁决keep本批证据最强的一条` | `1 0 0 0` | `反` | `1296 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md+本轮复核roundp4final20261030裁决revise由一条要求改为四` | `1 0 0 0` | `反` | `1910 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+fpg2127paulandvirginia中的自然节律不等于倒计时` | `1 0 0 0` | `反` | `1608 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+fpg10076lister’sgreatadventure中的威胁换类和职业边` | `1 0 0 0` | `适` | `856 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+fpg36950richardgalbraithmariner的叙述者观点与事实` | `1 0 0 0` | `例` | `1746 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+伦理反例pg62319cosmiccastaway` | `1 0 0 0` | `∅` | `665 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+反例到规则的决策表` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+跨书机制组20261031台账融合新增双源互证` | `1 0 0 0` | `∅` | `1671 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md+验收层级` | `1 0 0 0` | `反` | `462 / — / — / —` | `UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+环境物资与信号同一机制并非固定配方` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+群体身份与伦理角色做法有效不等于正当` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+pg14249halfachance类型边界` | `1 0 0 0` | `例` | `1023 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+三组跨书机制20261031融合新增双源互证` | `1 0 0 0` | `∅` | `1188 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+四组不应强行调和的冲突` | `1 0 0 0` | `∅` | `765 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md+退出和验证边界` | `1 0 0 0` | `∅` | `687 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG789` | `1 0 0 0` | `∅` | `7067 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/source-index.md+关键证据关系与去重` | `1 0 0 0` | `∅` | `1043 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/source-index.md+20261031证据修复的真实贡献` | `1 0 0 0` | `∅` | `1257 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `survival-crisis-escalation/references/source-index.md+法律和使用边界` | `1 0 0 0` | `∅` | `280 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+触发用本技能` | `1 0 0 0` | `∅` | `514 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+负触发不要用本技能` | `1 0 0 0` | `怎` | `535 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+输入少了就先问不要猜` | `1 0 0 0` | `∅` | `490 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+任务路由读完输入后先选一条` | `1 0 0 0` | `∅` | `516 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+步骤1定环境档位决定首日顺序不要套唯一顺序` | `1 0 0 0` | `∅` | `568 / — / — / —` | `UNALIGNED?` |
| `R-B` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `R-C` | `1 0 0 0` | `∅` | `498 / — / — / —` | `UNALIGNED?` |
| `R-D` | `1 0 0 0` | `∅` | `333 / — / — / —` | `UNALIGNED?` |
| `R-E` | `1 0 0 0` | `反` | `383 / — / — / —` | `UNALIGNED?` |
| `R-F` | `1 0 0 0` | `∅` | `381 / — / — / —` | `UNALIGNED?` |
| `R-G` | `1 0 0 0` | `∅` | `417 / — / — / —` | `UNALIGNED?` |
| `R-H` | `1 0 0 0` | `∅` | `312 / — / — / —` | `UNALIGNED?` |
| `R-I` | `1 0 0 0` | `∅` | `380 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+步骤10可选按题材制度线双引擎` | `1 0 0 0` | `∅` | `309 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+步骤11收尾与登记` | `1 0 0 0` | `规` | `383 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+输出合同每次必须给这些` | `1 0 0 0` | `∅` | `685 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+失败出口做不到就明确说不要硬编` | `1 0 0 0` | `规` | `796 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/SKILL.md+来源` | `1 0 0 0` | `规败` | `640 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `检` | `1497 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md+§1被保留的四条真实冲突` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C-1` | `1 0 0 0` | `∅` | `564 / — / — / —` | `UNALIGNED?` |
| `C-2` | `1 0 0 0` | `∅` | `335 / — / — / —` | `UNALIGNED?` |
| `C-3` | `1 0 0 0` | `∅` | `349 / — / — / —` | `UNALIGNED?` |
| `C-4` | `1 0 0 0` | `∅` | `285 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md+§2明确不采纳reject` | `1 0 0 0` | `∅` | `976 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md+§3notproven不得包装成通则` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md+§4singlesource清单使用时必须显式标注` | `1 0 0 0` | `∅` | `1406 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md+§5时代与体裁限定引用时必须同句标注` | `1 0 0 0` | `∅` | `779 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/failure-modes.md+快速判定顺序时间不够就走这5步` | `1 0 0 0` | `∅` | `313 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/failure-modes.md+诊断输出格式每次必须给这些` | `1 0 0 0` | `规` | `334 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/failure-modes.md+不适用的诊断请求走失败出口` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `R-K` | `1 0 0 0` | `规怎` | `536 / — / — / —` | `UNALIGNED?` |
| `R-A` | `1 0 0 0` | `规怎` | `536 / — / — / —` | `UNALIGNED?` |
| `R-J` | `1 0 0 0` | `怎适` | `795 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/rules.md+收尾母题三选一不要并列` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/rules.md+版本学登记引用pg电子文本时` | `1 0 0 0` | `∅` | `248 / — / — / —` | `UNALIGNED?` |
| `S-1` | `1 0 0 0` | `∅` | `857 / — / — / —` | `UNALIGNED?` |
| `S-2` | `1 0 0 0` | `∅` | `750 / — / — / —` | `UNALIGNED?` |
| `S-3` | `1 0 0 0` | `∅` | `816 / — / — / —` | `UNALIGNED?` |
| `S-4` | `1 0 0 0` | `∅` | `884 / — / — / —` | `UNALIGNED?` |
| `S-5` | `1 0 0 0` | `∅` | `875 / — / — / —` | `UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/scene-patterns.md+附短篇单场景的减法` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `PG215` | `1 0 0 0` | `∅` | `7118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG521` | `1 0 0 0` | `∅` | `7118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B01` | `1 0 0 0` | `∅` | `7118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG159` | `1 0 0 0` | `∅` | `7118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG393` | `1 0 0 0` | `∅` | `7118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `wilderness-disaster-survival-craft-b01/references/source-index.md+同环境取样建议构思时按环境挑样本` | `1 0 0 0` | `∅` | `554 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 08 探险寻宝（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 08 探险寻宝

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`adventure-treasure-craft`、`adventure-treasure-craft-b02`、`adventure-treasure-craft-b03`

**规则单元数 161；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 161（100.0%）**
**flag 计数**：SOURCE_ONLY=25；UNALIGNED?=161

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `P4` | `1 0 0 0` | `∅` | `2164 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+1.何时使用` | `1 0 0 0` | `例检` | `801 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+2.负触发不要用本skill` | `1 0 0 0` | `例反` | `600 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+3.最短路径` | `1 0 0 0` | `∅` | `1265 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `1041 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+5.证据声明` | `1 0 0 0` | `∅` | `1102 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `352 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/SKILL.md+7.跨skill单向接口` | `1 0 0 0` | `∅` | `738 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `167 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/examples/worked-example.md+example1沉船宝藏线价值论+藏宝四问+钓鱼收网` | `1 0 0 0` | `规` | `1755 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft/examples/worked-example.md+example2深空异变线非人对手破译+情绪武器` | `1 0 0 0` | `规` | `1879 / — / — / —` | `UNALIGNED?` |
| `M03` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M01` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M02` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M20` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M05` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M07` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M09` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M08` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M06` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M11` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M13` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M10` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M12` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M04` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M26` | `1 0 0 0` | `规适` | `280 / — / — / —` | `UNALIGNED?` |
| `M29` | `1 0 0 0` | `规适` | `264 / — / — / —` | `UNALIGNED?` |
| `M30` | `1 0 0 0` | `规适` | `296 / — / — / —` | `UNALIGNED?` |
| `M31` | `1 0 0 0` | `规适` | `243 / — / — / —` | `UNALIGNED?` |
| `M14` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M19` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M15` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M16` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M25` | `1 0 0 0` | `规适` | `337 / — / — / —` | `UNALIGNED?` |
| `M18` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M22` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M17` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M23` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M24` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `M27` | `1 0 0 0` | `规适` | `265 / — / — / —` | `UNALIGNED?` |
| `M21` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/06-endings-and-sources.md+§3来源索引` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `1253 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/06-endings-and-sources.md+3.2编号约定` | `1 0 0 0` | `规例反` | `716 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/06-endings-and-sources.md+3.3覆盖状态` | `1 0 0 0` | `适` | `467 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `M28` | `1 0 0 0` | `规适` | `320 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `M32` | `1 0 0 0` | `规适` | `258 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/06-endings-and-sources.md+7.决策统计全32条含第一部分24条+本部分8条` | `1 0 0 0` | `∅` | `1174 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/06-endings-and-sources.md+8.引文抽检本棒grep实检路径来源批次16类型小说专项14探险寻宝批次01` | `1 0 0 0` | `∅` | `1626 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `424 / — / — / —` | `UNALIGNED?` |
| `PG103` | `1 0 0 0` | `∅` | `92 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG120` | `1 0 0 0` | `∅` | `112 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG589` | `1 0 0 0` | `∅` | `92 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG647` | `1 0 0 0` | `∅` | `92 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG710` | `1 0 0 0` | `∅` | `172 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG788` | `1 0 0 0` | `∅` | `142 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft/references/version-and-provenance.md+全部来源与作用` | `1 0 0 0` | `∅` | `3326 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b02/SKILL.md+触发与排除` | `1 0 0 0` | `∅` | `336 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/SKILL.md+输入预检` | `1 0 0 0` | `∅` | `339 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/SKILL.md+路由与工作流` | `1 0 0 0` | `∅` | `1535 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/SKILL.md+冲突与缺料出口` | `1 0 0 0` | `∅` | `531 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/SKILL.md+输出原作与许可` | `1 0 0 0` | `∅` | `722 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re01｜revise` | `1 0 0 0` | `例反适` | `651 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re02｜revise` | `1 0 0 0` | `反适` | `707 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re03｜reject` | `1 0 0 0` | `反适` | `684 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re04｜revise` | `1 0 0 0` | `反适` | `733 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re05｜reject` | `1 0 0 0` | `反适` | `694 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re06｜reject` | `1 0 0 0` | `反适` | `644 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re07｜revise` | `1 0 0 0` | `反适` | `634 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re08｜revise` | `1 0 0 0` | `反适` | `706 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re09｜keep` | `1 0 0 0` | `反适` | `746 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re10｜revise` | `1 0 0 0` | `例反适` | `708 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re11｜revise` | `1 0 0 0` | `反检适` | `692 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re12｜revise` | `1 0 0 0` | `反适` | `710 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re13｜revise` | `1 0 0 0` | `反适` | `725 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re14｜reject` | `1 0 0 0` | `反适` | `667 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re15｜keep` | `1 0 0 0` | `反适` | `703 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re16｜reject` | `1 0 0 0` | `反适` | `658 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re17｜keep` | `1 0 0 0` | `例反适` | `700 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/rules.md+re18｜revise` | `1 0 0 0` | `反适` | `702 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/scope-and-conflicts.md+适用` | `1 0 0 0` | `∅` | `258 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/scope-and-conflicts.md+旧c11–c13冲突重裁` | `1 0 0 0` | `∅` | `617 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b02/references/scope-and-conflicts.md+失败出口` | `1 0 0 0` | `∅` | `331 / — / — / —` | `UNALIGNED?` |
| `PG839` | `1 0 0 0` | `∅` | `10522 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG236` | `1 0 0 0` | `∅` | `10522 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b02/references/source-index.md+本批次补证索引不携带原著原文` | `1 0 0 0` | `∅` | `640 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `T01` | `1 0 0 0` | `∅` | `437 / — / — / —` | `UNALIGNED?` |
| `T02` | `1 0 0 0` | `∅` | `581 / — / — / —` | `UNALIGNED?` |
| `T03` | `1 0 0 0` | `∅` | `425 / — / — / —` | `UNALIGNED?` |
| `T04` | `1 0 0 0` | `∅` | `393 / — / — / —` | `UNALIGNED?` |
| `T05` | `1 0 0 0` | `∅` | `416 / — / — / —` | `UNALIGNED?` |
| `T06` | `1 0 0 0` | `∅` | `291 / — / — / —` | `UNALIGNED?` |
| `T07` | `1 0 0 0` | `∅` | `522 / — / — / —` | `UNALIGNED?` |
| `T08` | `1 0 0 0` | `∅` | `552 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+触发` | `1 0 0 0` | `∅` | `302 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+负触发明确不做转给别的skill或直接说明` | `1 0 0 0` | `∅` | `456 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+输入缺失就写unknown不要替用户补` | `1 0 0 0` | `∅` | `659 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+执行步骤` | `1 0 0 0` | `∅` | `1508 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+规则速查详细裁决依据行号在referencesrules.md` | `1 0 0 0` | `∅` | `1325 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+冲突与缺料出口必须给用户条件分支不许替他选` | `1 0 0 0` | `规` | `620 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+输出合同` | `1 0 0 0` | `∅` | `484 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+失败出口` | `1 0 0 0` | `反适` | `380 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/SKILL.md+来源与许可` | `1 0 0 0` | `∅` | `410 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规` | `1931 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+第1步｜路由` | `1 0 0 0` | `规` | `409 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+第2步｜正当性四问本批最该先看的一步` | `1 0 0 0` | `∅` | `666 / — / — / —` | `UNALIGNED?` |
| `RE-17` | `1 0 0 0` | `∅` | `612 / — / — / —` | `UNALIGNED?` |
| `RE-11` | `1 0 0 0` | `∅` | `612 / — / — / —` | `UNALIGNED?` |
| `N4` | `1 0 0 0` | `∅` | `612 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+第4步｜路线与资源` | `1 0 0 0` | `∅` | `453 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+第5步｜结算` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+第6步｜分支` | `1 0 0 0` | `∅` | `432 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/examples/worked-example.md+输出给用户的答复要点` | `1 0 0 0` | `∅` | `486 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `815 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `适` | `652 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `590 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `528 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/conflicts-and-exceptions.md+例外本批明确"不适用"的来源` | `1 0 0 0` | `∅` | `390 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/conflicts-and-exceptions.md+未证明notproven` | `1 0 0 0` | `∅` | `608 / — / — / —` | `UNALIGNED?` |
| `RE-05` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-02` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `N6` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-01` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-15` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-08` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-18` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-12` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `N1` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-14` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-04` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-07` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-10` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-16` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-06` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `N5` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `N3` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-03` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-09` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `N2` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `RE-13` | `1 0 0 0` | `规检` | `522 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/rules.md+一re01–re18本批裁决` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/rules.md+二本批新增规则n1–n6` | `1 0 0 0` | `∅` | `1581 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/rules.md+三使用规则的三条纪律` | `1 0 0 0` | `∅` | `435 / — / — / —` | `UNALIGNED?` |
| `PG344` | `1 0 0 0` | `∅` | `5823 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG164` | `1 0 0 0` | `∅` | `5823 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b03/references/subtype-routing.md+为什么必须先路由` | `1 0 0 0` | `∅` | `659 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/subtype-routing.md+路由表` | `1 0 0 0` | `∅` | `1195 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/subtype-routing.md+判定顺序自上而下命中即停` | `1 0 0 0` | `∅` | `429 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/references/version-and-provenance.md+本版元数据` | `1 0 0 0` | `∅` | `904 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b03/references/version-and-provenance.md+与相邻批次的替代关系supersession` | `1 0 0 0` | `∅` | `699 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b03/references/version-and-provenance.md+本轮实质变更相对"无"的基线` | `1 0 0 0` | `∅` | `802 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b03/references/version-and-provenance.md+未解决` | `1 0 0 0` | `检` | `320 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+0.路由结论` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+1.正当性四问fhp分标` | `1 0 0 0` | `∅` | `204 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+2.线索表` | `1 0 0 0` | `∅` | `284 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+3.路线与资源表` | `1 0 0 0` | `∅` | `197 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+4.结算清单` | `1 0 0 0` | `∅` | `226 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+5.冲突与缺料分支` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+6.用到的规则` | `1 0 0 0` | `规` | `153 / — / — / —` | `UNALIGNED?` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md+7.交付物` | `1 0 0 0` | `检` | `119 / — / — / —` | `UNALIGNED?` |

---

## 题材 09 喜剧（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 09 喜剧

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`comedy-beat-craft`、`comedy-scene-mechanics`、`comic-engine-craft`、`comic-fiction-diagnosis`

**规则单元数 204；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 204（100.0%）**
**flag 计数**：SOURCE_ONLY=20；UNALIGNED?=204

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `comedy-beat-craft/SKILL.md+0.来源与可信边界` | `1 0 0 0` | `怎` | `1269 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+1.触发` | `1 0 0 0` | `适` | `483 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+2.负触发遇到了不要硬套直接说不适用` | `1 0 0 0` | `规例适` | `477 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+3.输入缺一项就先问不要替用户填` | `1 0 0 0` | `∅` | `631 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `956 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+5.执行步骤5个动作2个门` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `G1` | `1 0 0 0` | `∅` | `635 / — / — / —` | `UNALIGNED?` |
| `G2` | `1 0 0 0` | `∅` | `853 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `∅` | `853 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `∅` | `66 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+6.输出合同三件缺一件不算完成` | `1 0 0 0` | `∅` | `934 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+7.失败出口遇到就照着说不要绕过去` | `1 0 0 0` | `∅` | `993 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `规` | `113 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `规` | `177 / — / — / —` | `UNALIGNED?` |
| `B4A` | `1 0 0 0` | `规` | `144 / — / — / —` | `UNALIGNED?` |
| `B4B` | `1 0 0 0` | `规` | `163 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `规` | `116 / — / — / —` | `UNALIGNED?` |
| `B8` | `1 0 0 0` | `规` | `133 / — / — / —` | `UNALIGNED?` |
| `B10` | `1 0 0 0` | `规` | `102 / — / — / —` | `UNALIGNED?` |
| `B11` | `1 0 0 0` | `规` | `111 / — / — / —` | `UNALIGNED?` |
| `B12` | `1 0 0 0` | `规` | `156 / — / — / —` | `UNALIGNED?` |
| `B6A` | `1 0 0 0` | `规` | `117 / — / — / —` | `UNALIGNED?` |
| `B6B` | `1 0 0 0` | `规` | `122 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+8.规则索引本批派生` | `1 0 0 0` | `规` | `1794 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+9.禁止项` | `1 0 0 0` | `规` | `566 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/SKILL.md+10.与邻近批次成果的关系` | `1 0 0 0` | `∅` | `553 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `432 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+§1g1形态门先决定参数能不能用` | `1 0 0 0` | `∅` | `426 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+舞台短体可用的参数f来自pg5328` | `1 0 0 0` | `∅` | `558 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+长篇短篇集可用的只有三条` | `1 0 0 0` | `∅` | `1353 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+§2g2归属三格与b3` | `1 0 0 0` | `∅` | `562 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+§3节拍表模板逐场景逐章一行` | `1 0 0 0` | `检` | `1000 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/01-attribution-and-beats.md+§4场景与叙事节拍的容器来自哪里` | `1 0 0 0` | `∅` | `800 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+§1节拍型机制` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+§2情境型机制` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+§3语言型机制` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+§4结构型机制本批证据较弱只用不推广` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+机制可复制因而可失效` | `1 0 0 0` | `∅` | `381 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+递减序列` | `1 0 0 0` | `∅` | `480 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/02-mechanism-library.md+§5这三本不能当机制证据` | `1 0 0 0` | `∅` | `380 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+§1五组分叉` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+分支1省略vs铺陈` | `1 0 0 0` | `∅` | `740 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+分支2保密对象b4ab4b` | `1 0 0 0` | `∅` | `804 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+分支3可开玩笑的对象` | `1 0 0 0` | `∅` | `894 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+分支4终点` | `1 0 0 0` | `∅` | `670 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+分支5题材行情提醒采纳与否` | `1 0 0 0` | `∅` | `456 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+§2禁止项复述skill.md§9附证据` | `1 0 0 0` | `∅` | `700 / — / — / —` | `UNALIGNED?` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md+§3疲劳提示notproven只能当自查项` | `1 0 0 0` | `∅` | `573 / — / — / —` | `UNALIGNED?` |
| `B-04` | `1 0 0 0` | `∅` | `9538 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B02` | `1 0 0 0` | `∅` | `9538 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-beat-craft/references/04-source-index.md+族去重用共识前必须先做` | `1 0 0 0` | `∅` | `594 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-beat-craft/references/04-source-index.md+逐条引文复算` | `1 0 0 0` | `∅` | `266 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+0.这是什么` | `1 0 0 0` | `∅` | `483 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+1.证据底座` | `1 0 0 0` | `反` | `1029 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+触发` | `1 0 0 0` | `∅` | `359 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+负触发` | `1 0 0 0` | `例` | `468 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+3.输入缺任一项先问不猜` | `1 0 0 0` | `∅` | `545 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+4.最短执行路径3个门顺序不可跳` | `1 0 0 0` | `例` | `935 / — / — / —` | `UNALIGNED?` |
| `M1` | `1 0 0 0` | `∅` | `175 / — / — / —` | `UNALIGNED?` |
| `M2` | `1 0 0 0` | `∅` | `157 / — / — / —` | `UNALIGNED?` |
| `M3` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `M4` | `1 0 0 0` | `∅` | `160 / — / — / —` | `UNALIGNED?` |
| `M5` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `∅` | `169 / — / — / —` | `UNALIGNED?` |
| `M7` | `1 0 0 0` | `∅` | `162 / — / — / —` | `UNALIGNED?` |
| `M8` | `1 0 0 0` | `∅` | `144 / — / — / —` | `UNALIGNED?` |
| `M9` | `1 0 0 0` | `∅` | `165 / — / — / —` | `UNALIGNED?` |
| `M10` | `1 0 0 0` | `∅` | `158 / — / — / —` | `UNALIGNED?` |
| `M11` | `1 0 0 0` | `∅` | `170 / — / — / —` | `UNALIGNED?` |
| `M12` | `1 0 0 0` | `∅` | `179 / — / — / —` | `UNALIGNED?` |
| `S1` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+5.规则索引m1–m12+s1canonical在各文件` | `1 0 0 0` | `∅` | `2229 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+6.禁止项` | `1 0 0 0` | `∅` | `799 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+7.三张最小模板输出合同的一部分` | `1 0 0 0` | `例` | `546 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `813 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+9.文件地图与自检` | `1 0 0 0` | `∅` | `744 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/SKILL.md+10.元数据版本来源覆盖许可替代关系` | `1 0 0 0` | `∅` | `1452 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `检` | `1002 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/01-narrator-devices.md+1.m1冷面自欺叙述者置信高` | `1 0 0 0` | `规例反适` | `1758 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/01-narrator-devices.md+2.m11元叙述与机制自陈置信中取代历史规则c8` | `1 0 0 0` | `规` | `1881 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/01-narrator-devices.md+3.m12开场三型置信中修订历史规则c10` | `1 0 0 0` | `∅` | `1256 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/02-incongruity-devices.md+1.m2伪精确与冗余计算置信高` | `1 0 0 0` | `检` | `1356 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/02-incongruity-devices.md+2.m3清单递进置信高` | `1 0 0 0` | `∅` | `1249 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/02-incongruity-devices.md+3.m4比喻延长句置信高` | `1 0 0 0` | `∅` | `1537 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/02-incongruity-devices.md+4.m5语域错位与字面化置信中戏剧可用` | `1 0 0 0` | `∅` | `1706 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/03-plot-devices.md+1.m6重复签名与节拍置信高戏剧可用` | `1 0 0 0` | `∅` | `1627 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/03-plot-devices.md+2.m7错位对话置信中仅合谋位` | `1 0 0 0` | `∅` | `1480 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/03-plot-devices.md+3.m8即兴谎言的自生长与反噬置信中仅合谋位` | `1 0 0 0` | `反` | `1739 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/03-plot-devices.md+4.m9认知翻转置信中戏剧可用` | `1 0 0 0` | `∅` | `1349 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/03-plot-devices.md+5.m10荒诞前提+一本正经的机构流程置信中` | `1 0 0 0` | `适` | `1448 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/04-satire-costs.md+1.s1讽刺的成本与反噬置信中` | `1 0 0 0` | `∅` | `3006 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/04-satire-costs.md+2.三条保留冲突不由本skill统一` | `1 0 0 0` | `∅` | `1086 / — / — / —` | `UNALIGNED?` |
| `comedy-scene-mechanics/references/04-satire-costs.md+3.未证明写清不编` | `1 0 0 0` | `∅` | `362 / — / — / —` | `UNALIGNED?` |
| `PG844` | `1 0 0 0` | `∅` | `2811 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `SHA-256` | `1 0 0 0` | `∅` | `2811 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG883` | `1 0 0 0` | `∅` | `2811 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG308` | `1 0 0 0` | `∅` | `2811 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG119` | `1 0 0 0` | `∅` | `2811 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-scene-mechanics/references/05-source-index.md+2.族去重与覆盖档位` | `1 0 0 0` | `∅` | `1156 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-scene-mechanics/references/05-source-index.md+3.对历史规则集c1–c10的裁决完整记录` | `1 0 0 0` | `∅` | `3503 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comedy-scene-mechanics/references/05-source-index.md+4.单部作品的情节设计≠通则本skill明确拒绝的推广` | `1 0 0 0` | `∅` | `548 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-engine-craft/SKILL.md+0.这是什么不是什么` | `1 0 0 0` | `规` | `730 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `规` | `2105 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `521 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `992 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+4.最短执行路径两个门` | `1 0 0 0` | `∅` | `462 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `130 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `228 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `147 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `∅` | `109 / — / — / —` | `UNALIGNED?` |
| `C6` | `1 0 0 0` | `∅` | `141 / — / — / —` | `UNALIGNED?` |
| `C7` | `1 0 0 0` | `∅` | `123 / — / — / —` | `UNALIGNED?` |
| `C8` | `1 0 0 0` | `∅` | `96 / — / — / —` | `UNALIGNED?` |
| `C9` | `1 0 0 0` | `∅` | `94 / — / — / —` | `UNALIGNED?` |
| `C10` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `C11` | `1 0 0 0` | `∅` | `103 / — / — / —` | `UNALIGNED?` |
| `C12` | `1 0 0 0` | `∅` | `96 / — / — / —` | `UNALIGNED?` |
| `C13` | `1 0 0 0` | `∅` | `128 / — / — / —` | `UNALIGNED?` |
| `C14` | `1 0 0 0` | `∅` | `93 / — / — / —` | `UNALIGNED?` |
| `C15` | `1 0 0 0` | `∅` | `237 / — / — / —` | `UNALIGNED?` |
| `C16` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+5.规则索引16条` | `1 0 0 0` | `∅` | `2199 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+6.禁止项` | `1 0 0 0` | `规` | `655 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+7.两张最小模板` | `1 0 0 0` | `∅` | `402 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `725 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+9.元数据与替代关系从历史成果迁移` | `1 0 0 0` | `∅` | `1201 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+10.笑点调度与误会诊断执行要点` | `1 0 0 0` | `∅` | `1135 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/SKILL.md+11.1.0.120261031台账知识融合第二批` | `1 0 0 0` | `例` | `2280 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `665 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/examples/worked-example.md+正常社区业主会议虚构` | `1 0 0 0` | `∅` | `875 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/examples/worked-example.md+冲突作者要求嘲弄弱势群体` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/examples/worked-example.md+缺料一句“帮我写喜剧”` | `1 0 0 0` | `∅` | `318 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/examples/worked-example.md+边界葬礼与纯哀伤` | `1 0 0 0` | `∅` | `332 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/02-satire-engines.md+§6制度字面主义new三源互证20261031台账融合` | `1 0 0 0` | `适` | `1365 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/02-satire-engines.md+§7虚惊与讣告new双源互证20261031台账融合` | `1 0 0 0` | `∅` | `995 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§1c10开篇建立预期随后错位revise加连作例外` | `1 0 0 0` | `例` | `1136 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§2c11拒写与省略本身即包袱新增` | `1 0 0 0` | `规适` | `1649 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§3c12清单升级+一次结算新增` | `1 0 0 0` | `∅` | `1464 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§4c14单点装置反复结算新增` | `1 0 0 0` | `败` | `1671 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§5c15帮助反成对方的工具新增冲突项不调和` | `1 0 0 0` | `反` | `1905 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§6c16道德选择写成算账不画成长曲线新增` | `1 0 0 0` | `∅` | `467 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+§7文件层反讽new三源互证20261031台账融合` | `1 0 0 0` | `∅` | `1233 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/03-openings-and-formats.md+已验证的体裁差异不得统一为一条规则` | `1 0 0 0` | `∅` | `609 / — / — / —` | `UNALIGNED?` |
| `PG718` | `1 0 0 0` | `∅` | `4774 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG580` | `1 0 0 0` | `∅` | `4774 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG587` | `1 0 0 0` | `∅` | `4774 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-engine-craft/references/05-confidence-and-feedback.md+pg3829loveamongthechickens高信心与实质资源冲突` | `1 0 0 0` | `败` | `974 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/05-confidence-and-feedback.md+pg3184alonzofitzandotherstories善意的后果不是定律` | `1 0 0 0` | `∅` | `848 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/05-confidence-and-feedback.md+pg1999cromeyellow技法口号的舞台性` | `1 0 0 0` | `∅` | `556 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/05-confidence-and-feedback.md+pg7464theadventuresofsally别人的钱如何验证自信2026` | `1 0 0 0` | `∅` | `1405 / — / — / —` | `UNALIGNED?` |
| `comic-engine-craft/references/05-confidence-and-feedback.md+适用冲突与退出` | `1 0 0 0` | `例适` | `920 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+0.这是什么` | `1 0 0 0` | `∅` | `584 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+1.版本来源与可信边界必读影响每条规则的用法` | `1 0 0 0` | `∅` | `1963 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+触发` | `1 0 0 0` | `∅` | `505 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+负触发` | `1 0 0 0` | `例` | `430 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1152 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+4.最短执行路径4个门按顺序过` | `1 0 0 0` | `例检` | `1241 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+5.规则索引12条canonical在各references文件` | `1 0 0 0` | `∅` | `2191 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+5.1对comicenginecraft批次04c1–c10的迁移裁决摘要完整依` | `1 0 0 0` | `∅` | `1082 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+6.禁止项违反即输出无效` | `1 0 0 0` | `∅` | `1176 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+7.三张最小模板空列一律写"未知"不得留空不得编` | `1 0 0 0` | `∅` | `519 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `1206 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/SKILL.md+9.文件地图与自检` | `1 0 0 0` | `例` | `890 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `619 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/examples/worked-example.md+用户请求` | `1 0 0 0` | `∅` | `273 / — / — / —` | `UNALIGNED?` |
| `G3` | `1 0 0 0` | `∅` | `266 / — / — / —` | `UNALIGNED?` |
| `K-3` | `1 0 0 0` | `∅` | `266 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `530 / — / — / —` | `UNALIGNED?` |
| `B7` | `1 0 0 0` | `例` | `478 / — / — / —` | `UNALIGNED?` |
| `B6` | `1 0 0 0` | `例` | `478 / — / — / —` | `UNALIGNED?` |
| `B9` | `1 0 0 0` | `例` | `478 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/examples/worked-example.md+最终交付形态` | `1 0 0 0` | `例` | `1064 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/examples/worked-example.md+走完之后的自我检查` | `1 0 0 0` | `例` | `390 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/01-attribution-and-evidence.md+b101笑点归属keep多族` | `1 0 0 0` | `适` | `1560 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/01-attribution-and-evidence.md+b102荒诞前提靠"认真执行"成立keep有条件` | `1 0 0 0` | `例反适` | `862 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/01-attribution-and-evidence.md+b104物证比信息缺失更耐用keep本批最强` | `1 0 0 0` | `例反` | `1161 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/01-attribution-and-evidence.md+b111谎话连锁的内部自洽keep仅twain族` | `1 0 0 0` | `例检` | `956 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md+b103术语落到身体与实物上keep多族` | `1 0 0 0` | `败` | `1023 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md+b106全知解题者是角色设定不是写作方法reject普适keep边界` | `1 0 0 0` | `败` | `855 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md+b107公开版与私下版同时可见keep多族` | `1 0 0 0` | `∅` | `851 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md+b108讽刺到阈值必须让位keep硬伦理边界` | `1 0 0 0` | `∅` | `795 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md+b112依赖天生属性的笑点keep硬规则` | `1 0 0 0` | `∅` | `1443 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+b105重复包袱的变化维度revise原定量表述被拒` | `1 0 0 0` | `检` | `1175 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+b109陈述句本身可以是包袱keep有条件` | `1 0 0 0` | `适` | `1050 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+b110题目／口号／童年口头禅的反转回收keep有条件+反例` | `1 0 0 0` | `反` | `921 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+c2'期待差迁移改写载体从"信件"改为"可验证的承诺"` | `1 0 0 0` | `∅` | `1021 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+c10'开篇迁移改写从"建期待"扩为"给出一种可核对的承诺"` | `1 0 0 0` | `规反检` | `970 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md+c9'兑现位置迁移降级从"服从pov"改为"选择项"` | `1 0 0 0` | `规反` | `676 / — / — / —` | `UNALIGNED?` |
| `PG968` | `1 0 0 0` | `∅` | `2350 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-fiction-diagnosis/references/04-source-index.md+族去重引用时必须带族` | `1 0 0 0` | `∅` | `876 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-fiction-diagnosis/references/04-source-index.md+阅读台账分布供回源` | `1 0 0 0` | `∅` | `682 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-fiction-diagnosis/references/04-source-index.md+历史缺口与本轮处置如实` | `1 0 0 0` | `∅` | `763 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `comic-fiction-diagnosis/references/04-source-index.md+许可与引用` | `1 0 0 0` | `∅` | `308 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `K-1` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `K-4` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `K-2` | `1 0 0 0` | `∅` | `728 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/05-conflicts-and-anti-patterns.md+§2六条禁止升格为规则的观察真实存在但复制会受害` | `1 0 0 0` | `∅` | `1171 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/05-conflicts-and-anti-patterns.md+§3c1–c10迁移裁决的完整依据` | `1 0 0 0` | `∅` | `2326 / — / — / —` | `UNALIGNED?` |
| `comic-fiction-diagnosis/references/05-conflicts-and-anti-patterns.md+§4禁止输出的措辞清单` | `1 0 0 0` | `∅` | `436 / — / — / —` | `UNALIGNED?` |

---

## 题材 10 职业竞技（阈值 20%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 10 职业竞技

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK；本题材按 5.1 节 / §6.1 收紧到 20%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`competition-underdog-arc`、`profession-competition-craft`、`vocation-proof-and-price`

**规则单元数 336；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 336（100.0%）**
**flag 计数**：SOURCE_ONLY=48；UNALIGNED?=336

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `competition-underdog-arc/SKILL.md+0.一句话` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+1.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+触发` | `1 0 0 0` | `规检败` | `591 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+负触发不要用本skill` | `1 0 0 0` | `怎` | `550 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+2.p2来源事实闸门20261030roundp4final` | `1 0 0 0` | `例` | `1803 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+3.核心概念` | `1 0 0 0` | `规败` | `1290 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+4.任务路由` | `1 0 0 0` | `∅` | `787 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+5.最短执行路径a任务` | `1 0 0 0` | `∅` | `1710 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+6.输出物表` | `1 0 0 0` | `∅` | `1452 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `111 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `106 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `188 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `112 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `146 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `149 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `149 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `126 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `120 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `87 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `∅` | `115 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+7.规则索引仅已核实f` | `1 0 0 0` | `∅` | `2221 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `839 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+9.硬约束fictioncase` | `1 0 0 0` | `规反` | `829 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+10.本轮相对0.2.0的实质改动` | `1 0 0 0` | `∅` | `944 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/SKILL.md+11.0.3.1增量20261031台账补齐run` | `1 0 0 0` | `∅` | `1251 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `1241 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/examples/worked-example.md+b冲突输入导师是操纵者` | `1 0 0 0` | `∅` | `1527 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/examples/worked-example.md+c缺料输入只给"我想写一个电竞冠军"` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/examples/worked-example.md+d边界输入不参赛的私人工艺` | `1 0 0 0` | `∅` | `404 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/examples/worked-example.md+e新增输入稿里有一个"权威专家"角色` | `1 0 0 0` | `检` | `809 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/examples/worked-example.md+f新增输入越界之后要不要受罚` | `1 0 0 0` | `∅` | `457 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/01-arena-and-stakes.md+f已核实的文本现象` | `1 0 0 0` | `∅` | `931 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/01-arena-and-stakes.md+0.3.0新增本轮实读后解禁／首次入库` | `1 0 0 0` | `∅` | `1098 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/01-arena-and-stakes.md+h有条件的创作推导` | `1 0 0 0` | `∅` | `319 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/04-endings-ethics-and-counterexamples.md+反例与边界不得升格为规则` | `1 0 0 0` | `怎反` | `384 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/05-diagnosis-and-revision.md+面向草稿的体检表` | `1 0 0 0` | `∅` | `1412 / — / — / —` | `UNALIGNED?` |
| `competition-underdog-arc/references/05-diagnosis-and-revision.md+来源闸门` | `1 0 0 0` | `∅` | `327 / — / — / —` | `UNALIGNED?` |
| `PG717` | `1 0 0 0` | `∅` | `6039 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG154` | `1 0 0 0` | `∅` | `6039 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `competition-underdog-arc/references/source-index.md+其余来源的证据路径沿用前轮未改动` | `1 0 0 0` | `∅` | `1547 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `competition-underdog-arc/references/source-index.md+未完成的验收` | `1 0 0 0` | `检` | `479 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `P4` | `1 0 0 0` | `∅` | `1052 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+0.本skill是什么不是什么` | `1 0 0 0` | `规` | `1127 / — / — / —` | `UNALIGNED?` |
| `T1` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `T2` | `1 0 0 0` | `∅` | `95 / — / — / —` | `UNALIGNED?` |
| `T3` | `1 0 0 0` | `∅` | `102 / — / — / —` | `UNALIGNED?` |
| `T4` | `1 0 0 0` | `∅` | `81 / — / — / —` | `UNALIGNED?` |
| `T5` | `1 0 0 0` | `∅` | `95 / — / — / —` | `UNALIGNED?` |
| `T6` | `1 0 0 0` | `∅` | `92 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+1.触发条件何时用` | `1 0 0 0` | `∅` | `675 / — / — / —` | `UNALIGNED?` |
| `N1` | `1 0 0 0` | `∅` | `107 / — / — / —` | `UNALIGNED?` |
| `N2` | `1 0 0 0` | `∅` | `106 / — / — / —` | `UNALIGNED?` |
| `N3` | `1 0 0 0` | `∅` | `109 / — / — / —` | `UNALIGNED?` |
| `N4` | `1 0 0 0` | `∅` | `77 / — / — / —` | `UNALIGNED?` |
| `N5` | `1 0 0 0` | `∅` | `107 / — / — / —` | `UNALIGNED?` |
| `N6` | `1 0 0 0` | `∅` | `105 / — / — / —` | `UNALIGNED?` |
| `N7` | `1 0 0 0` | `∅` | `95 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+2.负触发何时不用用了会错` | `1 0 0 0` | `∅` | `856 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+3.输入要求` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+4.第一步三问定轴分支判断` | `1 0 0 0` | `例` | `1826 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+5.主工作流ab档七步` | `1 0 0 0` | `∅` | `705 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+6.十三条核心规则` | `1 0 0 0` | `∅` | `260 / — / — / —` | `UNALIGNED?` |
| `X7` | `1 0 0 0` | `规` | `817 / — / — / —` | `UNALIGNED?` |
| `X8` | `1 0 0 0` | `怎` | `875 / — / — / —` | `UNALIGNED?` |
| `X9` | `1 0 0 0` | `∅` | `1085 / — / — / —` | `UNALIGNED?` |
| `X10` | `1 0 0 0` | `反败` | `928 / — / — / —` | `UNALIGNED?` |
| `X11` | `1 0 0 0` | `例适` | `919 / — / — / —` | `UNALIGNED?` |
| `X12` | `1 0 0 0` | `规` | `1069 / — / — / —` | `UNALIGNED?` |
| `X13` | `1 0 0 0` | `规` | `1093 / — / — / —` | `UNALIGNED?` |
| `X14` | `1 0 0 0` | `∅` | `852 / — / — / —` | `UNALIGNED?` |
| `X15` | `1 0 0 0` | `∅` | `609 / — / — / —` | `UNALIGNED?` |
| `X16` | `1 0 0 0` | `例适` | `666 / — / — / —` | `UNALIGNED?` |
| `X17` | `1 0 0 0` | `∅` | `946 / — / — / —` | `UNALIGNED?` |
| `X18` | `1 0 0 0` | `例适` | `916 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+7.分支竞技轴vs职场轴` | `1 0 0 0` | `规` | `733 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+8.输出格式` | `1 0 0 0` | `∅` | `57 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+8.1职业账本8栏` | `1 0 0 0` | `∅` | `760 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+8.2场景卡8栏` | `1 0 0 0` | `∅` | `363 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+8.3审查表passrevisenotproven` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `X1` | `1 0 0 0` | `∅` | `112 / — / — / —` | `UNALIGNED?` |
| `X2` | `1 0 0 0` | `∅` | `111 / — / — / —` | `UNALIGNED?` |
| `X3` | `1 0 0 0` | `∅` | `100 / — / — / —` | `UNALIGNED?` |
| `X4` | `1 0 0 0` | `∅` | `105 / — / — / —` | `UNALIGNED?` |
| `X5` | `1 0 0 0` | `∅` | `94 / — / — / —` | `UNALIGNED?` |
| `X6` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+9.失败出口总表x1–x18` | `1 0 0 0` | `∅` | `1672 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+10.证据口径与口径限制` | `1 0 0 0` | `∅` | `1397 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+11.文件路由` | `1 0 0 0` | `∅` | `1396 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/SKILL.md+12.引文核验记录` | `1 0 0 0` | `∅` | `1675 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `190 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+1.pg4300主角拒绝“工作”职业小说仍成立` | `1 0 0 0` | `∅` | `508 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+2.pg19593职业浓度很低小说仍然成立` | `1 0 0 0` | `∅` | `519 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+3.pg12257不可能任务是被设计好的筛选不是公平考核` | `1 0 0 0` | `∅` | `537 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+4.pg3472卖“天赋测试函授课程”的行业本身是讽刺对象` | `1 0 0 0` | `∅` | `457 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+5.pg62409赛畜的“隐藏实力”不能迁移到人的职业竞争` | `1 0 0 0` | `∅` | `620 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+6.pg1693产量与安全分账是单本情节归纳` | `1 0 0 0` | `∅` | `600 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+7.pg3733职业爬升可以完全由外部资源驱动` | `1 0 0 0` | `∅` | `621 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+8.pg26485导师预留信件是情节装置不是训练系统` | `1 0 0 0` | `∅` | `533 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+9.pg1160把对手写成“兽”是时代偏见不是竞技写法` | `1 0 0 0` | `∅` | `557 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+10.pg4300反犹言论是人物台词不是作者结论` | `1 0 0 0` | `∅` | `498 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+11.pg11163讽刺小说的人物是“类型”不是圆整人物` | `1 0 0 0` | `∅` | `503 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+12.pg21223家长式“为你好”也是权力` | `1 0 0 0` | `∅` | `488 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/counterexamples.md+使用方式` | `1 0 0 0` | `规反` | `365 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例1报馆新人第一天门禁→等待→截稿` | `1 0 0 0` | `∅` | `1420 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例2一场拳赛的六段pg1160` | `1 0 0 0` | `∅` | `1487 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例3医学院的第一课pg3242` | `1 0 0 0` | `例败` | `1381 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例4房产经纪的逼单pg1156` | `1 0 0 0` | `∅` | `1239 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例5女演员的五年约pg62409` | `1 0 0 0` | `∅` | `1277 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例6背景档画家pg19593` | `1 0 0 0` | `∅` | `1130 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例7董事会控制权pg26485` | `1 0 0 0` | `∅` | `1089 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/examples.md+示例8失败后的行业回收pg11163pg1709` | `1 0 0 0` | `败` | `1056 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+本文件解决什么` | `1 0 0 0` | `∅` | `267 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+一三问定轴操作版` | `1 0 0 0` | `∅` | `511 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+逐档样本每档至少两个可对照的来源` | `1 0 0 0` | `规` | `1646 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+二门禁三层` | `1 0 0 0` | `∅` | `65 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `∅` | `748 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `规例` | `1327 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `973 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+三入场策略四型` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `适` | `850 / — / — / —` | `UNALIGNED?` |
| `E5` | `1 0 0 0` | `∅` | `288 / — / — / —` | `UNALIGNED?` |
| `E6` | `1 0 0 0` | `∅` | `727 / — / — / —` | `UNALIGNED?` |
| `E7` | `1 0 0 0` | `∅` | `501 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+四守门人利益表` | `1 0 0 0` | `∅` | `989 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+五边界案例pg16040kenny到底算哪一档` | `1 0 0 0` | `规` | `1021 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+六场景模板第一次进门` | `1 0 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/01-scope-and-entry.md+七本文件的边界` | `1 0 0 0` | `∅` | `668 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+本文件解决什么` | `1 0 0 0` | `∅` | `290 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+一t1训练三件套低风险真实任务+分级授权+外部考试节点` | `1 0 0 0` | `怎例适` | `1552 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+二t2证书与实操的错位证书是门禁实操是留任` | `1 0 0 0` | `反检` | `1281 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+三t3工作样本用"先交付后谈条件"累积声誉` | `1 0 0 0` | `例适` | `707 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+四t4刻意练习模仿拆解重复复盘` | `1 0 0 0` | `∅` | `1456 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+五t5反例三种"假训练"不可当范本` | `1 0 0 0` | `∅` | `95 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+t5.1"不可能任务"测试pg12257` | `1 0 0 0` | `∅` | `766 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+t5.2邮购"天赋测试"与函授课程pg3472` | `1 0 0 0` | `∅` | `444 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+t5.3"职业化"话语掩盖下的无训练pg1156` | `1 0 0 0` | `∅` | `426 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+六t6训练的代价必须记账` | `1 0 0 0` | `∅` | `922 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+七训练段场景模板` | `1 0 0 0` | `∅` | `493 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/02-training-and-competence.md+八边界` | `1 0 0 0` | `∅` | `785 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+本文件解决什么` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+一w1工序拆解5–9步每步一个可见物件` | `1 0 0 0` | `∅` | `1357 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+二w2把"机器"写成有节奏的物不是背景音` | `1 0 0 0` | `适` | `465 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+三w3生产链每个岗位都有独立利益` | `1 0 0 0` | `∅` | `1303 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+四w4产品拒收要写成"匹配失败"不是"坏人打压"` | `1 0 0 0` | `∅` | `650 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+五w5职业地理路线就是职业结构` | `1 0 0 0` | `∅` | `1104 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+六w6行话与物件少而准` | `1 0 0 0` | `∅` | `861 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+七w7广告媒体类职业把"创意"写成"位置+改稿+续约"` | `1 0 0 0` | `适` | `760 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+八w8协会行会把竞争变成可管理的小圈子` | `1 0 0 0` | `∅` | `965 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+九w9技术引入冲突是生计恐惧不是愚昧` | `1 0 0 0` | `∅` | `842 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+十工序段场景模板` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+十一失效信号` | `1 0 0 0` | `怎` | `376 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md+十二边界` | `1 0 0 0` | `∅` | `488 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+本文件解决什么` | `1 0 0 0` | `∅` | `288 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+一m1收入结构五件套底薪+计件佣金+报销+预付版税+隐性收入` | `1 0 0 0` | `∅` | `1777 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+二m2计件结算会直接制造"注水模板重复"` | `1 0 0 0` | `∅` | `691 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+三m3合同期限涨薪触发控制权` | `1 0 0 0` | `适` | `980 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+四m4控制权持股不等于控制董事会席位才是` | `1 0 0 0` | `∅` | `1046 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+五m5佣金场景信息差+场景控制+合同在手` | `1 0 0 0` | `怎例` | `1154 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+六m6现金流自由职业的真实感来自空档` | `1 0 0 0` | `∅` | `706 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+七m7晋升经验成果资格与守门人利益并列评估` | `1 0 0 0` | `∅` | `491 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+八钱段场景模板` | `1 0 0 0` | `∅` | `339 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+九失效信号` | `1 0 0 0` | `∅` | `345 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/04-pay-contract-and-career.md+十边界` | `1 0 0 0` | `∅` | `451 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+本文件解决什么` | `1 0 0 0` | `例` | `487 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+一c1六段节拍总表` | `1 0 0 0` | `∅` | `790 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+二c2赛前先给"最后一次"或"倒计时"` | `1 0 0 0` | `∅` | `262 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+三c3用赔率排名解释"强弱"与爆冷可能` | `1 0 0 0` | `∅` | `645 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+四c4竞技战术的读者可理解性可预告也可赛后解释` | `1 0 0 0` | `∅` | `872 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+五c5仪式程序规则要被"念出来"` | `1 0 0 0` | `∅` | `608 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+六c6规则边缘人物"明知在规则内"地使用` | `1 0 0 0` | `规` | `620 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+七c7意外前文必须埋过身体场地风险` | `1 0 0 0` | `∅` | `392 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+八c8赛后程序医生救护车记者更衣室` | `1 0 0 0` | `∅` | `347 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+九c9外行pov先误读再由规则纠正` | `1 0 0 0` | `规` | `342 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十c10考核通过率把"名额"写出来` | `1 0 0 0` | `规败` | `578 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十一c11竞技伦理胜利不能变成私刑` | `1 0 0 0` | `规例` | `602 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十二c12竞技作为职场关系的隐喻场` | `1 0 0 0` | `败` | `649 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十三比赛段场景模板` | `1 0 0 0` | `∅` | `408 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十四失效信号` | `1 0 0 0` | `规` | `543 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/05-competition-and-ranking.md+十五边界` | `1 0 0 0` | `适` | `583 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+本文件解决什么` | `1 0 0 0` | `∅` | `248 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+一e1先给行业一个"病名"` | `1 0 0 0` | `∅` | `759 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+二e2获利妥协退出或推动改革选项与其代价` | `1 0 0 0` | `∅` | `903 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+三e3行业惯例比单个坏人更有力` | `1 0 0 0` | `∅` | `906 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+四e4代价要能被看见被记账` | `1 0 0 0` | `∅` | `1208 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+五e5制度批判先让角色在规则内做选择再由叙述者点规则` | `1 0 0 0` | `∅` | `1296 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+六e6权威的边界一次越权善举足以暴露权力` | `1 0 0 0` | `例` | `593 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+七e7可结算个人亦可有条件地改变制度` | `1 0 0 0` | `败` | `1188 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+八e8成功线也要结算别让成功者白拿` | `1 0 0 0` | `败` | `622 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+九e9时代偏见登记不采纳` | `1 0 0 0` | `∅` | `874 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+十伦理段场景模板` | `1 0 0 0` | `∅` | `391 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+十一失效信号` | `1 0 0 0` | `∅` | `325 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md+十二边界` | `1 0 0 0` | `∅` | `620 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+本文件解决什么` | `1 0 0 0` | `∅` | `247 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+填法示例a出版业据pg1709` | `1 0 0 0` | `∅` | `612 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+填法示例b医疗据pg3242` | `1 0 0 0` | `∅` | `726 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+填法示例报馆第一天据pg9300pg13731` | `1 0 0 0` | `∅` | `657 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+填法示例新闻业据pg9300pg3472pg3669` | `1 0 0 0` | `∅` | `430 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+填法示例影视业据pg3472` | `1 0 0 0` | `∅` | `470 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+五审查表输出格式第3项` | `1 0 0 0` | `∅` | `975 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/07-templates.md+六边界` | `1 0 0 0` | `检` | `331 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/08-diagnosis-and-revision.md+用法` | `1 0 0 0` | `∅` | `329 / — / — / —` | `UNALIGNED?` |
| `F1` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `F2` | `1 0 0 0` | `∅` | `87 / — / — / —` | `UNALIGNED?` |
| `F3` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `F4` | `1 0 0 0` | `∅` | `74 / — / — / —` | `UNALIGNED?` |
| `F5` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `F6` | `1 0 0 0` | `∅` | `101 / — / — / —` | `UNALIGNED?` |
| `F7` | `1 0 0 0` | `∅` | `104 / — / — / —` | `UNALIGNED?` |
| `F8` | `1 0 0 0` | `∅` | `93 / — / — / —` | `UNALIGNED?` |
| `F9` | `1 0 0 0` | `∅` | `107 / — / — / —` | `UNALIGNED?` |
| `F10` | `1 0 0 0` | `∅` | `98 / — / — / —` | `UNALIGNED?` |
| `F11` | `1 0 0 0` | `∅` | `92 / — / — / —` | `UNALIGNED?` |
| `F12` | `1 0 0 0` | `∅` | `121 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/08-diagnosis-and-revision.md+分诊表` | `1 0 0 0` | `∅` | `1241 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/08-diagnosis-and-revision.md+改稿顺序建议` | `1 0 0 0` | `∅` | `382 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/08-diagnosis-and-revision.md+边界` | `1 0 0 0` | `败` | `381 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+本文件解决什么` | `1 0 0 0` | `∅` | `376 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§0来源族与去重重要23本≠23条独立证据` | `1 0 0 0` | `∅` | `990 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg23703theparthenonbywayofpapendrecht19` | `1 0 0 0` | `规` | `1485 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg12257pg12257thegogetter1921商业寓言` | `1 0 0 0` | `规` | `1046 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg1160pg1160thegame1905拳击` | `1 0 0 0` | `∅` | `1189 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg12677pg12677personalityplus1914广告业女装业` | `1 0 0 0` | `∅` | `1436 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg19593pg19593thethirdviolet1897画家` | `1 0 0 0` | `∅` | `890 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg19272pg19272theearlybird1910商业爱情` | `1 0 0 0` | `检` | `1530 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg3733pg3733belami1885新闻业政商` | `1 0 0 0` | `∅` | `1313 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg9300pg9300jenniebaxterjournalist1899报` | `1 0 0 0` | `规` | `1254 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg11163pg11163potterism1920报业讽刺` | `1 0 0 0` | `规` | `1305 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg21223pg21223thecarbonels1880s乡绅治理教区` | `1 0 0 0` | `规例` | `1700 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg9195pg9195theslaveofthelamp1892报业+政治惊` | `1 0 0 0` | `规` | `1871 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg13731pg13731romanceisland1906报业+冒险` | `1 0 0 0` | `规例` | `1543 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg16040pg16040kenny1917画家+记者` | `1 0 0 0` | `规例` | `1503 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg26485pg26485themakingofbobbyburnit190` | `1 0 0 0` | `败` | `1229 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg3242pg3242thedoctor1906医疗` | `1 0 0 0` | `∅` | `1815 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg3472pg3472mertonofthemovies1922好莱坞` | `1 0 0 0` | `规` | `1623 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg62409pg62409thegirlfromhollywood1923好` | `1 0 0 0` | `规` | `1432 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg1156pg1156babbitt1922房地产` | `1 0 0 0` | `规` | `1488 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg1693pg1693dangerousdays1919战时兵工` | `1 0 0 0` | `规` | `1371 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg3178pg3178thegildedage1873土地投机铁路国会` | `1 0 0 0` | `规检适` | `1501 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg3669pg3669awomanhater1877演艺经纪医学准入公共卫生` | `1 0 0 0` | `∅` | `1831 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg1709pg1709newgrubstreet1891文学生产` | `1 0 0 0` | `规败` | `1576 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§pg4300pg4300ulysses1922城市职业全景` | `1 0 0 0` | `怎` | `1564 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+§未决与孤儿项诚实登记` | `1 0 0 0` | `例` | `424 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/09-per-source-playbook.md+核验说明` | `1 0 0 0` | `∅` | `198 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `209 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B01` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B-06` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/rework-decision.md+最小有效输入与责任边界` | `1 0 0 0` | `∅` | `369 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/rework-decision.md+先定轴再选择场景合同` | `1 0 0 0` | `∅` | `969 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/rework-decision.md+不同能力执行器` | `1 0 0 0` | `∅` | `1592 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/references/rework-decision.md+推导交付失败出口` | `1 0 0 0` | `∅` | `547 / — / — / —` | `UNALIGNED?` |
| `profession-competition-craft/sources-index.md+使用说明` | `1 0 0 0` | `例` | `671 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/sources-index.md+总表` | `1 0 0 0` | `∅` | `3864 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/sources-index.md+证据分布` | `1 0 0 0` | `∅` | `887 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/sources-index.md+单源清单引用时必须标` | `1 0 0 0` | `∅` | `1118 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `profession-competition-craft/sources-index.md+版本与引用注意` | `1 0 0 0` | `∅` | `493 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+0.一句话` | `1 0 0 0` | `∅` | `258 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+1.本skill的来源与边界` | `1 0 0 0` | `∅` | `1160 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+2.触发条件命中任一即用` | `1 0 0 0` | `∅` | `696 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+3.负触发命中任一跳过主流程直接走出口` | `1 0 0 0` | `∅` | `708 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+5.定轴先选ple再判断职业引擎强度` | `1 0 0 0` | `∅` | `744 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+6.执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+6.1p轴写出"兑现机器"不要只写能力门` | `1 0 0 0` | `∅` | `1838 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+6.2l轴写出代价由谁付` | `1 0 0 0` | `∅` | `1422 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+6.3e轴三种收场不是两种` | `1 0 0 0` | `∅` | `1276 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+7.输出合同每次交付必须齐备` | `1 0 0 0` | `∅` | `1089 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+8.失败出口必须真的输出不许硬凑` | `1 0 0 0` | `∅` | `723 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+9.按需加载的参考文件` | `1 0 0 0` | `∅` | `1213 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/SKILL.md+10.与其他同父类别skill的关系不要混用也不要互相推翻` | `1 0 0 0` | `∅` | `519 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `1274 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+1.反例满口术语零交付pg2460是标本用法` | `1 0 0 0` | `∅` | `882 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+2.反例名声来自你宣称鄙视的东西pg11584` | `1 0 0 0` | `∅` | `385 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+3.反例制度是可以被改成功的pg1350` | `1 0 0 0` | `规适` | `450 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+4.反例改革实验可以自我推翻pg7502` | `1 0 0 0` | `败` | `321 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+5.反例不可量化的劣势同样成立pg3364` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+6.边界不要把单本机制写成通则` | `1 0 0 0` | `∅` | `792 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/counterexamples.md+7.边界本skill明确不覆盖` | `1 0 0 0` | `规败` | `466 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/examples.md+样例a｜p轴主角"明明很强却没人理"` | `1 0 0 0` | `∅` | `1558 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/examples.md+样例b｜l轴职业与关系二选一` | `1 0 0 0` | `∅` | `1316 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/examples.md+样例c｜e轴失明伤残之后` | `1 0 0 0` | `∅` | `1410 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/examples.md+样例d｜失败出口只给了职业标签` | `1 0 0 0` | `∅` | `967 / — / — / —` | `UNALIGNED?` |
| `PG351` | `1 0 0 0` | `反` | `5653 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG401` | `1 0 0 0` | `反` | `5653 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `R17` | `1 0 0 0` | `∅` | `180 / — / — / —` | `UNALIGNED?` |
| `R18` | `1 0 0 0` | `∅` | `240 / — / — / —` | `UNALIGNED?` |
| `R19` | `1 0 0 0` | `∅` | `132 / — / — / —` | `UNALIGNED?` |
| `R20` | `1 0 0 0` | `∅` | `148 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/02-rulings.md+必读的两条"不许照抄旧规则"` | `1 0 0 0` | `∅` | `369 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/03-proof-machine.md+主张` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/03-proof-machine.md+f支撑逐条可回源` | `1 0 0 0` | `∅` | `1878 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/03-proof-machine.md+裁决者类型决定自证方式不要选错` | `1 0 0 0` | `∅` | `800 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/03-proof-machine.md+p动作清单` | `1 0 0 0` | `∅` | `448 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/03-proof-machine.md+保留的冲突不统一` | `1 0 0 0` | `∅` | `674 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md+主张` | `1 0 0 0` | `∅` | `200 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md+f支撑` | `1 0 0 0` | `∅` | `1719 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md+三条硬性写法p` | `1 0 0 0` | `∅` | `752 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md+时代偏见的写法` | `1 0 0 0` | `∅` | `603 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md+保留的冲突不统一` | `1 0 0 0` | `∅` | `566 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+主张` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+三种收场附f` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+a.继续做带伤带败继续` | `1 0 0 0` | `∅` | `473 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+b.改换执行方式职业还在怎么做变了` | `1 0 0 0` | `∅` | `426 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+c.退出或崩解` | `1 0 0 0` | `反` | `360 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+痛点必须落在身份不是收入` | `1 0 0 0` | `∅` | `482 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+训练与失能都要写"难堪"` | `1 0 0 0` | `∅` | `472 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+"赢"必须写明失去什么` | `1 0 0 0` | `∅` | `293 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/05-disability-and-exit.md+一个常被写坏的点失败的责任归属` | `1 0 0 0` | `例` | `436 / — / — / —` | `UNALIGNED?` |
| `P1` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `P2` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `203 / — / — / —` | `UNALIGNED?` |
| `P5` | `1 0 0 0` | `∅` | `168 / — / — / —` | `UNALIGNED?` |
| `P6` | `1 0 0 0` | `∅` | `173 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md+p轴症状` | `1 0 0 0` | `∅` | `1131 / — / — / —` | `UNALIGNED?` |
| `L1` | `1 0 0 0` | `∅` | `139 / — / — / —` | `UNALIGNED?` |
| `L2` | `1 0 0 0` | `∅` | `154 / — / — / —` | `UNALIGNED?` |
| `L3` | `1 0 0 0` | `∅` | `130 / — / — / —` | `UNALIGNED?` |
| `L4` | `1 0 0 0` | `∅` | `176 / — / — / —` | `UNALIGNED?` |
| `L5` | `1 0 0 0` | `∅` | `166 / — / — / —` | `UNALIGNED?` |
| `L6` | `1 0 0 0` | `∅` | `158 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md+l轴症状` | `1 0 0 0` | `∅` | `1000 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md+e轴症状` | `1 0 0 0` | `∅` | `980 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md+改稿输出模板复制使用` | `1 0 0 0` | `∅` | `712 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md+自检三问改完必答` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `vocation-proof-and-price/references/07-per-source-playbook.md+艺术表演6本` | `1 0 0 0` | `∅` | `998 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/references/07-per-source-playbook.md+商业金融劳动5本` | `1 0 0 0` | `∅` | `963 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/references/08-provenance-and-compat.md+本skill的沿革` | `1 0 0 0` | `∅` | `603 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/references/08-provenance-and-compat.md+与同父类别另两份skill的关系` | `1 0 0 0` | `∅` | `842 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/references/08-provenance-and-compat.md+元数据必须随skill一起迁移不得丢弃` | `1 0 0 0` | `∅` | `527 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/references/08-provenance-and-compat.md+未证明已知缺口如实登记不得随版本流失` | `1 0 0 0` | `∅` | `989 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B03` | `1 0 0 0` | `∅` | `3502 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `vocation-proof-and-price/sources-index.md+使用限制` | `1 0 0 0` | `规` | `533 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 11 身份复仇权谋（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 11 身份复仇权谋

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`identity-revenge-intrigue-b06`、`identity-revenge-powercraft-fiction`、`intrigue-revenge-craft-b04`、`revenge-identity-craft`、`revenge-intrigue-architecture`、`revenge-intrigue-craft`

**规则单元数 610；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 610（100.0%）**
**flag 计数**：SOURCE_ONLY=29；UNALIGNED?=610

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `identity-revenge-intrigue-b06/SKILL.md+任务入口拒绝条件与文件路由` | `1 0 0 0` | `∅` | `1175 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/SKILL.md+输入权威与预检` | `1 0 0 0` | `败` | `759 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/SKILL.md+正常工作流计划创作修订` | `1 0 0 0` | `∅` | `1588 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/SKILL.md+缺料反证伦理及冲突处理` | `1 0 0 0` | `∅` | `679 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/SKILL.md+输出合同` | `1 0 0 0` | `∅` | `452 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/SKILL.md+材料许可与验证边界` | `1 0 0 0` | `∅` | `479 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/alliances-power.md+rb0605｜盟友不是免费的能力条` | `1 0 0 0` | `例反` | `917 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/alliances-power.md+rb0606｜制度是限制不是万能背景` | `1 0 0 0` | `规反` | `465 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/alliances-power.md+rb0610｜同一弱者可被多个组织排除新补证` | `1 0 0 0` | `反` | `681 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/alliances-power.md+rb0611｜角色的隐蔽动机经第三者转为控制资源新补证` | `1 0 0 0` | `反` | `612 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/diagnosis-and-revision.md+分类型定位` | `1 0 0 0` | `∅` | `1016 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/diagnosis-and-revision.md+输出格式` | `1 0 0 0` | `∅` | `366 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/diagnosis-and-revision.md+rb0609｜按原著顺序核对错位的因果链` | `1 0 0 0` | `反` | `623 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/identity-evidence.md+rb0601｜把“身份”拆成主张证明与被谁承认` | `1 0 0 0` | `反` | `810 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/identity-evidence.md+rb0602｜线索“可见”与读者公平` | `1 0 0 0` | `例反适` | `609 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/identity-evidence.md+拒绝与缺口出口` | `1 0 0 0` | `∅` | `247 / — / — / —` | `UNALIGNED?` |
| `PG786` | `1 0 0 0` | `∅` | `366 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/motives-and-costs.md+rb0603｜动机不是行动许可` | `1 0 0 0` | `反适` | `801 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/motives-and-costs.md+rb0604｜每个升级有因果而非固定次数` | `1 0 0 0` | `∅` | `639 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/revelation-and-repair.md+rb0607｜真假身份在不同时间视角中有不同“可见性”` | `1 0 0 0` | `∅` | `723 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/revelation-and-repair.md+rb0608｜结局按因果兑现不按惩罚模板` | `1 0 0 0` | `反` | `448 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/revelation-and-repair.md+伦理与版权` | `1 0 0 0` | `∅` | `260 / — / — / —` | `UNALIGNED?` |
| `PG33` | `1 0 0 0` | `∅` | `5604 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG917` | `1 0 0 0` | `∅` | `5604 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG600` | `1 0 0 0` | `∅` | `5604 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `identity-revenge-intrigue-b06/references/source-index.md+新增直接f的来源限制` | `1 0 0 0` | `∅` | `673 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `identity-revenge-intrigue-b06/templates/identity-stakes-map.md+情节分支` | `1 0 0 0` | `∅` | `442 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+1.触发与负触发` | `1 0 0 0` | `怎败` | `828 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+2.输入契约` | `1 0 0 0` | `怎` | `718 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `922 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+4.执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+流程d｜诊断有草稿设定阶段=草稿改稿` | `1 0 0 0` | `∅` | `2023 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+流程p｜设计阶段=构思` | `1 0 0 0` | `∅` | `589 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+流程r｜修订阶段=改稿收尾` | `1 0 0 0` | `∅` | `368 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+难例designexample非真实用户任务` | `1 0 0 0` | `∅` | `817 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+5.失败出口` | `1 0 0 0` | `规检` | `978 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/SKILL.md+6.输出合同` | `1 0 0 0` | `例` | `864 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规怎` | `1102 / — / — / —` | `UNALIGNED?` |
| `X-4` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `X-1` | `1 0 0 0` | `∅` | `187 / — / — / —` | `UNALIGNED?` |
| `X-2` | `1 0 0 0` | `适` | `667 / — / — / —` | `UNALIGNED?` |
| `X-3` | `1 0 0 0` | `适` | `548 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/references/conflict-ledger.md+附本批明确"未证明"的一项` | `1 0 0 0` | `∅` | `338 / — / — / —` | `UNALIGNED?` |
| `ID-4` | `1 0 0 0` | `∅` | `141 / — / — / —` | `UNALIGNED?` |
| `ID-1` | `1 0 0 0` | `∅` | `141 / — / — / —` | `UNALIGNED?` |
| `ID-2` | `1 0 0 0` | `∅` | `727 / — / — / —` | `UNALIGNED?` |
| `ID-3` | `1 0 0 0` | `∅` | `543 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/references/id-disguise-engine.md+本轴禁写的三条` | `1 0 0 0` | `∅` | `382 / — / — / —` | `UNALIGNED?` |
| `PM-1` | `1 0 0 0` | `检` | `191 / — / — / —` | `UNALIGNED?` |
| `PM-5` | `1 0 0 0` | `检` | `191 / — / — / —` | `UNALIGNED?` |
| `PM-2` | `1 0 0 0` | `∅` | `531 / — / — / —` | `UNALIGNED?` |
| `PM-3` | `1 0 0 0` | `∅` | `767 / — / — / —` | `UNALIGNED?` |
| `PM-4` | `1 0 0 0` | `∅` | `754 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/references/power-machine.md+本文件禁写的三条` | `1 0 0 0` | `∅` | `384 / — / — / —` | `UNALIGNED?` |
| `RC-2` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `RC-3` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `RC-1` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `identity-revenge-powercraft-fiction/references/revenge-cost-ledger.md+与"法律制度救济"的边界` | `1 0 0 0` | `∅` | `431 / — / — / —` | `UNALIGNED?` |
| `PG95` | `1 0 0 0` | `∅` | `5380 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG433` | `1 0 0 0` | `∅` | `5380 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG965` | `1 0 0 0` | `∅` | `5380 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `identity-revenge-powercraft-fiction/references/source-index.md+隔离回读检查本轮自测` | `1 0 0 0` | `∅` | `325 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `RM-01` | `1 0 0 0` | `∅` | `291 / — / — / —` | `UNALIGNED?` |
| `RM-11` | `1 0 0 0` | `∅` | `291 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+触发` | `1 0 0 0` | `∅` | `514 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+负触发不做并说明为什么` | `1 0 0 0` | `例适` | `603 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+需要哪些输入` | `1 0 0 0` | `规例` | `474 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+执行流程` | `1 0 0 0` | `∅` | `1357 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+输出合同` | `1 0 0 0` | `∅` | `674 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+失败出口` | `1 0 0 0` | `规` | `719 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/SKILL.md+已知未证明项不得写成结论` | `1 0 0 0` | `检` | `370 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规怎例反适` | `1538 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/examples/worked-cases.md+1.正常双社会结构中的角色行动` | `1 0 0 0` | `∅` | `568 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/examples/worked-cases.md+2.缺料只有题材词` | `1 0 0 0` | `检` | `331 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/examples/worked-cases.md+3.冲突设定中唯一继承人却突然双王登基` | `1 0 0 0` | `∅` | `394 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/examples/worked-cases.md+4.边界要求复刻蓄奴辩护` | `1 0 0 0` | `∅` | `279 / — / — / —` | `UNALIGNED?` |
| `RM-03` | `1 0 0 0` | `检` | `775 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md+身份保留不可改` | `1 0 0 0` | `∅` | `641 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md+基线产物保留不可覆盖` | `1 0 0 0` | `∅` | `1164 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md+保留的能力项本轮未删除` | `1 0 0 0` | `例适败` | `398 / — / — / —` | `UNALIGNED?` |
| `ID-11` | `1 0 0 0` | `规` | `423 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md+覆盖与许可` | `1 0 0 0` | `∅` | `661 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md+红线` | `1 0 0 0` | `∅` | `218 / — / — / —` | `UNALIGNED?` |
| `ADJ-01` | `1 0 0 0` | `∅` | `690 / — / — / —` | `UNALIGNED?` |
| `RM-02` | `1 0 0 0` | `反` | `855 / — / — / —` | `UNALIGNED?` |
| `RM-04` | `1 0 0 0` | `反适` | `2168 / — / — / —` | `UNALIGNED?` |
| `RM-05` | `1 0 0 0` | `反` | `999 / — / — / —` | `UNALIGNED?` |
| `RM-06` | `1 0 0 0` | `反` | `933 / — / — / —` | `UNALIGNED?` |
| `RM-07` | `1 0 0 0` | `反` | `860 / — / — / —` | `UNALIGNED?` |
| `RM-08` | `1 0 0 0` | `反` | `603 / — / — / —` | `UNALIGNED?` |
| `RM-09` | `1 0 0 0` | `反` | `2929 / — / — / —` | `UNALIGNED?` |
| `RM-10` | `1 0 0 0` | `反` | `961 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/rules.md+被拒绝的概括reject不得写入任何输出` | `1 0 0 0` | `规` | `516 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+适用` | `1 0 0 0` | `∅` | `279 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+不适用` | `1 0 0 0` | `∅` | `194 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+c16蓄奴制辩护vs反奴隶制作品` | `1 0 0 0` | `反` | `1040 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+帝国叙事工业揭露与反战立场` | `1 0 0 0` | `例` | `839 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+保留的冲突不得伪造共识` | `1 0 0 0` | `∅` | `1619 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+规则冲突处理` | `1 0 0 0` | `∅` | `315 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md+证据缺口` | `1 0 0 0` | `∅` | `453 / — / — / —` | `UNALIGNED?` |
| `PG693` | `1 0 0 0` | `∅` | `3680 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG140` | `1 0 0 0` | `∅` | `3680 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG203` | `1 0 0 0` | `∅` | `3680 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/source-index.md+核心规则的原著片段位置` | `1 0 0 0` | `∅` | `1632 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/source-index.md+来源属性权利p2与误用` | `1 0 0 0` | `∅` | `516 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `intrigue-revenge-craft-b04/references/techniques.md+诊断失败与修订` | `1 0 0 0` | `∅` | `211 / — / — / —` | `UNALIGNED?` |
| `ID-01` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `ID-02` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `ID-03` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `ID-04` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `ID-05` | `1 0 0 0` | `∅` | `85 / — / — / —` | `UNALIGNED?` |
| `ID-06` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `ID-07` | `1 0 0 0` | `∅` | `85 / — / — / —` | `UNALIGNED?` |
| `ID-08` | `1 0 0 0` | `∅` | `81 / — / — / —` | `UNALIGNED?` |
| `ID-09` | `1 0 0 0` | `∅` | `102 / — / — / —` | `UNALIGNED?` |
| `ID-10` | `1 0 0 0` | `∅` | `90 / — / — / —` | `UNALIGNED?` |
| `intrigue-revenge-craft-b04/templates/intrigue-diagnosis.md+判定与回归` | `1 0 0 0` | `适` | `1693 / — / — / —` | `UNALIGNED?` |
| `B01` | `1 0 0 0` | `∅` | `678 / — / — / —` | `UNALIGNED?` |
| `B-07` | `1 0 0 0` | `∅` | `678 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+1.触发与负触发` | `1 0 0 0` | `∅` | `930 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+2.输入与前置检查先问清这9项缺哪项就标notobserved` | `1 0 0 0` | `∅` | `1072 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1573 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+4.执行步骤五步不要跳` | `1 0 0 0` | `∅` | `1091 / — / — / —` | `UNALIGNED?` |
| `V1` | `1 0 0 0` | `∅` | `144 / — / — / —` | `UNALIGNED?` |
| `V2` | `1 0 0 0` | `∅` | `98 / — / — / —` | `UNALIGNED?` |
| `V3` | `1 0 0 0` | `∅` | `162 / — / — / —` | `UNALIGNED?` |
| `V4` | `1 0 0 0` | `∅` | `166 / — / — / —` | `UNALIGNED?` |
| `V5` | `1 0 0 0` | `∅` | `139 / — / — / —` | `UNALIGNED?` |
| `V6` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `V7` | `1 0 0 0` | `∅` | `118 / — / — / —` | `UNALIGNED?` |
| `V8` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `V9` | `1 0 0 0` | `∅` | `134 / — / — / —` | `UNALIGNED?` |
| `V10` | `1 0 0 0` | `∅` | `137 / — / — / —` | `UNALIGNED?` |
| `V11` | `1 0 0 0` | `∅` | `165 / — / — / —` | `UNALIGNED?` |
| `V12` | `1 0 0 0` | `∅` | `153 / — / — / —` | `UNALIGNED?` |
| `V13` | `1 0 0 0` | `∅` | `127 / — / — / —` | `UNALIGNED?` |
| `V14` | `1 0 0 0` | `∅` | `161 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+5.规则总表v1–v14全部为条件装置不是类型定律` | `1 0 0 0` | `∅` | `2338 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `684 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/SKILL.md+7.失败出口与停止条件` | `1 0 0 0` | `∅` | `671 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `879 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+1.正常身份证据与复仇结局` | `1 0 0 0` | `反检` | `618 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+2.缺料没给稿件却要逐章诊断` | `1 0 0 0` | `∅` | `240 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+3.冲突锁定设定与新提案相撞` | `1 0 0 0` | `适` | `311 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+4.越界要求用血统面相当设定依据` | `1 0 0 0` | `∅` | `365 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+5.未证明要求"保证读者爽"` | `1 0 0 0` | `∅` | `308 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/examples/worked-cases.md+6.机构权谋线改革话语是真是假` | `1 0 0 0` | `∅` | `527 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+1.v1公共误判与认定权revise` | `1 0 0 0` | `反` | `1594 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+2.v2格言题辞作为对照声部keep缩为可选项` | `1 0 0 0` | `例适` | `786 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+3.v3证据埋设与回收revise加"知情差"与"机关会失败"` | `1 0 0 0` | `反` | `1499 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+4.v4表演身份与认定权之差revise四类伪装介质+加固禁忌` | `1 0 0 0` | `例适` | `1921 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+5.v9双重身份换位新增来源pg2759` | `1 0 0 0` | `反` | `1079 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/01-identity-engines.md+6.v10改名重置与不可控证人新增来源pg2171` | `1 0 0 0` | `反` | `1300 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/02-revenge-closure.md+1.v5复仇的边界分开回答"由谁执行"与"何时终止"revise` | `1 0 0 0` | `反适` | `1636 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/02-revenge-closure.md+2.v6收束方式光谱keep扩为五种以上不设标准答案` | `1 0 0 0` | `例适` | `1571 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/02-revenge-closure.md+3.v7机关复盘与交割keep加"哪一步差点失败"` | `1 0 0 0` | `反败` | `1064 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/02-revenge-closure.md+4.v8复仇收益与去向revise先核归属再谈伦理` | `1 0 0 0` | `反` | `1364 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md+1.v11代际罪责与继承物新增` | `1 0 0 0` | `反` | `1920 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md+2.v12机构权谋公开理由实际受益者成本承担者分离新增` | `1 0 0 0` | `反` | `1551 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md+3.v13归属型身份新增` | `1 0 0 0` | `∅` | `1096 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md+4.v14禁用清单硬边界` | `1 0 0 0` | `∅` | `1027 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md+5.形态观察与迁移限制` | `1 0 0 0` | `∅` | `1410 / — / — / —` | `UNALIGNED?` |
| `PG102` | `1 0 0 0` | `∅` | `2839 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG77` | `1 0 0 0` | `∅` | `2839 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-identity-craft/references/04-source-index.md+2.证据层级口径本轮定义不再使用"分区间扫描"旧口径` | `1 0 0 0` | `规` | `632 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-identity-craft/references/04-source-index.md+3.遗留问题如实登记不掩盖` | `1 0 0 0` | `∅` | `891 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-identity-craft/references/04-source-index.md+4.文献权限与引用约定` | `1 0 0 0` | `∅` | `591 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-identity-craft/references/05-decision-guide.md+通用前置每条规则前都要过` | `1 0 0 0` | `∅` | `292 / — / — / —` | `UNALIGNED?` |
| `L296` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L292` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L295` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L294` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L290` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L293` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L291` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L297` | `1 0 0 0` | `∅` | `387 / — / — / —` | `UNALIGNED?` |
| `L306` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `L307` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `L308` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `L309` | `1 0 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `L334` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L333` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L354` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L335` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L360` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L346` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L357` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L352` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L349` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L340` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L345` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L353` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L361` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L359` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L347` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L356` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L344` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L362` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L355` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L358` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L338` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L348` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L336` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L343` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L351` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L332` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L337` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L350` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L341` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L342` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L339` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `L930` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L931` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L929` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L932` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L936` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L934` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L933` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L935` | `1 0 0 0` | `检` | `515 / — / — / —` | `UNALIGNED?` |
| `L778` | `1 0 0 0` | `∅` | `360 / — / — / —` | `UNALIGNED?` |
| `L779` | `1 0 0 0` | `∅` | `360 / — / — / —` | `UNALIGNED?` |
| `L780` | `1 0 0 0` | `∅` | `360 / — / — / —` | `UNALIGNED?` |
| `L395` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L766` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L763` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L767` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L768` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L750` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L394` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L742` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L745` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L752` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L776` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L764` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L758` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L761` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L759` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L769` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L740` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L748` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L751` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L772` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L399` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L773` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L755` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L743` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L771` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L397` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L757` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L777` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L775` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L744` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L760` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L739` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L753` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L756` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L754` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L774` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L741` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L400` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L770` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L398` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L749` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L396` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L747` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L746` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L765` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L762` | `1 0 0 0` | `例` | `389 / — / — / —` | `UNALIGNED?` |
| `L687` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L715` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L647` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L663` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L707` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L659` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L640` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L662` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L725` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L706` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L638` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L701` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L682` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L644` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L649` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L680` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L708` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L261` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L660` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L684` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L711` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L697` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L670` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L735` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L696` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L692` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L643` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L675` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L690` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L642` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L702` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L730` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L242` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L664` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L688` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L259` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L683` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L655` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L712` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L694` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L258` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L645` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L737` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L674` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L713` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L681` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L703` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L243` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L685` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L726` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L678` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L650` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L257` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L651` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L691` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L672` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L704` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L731` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L689` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L260` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L673` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L641` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L657` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L732` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L653` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L667` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L718` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L733` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L665` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L724` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L244` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L734` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L723` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L698` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L668` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L646` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L738` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L705` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L729` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L720` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L714` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L676` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L717` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L727` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L699` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L658` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L661` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L656` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L686` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L728` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L710` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L671` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L652` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L709` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L648` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L719` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L669` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L654` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L722` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L666` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L700` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L716` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L721` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L679` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L736` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L693` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L695` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L677` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L639` | `1 0 0 0` | `∅` | `464 / — / — / —` | `UNALIGNED?` |
| `L446` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L438` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L330` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L366` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L371` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L377` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L313` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L421` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L448` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L367` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L392` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L412` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L436` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L311` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L369` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L322` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L384` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L403` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L449` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L324` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L329` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L391` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L435` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L379` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L363` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L444` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L405` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L390` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L389` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L401` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L430` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L381` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L382` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L442` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L425` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L450` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L417` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L428` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L439` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L409` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L414` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L440` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L420` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L427` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L319` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L419` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L325` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L411` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L327` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L385` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L447` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L434` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L373` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L323` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L441` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L387` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L422` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L437` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L418` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L315` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L407` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L423` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L413` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L314` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L445` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L416` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L406` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L378` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L433` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L431` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L310` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L408` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L372` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L426` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L410` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L318` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L443` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L370` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L328` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L374` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L317` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L321` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L320` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L432` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L386` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L368` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L376` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L402` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L429` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L404` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L364` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L388` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L312` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L326` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L375` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L383` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L365` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L380` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L424` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L415` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L316` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L331` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `L393` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/05-decision-guide.md+输出前自检8条` | `1 0 0 0` | `∅` | `550 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/legacy-metadata.md+1.基线与继承链全部保留` | `1 0 0 0` | `∅` | `909 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/legacy-metadata.md+2.已被reject的旧断言不得回退` | `1 0 0 0` | `∅` | `532 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/legacy-metadata.md+3.本轮roundp4final20261030对wave4版的实际改动` | `1 0 0 0` | `∅` | `1247 / — / — / —` | `UNALIGNED?` |
| `revenge-identity-craft/references/legacy-metadata.md+4.版本与来源数迁移后仍完整` | `1 0 0 0` | `∅` | `626 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+0.这是什么不是什么` | `1 0 0 0` | `∅` | `456 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+1.证据底座来源不等于规则认证` | `1 0 0 0` | `规` | `1997 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+触发` | `1 0 0 0` | `适` | `673 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+负触发不要用` | `1 0 0 0` | `例适` | `485 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1731 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+4.执行路径先条件判别后选资料` | `1 0 0 0` | `适` | `1966 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `1578 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `1578 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `1578 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `140 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `125 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `136 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `127 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `152 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `131 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `117 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `118 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `127 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+6.核心规则索引` | `1 0 0 0` | `∅` | `2112 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+7.失败出口` | `1 0 0 0` | `规` | `1196 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+8.边界与退出` | `1 0 0 0` | `检` | `1842 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/SKILL.md+元数据与授权` | `1 0 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `478 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+0.输入虚构` | `1 0 0 0` | `∅` | `390 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+1.r1身份可信链` | `1 0 0 0` | `∅` | `704 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+2.r2假死物证表` | `1 0 0 0` | `∅` | `489 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+3.r3面具知情者表` | `1 0 0 0` | `∅` | `546 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+4.r4双份指令表` | `1 0 0 0` | `∅` | `548 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+5.r5r6制度场阶梯` | `1 0 0 0` | `∅` | `559 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+6.r7恩庇债账` | `1 0 0 0` | `∅` | `372 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+7.r8r9复仇结算` | `1 0 0 0` | `∅` | `621 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+8.r10公开揭示检查` | `1 0 0 0` | `∅` | `342 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/examples/worked-example.md+9.这个示例没有证明什么` | `1 0 0 0` | `检` | `282 / — / — / —` | `UNALIGNED?` |
| `WAVE4` | `1 0 0 0` | `检` | `525 / — / — / —` | `UNALIGNED?` |
| `M6` | `1 0 0 0` | `∅` | `391 / — / — / —` | `UNALIGNED?` |
| `PG559` | `1 0 0 0` | `适` | `1026 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/03-institutions-and-patronage.md+r13r14后半文本反证20261031pg50906l23216718实读` | `1 0 0 0` | `∅` | `376 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/03-institutions-and-patronage.md+20261031补齐run新增pg15454单源new` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/03-institutions-and-patronage.md+new影子政权复用既有结社网络pnew单源pg15454条件建议` | `1 0 0 0` | `规` | `997 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/03-institutions-and-patronage.md+new忠诚测试=空包弹处决pnew单源pg15454条件建议` | `1 0 0 0` | `规` | `558 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/05-reveal-and-boundaries.md+失败出口` | `1 0 0 0` | `检` | `548 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/05-reveal-and-boundaries.md+本批未覆盖` | `1 0 0 0` | `∅` | `216 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/05-reveal-and-boundaries.md+20261031补齐run新增pg15454单源new` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/05-reveal-and-boundaries.md+new叛变式披露pnew单源pg15454条件建议` | `1 0 0 0` | `规` | `855 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/06-post-victory-control.md+f起义前承诺与起义后失控` | `1 0 0 0` | `∅` | `1364 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/06-post-victory-control.md+h冲突而非公式` | `1 0 0 0` | `例` | `576 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/06-post-victory-control.md+p改写验收问题` | `1 0 0 0` | `∅` | `698 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-architecture/references/06-post-victory-control.md+证据和负触发` | `1 0 0 0` | `∅` | `322 / — / — / —` | `UNALIGNED?` |
| `PG403` | `1 0 0 0` | `∅` | `234 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG558` | `1 0 0 0` | `∅` | `226 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG560` | `1 0 0 0` | `∅` | `218 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG60` | `1 0 0 0` | `∅` | `243 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-architecture/references/source-index.md+规则与来源位置` | `1 0 0 0` | `∅` | `1195 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-architecture/references/source-index.md+20261031本轮覆盖更新覆盖下方历史wave4终轮旧数值` | `1 0 0 0` | `∅` | `1311 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-architecture/references/source-index.md+版权与使用边界` | `1 0 0 0` | `∅` | `279 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-architecture/references/source-index.md+当前p2结论` | `1 0 0 0` | `∅` | `268 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-architecture/references/source-index.md+20261030终轮roundp4final实测状态覆盖` | `1 0 0 0` | `例` | `3243 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `T1` | `1 0 0 0` | `∅` | `169 / — / — / —` | `UNALIGNED?` |
| `T2` | `1 0 0 0` | `∅` | `179 / — / — / —` | `UNALIGNED?` |
| `T3` | `1 0 0 0` | `∅` | `159 / — / — / —` | `UNALIGNED?` |
| `T4` | `1 0 0 0` | `∅` | `162 / — / — / —` | `UNALIGNED?` |
| `T5` | `1 0 0 0` | `∅` | `169 / — / — / —` | `UNALIGNED?` |
| `T6` | `1 0 0 0` | `∅` | `189 / — / — / —` | `UNALIGNED?` |
| `T7` | `1 0 0 0` | `∅` | `391 / — / — / —` | `UNALIGNED?` |
| `T8` | `1 0 0 0` | `∅` | `186 / — / — / —` | `UNALIGNED?` |
| `T9` | `1 0 0 0` | `∅` | `171 / — / — / —` | `UNALIGNED?` |
| `T10` | `1 0 0 0` | `∅` | `176 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+一触发与负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+正触发用这套规则` | `1 0 0 0` | `∅` | `449 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+负触发不要用这套规则` | `1 0 0 0` | `∅` | `629 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+二输入合同缺任一项先问不要猜` | `1 0 0 0` | `∅` | `786 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+三任务路由先看这张表再进规则` | `1 0 0 0` | `∅` | `765 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+四规则清单每条都带来源锚点` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+规则族a身份伪装维持与验真` | `1 0 0 0` | `怎反败` | `4591 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+规则族b权谋组织与舆论账本` | `1 0 0 0` | `规怎例` | `3919 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+五执行步骤按序不要跳` | `1 0 0 0` | `规怎反检败` | `1264 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+六输出合同每次交付必须包含这五块` | `1 0 0 0` | `∅` | `720 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+七失败出口遇到就停不要硬套` | `1 0 0 0` | `∅` | `703 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+八按需加载的references` | `1 0 0 0` | `∅` | `456 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/SKILL.md+九元数据沿用并迁移历史记录` | `1 0 0 0` | `∅` | `2252 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `1187 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/assets/icon-large.svg+iconlarge.svg` | `1 0 0 0` | `∅` | `430 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/assets/icon-small.svg+iconsmall.svg` | `1 0 0 0` | `∅` | `421 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+一内部反例同一机制在文本里被自己推翻` | `1 0 0 0` | `∅` | `748 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+二来源类型局限贯穿全部15源` | `1 0 0 0` | `∅` | `1646 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+三跨来源冲突登记unresolved不合并` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+c1｜"什么算身份证明"的分裂` | `1 0 0 0` | `∅` | `772 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+c2｜复仇收束形态` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+c3｜把柄机制的评价分歧` | `1 0 0 0` | `∅` | `107 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+四明确"不适用"的来源要素缺失禁止硬凑` | `1 0 0 0` | `∅` | `558 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+五被拒绝的"规则"曾出现在历史推断里本轮不采纳` | `1 0 0 0` | `∅` | `591 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md+六失败出口skill使用者的兜底` | `1 0 0 0` | `∅` | `746 / — / — / —` | `UNALIGNED?` |
| `A1` | `1 0 0 0` | `怎适` | `961 / — / — / —` | `UNALIGNED?` |
| `A2` | `1 0 0 0` | `怎` | `1031 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `怎` | `1031 / — / — / —` | `UNALIGNED?` |
| `A3` | `1 0 0 0` | `适` | `547 / — / — / —` | `UNALIGNED?` |
| `A4` | `1 0 0 0` | `∅` | `606 / — / — / —` | `UNALIGNED?` |
| `A5` | `1 0 0 0` | `反` | `703 / — / — / —` | `UNALIGNED?` |
| `A6` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `A7` | `1 0 0 0` | `∅` | `405 / — / — / —` | `UNALIGNED?` |
| `A8` | `1 0 0 0` | `∅` | `546 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/identity-disguise-and-proof.md+a8反例边界` | `1 0 0 0` | `∅` | `397 / — / — / —` | `UNALIGNED?` |
| `A9` | `1 0 0 0` | `∅` | `877 / — / — / —` | `UNALIGNED?` |
| `A10` | `1 0 0 0` | `∅` | `608 / — / — / —` | `UNALIGNED?` |
| `B1` | `1 0 0 0` | `适` | `971 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `适` | `971 / — / — / —` | `UNALIGNED?` |
| `B2` | `1 0 0 0` | `适` | `519 / — / — / —` | `UNALIGNED?` |
| `B3` | `1 0 0 0` | `例` | `1035 / — / — / —` | `UNALIGNED?` |
| `B4` | `1 0 0 0` | `∅` | `861 / — / — / —` | `UNALIGNED?` |
| `B5` | `1 0 0 0` | `∅` | `474 / — / — / —` | `UNALIGNED?` |
| `B6` | `1 0 0 0` | `适` | `517 / — / — / —` | `UNALIGNED?` |
| `B7` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `B8` | `1 0 0 0` | `∅` | `411 / — / — / —` | `UNALIGNED?` |
| `B9` | `1 0 0 0` | `∅` | `520 / — / — / —` | `UNALIGNED?` |
| `B10` | `1 0 0 0` | `例适` | `431 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `639 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `适` | `759 / — / — / —` | `UNALIGNED?` |
| `C5` | `1 0 0 0` | `规` | `728 / — / — / —` | `UNALIGNED?` |
| `C6` | `1 0 0 0` | `败` | `299 / — / — / —` | `UNALIGNED?` |
| `revenge-intrigue-craft/references/sources-index.md+索引表` | `1 0 0 0` | `∅` | `7087 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `revenge-intrigue-craft/references/sources-index.md+引用规则强制` | `1 0 0 0` | `∅` | `515 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 12 儿童青少年（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 12 儿童青少年

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`child-story-craft`、`children-ya-craft-b05`、`childrens-youth-fiction-craft-b01`

**规则单元数 175；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 175（100.0%）**
**flag 计数**：SOURCE_ONLY=14；UNALIGNED?=175

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `P4` | `1 0 0 0` | `∅` | `1498 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+0.这是什么` | `1 0 0 0` | `检` | `373 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+1.证据底座20261030最终复核` | `1 0 0 0` | `规` | `1280 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+触发` | `1 0 0 0` | `∅` | `274 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+负触发` | `1 0 0 0` | `例` | `196 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `437 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+4.最短执行路径1个门` | `1 0 0 0` | `规` | `350 / — / — / —` | `UNALIGNED?` |
| `S1` | `1 0 0 0` | `∅` | `123 / — / — / —` | `UNALIGNED?` |
| `S2` | `1 0 0 0` | `∅` | `122 / — / — / —` | `UNALIGNED?` |
| `S3` | `1 0 0 0` | `∅` | `126 / — / — / —` | `UNALIGNED?` |
| `S4` | `1 0 0 0` | `∅` | `109 / — / — / —` | `UNALIGNED?` |
| `S5` | `1 0 0 0` | `∅` | `109 / — / — / —` | `UNALIGNED?` |
| `S6` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `S7` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `S8` | `1 0 0 0` | `∅` | `118 / — / — / —` | `UNALIGNED?` |
| `S9` | `1 0 0 0` | `∅` | `125 / — / — / —` | `UNALIGNED?` |
| `S10` | `1 0 0 0` | `∅` | `132 / — / — / —` | `UNALIGNED?` |
| `S11` | `1 0 0 0` | `∅` | `129 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+5.历史规则索引11条均已逐条裁决表内旧名不是现行硬要求` | `1 0 0 0` | `∅` | `1412 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+6.禁止项` | `1 0 0 0` | `∅` | `449 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+7.两张最小模板` | `1 0 0 0` | `检` | `294 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/SKILL.md+9.文件地图与自检` | `1 0 0 0` | `∅` | `536 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `164 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+1.s1全然承诺律` | `1 0 0 0` | `规检` | `1102 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+2.s2事件节奏律` | `1 0 0 0` | `规例` | `710 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+3.s3永不露怯律` | `1 0 0 0` | `规` | `1205 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+4.s4领笑机制` | `1 0 0 0` | `规` | `839 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+5.s5回味停顿律` | `1 0 0 0` | `规` | `787 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+6.s613配比` | `1 0 0 0` | `规` | `1048 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+7.s7愚行教育学` | `1 0 0 0` | `规` | `986 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/01-oral-telling.md+8.s8可讲性筛选` | `1 0 0 0` | `规` | `741 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/02-child-narrator.md+1.s9第三人称自称` | `1 0 0 0` | `规` | `1122 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/02-child-narrator.md+2.s10公开延期道具` | `1 0 0 0` | `规` | `984 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/02-child-narrator.md+3.s11险境慢镜头` | `1 0 0 0` | `规` | `1075 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/02-child-narrator.md+4.补充儿童逻辑字面主义与争吵债务同源观察` | `1 0 0 0` | `规` | `395 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/03-formats.md+1.装置观察只证体例不支撑章内技巧` | `1 0 0 0` | `∅` | `836 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/03-formats.md+2.现代迁移全部hnotproven` | `1 0 0 0` | `∅` | `308 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/03-formats.md+本轮p4使用限制` | `1 0 0 0` | `∅` | `294 / — / — / —` | `UNALIGNED?` |
| `B-05` | `1 0 0 0` | `∅` | `5066 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG473` | `1 0 0 0` | `∅` | `5066 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `B03` | `1 0 0 0` | `∅` | `5066 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG859` | `1 0 0 0` | `∅` | `5066 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `child-story-craft/references/04-source-index.md+本轮覆盖总账agent2最终复核` | `1 0 0 0` | `反` | `919 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `child-story-craft/references/p4-field-guide.md+s4–s5笑点预告与回味` | `1 0 0 0` | `怎例反适` | `661 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/p4-field-guide.md+统一处理约定` | `1 0 0 0` | `∅` | `425 / — / — / —` | `UNALIGNED?` |
| `child-story-craft/references/p4-field-guide.md+年龄适配儿童视角与现实危险边界` | `1 0 0 0` | `∅` | `1404 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+触发负触发` | `1 0 0 0` | `∅` | `482 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+先确认的输入缺哪项就标unknown不要猜` | `1 0 0 0` | `∅` | `516 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+路由表先选行再加载文件` | `1 0 0 0` | `∅` | `1119 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+执行步骤按顺序做不要跳` | `1 0 0 0` | `∅` | `1314 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+缺料冲突与失败出口` | `1 0 0 0` | `∅` | `786 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+输出合同` | `1 0 0 0` | `∅` | `757 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/SKILL.md+来源许可与验收边界` | `1 0 0 0` | `适` | `901 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `501 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/examples.md+反例清单不得当作必选规则` | `1 0 0 0` | `∅` | `429 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+一rc01–rc15对历史规则的处置` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc01｜动物命名必须"外观+性格"→revise` | `1 0 0 0` | `反` | `597 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc02｜每章末必须有道德歌谣→reject证据状态notproven` | `1 0 0 0` | `反` | `402 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc03｜玩具"在无人时突然动起来"→revise` | `1 0 0 0` | `反适` | `532 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc04｜秘密空间承载成长行动→keep` | `1 0 0 0` | `反` | `398 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc05｜用"天真童言"承担政治法律知识→revise本轮加硬反例` | `1 0 0 0` | `反` | `627 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc06｜固定字数每天例行+教训→revise` | `1 0 0 0` | `反` | `420 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc07｜终章必须"童年逝去"的挽歌→reject证据状态notproven` | `1 0 0 0` | `反检` | `387 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc08｜动物本能=道德科学事实→revise` | `1 0 0 0` | `反` | `394 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc09｜儿童独立侦查=无风险→revise本轮加证据` | `1 0 0 0` | `反` | `404 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc10｜自然秘密地点必然治愈→revise` | `1 0 0 0` | `反` | `388 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc11｜教学提示与虚构内容分区→keep` | `1 0 0 0` | `反` | `347 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc12｜改编=降到固定词汇表→revise` | `1 0 0 0` | `反` | `409 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc13｜终章必须留续集伏笔→reject` | `1 0 0 0` | `反` | `370 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc14｜框架讲述人必须年长女性→reject` | `1 0 0 0` | `反` | `362 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+rc15｜按性别分类编排→revise本轮强化` | `1 0 0 0` | `反` | `515 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+二r16–r22本轮补读区间新取得的规则` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r16｜奖惩的可见部分与判据要分开写` | `1 0 0 0` | `∅` | `537 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r17｜成人任意处置儿童时必须写出儿童的内视角` | `1 0 0 0` | `例` | `677 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r18｜真实儿童言语可直接使用但必须标明性质` | `1 0 0 0` | `∅` | `476 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r19｜分级索引≠年龄分级` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r20｜汇编工具书与单卷叙事的收束要求不同` | `1 0 0 0` | `∅` | `218 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r21｜战利品与代价同频绑定` | `1 0 0 0` | `∅` | `455 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+r22｜同一符号允许多起源不必强行统一` | `1 0 0 0` | `∅` | `298 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/rules.md+三撤销与不可迁移清单审稿时逐条对照` | `1 0 0 0` | `∅` | `680 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/scope-and-conflicts.md+1.这批材料是什么` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `PG910` | `1 0 0 0` | `∅` | `1124 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/scope-and-conflicts.md+3.必须保留不许强行统一的冲突` | `1 0 0 0` | `∅` | `829 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/scope-and-conflicts.md+4.不适用的来源` | `1 0 0 0` | `∅` | `413 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/scope-and-conflicts.md+5.情节分歧与安全出口` | `1 0 0 0` | `∅` | `667 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/scope-and-conflicts.md+6.本包的证据边界` | `1 0 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `PG113` | `1 0 0 0` | `∅` | `224 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG359` | `1 0 0 0` | `∅` | `345 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG479` | `1 0 0 0` | `∅` | `215 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG74` | `1 0 0 0` | `∅` | `218 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `children-ya-craft-b05/references/source-index.md+本轮roundp4final20261030复核补充` | `1 0 0 0` | `∅` | `569 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `children-ya-craft-b05/references/source-index.md+本轮重新定位行号的可回源锚点供引用` | `1 0 0 0` | `∅` | `2334 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `children-ya-craft-b05/references/source-index.md+已作废的证据` | `1 0 0 0` | `∅` | `396 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `C01` | `1 0 0 0` | `例反` | `687 / — / — / —` | `UNALIGNED?` |
| `C02` | `1 0 0 0` | `反` | `725 / — / — / —` | `UNALIGNED?` |
| `C03` | `1 0 0 0` | `反` | `609 / — / — / —` | `UNALIGNED?` |
| `C04` | `1 0 0 0` | `反` | `606 / — / — / —` | `UNALIGNED?` |
| `C05` | `1 0 0 0` | `反适` | `568 / — / — / —` | `UNALIGNED?` |
| `C06` | `1 0 0 0` | `反` | `694 / — / — / —` | `UNALIGNED?` |
| `C07` | `1 0 0 0` | `反` | `659 / — / — / —` | `UNALIGNED?` |
| `children-ya-craft-b05/references/techniques.md+输入缺失时的分支所有c通用` | `1 0 0 0` | `规` | `355 / — / — / —` | `UNALIGNED?` |
| `CD-01` | `1 0 0 0` | `∅` | `81 / — / — / —` | `UNALIGNED?` |
| `CD-02` | `1 0 0 0` | `∅` | `49 / — / — / —` | `UNALIGNED?` |
| `CD-03` | `1 0 0 0` | `∅` | `51 / — / — / —` | `UNALIGNED?` |
| `CD-04` | `1 0 0 0` | `∅` | `44 / — / — / —` | `UNALIGNED?` |
| `CD-05` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `CD-06` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `CD-07` | `1 0 0 0` | `∅` | `75 / — / — / —` | `UNALIGNED?` |
| `CD-08` | `1 0 0 0` | `∅` | `46 / — / — / —` | `UNALIGNED?` |
| `CD-09` | `1 0 0 0` | `∅` | `99 / — / — / —` | `UNALIGNED?` |
| `CD-10` | `1 0 0 0` | `∅` | `84 / — / — / —` | `UNALIGNED?` |
| `CS-01` | `1 0 0 0` | `∅` | `45 / — / — / —` | `UNALIGNED?` |
| `CS-02` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `CS-03` | `1 0 0 0` | `∅` | `44 / — / — / —` | `UNALIGNED?` |
| `CS-04` | `1 0 0 0` | `∅` | `46 / — / — / —` | `UNALIGNED?` |
| `CS-05` | `1 0 0 0` | `∅` | `47 / — / — / —` | `UNALIGNED?` |
| `CS-06` | `1 0 0 0` | `∅` | `54 / — / — / —` | `UNALIGNED?` |
| `CS-07` | `1 0 0 0` | `∅` | `48 / — / — / —` | `UNALIGNED?` |
| `CS-08` | `1 0 0 0` | `∅` | `53 / — / — / —` | `UNALIGNED?` |
| `CS-09` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `CS-10` | `1 0 0 0` | `∅` | `48 / — / — / —` | `UNALIGNED?` |
| `CS-11` | `1 0 0 0` | `∅` | `44 / — / — / —` | `UNALIGNED?` |
| `CS-12` | `1 0 0 0` | `∅` | `53 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+触发与排除` | `1 0 0 0` | `例适` | `782 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+一线自检用户抱怨→查什么30秒定位` | `1 0 0 0` | `∅` | `1001 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+输入预检必须先做` | `1 0 0 0` | `∅` | `731 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+路由与工作流按任务加载不必全读` | `1 0 0 0` | `∅` | `865 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+执行步骤` | `1 0 0 0` | `规` | `1116 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+冲突与缺料出口原样输出不得自行化解` | `1 0 0 0` | `∅` | `886 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/SKILL.md+输出与许可` | `1 0 0 0` | `∅` | `461 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `检` | `1301 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md+1.年龄带` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md+2.四问` | `1 0 0 0` | `∅` | `541 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md+3.硬规则检查` | `1 0 0 0` | `∅` | `632 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md+4.建议` | `1 0 0 0` | `∅` | `506 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `∅` | `357 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `357 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md+6.开放项` | `1 0 0 0` | `∅` | `111 / — / — / —` | `UNALIGNED?` |
| `C4` | `1 0 0 0` | `∅` | `634 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `634 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/revision-conflict.md+例3｜用户要求"保证孩子读完会提升阅读理解"` | `1 0 0 0` | `怎` | `398 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/revision-conflict.md+例4｜用户要求"救命场面最后让全村送他一车东西"` | `1 0 0 0` | `∅` | `243 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/examples/revision-conflict.md+例5｜用户要求"配图怎么排"` | `1 0 0 0` | `∅` | `207 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/references/age-band-rules.md+a带的额外规则` | `1 0 0 0` | `∅` | `344 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/references/age-band-rules.md+b带的额外规则` | `1 0 0 0` | `规` | `427 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/references/age-band-rules.md+c带的额外规则` | `1 0 0 0` | `规` | `322 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/references/age-band-rules.md+跨带硬规则三条带都要过` | `1 0 0 0` | `∅` | `298 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `401 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `规` | `589 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `规` | `589 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `规` | `589 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `规` | `589 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `规` | `589 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `∅` | `395 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `∅` | `395 / — / — / —` | `UNALIGNED?` |
| `PG474` | `1 0 0 0` | `∅` | `4432 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/references/source-index.md+覆盖与校验状态` | `1 0 0 0` | `规` | `264 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `T01` | `1 0 0 0` | `规` | `369 / — / — / —` | `UNALIGNED?` |
| `T02` | `1 0 0 0` | `∅` | `535 / — / — / —` | `UNALIGNED?` |
| `T03` | `1 0 0 0` | `∅` | `426 / — / — / —` | `UNALIGNED?` |
| `T04` | `1 0 0 0` | `例` | `374 / — / — / —` | `UNALIGNED?` |
| `T05` | `1 0 0 0` | `∅` | `462 / — / — / —` | `UNALIGNED?` |
| `T06` | `1 0 0 0` | `∅` | `371 / — / — / —` | `UNALIGNED?` |
| `T07` | `1 0 0 0` | `∅` | `408 / — / — / —` | `UNALIGNED?` |
| `T08` | `1 0 0 0` | `∅` | `211 / — / — / —` | `UNALIGNED?` |
| `T09` | `1 0 0 0` | `∅` | `283 / — / — / —` | `UNALIGNED?` |
| `T10` | `1 0 0 0` | `败` | `293 / — / — / —` | `UNALIGNED?` |
| `T11` | `1 0 0 0` | `∅` | `210 / — / — / —` | `UNALIGNED?` |
| `T12` | `1 0 0 0` | `∅` | `230 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/templates/diagnosis-card.md+1.年龄带判定` | `1 0 0 0` | `∅` | `284 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/templates/diagnosis-card.md+4.建议三列不得省略` | `1 0 0 0` | `∅` | `93 / — / — / —` | `UNALIGNED?` |
| `childrens-youth-fiction-craft-b01/templates/diagnosis-card.md+6.开放项` | `1 0 0 0` | `∅` | `103 / — / — / —` | `UNALIGNED?` |

---

## 题材 13 异世界穿越（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 13 异世界穿越

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`isekai-crossworld-craft`、`isekai-crossworld-craft-b01`、`isekai-crossworld-craft-b02`

**规则单元数 110；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 110（100.0%）**
**flag 计数**：SOURCE_ONLY=22；UNALIGNED?=110

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `isekai-crossworld-craft/SKILL.md+1.触发与负触发` | `1 0 0 0` | `检` | `1071 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+2.输入缺什么先问什么不要猜` | `1 0 0 0` | `∅` | `493 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1125 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+4.执行步骤` | `1 0 0 0` | `∅` | `785 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 0 0 0` | `∅` | `89 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 0 0 0` | `∅` | `81 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 0 0 0` | `∅` | `55 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 0 0 0` | `∅` | `85 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 0 0 0` | `∅` | `110 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 0 0 0` | `∅` | `86 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 0 0 0` | `∅` | `87 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `49 / — / — / —` | `UNALIGNED?` |
| `R9` | `1 0 0 0` | `∅` | `49 / — / — / —` | `UNALIGNED?` |
| `R10` | `1 0 0 0` | `∅` | `91 / — / — / —` | `UNALIGNED?` |
| `R11` | `1 0 0 0` | `∅` | `65 / — / — / —` | `UNALIGNED?` |
| `R12` | `1 0 0 0` | `∅` | `59 / — / — / —` | `UNALIGNED?` |
| `R13` | `1 0 0 0` | `∅` | `88 / — / — / —` | `UNALIGNED?` |
| `R14` | `1 0 0 0` | `∅` | `56 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+5.规则裁决表摘要完整依据见referencesruleverdicts.md` | `1 0 0 0` | `∅` | `1322 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+6.输出合同` | `1 0 0 0` | `检` | `862 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+7.失败出口` | `1 0 0 0` | `规` | `744 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/SKILL.md+8.references索引` | `1 0 0 0` | `规` | `483 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/conflicts-and-exceptions.md+1.三处保留不统一的冲突不要伪造共识` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `C1` | `1 0 0 0` | `∅` | `713 / — / — / —` | `UNALIGNED?` |
| `C2` | `1 0 0 0` | `规` | `294 / — / — / —` | `UNALIGNED?` |
| `C3` | `1 0 0 0` | `∅` | `453 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/conflicts-and-exceptions.md+2.四类反例踩到就改` | `1 0 0 0` | `∅` | `684 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/conflicts-and-exceptions.md+3.明确不通用化的情节设计禁止升格为规则` | `1 0 0 0` | `∅` | `882 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/conflicts-and-exceptions.md+4.本skill自身的边界如实声明` | `1 0 0 0` | `∅` | `470 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+①门径型portal` | `1 0 0 0` | `规适` | `687 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+②时间位移型timeslip` | `1 0 0 0` | `∅` | `993 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+③前世返祖型reincarnationatavism` | `1 0 0 0` | `∅` | `801 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+④飞地邻近异界型enclave` | `1 0 0 0` | `例` | `780 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+⑤失落世界型lostworld` | `1 0 0 0` | `∅` | `831 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+⑥传送点悖论型transferparadox` | `1 0 0 0` | `规例` | `635 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md+分型提示` | `1 0 0 0` | `∅` | `304 / — / — / —` | `UNALIGNED?` |
| `PG783` | `1 0 0 0` | `∅` | `2401 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG86` | `1 0 0 0` | `∅` | `2401 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG11` | `1 0 0 0` | `∅` | `2401 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft/references/source-index.md+补充4` | `1 0 0 0` | `∅` | `781 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft/references/source-index.md+反例3` | `1 0 0 0` | `∅` | `546 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft/references/source-index.md+冲突3组` | `1 0 0 0` | `∅` | `525 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG234` | `1 0 0 0` | `∅` | `1057 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft/references/source-index.md+未证明0` | `1 0 0 0` | `∅` | `198 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+1.触发与负触发` | `1 0 0 0` | `规` | `971 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+2.输入必须先拿到什么缺哪一项就走§6失败出口` | `1 0 0 0` | `∅` | `934 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `884 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+4.执行步骤` | `1 0 0 0` | `∅` | `1624 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+5.输出合同` | `1 0 0 0` | `∅` | `714 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+6.失败出口` | `1 0 0 0` | `∅` | `771 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+7.references加载表按需读不要一次全读` | `1 0 0 0` | `∅` | `451 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/SKILL.md+8.元数据溯源` | `1 0 0 0` | `例` | `719 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规反` | `1062 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§1技术知识优势是否有用不统一` | `1 0 0 0` | `∅` | `766 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§2乌托邦的价值排序不统一三种不可调和` | `1 0 0 0` | `∅` | `771 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§3返乡是否可能不统一` | `1 0 0 0` | `∅` | `341 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§4超自然要不要解释不统一` | `1 0 0 0` | `∅` | `594 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§6同一册内的内部不一致不是错误是可学习的做法` | `1 0 0 0` | `∅` | `855 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md+§7边界本批次里不算本体裁的三部不要拿它们当证据` | `1 0 0 0` | `∅` | `370 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/mechanism-taxonomy.md+§1入口类型五类本批次内没有任何一类占多数` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `E1` | `1 0 0 0` | `怎` | `697 / — / — / —` | `UNALIGNED?` |
| `E2` | `1 0 0 0` | `∅` | `670 / — / — / —` | `UNALIGNED?` |
| `E3` | `1 0 0 0` | `∅` | `653 / — / — / —` | `UNALIGNED?` |
| `E4` | `1 0 0 0` | `∅` | `682 / — / — / —` | `UNALIGNED?` |
| `E5` | `1 0 0 0` | `∅` | `212 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/mechanism-taxonomy.md+§2出口类型三态开局必须选定一种` | `1 0 0 0` | `反败` | `899 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/mechanism-taxonomy.md+§3代价的三类写法本批次实际出现的` | `1 0 0 0` | `规` | `525 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/mechanism-taxonomy.md+§4入口×出口的搭配建议h非来源事实` | `1 0 0 0` | `∅` | `465 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/rule-verdicts.md+裁决汇总` | `1 0 0 0` | `规` | `387 / — / — / —` | `UNALIGNED?` |
| `PG620` | `1 0 0 0` | `∅` | `2097 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG55` | `1 0 0 0` | `∅` | `2097 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG62` | `1 0 0 0` | `∅` | `2097 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/source-index.md+乌托邦反乌托邦轴支持但互不相容` | `1 0 0 0` | `∅` | `893 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/source-index.md+相邻机制轴补充` | `1 0 0 0` | `∅` | `777 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/source-index.md+边界轴不适用不要当证据` | `1 0 0 0` | `∅` | `367 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b01/references/source-index.md+统计` | `1 0 0 0` | `∅` | `334 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+1.触发与负触发` | `1 0 0 0` | `规` | `1293 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+2.输入必须先拿到什么缺哪一项就走§6失败出口` | `1 0 0 0` | `∅` | `1108 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1211 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+4.执行步骤` | `1 0 0 0` | `检` | `2988 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+5.输出合同` | `1 0 0 0` | `∅` | `763 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+6.失败出口` | `1 0 0 0` | `∅` | `900 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+7.references加载表按需读不要一次全读` | `1 0 0 0` | `∅` | `538 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/SKILL.md+8.元数据溯源` | `1 0 0 0` | `例` | `1086 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `规反` | `1221 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md+§1梦离魂通道要不要给锚本批次最核心的分歧` | `1 0 0 0` | `怎` | `1546 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md+§5具体反例清单按规则编号` | `1 0 0 0` | `∅` | `1005 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md+§6只有单部作品支持的判断h清单不得作硬检查项` | `1 0 0 0` | `∅` | `953 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md+§7本批次无法回答的问题notproven遇到就明确说` | `1 0 0 0` | `∅` | `944 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+§1入口类型七类` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.1装置型` | `1 0 0 0` | `∅` | `554 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.2契约机构型` | `1 0 0 0` | `∅` | `445 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.3灾害事故型` | `1 0 0 0` | `∅` | `436 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.4睡眠梦型本批次主力7部中3部` | `1 0 0 0` | `∅` | `579 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.5离魂假死型` | `1 0 0 0` | `∅` | `380 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.6记忆前世型` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+1.7无入口被编排型` | `1 0 0 0` | `∅` | `562 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+§2出口类型四种结局本批次全有` | `1 0 0 0` | `∅` | `508 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+§3越界强度与"世界承认因果律"的对应` | `1 0 0 0` | `∅` | `644 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md+§4对不上号时怎么办` | `1 0 0 0` | `∅` | `526 / — / — / —` | `UNALIGNED?` |
| `R16` | `1 0 0 0` | `∅` | `567 / — / — / —` | `UNALIGNED?` |
| `R15` | `1 0 0 0` | `∅` | `567 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/rule-verdicts.md+裁决汇总` | `1 0 0 0` | `∅` | `496 / — / — / —` | `UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/source-index.md+一梦离魂前世通道轴批次02主力` | `1 0 0 0` | `∅` | `1980 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/source-index.md+二时间与社会制度轴` | `1 0 0 0` | `∅` | `2517 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/source-index.md+三技术赠礼与反噬轴` | `1 0 0 0` | `∅` | `676 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/source-index.md+四寓言无入口型` | `1 0 0 0` | `∅` | `868 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG289` | `1 0 0 0` | `∅` | `632 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG288` | `1 0 0 0` | `∅` | `478 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `isekai-crossworld-craft-b02/references/source-index.md+七按问题快速定位` | `1 0 0 0` | `∅` | `679 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

---

## 题材 14 年代现实（阈值 30%）

# K1 返工 raw 表（r2）· genre-fiction-craft / 题材 14 年代现实

- 版本：`2026-11-04-r2`（A.3 只追加不覆盖；W1 的 `2026-11-04` 旧表原样保留，两版并存）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文；表内只有编号/路径/字节/标记。
- **盘点单位（附录 A.1）= 规则单元**：优先规则编号；无编号的用「文件路径 + 标题」。genre 机制卡编号从标题括号与表格行提取。
- **对齐（2.8 节）**：不再按文件名/basename；用「规则编号（含 2.3 节新旧前缀对照）+ 标题 + 内容块」对齐。
- 新旧前缀对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 阈值：缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK；默认 30%。

### flag 语义（**补充标记不是丢失、待定向精读**）

| flag | 含义 |
|---|---|
| `MISSING` | **A.1**：只留给「编号体系可比（v3 目标目录仍使用同一编号族或 2.3 节改号后的编号族）+ 该编号确实缺号 + 无相似标题 + 无相似内容块（≥2 个 12 字连续片段）」的单元；编号整体改名/重组导致对不上的一律不记 MISSING。仅为机械判定，不等于内容丢失 |
| `SHRUNK` | **A.1**：v0→v3 缩减超阈值 |
| `BLOCK_LOST` | **A.1**：该单元某类小块在对齐到的 v3 单元里消失 |
| `RENUMBERED?` | **A.1**：编号消失但按改号前缀/相似标题对齐 |
| `UNALIGNED?` | **补充标记，不是丢失**：机械对齐失败，无法判定该单元是否缺失；须 W3 定向精读比内容 |
| `SOURCE_ONLY` | **补充标记，不是丢失**：来自 source-index / sources-and-editions / source-cases / version-and-provenance / *-provenance 等来源类文件；按 2.8 节「删掉的来源文件不直接恢复」 |
| `—` | 已对齐且无 A.1 信号 |

- `blocks` 简写：规/怎/例/反/检/适/败/∅；由标签行关键词机械识别。
- `bytes` 为该声明单元正文的字节数（表格行按行计）；重组后是信号，不是应恢复的量。
- 谱系 v0 来源：`realism-craft-b09`

**规则单元数 68；v3 对齐成功 26（38.2%）；对齐失败 UNALIGNED? 42（61.8%）**
**flag 计数**：RENUMBERED?=25；SOURCE_ONLY=9；UNALIGNED?=42；—=1

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `realism-craft-b09/SKILL.md+0.能力和来源边界` | `1 0 0 0` | `∅` | `1212 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/SKILL.md+1.最短执行流程五步而非六书结局照抄` | `1 0 0 0` | `∅` | `1148 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/SKILL.md+2.按任务选择的模块` | `1 0 0 0` | `∅` | `993 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/SKILL.md+3.核心规则从六部作品归纳的有条件hp不是作者共同宣言` | `1 0 0 0` | `∅` | `1910 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/SKILL.md+4.交付格式和停止规则` | `1 0 0 0` | `适` | `997 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/agents/openai.yaml+openai.yaml` | `1 0 0 0` | `∅` | `192 / — / — / —` | `UNALIGNED?` |
| `GQ5` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `B09` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/examples/worked-example.md+案例a地方家庭生活的经济选择` | `1 1 1 1` | `∅` | `1290 / — / — / —` | `RENUMBERED?` |
| `realism-craft-b09/examples/worked-example.md+案例b作者要求“把结尾改成人人都幸福”` | `1 1 1 1` | `∅` | `361 / — / — / —` | `RENUMBERED?` |
| `realism-craft-b09/examples/worked-example.md+案例c缺料越界` | `1 1 1 1` | `∅` | `324 / — / — / —` | `RENUMBERED?` |
| `RC1` | `1 0 0 0` | `反检适` | `959 / — / — / —` | `UNALIGNED?` |
| `RC2` | `1 0 0 0` | `反` | `942 / — / — / —` | `UNALIGNED?` |
| `RC3` | `1 0 0 0` | `例反` | `930 / — / — / —` | `UNALIGNED?` |
| `RC4` | `1 0 0 0` | `反适` | `872 / — / — / —` | `UNALIGNED?` |
| `RC5` | `1 0 0 0` | `反` | `804 / — / — / —` | `UNALIGNED?` |
| `RC6` | `1 0 0 0` | `反` | `821 / — / — / —` | `UNALIGNED?` |
| `RC7` | `1 0 0 0` | `反` | `893 / — / — / —` | `UNALIGNED?` |
| `RC8` | `1 0 0 0` | `反` | `706 / — / — / —` | `UNALIGNED?` |
| `RC9` | `1 0 0 0` | `反适` | `726 / — / — / —` | `UNALIGNED?` |
| `RC10` | `1 0 0 0` | `反` | `905 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/04-history-genre-and-evidence.md+类型不是互斥的“现实主义”标签` | `1 1 1 0` | `∅` | `1282 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/04-history-genre-and-evidence.md+真实史实vs小说中的事实` | `1 1 1 0` | `∅` | `834 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/04-history-genre-and-evidence.md+对旧价值与文本的安全边界` | `1 1 1 0` | `∅` | `535 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/04-history-genre-and-evidence.md+原书摘要不是“教材”` | `1 1 0 0` | `∅` | `274 / — / — / —` | `UNALIGNED?` |
| `W1` | `1 1 1 1` | `∅` | `1019 / 1414 / — / —` | `RENUMBERED?` |
| `W2` | `1 1 1 1` | `适` | `775 / 849 / — / —` | `RENUMBERED?` |
| `W3` | `1 1 1 1` | `∅` | `783 / 756 / — / —` | `RENUMBERED?` |
| `W4` | `1 1 0 0` | `∅` | `578 / 689 / — / —` | `UNALIGNED?` |
| `RL-01` | `1 1 1 1` | `∅` | `131 / 287 / 1025 / 1032` | `—` |
| `RC-02` | `1 1 0 0` | `∅` | `116 / 145 / — / —` | `UNALIGNED?` |
| `RC-03` | `1 1 0 0` | `∅` | `106 / 175 / — / —` | `UNALIGNED?` |
| `RC-04` | `1 1 0 0` | `∅` | `137 / 244 / — / —` | `UNALIGNED?` |
| `RC-05` | `1 1 0 0` | `∅` | `127 / 211 / — / —` | `UNALIGNED?` |
| `RC-06` | `1 1 0 0` | `∅` | `139 / 182 / — / —` | `UNALIGNED?` |
| `RC-07` | `1 1 0 0` | `∅` | `124 / 182 / — / —` | `UNALIGNED?` |
| `RC-08` | `1 1 0 0` | `∅` | `113 / 187 / — / —` | `UNALIGNED?` |
| `RC-09` | `1 1 0 0` | `∅` | `129 / 154 / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/scope-and-conflicts.md+适用范围` | `1 0 0 0` | `∅` | `253 / — / — / —` | `UNALIGNED?` |
| `realism-craft-b09/references/scope-and-conflicts.md+具体冲突` | `1 0 0 0` | `∅` | `1043 / — / — / —` | `UNALIGNED?` |
| `B-09` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG45` | `1 0 0 0` | `∅` | `138 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG46` | `1 0 0 0` | `∅` | `133 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG514` | `1 0 0 0` | `∅` | `156 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG76` | `1 0 0 0` | `∅` | `178 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG98` | `1 0 0 0` | `∅` | `137 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `realism-craft-b09/references/source-index.md+六部实际全文非六个独立作者` | `1 0 0 0` | `∅` | `1574 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `realism-craft-b09/references/source-index.md+真实fscene源锚点只证明小说里写过不证明真实历史` | `1 0 0 0` | `∅` | `1035 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `realism-craft-b09/references/source-index.md+来源族与结论限度` | `1 1 0 0` | `∅` | `775 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `RM-01` | `1 1 1 1` | `适` | `108 / 287 / 1025 / 1032` | `RENUMBERED?` |
| `RM-02` | `1 1 1 1` | `适` | `123 / 103 / 1169 / 1154` | `RENUMBERED?` |
| `RM-03` | `1 1 1 1` | `适` | `111 / 111 / 1196 / 1088` | `RENUMBERED?` |
| `RM-04` | `1 1 1 1` | `适` | `96 / 112 / 1096 / 1093` | `RENUMBERED?` |
| `RM-05` | `1 1 1 1` | `适` | `94 / 139 / 989 / 998` | `RENUMBERED?` |
| `RM-06` | `1 1 1 1` | `适` | `111 / 157 / 876 / 872` | `RENUMBERED?` |
| `RM-07` | `1 1 1 1` | `适` | `115 / 153 / 917 / 930` | `RENUMBERED?` |
| `RM-08` | `1 1 1 1` | `适` | `105 / 105 / 805 / 811` | `RENUMBERED?` |
| `RM-09` | `1 1 1 1` | `适` | `147 / 147 / 1086 / 1086` | `RENUMBERED?` |
| `RM-10` | `1 1 1 1` | `适` | `120 / 120 / 984 / 915` | `RENUMBERED?` |
| `RD-01` | `1 1 1 1` | `∅` | `93 / 93 / 1025 / 1032` | `RENUMBERED?` |
| `RD-02` | `1 1 1 1` | `∅` | `124 / 124 / 1169 / 1154` | `RENUMBERED?` |
| `RD-03` | `1 1 1 1` | `∅` | `120 / 120 / 1196 / 1088` | `RENUMBERED?` |
| `RD-04` | `1 1 1 1` | `∅` | `118 / 159 / 1096 / 1093` | `RENUMBERED?` |
| `RD-05` | `1 1 1 1` | `∅` | `127 / 127 / 989 / 998` | `RENUMBERED?` |
| `RD-06` | `1 1 1 1` | `∅` | `118 / 118 / 876 / 872` | `RENUMBERED?` |
| `RD-07` | `1 1 1 1` | `∅` | `105 / 105 / 917 / 930` | `RENUMBERED?` |
| `RD-08` | `1 1 1 1` | `∅` | `108 / 108 / 805 / 811` | `RENUMBERED?` |
| `RD-09` | `1 1 1 1` | `∅` | `100 / 109 / 1086 / 1086` | `RENUMBERED?` |


---

## 机制卡编号核对（从标题括号与表格行提取，2.3 节 / §6.1 修订依据）


| 题材 | 版本 | 编号范围 | 张数 | 连续 |
|---|---|---|---|---|
| G02 言情 | v0 | — | — | — |
| G02 言情 | v1 | — | — | — |
| G02 言情 | v2 | RO-K001–RO-K166 | 166 | 是 |
| G02 言情 | v3 | RO-K001–RO-K120 | 120 | 是 |
| G05 科幻 | v0 | — | — | — |
| G05 科幻 | v1 | — | — | — |
| G05 科幻 | v2 | SF-K001–SF-K102 | 102 | 是 |
| G05 科幻 | v3 | SF-K001–SF-K102 | 102 | 是 |

- **W1 已证实的事实（本表复核一致）**：G02 言情 `RO-K` v2 为 001–166 共 166 张、v3 为 001–120 共 120 张，**v2→v3 删 46 张（RO-K121–166）**；G05 科幻 `SF-K` 在 v2 / v3 均为 001–102 连续 102 张，**未删卡，属逐卡压缩**（`05-science-fiction/mechanisms.md` 32.4→20.4 KB）。
- 计划 §6.1 已据此修订：G02 是删卡、G05 是逐卡压缩，两者不是同一种丢失，**W3 分别处理**；G05 不套用 G02 的「补回删卡编号」做法。
- 机制卡正文含来源案例，本表只输出编号范围与张数，不复制任何原文。

---

## 如实记录（不伪造、不跳过）

- v0→v3 题材文件重组、编号与标题改写，按文件名无法对齐（2.8 节）；无法机械对齐的单元逐行记 `UNALIGNED?`，不记 `MISSING`、不伪造对齐行。
- `fantasy-adventure-structure-lab`（04/08）、`supernatural-power-craft`（04/03）为跨题材多归属，按主归属登记，副归属待 W3 核定。
- `title~` 为粗粒度相似标题信号，须 W3 比内容核定；本表只出信号，不做逐条决定。
