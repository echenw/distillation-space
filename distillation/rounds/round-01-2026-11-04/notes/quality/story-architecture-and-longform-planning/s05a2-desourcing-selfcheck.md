# S05a2 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S05a2（story：v0 `plot-architecture` 的 diagnosis / examples / scope-and-conflicts / decision-rework / templates×3 ＋ 来源类两件）｜代理：Agent 3（a2 段子代理）｜轮次：W3 主体轮第 7 批｜日期：2026-11-05
- 范围：`output/story-architecture-and-longform-planning/` 全部 21 个文件。本片改写其中 **5 个**：`references/plot-diagnosis.md`、`examples/plot-examples.md`、`templates/plot-canvas.md`、`templates/plot-diagnosis-report.md`、`templates/plot-scene-table.md`。`references/plot-scope-and-conflicts.md` 逐块比对零缺失、复扫零残留，本片零改动。其余 15 个为 a1 并行片落点（SKILL.md、references/plot-rules.md、plot-planning.md、plot-revision.md）与 S05b 范围（serial-*），命中如实按归属登记，本片未改动（写入范围经与 v3 基线 diff 核验：本片改动仅限 5 个落点文件，与 a1 的 4 文件无重叠）。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 34 条命中；本片 6 文件的 19 条正则命中全部判允许、零违规；其余 15 条按归属登记**。改写前本片落点的残留（「（未证实）」2、「用户明确要求」1、「语料」措辞 1、三张模板缺列 3 表、状态栏词形「部分」1）与四词外词形（「待验证/未核实/未验证/未核」8 处，含 a1 ledger 指名 4 处）全部清除并复扫归零。

## 一、全 11 类复扫计数（最终，本片改写后）

| # | 目标 | 全包命中 | 本片 6 文件 | 其余 15 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | 0 | 0 | 0（v2 基线的 plot-scope `-922` 残片已由 v2→v3 去来源轮清除，LI-ST-128 登记闭环） |
| 3 | 来源数量与年代 | 0 | 0 | 0 |
| 4 | 指向学习材料的说法 | 1 | 0 | 1（serial-zh-webnovel:9「一部书里的一卷」，S05b；语义指用户自己的连载作品，B.2 第 1 条方向，移交其分片复核） |
| 5a | 作家/大师类词 | 0 | 0 | 0 |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 8 | 6（plot-examples:15/42/74/109、plot-canvas:1、plot-diagnosis-report:1、plot-scene-table:1——见二节，其中模板题名 3 条在本片文件） | 2（SKILL.md:58「Skill Owner」＝a1，模板式短语非人名） |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | 0 | 0 | 0 |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 0 | 0 | 0（开工时 a1 文件 4 处「未证实」在本片末次复扫前已由 a1 自行收敛清零，未由本片动手） |
| 附 | 四词外状态词形（待验证／未核实／未验证／未核） | 0（收敛前 8 处，LI-ST-131） | 0 | 0（「未读」＝范围标记、「未定」＝冲突状态、「推断」＝证据级元数据，按 a1 D3 口径保留） |
| 10 | 删除后的残迹 | 21 | 13（见二节，全部为完整词误报） | 8（plot-rules ×2、plot-revision ×1、serial-production ×1、serial-examples ×2、SKILL ×2＝a1/S05b 归属，同型「证据/数据」误报） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0（改写前 plot-diagnosis:8 命中 1 处「用户明确要求」，已清，LI-ST-129） |

合计 34 条（1+8+21+1+3 类零命中不计）。附加扫：「未证实」全包零命中（本片 2 处已删括注、a1 4 处由 a1 收敛）；四词外词形「待验证/未核实/未验证/未核」经 LI-ST-131 收敛后在本片 6 文件归零，全包仅剩 4 处均在 serial-* 文件（serial-platform-migration ×3、serial-zh-webnovel ×1，S05b 范围，其 ledger 已认领清扫）；「未定/未读」为冲突状态与范围标记、「推断」为证据级元数据，按 a1 D3 口径保留。

## 二、本片 6 文件命中逐条判断（19 条，全部允许）

### #5b（6 条，非人名的连续大写词）

| 位置 | 命中 | 判断 |
|---|---|---|
| `plot-examples.md:15/42` | The Salt Road | 允许。自创虚构示例作品名（v0 编者所写、v3 沿用的编写示范），非真实作品、非人名；书名号已由 v3 去除，#1 零命中。 |
| `plot-examples.md:74/109` | The Last Tram | 允许。同上，虚构示例名。 |
| `plot-canvas.md:1`、`plot-diagnosis-report.md:1`、`plot-scene-table.md:1` | Plot Canvas／Diagnosis Report／Scene Table | 允许。模板文件标题（v0 起的既有命名），非人名。 |

### #10（13 条，`据[，。；]`／`见[，。；]` 类误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `plot-diagnosis.md:10/308` | 据； | 「证据；」（读者反应只作线索／代替具体证据） |
| `plot-scope-and-conflicts.md:90/119/148` | 据。/据，/据。 | 「考据。」「数据，」「证据。」 |
| `plot-examples.md:3/25/30/44/127/287` | 据。/见，/据，/见，/据，/据；据。 | 「数据。」「听见，」「证据，」「同一听证会的走私者」行的「见，」实为「听见，」误报、「作者信心判」前句「读者数据，」「反馈数据；」 |
| `plot-diagnosis-report.md:81` | 据； | 「文本证据；」 |

全部是完整句、语义通顺的正常词（证据/数据/考据/听见），不是删除来源后悬空的「见／据」；`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式在本片文件零命中。允许。

## 三、B.2 允许情形（本片 6 文件层面）

- **本包内部编号**：PL-01–16、PA-01–12、DR-01–10＋DR-SUM、ST-01–24、E-xx、F-xx、A/B/C/D 分支号、B1/B2/B3 路径号、C-01–C-13（本文件内部定位）。符合 B.2 第 3 条。
- **用户稿件版本号**：示例中「v2 稿」「大纲 v1」「版本：v3，2026-10-20」为虚构示例的稿件版本语境。符合 B.2 第 2 条。
- **操作默认数字**：3/4、72%、88%/12%、40%、10%、15%、8,200 词、45,200→29,600 词等——均为「默认值/可调整/不作硬门」限定的操作值或示例内演示数据，沿用 v3 既有口径与 S06a3 selfcheck 第三节判法。允许。
- **否定式规范说明**：三张模板用法段的「不指向来源编号或包外路径」「不得把未知写成已完成」为对成品的规范性禁令（S06a3 同判允许），不指向学习材料。
- **自创虚构示例名**：盐路（The Salt Road）、末班电车（The Last Tram）、铁河（River of Iron）及 Mira/Ivo/Kral/Nela 等示例人物名——v0 编者所写、v3 沿用的编写示范人物（B.3 骨架比对见下节），非真实作品与作者。

## 四、B.3 人工判断（逐文件回读本片改写的 5 份文件＋复核 1 份）

1. **与 v0 来源案例的骨架比对**：本片唯一新增文本是 `plot-diagnosis.md` §D6 的三条检查维度（喜剧缓解/对白与动作的关系/看似多余的角色）——为检查维度陈述，**不含任何情节示例**，骨架比对不适用。三张模板加列与本片残留清除不产生新示例。examples 的三综合例与 E1–E5 为 v0 编者所写、v3 沿用的虚构示例（与 v0 逐块相同，非本片新写），无新骨架比对义务；其人物关系（制图师×走私船长、售票员×稽查员）、关键事件、时代地点与 v0 scope 所引真实作品案例（莎剧、希腊悲剧等，v3 已全部清除）无两项以上对应，且本就属「编写示范」声明覆盖范围。
2. **具体作品的标志性情节元素**：6 文件复扫书名号零命中、#5b 全部为虚构示例名与模板题名；「电报解结」「失散亲人重逢」「临终忏悔」等是巧合类型的通用举例（v0/v3 一致），非具体作品情节。
3. **借来源背书的说法**：6 文件回读无「经典做法是……」「很多名作都……」式句子；「有限经验形成的可选起点」「按当前作品验证」等改写只保留判断方向，未添程度词或新断言；未编造替代数字（D6 三条细则无数值断言）。
4. **删除来源后语义**：diff 逐处复查（plot-diagnosis 2 处、plot-examples 2 处、plot-canvas 4 处、plot-diagnosis-report 3 处、plot-scene-table 3 处），无主语悬空、无空括号、无表格空列；「（未证实）」两处删括注后主句（「效果未验证」「不保证填完即写出好作品」）语义自足；「用户明确要求」改写后授权条件保留（与 §7 口径一致）。
5. **全包辅助复扫**：来源特征词（`L[0-9]{3,5}` 行号、`kd`、Gutenberg、公版、`source-index`、`historical-provenance`、`decision-rework`、`PG`、`TRUSTED`、`evidence_window`）全目录零命中；「RC-」旧编号残留复扫零命中（v3 已全部改 PL，D3 映射句的「RC」为 a1 处理对象，见其 D3）。

## 二.5、四词外词形收敛（LI-ST-131，8 处，含 a1 ledger 指名 4 处）

| 位置 | 收敛前 | 收敛后 |
|---|---|---|
| `plot-diagnosis.md` D1 表（版本/删节/翻译行） | 标 “未核” | 标 “未能核实” |
| `plot-diagnosis.md` D6 尾段 | 记录为待验证 | 记录为“未能核实” |
| `plot-scope-and-conflicts.md` §3.1 | 标“未核实” | 记“未能核实” |
| `plot-scope-and-conflicts.md` §3.2 | 标“推断/待验证” | 标“推断”、记“未能核实” |
| `plot-scope-and-conflicts.md` §4 | 未验证项 | 未能核实的项目 |
| `examples/plot-examples.md` 文件头 | 效果未验证 | 不保证实际效果 |
| `plot-diagnosis-report.md` 用法 | “未知”/“未读”/“未核” | “未知”/“未读”/“未能核实” |
| `plot-diagnosis-report.md` §7 | 只放“待验证” | 只放“未能核实” |

收敛口径与 a1 D3 一致（效果类用「不保证…」句式；「未核/待验证/未核实/未验证」→「未能核实」）；「未读」（范围标记）、「未定」（冲突状态）、「推断」（证据级元数据）按 a1 元数据口径保留。收敛后「待验证/未核实/未验证/未核」在本片 6 文件复扫归零。a1 移交的 The Salt Road/The Last Tram 骨架比对闭环见四.1（三项骨架均无两项以上对应，无需重写）。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 全包 #8 零命中；本片 6 文件无「本版补回」类自述；D6 补回句无「补回/旧稿」词形 |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE/GQ/R17/R18 附加扫） | 全包零命中 |
| 禁用说法（#11 全模式） | 全包零命中（改写前 plot-diagnosis:8 的「用户明确要求」已清） |
| 四词状态词 | 三张模板的「状态」列口径统一为「已完成／依据／未能核实／待作者决定／未知」，plot-canvas 状态栏「部分」已收敛；「未知是合法值、不得把未知写成已完成」在三表用法段写明；四词外词形 8 处收敛归零（见二.5） |
| 相对链接 | 本片 6 文件引用的 `references/plot-rules.md`、`plot-planning.md`、`plot-revision.md`、`plot-diagnosis.md`、`plot-scope-and-conflicts.md`、`templates/plot-*.md` 逐条 grep 核实全部存在；无指向已删除的 source-index/historical-provenance/decision-rework 的引用；a1 的 SKILL.md §10 出口列口径（未知/证据位置）与三表新增列一致 |
| GFM 表格分隔行 | 全包逐表核验：三张模板 §1 加列后表头/分隔/数据行列数一致（canvas 6 列、report/scene 7 列）；其余既有表分隔行未动；无「有数据行缺分隔行」 |
| 模板规范（合同第三节） | 三张模板每个编号独占一行、值/状态/稿件证据位置三列齐全、未知合法、证据位置只指当前稿件、分隔行齐全——逐项对照通过 |
| 写入范围 | 本片仅改 5 个落点文件＋新建 3 份 notes（LI／source-synthesis 追加节／selfcheck）；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a1 的 4 文件与 S05b 的 serial-* 文件 |
| 并行片协调 | 建包用 `cp -Rn`（不覆盖）；a1 在本片运行期间完成其 4 文件改写（含其 D1 四处硬门回潮恢复与 D3 措辞收敛），双方 diff 核验写入文件集无交集；source-synthesis 按「只追加」协议在 a1 节末追加，无整文件重写 |

## 六、待对应分片处理的登记（非本片文件命中，本片未动）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `references/serial-zh-webnovel.md`（S05b） | #4 ×1（:9「一部书里的一卷」）；「核验/未核实」词形 ×1 | 「书里」语义指用户自己的连载作品（B.2 第 1 条方向），预期判允许；全包 #4 现存唯一命中 |
| `references/serial-platform-migration.md`（S05b） | 四词外词形 ×3（:37「已核实／未核实／不适用」T1–T6 状态、:3/:5「核验」语境） | 其 ledger 已认领 serial-* 词形清扫；:37 的三态为迁移核验记录列，供其按交付状态词口径裁定 |
| `SKILL.md`（a1 已结片） | #5b ×1（:58「Skill Owner」）、#10 ×2 | a1 文件；「Skill Owner」为模板式短语非人名 |
| `references/plot-rules.md`、`plot-revision.md`（a1 已结片） | #10 ×3 | 「证据/数据」类同型误报 |
| `references/serial-production.md`、`examples/serial-examples.md`（S05b） | #10 ×3 | 同上 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S05a2／story-architecture-and-longform-planning：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/story-architecture-and-longform-planning/` 全部 21 文件。全包 34 条命中：#1/#2/#3/#5a/#6/#7/#8/#9/#11 零命中；#4=1（serial-zh-webnovel「书里」，S05b，B.2 第 1 条方向）、#5b=8（虚构示例名与模板题名，非人名）、#10=21（全部为「证据/数据/考据/听见」类完整词误报）。本片 6 文件命中 19 条逐条判允许、零违规。改写前本片落点残留：examples 与 plot-canvas 文件头「（未证实）」2 处（删括注，主句语义自足）、plot-diagnosis §0「用户明确要求」1 处（改「需用户授权并给出范围」）、「语料」措辞 1 处（改「按当前作品验证」）、plot-canvas 状态栏「部分」1 处（收敛四词＋未知）、四词外词形 8 处（「待验证/未核实/未验证/未核」→「未能核实」，「效果未验证」→「不保证实际效果」，含 a1 ledger 指名 4 处，LI-ST-131）、三张模板缺「值/状态/稿件证据位置」列 3 表（按合同第三节补列，canvas 补 1 列、report/scene 各补 3 列，行列数与分隔行核验一致）——全部清除并复扫归零。**S-1 必做核定：十一项已在 v3（plot-diagnosis:317–327，与 v1 逐条对照全覆盖，计划 2.4「仍缺」按实测修正）；三条细则（喜剧缓解、对白与动作的关系、看似多余的角色）v2/v3 均缺，已按通用写法补回 D6（LI-ST-101，唯一恢复项）。** 来源类两件（source-index 25 单元、historical-provenance 2 单元）按 2.8 节不恢复，通用语义落点逐句核实（scope §3.4/§3.5、plot-rules 权威版本定位、SKILL.md 输出四件）；decision-rework 五单元＋A-01 判「语义已承接」并闭环 a1 D5 移交（P4 微例判不补）；a1 移交的 The Salt Road/The Last Tram 骨架比对通过（三项骨架无两项以上对应）。基线其余 15 文件命中 15 条全部按归属登记（a1 6、S05b 9 类）。B.3 逐文件回读本片 6 份：唯一新增规则文本为 D6 三条检查维度（无情节示例、无来源指涉），相对链接无断链、表格分隔行齐全、与 a1 SKILL.md §10 出口列口径一致。**本片落点零违规，可交 W4 独立隔离回读。**
