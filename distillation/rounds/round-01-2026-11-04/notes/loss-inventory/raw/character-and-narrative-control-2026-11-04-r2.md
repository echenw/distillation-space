# K1 返工 raw 表（r2）· character-and-narrative-control

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
- 谱系 v0 来源：`narrative-pov-information-control`、`nonlinear-time-craft`、`character-psychology-trauma-craft`、`psycho-trauma-craft-b10`

**规则单元数 259；v3 对齐成功 62（23.9%）；对齐失败 UNALIGNED? 195（75.3%）**
**flag 计数**：MISSING=2；RENUMBERED?=49；SOURCE_ONLY=47；UNALIGNED?=195；—=13

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `narrative-pov-information-control/SKILL.md+1.适用与转介` | `1 0 1 1` | `∅` | `1060 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+2.使用方式` | `1 0 1 1` | `规例检` | `879 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+3.四条最短路径` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+选视角开新书或重构` | `1 0 1 1` | `∅` | `625 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+设计信息反转误会秘密` | `1 0 1 1` | `∅` | `522 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+写或改一场戏` | `1 0 1 1` | `∅` | `517 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+诊断稿子` | `1 0 0 0` | `∅` | `259 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+4.症状速查` | `1 0 1 1` | `∅` | `1383 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+5.规则卡` | `1 0 1 1` | `∅` | `106 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/SKILL.md+叙述者与视点` | `1 0 0 0` | `怎例` | `5329 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+信息控制` | `1 0 0 0` | `怎例` | `1767 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+场景概述与时间` | `1 0 0 0` | `怎例` | `3161 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+6.交付格式没有宿主格式时` | `1 0 0 0` | `∅` | `517 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+7.规则冲突时` | `1 0 0 0` | `∅` | `519 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+8.参考文件` | `1 0 0 0` | `∅` | `1296 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/SKILL.md+9.来源与可信度` | `1 0 0 0` | `规` | `863 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/examples/worked-example.md+例一三代盐场家族史选视角诊断群像` | `1 0 1 1` | `∅` | `1961 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/examples/worked-example.md+例二密室推理设计信息` | `1 0 1 1` | `∅` | `1286 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/examples/worked-example.md+例三认知变化写正文时演出意识` | `1 0 1 1` | `∅` | `1419 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/examples/worked-example.md+例四网文多视角的“与此同时”诊断切换` | `1 0 1 1` | `∅` | `1333 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+1.诊断顺序` | `1 0 1 1` | `∅` | `895 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+2.十种症状` | `1 0 1 1` | `∅` | `2410 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+3.修改单示例` | `1 0 1 1` | `∅` | `776 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+4.只能做一件事时` | `1 0 1 1` | `∅` | `510 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+5.规则的例外` | `1 0 1 1` | `∅` | `1409 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+6.作者坚持时` | `1 0 1 1` | `∅` | `847 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+7.误用本skill` | `1 0 1 1` | `∅` | `1202 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/diagnosis.md+8.不在本skill里诊断` | `1 0 1 1` | `∅` | `316 / — / — / —` | `RENUMBERED?` |
| `PV-09` | `1 0 1 1` | `∅` | `291 / — / 239 / 239` | `—` |
| `PV-16` | `1 0 1 1` | `∅` | `291 / — / 778 / 886` | `—` |
| `PV-11` | `1 0 1 1` | `∅` | `291 / — / 1168 / 1168` | `—` |
| `narrative-pov-information-control/references/information-control.md+1.两条底层约束` | `1 0 1 1` | `∅` | `506 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/information-control.md+2.四种信息结构` | `1 0 1 1` | `∅` | `571 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/information-control.md+3.知识表` | `1 0 1 1` | `∅` | `804 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/information-control.md+4.五种合法的隐瞒` | `1 0 1 1` | `∅` | `1167 / — / — / —` | `RENUMBERED?` |
| `PV-10` | `1 0 1 1` | `∅` | `743 / — / 864 / 870` | `—` |
| `narrative-pov-information-control/references/information-control.md+7.揭示三查` | `1 0 1 1` | `∅` | `380 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/information-control.md+9.常见错误` | `1 0 1 1` | `∅` | `651 / — / — / —` | `RENUMBERED?` |
| `PV-01` | `1 0 1 1` | `∅` | `130 / — / 1147 / 1229` | `—` |
| `PV-08` | `1 0 1 1` | `∅` | `130 / — / 1099 / 1133` | `—` |
| `PV-02` | `1 0 1 1` | `∅` | `701 / — / 905 / 905` | `—` |
| `PV-03` | `1 0 1 1` | `∅` | `966 / — / 1126 / 1207` | `—` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+3.1第一人称的三条默认限制` | `1 0 0 0` | `∅` | `669 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+3.2人物化叙述者的收益` | `1 0 1 1` | `∅` | `314 / — / — / —` | `RENUMBERED?` |
| `PV-04` | `1 0 1 1` | `∅` | `0 / — / 0 / 0` | `—` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+4.1三层` | `1 0 1 1` | `∅` | `318 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+4.2常见越界` | `1 0 1 1` | `∅` | `978 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+4.3合法化装置` | `1 0 1 1` | `∅` | `847 / — / — / —` | `RENUMBERED?` |
| `PV-05` | `1 0 1 1` | `∅` | `0 / — / 0 / 0` | `—` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+5.1四项` | `1 0 1 1` | `∅` | `785 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+5.2起点和放宽` | `1 0 1 1` | `∅` | `1012 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+5.3切换的写法` | `1 0 1 1` | `∅` | `301 / — / — / —` | `RENUMBERED?` |
| `PV-06` | `1 0 1 1` | `∅` | `685 / — / 685 / 764` | `—` |
| `PV-07` | `1 0 1 1` | `怎例` | `834 / — / 834 / 849` | `—` |
| `narrative-pov-information-control/references/narrator-and-viewpoint.md+9.自检` | `1 0 1 1` | `∅` | `408 / — / — / —` | `RENUMBERED?` |
| `PV-15` | `1 0 1 1` | `∅` | `88 / — / 1167 / 1911` | `—` |
| `PV-12` | `1 0 1 0` | `∅` | `88 / — / 1371 / —` | `UNALIGNED?` |
| `PV-17` | `1 0 1 0` | `∅` | `88 / — / 760 / —` | `UNALIGNED?` |
| `narrative-pov-information-control/references/scene-summary-and-time.md+1.四个词` | `1 0 1 0` | `∅` | `447 / — / — / —` | `UNALIGNED?` |
| `PV-13` | `1 0 1 0` | `∅` | `1185 / — / 1616 / —` | `MISSING` |
| `PV-14` | `1 0 1 0` | `∅` | `1231 / — / 1514 / —` | `MISSING` |
| `narrative-pov-information-control/references/scene-summary-and-time.md+7.时间跨度速查` | `1 0 1 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/references/scene-summary-and-time.md+8.自检` | `1 0 1 0` | `例` | `417 / — / — / —` | `UNALIGNED?` |
| `narrative-pov-information-control/references/source-index.md+1.主要来源` | `1 0 0 0` | `∅` | `581 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `narrative-pov-information-control/references/source-index.md+2.其他来源` | `1 0 0 0` | `∅` | `1864 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `narrative-pov-information-control/references/source-index.md+3.lubbock的位置` | `1 0 0 0` | `∅` | `4237 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `narrative-pov-information-control/references/source-index.md+4.规则与来源对照` | `1 0 0 0` | `∅` | `1393 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `narrative-pov-information-control/references/source-index.md+5.本skill不声称什么` | `1 0 0 0` | `规` | `283 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+1.称呼就是视点` | `1 0 1 1` | `检` | `651 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+2.没有时态时怎样控制距离` | `1 0 1 1` | `∅` | `1018 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+3.网文里常见的视角做法` | `1 0 1 1` | `∅` | `1020 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+4.系统面板弹幕群聊帖子文件类装置` | `1 0 1 1` | `规` | `731 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+5.重生穿越回溯时间合同` | `1 0 1 1` | `∅` | `675 / — / — / —` | `RENUMBERED?` |
| `narrative-pov-information-control/references/zh-and-serial.md+6.日更连载的视角` | `1 0 1 1` | `∅` | `745 / — / — / —` | `RENUMBERED?` |
| `P4` | `1 0 0 0` | `∅` | `1513 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+本轮p3p4强制区分四条时间轴` | `1 0 0 0` | `∅` | `648 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+0.这是什么` | `1 0 0 0` | `检` | `346 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+1.证据底座` | `1 0 0 0` | `规适` | `898 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+2.触发负触发` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+触发` | `1 0 0 0` | `∅` | `237 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+负触发` | `1 0 0 0` | `例` | `192 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `529 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+4.最短执行路径1个门` | `1 0 0 0` | `∅` | `513 / — / — / —` | `UNALIGNED?` |
| `N1` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `N2` | `1 0 0 0` | `∅` | `117 / — / — / —` | `UNALIGNED?` |
| `N3` | `1 0 0 0` | `∅` | `114 / — / — / —` | `UNALIGNED?` |
| `N4` | `1 0 0 0` | `∅` | `125 / — / — / —` | `UNALIGNED?` |
| `N5` | `1 0 0 0` | `∅` | `113 / — / — / —` | `UNALIGNED?` |
| `N6` | `1 0 0 0` | `∅` | `121 / — / — / —` | `UNALIGNED?` |
| `N7` | `1 0 0 0` | `∅` | `107 / — / — / —` | `UNALIGNED?` |
| `N8` | `1 0 0 0` | `∅` | `119 / — / — / —` | `UNALIGNED?` |
| `N9` | `1 0 0 0` | `∅` | `116 / — / — / —` | `UNALIGNED?` |
| `N10` | `1 0 0 0` | `∅` | `140 / — / — / —` | `UNALIGNED?` |
| `N11` | `1 0 0 0` | `∅` | `134 / — / — / —` | `UNALIGNED?` |
| `N12` | `1 0 0 0` | `∅` | `154 / — / — / —` | `UNALIGNED?` |
| `N13` | `1 0 0 0` | `∅` | `151 / — / — / —` | `UNALIGNED?` |
| `N14` | `1 0 0 0` | `∅` | `135 / — / — / —` | `UNALIGNED?` |
| `N15` | `1 0 0 0` | `∅` | `143 / — / — / —` | `UNALIGNED?` |
| `N16` | `1 0 0 0` | `∅` | `136 / — / — / —` | `UNALIGNED?` |
| `N17` | `1 0 0 0` | `∅` | `144 / — / — / —` | `UNALIGNED?` |
| `N18` | `1 0 0 0` | `∅` | `115 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+5.规则索引18条canonical在各文件` | `1 0 0 0` | `∅` | `2380 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+6.禁止项` | `1 0 0 0` | `规` | `367 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+7.两张最小模板` | `1 0 0 0` | `检` | `319 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+8.失败出口` | `1 0 0 0` | `∅` | `343 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/SKILL.md+9.文件地图与自检` | `1 0 0 0` | `∅` | `671 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/agents/openai.yaml+openai.yaml` | `1 1 0 0` | `∅` | `202 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+1.n1自罪侦查闭环` | `1 1 0 0` | `∅` | `563 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+2.n2自信息纸条` | `1 1 0 0` | `∅` | `538 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+3.n3时间复利劳动` | `1 1 0 0` | `规` | `674 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+4.n4自举抹除环` | `1 1 0 0` | `∅` | `578 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+5.n5错误升级链` | `1 1 0 0` | `∅` | `429 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/01-loops.md+6.round02全读复核` | `1 0 0 0` | `∅` | `418 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/02-flickers.md+1.n6时间线闪切` | `1 1 0 0` | `∅` | `636 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/02-flickers.md+2.n7动机倒置` | `1 1 0 0` | `∅` | `604 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/02-flickers.md+3.n8交叉信息体` | `1 1 0 0` | `规` | `563 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/02-flickers.md+4.n9振荡收束` | `1 1 0 0` | `∅` | `569 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/02-flickers.md+5.round02全读复核` | `1 0 0 0` | `∅` | `284 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/03-viewers.md+1.n10时间视者放逐` | `1 1 0 0` | `例` | `700 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/03-viewers.md+2.n11复仇者静默化` | `1 1 0 0` | `∅` | `580 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/03-viewers.md+3.n12遗稿制度化` | `1 1 0 0` | `∅` | `970 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/04-source-index.md+1.定位读法` | `1 0 0 0` | `∅` | `367 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG642` | `1 0 0 0` | `∅` | `6128 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `nonlinear-time-craft/references/04-source-index.md+3.覆盖声明` | `1 0 0 0` | `规` | `362 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `nonlinear-time-craft/references/04-source-index.md+4.unverified禁止引用` | `1 0 0 0` | `∅` | `179 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `nonlinear-time-craft/references/04-source-index.md+5.p4返工全部40来源的机制归类一个主要用处非互不相关的排他分类` | `1 0 0 0` | `例反` | `1259 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+1.n13互为未来时代互换` | `1 1 0 0` | `∅` | `1011 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+2.n14预装剧本律` | `1 1 0 0` | `∅` | `954 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+3.n15知识缺口律` | `1 1 0 0` | `∅` | `845 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+4.n16故障逆流律` | `1 1 0 0` | `怎` | `870 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+5.n17永生代价清单` | `1 1 0 0` | `∅` | `846 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/05-exchanges.md+6.n18等时铁律` | `1 1 0 0` | `∅` | `902 / — / — / —` | `UNALIGNED?` |
| `C-05` | `1 1 0 0` | `∅` | `0 / 0 / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/06-temporal-protocol.md+进入任务的两个问题避免错误路由` | `1 1 0 0` | `∅` | `878 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/06-temporal-protocol.md+建模四表` | `1 1 0 0` | `∅` | `1053 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/06-temporal-protocol.md+五类问题与条件操作` | `1 1 0 0` | `∅` | `1214 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/06-temporal-protocol.md+各源关系与反例非套路堆砌` | `1 1 0 0` | `适` | `1072 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/06-temporal-protocol.md+输出合同与失败出口` | `1 1 0 0` | `∅` | `404 / — / — / —` | `UNALIGNED?` |
| `nonlinear-time-craft/references/historical-provenance.md+原resultsskillsskill.md的非标准frontmatter` | `1 0 0 0` | `∅` | `16 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `nonlinear-time-craft/references/historical-provenance.md+本次返工前轮次入口的非标准frontmatter若有` | `1 0 0 0` | `∅` | `15 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+触发条件命中任一即可使用` | `1 0 0 0` | `∅` | `480 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+负触发命中即停止或转出不得套用` | `1 0 0 0` | `∅` | `809 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+输入与权限` | `1 0 0 0` | `∅` | `420 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+任务路由` | `1 1 0 0` | `∅` | `1391 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+主流程六步不要跳步` | `1 0 0 0` | `例` | `1927 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+输出合同` | `1 0 0 0` | `∅` | `388 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+失败出口` | `1 0 0 0` | `∅` | `395 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+保留的冲突不得在本skill内伪造共识` | `1 0 0 0` | `∅` | `793 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/SKILL.md+来源与版本迁移自历史成果不得删除` | `1 0 0 0` | `∅` | `529 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/agents/openai.yaml+openai.yaml` | `1 1 0 0` | `∅` | `636 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+正常规划` | `1 1 0 0` | `∅` | `620 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+缺料临床请求` | `1 1 0 0` | `∅` | `244 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+互斥设定无法自动改稿` | `1 1 0 0` | `∅` | `329 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+伦理边界强制和解` | `1 1 0 0` | `∅` | `256 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+本轮新增高强度场景的节律改写` | `1 0 0 0` | `∅` | `851 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/examples.md+本轮新增对峙戏不靠铁证` | `1 0 0 0` | `∅` | `704 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p01角色自辩与行为不一定一致keep补两项` | `1 1 0 0` | `∅` | `971 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p02强烈情感可以连续转向revise新增"可见触点"硬条件` | `1 0 0 0` | `∅` | `744 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p03微小物体承载注意revise拆成两种机制` | `1 0 0 0` | `∅` | `933 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p04身体信号与自述可以形成张力revise两处实质修正` | `1 0 0 0` | `∅` | `1123 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p05梦记忆不是自动的诊断工具revise分功能+反例` | `1 0 0 0` | `∅` | `710 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p06自我惩罚与被宽恕的张力keep补一条内部冲突` | `1 1 0 0` | `∅` | `806 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p07沉默和身体姿态不等于单一动机revise补社会成因禁止写成本性` | `1 0 0 0` | `∅` | `873 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p08关系改变不是一瞬治愈revise区分"触点"与"保证"` | `1 0 0 0` | `∅` | `909 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p09社会处境与心理推断分别保留keep补"羞辱的可见性"` | `1 1 0 0` | `∅` | `669 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p10角色感到失控与叙事可见因果分开revise补叙述者层面的因果` | `1 0 0 0` | `∅` | `974 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p11高强度场景的四拍节律new` | `1 1 0 0` | `∅` | `638 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+c09p12对峙戏由"双向可用的解释"驱动new` | `1 1 0 0` | `∅` | `889 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/psychological-mechanics.md+故障收敛` | `1 0 0 0` | `∅` | `251 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/scene-revision.md+未有正文心理弧线规划` | `1 0 0 0` | `∅` | `311 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/scene-revision.md+有正文诊断` | `1 0 0 0` | `∅` | `575 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/scene-revision.md+已获改写授权修订` | `1 0 0 0` | `∅` | `2112 / — / — / —` | `UNALIGNED?` |
| `character-psychology-trauma-craft/references/source-index.md+版本覆盖与许可历史元数据完整保留` | `1 0 0 0` | `∅` | `819 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `character-psychology-trauma-craft/references/source-index.md+本轮新增复核台账roundp4final20261030` | `1 0 0 0` | `∅` | `573 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `character-psychology-trauma-craft/references/source-index.md+证据映射表` | `1 0 0 0` | `∅` | `2671 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `character-psychology-trauma-craft/templates/character-state-card.md+本轮新增字段roundp4final20261030按修订后的规则必填` | `1 0 0 0` | `∅` | `1293 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+何时用何时不用` | `1 0 0 0` | `∅` | `856 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+输入缺什么就问什么不要替用户编` | `1 0 0 0` | `∅` | `594 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+任务路由先看这里再进references` | `1 0 0 0` | `∅` | `1975 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+判断流程六步逐步执行不要跳` | `1 0 0 0` | `适` | `1865 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+输出合同默认按这个顺序交付` | `1 0 0 0` | `∅` | `1018 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+失败出口出现任一情况只输出有证据的部分+缺口` | `1 0 0 0` | `∅` | `605 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/SKILL.md+来源与验证边界不要把覆盖范围说成效果` | `1 0 0 0` | `规` | `1209 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/agents/openai.yaml+openai.yaml` | `1 1 0 0` | `∅` | `525 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/examples/scene-examples.md+示例a感官线索与权力压力并存` | `1 1 0 0` | `∅` | `901 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/examples/scene-examples.md+示例b多层证词互相抵触不等于有人患病` | `1 0 0 0` | `∅` | `695 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/examples/scene-examples.md+缺料边界示例` | `1 1 0 0` | `∅` | `477 / — / — / —` | `UNALIGNED?` |
| `RT-16` | `1 1 0 0` | `反` | `1263 / 1301 / — / —` | `UNALIGNED?` |
| `RT-17` | `1 1 0 0` | `反` | `1155 / 1938 / — / —` | `UNALIGNED?` |
| `RT-18` | `1 1 0 0` | `规反` | `1109 / 1541 / — / —` | `UNALIGNED?` |
| `B-10` | `1 1 0 0` | `∅` | `313 / 0 / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+bodyobjectandspeculativemechanism` | `1 0 0 0` | `∅` | `2255 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG720` | `1 0 0 0` | `∅` | `2681 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG472` | `1 0 0 0` | `∅` | `2681 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG638` | `1 0 0 0` | `∅` | `2681 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG447` | `1 0 0 0` | `∅` | `2681 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG219` | `1 0 0 0` | `∅` | `229 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG220` | `1 0 0 0` | `∅` | `219 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG208` | `1 0 0 0` | `∅` | `204 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG211` | `1 0 0 0` | `∅` | `213 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG432` | `1 0 0 0` | `∅` | `207 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG898` | `1 0 0 0` | `∅` | `213 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG913` | `1 0 0 0` | `∅` | `218 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG804` | `1 0 0 0` | `∅` | `202 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG946` | `1 0 0 0` | `∅` | `225 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG467` | `1 0 0 0` | `∅` | `211 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG222` | `1 0 0 0` | `∅` | `199 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+narrativetestimonyanddelayedknowledge` | `1 0 0 0` | `∅` | `3451 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG284` | `1 0 0 0` | `∅` | `206 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG267` | `1 0 0 0` | `∅` | `246 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG165` | `1 0 0 0` | `∅` | `236 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG133` | `1 0 0 0` | `∅` | `225 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG143` | `1 0 0 0` | `∅` | `219 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+classfinanceandsocialfate` | `1 0 0 0` | `∅` | `4300 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG367` | `1 0 0 0` | `∅` | `3732 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG94` | `1 0 0 0` | `∅` | `3732 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+gamblingnarrativeandhistoricalmedicalcom` | `1 0 0 0` | `∅` | `669 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+conflictresolutionexit` | `1 0 0 0` | `∅` | `635 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/72-source-differences.md+本轮确认的不可统一冲突保留不伪造共识` | `1 0 0 0` | `∅` | `485 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `RT-01` | `1 1 0 0` | `检` | `1141 / 1226 / — / —` | `UNALIGNED?` |
| `RT-08` | `1 1 0 0` | `检` | `1141 / 869 / — / —` | `UNALIGNED?` |
| `RT-02` | `1 1 0 0` | `检` | `1141 / 853 / — / —` | `UNALIGNED?` |
| `RT-04` | `1 1 0 0` | `检` | `1141 / 1611 / — / —` | `UNALIGNED?` |
| `RT-07` | `1 1 0 0` | `检` | `1141 / 723 / — / —` | `UNALIGNED?` |
| `RT-11` | `1 1 0 0` | `检` | `1141 / 901 / — / —` | `UNALIGNED?` |
| `RT-12` | `1 1 0 0` | `检` | `1141 / 848 / — / —` | `UNALIGNED?` |
| `RT-13` | `1 1 0 0` | `检` | `1141 / 817 / — / —` | `UNALIGNED?` |
| `RT-03` | `1 1 0 0` | `检` | `1141 / 926 / — / —` | `UNALIGNED?` |
| `RT-15` | `1 1 0 0` | `检` | `1141 / 1324 / — / —` | `UNALIGNED?` |
| `RT-10` | `1 1 0 0` | `检` | `1141 / 1406 / — / —` | `UNALIGNED?` |
| `RT-05` | `1 1 0 0` | `检` | `1141 / 886 / — / —` | `UNALIGNED?` |
| `RT-06` | `1 1 0 0` | `检` | `1141 / 917 / — / —` | `UNALIGNED?` |
| `RT-09` | `1 1 0 0` | `检` | `1141 / 1093 / — / —` | `UNALIGNED?` |
| `RT-14` | `1 1 0 0` | `检` | `1141 / 745 / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/rules.md+十五规则共同边界` | `1 0 0 0` | `∅` | `1287 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+正向范围` | `1 1 0 0` | `∅` | `361 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+不适用必须退出或另找来源` | `1 1 0 0` | `∅` | `538 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+c18意识流vs物件传统叙述` | `1 1 0 0` | `∅` | `478 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+c19环境决定vs人物自身选择` | `1 1 0 0` | `适` | `402 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+c20帝国种族与文化的叙述所有权` | `1 1 0 0` | `∅` | `579 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+c21历史病理话语vs当代诊断` | `1 1 0 0` | `∅` | `486 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/scope-and-conflicts.md+输出风险等级` | `1 1 0 0` | `∅` | `534 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/source-index.md+scopelicense` | `1 0 0 0` | `∅` | `614 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/source-index.md+20261030p4final轮复核旧表全部保留未改动任何历史登记值` | `1 0 0 0` | `∅` | `347 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/source-index.md+引文回源命中数历史台账+本轮新台账逐字比对±3行` | `1 0 0 0` | `∅` | `1418 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `psycho-trauma-craft-b10/references/techniques.md+路由f跨书冲突与反例` | `1 0 0 0` | `∅` | `379 / — / — / —` | `UNALIGNED?` |
| `psycho-trauma-craft-b10/references/techniques.md+快速回归三问` | `1 0 0 0` | `∅` | `354 / — / — / —` | `UNALIGNED?` |
| `S-01` | `1 1 0 0` | `∅` | `406 / 428 / — / —` | `UNALIGNED?` |
| `PD-01` | `1 1 1 1` | `∅` | `139 / 139 / 1093 / 1093` | `RENUMBERED?` |
| `PD-02` | `1 1 1 1` | `∅` | `145 / 145 / 1293 / 1297` | `RENUMBERED?` |
| `PD-03` | `1 1 1 1` | `∅` | `133 / 133 / 936 / 936` | `RENUMBERED?` |
| `PD-04` | `1 1 1 1` | `∅` | `136 / 136 / 885 / 885` | `RENUMBERED?` |
| `PD-05` | `1 1 1 1` | `∅` | `151 / 151 / 1047 / 1047` | `RENUMBERED?` |
| `PD-06` | `1 1 1 1` | `∅` | `154 / 154 / 930 / 930` | `RENUMBERED?` |
| `PD-07` | `1 1 1 1` | `∅` | `144 / 144 / 894 / 894` | `RENUMBERED?` |
| `PD-08` | `1 1 1 1` | `∅` | `181 / 181 / 1031 / 1031` | `RENUMBERED?` |
| `PD-09` | `1 1 1 1` | `∅` | `147 / 147 / 1347 / 1347` | `RENUMBERED?` |
| `PD-10` | `1 1 1 1` | `∅` | `148 / 148 / 978 / 978` | `RENUMBERED?` |
| `psycho-trauma-craft-b10/templates/psycho-trauma-diagnosis.md+最短输出格式` | `1 1 0 0` | `∅` | `278 / — / — / —` | `UNALIGNED?` |

## 如实记录

- 无法按编号/标题对齐的单元记 `UNALIGNED?`，**不记 MISSING**；来源类文件记 `SOURCE_ONLY`。不伪造对齐行、不跳过。
- 本表只出信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。
