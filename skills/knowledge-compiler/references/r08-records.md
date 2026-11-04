# R08 — 组织知识记录

需要正式知识记录时，查这里的类型、字段和维护责任。原始观察、学习记录、可复用模式、正式条目和长期原则各有用途；保存格式以随包 Schema 和脚本为准。

历史来源： `.distill/round-2/05-DATA-MODEL.md` §1（行 8–22）、§3（行 75–99）、§4（行 101–114）、§5.1–5.6（行 116–239）、§6（行 241–255）、§7 DEFERRED（行 257–263）、§8 边界（行 265–270）。生成于 2026-10-06，wave 4。
状态说明：本文解释字段设计，文末保留历史对照；历史缺口不代表当前源码。保存格式与行为以 `../scripts/` 及 `../schemas/` 的 12 份 JSON Schema 为准。
引用约定：`[05:N]` = `05-DATA-MODEL.md` 第 N 行；`[07:N]` / `[10:N]` 同理。行号保留原整理时点的定位。provenance 11 字段的逐行内容见 R05，本文件不重复其表。

---

## 阅读导航

- Schema 一览：12 份数据格式各自管什么、由谁写入
- 1. 五个实体与它们的边界 `[05:10-16]`
- 2. 生命周期列：15 个条目列 + 1 个配置项 `[05:79-99]`
- 3. 与 Agent 12 字段集的 10 条合并裁决 `[05:103-114]`
- 4. 必含字段的定案（§5.1–§5.6）
- 5. 哪个表拿哪些列（`05` §6 照录）`[05:243-255]`
- 待确认与暂缓事项
- 历史源码对照

## Schema 一览

12 份 JSON Schema 在 `../schemas/` 目录，约定各类记录的数据格式。右列写明每种记录由哪个环节产生或保存。

| # | Schema | 用途与写入方 |
|---|---|---|
| SC01 | `evidence.schema.json` | S01/S03：原始证据 |
| SC02 | `learning.schema.json` | 一次学习记录；接入方需核对真实使用方式 |
| SC03 | `pattern.schema.json` | S05：可复用模式 |
| SC04 | `artifact.schema.json` | S12：正式知识条目 |
| SC05 | `lifecycle-record.schema.json` | S17 检查状态，S12 保存记录 |
| SC06 | `provenance-record.schema.json` | S13 生产完整 10 键 / 11 字段；S12 transaction history 保存，`read_provenance` 读取 |
| SC07 | `lifecycle-event-ledger.schema.json` | S12：唯一的状态变更记录写入方 |
| SC08 | `candidate-quarantine.schema.json` | S11：候选暂存；获批不等于 COMMITTED |
| SC09 | `eval-bundle.schema.json` | S15/S16：评测材料；记录本身不证明运行方身份 |
| SC10 | `budget-config.schema.json` | 人工确定预算，S18 执行检查 |
| SC11 | `scope-tuple.schema.json` | project/global/cohort：知识适用范围 |
| SC12 | `verdict.schema.json` | S10：逐项审核结果 |

Schema 只约定数据格式。`../scripts/kd_validate.py --kind <kind> --input <file>` 检查完整文档，缺少格式定义时返回 `SCHEMA_MISSING`。具体字段以 `../schemas/` 里的文件为准；输入上限和错误输出见 R02 §8。

## 1. 五个实体与它们的边界 `[05:10-16]`

```text
Evidence            原始观察事实。只追加，永不被裁决改写。
Learning            一次「问题→原因→处置」的记录，01/04/07 型 .learnings 条目的形式化。
Pattern             跨 Evidence 聚合出的复发单位，是晋升门唯一读取的计数载体。
Knowledge Artifact  落到常驻层的产物（rule / skill / doc / script / test / lint / eval）。
Lifecycle Status    前四者的状态、计数与门票列。独立成表，不与正文同生命周期存放。
```

三条实体级红线（每条都有直接证据）`[05:18-22]`：

| 红线 | 规则 | 证据 | 出处 |
|---|---|---|---|
| 1 | **`Lifecycle Status` 不得与可重建索引同生命周期存放**（索引可删，计数不得随之归零） | Agent 11 `counter_invariant` (5)；正例 `06:use-view-patch-split-instrumentation` 的四道闸与 sidecar 随目录原子迁移 | `[05:20]` |
| 2 | **一个业务语义只有一个 Owner** | DD-4 `rejected_alternatives` 点名 `10` 侧「同一业务语义 4 个 Owner」（`applyDecay 0.9^periods` / lesson-insight 线性周衰减 / retention `exp(-λΔT)` λ=0.01 / evict-auto-forget 规则驱逐），跨层分数不可比 ⇒ 本 schema 只有一个淘汰判据入口 | `[05:21]` |
| 3 | **每个字段必须绑定至少一个真实消费分支**（排序 / 写入权 / 晋升 / 失效 / 报告渲染 之一），否则 schema validator 拒绝写入。例外：`lifecycle_event` 账本类字段的消费者是 auditor 与人 | Agent 12 `self_reference_failures[4]`；反例 `10:write-time-origin-channel`（写入期不可变 origin，但 `context.ts`/`search.ts`/`enrich.ts` 无按 `origin.channel` 降权分支 ⇒ 只记录不决策）、`05:skill-mtime-field-without-consumer`（VERIFIED，算出 mtime 写进 JSON 而无任何步骤使用） | `[05:22]` |

---

## 2. 生命周期列：15 个条目列 + 1 个配置项 `[05:79-99]`

放在 **Lifecycle Status** 表；`[E]` 均出自 DD-4 `minimum_lifecycle_fields` 与其 evidence 数组。

| 列 | 类型 / 枚举 | 答哪一问 | 谁写入 | 何时失效 | 无它则哪问答不了 | 出处 |
|---|---|---|---|---|---|---|
| `lifecycle_state` | enum `{candidate, active, superseded, archived, rejected, failed}`（**6 个存储态**，见 07） | Q7 | **状态机唯一写路径** | 迁移即写新账行 | 淘汰结论若每次重算，复活无法撤销删除资格、误标无法回滚 | `[05:81]` |
| `last_activity_at` | datetime（= use/view/patch 三者最新；**显式不含 `created_at`**）；**派生列，禁止手工写** `[05:99]` | Q7 | 派生：由计数器写 | — | 不排除 `created_at` 就失去「从未活动」的可辨识度，新条目按创建时间被老化 | `[05:82]` |
| `use_count` | int | Q7 | `PreToolUse`/真实消费事件锚点 | 条目目录迁移时随目录走 | 无分子 → 无法算服从率 | `[05:83]` |
| `view_count` | int（**与 use 严格分离，禁止合并**；`patch` 单独且**不加分**） | Q7 | 读/展示事件锚点 | 同上 | 合并会把「被打开过」当「被遵守」，知识库将**选出写得好看的条目** | `[05:84]` |
| `opportunity_anchor` | int | Q7 | 首次纳管时播种 | 条目重建即重播 | 无 anchor → 分母退化成墙钟 | `[05:85]` |
| `layer_request_count` | int（`opportunities = max(0, request_count - anchor)`） | Q7 | 全局请求计数器（每层一个） | — | 分母必须是**机会数**而非墙钟，才使「从未被召回」不被判陈旧且判定不读时钟 | `[05:86]` |
| `created_by`（ownership） | enum/string 权威成员键 | Q5、Q7 | 装配层写盘时判定，**不由内容自报** | 归属变更仅人类 adopt | 无它则无法守「只对自己产出的条目计数与归档」的零侵入红线 | `[05:87]` |
| **`tombstoned_at`**（15 的原始列名 `superseded_at`） | datetime? —— **删除资格的唯一门票** | Q7 | **只有 decay 驱逐与 reconcile-delete 安全网两类动作写它** | **重新写入或再次真实使用时清空**（复活即撤销资格） | 无它则「安全网可能误判」只能靠另建 undo 系统兜，而 15 的 hard-delete 不可撤销 | `[05:88]` |
| `deletion_grace_days` | **配置项**（作用在 `tombstoned_at` 上，**不作用在条目年龄上**） | Q7 | 配置 Owner | 改配置即改判定 | 宽限期锚在标记时刻才与「零使用不判陈旧」一致 | `[05:89]`（M10 裁决：从条目列改为配置） |
| `absorbed_into` | ref?（merge/absorb 时**非空且目标必须已存在**） | Q7 | MERGE intent 的唯一写路径 | 目标伞形被删时该 intent 已被 fail-closed 挡住 | 归并留不下可验证的前向引用 → 「归档了一簇但没归并」不可检测（真实事故 #29912） | `[05:90]` |
| `first_seen_at` / `seeded_at` | datetime?（**合并为一列**） | Q4、Q7 | 首次观测时播种（并推迟一个周期） | — | 无播种时钟 → 新装机/更新的首个 tick 批量迁移整棵树 | `[05:91]` |
| `pinned` | bool（豁免轴 1） | Q7 | 人类显式设置 | 人工取消 | 无它则 pinned 条目被自动迁移（`14`：pinned 豁免每一个 auto-transition 与 LLM 评审） | `[05:92]` |
| `referenced_by_external` | ref 集合（豁免轴 2） | Q7 | 引用扫描器 | 引用消失即失效 | 无它则被 cron 引用的低频 job 被墙钟熬过期 | `[05:93]` |
| `decay_type` | enum `{reality, decision, dependency, relevance, unknown}`（第三条失效轴，**允许 unknown**） | Q7 | 失效归因写路径（模型判定后由代码回写） | 重验即改，且留账 | 年龄与使用都不能证明内容错误；不给通用半衰期、不编 owner | `[05:94]` |
| `last_validated_at` | datetime? | Q6、Q7 | **只有重验通过才推进** | 上游产物变化即视为过期 | 证据缺失/冲突时禁推进 | `[05:95]` |
| `validation_state` | enum `{pending, verified, unresolved}` | Q6 | eval/audit runner | 记录消失即回落 pending | 无它则把提案当已验证；**review 不是生命周期事件**（不加 Recurrence-Count、不刷 Last-Seen） | `[05:96]` |

**原子列核算（照录）** `[05:98]`：上表 **16 行** = **15 个 Lifecycle Status 条目列 + 1 个配置项**（`deletion_grace_days`，M10 裁决移出条目表）。相对 DD-4 原 14 条：展开内部并列写法后得 **20** 个原子列，随后收敛 **M6 −1 → 19**、**M1 −2 → 17**、`first_seen_at`/`seeded_at` 合并 **−1 → 16**、`deletion_grace_days` 转配置 ⇒ **15 条目列 + 1 配置项**。
`lifecycle_event` 表另含 `actor`/`reason`/`supersedes`/`superseded_by` 四列，**计入账本表而非条目表** `[05:99]`。

---

## 3. 与 Agent 12 字段集的 10 条合并裁决 `[05:103-114]`

| 编号 | 重复 / 冲突 | 裁决（要点照录） | 理由要点 | 出处 |
|---|---|---|---|---|
| **M1** | Agent 12 的 `lifecycle[] {at,op,actor,reason,supersedes\|superseded_by}` 与 DD-4 的 `transition_actor + transition_reason` **是同一张账** | **合并为单一 `lifecycle_event` 表**：列 = `{at, op, actor, reason, supersedes, superseded_by, entity, entity_id}`；actor 枚举取 DD-4 `{curator, user, merge, agent}` ∪ Agent 12 `{human, import, shared}`；reason 枚举取 DD-4 `{decay-sweep, archive, absorbed, reactivated, tombstone}` 并补 `reactivated`；约束取「append-only + 一次 batch op 只写一行 + detail 不作权威」 | 同一业务语义（迁移账）只能有一个 Owner；两份并存 = 第二权威。actor/reason 是**成对**写入的（`14:set_ledger_actor('curator')`、`10:strength-and-confidence-decay`、`11:read-telemetry-weight-settling`），故保留两列而非合成字符串 | `[05:105]` |
| **M2** | DD-4 的 `ownership(created_by)` 与 Agent 12 的 `provenance.actor` 看似重复 | **保留两列，职责不同**：`created_by` = 谁产出内容（决定**入池资格**：准入/召回/计数/策展/合并五条路径各自判定）；`provenance.actor` = 谁写了这次变更（决定**写入权与归因**） | 最强样本 `14` 里本来就是两套（`skill_usage.py created_by` vs `skill_ledger.py _VALID_ACTORS`）。合并会丢掉「必须能区分人挪的还是自治挪的，否则审计无法定位责任 Owner」 | `[05:106]` |
| **M3** | `generation.created_at` 与 `last_activity_at` 显式排除 `created_at` | **两者都保留**，`last_activity_at` 为派生列、禁止手工写 | 不冲突而是分工：前者答 Q4/Q5（不可变出生戳），后者供淘汰 anchor；删掉 `created_at` 反而答不了 Q4 | `[05:107]` |
| **M4** | 删除门票命名：DD-4 叫 `tombstoned_at`，`15`/Agent 11 叫 `superseded_at` | **统一命名 `tombstoned_at`**，`superseded_at` 作 15 的原始列名注记；`superseded_by`/`invalid_at` 独立成对。并**要求把产生原因写进 `lifecycle_event.reason`**，**不采纳** `15` 让两类门票「故意不可区分」的做法 | 「SUPERSEDE 与 DELETE 不得共享任何状态位」且「两个字段两种可逆性」（门票可被复活清除，语义链单调不可清空）；若命名 `superseded_at` 与 `superseded_by` 同族名，实现上极易被误当成「凡 supersede 都写它」 | `[05:108]` |
| **M5** | `evidence.status` 与 `verification[].verdict` 都含「已验证」 | **保留两列**：`status` 是单条**取证**状态（VERIFIED/UNVERIFIED/UNKNOWN，由 resolver/审计写），`verification[]` 是**判分**记录（eval runner 追加） | 回答不同问（Q2 vs Q6）。合并会让「我确实打开过这个文件」被当作「有 eval 通过」。反例 `[E]`：`07` 把未接线的门标 Implemented | `[05:109]` |
| **M6** | DD-4 的 `maturity_threshold_ref` 写成条目字段 | **从条目表移除**，配置为唯一 Owner；条目侧只允许可选的 `maturity_override`（默认 NULL = 继承） | 把阈值复制进每条条目 = 制造第二权威，直接违反 `04`/`14` 的 const-anchor 原则 | `[05:110]` |
| **M7** | `use_count/view_count` 与 Pattern 层 `support_count` 易被当成同一计数器 | **三个不同载体，禁止互通**：`Evidence` 层 = 事件计数（use/view/patch）；`Pattern` 层 = `support_count` / `distinct_occurrence_count`（晋升门唯一读取）；`Artifact` 层 = `adherence_rate`（淘汰判据） | 依据是三处各自独立实现（`02:repeated-workflow-threshold-promotion` 读 `matches.len()`、`06:adherence-rate-probation-capacity` 读 `rate=use/(watermark-anchor)`、`01:decay-type-maintenance-contract` 禁止用使用/年龄推内容错误）。混用一个计数器会让「被打开过」直接凑出晋升 | `[05:111]` |
| **M8** | `contradiction_count` 的写入者：`10:auto-forget-ttl-contradiction` 用 `Jaccard>0.9` 当冲突弃旧 | **拆两列**：`near_duplicate_count`（确定性 proxy 可写）与 `contradiction_count`（**只有模型判定后由代码回写，且必须逐条留 `lifecycle_event`**） | `10` 自身 risks 明写「高相似 ≠ 矛盾」；`14` holographic 的 `contradiction_score = entity_overlap*(1-content_sim)` 依赖英文实体正则，CJK 命中率低 | `[05:112]` |
| **M9** | Agent 12 的 `staleness` 字段 vs 07 的「stale 不作为存储态」 | **`staleness` 不物化**：只存计数器 + 时间戳 + 门票列，stale 每次读时计算；`derived_from[]` 作为**视图计算输入**保留，`staleness` 作为列删除 | `14` 把 stale 存进 `.usage.json`，结果必须由 `reanchor_clock` 回滚被旧 bug 误标的记录（artifact #79295）；`11` 明确反对——用 status 字段表达「已过期/已替换」会引入第三种状态并覆盖历史 | `[05:113]` |
| **M10** | `deletion_grace_days` per-entry vs 全局配置 | **配置为唯一 Owner**；条目侧默认 NULL 继承；显式覆盖必须留 `lifecycle_event` | `15:ttl-pinned-priority-and-forget-sweep` 的 Pass3 判据是「tombstone 且门票年龄 ≥ `hard_delete_after_days`（默认 180）」——是全局参数不是逐条参数；保留 DD-4 语义（作用在 `tombstoned_at` 上） | `[05:114]` |

---

## 4. 必含字段的定案（§5.1–§5.6）

### 4.1 `identity`：采信 DD-2 的分层 L0 / L1 / L2 `[05:118-149]`

```
L0 主判（唯一持有自动计数与写盘权）：
   identity = sha256( canonical 字段 NUL-join )[0:40] ‖ 显式 Pattern-Key 字段
   canonical 字段 = 结构化语义字段精确等值，**簿记字段排除**（形状来自 11 的 _duplicate_key）
   等值命中 → support_count += 1（DD-2 选定的唯一自动写入条件）                       [05:121-129]
L1 相似但不等值 → 只产提示/提案，绝不自动写盘：
   near_duplicate_count 计数、possible_duplicate 标记、T1 提案（11 的 _propose_merges 形态；10 的 0.4–0.7 similarTo 形态）
   提示进人工或后续 pass。                                                            [05:131-134]
合并写必须走可逆 supersede：
   删除只走单一审核通道(02 形态)；11 的 test_exact_duplicates_are_merged_by_supersede_not_by_deletion；
   10 的 >0.7 自动 supersede 之所以被接受，**唯一理由是其 version/parentId/supersedes 链可逆、KV 保留** [05:136-139]
L2 embedding 自动聚类：**不采用**。
   DD-2 立场 D 的唯一支撑 15:cold-cluster-dedup-merge 为 UNVERIFIED（adaptive_eps 数值 UNKNOWN），
   按 SPEC §2 不得当已证实使用。                                                       [05:141-143]
漏报（under-report）缓解只用确定性手段：
   降级分组（01：同 Area + ≥2 相同 Tags 或 Related Files 精确路径匹配，**仍禁止 fuzzy-match**，
   原文「Do NOT fuzzy-match on Summary text — false groupings are worse than ungrouped entries」）+ 窄归一（12） [05:145-147]
```

残余风险（如实记）`[05:148-149]`：等值主层仍漏同义写法，需 L1 提示层 + 人工 pass 出口兑现；`02` 的 rejected 提案会被下轮重复提议（无抑制），属提案通道已知缺陷 `[E]`。**分层本身无单项目 1:1 完整实现（11/10/02 各实现一个子集）→ 组合形态标 `[I]`，各层有据、拼法无据。**

### 4.2 `content_hash` `[05:154-164]`

```
列：content_hash = sha256(归一化后的正文字节)，归一化 = normalize(CRLF→LF, 去行尾空白, 去尾空行, trim)
(a) 精确等值判重的唯一依据 —— distill dedupe.rs 原话 identity = NORMALIZED FULL TEXT EQUALITY，
    「No similarity, no hashing prefix, no semantics — a paraphrase is never detected」；canonical = 字典序最小文件名，
    已有 pending remove 即幂等，--dry-run 不写不建目录（8 个单元测试）
(b) 内容相等短路：sha 相同 → 不产生新版本、不建假链（15:page-supersession-chain）
(c) 使 verification[].artifact_sha 有可指认的比对目标 → 正文变了旧 verdict 自动过期
禁止：把 content_hash 当 identity 的全部（identity 还需 scope 与 canonical 语义字段），
     也禁止让模型命名 hash 的输入字段集合（见 04 §7.1）。
```

### 4.3 `scope`：显式解决 `02` 的「算了无消费者」全局污染 `[05:167-189]`

问题陈述（**全局性风险，不是可选优化**）`[05:169]`：`worker-caveats 02` 记录 `SessionDescriptor.project` 与 `cohort_key` **被计算但从不参与分组**，pattern aggregation / promotion / dedupe 全为 global；DD-6 矛盾列表原话「即确定性门当前在跨项目语料上开门」；DD-1 立场 A 的 F3「作用域算了不消费 → 跨项目同键合并计数（反向假阳性）」。DD-6 重开条件第 5 项明文：**该问题必须先修，否则本裁决会在跨项目语料上误开门。**

```
scope = 类型化三元组 { workspace, project, layer }，layer ∈ {project, global, cohort}      [05:174]
S1 非空且 fail-closed：scope 缺失或不可解析 → 拒绝入库，不默认 global。                      [05:176-179]
S2 每个消费者必须显式声明过滤维度，schema validator 拒绝无消费者的 scope 列；
   判定方法 = 静态列出该列的全部读取点，为空即拒（红线 3 的直接应用）。                        [05:180-182]
S3 计数器按 scope 分桶：support_count / distinct_occurrence_count / layer_request_count 的 key 必须含 scope；
   跨 scope 聚合只有在 layer=global 的晋升通道上、且经过 distinct-source 去重后才允许。 [I]  [05:183-185]
S4 晋升门的裁决对象必须带 scope，且 Project Rule 与 Global Rule 是两条不同终态（见 06）。
   反例：scan-skills.sh:91-114 用 jq -s 'add' 拼接全局层与项目层、无去重、条目无 layer/source 字段，
   「同一 skill 的两份副本可把 1 个来源伪造成 2+ 并直接满足晋升门槛」（DD-1 F1）。            [05:186-189]
```

### 4.4 计数器准入规则（`support_count` / `distinct_occurrence_count` / `contradiction_count`）`[05:192-219]`

**任何进入决策的计数器必须有可指认的写入者与测试。** 五条准入条件（Agent 11 `counter_invariant`，原样采纳）`[05:194-203]`：

```
(1) 写入者：一个明确的事件锚点 + 调用点（谁在什么事件 +1），实现清单里给出文件与符号
(2) 测试：至少一条「事件发生 → 字段变化」的行为测试 + 一条「字段变化 → 决策改变」的端到端断言
(3) 消费者闭合：默认值/无值状态不得被渲染成真实数据；模板必须能区分「从未测得」与「0」
(4) 生命周期配套：拥有该字段的条目必须同时存在衰减/归档/淘汰路径，否则库只增不减
(5) 存放边界：使用计数不得与可重建索引同生命周期存放
缺 (1) 或 (2) → 该字段**禁止进入任何决策，且不得作为「证据缺失」的旁证**。
```

**头号反例（必须内嵌）** `[05:205]`：`08` pro-workflow 的 `learnings.times_applied` —— `schema.sql` 有 `DEFAULT 0`，`store.ts:85` 接口、`:143-145` 语句、`:306-307` 实现三处 `incrementTimesApplied`，但 `grep -rn "incrementTimesApplied" scripts src commands skills hooks` **无任何外部调用者 → 计数器恒为 0**；而 `searchByCategory` 按 `times_applied DESC` 排序、`getMostAppliedLearnings` 过滤 `>0`、`collectTrajStmt` 按它选训练轨迹、`trajectoriesToValidation` 用它算 eval 权重 `1+min(2,log2(1+timesApplied))`，模板把 `(applied 8x)` 当真实数据渲染 —— **一个无写入者的字段穿过排序、采样、权重、渲染、淘汰提示五条决策路径**；该项目另无任何 decay/archive/prune 实现，违反 (4)。
同类缺口 `[05:207]`：`06` 的 sidecar `verification` 本轮未见写入者（UNKNOWN）；`15` 的 `breadth_weight` 默认 0 使团队广度信号默认不生效；`10:mem::cascade-update` 的 `siblingMemories` **只计数不写状态**（落差被测试固化）。

| 字段 | 载体 | 写入者（事件 → 调用点） | 消费者 | 测试要求 | 出处 |
|---|---|---|---|---|---|
| `support_count` | Pattern | L0 identity 等值命中（ingest 时） | Stage 1 阈值门 | ①命中→+1 ②达阈→产提案；配对列 `last_attempted_count`（`state.rs:161 matches.len() <= last_attempted_count`，重试必须是新增第 N+1 条证据） | `[05:215]` |
| `distinct_occurrence_count` | Pattern | canonical occurrence 折叠后（同一 Occurrence-ID 跨镜像/fork/转发/trace 折叠；**不同路径 ≠ 独立证据**） | Stage 1 的「最小来源数」门（挡住 F1 批量同源瞬间达标） | 三条行为断言：copied log 折叠 / legacy 不能证明 2 distinct tasks / terminal 不再晋升；legacy 无 provenance 时 **unknown-lineage 合计最多算 1 个 distinct task** | `[05:216]` |
| `contradiction_count` | Pattern / Artifact | **模型判定后由代码回写**（M8 的 `near_duplicate_count` 分离）；确定性只允许写 proxy 列 | Stage 0 冲突路由 + 报告渲染 | 「模型判为矛盾→字段变化→进入 judge 队列」的端到端断言 | `[05:217]` |

并发正确性必须写进设计（不能留作实现细节）`[05:219]`：`06` 的 sidecar bump 是 read-modify-write、**跨进程非原子、锁 deferred**，其 caveats 明确「计数偏低 → 更早归档」；对策采 `10` 的形状：**keyed lock + `count = max(count, recent.length)` 自愈**；若拿不到锁证明，则必须把「偏低」写进零使用判定（对照 `use==0 && view==0` 双条件）。

### 4.5 三个不由被记录对象自报的字段 `[05:221-223]`

`provenance.actor` / `verification` / `lifecycle`：共同约束是**都不由被记录对象自报**，都只能由网关/runner/账本 Owner 写；`provenance.actor` 缺省 **fail-closed**；`verification` 正文不得编辑既有 verdict；`lifecycle` 只追加。（逐字段内容见 R05 §2。）

### 4.6 `tombstoned_at` —— 可撤销删除资格位 `[05:228-238]`

```
定义：datetime?，NULL = 无删除资格。只有两类动作可写它（decay 驱逐 / reconcile-delete 安全网），其余一律不写。
撤销：同一目标被重新写入或再次真实使用时清空 → 旧版本从 hard-delete 候选变回受保护的链成员。
唯一性：物理 DELETE 的判据只吃这一列 + 门票年龄 ≥ deletion_grace_days + 人工执行。
     （11:gc-only-human-physical-deletion + test_gc_is_the_only_road_to_physical_removal）
五家印证（distinct projects，SPEC §7.7）：06/10/11/14/15 都把「标记」与「物理移除」实现成两个动作，
     中间隔一个可撤销状态。这是 DD-4 认定「共识最强的一条」。
禁止：把 15 的「两类门票来源故意不可区分」原样采用 → 改由 lifecycle_event.reason 记来源（见 M4）。
```

---

## 5. 哪个表拿哪些列（`05` §6 照录）`[05:243-255]`

```text
Evidence            content_hash · scope(S1–S4) · origin.{problem,why,source_refs} · evidence_refs[] ·
                    evidence.status + status_basis · generation{...} · record_locator · refs_integrity
                    （无计数器：Evidence 不参与淘汰，避免把原始观察当成可晋升单位）
Learning            Evidence 的全部 provenance 列 + identity(L0) + Pattern 链接 + decay_type +
                    last_validated_at/validation_state（01 型 .learnings 条目的形式化）
Pattern             identity · support_count · distinct_occurrence_count · last_attempted_count ·
                    near_duplicate_count · contradiction_count · scope · absorbed_into（合并终态）
Knowledge Artifact  content_hash · identity · scope · provenance.actor · verification[] ·
                    use_count/view_count(+patch 单独) · opportunity_anchor · layer_request_count ·
                    pinned · referenced_by_external · first_seen_at/seeded_at · absorbed_into
Lifecycle Status    lifecycle_state · last_activity_at · tombstoned_at · lifecycle_event[]（唯一账本，M1）
```

§6 与 §3 的关系：§3 声明 15 列**住在** Lifecycle Status 表；§6 只列 4 个「不与 §3 重复归属」的列，其余 11 列在 §6 里被写到 Artifact / Learning / Pattern 名下 ⇒ 两处口径不完全一致，见文末核算第 6 条。

---

## 待确认与暂缓事项

`05` §7 的 3 条 DEFERRED（本文新增 2 条的说法照录原文，**本文件不关闭任何一条**）`[05:257-263]`：

- `DEFERRED id DM-1`：`identity` canonical 字段集合的最终清单（哪些字段进 NUL-join、簿记字段如何枚举）与 hash 截断长度。与 `04` 的 **D6-a** 同一个缺口：≥50 个真实候选上的口径分歧度量。当前只定到「必须含 scope + 语义字段 + 排除簿记字段」。
- `DEFERRED id DM-2`：`provenance.actor` 的具体数值如何映射为降权系数（D1 排序的权重表）。当前只定到「层级顺序 + verification 为空即不进 always-on 注入」这一保守形状。（同一条在 R05 以 `D10-1` 名义登记。）
- `DEFERRED id DM-3`：`distinct_occurrence_count` 的 Occurrence-ID 来源（宿主事件 id？会话 id 派生？）。需确认 Compiler 侧能拿到稳定 occurrence 锚点，**否则该列降级为 `distinct_source_projects` 计数**。
- `UNKNOWN` / `[I]` 位（照录，不得当作定案）：identity 的**组合形态标 `[I]`，各层有据、拼法无据** `[05:149]`；`scope` 的 **S3 标 `[I]`**（由 S1+S2 与 DD-1 F1/F3 推出）`[05:183-185]`；`contradiction_count` 的要求列 `[I]` `[05:217]`。
- 证据边界 `[05:267-270]`：`13`（awesome-Self-Improving-Agents）**无实现**，不用它支撑任何字段设计；本文所有 MUST 均为**簇级 32** 口径（成员级 188 为刻意通胀）；许可缺失集 = {`distill`, `pskoett-ai-skills`, `hermes-agent-self-evolution`, `pro-workflow`}，`worker-11`(agent-memory) 许可类型 **UNKNOWN**；`05` §2 各行的「实测」均为 Round 1 / Round 2 已落盘的静态取证结果，**未运行任何 test/build**。

## 历史源码对照

以下保留历史构建时点对 12 份 Schema 的只读观察（python3 stdlib；当时未运行测试套件），不作为当前实现或本轮验证证明：

1. **`lifecycle-record.schema.json`（SC05）恰为 §3 的 15 个条目列**：`required` = `properties` = 15 项，逐字为 `lifecycle_state, last_activity_at, use_count, view_count, opportunity_anchor, layer_request_count, created_by, tombstoned_at, absorbed_into, first_seen_at, pinned, referenced_by_external, decay_type, last_validated_at, validation_state`，`additionalProperties: false`。**`deletion_grace_days` 不在 properties/required**，而在 `$defs.lifecycle_config`（schema 描述原文：「The one admitted configuration item, `deletion_grace_days`, lives in $defs.lifecycle_config and is NOT an entry column (05 §4 M10)」）⇒ **15 + 1 的口径与 `[05:98]` 完全一致**；`first_seen_at`/`seeded_at` 也确实只剩一列。
2. **三个枚举逐字相同**：`lifecycle_state` = `[candidate, active, superseded, archived, rejected, failed]`（6）`[05:81]`；`decay_type` = `[reality, decision, dependency, relevance, unknown]`（5）`[05:94]`；`validation_state` = `[pending, verified, unresolved]`（3）`[05:96]`。`artifact.schema.json` 的 `kind` = `[rule, skill, doc, script, test, lint, eval]`（7）逐字等于 §1 的 Knowledge Artifact 定义行 `[05:14]`。
3. **M1 的账本列已实现且超出 8 列**：`lifecycle-event-ledger.schema.json`（SC07）`required` = 12 项 = M1 的 `{at, op, actor, reason, supersedes, superseded_by, entity, entity_id}`（8）`[05:105]` **加** `{seq, detail, record_locator, content_hash}`（4）。`actor` 枚举 = `[curator, user, merge, agent, human, import, shared]`（7，恰为 DD-4 ∪ Agent 12）；`reason` 枚举 = `[decay-sweep, archive, absorbed, reactivated, tombstone, null]`（5 + null）；`op` 枚举 = `[ADD, MERGE, UPDATE, SUPERSEDE, DELETE, REINFORCE, DECAY, ARCHIVE]`（8，**`05` 未列举 op 词表**）。⇒ 4 个附加列与 op 词表是代码侧新增，`05` 无对应行；`detail` 保留且 schema 不作权威（与 `[05:49]` 一致）。
4. **`scope-tuple.schema.json`（SC11）逐字实现 §5.3**：`required`/`properties` = `{workspace, project, layer}`（3），`layer` 枚举 = `[project, global, cohort]` ⇒ 与 `[05:174]` 一致；S1 的 fail-closed 体现在 3 项全 required（无默认 global）。
5. **三个计数载体的分桶符合 M7（禁止互通）**：`pattern.schema.json` 有 `support_count`、`distinct_occurrence_count`、`last_attempted_count`、`near_duplicate_count`、`contradiction_count`、`scope`、`absorbed_into`（+ `possible_duplicate`，见下条）；`artifact.schema.json` 有 `use_count`/`view_count`/`patch_count`/`opportunity_anchor`/`layer_request_count`；`evidence.schema.json` **无任何计数列** ⇒ `[05:246]`「无计数器：Evidence 不参与淘汰」被 schema 落实。
6. **代码里有、`05` §6 的名下清单里没有**（逐个登记，不判定谁对）：
   - `pattern.schema.json` → `possible_duplicate`。它出现在 §5.1 的 L1 描述里 `[05:132]`，但**不在 §6 的 Pattern 列清单** `[05:249-250]`。
   - `artifact.schema.json` 的 `artifact_id`、`kind`、`body`、`claims`、`evidence_refs`、`refs_integrity`、`record_locator`、`state`、`revision`、`written_by`、`produced_by` 均不在 §6 的 Artifact 清单 `[05:251-253]`。其中 **`state` 与 `lifecycle-record.lifecycle_state` 是同一枚 6 值枚举的两个存储位**（历史构建时点比对：两者枚举逐字相同）⇒ 与红线 1 / 红线 2 的「Lifecycle Status 独立成表」存在张力；`05` §6 只把 `lifecycle_state` 归给 Lifecycle Status 表。`kind`/`body` 属 §1 实体定义隐含但未列入 §6 的正文字段。
   - `evidence.schema.json` 的封装列 `schema_version`、`evidence_id`、`source_class`、`locator`、`cohort`、`content`、`produced_by`、`record_type`（8 个）不在 §6 的 Evidence 清单；`source_class` 枚举 = `[external_event, human_input, compiler_artifact, model_output, restated_knowledge]`（5），该词表**在 `05` 全文不存在**。
   - `evidence.schema.json` 的 `scope` 与 `refs_integrity` **不在 `required` 内**（是 properties）⇒ §5.3 S1「scope 缺失即拒绝入库」在 Evidence 层不是 schema 强制，而是靠 `kd_provenance_stamp` 的 `AmbiguousOrigin` 拒盖戳 + 写入网关；`learning` / `pattern` 两侧则把 `scope` 放进 required。
   - `learning.schema.json` 与 §6 的「Evidence 的全部 provenance 列」不完全等价：schema 给了 `origin, evidence_refs, evidence, generation, record_locator, refs_integrity`（6 列）**加** `scope, content_hash, identity, pattern_ref, decay_type, last_validated_at, validation_state`，但**不含** SC06 的 `actor`、`verification`、`lifecycle_event`、`derived_from` ⇒ 完整 11 字段形状只在 `provenance-record.schema.json` 里（R05 核算）。
7. **`verdict.schema.json`（SC12）不在五实体内**（属 `06` §5.1 的终态落点）：`item_verdict` 7 值 `[PROMOTE, HOLD_AT_PATTERN, DROP_SILENT, DROP_WITH_LEDGER, RETIRE_TO_ARCHIVE, PROPOSE_DISPOSITION, REFUSE]`、`terminal_landing` 11 值 + null（含两个 `L-NOTHING` 变体）、`exit_code` `[0,2,3]`。`05` 未定义这些词表，故本文件不为其提供出处，仅登记存在。
8. **§6/§3 的表归属与 SC05 的冲突（数值化）**：§3 声明 **15 列住 Lifecycle Status 表**，§6 只在该表名下写 **4 列**（`lifecycle_state`、`last_activity_at`、`tombstoned_at`、`lifecycle_event[]`），其余 **11 列**在 §6 里被写进 Artifact / Learning / Pattern 名下；而 `lifecycle-record.schema.json` 把 **15 列全部**放在一个记录里、`artifact.schema.json` 又重复其中 8 列（`use_count, view_count, patch_count, opportunity_anchor, layer_request_count, pinned, referenced_by_external, first_seen_at` + `absorbed_into` = 9 个重叠）。⇒ 报告为**归属口径不唯一**，两侧都不由本文件改动。
