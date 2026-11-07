# W4-09 `field_ids` 冻结独立判定报告（QF 席 · 非作者）

- 日期：2026-11-06
- 席位：W4-r2 QF 席，`field_ids` 冻结独立判定；**非作者**，只读判定 + 仅写本报告
- 判定对象：`notes/delivery-preflight-spec/delivery-preflight-spec.json` 的 8 条 templates／99 个 `field_ids`
- 任务来源：收口席 A 记「field_ids 未冻结（W4-09）：须由非作者按 `inputs/requirements.md` 判定哪些族真要求逐项可填」（`delivery-preflight-spec.json:3`、`INDEX.md:82`）

---

## 0. 判定边界与不变量

- **写入范围**：仅本文件 `notes/quality/field-ids-verdict-2026-11-06.md`。未改 `delivery-preflight-spec.json`、`INDEX.md`、`field-id-matrix.md`、任何 `output/`、`review.json`、`checklist.md`、`log.md`、总账；未做 git 写操作。
- **验证权限**＝static：未跑测试／构建／宿主／真实任务；未运行 `kd_delivery_preflight.py`（`INDEX.md:3`、R18 §6:166 通过亦仅 `STATIC_ONLY_SEMANTICS_NOT_PROVEN`）；`grep` 统一 `/usr/bin/grep -rnE`。
- **已读**：`inputs/requirements.md`；`skills/knowledge-compiler/references/r18-consumer-operations.md`；`notes/delivery-preflight-spec/**`（json／matrix／INDEX／8 份 spec.md）；8 个成品包的 `templates/*.md`；`notes/quality/*/brief.json` 的枚举面字段。
- **未读**：`review.json` 及其档位、`notes/w4-*`、`log.md`、`checklist.md`、其他分片 ledger、`docs/plans/**`、v0–v3 提交（`git show` 禁用）、`scratchpad/**`（唯一下述例外）。
- **scratchpad 例外**：任务 5 明确要求「与 `scratchpad/repair-tree-after-2026-11-06.tsv` 只读比对」，构成对该**单一文件**的显式只读授权（特殊授权优于一般禁读）。本席只读此 1 个 tsv 的 8 行件数／字节列，`scratchpad/` 其余内容一律未读。此边界解读在此留痕，供主代理复核。

---

## 1. 判据原文（不凭编号前缀猜）

| 判据 | 位置 | 要点 |
|---|---|---|
| 需求层 | `inputs/requirements.md:11` | 只要求 8 个 skill「满足 knowledge-compiler 对成品 Skill 的要求（R18 §1–4、**§2a–2d**…）」——是**规范引用** |
| 需求层 | `inputs/requirements.md:13` | 「重点是反例、失败出口、适用条件、**模板字段**和机制卡」——是**泛重点**，未列任何 N 项维度／字段清单 |
| R18 §2a | `r18-consumer-operations.md:41` | 「**若用户要求独立记录 N 项维度/步骤/字段**，先从确认的 requirements 中**冻结 N 个唯一 ID**和对应消费者」——触发条件是需求侧的 N 项枚举 |
| R18 §2a | `r18-consumer-operations.md:43` | 「对每个 ID 留下独立一行或独立字段…**不强制为不适用字段生造事实，不要求每项都填满**」 |
| R18 §2a | `r18-consumer-operations.md:46` | 「**如果用户只要求总体摘要，单行不会成为缺陷**」 |
| R18 §6 | `r18-consumer-operations.md:126` | 「**有明确枚举可填字段时**，可以在…`delivery-preflight-spec.json` 中记录要求」 |
| R18 §6 | `r18-consumer-operations.md:138` | 「必须从**真实需求和已读材料**生成完整 field_ids；Markdown 模板每个字段 ID 应位于**独立表格行的第一列**」 |
| R18 §6 | `r18-consumer-operations.md:165` | 「**没有枚举模板的简单成果，不需要写空 spec**」 |
| 作者裁决 #3A | 题面给定；落地见 `character-and-narrative-control.md:27`（W4-47 边界句） | 「整册交付时按 `narrative-workbook.md:3` 先只挑用得上的节（**占位行即合法可填面**）…两者是「先选节、再逐项成行」的先后取舍」 |

**根本张力（须写进冻结依据）**：唯一的判据源 `requirements.md` 第 11／13 行**没有枚举任何「独立记录 N 项维度」的清单**；R18 §2a:41 的冻结触发条件在需求层无对应物。因此本报告的 A 类只是「**模板正文自述明文**」层面的可冻候选，**不是**「需求已确认 N 项」层面的冻结。此点独立构成 W4-09 不宜销账的理由之一（见 §5）。

**分类口径**（照题面）：
- **A 真要求逐项可填**：模板正文确有「每个编号独占一行」／「逐项填写」类明文，且成品里存在对应编号卡体；
- **B 占位行即合法可填面（#3A）**：模板只有占位示例行、正文写明「按任务只填用得上的那几节」，无逐项成行要求；
- **C 未能核实**：证据不足、编号族与模板正文对不上、或有同名异指。

---

## 2. 8 条 templates 与各自 `field_ids`（逐条列）

来源 `delivery-preflight-spec.json:4-152`；数量按 JSON 数组实点，连续性按编号序列核，卡体行号由 `/usr/bin/grep -rnE '^\| (前缀)-[0-9]'` 实测。

| # | path（JSON `path`） | 数量 | 前缀 | 编号连续无缺号 | JSON 行号 |
|---|---|---|---|---|---|
| 1 | `output/story-architecture-and-longform-planning/templates/plot-canvas.md` | 12 | PA | ✓ `PA-01…12` | `:6`,`:9-20` |
| 2 | `output/story-architecture-and-longform-planning/templates/plot-diagnosis-report.md` | 10 | DR | ✓ `DR-01…10` | `:24`,`:27-36` |
| 3 | `output/story-architecture-and-longform-planning/templates/plot-scene-table.md` | 24 | ST | ✓ `ST-01…24` | `:40`,`:43-66` |
| 4 | `output/character-and-narrative-control/templates/narrative-workbook.md` | 3 | PV | ✗ **跳号**：`PV-04 / PV-09 / PV-14` | `:70`,`:73-75` |
| 5 | `output/fiction-planning-and-diagnosis/templates/diagnosis-report.md` | 12 | DR | ✓ `DR-01…12` | `:79`,`:82-93` |
| 6 | `output/fiction-planning-and-diagnosis/templates/novel-plan.md` | 14 | NP | ✓ `NP-01…14` | `:97`,`:100-113` |
| 7 | `output/fiction-planning-and-diagnosis/templates/revision-sheet.md` | 12 | RV | ✓ `RV-01…12` | `:117`,`:120-131` |
| 8 | `output/fiction-planning-and-diagnosis/templates/scene-plan.md` | 12 | SP | ✓ `SP-01…12` | `:135`,`:138-149` |

合计 **8 条／99 个**（12+10+24+3+12+14+12+12=99），与 `INDEX.md:16`、`field-id-matrix.md:69` 一致。

补充实测：模板正文首列真 ID 行数＝`plot-canvas.md` 12（`:11-22`）、`plot-diagnosis-report.md` 10（`:9-18`）、`plot-scene-table.md` 24（`:11-34`）、fiction 四件 12/14/12/12（`diagnosis-report.md:8-19`、`novel-plan.md:9-22`、`revision-sheet.md:8-19`、`scene-plan.md:8-19`）——与 JSON 逐条相符。**但 JSON 未收模板正文里的 `DR-SUM`**（`plot-diagnosis-report.md:19`、`diagnosis-report.md:20`），亦未收 `DR-11/12` 于 story 侧；`field-id-matrix.md:91` 自承 99 是「可跑预检的**下界清单**，不是全集」。

---

## 3. 逐族判定（A／B／C）与 `文件:行` 证据

### 3.1 A 类（3 族／46 个）——能冻候选

**① PA-01…12（12，`plot-canvas.md`）＝ A**
- 明文：`plot-canvas.md:3`「先填 §1 的 `PA-01`–`PA-12` 字段行（**每个 ID 独占一行**…）」「**字段 ID 供逐项核对**」「**留空不等于完成**」。
- 逐行验收：`plot-canvas.md:69`「`PA-01`–`PA-12` **每行有值或「未知」**，状态与稿件证据位置已按 §1 口径填写或标「未知」」。
- 卡体：`plot-canvas.md:9` 表头「字段 ID | 字段 | 填写口径 | 填写 | 状态 | 稿件证据位置」；`:11-22` 为 `PA-01…12` 连续真 ID 行。
- 判：逐项明文 + 完成检查 + 卡体三者齐备，无跳过条款 → **A**。

**② DR-01…10（10，`plot-diagnosis-report.md`，story 包）＝ A**（同名异指警示见 §3.3）
- 明文：`plot-diagnosis-report.md:3`「先填 §1 的 `DR-01`–`DR-10` 与 `DR-SUM` 字段行（**每个 ID 独占一行**）」；`:5` 标题「字段清单（DR-01–DR-10 + DR-SUM，**每 ID 一行**）」；`:3`「不得留空或猜」。
- 逐行验收：`:80`「`DR-01`–`DR-10` **每行有值**…没有空白冒充「无问题」」。
- 卡体：`:7` 表头；`:9-18` 为 `DR-01…10` 连续真 ID 行，`:19` `DR-SUM`。
- 判：明文 + 完成检查 + 卡体齐备 → **A**（但 `DR` 跨包同名异指，冻结前须解决命名空间，见未决项 1）。

**③ ST-01…24（24，`plot-scene-table.md`）＝ A**
- 明文：`plot-scene-table.md:3`「先看 §1 的字段清单（**每个 ID 独占一行**）…不知道写「未知」，**不要留空**」。
- 逐行验收：`:92`「`ST-01`–`ST-24` **各行的「填写／状态／稿件证据位置」已按 §1 口径回填或标「未知」**」。
- 卡体：`:9` 表头；`:11-34` 为 `ST-01…24` 连续真 ID 行。
- 判 → **A**。

> 三族共 46 个，恰等于 `INDEX.md:14` story 包「JSON field_ids 合计 46」，与 `story-architecture-and-longform-planning.md:16` 一致。

### 3.2 B 类（1 族／3 个）——按 #3A 保留占位面

**④ PV-04 / PV-09 / PV-14（3，`narrative-workbook.md`，character 包）＝ B**
- 明文（B 特征原话）：`narrative-workbook.md:3`「**按任务只填用得上的那几节，用不上的整节跳过**；不知道的格子写「未知」，不为填满而编」。
- 占位形态：`:132` §8「逐编号台账」；`:138-140` 三行 `PV-04 / PV-09 / PV-14` 是**填法示例**，`:142` 明写「**示例行只是填法示意，不是固定答案**」。
- 逐项明文为**条件性**、非全册要求：`:134`「审已有稿子、或一次改稿牵动多条规则时，把**用到的**规则编号逐条记一行。每个编号独占一行…」——只在「启用 §8」时成立，且对象为「用到的编号」，不是预印全集。
- 作者裁决落地：`character-and-narrative-control.md:27`（W4-47 边界句）「整册交付时按 `narrative-workbook.md:3` 先只挑用得上的节（**占位行即合法可填面**）…「先选节、再逐项成行」的先后取舍，不是二选一」。即 **#3A**。
- 判：模板只有占位示例行、正文有「按任务只填用得上的那几节」、整册交付无逐项成行要求 → **B**（保留占位面，不按 3 个 ID 逐项冻结）。编号跳号（04/09/14）亦印证它是选节示例而非枚举全集。

### 3.3 C 类（4 族／50 个）——未能核实，交作者

**⑤ DR-01…12（12，`diagnosis-report.md`，fiction 包）＝ C**
- **同名异指（确凿）**：story 侧 `plot-diagnosis-report.md:9-18` 与 fiction 侧 `diagnosis-report.md:8-19` 都使用 `DR-01…10` **字面完全相同的编号**，但字段语义不同——`DR-03`：story=「症状」(`plot-diagnosis-report.md:11`) / fiction=「证据」(`diagnosis-report.md:10`)；`DR-04`：story=「适用规则」(`:12`) / fiction=「症状」(`:11`)；`DR-09`：story=「回归检查」(`:17`) / fiction=「建议」(`:16`)；`DR-10`：story=「未决项（发现级）」(`:18`) / fiction=「回归项」(`:17`)。JSON 两条 templates 的 `field_ids` 均只写 `DR-01`、`DR-02`…**不带包路径**（`delivery-preflight-spec.json:27-36` 与 `:82-93`），冻结后无法区分所指。
- 无逐项明文，反有**跳填明文**：`diagnosis-report.md:4`「无文本 → **只填 DR-01/02/12** 和取样清单，**不填 DR-04…DR-11**」「只有梗概 → DR-01…09、DR-12 照填」；`:5`「未定项如实标未知…不要用套话填满」；`:48` 只有「**每行**的状态与稿件证据位置」的列级要求，无「每个 ID 独占一行」。
- 判：同名异指 + 按情形跳填明文，既不满足 A 的逐项门槛，也不满足 B 的「占位示例行」形态 → **C**。

**⑥ NP-01…14（14，`novel-plan.md`）＝ C**
- 无「每个 ID 独占一行」明文；`:41` 仅「**每行**的状态与稿件证据位置」；`:5`「未定项如实标「未知」或「待作者决定」，**不要用套话填满**；操作默认值…只作默认，不作硬门」。
- 反向明文：`novel-plan.md:43-53`「规划完成的最低标准」「**缺 3 项以上 → 不进入起草**」——即允许缺项，与「真要求逐项可填」冲突。
- 卡体：`:7` 表头、`:9-22` 真 ID 行齐备（非占位示例行），故不满足 B 的形态门槛。
- 判 → **C**。

**⑦ RV-01…12（12，`revision-sheet.md`）＝ C**
- 无「每个 ID 独占一行」明文；`:59` 仅「**每行**的状态与稿件证据位置」。`:17`／`:57` 的「逐项勾」指 `RV-10` 回归项**内部 6 项**（`:42-49`），不是 12 个 field_id 逐项。
- 反向明文：`revision-sheet.md:53`「**一单一个主目标**；不要把「结构重排 + 句段润色 + 校对」混在一单」；`:4`「未授权项记「待作者决定」」。
- 判 → **C**。

**⑧ SP-01…12（12，`scene-plan.md`）＝ C**
- 无「每个 ID 独占一行」明文；`:34` 仅「**每行**的状态与稿件证据位置」。
- 反向明文：`scene-plan.md:36-44`「起草前最低标准」「**缺 2 项以上 → 先补卡**」「作者要求直接写，就补假设并标「假设」」——允许缺项／跳填。
- 判 → **C**。

> **C 类的边界性（诚实标注，交作者复核）**：NP／RV／SP 三族**同时**具备「预印真 ID 卡体」（近 A）与「允许缺项／每行填状态」（近 B／#3A 占位面）两种特征，本席按「**存在允许缺项、跳填的反向明文**」从严判 C，不臆断其属 A 或 B。若作者认定 `:48`／`:41`／`:59`／`:34` 的「每行的状态与稿件证据位置」已构成 R18 §2a 的「逐项填写类明文」，则此三族可上抬为 A；该口径取舍列为**未决项 2**，本席不代裁。

### 3.4 计数

| 类别 | 族数 | `field_ids` 个数 | 族 |
|---|---|---|---|
| **A** | **3** | **46** | PA(12)、DR-story(10)、ST(24) |
| **B** | **1** | **3** | PV-04/09/14(3) |
| **C** | **4** | **50** | DR-fiction(12)、NP(14)、RV(12)、SP(12) |
| **合计** | **8** | **99** | 与 JSON 99 相符 |

---

## 4. 三套数字归因

### 4.1 同一口径内：**平**

`INDEX.md:7-14` 8 行「宽式唯一 ID」列逐行相加：
`25 + 4 + 83 + 494 + 0 + 0 + 23 + 87 = 716` ✓ 与 `INDEX.md:16`、`field-id-matrix.md:136` 的 **716** 相符。

`delivery-preflight-spec.json` 8 条 `field_ids` 相加：`12+10+24+3+12+14+12+12 = 99` ✓；`INDEX.md:7-14`「JSON field_ids 合计」列 `3+0+50+0+0+0+0+46 = 99` ✓。

差额 `716 − 99 = 617` ✓ 与 `INDEX.md:16` 相符。

### 4.2 差额 617 的精确归因（可核，不臆造）

全部来自 `INDEX.md:7-14` 同表内数字，逐包相减：

| 包 | 宽式唯一 ID | JSON field_ids | 差额 |
|---|---|---|---|
| genre-fiction-craft | 494 | 0 | **494** |
| story-architecture | 87 | 46 | 41 |
| character-and-narrative | 25 | 3 | 22 |
| fiction-planning | 83 | 50 | 33 |
| scene-conflict | 23 | 0 | 23 |
| cross-media | 4 | 0 | 4 |
| line-editing／preset-card | 0／0 | 0／0 | 0／0 |
| **合计** | **716** | **99** | **617** |

`494（genre 14 件题材模板未收进 JSON） + 123（非 genre 各包模板正文里的标题级／正文级非行级 ID：41+22+33+23+4） = 617` ✓ 与 `INDEX.md:16`「差额集中在 genre…以及各 skill 模板正文里的非行级 ID」、`field-id-matrix.md:91`「99 只取真 ID 行…不含任何 genre 编号…是下界清单」一致。**此层归因：平。**

### 4.3 跨口径：**不平，原因待核**

第三套数「包内编号全集」来自 `field-id-matrix.md` 首段「包内编号唯一集（任意形态）」：
story **82** (`:8`) + character **69** (`:16`) + fiction **119** (`:21`) + scene **55** (`:29`) + cross-media **40** (`:35`) + line-editing **56** (`:41`) + preset-card **0** (`:45`) + genre **442** (`:49`) = **863**。

`863 ≠ 716 ≠ 99`。**不平，原因待核**。可核线索（只列事实，不臆造差额结论）：

1. **统计对象不同**：matrix 首段是「**全包**任意形态编号唯一集」（含 SKILL.md／references／examples）；716 是「**模板件内宽式取词**唯一 ID」，宽式定义见 `field-id-matrix.md:97`（`\b([A-Z]{1,4}-[A-Z]{0,2}\d{1,3}[A-Z]?)\b`）；99 是「模板**首列真 ID 行**」。`story 82`（matrix:8）与 `story 87`（INDEX:14）即同一包两种口径的实证。
2. **genre 自承下界**：`field-id-matrix.md:66`「两段式集合 442 是**下界**，另有 **616 个三段式**编号未被捕获」；`:116` 递归复测 genre 14 件模板宽式 **494**。故 442 与 494 不可互代。
3. **无 templates 两包不入 716**：`INDEX.md:11-12` line-editing／preset-card 宽式唯一 ID 均为 0；`field-id-matrix.md:42`／`:46` 按 R18 §6「无 `templates/*.md` 不建 spec 条目」。但 line-editing **56**（`brief.json:33-35`：SR 16＋EN 40，两端连续无缺号）与 preset-card **点分标识 49**（`preset-card-generation.md:104`：`49＝34＋15`；`brief.json:45` 连字符编号 `PC-/SR-` 实测零命中，属取词盲区）**都在 863 或包内枚举面里、都不在 716 里**。
4. **动作未闭合**：`field-id-matrix.md:135`／`INDEX.md:59` 均记「genre 段 14 件模板编号普查（494／88／189）本批未逐件重跑，属 K5 冻结前重跑并归因范围」。

结论：**同一口径内（INDEX 表内 716／99／617）平；跨口径（863 全包任意形态 vs 716 模板内宽式 vs 99 首列真 ID 行）不平，原因待核**，三套数不是同一统计对象，硬凑差额即臆造；逐项复跑归主代理 K5 冻结前「编号普查」。

---

## 5. 冻结建议与 W4-09 能否销账

### 5.1 冻结建议

- **能冻的族清单（A 类，3 族／46 个）**：`PA-01…12`、`DR-01…10`（story `plot-diagnosis-report.md`）、`ST-01…24`。证据见 §3.1。**但附条件**：`DR` 跨两包同名异指，冻结前须先解决命名空间（未决项 1），否则此 46 个不可整体签「已冻结」。
- **按 #3A 保留占位面的族清单（B 类，1 族／3 个）**：`PV-04 / PV-09 / PV-14`。按 `narrative-workbook.md:3` 与 `character-and-narrative-control.md:27`（W4-47）**保留占位面，不按逐项成行冻结**。
- **须交作者的未决项**：C 类 4 族／50 个，及 §7 全部条目。`delivery-preflight-spec.json` 本体、`INDEX.md`、`field-id-matrix.md` 本席**一字未改**。

### 5.2 W4-09 能否在本轮销账：**不能**

理由全部落在证据上：

1. **8 族中 4 族（50 个）判 C 未决**，且 `DR-01…10` 跨 story／fiction 两包**同名异指**（`plot-diagnosis-report.md:9-18` vs `diagnosis-report.md:8-19`，字段语义不同），JSON `field_ids` 不带包路径（`delivery-preflight-spec.json:27-36`／`:82-93`），冻结即产出互相冲突的 ID 面。
2. **需求层缺冻结依据**：`requirements.md:11`／`:13` 只引用 R18 §2a–2d 与「模板字段」为泛重点，未枚举任何「独立记录 N 项」；R18 §2a:41 的「用户要求独立记录 N 项维度」触发条件在需求层无对应。A 类只是「模板自述明文」层面的可冻候选，非「需求已确认」层面的冻结。
3. **决定逐项成行前提的两条仍开放且明记交作者**：`INDEX.md:30`／`:37`「占位行是否算可填字段（W4-11／W4-79）、四行「同上」是否算实质填充（W4-70）…**交作者定，本席不代裁**」。
4. **前置依赖未销**：`INDEX.md:23` 需先销 W4-45／W4-47／W4-52 与 K4 非作者对「prose／标题级 ID 是否构成枚举模板」的判定；`field-id-matrix.md:135`／`INDEX.md:59` 记 genre 14 件模板编号普查未逐件重跑，属 K5 冻结前未闭合。
5. **验证权限 static**：未跑 `kd_delivery_preflight.py`（`INDEX.md:3`），R18 §6:166 明确即便通过也只返回 `STATIC_ONLY_SEMANTICS_NOT_PROVEN`；GQ5 维持 `NOT_PROVEN`（`INDEX.md:60`／`:82`）。

本席只提供判定依据与建议，**不代作者冻结、不签「spec 已交付」**。

---

## 6. INDEX.md 与 tsv 比对（任务 5）

比对对象：`notes/delivery-preflight-spec/INDEX.md:46-53`「修复批树重算」8 行件数／字节 ↔ `scratchpad/repair-tree-after-2026-11-06.tsv:1-8` 第 3／4 列（按本任务显式授权只读该单文件）。

| 包 | INDEX 件数/字节 | tsv 件数/字节 | 一致 |
|---|---|---|---|
| character-and-narrative-control | 17 / 194,854 | 17 / 194854 | ✓ |
| cross-media-drama-adaptation | 13 / 75,549 | 13 / 75549 | ✓ |
| fiction-planning-and-diagnosis | 27 / 349,507 | 27 / 349507 | ✓ |
| genre-fiction-craft | 101 / 1,058,396 | 101 / 1058396 | ✓ |
| line-editing-and-proofreading | 10 / 114,289（1,303 行） | 10 / 114289 | ✓ |
| preset-card-generation | 11 / 115,304（1,347 行） | 11 / 115304 | ✓ |
| scene-conflict-and-rhythm | 17 / 169,017 | 17 / 169017 | ✓ |
| story-architecture-and-longform-planning | 21 / 284,595 | 21 / 284595 | ✓ |

**结论：8 行件数／字节全部一致**（tsv 第 9 行为尾随空行，非差异）。附带核：tsv 第 2 列 tree_sha256 亦与 `INDEX.md:72-79`「K5 冻结回填」8 行逐行相符。

**边界说明**：题面所问「修复批造成**行号位移**」属**行号锚**层面，不在本次「件数／字节」比对范围内；`INDEX.md:59` 自承「两结构性 spec 正文内大量 `SKILL.md:NNN`／`workflow.md:NNN` 行号锚依修复前树…逐锚重测属 K5 冻结前「锚抽验」范围，本席未逐条重测，不在此批闭合」。该未闭合项照录于 §7 第 10 条，不计作本次比对的不一致。

---

## 7. 未决项清单（须交作者）

1. **DR 同名异指**：`DR-01…10` 同时出现在 story `plot-diagnosis-report.md:9-18` 与 fiction `diagnosis-report.md:8-19`，字面重叠、字段语义不同；JSON `field_ids` 无包路径。须裁：是否加包前缀／命名空间，或按包隔离冻结。
2. **fiction 4 族归类口径**：NP／RV／SP／DR-fiction（50 个）无「每个 ID 独占一行」明文，反有跳填／缺项明文（`diagnosis-report.md:4`、`novel-plan.md:53`、`scene-plan.md:44`、`revision-sheet.md:53`），本席从严判 C；若「每行的状态与稿件证据位置」（`:48`／`:41`／`:59`／`:34`）被认定构成「逐项填写类明文」，可上抬为 A。须裁。
3. **占位行是否算可填字段（W4-11／W4-79）**：本轮按 #3A「占位行即合法可填面」判 B；该裁决对 scene／cross-media／line-editing 的占位台账（`field-id-matrix.md:74`、`:79-82`）及 fiction 4 族的空填值格是否一体适用，须作者确认（`INDEX.md:30`／`:37`）。
4. **四行「同上」是否算实质填充（W4-70）**：影响逐项成行判定（`INDEX.md:30`／`:37`）。
5. **需求层无 N 项枚举**：`requirements.md:11`／`:13` 未列任何 N 项维度清单，R18 §2a:41 触发条件缺对应；A 类冻结依据是否成立须作者确认。
6. **genre 14 件题材模板**：列形与 §2a 两案（W4-52，`field-id-matrix.md:124`）、宽式 494／标题级 88／独占行 189 的编号普查未逐件重跑（`field-id-matrix.md:135`、`INDEX.md:59`）。
7. **无 templates 两包的枚举面**：line-editing 56（`brief.json:33-35`，`line-editing-and-proofreading.md:69`／`:81`）、preset-card 点分标识 49（`preset-card-generation.md:92`／`:104`）是否属须逐项可填、是否另立项补模板；两包 JSON=0（`field-id-matrix.md:42`／`:46`）。
8. **K4 非作者判定**：「prose／标题级 ID 是否构成枚举模板」（`INDEX.md:23`）。
9. **前置依赖**：W4-45／W4-47／W4-52（`INDEX.md:23`）与 `INDEX.md:30` 两条开放项未销。
10. **行号锚位移**：两结构性 spec 的 `SKILL.md:NNN` 锚依修复前树、未逐锚重测，属 K5 冻结前锚抽验（`INDEX.md:59`）。

---

## 8. 本报告未做的事（复核用）

未改任何被判对象本体；未写 `output/`／`skills/`；未跑 `kd_*` 检查器、测试、构建、宿主或真实任务；未做 `git show`／v0–v3 提交读取／任何 git 写操作；未读 §0 未读清单所列文件；未自造 SHA、未提前冻结 `field_ids`、未签「spec 已交付」。`scratchpad/` 仅读任务 5 显式指定的那 1 个 tsv。
