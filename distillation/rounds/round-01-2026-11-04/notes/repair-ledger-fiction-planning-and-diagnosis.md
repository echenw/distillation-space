# 修复批分片 ledger · fiction-planning-and-diagnosis（R5 席，2026-11-06）

- 席／Owner：R5 席，唯一 Owner 包 `output/fiction-planning-and-diagnosis/`。作者答复「全部按推荐」，修复批已发车；本席只做直接落笔，不重新设计、不替作者裁新口径、不扩大范围。
- 依据：`notes/repair-ledger-2026-11-06.md`（总账／裁决表／第五节未闭合项，本席只读）、`notes/repair-workplan-2026-11-06.md` §二 #10A 与 §三 fp SEM／GQ3／W4-14/15、`notes/user-decisions-2026-11-05.md` #10 原文、`notes/suite-contract.md` §2.1／§4.2／§4.2bis／§五、`notes/quality/fiction-planning-and-diagnosis/review.json`（GQ2/GQ3、semantics SEM-01…07、findings F-01…F-10、interfaces IF-01…07）、`notes/w4-closure-2026-11-05.md` §六 CL-verify 6.1／6.3、`notes/w4-review-queue.md` W4-15 原文、`notes/loss-inventory/fiction-planning-and-diagnosis-S06a3.md` LI-FP-134（RV-05 先例），以及本包 output 27 文件全文。
- 写入范围（严格）：本包 `output/fiction-planning-and-diagnosis/` 内 13 个文件、本分片 ledger、`notes/quality/fiction-planning-and-diagnosis/r5-appendixB-selfcheck-2026-11-06.md`。未写 `brief.json`／`review.json`／`k5-bindings-*.tsv`／`checklist.md`／`log.md`／`desourcing-ledger.md`／总账／其他 7 包／`skills/`／计划文档／`notes/delivery-preflight-spec/`；未做 git 写操作；未跑测试／构建／真实任务（GQ5 维持 NOT_PROVEN，未授权）。
- 定位方式：按内容定位，行号只作线索；改后行号已逐处回读确认。
- 行号备注：`SKILL.md` 在 :45 后新增 6 行、§8 自查后新增 1 行 ⇒ 原 :46 起 +6、原 :307 起再 +1（合计 +7）。位移影响 brief 锚（含 F-05 `fp:147` 裸对端行号，现为 :153），归主代理 brief 层统一处理，本席未碰 `brief.json`。

## 一、逐处改动（位置／改前／改后／依据／裁决编号）

| # | 位置（改后行号） | 改前 | 改后 | 依据 | 裁决编号 |
|---|---|---|---|---|---|
| 1 | `SKILL.md:71`（原 :65） | 缺赛道的信息时，给两三个赛道方案和各自的代价，按最可能的一个往下做，标“暂定”；只有答案会彻底改变方案时才停下来问，…… | 缺赛道的信息时，按 §3「规划新作」的「缺料或冲突时」一句处理（FC-01 卡住时）；……（保留同句后半「只问最影响判断的一项」） | `review.json` SEM-01／F-03／FP-T1：:86 为权威行且与 `rules-premise-and-structure.md:42`、`planning.md:43` 三处一致，:65 为相反指令；二选一归口取 :86，:65 改引用，不新造口径 | SEM-01 |
| 2 | `SKILL.md:117`（原 :111） | 只说“太长”、没有目标字数时，给**两三个**删减方案和代价 | 给**三个**删减方案和代价 | `review.json` SEM-02／F-04／FP-T7；「三个」逐字取 `references/revision.md:14`「给三个删减方案与代价」，与 :19「删减方案 A/B/C」同档 | SEM-02 |
| 3 | `agents/openai.yaml:6` | 请先问清篇幅、媒介、类型和交付方式……材料不全时给出标明“假设”或“暂定”的方案，**最多问我三个问题** | 请按我的素材、构思或稿子做……；材料不全时，**缺少关键输入只问最影响判断的一项，其余列为假设或待确认，把补的假设列出来请作者确认** | `review.json` SEM-03／F-05／FQ-G08／FQ-AP-09：提问口径归口到 SKILL 正文；措辞逐字取 `SKILL.md:65`「只问最影响判断的一项，其余列为假设或待确认」与 `:64`「把假设列出来请作者确认」 | SEM-03 |
| 4 | `SKILL.md:219`（原 :213，FC-20 卡体） | 把类型当作和读者的约定，不是本体上的硬边界。**写之前列三到五个必要的特征和承诺，写完逐条验收**；…… | 把类型当作和读者的约定，不是本体上的硬边界；**题材契约由 `genre-fiction-craft` 登记，本 Skill 按 genre 的题材契约核对，缺项回本包登记**；…… | `user-decisions` #10 A、`repair-workplan` §二 #10A、`review.json` SEM-04／F-01／FQ-IF-05；genre 为唯一登记 Owner | #10A／SEM-04 |
| 5 | `references/diagnosis.md:309`（S8） | **对应规则**：FC-20（类型契约/市场约束分层）。 | **对应规则**：FC-20（按 `genre-fiction-craft` 的题材契约核对，缺项回本包登记／市场约束分层）。 | 同上（SEM-04 五处原文之一） | #10A／SEM-04 |
| 6 | `references/self-check-diagnosis.md:31` | 类型契约是**本 skill 自有的 FC-20，按契约自查**，题材专项技法转 `genre-fiction-craft` | **按 genre 的题材契约核对，缺项回本包登记**，题材专项技法转 `genre-fiction-craft` | 同上；转介行「题材专项技法转 `genre-fiction-craft`」原样保留 | #10A／SEM-04 |
| 7 | `SKILL.md:32`、`:153`（原 :147） | — | **未改**（转介行与症状速查再转列原样保留） | #10A 要求「不要删除或削弱已有的转介行」；已逐行回读确认在位 | #10A（核对无动作） |
| 8 | `references/rules-premise-and-structure.md:6` | 每条规则包含：层级、规则、适用场景、观察信号、分支与反信号、操作步骤、交付、反例、适用范围、卡住时的处理和**验证边界** | 每条规则包含：层级、规则、**用在、看什么、分支、怎么做、交付、反例、适用范围、卡住时、冲突处理** | `review.json` SEM-05／F-06／FQ-G01：声明 10 项含「验证边界」（条级实测 0 条），改为实测条级 11 项 bullet 名，逐字取自本文件 | SEM-05 |
| 9 | `references/rules-units-and-endings.md:6` | 同 #8 | 同 #8 | 同上 | SEM-05 |
| 10 | `references/rules-drafting.md:6` | 同 #8 | 同 #8 | 同上 | SEM-05 |
| 11 | `references/rules-revision-and-method.md:6` | 同 #8 | 同 #8 | 同上 | SEM-05 |
| 12 | `SKILL.md:272`（原 :266，§6 索引） | ……卡住时、**冲突处理与验证边界** | ……卡住时、**冲突处理** | 同上；「验证边界」只作文件级小节（`scope-and-conflicts.md` §4.3），不再列为条级字段 | SEM-05 |
| 13 | `SKILL.md:326`（原 :319） | 故事结构、长篇/连载架构成为主要问题时，转交**故事架构 Skill**。 | 转交 `story-architecture-and-longform-planning`。 | `review.json` SEM-07／F-08／FQ-IF-03：§9 五行泛称按包名不可回查；包名逐字取 §1 转介表 `:28` | SEM-07 |
| 14 | `SKILL.md:327`（原 :320） | 转交**场景冲突 Skill** | 转交 `scene-conflict-and-rhythm`（取 §1 `:29`） | 同上 | SEM-07 |
| 15 | `SKILL.md:328`（原 :321） | 转交**人物叙事 Skill** | 转交 `character-and-narrative-control`（取 §1 `:30`） | 同上 | SEM-07 |
| 16 | `SKILL.md:329`（原 :322） | 转交**语言精修 Skill** | 转交 `line-editing-and-proofreading`（取 §1 `:31`） | 同上 | SEM-07 |
| 17 | `SKILL.md:330`（原 :323） | 题材专属规则、媒介改编或外部事实核验超出当前能力时，说明边界并**交给相应专业流程**。 | 题材专属规则超出当前能力时转 `genre-fiction-craft`，媒介改编转 `cross-media-drama-adaptation`；外部事实核验超出当前能力时，说明边界，**本 Skill 不提供专业意见**。 | 同上；两处包名取 §1 `:32`/`:33`，末句逐字取 `SKILL.md:312`。「外部事实核验」套件内无具名接收方 ⇒ 未能定位，不臆造（见第五节） | SEM-07 |
| 18 | `references/scope-and-conflicts.md:33`（§2 引言新增一行） | 无该行；§2 为 K-01…K-19 19 行 | 新增：「以下 19 条只裁规则层争点；方案数、提问数、赛道缺项时停等还是继续这类交付口径不在此表，按 SKILL.md §2、§3 的对应行执行。」 | `repair-workplan` §三「scope-and-conflicts §2 K 表不扩（交付口径归口后引它）」；`review.json` GQ2 `arbitration_gap`（K 表只裁规则层争点、不裁交付口径）。**K 表 19 行未增未改** | SEM 收口／GQ2 |
| 19 | `SKILL.md:46` | 无 | 从 `story-architecture-and-longform-planning` 转入本 skill 的：注水诊断和删段方法；非虚构的事实核验与论证结构不在本 skill 范围（见「不在范围」）。 | `review.json` GQ3 basis「六向无对应接收行」、F-09；内容取 IF-03 `consumer_ref`／`one_way_evidence` 原文与 `SKILL.md:47`「不在范围」 | GQ3 |
| 20 | `SKILL.md:47` | 无 | 从 `scene-conflict-and-rhythm` 转入本 skill 的：选题、读者契约、资料核验、读者反馈、不确定用哪个 skill。 | 同上；逐字取 IF-02 对端 `scene/SKILL.md:25` 原文 | GQ3 |
| 21 | `SKILL.md:48` | 无 | 从 `character-and-narrative-control` 转入本 skill 的：新作规划入口、成稿整体诊断、读者反馈、事实核验、不确定用哪个 skill。 | 同上；逐字取 IF-01 对端 `character/SKILL.md:33` 原文 | GQ3 |
| 22 | `SKILL.md:49` | 无 | 从 `line-editing-and-proofreading` 转入本 skill 的：原创故事结构、整体诊断和内容层修订；不用润色掩盖因果或结构问题。 | 同上；逐字取 IF-04 对端 `line/SKILL.md:203` 原文 | GQ3 |
| 23 | `SKILL.md:50` | 无 | 从 `genre-fiction-craft` 转入本 skill 的：选题、读者契约、事实核验、读者反馈、不确定用哪个 skill；题材契约按 FC-20 的核对口径处理。 | 同上；逐字取 IF-05 对端 `genre/SKILL.md:24` 原文，末句接改后 FC-20 | GQ3 |
| 24 | `SKILL.md:51` | 无 | 从 `cross-media-drama-adaptation` 转入本 skill 的：原作的读者契约和事实核验；人物层按 §1 转介表转 `character-and-narrative-control`。 | 同上；逐字取 IF-06 对端 `cross-media/SKILL.md:34` 原文；「人物」归 character 取 `SKILL.md:30` | GQ3 |
| 25 | `templates/novel-plan.md:7-8`＋14 数据行 | 7 列（字段 ID／字段／填写内容／状态／稿件证据位置／依据规则／写不出的出口） | 8 列，末列「**转出去向**」；表头、GFM 分隔行、14 个数据行各补 1 个空单元格 | `review.json` GQ3 basis／F-10「四张交付模板无『转出去向／接收包』留痕列」；`repair-workplan` §三 GQ3 | GQ3 |
| 26 | `templates/scene-plan.md:6-7`＋12 数据行 | 7 列 | 8 列，末列「转出去向」；表头／分隔行／12 行同补 | 同上 | GQ3 |
| 27 | `templates/diagnosis-report.md:6-7`＋13 数据行 | 6 列 | 7 列，末列「转出去向」；表头／分隔行／13 行（含 DR-SUM）同补 | 同上 | GQ3 |
| 28 | `templates/revision-sheet.md:6-7`＋12 数据行 | 6 列 | 7 列，末列「转出去向」；表头／分隔行／12 行同补 | 同上 | GQ3 |
| 29 | `SKILL.md:313`（§8 自查新增一问） | 七问（原 :300-:306）无「该转的是否转了」 | 于七问后补第八问：「该转的是否转了？转出去向写进交付表了吗？」 | `review.json` GQ3 basis／F-10「『§8 交付前自查七问』无『该转的是否转了』一项」；问句逐字取该发现；原七问行序未动 | GQ3 |
| 30 | `references/rules-revision-and-method.md:178`（FC-21 交付行） | `规则卡`（**layer/scope/signals/branches/failures/counterexamples/confidence**） | `规则卡`（**层/范围/可观察的信号/分支/失败条件/反例/可信度**） | `repair-workplan` §三 W4-14；`w4-closure` CL-verify 6.1／6.3（LI-FP-134 RV-05 先例：v0 `event/scene` 英文字段名 v3 已中文化）；中文名逐字取同卡「怎么做」`:172-:176`（层／范围／可观察的信号／失败条件／反例）、`:166`（分支）、`SKILL.md:165` 与 `examples/rule-examples.md:153`「可信度」 | W4-14 |
| 31 | `references/scope-and-conflicts.md:42`（K-06，原 :41） | 开放须 **latent**、线头有收束 | 开放须有**潜伏意象**、线头有收束 | `w4-closure` CL-verify 6.1 坐标／6.3「10 处逐处判定」；词形取包内既有 `潜伏意象`（同文件 `:88` 既有「中文同位语」判定、`rules-units-and-endings.md:141/:144`、planning.md 多处、examples 多处） | W4-15 |
| 32 | `references/rules-revision-and-method.md:32` | 检查因果链与结尾 **latent** | 检查因果链与结尾的**潜伏意象** | 同上 | W4-15 |
| 33 | `references/rules-revision-and-method.md:42` | 「每场功能 + 结尾 **latent**」两项 | 「每场功能 + 结尾**潜伏意象**」两项 | 同上 | W4-15 |
| 34 | `references/rules-units-and-endings.md:122` | 结尾须 **latent 于开头** | 结尾须**潜伏在开头里**（逐字取 `SKILL.md:189`） | 同上 | W4-15 |
| 35 | `references/rules-units-and-endings.md:133` | 开头已埋 **latent image** | 开头已埋**潜伏意象** | 同上 | W4-15 |
| 36 | `references/rules-units-and-endings.md:146` | C 分支必须检查 **latent image** 与线头 | C 分支必须检查**潜伏意象**与线头 | 同上 | W4-15 |
| 37 | `references/rules-units-and-endings.md:151` | ……与 **latent image** | ……与**潜伏意象** | 同上 | W4-15 |
| 38 | `references/diagnosis.md:236` | 开放结尾没有 **latent image**/线头收束 | 开放结尾没有**潜伏意象**/线头收束 | 同上 | W4-15 |
| 39 | `references/diagnosis.md:245` | 检查 **latent image**/线头 | 检查**潜伏意象**/线头（与 `rules-units-and-endings.md:141` 同一句的中文版对齐） | 同上 | W4-15 |
| 40 | `references/diagnosis.md:258` | 并检查 **latent image** | 并检查**潜伏意象** | 同上 | W4-15 |
| 41 | `references/scope-and-conflicts.md:44`（原 :43，K-08 `probability`）、`:89`（原 :88 `scène à faire`） | — | **未改**：6.1 已判「K-08 行内带中文语境」「行内自带『舞台专属；小说无对应强制力』降级说明」，判定保留英文 | `w4-closure` CL-verify 6.1 对这两处的既有判定；不扩范围 | W4-15（判定保留） |

> 说明：W4-14/15 的中文词形均取自盘上既有表述（「潜伏意象／潜伏」「可信度／层／范围／可观察的信号／失败条件／反例」），非另裁新词形；若作者后续另裁词形，按本批 10 处坐标统一替换，见第五节。

## 二、无动作项（记「无动作」，未改任何文件）

| 裁决号 | 结论 | 说明 |
|---|---|---|
| #3A | 无动作 | 占位行即合法可填面，spec 已预写 |
| #5A | 无动作 | 两列只需 §6 参考文件表；十四题材表属 genre §4，非本包 |
| #9 | 无动作 | 登记类保留：该书／某书 8 行、RO-K117–119 不补回、导演 vs 作者不改；工作单无 #9 落地项 |
| #12 | 无动作 | 保留原句（CY-07 防口已覆盖） |
| #13 | 无动作 | 豁免并按 W4-123 先例登记 |
| F-01／F-05／F-06／W4-116 前缀补缀、`brief.json`／`review.json`／`k5-bindings-*.tsv` | 本席不碰 | 任务第 6 点明列属主代理后续统一处理；逐项核对未写入 |

## 三、附录 B 自检结论（详见 `notes/quality/fiction-planning-and-diagnosis/r5-appendixB-selfcheck-2026-11-06.md`）

- 工具：`LC_ALL=en_US.UTF-8 /usr/bin/grep -rnE`（本机 ugrep，中文长模式规避）；改前／改后用同一命令同一模式集，覆盖 B.1 全 11 类 + §4.2bis 补档（#8 `旧例|原例`、#2 标准号、#3 CN1 中文数词、#6 起点字符集 `["“]`、#5b 排除表）。
- 改前→改后逐类计数：#1 0→0；#2a/b/c 0→0；#3a/b/c 0→0；#3CN1 1→1；#4 3→3；#5a 13→13；#5b 0→0；#6 0→0；#7 0→0；#8 7→7；#9 0→0；#10 **43→44**；#11 0→0。
- 唯一计数变化：#10 +1 为本席改写行 `SKILL.md:330`「本 Skill 不提供专业**意见。**」中「见。」词尾子串；按 §4.2bis 的「标点后悬空＋同行共现」A∧B 语义判据，「见」是「意见」的末字、主语完整，属裸 A 判据假阳性（同类见 R1/R2 自检「依据／证据／可见／不见」），**真违规 0**。其余各类命中改前改后同址同数，逐条判为 B.2 允许（用户作品语义、事实核验语境）、被拒绝立场／领域语义（「大师」13 行）、稿件版本／核验语境（#8 7 行）或词内假阳性（「超出自己」含「出自」）。
- 新增内容禁词专项（本席改写／新增行）：审计词、分档词、「硬规则」、「用户明确要求」、「融合版」、改动痕迹、来源信息（书名／作者／作品人物情节／原句／来源编号／年代／篇数）**0 命中**。
- B.3 四项人工判断：改动文件全文回读、四张表列数逐行核对（表头／分隔行／数据行全齐，无表格空列、无悬空半句）、四个 examples 均带自创声明、借来源背书 grep 命中 6 行全为「不写／不得写／不能写」守卫句；本批新增内容均为条文、字段名、包名、模板列，无例子骨架相近、无标志性情节元素、无借来源背书、无删除来源后语义不通。
- 诚实线：按 `suite-contract §4.2bis`／`p4-closure`，19 条子模式中 13 条检测有效性未证（1a、2b、3a、4a、5a、5b、6a、8a、10a–10e），本结论**只表述为「所用正则未发现新增违规」**，不写成「全类零违规」。既有残留 `scope-and-conflicts.md:118`「Genette/Booth」（`review.json` F-14 登记的附录 B #5 名人姓名）非本席新增、本批未动、不在授权内，如实留档。GQ5 维持 NOT_PROVEN（未跑测试／构建／真实任务，未授权）。

## 四、改动后文件数与字节

| | 文件数 | 字节 |
|---|---|---|
| 改前 | 27 | 348056（与 `review.json` `tree_bytes` 一致） |
| 改后 | 27 | 349507（+1451） |

改动文件 13 个：`SKILL.md`、`agents/openai.yaml`、`references/diagnosis.md`、`references/rules-drafting.md`、`references/rules-premise-and-structure.md`、`references/rules-revision-and-method.md`、`references/rules-units-and-endings.md`、`references/scope-and-conflicts.md`、`references/self-check-diagnosis.md`、`templates/novel-plan.md`、`templates/scene-plan.md`、`templates/diagnosis-report.md`、`templates/revision-sheet.md`。其余 14 个文件未动。

## 五、断点与未闭合项（交主代理，不臆造）

1. **brief 锚位移**：`SKILL.md` :45 后增 6 行、§8 后增 1 行 ⇒ 原 :46 起 +6、原 :307 起 +7。工作单 §三 brief 层 F-05 的 `fp:147` 裸对端行号现为 `:153`（+6）；该补缀、`brief.json`／`review.json`／`k5-bindings-*.tsv` 重绑、整树 SHA 重测与 spec/INDEX/JSON 重算归主代理，本席未碰。
2. **`SKILL.md:330` 外部事实核验接收方未能定位**：`review.json` SEM-07／F-08 明记「套件内无接收方指名」。本席只把有实体的两处（题材→genre、媒介改编→cross-media）具名，并收为「说明边界，本 Skill 不提供专业意见」（取 `SKILL.md:312`），**未臆造对端 Owner**；若需具名接收方请主代理另裁。
3. **W4-15 词形归作者一句**：6.3 记「若判中文化，词形归作者」。本批 10 处判中文化，但词形逐字取自盘上既有（「潜伏意象」「潜伏」在包内 13+ 处、`可信度` 在 `rule-examples.md:153`），属归一到既有中文表述、非另裁新词形；若作者后续另定词形，按本批 10 处坐标统一替换。`:44`（probability）与 `:89`（scène à faire）按 6.1 既有判定保留英文、未动。
4. **§8「第七问」读法**：`review.json` GQ3/F-10 记「自查七问（:300-:306）无『该转的是否转了』一项」，本席按该发现补为**第八问**（原七问行序未动），未删改原第七问；派单简称「第七问」按「七问缺一项」理解闭合，如主代理另有位序要求请回执。
5. **跨包对端承接不在本席范围**：`FQ-IF-03`（非虚构事实核验）、`FQ-IF-05`（题材承诺验收双 Owner）、`FQ-IF-06`（原作人物）的 genre／story／cross-media 侧承接行由别的席／主代理处理；本席仅补本包侧接收行与边界说明，未写任何其他 output 包。
6. 其余既有暴露（`review.json` FQ-R10 列形 fail、F-14 Genette/Booth、F-11/F-12/F-15/F-16、GQ2 另列项、S-03/04/05 等）不在本批授权内，未动，不替作者裁新口径。GQ5 全包维持 NOT_PROVEN；本批只做静态文本落笔，不证明宿主加载或效果。
