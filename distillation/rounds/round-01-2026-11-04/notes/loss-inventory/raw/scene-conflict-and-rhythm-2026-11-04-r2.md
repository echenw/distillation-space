# K1 返工 raw 表（r2）· scene-conflict-and-rhythm

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
- 谱系 v0 来源：`foreshadowing-and-rhythm`、`scene-chapter-design-lab`、`action-fight-scene-craft`

**规则单元数 147；v3 对齐成功 64（43.5%）；对齐失败 UNALIGNED? 76（51.7%）**
**flag 计数**：BLOCK_LOST=17；MISSING=7；RENUMBERED?=30；SHRUNK=12；SOURCE_ONLY=13；UNALIGNED?=76；—=16

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `foreshadowing-and-rhythm/SKILL.md+1.适用与转介` | `1 0 1 1` | `检` | `872 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+2.使用方式` | `1 0 1 1` | `例` | `716 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+3.三条最短路径` | `1 0 0 0` | `∅` | `0 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/SKILL.md+设计从构思到可写` | `1 0 0 0` | `∅` | `1151 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/SKILL.md+诊断和修改已有稿子` | `1 0 0 0` | `∅` | `480 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/SKILL.md+章末和结尾检查连载长篇` | `1 0 0 0` | `∅` | `373 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/SKILL.md+4.症状速查` | `1 0 1 1` | `∅` | `1347 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+5.规则卡` | `1 0 1 1` | `∅` | `118 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+伏笔与兑现referencessetupandpayoff.md` | `1 0 1 1` | `∅` | `1284 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+悬念与揭晓referencessuspenseandreveal.md` | `1 0 1 1` | `例` | `1176 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+强度与节奏referencesintensityandrhythm.md` | `1 0 1 1` | `∅` | `1763 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+章末与结尾referenceschapterendsandendings.md` | `1 0 1 1` | `∅` | `1273 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+交付前referencesdiagnosis.md` | `1 0 0 0` | `∅` | `272 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/SKILL.md+6.参考文件` | `1 0 1 1` | `∅` | `890 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+7.冲突时的顺序` | `1 0 1 1` | `∅` | `340 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/SKILL.md+8.来源与可信度` | `1 0 1 0` | `规` | `678 / — / — / —` | `UNALIGNED?` |
| `foreshadowing-and-rhythm/examples/worked-example.md+例一设计一个约八千字的悬疑短篇` | `1 0 1 1` | `∅` | `150 / — / — / —` | `RENUMBERED?` |
| `SU-01` | `1 0 1 1` | `∅` | `575 / — / 2330 / 1343` | `—` |
| `SU-02` | `1 0 1 1` | `∅` | `447 / — / 1690 / 1166` | `—` |
| `SU-04` | `1 0 1 1` | `∅` | `447 / — / 300 / 429` | `—` |
| `SU-05` | `1 0 1 1` | `∅` | `353 / — / 190 / 187` | `SHRUNK` |
| `SU-06` | `1 0 1 1` | `∅` | `349 / — / 2079 / 1179` | `—` |
| `SU-07` | `1 0 1 1` | `∅` | `349 / — / 300 / 429` | `—` |
| `SU-11` | `1 0 1 1` | `∅` | `191 / — / 2248 / 761` | `—` |
| `SU-10` | `1 0 1 1` | `∅` | `191 / — / 1768 / 849` | `—` |
| `SU-17` | `1 0 1 1` | `∅` | `364 / — / 1862 / 1945` | `—` |
| `SU-18` | `1 0 1 1` | `∅` | `364 / — / 2909 / 2018` | `—` |
| `foreshadowing-and-rhythm/examples/worked-example.md+例二连载第12–15章的章末诊断` | `1 0 1 1` | `∅` | `87 / — / — / —` | `RENUMBERED?` |
| `SU-15` | `1 0 1 1` | `∅` | `412 / — / 2804 / 2474` | `—` |
| `SU-16` | `1 0 1 1` | `∅` | `184 / — / 184 / 184` | `—` |
| `foreshadowing-and-rhythm/examples/worked-example.md+3.修改单` | `1 0 1 1` | `∅` | `985 / — / — / —` | `RENUMBERED?` |
| `SU-19` | `1 0 1 1` | `∅` | `35 / — / 1879 / 728` | `—` |
| `foreshadowing-and-rhythm/references/diagnosis.md+1.诊断流程` | `1 0 1 1` | `∅` | `930 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/references/diagnosis.md+2.修改单格式` | `1 0 1 1` | `∅` | `742 / — / — / —` | `RENUMBERED?` |
| `foreshadowing-and-rhythm/references/diagnosis.md+4.作者坚持时` | `1 0 1 0` | `∅` | `1366 / — / — / —` | `UNALIGNED?` |
| `SU-14` | `1 0 1 1` | `∅` | `212 / — / 1258 / 713` | `—` |
| `SU-12` | `1 0 1 1` | `规怎例检` | `1237 / — / 1817 / 615` | `SHRUNK;BLOCK_LOST` |
| `SU-13` | `1 0 1 1` | `规怎例反` | `1873 / — / 190 / 187` | `SHRUNK;BLOCK_LOST` |
| `SU-08` | `1 0 1 1` | `∅` | `134 / — / 2179 / 667` | `—` |
| `foreshadowing-and-rhythm/references/source-index.md+1.主要来源` | `1 0 0 0` | `∅` | `582 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `foreshadowing-and-rhythm/references/source-index.md+2.其他来源` | `1 0 0 0` | `∅` | `2541 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `foreshadowing-and-rhythm/references/source-index.md+3.规则与来源对照` | `1 0 0 0` | `∅` | `2408 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `foreshadowing-and-rhythm/references/source-index.md+4.本skill不声称什么` | `1 0 0 0` | `规` | `293 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `SU-09` | `1 0 1 1` | `∅` | `93 / — / 1815 / 1094` | `—` |
| `SU-03` | `1 0 1 1` | `∅` | `93 / — / 1314 / 1153` | `—` |
| `C-06` | `1 0 0 0` | `∅` | `263 / — / — / —` | `MISSING` |
| `scene-chapter-design-lab/SKILL.md+0.元数据沿革与来源迁移自历史skill不得丢弃` | `1 0 0 0` | `∅` | `1156 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+1.何时触发／何时不要触发` | `1 0 0 0` | `检` | `1265 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+2.输入契约` | `1 0 0 0` | `∅` | `711 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1090 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+4.执行步骤按序不许跳` | `1 0 0 0` | `∅` | `1843 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+5.输出合同` | `1 0 0 0` | `∅` | `1038 / — / — / —` | `UNALIGNED?` |
| `S0` | `1 1 0 0` | `∅` | `92 / 1956 / — / —` | `UNALIGNED?` |
| `S1` | `1 1 0 0` | `∅` | `87 / 1179 / — / —` | `UNALIGNED?` |
| `S2` | `1 1 0 0` | `∅` | `99 / 1612 / — / —` | `UNALIGNED?` |
| `S3` | `1 1 0 0` | `∅` | `96 / 1934 / — / —` | `UNALIGNED?` |
| `S4` | `1 1 0 0` | `∅` | `67 / 1633 / — / —` | `UNALIGNED?` |
| `S5` | `1 1 0 0` | `∅` | `75 / 1374 / — / —` | `UNALIGNED?` |
| `S6` | `1 1 0 0` | `∅` | `109 / 3247 / — / —` | `UNALIGNED?` |
| `S6A` | `1 0 0 0` | `∅` | `79 / — / — / —` | `UNALIGNED?` |
| `S7` | `1 1 0 0` | `∅` | `101 / 2526 / — / —` | `UNALIGNED?` |
| `S8` | `1 1 0 0` | `∅` | `95 / 943 / — / —` | `UNALIGNED?` |
| `S9` | `1 1 0 0` | `∅` | `60 / 2037 / — / —` | `UNALIGNED?` |
| `S10` | `1 1 0 0` | `∅` | `77 / 1956 / — / —` | `UNALIGNED?` |
| `S11` | `1 1 0 0` | `∅` | `81 / 1243 / — / —` | `UNALIGNED?` |
| `S12` | `1 1 0 0` | `∅` | `55 / 1014 / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+6.规则索引正文在references这里只作定位` | `1 0 0 0` | `∅` | `1342 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+7.失败出口` | `1 0 0 0` | `规` | `657 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/SKILL.md+8.边界声明` | `1 0 0 0` | `适` | `663 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/agents/openai.yaml+openai.yaml` | `1 1 0 0` | `∅` | `1008 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/examples/worked-example.md+用例1｜正常输入灯塔停电的三个场景` | `1 1 0 0` | `怎` | `2573 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/examples/worked-example.md+用例2｜边界输入一章只有散步没有冲突` | `1 1 0 0` | `怎例` | `962 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/examples/worked-example.md+用例3｜负触发历史戏剧格式当通则` | `1 1 0 0` | `怎适` | `1130 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/examples/worked-example.md+用例4｜s0的否决演示本轮新增历史版本没有` | `1 1 0 0` | `规怎` | `876 / — / — / —` | `UNALIGNED?` |
| `K3` | `1 1 0 0` | `∅` | `226 / 179 / — / —` | `UNALIGNED?` |
| `K4` | `1 1 0 0` | `∅` | `226 / 643 / — / —` | `UNALIGNED?` |
| `K6` | `1 1 0 0` | `∅` | `226 / 1009 / — / —` | `UNALIGNED?` |
| `K1` | `1 1 0 0` | `∅` | `226 / 255 / — / —` | `UNALIGNED?` |
| `K2` | `1 1 0 0` | `∅` | `226 / 231 / — / —` | `UNALIGNED?` |
| `K5` | `1 1 0 0` | `∅` | `226 / 459 / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/references/conflicts-and-exceptions.md+不适用清单一句话版` | `1 0 0 0` | `∅` | `398 / — / — / —` | `UNALIGNED?` |
| `scene-chapter-design-lab/references/source-index.md+台账回查与来源边界` | `1 0 0 0` | `∅` | `1425 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scene-chapter-design-lab/references/source-index.md+本轮新增证据roundp4final20261030` | `1 0 0 0` | `∅` | `521 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `scene-chapter-design-lab/references/source-index.md+引用与管理边界沿用历史条款未删` | `1 0 0 0` | `怎` | `630 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+0.这是什么` | `1 0 0 0` | `规` | `1215 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+1.触发负触发` | `1 0 0 0` | `∅` | `254 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+触发满足任一` | `1 0 0 0` | `∅` | `839 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+负触发不要用` | `1 0 0 0` | `规怎检` | `1112 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+2.输入权限` | `1 0 0 0` | `规检` | `844 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+3.任务路由` | `1 0 0 0` | `∅` | `1233 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+4.最小工作流3步内开始` | `1 0 0 0` | `∅` | `687 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+5.规则地图18条正文在rules.md` | `1 0 0 0` | `∅` | `1131 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+6.输出合同` | `1 0 0 0` | `∅` | `296 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+7.失败退出` | `1 0 0 0` | `∅` | `1256 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+8.证据边界与验证状态` | `1 0 0 0` | `∅` | `1000 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/SKILL.md+9.文件地图` | `1 0 0 0` | `规检` | `847 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/references/diagnosis.md+诊断输出格式照抄填空` | `1 1 0 0` | `∅` | `409 / — / — / —` | `UNALIGNED?` |
| `AF-01` | `1 0 0 0` | `怎反适` | `1159 / — / — / —` | `MISSING` |
| `AF-02` | `1 1 1 1` | `怎反适` | `1043 / 1312 / 959 / 920` | `BLOCK_LOST` |
| `AF-03` | `1 1 1 1` | `怎反适` | `1143 / 1645 / 1043 / 902` | `BLOCK_LOST` |
| `AF-04` | `1 1 1 1` | `怎反适` | `1058 / 1085 / 828 / 750` | `BLOCK_LOST` |
| `AF-05` | `1 1 1 1` | `怎反适` | `951 / 1301 / 740 / 681` | `BLOCK_LOST` |
| `AF-06` | `1 1 1 1` | `怎反适` | `1150 / 1381 / 300 / 429` | `SHRUNK;BLOCK_LOST` |
| `AF-07` | `1 1 1 1` | `怎反适` | `818 / 1072 / 833 / 660` | `BLOCK_LOST` |
| `AF-08` | `1 1 1 1` | `规怎反检适` | `968 / 1597 / 1211 / 853` | `BLOCK_LOST` |
| `AF-09` | `1 0 0 0` | `怎反适` | `876 / — / — / —` | `MISSING` |
| `AF-10` | `1 1 1 1` | `怎反适` | `869 / 1000 / 952 / 561` | `SHRUNK;BLOCK_LOST` |
| `AF-11` | `1 1 1 1` | `怎反适` | `834 / 1309 / 793 / 737` | `BLOCK_LOST` |
| `AF-12` | `1 0 1 1` | `怎反适` | `806 / — / 933 / 573` | `BLOCK_LOST` |
| `AF-13` | `1 1 1 1` | `怎反适` | `1031 / 1459 / 300 / 429` | `SHRUNK;BLOCK_LOST` |
| `AF-14` | `1 1 1 1` | `规怎反适` | `982 / 1349 / 1771 / 754` | `BLOCK_LOST` |
| `AF-15` | `1 0 0 0` | `怎例反适` | `1135 / — / — / —` | `MISSING` |
| `AF-16` | `1 1 1 1` | `怎反适` | `828 / 1190 / 896 / 517` | `SHRUNK;BLOCK_LOST` |
| `AF-17` | `1 0 1 1` | `规怎反适` | `974 / — / 1018 / 548` | `SHRUNK;BLOCK_LOST` |
| `AF-18` | `1 1 1 1` | `怎反适` | `832 / 1625 / 1162 / 600` | `BLOCK_LOST` |
| `action-fight-scene-craft/references/rules.md+硬排除任何规则的可执行部分都不许包含` | `1 0 0 0` | `∅` | `767 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/references/scope-and-conflicts.md+1.证据边界超出即标hnotproven` | `1 1 0 0` | `∅` | `1104 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/references/scope-and-conflicts.md+2.六组未决冲突保留不伪造共识` | `1 0 0 0` | `∅` | `1984 / — / — / —` | `UNALIGNED?` |
| `P3` | `1 0 0 0` | `∅` | `1501 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/references/scope-and-conflicts.md+4.硬排除红线` | `1 1 0 0` | `∅` | `663 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/references/scope-and-conflicts.md+5.与其他skill的接口不要重复做别人的活` | `1 0 0 0` | `∅` | `488 / — / — / —` | `UNALIGNED?` |
| `PG903` | `1 0 0 0` | `∅` | `3339 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG940` | `1 0 0 0` | `∅` | `3339 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG73` | `1 0 0 0` | `∅` | `3339 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG780` | `1 0 0 0` | `∅` | `4385 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `PG171` | `1 0 0 0` | `∅` | `4385 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `action-fight-scene-craft/references/source-index.md+引文回源方法` | `1 0 0 0` | `∅` | `482 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `AC-10` | `1 1 1 1` | `∅` | `130 / 176 / 182 / 182` | `RENUMBERED?` |
| `AC-04` | `1 1 1 1` | `∅` | `130 / 86 / 76 / 76` | `SHRUNK;RENUMBERED?` |
| `AC-16` | `1 1 0 0` | `∅` | `130 / 709 / — / —` | `MISSING` |
| `AC-08` | `1 1 1 1` | `∅` | `130 / 98 / 193 / 193` | `RENUMBERED?` |
| `AC-17` | `1 1 0 0` | `∅` | `130 / 709 / — / —` | `MISSING` |
| `AC-03` | `1 1 1 1` | `∅` | `130 / 59 / 44 / 44` | `SHRUNK;RENUMBERED?` |
| `AC-05` | `1 1 1 1` | `∅` | `130 / 116 / 110 / 110` | `RENUMBERED?` |
| `AC-09` | `1 1 1 1` | `∅` | `130 / 101 / 133 / 133` | `RENUMBERED?` |
| `AC-12` | `1 1 1 1` | `∅` | `130 / 110 / 176 / 176` | `RENUMBERED?` |
| `AC-18` | `1 1 0 0` | `∅` | `130 / 709 / — / —` | `MISSING` |
| `AC-06` | `1 1 1 1` | `∅` | `130 / 83 / 80 / 80` | `SHRUNK;RENUMBERED?` |
| `AC-15` | `1 1 1 1` | `∅` | `130 / 167 / 747 / 747` | `RENUMBERED?` |
| `AC-01` | `1 1 1 1` | `∅` | `130 / 97 / 97 / 97` | `RENUMBERED?` |
| `AC-13` | `1 1 1 1` | `∅` | `130 / 191 / 747 / 747` | `RENUMBERED?` |
| `AC-11` | `1 1 1 1` | `∅` | `130 / 164 / 146 / 146` | `RENUMBERED?` |
| `AC-07` | `1 1 1 1` | `∅` | `130 / 161 / 173 / 173` | `RENUMBERED?` |
| `AC-02` | `1 1 1 1` | `∅` | `130 / 71 / 64 / 64` | `SHRUNK;RENUMBERED?` |
| `AC-14` | `1 1 1 1` | `∅` | `130 / 170 / 747 / 747` | `RENUMBERED?` |
| `action-fight-scene-craft/templates/action-checklist.md+a组开工前9项` | `1 1 0 0` | `∅` | `857 / — / — / —` | `UNALIGNED?` |
| `action-fight-scene-craft/templates/action-checklist.md+b组写完后6项` | `1 1 0 0` | `∅` | `665 / — / — / —` | `UNALIGNED?` |

## 如实记录

- 无法按编号/标题对齐的单元记 `UNALIGNED?`，**不记 MISSING**；来源类文件记 `SOURCE_ONLY`。不伪造对齐行、不跳过。
- 本表只出信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。
