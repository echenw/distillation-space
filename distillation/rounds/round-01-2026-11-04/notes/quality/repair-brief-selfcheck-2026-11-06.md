# 修复批收口席 A 自检（2026-11-06）

- 对象：`quality/genre-fiction-craft/brief.json`、`operations-contract/genre-fiction-craft.md`、`delivery-preflight-spec/` 内 INDEX／spec.json／8 份 spec／field-id-matrix 的内容层修订。
- 方法：static 只读＋逐处回读；`/usr/bin/grep -Fn`（本机 grep 为 ugrep，中文长模式不走它）；`python3 json.load` 校验 JSON；`shasum -a 256` 取原始字节哈希。未跑测试／构建／真实任务，无 git 写操作，GQ5 维持 NOT_PROVEN。
- 逐处改动台账：`notes/repair-ledger-brief-spec-2026-11-06.md`。

## 一、逐处回读

| 项 | 结果 |
|---|---|
| brief.json JSON 可解析 | PASS：`json.load` OK，六组条数 requirements 19／capabilities 16／interfaces 7／applicability 11／cases 12／gaps 12 与改前一致 |
| F-01 六处＋括注（GE-G05／G06／IF-05／IF-07／R18／T6；CAP-15 what/name/limit、T6 expected、G07 括注） | 逐处回读 PASS；`status=missing`、`bidirectional=one-way…`、gaps `level`／`kind` 等档位字段**未改**，无「通过／pass」字样，条目与编号全保留 |
| F-01 同族下游（probe.conclusion、queue_overlap 两条） | 回读 PASS，均标「修复前」＋现树更正 |
| F-06（GE-CAP-15 what/name） | 回读 PASS：description 六类→七类，位置 `:3`／`:30` 与实测依据在位 |
| F-05① 4 处 prose 裸对端行号 | 回读 PASS：均带完整包名前缀、行号为现树实测（见第三节），旧 `:290/:308/:148/:189` 裸值不再指向空行 |
| F-05② 4 处 gaps 裸文件名 | 回读 PASS：`references/10-profession-competition/` 三处、`references/` 一处；四处行号实测与旧值相同（references/ 未被修复批改动） |
| notes/ 元数据自引 | 路径字符串本身未改，PASS |
| W4-116 与 F-05① 同族 | 一次处理（B18–B21），无重复改，PASS |
| operations-contract Q6 行 | 回读 PASS：`awk -F'|' NF-1=4`（3 列未破坏）；状态列仍 `FAIL`；文末新增节 4 小节齐 |
| spec/INDEX/JSON | `json.load` PASS：templates 8 条、field_ids 合计 99 未动；`待整树 SHA 冻结后` 措辞在 INDEX／两 spec／JSON／matrix 均在位；旧树哈希与旧字节仅出现在「基线说明」语境，无自造 SHA |

## 二、genre brief.json 改后原始字节 sha256

```
7d5e5c847c957f54396ee6e685ecdcbb3bec3eda5d2cd16c625a611c0a3495a9
```

（`shasum -a 256 notes/quality/genre-fiction-craft/brief.json`；改前基线 `7872b7917168b836232bab98b9f6c7dda85a7b3450c3697217c1ad4c99731053`。主代理可写入 review.json。）

## 三、F-05 四处对端行号（修复后现树实测）

| 条目 | 包名＋行号 | 该行文本前 40 字 |
|---|---|---|
| IF-02 | `scene-conflict-and-rhythm/SKILL.md:290` | `| 「武侠打斗写不好」 | 题材约束看 \`genre-fiction-craft` |
| IF-03 | `character-and-narrative-control/SKILL.md:309` | `| 「武侠打斗写不好」 | 题材约束看 \`genre-fiction-craft` |
| IF-04 | `fiction-planning-and-diagnosis/SKILL.md:153` | `| 不像这个类型，读者觉得货不对板 | FC-20 | \`genre-ficti` |
| IF-06 | `line-editing-and-proofreading/SKILL.md:188` | `| 「武侠打斗写不好」 | 题材约束看 \`genre-fiction-craft` |

四处均以 `/usr/bin/grep -Fn` 按文本实测，未照抄工作单旧行号 `scene:289／character:307／fp:147／line:188`。scene 实测 `:290` 与旧行文数字巧合相同，但旧值指空行、现树 `:290` 为实文（R2 在 `:275` 增 1 行致 `:289` 起 +1）。

## 四、Q6 重取六问事实（摘要）与建议档位（不自行落档）

| 问 | 现树事实 | 现记档 | 建议档 |
|---|---|---|---|
| Q1 触发 | 转给表 `:24`–`:30` 共 7 行；description `:3` 已补 preset-card-generation（实测命中 `:3/:30` 2 行）；两条负触发 `:34`；7/7 对侧有接收行（character 5／fp 6／scene 3／line 3／cross-media 3／preset 3／story 2，较 Q1 行旧数字有位移、Q1 行按范围未动） | STATIC_CHECKED | 维持；Q1 行数字待主代理重冻结刷新 |
| Q2 缺料 | 禁止编造 `:40/:52/:44`；14 目录无稿出口；「未知」分布 53 文件；无脚本／自动执行声明 | STATIC_CHECKED | 维持 |
| Q3 冲突 | `:108` 顺序成文、决定者＝作者、局部暂停不报整体 | STATIC_CHECKED | 维持 |
| Q4 权限 | `agents/openai.yaml:2/:8`、`:42`；无脚本无写入声明 | STATIC_CHECKED | 维持 |
| Q5 格式 | 非 md/yaml 文件 0 命中；14 件模板、ID 独占表行 189（60/32/37/26/15/19）复测一致；四表数据行 30；列名裁定在册 | STATIC_CHECKED | 维持 |
| Q6 消费者 | §6 措辞按 #11A 已对齐实况（不再承诺两栏）；栏目实测 10/14、0/14、9/14、独立 H2 3/14（含 13 变体 4/14）；原「承诺落空」FAIL 主据不成立；F-02 数值未变、GE-R16 八目录无出口承载未变 | **FAIL（本批未改）** | **待独立复核**：由主代理依独立复核席结论定档；本席不写 STATIC_CHECKED／PASS |

## 五、未能定位／未闭合项

1. brief.json 结构化 `peer_side_anchors`（scene:289／character:307／fp:147／line:188）仍为修复前值 —— F-05① 只授权改 4 处 prose 裸行号，结构化锚重测属主代理冻结前锚抽验，未动、未闭合。
2. brief.json `interface_two_way_summary`（one_way 两档、cross-media 0 命中计数）、`cannot_judge` 的 GE-R18 missing 条、`preset_card_interface_probe` 的 0 命中 probe 数据：修复前档位／取证记录，依「不改档位」保留，待主代理重冻结。
3. operations-contract Q1 行数字、§四 19:41:22 时点表、X-1／X-10：按「Q6 之外各行不动」未改，待主代理重取。
4. 两结构性 spec 正文内行号锚依修复前树（R7／R6 改文有位移），未逐条重测，属 K5 冻结前锚抽验。
5. `field-id-matrix.md` genre 段编号普查未逐件重跑，须 K5 冻结前重跑并归因。
6. GE-R16 八目录出口承载不齐、cross-media description 未列 genre（对侧 F-11）未随 #11A 闭合，属他席／主代理范围。
7. 哈希冻结、field_ids 冻结、tsv 单笔更新、checklist／log／desourcing-ledger 收官行、review.json 写入、8 包重绑复测与锚抽验 —— 均属主代理冻结步骤，本席未做。

## 六、自检结论

内容层修订**闭合**：F-01 六处及括注、F-06、F-05 八处寻址补缀、Q6 事实更新、spec／INDEX／JSON 树重算均按修复后现树逐处落地并回读；档位未落、SHA 未自造、field_ids 未提前冻结、写入范围未越界、未跑测试／构建／真实任务、无 git 写操作。上述 7 类未闭合项已如实登记，交主代理冻结批接续。

收口席 A · 自检完（2026-11-06）
