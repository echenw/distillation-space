# K1 返工 raw 表（r2）· line-editing-and-proofreading

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
- 谱系 v0 来源：`style-refinement-and-proofreading`

**规则单元数 90；v3 对齐成功 53（58.9%）；对齐失败 UNALIGNED? 37（41.1%）**
**flag 计数**：RENUMBERED?=37；SOURCE_ONLY=6；UNALIGNED?=37；—=16

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `style-refinement-and-proofreading/SKILL.md+1.什么时候用` | `1 0 1 1` | `怎检` | `767 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+2.使用方式` | `1 0 1 1` | `∅` | `449 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+3.先定三件事第0轮` | `1 0 1 1` | `∅` | `689 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+4.按层次修改第1–6轮` | `1 0 1 1` | `∅` | `935 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+5.核心规则` | `1 0 1 1` | `∅` | `5321 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+6.英文稿` | `1 0 1 1` | `∅` | `928 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+7.参考文件` | `1 0 1 1` | `∅` | `838 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+8.交付` | `1 0 1 1` | `∅` | `659 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/SKILL.md+9.来源与可信度` | `1 0 1 0` | `规检` | `419 / — / — / —` | `UNALIGNED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+例一中文小说片段精修` | `1 0 1 1` | `∅` | `0 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+输入` | `1 0 1 1` | `∅` | `584 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+第0轮定范围` | `1 0 1 1` | `∅` | `178 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+修改按层次` | `1 0 1 1` | `∅` | `1538 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+改好的文本` | `1 0 1 1` | `∅` | `868 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+例二英文说明文只做机械校对` | `1 0 1 1` | `∅` | `0 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/examples/worked-example.md+判断` | `1 0 1 1` | `∅` | `731 / — / — / —` | `RENUMBERED?` |
| `C01` | `1 1 0 0` | `怎反` | `1171 / 1299 / — / —` | `UNALIGNED?` |
| `C02` | `1 1 0 0` | `例反` | `1389 / 1368 / — / —` | `UNALIGNED?` |
| `C03` | `1 1 0 0` | `规例反` | `1231 / 1267 / — / —` | `UNALIGNED?` |
| `C04` | `1 1 0 0` | `反` | `1048 / 1308 / — / —` | `UNALIGNED?` |
| `C05` | `1 1 0 0` | `反适` | `1090 / 1116 / — / —` | `UNALIGNED?` |
| `C06` | `1 1 0 0` | `规反` | `1114 / 1225 / — / —` | `UNALIGNED?` |
| `C07` | `1 1 0 0` | `规反` | `913 / 988 / — / —` | `UNALIGNED?` |
| `C08` | `1 1 0 0` | `反` | `953 / 985 / — / —` | `UNALIGNED?` |
| `C09` | `1 1 0 0` | `规反` | `1144 / 1170 / — / —` | `UNALIGNED?` |
| `C10` | `1 1 0 0` | `反检` | `1269 / 1364 / — / —` | `UNALIGNED?` |
| `C20` | `1 1 0 0` | `反` | `1080 / 1095 / — / —` | `UNALIGNED?` |
| `C21` | `1 1 0 0` | `规反适` | `1084 / 1139 / — / —` | `UNALIGNED?` |
| `C22` | `1 1 0 0` | `规反` | `1504 / 1695 / — / —` | `UNALIGNED?` |
| `C23` | `1 1 0 0` | `例反` | `961 / 965 / — / —` | `UNALIGNED?` |
| `C24` | `1 1 0 0` | `反` | `1007 / 1055 / — / —` | `UNALIGNED?` |
| `C11` | `1 1 0 0` | `规例反` | `1426 / 1451 / — / —` | `UNALIGNED?` |
| `C12` | `1 1 0 0` | `规反` | `1320 / 1369 / — / —` | `UNALIGNED?` |
| `C13` | `1 1 0 0` | `规反适` | `1648 / 1707 / — / —` | `UNALIGNED?` |
| `C14` | `1 1 0 0` | `反` | `1221 / 1224 / — / —` | `UNALIGNED?` |
| `C15` | `1 1 0 0` | `规反` | `1198 / 1207 / — / —` | `UNALIGNED?` |
| `C16` | `1 1 0 0` | `例反` | `1386 / 1301 / — / —` | `UNALIGNED?` |
| `C17` | `1 1 0 0` | `反` | `1054 / 1108 / — / —` | `UNALIGNED?` |
| `C18` | `1 1 0 0` | `反` | `1239 / 1175 / — / —` | `UNALIGNED?` |
| `C19` | `1 1 0 0` | `反` | `961 / 937 / — / —` | `UNALIGNED?` |
| `C25` | `1 1 0 0` | `反` | `1083 / 1119 / — / —` | `UNALIGNED?` |
| `C26` | `1 1 0 0` | `例反` | `1222 / 1276 / — / —` | `UNALIGNED?` |
| `C27` | `1 1 0 0` | `反` | `1372 / 1336 / — / —` | `UNALIGNED?` |
| `C28` | `1 1 0 0` | `反` | `1186 / 1120 / — / —` | `UNALIGNED?` |
| `C29` | `1 1 0 0` | `怎反适` | `2638 / 2738 / — / —` | `UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+1.来源` | `1 0 0 0` | `∅` | `1495 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+2.英文规则卡行号c01–c29` | `1 0 0 0` | `∅` | `2756 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+3.中文规则与英文规则卡的对应` | `1 0 0 0` | `∅` | `1322 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+4.不采纳为规则的常见误读` | `1 0 0 0` | `∅` | `1844 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+5.书里两说并存的地方` | `1 0 0 0` | `∅` | `524 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/source-index.md+6.本skill不声称什么` | `1 0 0 0` | `规怎检` | `331 / — / — / —` | `SOURCE_ONLY;UNALIGNED?` |
| `style-refinement-and-proofreading/references/workflow.md+总则` | `1 0 1 1` | `∅` | `764 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第0轮定范围建台账` | `1 0 1 1` | `∅` | `754 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第1轮段落` | `1 0 1 1` | `∅` | `360 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第2轮句子骨架` | `1 0 1 1` | `∅` | `592 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第3轮强调与节奏` | `1 0 1 1` | `∅` | `244 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第4轮简洁与用词` | `1 0 1 1` | `∅` | `494 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第5轮机械校对` | `1 0 1 1` | `∅` | `434 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+第6轮誊清与复核` | `1 0 1 1` | `∅` | `391 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+冲突裁决` | `1 0 1 1` | `∅` | `890 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/workflow.md+停手情形` | `1 0 1 1` | `∅` | `1178 / — / — / —` | `RENUMBERED?` |
| `SR-15` | `1 0 1 1` | `∅` | `683 / — / 0 / 0` | `—` |
| `SR-13` | `1 0 1 1` | `∅` | `683 / — / 0 / 0` | `—` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+全角与半角` | `1 0 1 1` | `∅` | `282 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+引号` | `1 0 1 1` | `∅` | `445 / — / — / —` | `RENUMBERED?` |
| `SR-14` | `1 0 1 1` | `∅` | `1027 / — / 1027 / 1027` | `—` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+省略号与破折号` | `1 0 1 1` | `∅` | `624 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+顿号逗号分号` | `1 0 1 1` | `∅` | `502 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+问号与叹号` | `1 0 1 1` | `∅` | `325 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+书名号间隔号括号连接号` | `1 0 1 1` | `∅` | `689 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+的地得` | `1 0 1 1` | `∅` | `504 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+数字` | `1 0 1 1` | `∅` | `825 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+常见错别字与易混词` | `1 0 1 1` | `∅` | `2206 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+异形词` | `1 0 1 1` | `∅` | `416 / — / — / —` | `RENUMBERED?` |
| `style-refinement-and-proofreading/references/zh-mechanics.md+全稿体例表` | `1 0 1 1` | `∅` | `736 / — / — / —` | `RENUMBERED?` |
| `SR-16` | `1 0 1 1` | `∅` | `459 / — / 440 / 440` | `—` |
| `SR-01` | `1 0 1 1` | `∅` | `459 / — / 912 / 995` | `—` |
| `SR-12` | `1 0 1 1` | `∅` | `459 / — / 1507 / 1507` | `—` |
| `style-refinement-and-proofreading/references/zh-sentence-and-wording.md+判断声口的三个问题` | `1 0 1 1` | `∅` | `374 / — / — / —` | `RENUMBERED?` |
| `SR-02` | `1 0 1 1` | `怎例适` | `468 / — / 470 / 488` | `—` |
| `SR-03` | `1 0 1 1` | `怎例适` | `816 / — / 818 / 818` | `—` |
| `SR-04` | `1 0 1 1` | `怎例检适` | `765 / — / 765 / 765` | `—` |
| `SR-05` | `1 0 1 1` | `怎例适` | `876 / — / 878 / 1202` | `—` |
| `SR-06` | `1 0 1 1` | `怎例检适` | `965 / — / 996 / 925` | `—` |
| `SR-07` | `1 0 1 1` | `怎例适` | `733 / — / 751 / 802` | `—` |
| `SR-08` | `1 0 1 1` | `怎例适` | `666 / — / 668 / 720` | `—` |
| `SR-09` | `1 0 1 1` | `怎例适` | `417 / — / 419 / 437` | `—` |
| `SR-10` | `1 0 1 1` | `怎例反检适` | `948 / — / 952 / 997` | `—` |
| `SR-11` | `1 0 1 1` | `怎例适` | `792 / — / 794 / 815` | `—` |
| `style-refinement-and-proofreading/references/zh-sentence-and-wording.md+中文没有直接对应的strunk规则` | `1 0 1 0` | `怎例检` | `456 / — / — / —` | `UNALIGNED?` |

## 如实记录

- 无法按编号/标题对齐的单元记 `UNALIGNED?`，**不记 MISSING**；来源类文件记 `SOURCE_ONLY`。不伪造对齐行、不跳过。
- 本表只出信号，不做逐条「恢复/不恢复」决定；逐条核定归 W3 定向精读。
