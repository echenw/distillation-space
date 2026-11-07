# delivery-preflight-spec 索引（主代理机械实测，2026-11-05 15:54）

覆盖 22.4 第 4 项：逐 skill 的枚举模板全集与 §2a 可填性判定。R18 §6 的 `kd_delivery_preflight.py` **未运行**（static 权限；且 R18 §6 与 R09 收口条文明确「可选」「不另设机器门禁」），全部条目的脚本预检档一律记 **未能核实／NOT_PROVEN**。JSON 载体＝`delivery-preflight-spec.json`（version 1，8 条 templates 记录）；逐件编号全集见各 `<skill>.md`。

| skill | 模板件数 | ID 独占表行数 | 宽式唯一 ID | 其中标题级 | JSON 条目 | JSON field_ids 合计 | spec 文件 | 判定 |
|---|---|---|---|---|---|---|---|---|
| character-and-narrative-control | 1 | 3 | 25 | 0 | 1 | 3 | `character-and-narrative-control.md` | ID 独占行 3 条／1 件｜列名不统一待裁 |
| cross-media-drama-adaptation | 2 | 0 | 4 | 3 | 0 | 0 | `cross-media-drama-adaptation.md` | 有模板件、无 ID 独占行｜§2a 不满足 |
| fiction-planning-and-diagnosis | 4 | 50 | 83 | 1 | 4 | 50 | `fiction-planning-and-diagnosis.md` | ID 独占行 50 条／4 件｜列名不统一待裁 |
| genre-fiction-craft | 14 | 189 | 494 | 88 | 0 | 0 | `genre-fiction-craft.md` | ID 独占行 189 条／6 件｜列名不统一待裁 |
| line-editing-and-proofreading | 0 | 0 | 0 | 0 | 0 | 0 | `line-editing-and-proofreading.md` | 无 templates/；枚举面＝台账/体例表/交付表（56＝SR-01–16＋EN-01–40 连续无缺号）｜结构性 spec 建于 2026-11-06（PS-spec） |
| preset-card-generation | 0 | 0 | 0 | 0 | 0 | 0 | `preset-card-generation.md` | 无 templates/；枚举面＝点分缺陷标识 49＋三卡字段集/卡族表/字数带｜结构性 spec 建于 2026-11-06（PS-spec） |
| scene-conflict-and-rhythm | 2 | 0 | 23 | 15 | 0 | 0 | `scene-conflict-and-rhythm.md` | 有模板件、无 ID 独占行｜§2a 不满足 |
| story-architecture-and-longform-planning | 4 | 54 | 87 | 36 | 3 | 46 | `story-architecture-and-longform-planning.md` | ID 独占行 54 条／3 件｜列名不统一待裁 |

求和回显：模板件 **27**｜ID 独占表行 **296**｜宽式唯一 ID **716**｜JSON field_ids 合计 **99**｜全集与 JSON 差额 **617**（差额集中在 genre：JSON 未收录 14 件题材模板，以及各 skill 模板正文里的非行级 ID）。

未覆盖与不执行声明：

1. **genre-fiction-craft** 的 14 件题材模板此前在 §二十二 22.3 记「未计入」，本轮已递归补测（见 `field-id-matrix.md` 的 genre 复测节与更正注）；是否把 189 条 ID 独占行统一成 §2a 三列形属交付格式裁决，**入 W4-52**。
2. 无 `templates/` 的 skill **不建空 spec**（R18 §6 的可选性；同口径已用于 preset-card 的 G-3 判定），理由在本索引列明。
3. 本索引与逐 skill 文件**不修正品**；`delivery-preflight-spec.json` 保持原样未改写，其与实测全集的差额按「初稿口径」登记，是否重冻 JSON 归 G00／W4 裁决（承 §二十六 的「字段 ID 全集须先按 `inputs/requirements.md` 冻结再进 JSON」补条）。
4. 冻结状态：本目录 **取数与判定已就绪、未冻结**；22.4 第 4 项达成需先销掉 W4-45／W4-47／W4-52 与 K4 非作者对「prose／标题级 ID 是否构成分枚举模板」的判定。


## 列形裁定（2026-11-05 16:57，主代理，依 G00 席判定）

- **裁定**：R18 §2a 所要求的「编号独占一行＋值／状态／稿件证据位置」**不要求各包使用字面相同的列名**。G00 席实测 13 件模板表头与 §2a 语义等价（列名异形：「值／状态／稿件证据位置」vs「填写」「依据／结论」「T｜M｜O｜K」等），故 **不统一字面列名**，改在本节保留理由与对照口径。
- **对冻结的影响**：preflight 的 `field_ids` 判据以「**表行首列为编号**」为准（宽式取词，须含三段式如 `HI-C01`／`AT-D01`／`RO-K121`），不按列名字面匹配；标题式行与占位行另档回显。
- **仍开放**：占位行是否算「可填字段」（W4-11／W4-79）、四行「同上」是否算实质填充（W4-70）——这两条决定 spec 是否要求逐项成行，**交作者定**，本席不代裁。

## 结构性 spec 补建（2026-11-06，PS-spec 席，主代理登记）

- 上面两行原判「无枚举模板件｜不建 spec（R18 §6）」按 2026-11-05 口径成立（指不建**空模板 spec**）；PS-spec 席已为两包建成**结构性 spec**（枚举面＝台账/体例表/交付表列集与三卡字段集/卡族表/字数带，非模板文件），判定更新如上两行。第 21 行「不建空 spec」理由不变、与本更新不冲突。
- JSON（8 条 templates 记录）**维持原样**：两包无模板文件、无 field_ids 条目可加；**field_ids 冻结明确标注「待整树 SHA 冻结后」（W4-09），本批不提前冻结**。
- 两 spec 的树绑定（修复批后现树，依 `scratchpad/repair-tree-after-2026-11-06.tsv` 与现树实测）：line-editing **10 件／114,289 B／1,303 行**、preset-card **11 件／115,304 B／1,347 行**；两包树哈希字段＝「**待主代理 K5 冻结**」（本席不自造 SHA，冻结由主代理统一做）。依赖未答决定件的字段（#2/#6/#7/#8/#10）在各 spec 内标注「未裁」，不预设。
- 「同上」四行（W4-70）与占位行判定（W4-11/79）仍**交作者定**，本席不代裁（承 16:57 列形裁定的开放项口径）。

## 修复批树重算（2026-11-06，收口席 A 内容层）

- 依据：`scratchpad/repair-tree-after-2026-11-06.tsv`（8 包修复后件数／字节）＋现树实测（`find`＋逐件 `wc -l -c`）。**哈希字段一律写「待主代理 K5 冻结」占位，本席不自造 SHA**；冻结由主代理统一做（tsv 单笔更新）。
- 8 包修复后绑定值：

| skill | 件数 | 字节 | 树哈希 |
|---|---|---|---|
| character-and-narrative-control | 17 | 194,854 | 待主代理 K5 冻结 |
| cross-media-drama-adaptation | 13 | 75,549 | 待主代理 K5 冻结 |
| fiction-planning-and-diagnosis | 27 | 349,507 | 待主代理 K5 冻结 |
| genre-fiction-craft | 101 | 1,058,396 | 待主代理 K5 冻结 |
| line-editing-and-proofreading | 10 | 114,289（1,303 行） | 待主代理 K5 冻结 |
| preset-card-generation | 11 | 115,304（1,347 行） | 待主代理 K5 冻结 |
| scene-conflict-and-rhythm | 17 | 169,017 | 待主代理 K5 冻结 |
| story-architecture-and-longform-planning | 21 | 284,595 | 待主代理 K5 冻结 |

- **重算复核（未改）**：第 16 行求和回显（模板件 27／ID 独占表行 296／宽式唯一 ID 716／JSON field_ids 合计 99／差额 617）与 8 份逐 skill spec 首表（模板件／ID 独占表行／宽式唯一 ID／标题级 ID）依修复后现树逐件复测**全部一致**，故数值不改；模板件集合本身未因修复批增删。
- **同批更正的依赖旧树结论**：`line-editing-and-proofreading.md` 与 `preset-card-generation.md` 两结构性 spec 的 `files／bytes`、逐件行数、`tree_sha256`／`brief_sha256` 绑定值、回执「绑定值」句、W4-09 措辞与「绑定值为已完成」状态句；本索引「结构性 spec 补建」节的两条树绑定句与 W4-09 句。逐处见 `notes/repair-ledger-brief-spec-2026-11-06.md`。
- **field_ids 冻结（W4-09）**：明确标注「**待整树 SHA 冻结后**」，本批**不提前冻结**；`delivery-preflight-spec.json` 的 8 条 templates／99 个 field_ids 原样未动，仅加一条冻结状态注记。
- **W4-47 边界句**：已由 R1 写入 `character-and-narrative-control.md:27`，本席**未重复写**。
- **未闭合（登记）**：两结构性 spec 正文内大量 `SKILL.md:NNN`／`workflow.md:NNN` 等行号锚依修复前树；修复批造成 R7／R6 行内改文与位移，逐锚重测属主代理 K5 冻结前「锚抽验」范围，本席未逐条重测，不在此批闭合。`field-id-matrix.md` 旧「genre 段中途快照、冻结前须重跑」的时点条件随修复批树稳定而解除，但 genre 段编号普查仍须在 K5 冻结前重跑一次并归因。
- 本席未运行 `kd_delivery_preflight.py`、未跑测试／构建／真实任务、未写 `output/`、未做 git 写操作；GQ5 维持 NOT_PROVEN。

## K5 冻结回填（2026-11-06，主代理）

上表与两份结构性 spec 里的「待主代理 K5 冻结」占位，**以下列实测值为准**；占位文字保留为修复批时点的历史记录，不逐字替换（该字符串同时出现在「本批不提前冻结」等状态说明句中，逐字替换会破坏上下文）。

- `output/` 整树两级 SHA-256（217 件／2,363,926 B）：**`1fd053fe1fc83d51b4ce8edc82d759ccd53307f8304fccf3a2ff3bcc2e05eafd`**
- 算法：`skills/knowledge-compiler/scripts/kd_round_output.py:123-127`（路径字节序升序 → 逐行 `<relpath>\t<sha256>\n` → 拼接串再取 SHA-256）。
- 权威绑定表：`notes/k5-bindings-2026-11-07.tsv`（2026-11-07 r3 重冻结，8 包完整 tree_sha256／brief_sha256／件数／字节；11-06 版 `notes/k5-bindings-2026-11-06.tsv` 按 A.3 原样保留为历史证据）。

| 包 | tree_sha256（完整 64 位） | brief_sha256（完整 64 位） |
|---|---|---|
| character-and-narrative-control | `82ab523bd24fe0b0a1ec15622236981373e202fcd554e4646f875e193da2b3a5` | `d78a91d561955b16e24fb4dfd273082b1cec6e4b3684d3e78ec4b91c03e1ddeb` |
| cross-media-drama-adaptation | `748b1f50d3f64872f71d9355c61ae4c791e73b9fb9f15f31b6c08d291c40e8fe` | `c8dc3f07463dcd99b656eac77153920dc059dc6b661d3c7ce786143d2c83d620` |
| fiction-planning-and-diagnosis | `dd9c4874214edaae51f9df4b8ca9d86c86870eee91e23746332038d67bbabf1b` | `9773ab9e629c6ffae88b48ac888e63eb142ff3ef5aa05aa3b56c82d11d07876b` |
| genre-fiction-craft | `ae52a58958df8efad9e5e0113e9f21167552d7e9e3f0b10d1f6d849579b2395c` | `21fe7d0d0bcb459b6831a9a3558d2aa9f20ac159e4abe9bcf1479159d718e21c` |
| line-editing-and-proofreading | `46ed93381b432515f9efba03c81d3acfe18d8001b6cc62324fec496ac28d1af0` | `ca9fa27aa59d5c236a0a2d2cdb856046cdc55b579806418250318b4675d6ec42` |
| preset-card-generation | `9f6fad5cc72922e00c89152ed72ff6c5b07098bdae0698b0476eac71dfa777d6` | `efc6373ac75106b4c63c1f7a00fcf6615c2f603f519bbdace7d4d6bce24b4d6c` |
| scene-conflict-and-rhythm | `931710a8cd1400b240d0af67cf053480c26bb072564183d45c1aa2ff6408eea4` | `cf2963ca342e81008787fcd7cc3bfd04ed54eeb32f11e682a3576b8651c903b1` |
| story-architecture-and-longform-planning | `38a4252dde8400c9cc6228bdc10917744ea970c941e7867f6900f325b6dd0cd5` | `b28d282f02f6ec7ae3da452360d249bc48e00861f9456d3458759b907f666b63` |

- **仅 genre brief 本批被改**（F-01／F-05／F-06／W4-116），brief SHA 由 `7872b791…` → `7d5e5c84…`；其余 7 份 brief 实测与基线逐包相等。（上节绑定值与 brief_sha256 列已于 2026-11-07 由 brief-repair 席按 r3 重冻结刷新：整树 `1fd053fe…`／217 件／2,363,926 B；brief 列为该席改后 8 份 brief 实测值，与 `notes/k5-bindings-2026-11-07.tsv` 一致。）
- **`field_ids` 冻结（W4-09）仍未做**：须由非作者按 `inputs/requirements.md` 判定哪些编号族真要求逐项可填，属判定动作，主代理不代裁、不提前冻结。GQ5 维持 NOT_PROVEN。
