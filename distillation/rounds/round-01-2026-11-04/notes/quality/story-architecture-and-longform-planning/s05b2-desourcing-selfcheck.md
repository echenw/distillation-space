# S05b2 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S05b2（story：v0 `serialized-volume-planning` 的 b2 段＝worked-example＋05-production-constraints＋08-cross-volume-dependencies＋legacy-metadata；06-source-index 为 SOURCE_ONLY 逐块判定）｜代理：Agent 3（b2 段子代理）｜轮次：W3 主体轮第 8 批｜日期：2026-11-05
- 范围：`output/story-architecture-and-longform-planning/` 全部 21 个文件。本片改写其中 **6 个**：`references/serial-production.md`、`references/serial-chapters-and-installments.md`（SV-10/SV-16 节）、`references/serial-volume-and-closure.md`（文件尾跨卷节）、`examples/serial-examples.md`（例 A/例 B 出口块）、`references/serial-platform-migration.md`、`references/serial-zh-webnovel.md`。a 段已修 10 文件（SKILL.md、plot-rules、plot-planning、plot-revision、plot-diagnosis、plot-examples、plot-scope-and-conflicts、plot-canvas、plot-diagnosis-report、plot-scene-table）本片零改动；b1 范围文件（serial-rules、serial-open-lines-and-continuity、serial-formula-and-escalation、serial-tables）本片零改动。共写文件（serial-production、serial-chapters、serial-volume-and-closure、serial-examples）经与 b1 并行写入 diff 核验：b1 追加其谱系节（SV-14 步骤 5、SV-09 两处、SV-02 一处、SV-06 修复窗口表），与本片写入区域零重叠、零冲突。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 29 条命中；本片 6 文件的 3 条正则命中全部为完整词误报、判允许、零违规；其余 26 条按归属登记（a1 5、a2 21，均沿用其 selfcheck 已判结论）；全包四词外词形归零**。改写前本片落点的残留（platform-migration 三态「已核实/未核实/不适用」及「未核实」×3、zh-webnovel「未核实」×1 与「一部书里的一卷」#4 命中 ×1、serial-chapters SV-16「未核」×1）全部清除并复扫归零。

## 一、全 11 类复扫计数（最终，本片改写后；含 b1 并行写入后的全包状态）

| # | 目标 | 全包命中 | 本片 6 文件 | 其余 15 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | 0 | 0 | 0 |
| 3 | 来源数量与年代 | 0 | 0 | 0 |
| 4 | 指向学习材料的说法 | **0**（改写前 1：serial-zh-webnovel:9「一部书里的一卷」，本片 LI-ST-345 改写归零） | 0 | 0 |
| 5a | 作家/大师类词 | 0 | 0 | 0 |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 8 | 0 | 8（plot-examples The Salt Road ×2、The Last Tram ×2＝a2；SKILL.md「Skill Owner」＝a1；plot 三模板题名 ×3＝a2——沿用 s05a2/s05a1 selfcheck 判允许结论，本片未动其文件） |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | 0 | 0 | 0 |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 0 | 0 | 0 |
| 附 | 四词外状态词形（待验证／未核实／未验证／未核／未证实） | **0**（改写前本片落点 5 处：platform-migration ×3、zh-webnovel ×1、serial-chapters SV-16 ×1；另有 b1 谱系 6 处——serial-open-lines ×2、serial-volume-and-closure:158、serial-tables ×3——LI-ST-347 移交 b1，本片收尾复扫确认 b1 已全部收敛） | 0 | 0（「未读」＝范围标记、「未定」＝冲突状态、「推断」＝证据级元数据，按 a1 D3 口径保留） |
| 10 | 删除后的残迹 `见[，。；]`、`据[，。；]` | 21 | 3（serial-production:72「读者数据；」、serial-examples:3「读者数据，」、serial-examples:64「判据，」——全部为完整词误报，见二节） | 18（SKILL ×2、plot-rules ×2、plot-revision ×1＝a1；plot-diagnosis ×2、plot-scope ×3、plot-examples ×7、plot-diagnosis-report ×1＝a2；均沿用其 selfcheck 判允许结论） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 |

合计 29 条（8+21）。`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式全包零命中。附加扫：审计词全模式（含 OBSERVED/DESIGN_EXAMPLE/GQ/R17/R18）全包零命中；来源特征词（`L[0-9]{3,5}` 行号、`kd`、Gutenberg、公版、`source-index`、`legacy-metadata`、`historical-provenance`、`SHA`、`TRUSTED`、`NOT_OBSERVED`）全包零命中——SOURCE_ONLY 两件（06-source-index 47820 B、legacy-metadata 1743 B）的任何词形均未进入成品。

## 二、本片 6 文件命中逐条判断（3 条，全部允许）

### #10（3 条，`据[，。；]` 类误报）

| 位置 | 命中子串 | 所在词 | 判断 |
|---|---|---|---|
| `serial-production.md:72` | 据； | 「读者数据；」（卡住时「不假装有读者数据」） | 允许。完整句、语义通顺的正常词，非删除来源后悬空的「据」；v3 基线原有，本片未改该句。 |
| `serial-examples.md:3` | 据， | 「读者数据，」（文件头「不指向…读者数据」） | 允许。同上，v3 基线原有。 |
| `serial-examples.md:64` | 据， | 「判据，」（「按 SV-14 的判据，更适合多攒存稿再开」） | 允许。同上，v3 基线原有。 |

本片新增文本（联动段、S-2 补句、备用结局句、跨卷节、两个出口块、迁移记录表、SV-10 篇幅段、SV-16 词形、zh-webnovel 两处）复扫：#10、#附、#1–#9、#11 全部零命中。

## 三、B.2 允许情形（本片 6 文件层面）

- **本包内部编号**：SV-01–SV-16、T1–T6（迁移检查项编号）、serial-tables §1–§11 表号（引用）。符合 B.2 第 3 条。
- **事实核验场景的指物**：迁移记录表「依据位置（合同条款、官方说明或账号后台页面）」指作者要核验的资料（B.2 第 5 条方向），不指向学习材料或包外路径。
- **操作假设数字**：serial-examples 例 A「合同砍到 24 章」为例内假设分支（对应 v0 A11 出口演示），带「计划赶不上变化时」的条件框架，非通用阈值。
- **虚构示例人物沿用**：出口块沿用例 A/例 B 既有人物（Rusk、Ivo、Juno）与事件（第 18/28/29/30 章、里斯本买主）——v0 编者所写、v3 改名沿用的编写示范要素（S05a2 selfcheck 已判允许），本片未新增人物或情节骨架。
- **否定式规范说明**：迁移状态口径段「不得把未知写成『已完成』」「不得作为公开承诺」为对成品的规范性禁令，不指向学习材料。

## 四、B.3 人工判断（逐文件回读本片改写的 6 份文件）

1. **与 v0 来源案例的骨架比对**：本片新增文本分两类。规则与表格类（跨卷节层级表/权威段/六步链/卡住时、SV-13 联动段、SV-10 篇幅段、迁移记录表、SV-15 两句）为规则陈述与表格骨架，**不含任何情节示例**，骨架比对不适用。示例出口块类（例 A「计划赶不上变化时」、例 B「退出与拒绝」）沿用例内既有事件与人物，与 v0 worked-example 同源（v3 已将系列名/地名中文化：The Lantern Line→灯塔线、The Glass Harbor→玻璃港；人物名 Mara/Ivo/Juno/Rusk 与「里斯本买主」为 v0 编者所写、v3 沿用），属「编写示范」声明覆盖范围；未从 v0 引入任何 v3 没有的情节骨架（出口块只复用例内已建立的事件并新增通用假设分支「砍到 24 章」「四条线」，无人物关系/关键事件/时代地点三项与任何真实作品两项以上对应的情形）。
2. **具体作品的标志性情节元素**：6 文件复扫书名号零命中、#5b 零命中；「备用结局」「半开」「开放线」「里斯本买主」均为例内虚构要素；无具体作品标志性情节。
3. **借来源背书的说法**：6 文件回读无「经典做法是……」「很多名作都……」式句子；跨卷节的「低层不能替代高层」三条写成直接判断；SV-10 篇幅段与 SV-13 联动段只写适用条件与出口，未添程度词或新断言；未编造阈值（联动段不设数字门槛，「按固定周期」口径保留）。
4. **删除来源后语义**：逐处复查本片全部改动（serial-production 4 处、serial-chapters 2 处、serial-volume-and-closure 1 节、serial-examples 2 块、serial-platform-migration 3 处、serial-zh-webnovel 2 处）：无主语悬空、无空括号、无表格空列；platform-migration 文件头「还没核验的事项标『未能核实』」与导语「『未能核实』不等于平台不支持」语义自足；迁移记录表拆两表后「核验材料位置与仍缺信息」行保留，「不适用项在迁移记录表标『不适用』」导语与状态栏口径一致；zh-webnovel 第 1 行改写后「同一部连载作品中的一卷」与 SV-01「一部书分卷连载」术语呼应完整；SV-16「未能核实」句与 serial-tables 头部口径（b1 已同步收敛）一致。
5. **相对链接**：本片 6 文件的既有 markdown 链接（`../SKILL.md`、`../templates/serial-tables.md`）逐条核实存在；本片新增文本无新 markdown 链接，跨文件引用一律用卡号或「serial-tables.md §11」式纯文本指称（与各 SV 卡既有写法一致）。
6. **表格分隔行**：本片新增两张表（跨卷节层级表 4 列、迁移记录逐项状态表 3 列）表头/分隔/数据行列数一致；迁移记录项目表（2 列）沿用原表结构；既有表未动。

## 五、模板规范核对（合同第三节；serial-platform-migration 迁移记录表）

| 要求 | 核对 |
|---|---|
| 每个编号独占一行 | T1–T6 六行，每行一个检查项 |
| 三列齐全 | 检查项／状态／依据位置，表头分隔数据均 3 列 |
| 允许填「未知」 | 状态栏口径写明「缺输入填『未知』；『未知』是合法值，但不得把未知写成『已完成』」 |
| 状态按四词填 | 已完成／依据／未能核实／待作者决定；「不适用」仅用于该项无对应对象（沿用 serial-tables §3 的合法用法） |
| 稿件证据位置只指向用户当前材料 | 「依据位置（合同条款、官方说明或账号后台页面）」，不指向来源编号、批次或包外路径 |
| 有数据行缺分隔行视为格式失败 | 两表均有分隔行 |

注：v3 基线把 T1–T6 状态并为一行且用「已核实／未核实／不适用」三态；本片按合同第三节改造（LI-ST-344），移交项 ② 闭环。

## 六、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 全包 #8 零命中；跨卷节无「补回/旧稿/取代」词形（v0 legacy-metadata 的「取代/保留未变」叙事未进成品） |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE/GQ/R17/R18 附加扫） | 全包零命中（v0 的 NOT_OBSERVED/DESIGN_EXAMPLE/UNRESOLVED/REJECT/UNVERIFIED 均未进成品；「未能核实」为四词） |
| 禁用说法（#11 全模式） | 全包零命中 |
| 四词状态词 | 迁移记录表状态列口径统一；本片无新增「部分」类四词外词形；全包「待验证/未核实/未验证/未核/未证实」归零 |
| SOURCE_ONLY 隔离 | 06-source-index、legacy-metadata 的特征词（SHA/台账/门禁/PG/书名族名/年代窗口）全包零命中；两文件按 2.8 节不恢复，十四块＋两节逐块判定入账（LI-ST-328–343） |
| 写入范围 | 本片仅改 6 个落点文件＋新建 2 份 notes（LI 记录含补记、本 selfcheck）＋追加 1 份 source-synthesis 节；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a1/a2 的 10 文件与 b1 范围文件 |
| 并行片协调 | 与 b1 共写三文件（serial-production、serial-chapters、serial-volume-and-closure）＋serial-examples：b1 写入后 diff 核验其追加节与本片区域零重叠；b1 已收敛本片移交的 6 处「未核」（LI-ST-347 闭环）；source-synthesis 按「只追加」协议在 a2 补记之后追加「S05b2 决策链」节，追加前重读文件尾确认无冲突，无整文件重写 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S05b2／story-architecture-and-longform-planning：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/story-architecture-and-longform-planning/` 全部 21 文件（含 b1 并行写入后的当前状态）。全包 29 条命中：#1/#2/#3/#4/#5a/#6/#7/#8/#9/#11 零命中（#4 原唯一命中 serial-zh-webnovel:9「一部书里的一卷」经 LI-ST-345 改写为「同一部连载作品中的一卷」后归零）；#5b=8（虚构示例名与模板题名，a1/a2 文件，沿用其判允许结论）；#10=21（全部「读者数据/判据/证据/考据」类完整词误报，本片 3 条逐条判允许，零违规）。四词外词形全包归零（本片落点 5 处由本片收敛；b1 谱系 6 处由 b1 收敛，LI-ST-347 移交闭环）。本片残留清除：platform-migration 三态列与「未核实」×3（按合同第三节改四词＋T1–T6 六行三列表，LI-ST-344）、zh-webnovel「未核实」×1 与「书里」×1（LI-ST-345/346）、serial-chapters SV-16「未核」×1（LI-ST-346）。**S-2 必做闭环：SV-15 步骤 2 补「设定矛盾、时间线错误这类可核对错误，不必等第二个信号；改不改、改在哪一版，仍按合同和已发表范围决定」（计划 2.4「部分补回」按实测收口）。S-4 核心落点：serial-volume-and-closure 文件尾新增「跨卷承诺的层级、正典权威与变更检查」节（五层层级表＋正典权威段＋六步变更影响链＋版本冲突卡住时；LI-ST-321/322/324/327）；series-volume-dependency 模板矩阵本体移交 b1。** 来源类大件 06-source-index（47820 B）十四块与 legacy-metadata（1743 B）两节按 2.8 节不恢复、通用内核逐块核对均有既有落点（SKILL §11、plot-scope §3.4、SV-03/04/08/11/16、serial-zh-webnovel §2/§3、serial-production 风险检查表），逐条登记 LI-ST-328–343；worked-example 的示例级失败出口缺块补回（例 A/例 B 两块，LI-ST-316/319）。B.3 逐文件回读本片 6 份：新增文本无情节示例（出口块沿用例内既有虚构要素）、相对链接无断链、新表分隔行齐全、迁移记录表满足模板规范五项。**本片落点零违规，可交 W4 独立隔离回读。**
