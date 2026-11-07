# S06c 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S06c（fiction-planning：v0 `reader-experience-and-critique` 全 7 文件＋`research-fact-verification` 全 9 文件）｜代理：Agent 4（S06c 段子代理）｜轮次：W3 主体轮第 6 批｜日期：2026-11-05
- 范围：`output/fiction-planning-and-diagnosis/` 全部 27 个文件。本片改写其中 **1 个**：`references/research-and-verification.md`（三处：§4.1 一句、§7.2 加一行、文末新增 §10）。其余 26 个为 a1 已修 5 文件（SKILL.md＋四个 rules-*）、a2 落点 4 个（diagnosis、drafting、planning、examples/planning-cases）、a3 落点 7 个（revision、scope-and-conflicts、rule-examples、templates×4）、S06b 落点 6 个（self-check-*×6；其中 self-check-modern-and-zh/self-check-character/self-check-contract 在本片收尾时已见并行改动）与基线文件（examples/self-check-cases），命中如实按归属登记，本片未改动（与基线比对：本片开工时 3 个落点文件中 reader-feedback 与 research-and-feedback-cases 全程未改，research-and-verification 仅含本片三处改动）。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 66 条命中；本片落点 3 文件的 23 条命中全部判允许、零违规**（#4 ×2 与 #8 ×3 为事实核验语境，B.2 第 5 条；#10 ×18 为「证据/依据/意见/数据」类误报）；其余 43 条按归属登记为已判分片或待对应分片。改写前本片文件仅 1 处正则查不出的悬空指涉（research §4.1「历史例文」），已清除并复扫归零。

## 一、全 11 类复扫计数（最终，本片改写后）

| # | 目标 | 全包命中 | 本片 3 文件 | 其余 24 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | 0 | 0 | 0 |
| 3 | 来源数量与年代 | **0** | 0 | 0（a3 记录的 self-check-modern-and-zh:32 唯一命中已由 S06b 并行修复，本片复扫确认闭环） |
| 4 | 指向学习材料的说法 | **3** | 2（research:121/:142） | 1（self-check-character:55「超出自己」子串误报＝S06b） |
| 5a | 作家/大师类词 | **13** | 0 | 13（rules-revision ×6、SKILL:215＝a1 已判；planning:305、diagnosis:364＝a2 自检；scope:140、rule-examples:151–153＝a3 已判） |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 0 | 0 | 0 |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | **7** | 3（research:48/:52/:192） | 4（revision:151＝a3 已判；self-check-contract:91＝S06b；SKILL:330/:340「文本版本」子串误报＝a1 已判） |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | **0** | 0 | 0（「未证实」附加扫亦零命中；a1/a2/a3 移交的 5 处「未证实」均已在各自分片收敛） |
| 10 | 删除后的残迹 | **43** | 18（research 15＋reader-feedback 3） | 25（SKILL ×5、rules-premise ×3、rules-revision ×3＝a1；diagnosis ×4、planning-cases ×1＝a2；revision ×1、scope ×1、rule-examples ×3、revision-sheet ×1＝a3；self-check-character/contract/language 各 1＝S06b） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 |

合计 66 条（3+13+7+43）。改写前本片 3 文件的命中形态与改写后一致（本片改动未新增任何命中，见二节逐条核对）；改写前 research §4.1 另有 1 处 B.3 类悬空指涉（「历史例文」），正则查不出，已清除（LI-FP-228）。

## 二、本片 3 文件命中逐条判断（23 条，全部允许）

### #4（2 条，事实核验语境）

| 位置 | 原句要点 | 判断 |
|---|---|---|
| `research-and-verification.md:121`（RS-06 不查的后果） | 「一句『原文说』若**出自**意译本或两层转译，只支持到译者的理解」 | 允许。「出自」指引语出自用户要核的译本（RS-06 著录层级方法本体），非指学习材料；合同 B.2 第 5 条事实核验场景。 |
| `research-and-verification.md:142`（RS-09 怎么查） | 「原型属实和情节虚构可以出现在同一个来源里，不因为原型被证实，就把**书里**的情节一并认证」 | 允许。「书里」指被核作品内的情节（RS-09 原型与虚构拆分方法本体），非指学习材料；B.2 第 5 条。 |

### #8（3 条，事实核验语境）

| 位置 | 原句要点 | 判断 |
|---|---|---|
| `research-and-verification.md:48`（§4.2） | 「先记正式发布的日期、**更正**记录、版本和原文定位」 | 允许。「更正记录」指被核资料自身的发布更正，核验方法本体；#8 目标是包的改动痕迹自述，此处为核验对象语境（B.2 第 5 条方向）。 |
| `research-and-verification.md:52`（§4.6） | 「处理**更正**和版本差异……**旧版**和**新版**分别留定位」 | 允许。同上——被核资料的更正与两版并列是核验核心动作（§7.1.1 同口径）。 |
| `research-and-verification.md:192`（§7.1.4） | 「底稿被**更正**过时，记下**更正**的链条」 | 允许。同上。 |

### #10（18 条，`据[，。；]`／`见[，。；]` 类误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `research-and-verification.md:34` | 据， | 「证据，说明时区和历法」 |
| `research-and-verification.md:47` | 据。 | 「专业证据。」 |
| `research-and-verification.md:62` | 据； | 「原始证据；」 |
| `research-and-verification.md:68` | 据。 | 「证据。」 |
| `research-and-verification.md:106` | 据。 | 「各自的证据。」 |
| `research-and-verification.md:113` | 据。 | 「直接证据。」 |
| `research-and-verification.md:114` | 据。 | 「独立的证据。」 |
| `research-and-verification.md:135` | 据。 | 「缺少的证据。」 |
| `research-and-verification.md:136` | 据； | 「独立证据；」 |
| `research-and-verification.md:142` | 据； | 「定案依据；」 |
| `research-and-verification.md:157` | 据； | 「时间和证据；」 |
| `research-and-verification.md:162` | 据， | 「真假的证据，」 |
| `research-and-verification.md:167` | 据， | 「当证据，」 |
| `research-and-verification.md:189` | 据。 | 「同口径的数据。」 |
| `research-and-verification.md:221` | 据， | 「哪项证据，」 |
| `reader-feedback.md:40` | 据。 | 「文本证据。」 |
| `reader-feedback.md:48` | 据。 | 「具体证据。」 |
| `reader-feedback.md:104` | 见， | 「『模拟评审』意见，」 |

全部是完整句、语义通顺的正常词（证据/依据/数据/意见），不是删除来源后悬空的「见／据」；`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式在本片 3 文件零命中。允许。

## 三、B.2 允许情形（本片 3 文件层面）

- **事实核验场景的「来源／出处／引语」**：本片新增 §10 的「支持来源及定位」「来源自陈的证据边界」「引语逐字回查」及全文既有「来源」「出处」均指用户要核验的资料（合同 B.2 第 5 条；派发说明明令不得为躲正则改写）。逐条核对：§10 无一处「来源」指向学习材料或本包来源清单。
- **自建示例年份**：`research-and-feedback-cases.md` Case A「1912 年」——自建示例的虚构设定年份（B.2 第 4 条）；骨架比对通过（见四节）。
- **用户稿件指涉**：`reader-feedback.md` RF-12「原文定位」「评论原句」指用户稿件与用户提供的评论（B.2 第 1 条方向）。
- **核验域结论词形**：§5 六种结论（在声明的范围内核实/有限支持/有争议/被推翻/无法核实/虚构设计）与「无法核对」「待核」为核验与反馈处理的过程标注（对断言与反馈分类），非交付回执状态；交付回执四词在 SKILL.md §9（a1 已改）。已列移交项供 W4 复核（LI 文移交项 2）。

## 四、B.3 人工判断（逐文件回读本片改写的 1 份＋复核 2 份未改落点）

1. **与 v0 来源案例的骨架比对**：本片没有新增自创例（§10 为记录格式，无情节性示例）。对 v3 既有 4 个自建 Case 复核骨架：Case A（公共建筑揭幕/开放年份）与 v0 A4（轮船首航分层）、B2（年报修订）——人物关系无、关键事件异、时代地点异，零项对应；Case B（车站到医院的因果桥）与 v0 示例 A（信件段落矛盾反馈）——关键事件与人物关系均异；Case C（社群问卷偏好）与 v0 A2（助理教授统计）——仅「样本推普遍」方法同型，事件内容异；Case D（职业原型情节虚构）与 v0 A3（原型主张定案）——仅「原型/虚构拆分」方法同型，无具体事件对应。方法同型是改写目的，事件骨架零至一项对应，不触发重写。
2. **具体作品的标志性情节元素**：3 文件复扫书名号零命中、#5b 人名零命中；无具体作品情节元素。
3. **借来源背书的说法**：3 文件回读无「经典做法是……」「很多名作都……」式句子；§4.1 改写后「本 skill 文件里的示例代替不了相应的专业证据」只保留边界判断，无背书；§10 新增文本无程度词与新断言。
4. **删除来源后语义**：§4.1 改写句主语完整（「本 skill 文件里的示例」），「示例不作专业证据」的限定保留；§7.2 新行与既有六行结构、语气一致；§10 与 §9（记录留在中间工作记录）、§6/§8（写回断言表）、RF-12（反馈交付行）四处口径互洽，无重复建表、无悬空引用；§10.1 成果目标一行与 §7.2 新行互相指认一致。
5. **全包辅助复扫**：来源特征词（`L[0-9]{3,5}` 行号、`kd32`、`ledger`、Gutenberg、公版、`source-index`、`version-and-provenance`、`p4-field-guide`、`TRUSTED`、`source_provenance`）全目录零命中；本片无新建文件。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 本片新增文本零命中；research 既有 3 处 #8 判允许（见二节） |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫＋「未证实」附加扫） | 本片 3 文件与全包零命中；§10 交付字段用四词口径（建议句或作者决定／未实际打开／未知） |
| 禁用说法（#11 全模式） | 零命中；草稿中「这批材料」一词已在落笔前改为「本次待核资料」 |
| 四词状态词 | §10 的状态列引 §5 六种结论（核验域）；交付相关字段用「待作者决定」「未知」「未实际打开」；无四词外交付状态 |
| 相对链接 | research-and-verification.md 的 `../SKILL.md`、`self-check-character.md`、`self-check-language.md` 链接 grep 核实在位；§10 为内部节引用（§3/§4/§5/§7.2/§8/§9/RS-10），无新文件链接、无断链 |
| GFM 表格分隔行 | §3/§7.2/§7.3 逐表核对：表头与数据行列数一致、分隔行在位（§7.2 新行 3 列对齐）；无「有数据行缺分隔行」 |
| 写入范围 | 本片仅改 1 个落点文件（3 处）＋新建 2 份 notes（LI/S06c 决策链追加/selfcheck）；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a1/a2/a3 已修文件与 S06b 文件 |
| 模板规范（合同第三节） | §10 逐条断言记录为字段型记录行（无枚举编号 ID），同 RF-12 交付行先例，不属「枚举编号模板」三列规范对象；四张枚举模板的三列规范由 a3 完成，本片复扫确认未破坏 |

## 六、待对应分片处理的登记（非本片文件命中，本片未动）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `SKILL.md`、`rules-premise-and-structure.md`、`rules-revision-and-method.md`（a1 已结片） | #5a ×7、#10 ×11、#8 ×2（「文本版本」子串） | a1 自检已判允许，本片沿用 |
| `references/diagnosis.md`、`references/planning.md`、`examples/planning-cases.md`（a2） | #5a ×2、#10 ×5 | a2 自检（s06a2）已出，按其判读沿用；「大师」两处为通用元规则对象 |
| `references/revision.md`、`references/scope-and-conflicts.md`、`examples/rule-examples.md`、`templates/revision-sheet.md`（a3） | #5a ×4、#8 ×1、#10 ×6 | a3 自检已判允许，本片沿用 |
| `references/self-check-character.md`、`self-check-contract.md`、`self-check-language.md`（S06b） | #4 ×1（「超出自己」子串）、#8 ×1（「旧版本」用户稿件语境）、#10 ×3 | S06b 分片判读；a1/a3 登记口径与本片复扫一致；`self-check-modern-and-zh.md:32` 年代已由 S06b 修复（本片复扫 #3 全包零命中，闭环确认） |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S06c／fiction-planning-and-diagnosis：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/fiction-planning-and-diagnosis/` 全部 27 文件。全包 66 条命中：#1/#2/#3/#5b/#6/#7/#9/#11 零命中；#4=3、#5a=13、#8=7、#10=43。本片落点 3 文件（reader-feedback、research-and-verification、research-and-feedback-cases）命中 23 条，逐条判允许、零违规（#4 ×2 与 #8 ×3 为事实核验语境——被核资料的译本/情节/更正记录，合同 B.2 第 5 条，未为躲正则改写；#10 ×18 为证据/依据/意见/数据类误报）。改写前该 3 文件仅 1 处正则查不出的悬空指涉（research §4.1「历史例文」——v1 指来源历史例文、v3 示例已全为自建），已改「本 skill 文件里的示例」并复扫归零；本片新增 §10 核查记录（范围头/逐条断言记录 13 字段/整体摘要）与 §7.2 成果目标行，为 v0 templates.md 四单元与 C-2 经 v1 工作簿确认的连带删除补回（LI-FP-210/212/214/218/226），新增文本零命中。两个 source-index 与 source-boundaries 按 2.8 节不恢复；source-derived-checks 九行经 r2 flag 与内容双核对判「方法在位」（RS-01–14 全量承接，含 v1 四条修订）；failure-modes 23 条逐条找到承接落点（#1 判 v1 有意放宽）。基线其余 24 文件命中 43 条全部按归属登记（a1 已判 18、a2 已出自检 7、a3 已判 11、S06b 7——其中 self-check-modern-and-zh 的 #3 命中已由 S06b 修复，本片复扫确认 #3 全包归零）。B.3 逐文件回读：无新增自创例、无背书、无残迹、4 个自建 Case 骨架比对通过；相对链接无断链、表格分隔行齐全。**本片落点零违规，可交 W4 独立隔离回读。**
