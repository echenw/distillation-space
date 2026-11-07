# S05b1 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S05b1（story：v0 `serialized-volume-planning` b1 段＝SKILL.md＋agents＋wave4-casebook＋references/01–04＋07-production-discipline＋templates/series-volume-dependency，90905 B）｜代理：Agent 3（b1 段子代理）｜轮次：W3 主体轮第 8 批｜日期：2026-11-05
- 范围：`output/story-architecture-and-longform-planning/` 全部 21 个文件。本片改写其中 **7 个**：`references/serial-rules.md`、`references/serial-volume-and-closure.md`、`references/serial-chapters-and-installments.md`、`references/serial-open-lines-and-continuity.md`、`references/serial-formula-and-escalation.md`、`references/serial-production.md`、`templates/serial-tables.md`；另复核 `references/serial-zh-webnovel.md`、`references/serial-platform-migration.md`（b2 改写，本片只复核登记、未动其正文）。其余 12 个为 a1/a2 已结片落点（SKILL.md、plot-* 六件、plot-canvas/plot-diagnosis-report/plot-scene-table、agents/openai.yaml、examples/plot-examples.md），命中引用其自检。serial-production.md 与 serial-volume-and-closure.md、serial-chapters-and-installments.md 为两片共写文件：本片写入限于 SV-13–15 的 SV-14 步骤与 SV-01–07/SV-09 区段，b2 写入其追加节与 SV-10 篇幅段，编辑前后重读核验无同行冲突。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目标>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 28 条命中；本片新增文本零命中（未引入任何命中），零违规**；本片落点文件内唯一命中为 `serial-production.md:72`（SV-15 卡住时基线句「读者数据；」，属 b2 主落点既有文本，非本片新增行，登记待 S05b2 复判）；其余 25 条在 a1/a2 文件（其自检已逐条判允许）。改写前本片落点的残留（四词外词形「未核」6 处、「未核实」1 处）全部收敛并复扫归零；全包 #4「书里」唯一命中由 b2 改写清零（本片复核闭环）。

## 一、全 11 类复扫计数（最终，本片改写后）

| # | 目标 | 全包命中 | 本片 7 文件 | 其余 14 文件（归属） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]`、`-[0-9]{3,5}` | 0 | 0 | 0 |
| 3 | 来源数量与年代 | 0 | 0 | 0 |
| 4 | 指向学习材料的说法 | 0 | 0 | 0（改写前 serial-zh-webnovel:9「一部书里的一卷」1 处，b2 已改「同一部连载作品中的一卷」，LI-ST-245 复核闭环） |
| 5a | 作家/大师类词 | 0 | 0 | 0 |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 8 | 0 | 8（SKILL.md:58「跨 Skill Owner」＝a1；plot-examples:15/42/74/109 盐路/末班电车＝a2；plot-canvas:1、plot-diagnosis-report:1、plot-scene-table:1 模板题名＝a2——均其自检已判允许） |
| 6 | 英文原句（含弯引号变体加扫） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹 | 0 | 0 | 0 |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE/NOT_OBSERVED 附加扫） | 0 | 0 | 0 |
| 附 | 四词外状态词形（待验证／未核实／未验证／未核／未证实） | 0 | 0 | 0（收敛前 serial-* 共 9 处：本片 6 处 LI-ST-247、b2 3 处；「未读」17 处＝范围标记、「未定」10 处＝冲突状态、「推断」16 处＝证据级元数据，按 a1/a2 口径保留） |
| 10 | 删除后的残迹 | 20 | 1（serial-production:72「读者数据；」＝SV-15 卡住时基线句，b2 主落点既有文本，本片新增行零命中；登记待 S05b2 复判） | 19（SKILL ×2、plot-examples ×6、plot-diagnosis ×2、plot-revision ×1、plot-rules ×2、plot-scope ×3、plot-diagnosis-report ×1＝a1/a2 已判；serial-examples ×2＝b2 主落点，登记待 S05b2） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 |

合计 28 条（1+8+20；其余类零命中不计）。附加扫：来源特征词（Trollope/Daudet 等责任者、Gutenberg、公版、`source-index`、`historical-provenance`、`legacy-metadata`、`kd`、`ledger`、`wave4`、`NOT_OBSERVED`、`retcon`）全目录零命中；v0 旧编号（M01–M17）在 serial 落点零残留（M→SV 改号已全覆盖，LI-ST-208）。

## 二、本片 7 文件命中逐条判断（1 条基线误报，非本片新增；本片新增文本 0 命中）

- 11 类正则 + 四词外词形附加扫在本片 7 个落点文件合计 1 条命中：`serial-production.md:72`「……不假装有读者数据；」——所在句为 SV-15 卡住时的 v3 基线文本（b2 主落点范围，本片在该文件仅于 SV-14 怎么做新增第 5 行），「数据；」是完整词「数据」加正常分号，不是删除来源后悬空的「据」；判允许（与 a2 selfcheck 对「证据；」「数据，」同型判法一致），登记待 S05b2 复判归账。其余子模式（`（\s*）`、`\(\s*\)`、`见\s*[，。；]`、`与\s*同`）在本片 7 文件零命中。
- 本片新增文本（约 30 行）逐句不含「书里/出自/据称/批次」类指涉、不含年代与编号残片、不含空括号或悬空「见/据」；「据/见」后接标点的子模式对新增句零命中（新增句无「证据；」「数据，」类搭配）。

## 三、B.2 允许情形（本片 7 文件层面）

- **本包内部编号**：SV-01–SV-16、serial-tables.md §1–§12、PL 编号引用、SU-15/SU-16 转介、T1–T6（迁移检查节号，b2 落点）。符合 B.2 第 3 条。
- **用户稿件语境的版本指涉**：§12 依赖矩阵「正典版本」列的「用户当前稿件或已发表章节」、回归段「按前卷实际存在的行动、读者已经收到的承诺」——指用户自己的连载作品与稿件（B.2 第 1 条），非学习材料。
- **自创年份/年代**：无（本片新增文本不含任何年份）。
- **模板状态值**：serial-tables §12「作者决定」列的「已确认／未能核实／待作者决定／不适用」——交付状态按四词填（「不适用」为逐项核对值，同 serial-tables §3 卷末四问与迁移记录表口径，非审计词 NOT_APPLICABLE）。

## 四、B.3 人工判断（逐文件回读本片改写的 7 份文件＋复核 2 份）

1. **与 v0 来源案例的骨架比对**：本片新增文本为——①SV-02 发行装置边界句、②SV-05 修复窗口三行表、③SV-09 两句处置、④SV-11 两句边界、⑤SV-14 破例记账句、⑥serial-tables §12 依赖矩阵（列说明＋空白矩阵＋回归段）。全部为规则/表格/检查维度陈述，**不含任何情节示例或自创故事**，骨架比对不适用；serial-examples 的例 A/B/C 为 b2 范围文件且本片未改动。§12 的列说明与 v0 模板逐列对照为「恢复改写」而非新例：13 列中删去 v0 的英文段名与来源语境（proof 的 F/H/P→证据类型、NOT_OBSERVED→未知），无人物、无事件、无地点。
2. **具体作品的标志性情节元素**：8 文件复扫书名号零命中、#5b 零命中；「密令、委任、实物、坐标、一张纸条」「比分、破案、追回的钱」等为 v0/v3 一致的通用举例，非具体作品情节；修复窗口表的「番外或加更」「下一卷开头桥段」为发表形态通用词，非作品元素。
3. **借来源背书的说法**：8 文件回读无「经典做法是……」「很多名作都……」式句子；本片新增句均为条件句或处置句（「只说明发行安排，不说明……」「确实要在同一章换多项时，检查……」），未添程度词或背书；未编造阈值或成体系反例（SV-14 步骤 5 与 SV-09 卡住时均无数字门槛）。
4. **删除来源后语义**：本片未删除任何 v3 既有内容（纯追加与词形替换）；词形替换 6 处逐处复读——「标『未能核实』」三处主句自足（跨卷判断/查不到的写/缺失的信息标），「活动线计数（『未能核实』的线不计入）」与模板 §5 枚举一致，「没读到的写『未读』」与同句「推测的写假设、不知道的写未知」三元组成立；SV-07 卡住时替换后「不写回顾，标『未能核实』；只给结构，等作者补上一卷的结果」语义完整。
5. **共写文件复核**：serial-volume-and-closure（b2 尾部追加「跨卷承诺的层级」节，其卡住时已用「未能核实」）、serial-chapters-and-installments（b2 已收敛 SV-16 并扩 SV-10 篇幅段）、serial-production（b2 扩 SV-13 卡住时）——三文件逐节复读，两片写入无语义冲突、无重复规则；serial-platform-migration 迁移记录表（b2 改写）按合同第三节复核：T1–T6 每项独占一行、三列齐全、分隔行齐、口径段含四词＋未知＋不适用，复核通过。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回／续排／编号续排／旧版／本版／更正／融合版／上一版） | 全包 #8 零命中；本片新增句无「补回/旧稿/恢复」类自述；§12 表题与说明无改动痕迹词形 |
| 审计词与状态码（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE/NOT_OBSERVED/GQ/R17/R18 附加扫） | 全包零命中（v0 的 NOT_OBSERVED/F/H/P/UNVERIFIED 均未进 §12 或本片任何新增句） |
| 禁用说法（#11 全模式） | 全包零命中 |
| 四词状态词 | serial-tables §12「作者决定」列与 §5 台账枚举收敛后口径统一（已完成／依据／未能核实／待作者决定／未知／不适用——「不适用」仅作逐项核对值）；「未知是合法值、不得把未知写成已完成」口径已在 §3/迁移记录表（既有）与 §12 回归段一致 |
| 相对链接 | 本片新增引用三处：`serial-rules.md` SV-08 卡的 `` `templates/serial-tables.md` §12 ``（行内代码，随 SKILL.md §10 口径）、`serial-open-lines-and-continuity.md` 产物行 `[serial-tables.md](../templates/serial-tables.md)`（相对路径自 references/ 解析成功，文件在位）、`serial-volume-and-closure.md` SV-05 表内 SV-08/SV-05 卡号（本包内引用）；既有链接未动 |
| GFM 表格分隔行 | 本片新增/改动的 4 张表（SV-05 修复窗口、§12 列说明、§12 空白矩阵、§5 台账枚举行改写）表头/分隔/数据行列数一致（修复窗口 4 列、列说明 2 列、空白矩阵 13 列）；全包逐表抽验无「有数据行缺分隔行」 |
| 模板规范（合同第三节） | serial-tables 各节为空白填表、无枚举编号字段清单，故不适用「逐编号一行三列」扩展（PA/DR/ST 三表已由 a2 落地）；§12 以列说明表替代编号清单并在回归段写明填写口径（假设/未读/未知、证据类型只指当前稿件） |
| 写入范围 | 本片仅改 7 个落点文件＋新建/追加 3 份 notes（LI／source-synthesis 追加节／selfcheck）；`git status` 无 `skills/` 改动；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md；未动 a1/a2 的 10 文件、未动 b2 谱系正文（05/06/08/legacy-metadata/worked-example 落点） |
| 并行片协调 | b2 在本片运行期间完成其追加节与移交三项落笔；本片编辑前重读三个共写文件与 source-synthesis 末尾（b2 已追加 S05b2 决策链节），写入节段互斥；source-synthesis 按「只追加」协议在 b2 节末追加本片节，无整文件重写；LI 编号段无交集（本片 201–247，b2 301–349） |

## 六、待对应分片处理的登记（非本片文件命中，本片未动）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `references/serial-production.md`（S05b2 主落点，本片仅 SV-14 加 1 行） | #10 ×1（:72「读者数据；」） | 基线误报（完整词「数据；」），a2 selfcheck 已登记同型判允许；b2 自检复判即可 |
| `examples/serial-examples.md`（S05b2，本片未动） | #10 ×2（:3「读者数据，」、:64「判据，」） | 同上，基线误报 |
| a1/a2 已结片 9 文件 | #5b ×8、#10 ×17 | 引用 `s05a1-desourcing-selfcheck.md`、`s05a2-desourcing-selfcheck.md`，均判允许 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S05b1／story-architecture-and-longform-planning：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/story-architecture-and-longform-planning/` 全部 21 文件。全包 28 条命中：#1/#2/#3/#4/#5a/#6/#7/#8/#9/#11 零命中；#5b=8（虚构示例名与模板题名，a1/a2 文件）、#10=20（「证据/数据/考据/听见」类完整词误报：a1/a2 文件 17、b2 主落点 3）。**本片 7 个落点文件命中 0 条、零违规**；本片新增文本（约 30 行：SV-02 发行装置边界、SV-05 修复窗口表、SV-09 末章二选一与钩子过强处置、SV-11 重复可为设计与因果清楚、SV-14 破例记账、serial-tables §12 依赖矩阵）逐句为通用条件句与核对表，无来源指涉、无情节示例、无审计词形。改写前本片落点残留：四词外词形「未核」6 处（open-lines:46/63、volume-and-closure:158、serial-tables:3/47/51——其中 serial-tables:3 收敛为范围标记「未读」，其余 5 处收敛为「未能核实」）与「未核实」1 处复核（zh-webnovel:40 由 b2 收敛），全部清除并复扫归零；全包 #4「书里」唯一命中由 b2 改「同一部连载作品中的一卷」清零（LI-ST-245 复核闭环）、迁移三态列按合同第二/三节改造为 T1–T6 六行三列＋口径段（LI-ST-246 复核闭环）。**S-4 必做核定：系列—卷—章依赖矩阵专表 v3 确缺（serial-tables 仅 §1–§11，v1 SP17 仍列依赖矩阵），已按去来源改写恢复为 serial-tables §12（13 列说明＋空白矩阵＋回归段，proof 的 F/H/P→证据类型、NOT_OBSERVED→未知、author_decision→已确认／未能核实／待作者决定／不适用），并在 serial-rules SV-08 卡与 serial-open-lines 产物行加路由指针（LI-ST-244，唯一恢复项）**；六处合并补强（发行装置/修复窗口/末章二选一/钩子过强处置/重复可为设计/破例记账）均有 v0＋v1 双佐证，逐处并入既有 SV 卡；十一组差异经 v1 核 v1→v3 同向判有意调整不回退（路线 C 拆轴、回顾与配额去数值化、活动线去硬限、缓冲章放宽等）。基线其余命中 25 条全部按归属登记（a1/a2 已判 22、待 S05b2 3）。B.3 逐文件回读本片 7 份：新增文本无情节示例（骨架比对不适用）、相对链接无断链、新增 4 表分隔行齐全、共写文件与 b2 写入节段互斥。**本片落点零违规，可交 W4 独立隔离回读。**
