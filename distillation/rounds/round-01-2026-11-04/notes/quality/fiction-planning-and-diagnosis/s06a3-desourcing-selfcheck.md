# S06a3 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S06a3（fiction-planning：v0 `fiction-craft` 的 revision / rule-examples / scope-and-conflicts / templates×4 / 来源类两件＋p4-field-guide）｜代理：Agent 4（a3 段子代理）｜轮次：W3 主体轮第 5 批｜日期：2026-11-05
- 范围：`output/fiction-planning-and-diagnosis/` 全部 27 个文件。本片改写其中 **7 个**：`references/revision.md`、`references/scope-and-conflicts.md`、`examples/rule-examples.md`、`templates/novel-plan.md`、`templates/diagnosis-report.md`、`templates/revision-sheet.md`、`templates/scene-plan.md`。其余 20 个为 a1 已修 5 文件（SKILL.md＋四个 rules-*）、a2 并行片落点、S06b/S06c 落点与基线文件，命中如实按归属登记，本片未改动（与 v3 基线 diff 核验：本片开工时 7 个落点文件与 `2a10c07` 逐字节一致，a1/a2 未越界）。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 65 条命中；本片落点 7 文件的 11 条命中全部判允许、零违规；其余 54 条按归属登记为待对应分片/已判分片复核**。三项必做移交（scope 74–76、revision 123/169、scope §3 三处「未证实」）全部清除并复扫归零。

## 一、全 11 类复扫计数（最终，本片改写后）

| # | 目标 | 全包命中 | 本片 7 文件 | 其余 20 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | **0** | 0 | 0（改写前本片文件有 4 处：revision `-1328`/`-3143`、scope `-2236`/`-2111`，已清） |
| 3 | 来源数量与年代 | **1** | 0 | 1（self-check-modern-and-zh:32，S06b；改写前 scope 有 2 处正则命中＋7 处语义年代词，已清） |
| 4 | 指向学习材料的说法 | **3** | 0 | 3（research-and-verification ×2、self-check-character ×1；本片新写说明句曾用「批次」列举词 4 处，按 S01 口径顺手消除归零） |
| 5a | 作家/大师类词 | **13** | 4（scope:140、rule-examples:151/152/153） | 9（rules-revision ×6、SKILL:215＝a1 已判；planning:305、diagnosis:364＝待 a2） |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 0 | 0 | 0 |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | **7** | 1（revision:151「上一版」） | 6（research ×3＝S06c、self-check-contract:75＝S06b、SKILL ×2「文本版本」子串误报＝a1 已判） |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | **0** | 0 | 0（a1 记录的 diagnosis:411 已由 a2 清除，本片复扫确认闭环；改写前本片文件 3 处「未证实」亦已收敛四词） |
| 10 | 删除后的残迹 | **41** | 6（revision:185、scope:122、rule-examples:4/23/47、revision-sheet:27） | 35（research ×15、diagnosis ×4、SKILL ×4、rules-premise ×3、rules-revision ×3、reader-feedback ×3、rule-examples 外的误报见二节、planning-cases ×1、self-check-language ×1、self-check-contract ×1） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 |

合计 65 条（1+3+13+7+41）。附加扫：「未证实」在本片 7 文件零命中（改写前 5 处已收敛）；a1 的 rules-revision-and-method 3 处与 a2 的 drafting:320/diagnosis:399 各 1 处为移交项（见其分片）；「见FC」排版残迹 6 处已修（LI-FP-145），全包「见F」零命中。改写前本片 7 文件的残留合计：`-NNNN` 残片 4、年代说法 9、「标 未证实」3、文件头括注 1、「单来源」3、「见FC」6、模板缺两列 4 表——全部清除或补齐并经本复扫确认。

## 二、本片 7 文件命中逐条判断（11 条，全部允许）

### #5a（4 条，「大师」）

| 位置 | 原句要点 | 判断 |
|---|---|---|
| `scope-and-conflicts.md:140`（§4.4 第 5 条） | 「不把“大师这样做”写成“人人应这样做”；例外登记，不升格」 | 允许。FC-21 元规则自身的处理对象（例外登记机制的外推禁令），不指任何具体人物、无作品名、无背书句；与 a1 selfcheck 第二节对 FC-21 六处的判法一致，SKILL.md:215 同款 a1 已判允许。 |
| `rule-examples.md:151` | 输入：「有人主张“每场都必须有反转”，理由是某大师每场都反转」 | 允许。FC-21 示例中被降格处理的对象主张（该主张随后被判「假设」），泛称无具体人物；a1 移交项指名参考其判法。 |
| `rule-examples.md:152` | 「该主张只有 1 个大师例、无 ≥2 反例」 | 同上，允许。 |
| `rule-examples.md:153` | 「`例外记录=大师例外登记`」 | 同上，允许；同行 `可信度: 低` 为 FC-21 规则卡 `confidence` 字段（规则本体交付块既有，本包内部字段，B.2 第 3 条），非来源证据标记，保留以与规则卡格式一致。 |

### #8（1 条）

| 位置 | 原句 | 判断 |
|---|---|---|
| `revision.md:151` | 「回归项 3 项以上失败 → 回退到上一版」 | 允许。「上一版」指用户稿件版本回退（B.2 第 2 条方向），非改动痕迹自述；a1 selfcheck 第六节已预判此口径。 |

### #10（6 条，`据[，。；]`／`见[，。；]` 类误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `revision.md:185` | 据， | 「证据，不改字」 |
| `scope-and-conflicts.md:122` | 据； | 「历史证据；」 |
| `rule-examples.md:4` | 据； | 「虚构数据；」 |
| `rule-examples.md:23` | 据， | 「判据，」 |
| `rule-examples.md:47` | 据， | 「证据，」 |
| `revision-sheet.md:27` | 据， | 「证据，」 |

全部是完整句、语义通顺的正常词（证据/数据/判据），不是删除来源后悬空的「见／据」；`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式在本片文件零命中。允许。

## 三、B.2 允许情形（本片 7 文件层面）

- **本包内部编号**：FC-01–21、NP-01–14、DR-01–12＋DR-SUM、RV-01–12、SP-01–12、K-01–19、L0–L4（改写级别）。符合 B.2 第 3 条。
- **用户稿件版本号**：`v1→v2`（RV-02/RV-11）、「回退到上一版」（revision:151）、「先复制版本，标 `v1`」（revision §0）。符合 B.2 第 2 条。
- **操作默认数字**：`3–5 必要特征`、`3/4 处`、`8–9 段`、`2–3 reflector`、`40 章/3,000 字`（示例）、`1,000–10,000/50,000 词`（历史约定界线）——均为「默认/非硬门/历史约定」限定的操作值，沿用 a1 对 FC 卡同类数字的判法。允许。
- **演示用虚构年份**：`rule-examples.md` FC-14 输入「1900 年代廉租公寓场景」——演示用虚构设定的历史背景（B.2 第 4 条）；B.3 骨架比对通过（见下节），且不与任何来源案例两项以上对应。允许。
- **否定式规范说明**：四张模板说明中的「不指向任何来源编号或包外路径」「不写“研究支持”」「不得把未知写成已完成」——对成品的规范性禁令，不指向学习材料（「批次」列举词已按 S01 口径顺手消除，消除后语义不变）。允许。
- **术语保留（B.3 登记）**：scope §1/§2 的 `probability`（或然律概念）、`latent`、§3.1 的 `scène à faire` 与「apt/specific/attractive/new/short」——v2/v3 有意保留的叙事学术语（v2→v3 去来源轮清空了同文件的书名、人名、PG 编号、年代，独留这些术语），非原句、非人名书名年代编号，11 类正则不命中；已列移交项供 W4 隔离回读复核。

## 四、B.3 人工判断（逐文件回读本片改写的 7 份文件）

1. **与 v0 来源案例的骨架比对**：本片没有新增自创例。全部改动是（a）删除截断锚点残片 4 处（判断内容均已在句内），（b）年代词泛化为「特定时期/早期/历史」陈述 9 处（a1 同型口径），（c）状态词收敛 5 处，（d）模板加列与说明条，（e）「单来源→操作默认」改名与 NP-09 一致性修复，（f）「见FC」残迹修复。rule-examples 的 21 个演示示例为 v0 编者所写、v3 沿用的虚构数据（夜班护士/电梯困人/姐妹申冤/出租车巧合等），逐个与 v0 rules.md 引用的真实作品案例（Montgomery/Stribling、Hardy、Oedipus 等，a1 已清除）比对：人物关系、关键事件、时代地点三项均无两项以上对应，不触发重写。
2. **具体作品的标志性情节元素**：7 文件复扫书名号零命中、#5b 人名零命中；「侦探不解释、言情无情感落点、升级流无升级」（revision §9.3）是类型承诺的通用举例，非具体作品情节。
3. **借来源背书的说法**：7 文件回读无「经典做法是……」「很多名作都……」式句子；「商业剧场惯例」「历史分类样本」等改写只保留判断方向（历史注、不进规则），未添程度词或新断言；「0 到 20+ 次并存」来源数据删除后以 v1 显式语义（按目标与收益判停）替代，未编造替代数字。
4. **删除来源后语义**：diff 逐处复查（scope 10 处、revision 4 处、rule-examples 2 处、templates 6 处＋6 表行×2 列、文件头 3 处），无主语悬空、无空括号、无表格空列；行 74 改写后「特定历史时期的市场惯例，已过期」主语完整、限定保留；revision:169 改写后与 §7.1 停止规则、§7.3 不重复不矛盾。
5. **全包辅助复扫**：来源特征词（行号 `L[0-9]{3,5}`、`kd32`、`ledger`、Gutenberg、公版、`source-index`、`version-and-provenance`、`p4-field-guide`、`TRUSTED`）全目录零命中；无新建文件。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 本片 7 文件除 revision:151（允许，见二节）外零命中；无「本版补回」类自述 |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 本片 7 文件零命中；「未证实」收敛后本片零命中 |
| 禁用说法（#11 全模式＋「硬门」甄别） | 零命中；「硬门」（revision §11、scope §3 等）不在禁用清单（#11 禁「硬规则」），为「非硬门」限定的组成部分，与 a1 文件口径一致，保留 |
| 四词状态词 | 本片 7 文件的交付状态表述全部为「已完成／依据／未能核实／待作者决定／未知」；模板说明条写明「未知合法、不得把未知写成已完成」；文件头「未定/待补」「未授权」已改四词口径 |
| 相对链接 | 本片 7 文件与 SKILL.md §6 路由互指（revision→diagnosis/planning/revision-sheet、scope→rules 文件、模板→流程文件）逐条 grep 核实，无断链；无指向已删除的 source-index/version-and-provenance/p4-field-guide 的引用 |
| GFM 表格分隔行 | 全包逐表脚本校验：表头与数据行列数差异 0 处；四张模板加列后分隔行同步 6/7 列；无「有数据行缺分隔行」 |
| 写入范围 | 本片仅改 7 个落点文件＋新建 3 份 notes（LI/S06a3 决策链追加/selfcheck）；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a1 已修 5 文件与 a2 落点文件 |
| 模板规范（合同第三节） | 四张模板每个编号独占一行、值/状态/稿件证据位置三列齐全、未知合法、证据位置只指当前稿件、分隔行齐全——逐项对照通过 |

## 六、待对应分片处理的登记（非本片文件命中，本片未动）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `references/rules-revision-and-method.md`（a1 已结片，移交 Agent 1） | 「未证实」×3（:43、:78、:216） | a1 把 v0 `NOT_PROVEN` 替换为「未证实」，四词中无此词形；建议按合同 2.2 收敛为「未能核实」（同本片 revision:177/:199 的改法）。另其 FC-21 交付块的 `confidence` 英文字段与本片 rule-examples:153 的「可信度: 低」对应，如需中文化两处同步 |
| `references/drafting.md`、`references/diagnosis.md`（a2） | 「未证实」×2（drafting:320、diagnosis:399）；#5a ×2（planning:305、diagnosis:364）；#10 ×7 | a2 已清 diagnosis:411 审计词（本片复扫确认闭环）；「未证实」同上四词收敛口径；「大师」两处按 a1 selfcheck 第二节判法 |
| `references/self-check-modern-and-zh.md`（S06b） | #3 ×1（:32「1884 年的出版建议」） | §3.1 指名项；全包 #3 现存唯一命中 |
| `references/self-check-character.md`（S06b） | #4 ×1（:55「超出自己」子串误报） | a1 已预判语义与来源无关 |
| `references/self-check-contract.md`（S06b） | #8 ×1（:75「旧版本」＝用户稿件版本）；#10 ×1 | B.2 第 2 条方向 |
| `references/self-check-language.md`（S06b） | #10 ×1 | 「看见」类正常词误报 |
| `references/research-and-verification.md`（S06c） | #4 ×2（:121/:142）；#8 ×3（:48/:52/:192）；#10 ×15 | #4/#8 均为事实核验语境（B.2 第 5 条方向）；#10 多为「证据/依据」类误报，逐条读原句 |
| `references/reader-feedback.md`（S06c） | #10 ×3 | 同上 |
| `SKILL.md`（a1 已结片） | #5a ×1（:215）；#8 ×2（:330/:340「文本版本」子串误报）；#10 ×4 | a1 已判允许，本片沿用 |
| `references/rules-premise-and-structure.md`、`rules-revision-and-method.md`（a1 已结片） | #10 ×6、#5a ×6 | a1 已判允许 |
| `examples/planning-cases.md`（a2） | #10 ×1 | 读原句判误报 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S06a3／fiction-planning-and-diagnosis：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/fiction-planning-and-diagnosis/` 全部 27 文件。全包 65 条命中：#1/#2/#5b/#6/#7/#9/#11 零命中；#3=1、#4=3、#5a=13、#8=7、#10=41。本片落点 7 文件（revision、scope-and-conflicts、rule-examples、templates×4）命中 11 条，逐条判允许、零违规（「大师」4 条为 FC-21 元规则自身对象/被降格主张；「上一版」1 条为用户稿件版本；「据/见」6 条为证据/数据/判据类误报）。改写前该 7 文件含 -NNNN 残片 4 处（含 §3.1 指名的 scope:74 `-2236`、:76 `-2111` 与 a1 移交的 revision:123 `-1328`、:169 `-3143`）、年代说法 9 处（含指名的「1890 年代英国市场」「1911 年前的手册」及复扫扩大的 7 处）、「标 未证实」3 处（含指名的 §3 三处，已按交付状态词收敛「未能核实」并与 SKILL.md §7 联动句对齐）、文件头括注 1 处、「单来源」3 处、「见FC」残迹 6 处，全部清除；四张模板按合同第三节补齐「状态/稿件证据位置」两列（每编号一行、三列齐全、未知合法、分隔行齐全），文件头「未定/待补」「未授权」改四词口径。来源类三件（source-index、version-and-provenance、p4-field-guide）按 2.8 节不恢复，通用语义落点逐句核实（RS-05、SKILL.md §2/§6/§9、scope §4.3、FC 规则卡）；r2 `K-16` 行确认为计量假象不恢复（a2 交接闭环）。基线其余 20 文件命中 54 条全部按归属登记（a1 已判 16、待 a2 10、待 S06b 4、待 S06c 21、Agent 1 裁处 3）。B.3 逐文件回读本片 7 份：无新增自创例、无背书、无残迹、骨架比对通过；相对链接无断链、表格分隔行齐全。**本片落点零违规，可交 W4 独立隔离回读。**
