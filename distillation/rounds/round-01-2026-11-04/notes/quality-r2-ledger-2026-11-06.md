# W4-r2 质量收口总账（2026-11-06，主代理 Owner）

- 触发：作者「继续质量收口」。上一轮已把机械收口序列做完（`checklist.md §八十四` 状态＝出口（静态交付）），本轮处理**质量口径**的未闭合项。
- 依据：计划 22.4 第 5 项（D3-C，独立回读由另派只读子代理、Agent 1 只汇总不自审自过）、`notes/k4-reviewer-brief.md`、`skills/knowledge-compiler/references/r18-consumer-operations.md:107-114`（六问判据）、`inputs/requirements.md`。
- 权威绑定（修复后树）：`notes/k5-bindings-2026-11-06.tsv`；整树 `d86672d4497c03b64b3861ef3750a600f82075c56d370219f26fe4d45de8df2c`（217 件／2,361,511 B）；完整说明 `notes/repair-rebinding-2026-11-06.md`。

## 一、本轮目标、验收、范围、非目标、停止条件

| 项 | 内容 |
|---|---|
| 目标 | ① 8 包对修复后树做独立隔离回读，出 GQ1–GQ4 与 B.3 非作者判断；② `field_ids` 冻结判定（W4-09）；③ Q6 六问重取与档位重定；④ 多数 GQ2/GQ3 FAIL 项逐条复议并定性 |
| 验收 | 8 份 W4-r2 回读回执齐（每包 4 项门禁＋附录 B 11 类逐类计数＋B.3 处数）；产量文件可解析；档位变更均有可复现证据；GQ5 全包仍 NOT_PROVEN |
| 范围 | 只写 `notes/quality/`、本总账、`checklist.md`、`log.md`、`notes/delivery-preflight-spec/`；`review.json`（修复前树）**不改写**，W4-r2 结论另立文件 |
| 非目标 | 不改 `output/` 任何字节；不改 `skills/`；不改 `docs/plans/*`；不跑真实任务／测试／构建／宿主加载；不做 git 写操作（无 add/commit/push/reset/checkout/clean）；不把静态落笔写成效果已证 |
| 停止条件 | 出现需作者裁决的产品取舍、范围扩大、或凭据/权限变化即暂停；证据不足时标「未能核实」不臆造 |

## 二、隔离条件（每席必须遵守，违反则该席结论作废）

依据 `notes/k4-reviewer-brief.md` §一。该任务书 §一第 2 条写「不得读 `notes/**`」、§三第 1 条又要求「先读 `notes/quality/<skill>/brief.json` 的四个用例」——**两处冲突，本轮明确例外边界**：

- **允许读**：单个成品包 `output/<skill>/` 全部文件；**仅** `notes/quality/<skill>/brief.json`（只为取四个用例与判据，依 §三）。
- **禁止读**：其他 `notes/**`（总账、分片 ledger、队列、其他席记录、旧 `review.json` 及其档位、desourcing-ledger、operations-contract、delivery-preflight-spec）、`inputs/**`、`distillation/requirements.md`、`docs/plans/**`、`log.md`、`checklist.md`、`scratchpad/**`；`git show` 与任何 v0–v3 提交内容一律禁用。
- **禁止写盘**：只交问题清单（消息返回），不产出对成品的修改，不代改。
- **禁止**跑测试／构建／宿主／真实任务；验证权限＝static；`grep` 统一 `/usr/bin/grep -rnE`。
- 席位**不得预置判过结论**：判据须由本席独立写成可核验清单并冻结再执行；不得沿用主代理或旧 review 的措辞直接判过。

## 三、档位口径（写死）

- 三档：`FAIL`（实测失败，须给可复现命令与输出）／`STATIC_CHECKED`（只做静态检查）／`NOT_PROVEN`（无独立回执）。
- **GQ5 恒 `NOT_PROVEN`**（真实任务测试未授权），任何静态通过不等于效果已证。
- 档位词只写在 W4-r2 产量文件与 notes，**不进成品**。
- 「主据消解」不等于「通过」：FAIL 项须逐条给出「事实层是否仍成立／是否需作者裁决／建议档位」，主代理不降门槛造绿。

## 四、席位分工（8 包 × 1 席，≤3 并发分批；另有 2 个专项席）

| 批 | 席 | 对象 | 产量 |
|---|---|---|---|
| 1 | Q1 | character-and-narrative-control | 消息回执（不落盘） |
| 1 | Q2 | scene-conflict-and-rhythm | 消息回执 |
| 1 | Q3 | story-architecture-and-longform-planning | 消息回执 |
| 2 | Q4 | cross-media-drama-adaptation | 消息回执 |
| 2 | Q5 | fiction-planning-and-diagnosis | 消息回执 |
| 2 | Q6 | preset-card-generation | 消息回执 |
| 3 | Q7 | line-editing-and-proofreading | 消息回执 |
| 3 | Q8 | genre-fiction-craft | 消息回执 |
| 3 | QF | `field_ids` 独立判定（允许读 `inputs/requirements.md` 与 `delivery-preflight-spec/`） | `notes/quality/field-ids-verdict-2026-11-06.md` |
| 4 | QQ | Q6 六问重取与档位建议（独立复核，非作者） | `notes/quality/q6-verdict-2026-11-06.md` |

主代理按回执统一写 `notes/quality/review-r2-2026-11-06.md`（汇总，不覆盖 8 份旧 `review.json`），并销账。

## 五、与上一轮裁定的关系

上一轮主代理裁定「8 份 `review.json` 逐字节不动」（`repair-rebinding-2026-11-06.md §三`），理由：它们绑定修复前树、是 `review-independent-r1` 非作者独立复核件，作者侧改写会把未复核的新树写成通过。**本轮不改变该裁定**：W4-r2 是另派的独立回读，结论另立 `review-r2-2026-11-06.md`，旧 8 份保留为修复前树的历史证据。两者各自标明所绑树，避免双权威。

## 六、进度

- 2026-11-06 17:5x：判据取证完成（22.4 第 5 项、R18 六问、K4 任务书、spec.json 结构）；本总账落盘；开始分批派席。
- 2026-11-06 18:0x：第 1 批 Q1/Q2/Q3 三席回执齐，均遵守隔离条件、未写盘、GQ5 恒 NOT_PROVEN。三席四项门禁均记 `STATIC_CHECKED`，附录 B 真违规均 0，B.3 相符项均 0。**但三席都列出修复批引入的新不一致**（明细见 §八），说明「静态检查」不等于「无缺陷」——档位与发现之间有张力，主代理汇总时不得把 `STATIC_CHECKED` 读成「通过」。
- 收口序列见 §七（派完席位后逐项销账）。
- 2026-11-06 18:1x–18:3x：第 2 批 Q4/Q5/Q6 回执齐（档位与发现见 §九；Q4 的 GQ4 FAIL 系隔离下自拟判据，后经主代理裁定不采信）。
- 2026-11-06 18:2x–18:4x：第 3 批 Q7/Q8/QF 回执齐；QF 产量 `field-ids-verdict-2026-11-06.md` 落盘，**W4-09 判「不能冻结」**（A46/B3/C50＋DR 同名异指）。
- 2026-11-06 18:4x–18:5x：第 4 批 QQ 回执齐，`q6-verdict-2026-11-06.md` 落盘；Q6 档位重定 `NOT_PROVEN` 写入 genre 合同 §三；`review-r2-2026-11-06.md` 汇总落盘。
- 2026-11-06 18:5x：席位全部回传后、收官簿记前被叫停（停止派发与写入）；三件簿记缺口经作者授权 **①+②** 后由主代理补齐，销账见 §七。

## 八、W4-r2 第 1 批发现（Q1/Q2/Q3，照录，均为修复批新引入）

| 席／包 | 具体发现（文件:行） | 性质 |
|---|---|---|
| Q1 character | `SKILL.md:270`「设计假设→未能核实」与 `:275`「设计方案→依据」同一情形相反落位；五档首档三名（`:105`／`boundaries-and-ethics.md:87`／`:275`）；`:153` PV-09 操作卡承载「登记归 genre」治理句 | 修复批引入的口径冲突 |
| Q1 character | `boundaries-and-ethics.md:95-97` 新增 §6 现实求助指引，`SKILL.md:237` 出口列与 §9.2 表均未登记 ⇒ 新增内容不可从 SKILL.md 到达（违反 C.3） | 修复批引入的可达性缺口 |
| Q1 character | `pov-cases.md:110/111/136/138` 状态值改「依据」与 `:96/:134` 表头列名「依据」重名 | 修复批引入的列名／值混淆 |
| Q1 character | GQ3：7 兄弟中仅 `fiction-planning/SKILL.md:48` 点名接收「从本包转入」；余 6 家仅转出行或规矩句；与 `SKILL.md:318`「B 都要说接收什么」单向缺失 | 既有＋修复批残留 |
| Q2 scene | `SKILL.md:275` 新增「无授权不写文件」行，但 `rhythm-diagnosis.md §7` 仍 7 条、§10 为 10 条，两表行数不等 | 修复批引入的不同步 |
| Q2 scene | `chapter-ends-and-endings.md:9`「场、章、幕」与归一后单元（`SKILL.md:177`／`intensity:28` 全篇｜章｜场景）交集仅「章」；`scene-units.md:73/82` 把「幕」列为不必守却仍在值域 | 既有（R2 已登记移交），本轮实测确认仍冲突 |
| Q2 scene | `setup-and-payoff.md:47-60` SU-07 八字段齐，`SKILL.md:224` 只列 5 项；`examples/scene-cases.md:111` 跨章重排主责不明 | 修复批引入的入口层不同步 |
| Q3 story | `SKILL.md:403-412` §12 四词表与包内状态词不一致：`templates/serial-tables.md:133`「已确认／待作者决定／不适用」、`:3`「假设／未读／未知」；全包计数 已确认1／不适用21／假设52／未读21／未知48／待登记1 | 修复批引入的上浮表未覆盖既有填值面 |
| Q3 story | `references/serial-platform-migration.md:52` 改指针后悬空：`:5`「标不适用」＋`:41-50` 状态栏，§12 无「不适用」；`:44`「依据位置＝合同／官方说明／账号后台」与 `SKILL.md:410`「依据＝稿件内可核位置」口径不一；§12 同名异指（`:325`／`serial-rules.md:27`／`serial-open-lines-and-continuity.md:41` 指的是 `serial-tables.md` 第 12 节） | 修复批引入的悬空引用与同名异指 |
| Q3 story | `SKILL.md §7` 仍有 8 处「同上」未处理（`:322/:323/:324/:325/:326/:328/:329/:330`）；§10 四行 `:384/:386/:387/:388` 已改独立句且**四句在目标文件里均实测存在** | 第 4 号裁决只授权 §10 四行，§7 属范围外，如实登记 |

三席 `EXTERNAL_NOTES_REFERENCE` 共 3 组：宿主输出格式／工具授权清单、对端接收字段细则、外部核实资料与执行方；B.3 因 `inputs/**` 禁读，与包外来源比对**未能核实**（不臆造）。

## 九、W4-r2 第 2 批发现（Q4/Q5/Q6）

| 席／包 | 档位（席位自报） | 具体发现 |
|---|---|---|
| Q4 cross-media | GQ1 `NOT_PROVEN`／GQ2·GQ3 `STATIC_CHECKED`／**GQ4 `FAIL`**／GQ5 `NOT_PROVEN` | `templates/interactive-branch-sheet.md:39` 称可填「未知」但 `:41` 四值表头无「未知」（冲突未消）；`SKILL.md:201`「检查已执行」vs `:204`「未执行归未能核实」vs `references/interactive-adaptation.md:54` 口径不齐；`conflicts.md:42` 仍「请导演或作者选择」而 `SKILL.md:202/:212` 只认作者；现树 897 行（brief 记 236/91）⇒ 锚失效；四词权威定义表实测 1 份（`SKILL.md:197-202`） |
| Q5 fiction-planning | GQ1–GQ4 `STATIC_CHECKED`／GQ5 `NOT_PROVEN` | **`SKILL.md:219` 单方写「题材契约由 genre 登记」，对端 `genre-fiction-craft/SKILL.md:17` 全篇「题材契约／登记」0 命中 ⇒ #10A 互认不成立**；且「缺项回本包登记」成第二登记处；`rules-revision-and-method.md:178` 七字段与「怎么做」`:171-177` 不对齐（分支／可信度无产出步）；`SKILL.md:117`「三个删减方案」未定义、与 `:120`「四方案」切换无句；`SKILL.md:331` 自陈「没有对应的外部 Owner」 |
| Q6 preset-card | GQ1·GQ2 `STATIC_CHECKED`／**GQ3 `FAIL`**／GQ4 `NOT_PROVEN`／GQ5 `NOT_PROVEN` | `SKILL.md:202`「B 都要说接收」，但 `genre/SKILL.md` 只有 `:3/:30` 转出、**0 接收行**（单向缺 genre）；`references/expression.md:95/:96` 改名仅 2 行，`style.md:101`／`progression.md:125`／`SKILL.md:118` 仍裸「正文」（双义残留）；字数带实测：含 md 619／614 在 600-750，剔 md 后 594／589 **跌出带外**，与 R6 席报告的 607 不一致；`SKILL.md:169`「标待作者决定」与 `:172`「按最小改动处理」互斥 |

三席附录 B 真违规：Q5＝0、Q6＝0（自拟近似，标 `NOT_PROVEN`）；Q4 自报 2。B.3 相符项均 0，与包外来源比对均「未能核实」。

### 主代理裁定 1：Q4 的 GQ4 `FAIL` 不予采信

Q4 在隔离条件下**禁读附录 B 原文**，遂自行冻结 C01–C11 正则，并把 `SKILL.md:221`／`:227` 的「套件合同」判为 C02 真违规。核查：「套件合同」是本套件内部的公开契约名，不属附录 B 11 类（书名号／作者名／来源编号／年代篇数／空括号／审计词／禁用词等）任何一类；席 B 上一轮按**权威 11 类原文**复扫 8 包得「可见范围零新增违规」，且 8 份修复分片 ledger 的禁词专项均 0。⇒ Q4 该 `FAIL` 来自**自拟判据误伤**，登记为「席位判据与权威附录 B 不一致，不予采信」，不改成品、不改 GQ4 档位。Q4 其余发现（branch-sheet 冲突、导演 vs 作者、锚失效）照录有效。

### 主代理裁定 2：#10A 是单侧落地，属新发现的结构性缺口

Q1（character `:153` 治理句入操作卡）、Q5（fp `:219` 单方指派、对端 0 命中）、Q6（preset-card 单向缺 genre 接收）三席独立指向同一事实：**作者裁决 #10A「题材契约归 genre」只在 fp／character 侧改了措辞，`genre` 侧没有建立对应的登记 Owner 与承接行**。R8 席上一轮报「genre:17 确主张职责、互认成立」，但 Q5 实测 `genre/SKILL.md` 全篇「题材契约／登记」0 命中——两者结论冲突，须由第 3 批 Q8（genre 独立回读）实测核定。本项属**成品语义缺口**，修复需改 `output/`，超出本轮「只写 notes」范围，登记交作者裁决，不擅自落笔。

## 七、收口序列（逐项销账，派完再勾）

1. [x] 8 席 W4-r2 独立回读回执齐（Q1–Q8 汇总于 `review-r2-2026-11-06.md` §一；Q4 GQ4 FAIL 经裁定不采信，见 §二/§八）
2. [x] `field_ids` 判定完成＝**判「不能冻结」**，W4-09 保持未冻结不销账（`field-ids-verdict-2026-11-06.md`，非作者席）
3. [x] Q6 档位重定 `FAIL`→`NOT_PROVEN`（QQ 席 `q6-verdict-2026-11-06.md`；已写入 genre 合同 §三，判据原文未改、缺口仍挂账）
4. [x] GQ2/GQ3 FAIL 项逐条复议定性（`review-r2-2026-11-06.md` §五 三类：消解／需作者裁／修复批新引入；需裁清单待呈作者）
5. [x] `review-r2-2026-11-06.md` 汇总落盘；旧 8 份 review 逐字节未动
6. [x] `checklist.md` 追加 §八十五、`log.md` 收官行、本总账销账（2026-11-06 主代理补记，作者授权①+②后执行）
7. [x] GQ5 全包维持 NOT_PROVEN（本轮全程）；静态复核三项由主代理独立复测：整树 `d86672d4…`/217 件/2,361,511 B 与冻结值全等、28 份 notes JSON 可解析 0 损坏、HEAD `ed22434` 无 git 写操作

**销账后状态**：本轮判定类工作全部收账。遗留＝①修复批 20+ 条新不一致与 #10A genre 侧落地（作者已授权 r3，改 `output/` 后触发重绑与 W4-r3 回读）；②需作者再裁项清单；③`field_ids` C 类 50 个与 DR 命名空间；④GQ5 待真实任务测试授权。
