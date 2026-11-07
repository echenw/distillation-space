# S06b 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S06b（fiction-planning：v0 `fiction-craft-and-language` 全谱系 = 成稿自检线）｜代理：Agent 4（S06b 段子代理）｜轮次：W3 主体轮第 6 批｜日期：2026-11-05
- 范围：`output/fiction-planning-and-diagnosis/` 全部 27 个文件。本片改写其中 **3 个**：`references/self-check-modern-and-zh.md`（清 :32 年代指涉）、`references/self-check-character.md`（改自创例）、`references/self-check-contract.md`（新增 §2.1 定位卡）。其余 4 个本片落点（self-check-diagnosis、self-check-language、self-check-scenes、examples/self-check-cases）与 v3 基线 `2a10c07` 逐字节一致（diff 核验）；其余 17 个文件为 a1/a2/a3 已修落点、S06c 落点与 a 段基线文件，命中如实按归属登记，本片未改动（`git status` 对 `skills/` 零改动）。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 扫描时点说明：全包复扫在 S06b 与并行片 S06c 的落点改写均落盘后执行，计数为**当前合并状态**；S06c 落点（reader-feedback、research-and-verification、examples/research-and-feedback-cases）的逐条判断以其自检 `s06c-desourcing-selfcheck.md` 为准，本记录按归属登记。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 66 条命中；本片落点 7 文件的 5 条命中全部判允许、零违规；其余 61 条按归属登记（a1/a2/a3 已判 30、S06c 落点 31 中的对应条目见其自检）**。必做移交（self-check-modern-and-zh:32「1884 年的出版建议」）已清除，**附录 B #3 在 fiction-planning 全包清零**（三个子模式 27 文件零命中）。

## 一、全 11 类复扫计数（最终，本片改写后、全包合并状态）

| # | 目标 | 全包命中 | 本片 7 文件 | 其余 20 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | 0 | 0 | 0（a1/a2/a3 清残片后维持零命中） |
| 3 | 来源数量与年代 | **0（清零）** | 0 | 0（改写前唯一命中 self-check-modern-and-zh:32，本片已清，见 LI-FP-187/198） |
| 4 | 指向学习材料的说法 | 3 | 1（self-check-character:55「超出自己」子串误报） | 2（research:121/:142＝S06c，事实核验语境，B.2 第 5 条方向） |
| 5a | 作家/大师类词 | 13 | 0 | 13（SKILL:215＝a1；rules-revision ×6＝a1；planning:305、diagnosis:364＝a2；scope:140、rule-examples:151–153＝a3——均为 FC-21 元规则自身对象或被降格主张，a1 selfcheck 第二节判法，判允许） |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 0 | 0 | 0（改写前 character:141「卡夫卡」为中文人名，正则不命中，属 B.3 类残留，本片改自创例清除，见 LI-FP-195） |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | 7 | 1（self-check-contract:91「旧版本」＝用户稿件版本语境，B.2 第 2 条，允许） | 6（SKILL:330/:340「文本版本」子串误报＝a1 已判；revision:151「回退到上一版」＝a3 已判，用户稿件回退；research ×3＝S06c，核验语境） |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 0 | 0 | 0 |
| 10 | 删除后的残迹 | 43 | 3（character:133「判据；」、contract:93「意见。」、language:37「看见，」——正常词误报） | 40（SKILL ×5＝a1；rules-premise ×3、rules-revision-and-method ×3＝a1；revision:185、revision-sheet:27、scope:122、rule-examples ×3＝a3；diagnosis ×4、planning-cases:3＝a2；research ×15、reader-feedback ×3＝S06c） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 |

合计 66 条（3+13+7+43）。附加扫：「未证实」（四词外词形）全包零命中——a1/a2 移交的 5 处收敛项（rules-revision ×3、drafting:320、diagnosis:399）在本片开工复扫时已归零且原位现为「未能核实」四词写法，非本片所改，供 Agent 1 对账；「见F」排版残迹零命中（a3 LI-FP-145 后维持）。空括号 `（\s*）`／`\(\s*\)` 与「与同」子模式全包零命中。

## 二、本片 7 文件命中逐条判断（5 条，全部允许）

### #4（1 条）

| 位置 | 原句 | 判断 |
|---|---|---|
| `self-check-character.md:55` | 「也不要因为“没有亲历”就把超出自己生活的材料都删掉」 | 允许。#4 命中系「**出自**」子串误报（超**出自**己），句义是作者自己的生活材料（用户创作语境），与学习材料无关；a1 selfcheck 第六节已预判，本片复核确认。 |

### #8（1 条）

| 位置 | 原句 | 判断 |
|---|---|---|
| `self-check-contract.md:91`（本片增定位卡节后由原 :75 下移；文字未改） | 「修改后重新检查当前版本，不继承旧版本的通过结果。」 | 允许。「当前版本／旧版本」指用户稿件的修订版本（B.2 第 2 条方向），非本包改动痕迹自述；a1/a3 selfcheck 已预判此口径。 |

### #10（3 条，`见/据 + 标点` 类误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `self-check-character.md:133` | 据； | 「统一判据；」 |
| `self-check-contract.md:93` | 见。 | 「专业意见。」 |
| `self-check-language.md:37` | 见， | 「读者能看见，」 |

全部是完整句、语义通顺的正常词（判据／意见／看见），不是删除来源后悬空的「见／据」；`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式全包零命中。允许。

## 三、B.2 允许情形（本片 7 文件层面）

- **本包内部编号**：CL-01–14、SU-15/SU-16、PV-12/PV-13、FC-20、RS 卡（self-check 文件内交叉引用）。符合 B.2 第 3 条。
- **用户稿件版本号**：`self-check-contract.md:91`「当前版本／旧版本」。符合 B.2 第 2 条。
- **事实核验语境**：self-check-character §4.3「记下来源」（作者自己的借材台账）、§2 检查表「有没有可复核依据」——指用户要核验的资料与自身研究记录。符合 B.2 第 5 条方向。
- **自创例**：self-check-character §5 新例「能听见旧物件说话的叙述者」（本片改写，无年代、无书名、无作者）；self-check-cases 三例为 v0 编者所写演示（含「明代县衙」朝代设定，无具体作品与作者）。
- **泛化立场短语（B.3 登记）**：self-check-scenes §4.2「故事就是一切」「打动人心靠人物」、§3「每一场都要写完」、self-check-character §3.3「杀了他，埋了他」——v2/v3 有意去名保留的无归属泛化判语，是被拒绝的立场或泛化标准，无书名、无人名、无年代、无背书功能（与 a3 对 scope §3.1 术语保留的登记口径一致）；已列 W4 复核项。

## 四、B.3 人工判断（逐文件回读本片改写的 3 份文件＋核对 4 份未改落点）

1. **与 v0 来源案例的骨架比对**：本片唯一新增自创例（character §5「能听见旧物件说话的叙述者，面对老屋要被拆掉」）。与 v0 来源案例逐一比对——变形记（家庭＋变形失业＋早年城市公寓）、修道院与家庭书例（主人公穿越法国＋风景留背景）、《罗慕拉》（佛罗伦萨＋人物研究）：人物关系、关键事件、时代地点三项均零项对应，不触发重写；「老屋拆迁」与包内自检演示（海边小镇卖老房）也无骨架重合（人物关系、关键事件均不同）。
2. **具体作品的标志性情节元素**：本片 7 文件复扫书名号零命中、#5b 人名零命中；改写前的「卡夫卡的格里高尔」（作者人名＋变虫标志性元素）已清除（LI-FP-195）。「九重天、七大宗门、测灵根」（self-check-cases 例三）为演示用通用玄幻设定，非具体作品元素。
3. **借来源背书的说法**：3 份改写文件回读无「经典做法是……」「很多名作都……」式句子；:32 改写只保留判断方向（手艺／市场两分、不预测市场）并接通 §4.1 落点，未添程度词或新断言；新增定位卡节全部为 v0 §6 原有五字段的恢复改写，无新规则自创。
4. **删除来源后语义**：:32 改写后「手艺项与市场项分开处理（`self-check-contract.md` §4.1）；本 skill 不预测市场」主语完整、表格行结构不变；character §5 例句替换后「（这是本 skill 加的自创例）」与上下文衔接、双审表的「不过时」列语义不受影响；contract §2.1 插入后 §2/§3 之间编号连续（2.1 为 §2 子节）、目录结构无跳号。无主语悬空、无空括号、无表格空列。
5. **悬空引用修复确认**：改写前 self-check-diagnosis:27 与 self-check-character:25 两处「在定位卡上写明」在全包无「定位卡」定义；本片 §2.1 落地后两处引用可解析（回读核实：两处所在文件与本文件同目录，相对可达）。
6. **全包辅助复扫**：来源特征词（行号 `L[0-9]{3,5}`、`kd32`、`ledger`、Gutenberg、公版、`source-index`、`version-and-provenance`、`p4-field-guide`、`TRUSTED`）全目录零命中；无新建文件（`git status` 对 `skills/` 零改动、output 目录文件数仍 27）。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 本片 7 文件除 contract:91（允许，见二节）外零命中；新增 §2.1 无「补回／恢复」类自述措辞 |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 本片 7 文件零命中；「未证实」全包零命中 |
| 禁用说法（#11 全模式＋「硬门」甄别） | 零命中；本片文件无「硬门」用例 |
| 四词状态词 | 本片新增 §2.1 的纪律条写「如实标“未知”或“待作者决定”，不把未知写成已完成」（初稿曾用「待补」词形，落笔时按 a3 模板文件头的四词收敛口径同款修正）；7 文件无其他自造状态词形。备查：a 段已结片文件余 2 处「待补」（diagnosis:14「待补取样」、rule-examples:153 反例字段值），不属本片范围，供 Agent 1 收口时甄别 |
| 相对链接 | 新增 §2.1 的三处交叉引用（`self-check-character.md` §3.1/§4.1、`self-check-diagnosis.md` §1）逐条核实可达（同目录、节号实存）；:32 改写的 `self-check-contract.md` §4.1 核实可达；7 文件与 SKILL.md §6 路由互指无断链、无指向已删除文件（source-index 等）的引用 |
| GFM 表格分隔行 | 新增 §2.1 定位卡表有分隔行（3 列 7 行）；7 文件全部既有表格分隔行齐全（逐表核对） |
| 写入范围 | 本片仅改 3 个落点文件＋新建 3 份 notes（LI 记录、S06b 决策链追加、本 selfcheck）；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a 段已修文件与 S06c 落点文件（S06c 的追加在其节内，编号段 LI-FP-201 起，与本片 151–198 无重叠） |
| 模板规范（合同第三节） | 本片未改四张模板；新增定位卡表非枚举编号模板，仍按规范做到每字段一行、分隔行齐全 |
| r2 覆盖核对 | 本谱系 66 个 r2 单元全部有决定（LI-FP-151–198，相邻小节合并记账的关系在来源位置列写明）；r2 未列的 worked-example 例三与 character:141 残留已作计划外登记 |

## 六、待对应分片处理的登记（非本片文件命中，本片未动）

| 文件（归属分片） | 命中 | 供该分片/收口参考的只读观察 |
|---|---|---|
| `references/research-and-verification.md`、`references/reader-feedback.md`（S06c） | #4 ×2、#8 ×3、#10 ×18 | 均为事实核验语境（B.2 第 5 条方向）与「证据/依据」类误报；S06c 自检 `s06c-desourcing-selfcheck.md` 已逐条判断，本片按其结论登记 |
| `SKILL.md`、`references/rules-*.md`、`references/diagnosis.md`、`references/planning.md`、`references/scope-and-conflicts.md`、`references/revision.md`、`examples/rule-examples.md`、`examples/planning-cases.md`、`templates/revision-sheet.md`（a1/a2/a3 已结片） | #5a ×13、#8 ×4、#10 ×24 | 沿用 a1 selfcheck 第二节（FC-21「大师」判法）、a2、a3 selfcheck 的既有允许判定；本片复扫确认无新增命中 |
| `references/drafting.md`、`references/diagnosis.md`、`references/rules-revision-and-method.md`（a1/a2，四词收敛移交项） | 0（已归零） | a1/a2 移交的 5 处「未证实」在本片开工复扫时已为「未能核实」四词写法，非本片所改；供 Agent 1 对账 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S06b／fiction-planning-and-diagnosis：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/fiction-planning-and-diagnosis/` 全部 27 文件（S06b 与并行片 S06c 改写落盘后的合并状态）。全包 66 条命中：#1/#2/#3/#5b/#6/#7/#9/#11 零命中；#4=3、#5a=13、#8=7、#10=43。本片落点 7 文件（self-check×6＋examples/self-check-cases）命中 5 条，逐条判允许、零违规（「超出自己」子串误报 1、「旧版本」用户稿件版本 1、「判据/意见/看见」正常词误报 3）。**slice-prep §3.1 指名的 self-check-modern-and-zh.md:32「1884 年的出版建议」已清除（改「手艺项与市场项分开处理（self-check-contract §4.1）；本 skill 不预测市场」），附录 B #3 在 fiction-planning 全包 27 文件清零**——至此 2.5 节所列本 skill 年代类残留全部归零。B.3 回读清除 v2/v3 清扫漏网的「卡夫卡的格里高尔」（作者人名＋作品标志性元素，中文人名正则不命中），改自创例（骨架比对零项对应）；按计划 6.6 F-1 恢复 v0 SKILL.md §6 的定位卡五字段（v2 重组时连带丢失、v3 两处悬空引用），落 self-check-contract §2.1（五项一行表＋纪律＋交叉引用），未动 SKILL.md。source-index 四节（SOURCE_ONLY）不恢复，否定式规范落点逐条核实（八条主张中七条已在成品、一条按 P1 第三类排除并列 Agent 1 裁处）。基线其余 20 文件命中 61 条全部按归属登记（a1/a2/a3 已判 30、S06c 落点 31 见其自检）。本片改写 3 文件、4 落点与 v3 基线逐字节一致；相对链接无断链、表格分隔行齐全；`git status` 对 skills/ 零改动。**本片落点零违规，可交 W4 独立隔离回读。**
