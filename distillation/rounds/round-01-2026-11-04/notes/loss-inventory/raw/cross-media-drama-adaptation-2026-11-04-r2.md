# K1 返工 raw 表（r2）· cross-media-drama-adaptation

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
- 谱系 v0 来源：`cross-media-drama-transfer`

**规则单元数 86；v3 对齐成功 0（0.0%）；对齐失败 UNALIGNED? 86（100.0%）**
**flag 计数**：SOURCE_ONLY=9；UNALIGNED?=86

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `cross-media-drama-transfer/SKILL.md+1.何时使用` | `1 0 0 0` | `∅` | `671 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+2.负触发不要用本skill` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+3.输入契约缺什么就先问什么` | `1 0 0 0` | `∅` | `677 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+4.任务路由先读哪份reference` | `1 0 0 0` | `∅` | `1340 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.执行步骤` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.1判可转移性先做这一步不判就不要动笔` | `1 0 0 0` | `∅` | `467 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.2承认"原作不是画面故事"` | `1 0 0 0` | `∅` | `142 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.3分场` | `1 0 0 0` | `∅` | `322 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.4长度` | `1 0 0 0` | `∅` | `285 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.5连续性` | `1 0 0 0` | `∅` | `471 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.6成本闸门` | `1 0 0 0` | `∅` | `331 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.7结局与高潮` | `1 0 0 0` | `∅` | `527 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.8舞台落地若目标是舞台` | `1 0 0 0` | `∅` | `219 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+5.9画面层检查若目标是银幕` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `771 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+7.失败出口` | `1 0 0 0` | `∅` | `651 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/SKILL.md+8.证据声明` | `1 0 0 0` | `∅` | `1016 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/agents/openai.yaml+openai.yaml` | `1 1 0 0` | `∅` | `331 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/examples/worked-example.md+例一判断一个题材能不能改到银幕无声片口径` | `1 1 0 0` | `∅` | `1494 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/examples/worked-example.md+例二一段分场的连续性与载体体检` | `1 1 0 0` | `∅` | `1318 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/examples/worked-example.md+例三反向不要把案例写成规则` | `1 1 0 0` | `∅` | `555 / — / — / —` | `UNALIGNED?` |
| `R1` | `1 1 0 0` | `∅` | `0 / 0 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/01-transferability.md+r1.1三条判据f` | `1 0 0 0` | `∅` | `898 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/01-transferability.md+r1.2反向判据什么在银幕上更强f` | `1 1 0 0` | `∅` | `471 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/01-transferability.md+r1.3一手反例不要以为"能演就必须演"f` | `1 1 0 0` | `例` | `892 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/01-transferability.md+r1.4可执行动作p` | `1 1 0 0` | `∅` | `336 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/01-transferability.md+r1.5容易犯的错` | `1 1 0 0` | `∅` | `235 / — / — / —` | `UNALIGNED?` |
| `R2` | `1 1 0 0` | `∅` | `0 / 0 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.1场景的定义最稳的一条f` | `1 0 0 0` | `∅` | `733 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.2空间连续性f` | `1 1 0 0` | `∅` | `463 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.3时间连续性f` | `1 0 0 0` | `例` | `890 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.4长度与场数f` | `1 1 0 0` | `∅` | `636 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.5检查清单p` | `1 1 0 0` | `∅` | `439 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/02-scene-and-continuity.md+r2.6反例与边界` | `1 1 0 0` | `∅` | `385 / — / — / —` | `UNALIGNED?` |
| `R3` | `1 1 0 0` | `∅` | `0 / 0 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.1载体优先级f` | `1 0 0 0` | `∅` | `431 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.2字幕leadersubtitlecaption的四项职务fpg17903` | `1 1 0 0` | `∅` | `422 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.3字幕的两条硬约束f` | `1 0 0 0` | `∅` | `537 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.4信件电报报剪insertf` | `1 1 0 0` | `∅` | `495 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.5物件与布景即叙事f` | `1 1 0 0` | `∅` | `468 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.6声音怎么办无声片口径f` | `1 1 0 0` | `反` | `374 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.7可执行动作p` | `1 1 0 0` | `∅` | `402 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/03-information-carriers.md+r3.8常见错误` | `1 1 0 0` | `∅` | `330 / — / — / —` | `UNALIGNED?` |
| `R4` | `1 1 0 0` | `∅` | `0 / 0 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.1情节结构f` | `1 0 0 0` | `∅` | `774 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.2先定高潮f` | `1 0 0 0` | `∅` | `673 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.3结局三说并存不合并交用户裁决` | `1 0 0 0` | `∅` | `544 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.4信息量与悬念冲突区见07` | `1 1 0 0` | `∅` | `670 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.5兴趣中心与同情f` | `1 0 0 0` | `适` | `772 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.6反例与边界f一手` | `1 1 0 0` | `∅` | `365 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/04-plot-and-ending.md+r4.7可执行动作p` | `1 1 0 0` | `∅` | `400 / — / — / —` | `UNALIGNED?` |
| `R5` | `1 1 0 0` | `∅` | `209 / 250 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.1先读透文本指示不足与指示过多f` | `1 1 0 0` | `∅` | `991 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.2走位与构图f` | `1 0 0 0` | `∅` | `466 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.3群众f` | `1 1 0 0` | `∅` | `372 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.4布景与灯光f` | `1 0 0 0` | `∅` | `709 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.5aside旁白这一类舞台专属约定f边界` | `1 1 0 0` | `∅` | `532 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.6排练与节奏f` | `1 1 0 0` | `∅` | `432 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.7版权边界f历史口径` | `1 1 0 0` | `∅` | `181 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/05-stage-realization.md+r5.8检查清单p` | `1 1 0 0` | `∅` | `430 / — / — / —` | `UNALIGNED?` |
| `R6` | `1 1 0 0` | `∅` | `169 / 268 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.1构图f` | `1 1 0 0` | `∅` | `717 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.2运动f` | `1 1 0 0` | `∅` | `630 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.3节奏f` | `1 1 0 0` | `规` | `803 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.4三条硬禁忌f` | `1 0 0 0` | `∅` | `595 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.5谁负责f` | `1 1 0 0` | `∅` | `405 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.6与导演层来源的接口fpg53117` | `1 1 0 0` | `∅` | `534 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.7检查清单p` | `1 1 0 0` | `∅` | `447 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/06-pictorial-checks.md+r6.8边界` | `1 1 0 0` | `检` | `205 / — / — / —` | `UNALIGNED?` |
| `R7` | `1 1 0 0` | `∅` | `182 / 277 / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+冲突1结局信息量` | `1 1 0 0` | `∅` | `475 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+冲突2节奏快慢` | `1 1 0 0` | `∅` | `469 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+冲突3结尾形态` | `1 1 0 0` | `∅` | `418 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+冲突4演员指导` | `1 1 0 0` | `检` | `451 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+冲突5长片长度` | `1 1 0 0` | `∅` | `440 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+裁决备忘模板输出用` | `1 1 0 0` | `∅` | `207 / — / — / —` | `UNALIGNED?` |
| `cross-media-drama-transfer/references/07-conflicts-and-adjudication.md+关于"共识"的纪律` | `1 1 0 0` | `规` | `431 / — / — / —` | `UNALIGNED?` |
| `R8` | `1 0 0 0` | `∅` | `0 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `cross-media-drama-transfer/references/08-source-index.md+r8.1规则来源7部作者训诫手册` | `1 0 0 0` | `∅` | `1617 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `cross-media-drama-transfer/references/08-source-index.md+r8.2案例基座82部戏剧文本` | `1 0 0 0` | `规` | `615 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `cross-media-drama-transfer/references/08-source-index.md+r8.3覆盖与证据可信度` | `1 0 0 0` | `∅` | `531 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `cross-media-drama-transfer/references/08-source-index.md+r8.4引文行号的两处已知错位必须按更正引用` | `1 0 0 0` | `∅` | `421 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `cross-media-drama-transfer/references/08-source-index.md+r8.5边界负触发的根据` | `1 0 0 0` | `∅` | `560 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG885` | `1 0 0 0` | `∅` | `8730 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG875` | `1 0 0 0` | `∅` | `8730 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG554` | `1 0 0 0` | `∅` | `8730 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |

## 如实记录

- 无法按编号/标题对齐的单元记 `UNALIGNED?`，**不记 MISSING**；来源类文件记 `SOURCE_ONLY`。不伪造对齐行、不跳过。
- 本表只出信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。
