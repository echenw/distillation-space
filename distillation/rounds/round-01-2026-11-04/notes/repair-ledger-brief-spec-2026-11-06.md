# 修复批收口席 A · brief／operations-contract／delivery-preflight-spec 逐处改动台账（2026-11-06）

- 席位：收口席 A（内容层修订）。作者「全部按推荐」，8 个 output 包已由 R1–R8 改完并通过附录 B 自检；本席不写 `output/`、不写 8 份 `review.json`、不写 `k5-bindings-*.tsv`、不写 checklist／log／desourcing-ledger、不做冻结。
- 依据：`repair-ledger-2026-11-06.md` §六（R4 核定）／§七（F-05 行号须按修复后现树重取）、`repair-workplan-2026-11-06.md` §三／§四、`user-decisions-2026-11-05.md`、`review.json` 的 F-01／F-05／F-06 与 `addressing_defects`、`scratchpad/repair-tree-after-2026-11-06.tsv`、修复后现树实测。
- 本机 grep 为 ugrep，中文长模式一律走 `/usr/bin/grep -rnE`／`grep -Fn`；行号只作线索，逐处按内容定位并回读。
- 写入范围（严格）：`quality/genre-fiction-craft/brief.json`、`operations-contract/genre-fiction-craft.md`、`delivery-preflight-spec/` 内文件、本台账、`quality/repair-brief-selfcheck-2026-11-06.md`。无 git 写操作，未跑测试／构建／真实任务（GQ5 维持 NOT_PROVEN）。

## 一、逐处改动（位置／改前／改后／依据／编号）

编号前缀：B＝brief.json，O＝operations-contract，I＝INDEX，L＝line-editing spec，P＝preset-card spec，M＝field-id-matrix，J＝spec.json。行号为**改后**文件行号。

| 编号 | 位置 | 改前 | 改后 | 依据 |
|---|---|---|---|---|
| B01 | brief.json:750 `requirements[18] GE-R18.text` | 仅「…转出 preset-card-generation」 | 追加现树事实括注：转介句已在 `SKILL.md:3` description 末句与 `:30` 路由表末行在位，`/usr/bin/grep -Fn` 命中 `:3/:30` 两行；`status=missing` 明记为修复前 113 行树档位、本批不改档 | review F-01①；R8 改 `SKILL.md:3/:101`；现树实测 | F-01／GE-R18 |
| B02 | brief.json:1177 `GE-CAP-15.name` | 「跨包转介与接收（六类兄弟包）」 | 「…（七类兄弟包）」 | `SKILL.md:3/:30` 现列 7 家 | F-06 |
| B03 | brief.json:1184 `GE-CAP-15.what` | description 与路由表「把…六类转给兄弟包」 | 「…七类转给兄弟包」＋补「description 末句（`:3`）与路由表末行（`:30`）已列 preset-card-generation，实测命中 :3/:30 两行」 | review F-06；`/usr/bin/grep -Fn 'preset-card-generation' output/genre-fiction-craft/SKILL.md` 命中 2 行 | F-06 |
| B04 | brief.json:1198 `GE-CAP-15.limit` | 「preset-card 一类未写（GE-G05）」 | 「preset-card 一类现已在 `:3`／`:30` 写出（R8 修复批，实测命中），而非旧树所记『未写』」；前半句「无字段级交接契约」保留 | review F-01 detail §③ 括注 | F-01 括注 |
| B05 | brief.json:1322 `GE-IF-05.peer_role` | 「未声明接收本包转出：全包 0 次提到 genre-fiction-craft」 | 「现树已在 cross-media-drama-adaptation/SKILL.md §12.4（:238/:240/:241）三行声明双向转介并接收；实测命中 3 行，修复前 113 行树为 0」 | `/usr/bin/grep -rnF 'genre-fiction-craft' output/cross-media-drama-adaptation/` 命中 3 行 | F-01／GE-IF-05 |
| B06 | brief.json:1323 `GE-IF-05.handoff_condition` | 「对侧 description 与路由表只列六家，未列 genre」 | 保留「description 仍列六家不含 genre（对侧 F-11 面）」，补「§12.4 三行已补双向转介、实测命中 3 行」 | 同上＋R4 §六核定不改 description | F-01／GE-IF-05 |
| B07 | brief.json:1331 `GE-IF-05.note` | 「实测…命中 0（退出码 1）」 | 「修复前…命中 0；修复批后现树复测命中 3 行，均在 `:238/:240/:241`，零命中结论不再成立」 | 同上 | F-01／GE-IF-05 |
| B08 | brief.json:1357 `GE-IF-07.this_role` | 「未声明：本包全包 0 次提到 preset-card-generation／预设卡／preset／预设」 | 「现树已声明：`:3`／`:30` 写出转介句；实测 -Fn 命中 2 行、-Finc 'preset' 命中 2 行、-Fn '预设卡'/'预设' 仍 0、全包 -rlF 命中 1 文件；修复前 113 行树四条探测均 0」 | `/usr/bin/grep -Fn/-Finc/-rlF` 现树实测 | F-01／GE-IF-07 |
| B09 | brief.json:1359 `GE-IF-07.handoff_condition` | 「本包侧路由表 SKILL.md:22-29 只有六行，无 preset 一行」 | 「现树路由表 `:24`–`:30` 共 7 行，末行 `:30` 已补 preset，description `:3` 亦含；旧树结论不再成立」 | `sed -n '22,30p'` 现树实测（表头 `:22`／分隔 `:23`／7 数据行 `:24-:30`） | F-01／GE-IF-07 |
| B10 | brief.json:1371 `GE-IF-07.note` | 113 行树四条命令退出码 1、全包 101 文件退出码 1 | 修复前取证标时＋修复批后现树复测（命中 :3/:30 两行、2/2/0/0/1） | 现树实测 | F-01／GE-IF-07 |
| B11 | brief.json:1678 `cases[5] GE-T6.expected` 括注 | 「（本包目前无该行，见 GE-G05）」 | 「（该转介句现已在 `:3`／`:30` 在位，R8 实测命中；见 GE-G05 现树更正）」 | review F-01 detail §③ 括注 | F-01 括注／GE-T6 |
| B12 | brief.json:1873 `gaps[4] GE-G05.finding` | 「genre 侧对 preset-card-generation 零转出」（113 行树四条 0 命中、路由表 6 行） | 现树事实：`:3`／`:30` 在位（R8 #11A／F-06、117 行无位移）＋实测依据；旧 0 命中降格为「修复前取证、对现树不成立」；`level`／`kind` 档位维持 | review F-01①；R8 selfcheck；现树实测 | F-01／GE-G05 |
| B13 | brief.json:1887 `gaps[5] GE-G06.finding` | 「cross-media 侧无本包回执：命中 0」 | 现树事实：§12.4（`:238/:240/:241`）三行在位、实测命中 3；旧零非空扫为修复前取证；「对方 description 仍不列 genre」保留并标 F-11 面 | `/usr/bin/grep -rnF` 现树实测 | F-01／GE-G06 |
| B14 | brief.json:1898 `gaps[6] GE-G07.finding` 括注 | 「yaml 同样不含 preset-card 转出（与 GE-G05 同因）」 | 「本批未改 agents/openai.yaml，此句仍成立；`:3/:30` 已补，见 GE-G05 现树更正，旧『同因』不再成立」 | R8 只改 SKILL.md:3/:101 | F-01 括注 |
| B15 | brief.json:2228 `preset_card_interface_probe.conclusion` | 「单向：…本包 SKILL.md 与全包对 preset-card 零转出。记为 GE-R18 status=missing、GE-G05 与 GE-IF-07」 | 修复前单向结论标时＋现树更正（`:3/:30` 已补、六处口径已改）；上方 probes 的 0 命中数值注明为修复前取证、不作现树结论；档位维持修复前取值 | F-01 同族下游结论，同批更正 | F-01 |
| B16 | brief.json:2038 `notes_on_method.queue_overlap[0]` | 「本席只是复测到当前盘仍然成立」 | 「修复前复测成立；修复批后 `:3/:30` 已补、主据已闭合，台账销项归主代理裁」 | F-01 同族下游结论 | F-01 |
| B17 | brief.json:2041 `notes_on_method.queue_overlap[3]` | 「cross-media 侧无 genre 回执是该项的一部分」 | 修复前事实＋「修复批后 §12.4 三行已补（实测命中 3 行）」 | F-01 同族下游结论 | F-01 |
| B18 | brief.json:1258 `GE-IF-02.handoff_condition` | 裸 `SKILL.md:290` | `scene-conflict-and-rhythm/SKILL.md:290` | `/usr/bin/grep -Fn '武侠打斗写不好'` 现树实测 `:290`（旧 `:289` 因 R2 在 `:275` 增 1 行 +1） | F-05①／W4-116 |
| B19 | brief.json:1280 `GE-IF-03.handoff_condition` | 裸 `SKILL.md:308` | `character-and-narrative-control/SKILL.md:309` | `grep -Fn` 实测 `:309`（R1 §9.1 +2，旧 `:307`） | F-05①／W4-116 |
| B20 | brief.json:1302 `GE-IF-04.handoff_condition` | 裸 `SKILL.md:148` | `fiction-planning-and-diagnosis/SKILL.md:153` | `grep -Fn '不像这个类型'` 实测 `:153`（R5 `:45` 后 +6，旧 `:147`） | F-05①／W4-116 |
| B21 | brief.json:1339 `GE-IF-06.handoff_condition` | 裸 `SKILL.md:189` | `line-editing-and-proofreading/SKILL.md:188` | `grep -Fn '武侠打斗写不好'` 实测 `:188`（旧行文 `:189` 指空行） | F-05①／W4-116 |
| B22 | brief.json:1832 `gaps[1] GE-G02.finding`（3 小处） | `case-notes.md:1`／`guide.md:3`／`guide.md:24` | 各补 `references/10-profession-competition/` 前缀；三行号实测未变（`:1` H1 括注、`:3` 区间声明、`:24` 分流行） | `sed -n '1p;3p;24p'` 逐行实测 | F-05②／W4-117 |
| B23 | brief.json:1914 `gaps[7] GE-G08.finding` | `01-mystery/guide.md:34` | `references/01-mystery/guide.md:34`；行号 `:34` 实测未变 | `sed -n '34p'` 实测 | F-05②／W4-117 |
| O01 | operations-contract/genre-fiction-craft.md:142 §三 Q6 行中段 | 「§6 承诺两栏、实测 0/14 与 10/14、指向落空、实测无承载，故记 FAIL」 | 现树事实：#11A 已把 §6 措辞改为「分流表在 guide 首节、标题不统一；触发条件在规则文件」（R8 行内改文、117 行无位移），不再承诺两栏；栏目实测 10/14、0/14、9/14、独立 H2 3/14（含 13 变体 4/14）为结构实测值；原 FAIL 主据不成立、X-2 按 #11A 落地、F-02 数值未变定性改、GE-R16 出口不齐未变 | `repair-ledger` §六／用户决定件 #11A；R8 selfcheck；现树逐目录 grep；review F-02；GE-R16 实测 | 任务 4／Q6 |
| O02 | operations-contract/genre-fiction-craft.md:205–242 | 无 | 追加「修复批事实更新（2026-11-06）」：逐句对照（5 句）、依据、六问事实重取与建议档（不落档）、未闭合与范围声明 | 任务 4④ | 任务 4 |
| I01 | delivery-preflight-spec/INDEX.md:35 | 「field_ids 冻结仍待整树 SHA（W4-09）」 | 「field_ids 冻结明确标注『待整树 SHA 冻结后』（W4-09），本批不提前冻结」 | 任务 5 | W4-09 |
| I02 | delivery-preflight-spec/INDEX.md:36 | 「line-editing `63d89e5f…`（10 件/114,211 B）、preset-card `be89d163…`（11 件/113,900 B）」 | 「line-editing 10 件／114,289 B／1,303 行、preset-card 11 件／115,304 B／1,347 行；两包树哈希＝『待主代理 K5 冻结』」 | `scratchpad/repair-tree-after-2026-11-06.tsv`＋现树 `find`／`wc -l -c` | 任务 5 |
| I03 | delivery-preflight-spec/INDEX.md:39–62 | 无 | 追加「修复批树重算（2026-11-06）」：8 包件数／字节表（哈希全占位）、求和回显 27／296／716／99／617 与 8 份 spec 首表复测一致未改、W4-47 勿重复、未闭合登记 | 同上 | 任务 5 |
| L01 | line-editing-and-proofreading.md:9 `tree_sha256` | `63d89e5f…`（旧树值） | 「待主代理 K5 冻结」占位＋旧值降为 2026-11-05 基线说明 | 任务 5（不自造 SHA） | 树哈希 |
| L02 | line-editing-and-proofreading.md:10 `files／bytes` | 10 件／114,211 B | 10 件／114,289 B（1,303 行实测） | tsv＋现树实测 | 件数／字节 |
| L03 | line-editing-and-proofreading.md:11 `brief_sha256` | `9d29bd3c…` | 「待主代理 K5 冻结」占位＋注「本批未改该 brief，`shasum -a 256` 实测仍为 `9d29bd3c…`」 | `shasum -a 256` 实测 | 哈希字段 |
| L04 | line-editing-and-proofreading.md:13 | 「树一迁移动，逐行号引用须重测」 | 「修复批后树已迁移，逐行号引用须在 K5 冻结前锚抽验重测」 | 任务 5 依赖旧树结论 | 同批更正 |
| L05 | line-editing-and-proofreading.md:69 W4-09 | 「冻结须待整树 SHA 收口」 | 「冻结明确标注『待整树 SHA 冻结后』，本批不提前冻结」 | 任务 5 | W4-09 |
| L06 | line-editing-and-proofreading.md:75 状态词 | 「编号全集与绑定值为已完成」 | 「编号全集与件数／字节／行数为已完成；树哈希绑定＝待主代理 K5 冻结」 | 任务 5 | 同批更正 |
| L07 | line-editing-and-proofreading.md:81 回执绑定值 | tree `63d89e5f…`（10 件／114,211 B，1,303 行）＝brief_sha `9d29bd3c…` | 10 件／114,289 B／1,303 行；tree/brief SHA 均占位（brief 实测仍 `9d29bd3c…`）；编号全集 56 不变 | tsv＋现树实测 | 树绑定 |
| P01 | preset-card-generation.md:9 `tree_sha256` | `be89d163…` | 「待主代理 K5 冻结」占位＋旧值降为基线说明 | 任务 5 | 树哈希 |
| P02 | preset-card-generation.md:10 `files／bytes` | 11 件／113,900 B（1,345 行） | 11 件／115,304 B（1,347 行，R6 净增 2 行） | tsv＋现树实测 | 件数／字节 |
| P03 | preset-card-generation.md:11 `brief_sha256` | `cfe0c1fd…` | 「待主代理 K5 冻结」占位＋注「实测仍 `cfe0c1fd…`」 | `shasum -a 256` 实测 | 哈希字段 |
| P04 | preset-card-generation.md:13 | 「树迁移后逐行号引用须重测」 | 「修复批后树已迁移，逐行号引用须在 K5 冻结前锚抽验重测」 | 任务 5 | 同批更正 |
| P05 | preset-card-generation.md:92 W4-09 | 「冻结须待整树 SHA 收口」 | 「冻结明确标注『待整树 SHA 冻结后』，本批不提前冻结」 | 任务 5 | W4-09 |
| P06 | preset-card-generation.md:98 状态词 | 「编号全集、卡族行数与绑定值为已完成」 | 「…件数／字节／行数为已完成；树哈希绑定＝待主代理 K5 冻结」 | 任务 5 | 同批更正 |
| P07 | preset-card-generation.md:104 回执绑定值 | tree `be89d163…`（11 件／113,900 B，1,345 行）＝brief_sha `cfe0c1fd…` | 11 件／115,304 B／1,347 行；两 SHA 占位；编号／卡族／字数带计数不变 | tsv＋现树实测 | 树绑定 |
| M01 | field-id-matrix.md:132–136 | 无 | 追加「修复批时点更新（2026-11-06）」：第 68 行「中途快照」时点条件随现树稳定（101 件／1,058,396 B）解除，genre 编号普查仍须 K5 冻结前重跑；INDEX 求和与 8 份 spec 首表复测一致 | 任务 5 依赖旧树结论 | 同批更正 |
| J01 | delivery-preflight-spec.json:3 | 仅 `version`／`templates` | 加 `_freeze_note`：field_ids 未冻结、明确「待整树 SHA 冻结后」、8 条 templates／99 个 field_ids 原样未改、树哈希占位 | 任务 5（不提前冻结） | W4-09 |

## 二、W4-116 与 F-05① 同族声明（按要求）

工作单「W4-116 前缀补缀」与 `review.json` F-05① 指向**同一批 4 处裸 `SKILL.md:NNN`**（`GE-IF-02`／`IF-03`／`IF-04`／`IF-06` 的 `handoff_condition` 行文内）。本席**只处理一次**（B18–B21）：按条目上下文补完整包名前缀并按修复后现树用 `/usr/bin/grep -Fn` 重取行号，**未重复改**、未另立第二组。旧行号 `scene:289／character:307／fp:147／line:188` 与行文 `:290/:308/:148/:189` 均为修复前基线，一律未照抄。

## 三、notes/ 元数据自引未改

`notes/w4-review-queue.md:13`、`queue:30`、`notes/quality/…`、`notes/delivery-preflight-spec/…` 等 `notes/` 层自引按 `review.json` F-05 定性为合法自引，本批**未改**（B16／B17 仅改其后的结论措辞，路径字符串本身未动）。

## 四、档位与哈希纪律

- brief.json 的 `status`（GE-R18=missing）、`bidirectional`（GE-IF-05／GE-IF-07=one-way…）、gaps 的 `level`／`kind`、cases 的 `kind` 等**档位字段一律未改**，未写「通过／pass」，未删条目，保留全部编号与 JSON 结构（六组条数 19／16／7／11／12／12 回读一致）。
- operations-contract Q6 状态列**仍留 FAIL**，未写 STATIC_CHECKED／PASS。
- 所有树哈希字段写「待主代理 K5 冻结」占位，**未自造任何 SHA**；`field_ids` 冻结明确「待整树 SHA 冻结后」，本批不提前冻结。

## 五、未能定位／未闭合项（交主代理）

1. brief.json 结构化 `peer_side_anchors`：IF-02 `scene…:289`、IF-03 `character…:307`、IF-04 `fp…:147`、IF-06 `line…:188` 仍为修复前值；本批只按 F-05① 改 4 处 prose 裸行号，结构化锚重测属主代理冻结前「锚抽验」范围，未动、未闭合。
2. brief.json `interface_two_way_summary`（one_way 两档、`peer_receipt_counts_measured` cross-media 0 命中）、`notes_on_method.cannot_judge`「GE-R18 判 missing 之后…」、`preset_card_interface_probe` 的 `probes_on_skill_md`／`whole_package_probe` 0 命中数据：均属修复前档位／取证记录，依「不改档位」与 F-01 六处范围保留原样，待主代理重冻结统一处理。
3. operations-contract §三 Q1 行「实测提及本包行数」、§四 19:41:22 时点数字表、§五 X-1／X-10：按「§三 Q6 之外各行不动」未改，待主代理重取。
4. 两结构性 spec 正文内大量 `SKILL.md:NNN`／`workflow.md:NNN` 行号锚依修复前树（R7／R6 改文有位移），未逐条重测，属 K5 冻结前锚抽验范围。
5. `field-id-matrix.md` genre 段编号普查（494／88／189）未逐件重跑，须在 K5 冻结前重跑并归因。
6. F-05 gaps 四处行号经实测与旧值相同（`:1`／`:3`／`:24`／`:34`），原因是 R8 只改 genre `SKILL.md:3/:101`、未动 `references/`；已在台账登记依据。
7. GE-R16「八目录无出口承载」、cross-media description 未列 genre（对侧 F-11）未随 #11A 闭合，属他席／主代理范围，未代改。

## 六、自检与哈希

- 逐处回读＋`python3 json.load` 校验 brief.json／spec.json 均可解析；Q6 表格列数 3 列未破坏；`shasum -a 256` 取 genre brief.json 改后原始字节哈希（完整 64 位见自检文件与回报）。
- 详见 `notes/quality/repair-brief-selfcheck-2026-11-06.md`。
