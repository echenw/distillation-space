# 修复批总账（2026-11-06，主代理 Owner）

- 触发：作者答复「全部按推荐」（13 条决定件，`notes/user-decisions-2026-11-05.md`）。本文件是唯一权威总账；各席只写自己的分片 `notes/repair-ledger-<pkg>.md`，不并发写本文件。
- 依据：`notes/repair-workplan-2026-11-06.md`（参数化工作单）、`notes/user-decisions-2026-11-05.md`。
- 改前快照：`scratchpad/repair-baseline-2026-11-06.tsv`（8 包 brief/树 SHA、件数、字节，取自 `notes/k5-bindings-2026-11-05.tsv` 现行值）。
- 改前并发检查：`find output -type f -newermt '2026-11-06 00:00'` 为空 ⇒ 无并发写入者；`git status` 仅 `M docs/plans/novel-skill-improvement-plan.md` 与 `?? distillation/`。
- 原则：一次过（8 包 output 与 brief 改动单批完成，避免 review 绑定反复过期）；修复席不携「作者裁决」名义自创新口径；逐处改动落 ledger；GQ5 维持 NOT_PROVEN。

## 一、作者裁决值（照录，不代改）

| # | 裁决 | 落地分支 |
|---|---|---|
| 1 | A | character `boundaries-and-ethics.md` §1 外加「即时危险→一句现实求助指引」小节 |
| 2 | A | SKILL 层唯一状态词表：scene 删重复表、story 上浮、cross-media 以 SKILL 为准并给「本轮未执行」归档位 |
| 3 | A | 无动作（占位行即合法可填面，spec 已预写） |
| 4 | B | story `SKILL.md` §10 四行「同上」逐行补独立句 |
| 5 | A | 无动作（两列只需 §6 参考文件表） |
| 6 | A | preset-card 字数带＝「含标点的非空白字符数，小节标题行不计」＋示例卡复测 |
| 7 | A | preset-card 三状态＋依据作附件、已知降级记录槽、正文双义改名、§3 声明不提供空白模板 |
| 8 | A | line-editing 加「本包用「」标记术语与条目名，稿件引号仍按 SR-13」；GB/T 15834/15835 编号保留；worked-example 稿件片段引号统一 |
| 9 | 默认（文件标注「不必现在答复」） | 不动：该书／某书 8 行保留、RO-K117–119 不补回、导演 vs 作者不改；工作单无 #9 落地项 |
| 10 | A | 题材契约归 genre；fp 三处改「按 genre 的题材契约核对，缺项回本包登记」 |
| 11 | A | genre §6 措辞改与实际一致（行内改文、不动锚点） |
| 12 | 默认 | 保留原句（CY-07 防口已覆盖） |
| 13 | 默认 | 豁免并按 W4-123 先例登记 |

## 二、席位分工（按包 Owner，互不重叠；8 席全齐）

| 席 | 包 | 分片 ledger | 状态 |
|---|---|---|---|
| R1 | character-and-narrative-control | `repair-ledger-character-and-narrative-control.md` | 已落盘 |
| R2 | scene-conflict-and-rhythm | `repair-ledger-scene-conflict-and-rhythm.md` | 已落盘 |
| R3 | story-architecture-and-longform-planning | `repair-ledger-story-architecture-and-longform-planning.md` | 已落盘（中断后重派） |
| R4 | cross-media-drama-adaptation | `repair-ledger-cross-media-drama-adaptation.md` | 已落盘；范围核定见 §六 |
| R5 | fiction-planning-and-diagnosis | `repair-ledger-fiction-planning-and-diagnosis.md` | 已落盘 |
| R6 | preset-card-generation | `repair-ledger-preset-card-generation.md` | 已落盘 |
| R7 | line-editing-and-proofreading | `repair-ledger-line-editing-and-proofreading.md` | 已落盘 |
| R8 | genre-fiction-craft | `repair-ledger-genre-fiction-craft.md` | 已落盘；零位移 |

收口席 A（brief/spec 层，`repair-ledger-brief-spec-2026-11-06.md`）、收口席 B（独立只读复核，**不落盘**，结论以消息返回）。复测与冻结由主代理承担。

## 三、收口序列（工作单第四节，逐项销账）

1. [x] 8 包 output 依裁决落地 —— R1–R8 共 8 席，8 份分片 ledger 齐；树哈希 8/8 变更并经两方独立复算全等
2. [x] 全 8 包附录 B 11 类重扫 —— 独立只读复核席 B 复跑，可见范围零新增违规（诚实线不写「全类零违规」）；已并入 `desourcing-ledger.md`
3. [x] brief 层 —— 收口席 A 共 33 处：F-01 六处＋F-05 八处（行号按现树重取）＋W4-116 同族＋F-06；genre brief SHA `7d5e5c84…`
4. [x] spec / INDEX / JSON 依修复后树重算 —— 件数／字节／行数已改，哈希以 `repair-rebinding-2026-11-06.md` §一 冻结值回填（INDEX 追加节）；W4-47 由 R1 写入 character spec:27
5. [x] 8 包重绑复测 —— 整树两级 SHA `d86672d4…`（217 件／2,361,511 B），新 tsv 落盘；**genre peer 旧值刷新未按字面执行**，理由见 §八（主代理裁定）；锚抽验留 W4-r2
6. [x] 冻结序列 —— 新 tsv → INDEX 冻结回填节 → checklist 状态「出口（静态交付）」→ log.md 收官表 → desourcing-ledger 修复批节 → 本总账销账。**`field_ids`（W4-09）未冻结**，须非作者判定，如实挂账
7. [x] GQ5 全包维持 NOT_PROVEN —— 8/8 未改，真实任务测试未授权

## 四、状态

- 2026-11-06 14:01：快照与总账落盘，派发第一批席位。
- 2026-11-06 14:18：R2（scene）、R1（character）已落盘，分片 ledger 与附录 B 自检齐；主代理用唯一权威树哈希算法复测确认两包真实变更：scene 17 件 168166→169017 B（b00f59d1→2cdf8c5c）、character 17 件 193531→194854 B（f32f4dca→3355d7ca）；其余 6 包树哈希与基线逐包一致，未被改动。R3（story）未执行、无任何写入。
- 2026-11-06 14:39：会话中断后恢复，按上述硬证据续派，不重派 R1/R2（避免重复写入）。
- 2026-11-06 14:39–15:33：R3–R8 六席全部落盘，8 包 output 全部变更（`output/` 最后写入 15:33:29）；随后收口席 A（brief/spec 内容层）与席 B（独立只读复核）并行返回。席 B 复算 8 包树哈希与主代理 8/8 全等、13 条裁决逐条核过、附录 B 可见范围零新增违规，但建议不放行冻结（绑定全旧、Q6 未定档）。
- 2026-11-06 16:1x：主代理完成 K5 冻结与出口。`output/` 整树两级 SHA `d86672d4…`（217 件／2,361,511 B）；`notes/k5-bindings-2026-11-06.tsv`、`notes/repair-rebinding-2026-11-06.md` 落盘；`checklist.md` 状态改「出口（静态交付）」并追加 §八十四；`log.md` 收官表、`notes/desourcing-ledger.md` 修复批节、`INDEX.md` 冻结回填节齐；§三 收口序列 7 项销账。
- **主代理裁定（§八）**：8 份 `review.json` 不改写。席 B 建议刷新其 SHA／peer 值，本席不采纳——这些是 `review-independent-r1` 非作者独立复核件，绑定修复前树；作者侧改写会把未复核新树写成通过。新树绑定另立台账，原件留作历史证据。工作单 §四「genre peer 三处旧值刷新」未按字面执行，属有依据的范围收窄，交作者复核。
- 完成度口径：本文件只记「已落地并有证据」的项，未验证项不写通过。出口＝**静态交付出口**，不等于 GQ 全绿或效果已证。

## 八、裁定与未闭合（销账后残余，交作者／后续授权）

| 项 | 状态 | 归属 |
|---|---|---|
| 8 份 `review.json` 绑定修复前树 | **不改**（本席裁定，理由见 `repair-rebinding-2026-11-06.md` §三） | 作者复核该裁定；若采纳席 B 方案需 W4-r2 整份重做 |
| 修复后树的独立隔离回读／GQ1–GQ4 档位复议 | 未执行 | 需新授权，非作者只读子代理（W4-r2） |
| Q6 档位（现 FAIL，主据已消解） | 未改 | 待独立复测重定，不降门槛造绿 |
| `field_ids` 冻结（W4-09） | 未冻结 | 须非作者按 `inputs/requirements.md` 判定 |
| 多数 GQ2／GQ3 FAIL（character S1–S3／IF-01/03/05、scene ②、story SV-16、cross-media ①④⑥、preset F-02、genre GE-R16／IF-03、fp IF-03/05/06 等） | 未闭合 | 逐项见各分片 ledger 与 `checklist.md §八十四` |
| brief `peer_side_anchors` 4 处旧行号、两结构性 spec 正文行号锚、field-id-matrix genre 编号普查 | 未逐条重测 | W4-r2 锚抽验 |
| R2 的 `chapter-ends-and-endings.md:9` 第三处值域、R4 的「未知」三选一、R6 的 IF-03 分单规则、R7 包内「」引话语 | 未闭合 | 已登记，不扩大范围 |
| **GQ5 全包** | **NOT_PROVEN** | 真实任务测试未授权，恒不写成通过 |

## 五、R1/R2 交主代理的未闭合项（照录，不擅自扩大范围）

| 来源 | 项 | 处置 |
|---|---|---|
| R1 | IF-01 切片表互认／字段映射 | review.json S4 记为「跨包契约，交用户或 G00 裁」；13 条决定件未含此项，对端是 scene。不臆造映射条，留 W4 如实登记 |
| R1 | IF-03 preset-card 7↔3 互逆对齐 | 除项数外还缺「同一请求既要卡又要视角裁决」的分单规则，属裁口径；对端 R6 席本批处理对象，主代理在 R6 回执后核定 |
| R1 | IF-05 对端承接行与具体存放表 | 本席已在 character `SKILL.md:153` 补「登记归 genre」；对端 genre 承接由 R8 核定 |
| R2 | brief 层 F-05 `scene:289` 裸对端行号 +1 | R2 在 `SKILL.md §10`（:275）增 1 行致 :289 起整体 +1；归主代理 brief 层统一处理 |
| R2 | `chapter-ends-and-endings.md:9` 第三处「场景或章节单元（场、章、幕）」值域 | 工作单只点名 SKILL:177 与 intensity :11/:28；不扩范围，留如实登记 |
| R2 | GQ2 另列 ③⑤、GQ3 七接口、S-03/04/05、SC-G02、F-01 字段承诺措辞 | 不在本批「GQ2 四项」授权内，未动；不替作者裁新口径 |

GQ5 全包维持 NOT_PROVEN；本批只做静态文本落笔，不证明宿主加载或效果。

## 六、R4 范围核定（主代理，2026-11-06）

R4 回执提出「派单只写『其余两处』，本席共收敛 4 文件 5 处，请核定是否回退改动 1/2/3」。核定结论：**不回退，5 处均在裁决 #2A 授权内**，依据如下：

| 改动 | 核定 | 依据 |
|---|---|---|
| 1 `SKILL.md:168` 判据让位句改指向 §10 | 结构性必要 | 裁决 A「每包统一为 SKILL 层唯一表＋其余处改引用」；若保留原句，§6 表仍把判据权威让给判据侧，与 `:195` 自称唯一并存，且与改动 3 删表后指向空节矛盾 |
| 2 `SKILL.md:204` 唯一权威声明＋「本轮未执行」归档 | 裁决直接要求 | `#2A` 原文「cross-media 以 SKILL 为准（**并决定"本轮未执行"归哪一档**）」；R4 按 `suite-contract §2.2`（NOT_RUN→未能核实）归档，未新增第五状态词、未改四词表 :195-202 |
| 3 `references/interactive-adaptation.md:52-57` 删第二份逐字重复表 | 裁决「其余处改引用」 | `review.json` GQ2②/`K4-r1.md:104` 明记这是第二份定义表且与权威表相斥；R2 席对 `rhythm-diagnosis.md` 已用同一处理（删表改指针），同族先例一致 |
| 4/5 两个模板改引用 | 即派单「其余两处」 | W4-77 三处减权威侧 = 两模板 |

额外处置（如实登记，非新裁）：R4 依 `suite-contract §3` 既有定性把「未知」定为模板占位填值而非状态词、并把 `:204`「那一列」改「两列」消歧——属与裁决直接配套的最小改动，不属新增口径。W4-77 九条里的其余条目（AD-40 检查落稿行、五分歧缺三类、节点编号规则、§12.3 自指、音频载体导航）**不在本批授权内，未动**，不因本席核定而扩大范围。

## 七、F-05 行号须按修复后现树重取（重要，派单口径更正）

工作单 §三写的 F-05 四处裸对端行号 `scene:289／character:307／fp:147／line:188` 是**修复前**基线。修复批本身又造成位移：R1 在 character `SKILL.md §9.1` 增行致 `:277` 起 +2；R5 在 fp `:45` 后增 6 行致原 `:147`→`:153`；R2 在 scene `SKILL.md:275` 增 1 行致 `:289` 起 +1；R7 把 line-editing `:109/:110` 两行并一行致后续 −1。因此 brief 层补缀**不得照抄旧行号**，须按修复后现树用 `/usr/bin/grep -Fn` 实测对端文本所在行再写入，否则会制造新的寻址失配。
