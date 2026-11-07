# delivery-preflight-spec 取数矩阵（主代理机械实测，2026-11-05）

性质：**spec 的取数准备，不是已冻结的 spec**。R18 §6 要求 `field_ids` 必须来自已确认真实需求并已冻结的唯一 ID；本表只回答「哪些编号已经在模板里独占一行、哪些没有」，不判定哪些需求要求逐项可填。判定归 W4 由非作者按 requirements 做。

取词两法并列：首列独立行 `^\|\s*`?ID`?\s*\|`，标题式 `^#{2,6} …ID`。两者计数都打印，不以单档下结论。

## story-architecture-and-longform-planning
- 包内编号唯一集（任意形态）=82，族分布：DR:10, PA:12, PL:16, ST:24, SU:4, SV:16
- 模板 `templates/plot-canvas.md`：首列独立行 12 个（标题式 6 个）；样例 PA-01,PA-02,PA-03,PA-04,PA-05,PA-06
- 模板 `templates/plot-diagnosis-report.md`：首列独立行 10 个（标题式 3 个）；样例 DR-01,DR-02,DR-03,DR-04,DR-05,DR-06
- 模板 `templates/plot-scene-table.md`：首列独立行 24 个（标题式 5 个）；样例 ST-01,ST-02,ST-03,ST-04,ST-05,ST-06
- 模板 `templates/serial-tables.md`：首列独立行 0 个（标题式 10 个）
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：PL 缺 16 个（PL-01…）；SU 缺 4 个（SU-03…）；SV 缺 16 个（SV-01…）

## character-and-narrative-control
- 包内编号唯一集（任意形态）=69，族分布：PS:30, PV:17, SC:1, SU:3, TM:18
- 模板 `templates/narrative-workbook.md`：首列独立行 3 个（标题式 0 个）；样例 PV-04,PV-09,PV-14
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：PS 缺 30 个（PS-01…）；PV 缺 14 个（PV-01…）；SC 缺 1 个（SC-06…）；SU 缺 3 个（SU-04…）；TM 缺 18 个（TM-01…）

## fiction-planning-and-diagnosis
- 包内编号唯一集（任意形态）=119，族分布：CL:14, DR:12, FC:21, NP:14, PL:3, PV:2, RF:12, RS:14, RV:12, SP:12, SU:3
- 模板 `templates/diagnosis-report.md`：首列独立行 12 个（标题式 0 个）；样例 DR-01,DR-02,DR-03,DR-04,DR-05,DR-06
- 模板 `templates/novel-plan.md`：首列独立行 14 个（标题式 0 个）；样例 NP-01,NP-02,NP-03,NP-04,NP-05,NP-06
- 模板 `templates/revision-sheet.md`：首列独立行 12 个（标题式 1 个）；样例 RV-01,RV-02,RV-03,RV-04,RV-05,RV-06
- 模板 `templates/scene-plan.md`：首列独立行 12 个（标题式 0 个）；样例 SP-01,SP-02,SP-03,SP-04,SP-05,SP-06
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：CL 缺 14 个（CL-01…）；FC 缺 21 个（FC-01…）；PL 缺 3 个（PL-04…）；PV 缺 2 个（PV-12…）；RF 缺 12 个（RF-01…）；RS 缺 14 个（RS-01…）；SU 缺 3 个（SU-15…）

## scene-conflict-and-rhythm
- 包内编号唯一集（任意形态）=55，族分布：AF:18, PL:1, SC:14, SU:19, SV:3
- 模板 `templates/action-checklist.md`：首列独立行 0 个（标题式 0 个）
- 模板 `templates/scene-workbook.md`：首列独立行 0 个（标题式 5 个）
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：AF 缺 18 个（AF-01…）；PL 缺 1 个（PL-11…）；SC 缺 14 个（SC-01…）；SU 缺 19 个（SU-01…）；SV 缺 3 个（SV-04…）

## cross-media-drama-adaptation
- 包内编号唯一集（任意形态）=40，族分布：AD:40
- 模板 `templates/adaptation-workbook.md`：首列独立行 0 个（标题式 2 个）
- 模板 `templates/interactive-branch-sheet.md`：首列独立行 0 个（标题式 0 个）
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：AD 缺 40 个（AD-01…）

## line-editing-and-proofreading
- 包内编号唯一集（任意形态）=56，族分布：EN:40, SR:16
- **无 `templates/*.md`**：按 R18 §6 不建 spec 条目；若编号需在交付时逐项可填，另立项补模板。

## preset-card-generation
- 包内编号唯一集（任意形态）=0，族分布：
- **无 `templates/*.md`**：按 R18 §6 不建 spec 条目；若编号需在交付时逐项可填，另立项补模板。

## genre-fiction-craft
- 包内编号唯一集（任意形态）=442，族分布：AT:18, CO:7, CY:13, HI:90, HO:64, IR:7, IS:20, MY:7, PR:7, RL:10, RO:50, SD:14, SF:39, WX:96
- 模板 `references/02-romance/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/03-horror/templates-and-cases.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/04-wuxia-xianxia-fantasy/templates-and-cases.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/05-science-fiction/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/06-historical-alternate/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/07-survival-disaster/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/08-adventure-treasure/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/09-comedy/templates-and-examples.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/11-identity-revenge-intrigue/templates-and-examples.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/12-children-youth/templates.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/13-isekai-time-travel/templates-and-cases.md`：首列独立行 0 个（标题式 0 个）
- 模板 `references/14-period-realism/templates-and-examples.md`：首列独立行 0 个（标题式 0 个）
- 未成模板独立行的编号（**是否属须逐项可填字段，须按 `inputs/requirements.md` 判，本表不判**）：AT 缺 18 个（AT-01…）；CO 缺 7 个（CO-01…）；CY 缺 13 个（CY-01…）；HI 缺 90 个（HI-01…）；HO 缺 64 个（HO-01…）；IR 缺 7 个（IR-01…）；IS 缺 20 个（IS-01…）；MY 缺 7 个（MY-01…）；PR 缺 7 个（PR-01…）；RL 缺 10 个（RL-01…）；RO 缺 50 个（RO-01…）；SD 缺 14 个（SD-01…）；SF 缺 39 个（SF-01…）；WX 缺 96 个（WX-01…）

## 取词式覆盖边界与更正（主代理追加，2026-11-05 14:39；不删上文，只限定其效力）

- 本表取词式只覆盖**两段式** `XX-01`。实测 genre 另有 **616 个三段式**编号（`AT-D01`、`HI-C01`、`RO-K121`、`WX-T01` 一类，`grep -oE "\b[A-Z]{2,3}-[A-Z][0-9]{1,3}\b" | sort -u`）未被捕获。故 genre 那行「包内编号唯一集＝442」是**下界**，不得当 genre 卡号全集引用，也不得据此判「三段式卡号全都缺模板行」。
- 反向也成立：两段式集合里含 `RO-01…RO-05` 这类与三段式 `RO-K121` 并存的写法，**是否同一族不可由取词式判定**，须按卡体逐条对；本表不判。
- 快照时点：genre 的 01／03／06／07／10／11 目录此刻正被第 15／16／17 批席位并行落笔（06、11、03 已在 14:25–14:27 各净增数 KB），本表 genre 段是**中途快照**，W4 冻结前须重跑一次并把差额归因到本片落笔。
- `delivery-preflight-spec.json`（同目录）只收 **8 条非 genre 模板**、合计 99 个 `field_ids`，全部来自「模板文件首列独立行」实测，不含上述下界数字，也不含 `source_index` 键（R18 §6 拒绝）。它是**取数准备**：R18 §6 要求 `field_ids` 来自已确认真实需求并冻结的唯一 ID，冻结与判定归 W4，本轮不签「spec 已交付」。


## 第四形态复测与 W4-11 收窄（主代理追加，2026-11-05 14:51；上文两档计数保留不改）

- **触发的错误**：上文只数「首列是真实编号的行」与「首列是标题的行」两档，于是把 scene 与 cross-media 记成「模板首列 0 行」。第三档复测发现：这两个包的台账**用的是占位行**，不是预印真 ID 行——`scene-workbook.md` §7 有「每个编号独占一行」声明＋`| 编号 | 值 | 状态 | 稿件证据位置 |` 表头＋`<规则编号，如 SU-02 / SU-06 / SU-19>` 占位行；`adaptation-workbook.md:53–57` 同构（占位示例 AD-01／AD-07／AD-19）。**故「0 行」是取词假象，不是交付缺口**。
- **四档复测全表**（声明／台账表头／占位行／真 ID 行；`specgen.py` 的 2.0 版判据）：

| 包 | 模板 | 声明 | 表头 | 占位行 | 真 ID 行 |
|---|---|---|---|---|---|
| character | `narrative-workbook.md` | 1 | 1 | 0 | 3 |
| cross-media | `adaptation-workbook.md` | 1 | 1 | **1** | 0 |
| cross-media | `interactive-branch-sheet.md` | 0 | 0 | 0 | 0 |
| scene | `scene-workbook.md` | 1 | 1 | **1** | 0 |
| scene | `action-checklist.md` | 0 | 0 | 0 | 0 |
| story | `plot-canvas.md`／`plot-diagnosis-report.md`／`plot-scene-table.md` | 0 | 0 | 0 | 12／10／24 |
| story | `serial-tables.md` | 0 | 0 | 0 | **0** |
| fiction-planning | `diagnosis-report／novel-plan／revision-sheet／scene-plan` | 0 | 0 | 0 | 12／14／12／12 |
| genre | `07-survival`／`08-adventure`／`12-children`／`13-isekai`／`14-period`／`02-romance` templates | 0 | 0 | 0 | 32／37／26／15／19／60 |
| genre | `03-horror`／`04-wuxia`／`05-science`／`06-historical`／`09-comedy`／`11-identity` templates | 0 | 0 | 0 | **0** |

- **收窄后的真缺口候选（只有这些，且仍未按 requirements 判定是否属须逐项可填）**：scene `action-checklist.md`（AF 族 18 个编号在包内但模板无台账）、cross-media `interactive-branch-sheet.md`、story `serial-tables.md`（SV 族 16 个）、genre 六个题材目录的模板（03／04／05／06／09／11 真 ID 行 0——但这六目录的卡号大量以 `###` 标题或第二列承载，**首列判据对它们不适用**，须换形态再测，本节不下结论）。
- **仍成立的结论**：`delivery-preflight-spec.json` 的 99 个 field_ids 只取「真 ID 行」，因此**不含 scene／cross-media 的占位台账**，也不含任何 genre 编号——它是可跑预检的下界清单，不是全集。W4 若要把 scene／cross-media 纳入预检，须先决定占位行是否算可填字段（R18 §2a 的判据是「每个 ID 独立一行或独立字段」，占位行满足结构、但不满足「从需求 ID 逐项找到」的反向验证）。

## genre 递归枚举复测（主代理追加，2026-11-05 15:50；上文 genre 行「未计入」的效力被本节替代）

上文 §genre 记「模板嵌在 14 个题材子目录内，本轮未计入」。本轮补递归扫描 `output/genre-fiction-craft/references/*/{*templates*,*worksheets*}.md`：实测 **14 个题材目录各命中 1 件、共 14 件模板**（这些目录内 md 文件共 99 件）。

取词改为宽式 `\b([A-Z]{1,4}-[A-Z]{0,2}\d{1,3}[A-Z]?)\b`。上文所用窄式 `[A-Z]{2}-\d\d[A-Za-z]?` 对 `HO-T01`、`IS-X01` 两族**恒零命中**——同一条测试串实测回显：窄式命中 `[]`，宽式命中 `['HO-T01', 'IS-X01', 'MY-02B', 'PR-06A', 'CY-07']`。这是本节复测的直接理由（漏计风险），不是重新判分；上文数字保留不改，只限定其效力。

| 题材目录 | 模板件 | 宽式唯一 ID | 其中标题级 | 其中正文级 | ID 独占表行首列 | 空编号列表头行数 | ID 样例 |
|---|---|---|---|---|---|---|---|
| 01-mystery | worksheets-and-cases.md | 12 | 6 | 6 | 0 | 0 | MY-02B MY-03A |
| 02-romance | templates.md | 98 | 0 | 98 | 60 | 1 | RO-01 RO-02 |
| 03-horror | templates-and-cases.md | 26 | 26 | 0 | 0 | 0 | HO-C01 HO-C02 |
| 04-wuxia-xianxia-fantasy | templates-and-cases.md | 108 | 33 | 75 | 0 | 0 | WX-01 WX-02 |
| 05-science-fiction | templates.md | 30 | 0 | 30 | 0 | 0 | SF-01 SF-02 |
| 06-historical-alternate | templates.md | 53 | 12 | 41 | 0 | 0 | HI-01 HI-06 |
| 07-survival-disaster | templates.md | 32 | 0 | 32 | 32 | 1 | SD-T01 SD-T02 |
| 08-adventure-treasure | templates.md | 55 | 0 | 55 | 37 | 1 | AT-01 AT-02 |
| 09-comedy | templates-and-examples.md | 1 | 1 | 0 | 0 | 0 | CO-06 |
| 10-profession-competition | worksheets-and-cases.md | 14 | 4 | 10 | 0 | 0 | PR-01A PR-01B |
| 11-identity-revenge-intrigue | templates-and-examples.md | 5 | 5 | 0 | 0 | 0 | IR-06 IR-06A |
| 12-children-youth | templates.md | 26 | 0 | 26 | 26 | 2 | CY-T01 CY-T02 |
| 13-isekai-time-travel | templates-and-cases.md | 15 | 1 | 14 | 15 | 1 | IS-X01 IS-X02 |
| 14-period-realism | templates-and-examples.md | 19 | 0 | 19 | 19 | 2 | RL-D01 RL-D02 |

求和回显（逐件相加）：宽式唯一 ID 合计 **494** ＝ 标题级 **88** ＋ 正文级 **406**；有 ID 的模板件 **14** 件、完全无 ID 的 **0** 件；**ID 独占表行首列合计 189 行，集中在 6 件模板内**（02(60), 07(32), 08(37), 12(26), 13(15), 14(19)）；另 8 件为 0（01-mystery, 03-horror, 04-wuxia-xianxia-fantasy, 05-science-fiction, 06-historical-alternate, 09-comedy, 10-profession-competition, 11-identity-revenge-intrigue）；带「编号／字段编号／ID」列头的行为 **8 行**。

三档定性（判据＝ID 出现在哪一层，对照 R18 §2a「编号独占一行＋值／状态／稿件证据位置」）：

- **A 档｜ID 只出现在正文级（prose 或表格内容列），无 ID 独占行**：8 件——01-mystery, 03-horror, 04-wuxia-xianxia-fantasy, 05-science-fiction, 06-historical-alternate, 09-comedy, 10-profession-competition, 11-identity-revenge-intrigue。
- **B 档｜ID 只出现在标题级**：编号形带字母中缀（`HO-T##`、`IS-X##`），窄式取词对其恒零命中，标题级合计 88 个。
- **C 档｜模板表体有「编号／ID」列但整列为空**：属用户填的空白行，既非预置编号全集、也非占位假数据；07、12、13、14 四件在此列（列头行数见上表）。

对 22.4 第 4 项的影响：genre 侧现存的编号全集只有 prose／标题两种层级（宽式合计 494 个，逐件见上表），**6 件已具备 ID 独占行（合计 189 行），但列名与 §2a 的「值／状态／稿件证据位置」不同形（表头列数：3 列／4 列／5 列／6 列）；8 件无 ID 独占行**。`delivery-preflight-spec/genre-fiction-craft.md` 要满足 §2a 只有两条路——① 新建一张符合 §2a 列形的表（动 14 件，且与各件自带的「按任务选择、不强制填满」声明冲突）；② 按 R18 §6 判 genre 属「无枚举模板」不建 spec，并在 spec 索引写理由。**两案代价入 W4-52 登记，本轮不改成品。**

诚实边界：本节只证「ID 出现在哪一层」与「空列是否存在」，不判这些表够不够用；A／B 档的 prose／标题级 ID 是否构成「枚举模板」取决于需求原文，归 W4 非作者判定（承 22.4 第 4 项补条与 §二十六 口径）。同一件内 A／B／C 可并存，档位按件内形态分列计数，不按件排他。

### 更正注（主代理自纠，2026-11-05 15:52；只改本节内三处判 0 的表述，不改上文历史数字）

上节正文写完即复测发现三处表述与回显不符，已就地更正，此处留痕：① 「ID 独占表行首列 14 件全为 0」错——实测合计 **189 行**，分布在 02-romance＝60 行、07-survival-disaster＝32 行、08-adventure-treasure＝37 行、12-children-youth＝26 行、13-isekai-time-travel＝15 行、14-period-realism＝19 行，另 8 件为 0；② 「没有任何一件 genre 模板把编号做成逐行可填」错——6 件已经是 ID 独占行；③ 由此 W4-52 的「无一具备」与「从零建表」表述一并改为「列形不合 §2a、需统一列名或判不建 spec」。根因：同一脚本内先跑窄式（表行首列 0）后跑宽式，正文按窄式结论落笔、求和行按宽式回显，两套取词的差额没有逐档对齐——与 `feedback-mechanical-field-extraction-traps` 的「取词式改版必复跑并双档回显」同型，本轮再犯，登记为方法缺陷而非成品缺陷。表头实测（6 件）：02-romance→ID／字段／填写内容／何时使用／规则／例子/校验 | 07-survival-disaster→编号／字段／已定事实/位置/版本／解释与反面信号／建议/替代／回看/未知 | 08-adventure-treasure→编号／对象／条件与动作提示／规则／事实/推断/建议、证据或文本位置、成本/结果

### 修复批时点更新（2026-11-06，收口席 A 内容层）

- 上文「快照时点」条（第 68 行）所记「genre 的 01／03／06／07／10／11 目录此刻正被并行落笔、genre 段是中途快照」的**时点条件随修复批收口而解除**：现树 genre 已稳定为 **101 件／1,058,396 B**（`scratchpad/repair-tree-after-2026-11-06.tsv` 与现树实测），树哈希＝**待主代理 K5 冻结**（本席不自造 SHA）。历史数字按本文件惯例保留不改，只限定其效力。
- 但「W4 冻结前须重跑一次并把差额归因」的**动作仍未闭合**：genre 段 14 件模板的编号普查（宽式唯一 ID 494、标题级 88、ID 独占表行 189）本批未逐件重跑，属主代理 K5 冻结前「锚抽验／编号普查」范围，登记为未闭合。
- 本批已复测：`INDEX.md` 求和回显（模板件 27／ID 独占表行 296／宽式唯一 ID 716／JSON field_ids 99／差额 617）与 8 份逐 skill spec 首表逐件一致，未改；`delivery-preflight-spec.json` 的 8 条 templates／99 个 field_ids 原样未动，field_ids 冻结明确标注「待整树 SHA 冻结后」（W4-09），本批不提前冻结。逐处见 `notes/repair-ledger-brief-spec-2026-11-06.md`。
