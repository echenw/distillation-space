# R04 — 采集与核对证据

需要把观察结果整理成正式证据时使用。记录实际事件，先脱敏再截取，并把采集失败与正常空结果分开。普通笔记无需直接转换成正式证据；当前采集接口见 §9–10。

历史来源： `.distill/round-2/04-DETERMINISTIC-VS-LLM.md` 行 1（`:47`）与行 17（`:63`）、`.distill/round-2/11-FAILURE-MODES.md` §0.3 第 1 条（`:57`）与第 4 条（`:63`）、`.distill/round-2/02-FINAL-MECHANISMS.md` 的 CM-01/04/08/09/49 条目；生成 2026-10-06，wave 4。
状态说明：本文供参考；具体行为以 `../scripts` 为准（本文只转录 Round 2 已裁定的契约，不新增判定）。

---

## 阅读导航

- 1. 采集成败必须可见（CM-01）
- 2. 逐行 parse 与事件允许清单（04 行 1）
- 3. scrub 早于 truncate 的顺序契约（04 行 1 + 行 17）
- 4. 类型化边界：唯一的 ingress（04 行 17）
- 5. 自产证据排除：机制形态（11 §0.3 第 1 条）
- 6. occurrences 由确定性代码持有（11 §0.3 第 4 条）
- 7. 本契约涉及的其它 CORE 簇（本文只登记事实，不重裁）
- 8. SUPPORTING / reference 实现位置（不得当门机制）
- 9. S01 / S03 的契约落点（脚本为准，本文不重述行为）
- 10. 当前 S01 的清单绑定快照（本轮实现补记）

## 1. 采集成败必须可见（CM-01）

- 契约：`04:63` 行 17 的 Deterministic 列点名「硬编码模式 + 长度锚定 + **spool 不丢** + 自产证据排除」，采集侧失败不得与「正常空结果」同态。
- 出处（可见性归属）：`12-SKILL-DESIGN-BRIEF.md:524`「可见性　过滤失效必须是可见失败　owner: CM-01 capture-failure-visible-marker（MUST）　实现: S01/S03 的退出码 10/2」。
- 簇事实（`02-FINAL-MECHANISMS.md:494`）：CM-01 cp=3 / members=5 / worker 06,09,11 / disposition CORE。

## 2. 逐行 parse 与事件允许清单（04 行 1）

`04:47` 原文（行 1 Evidence parsing，Deterministic 列 = **唯一**）：

> `JSONL 逐行 parse + 事件允许清单 + normalize_excerpt + **scrub 早于 truncate 的顺序契约**`

Small LLM / Judge / Human 三列在 `04:47` 均为「无」——该行的唯一性不允许把解析交给模型。
一致确认（不裁决）名单包含 `#1 Evidence parsing`：`04:73`。
管线对应步骤：`04:96`「2 逐行 parse + 事件允许清单　det」、`04:97`「3 scrub 早于 truncate + 类型门　det」。

## 3. scrub 早于 truncate 的顺序契约（04 行 1 + 行 17）

- 两行同时写明顺序：`04:47`（「scrub 早于 truncate 的顺序契约」）与 `04:63`（「类型化边界 `Sanitized<T>` 唯一构造函数（无其他 ingress）+ scrub 早于 truncate + …」）。
- 该契约在 Round 1 的正面范例（`04:142-143`）：「顺序契约 scrub 早于 truncate（`assistant_capture.rs:137-138` + 测试 `:342 client_transform_scrubs_before_truncating`）」——契约与锁定它的测试名一并转录。
- 语义后果（`04:63` 的「无其他 ingress」）：先截后脱敏可把被截掉的边界外的敏感片段变成「看不见」而非「已替换」；`04:142` 同时把该顺序列为「类型层强制」的一部分。

## 4. 类型化边界：唯一的 ingress（04 行 17）

`04:63` 行 17（Capture / ingress gating，附加行）的 Deterministic 列逐字为：

> `类型化边界 Sanitized<T> 唯一构造函数（无其他 ingress）+ scrub 早于 truncate + 硬编码模式 + 长度锚定 + spool 不丢 + 自产证据排除`

Small LLM 列只有一个合法剩余位置（`04:63`）：「◐ 仅残余歧义（某段文本是否敏感）」；Judge / Human 为「无」。
正面范例转录（`04:141-142`）：「`Sanitized<NewObservation>` 无 `sanitize()` 之外的构造路径（`payload.rs:1062, router.rs:465/3064`）」。
同一条在 `15` ai-memory 被列为跨切面不变量 #6（`11:148` 引 `15` invariant #6「`Sanitized<NewObservation>` 无其它构造器」）。

## 5. 自产证据排除：机制形态（11 §0.3 第 1 条）

`11:57` 原文（逐字，不软化）：

> **自产物识别不用内容字符串匹配**，改用**写入时不可伪造标记**（会话来源记录 / harness 事件 id）+ **读侧按标记过滤**。该机制需 **CORE 而非 OPTIONAL**（CM-09 的 tier 需在第三轮重裁）。对抗性测试锁定：`注入一条自产物 → 必须被排除`，删掉排除逻辑必须变红。

- 证据标注（`11:58`）：`RT-05 required_guard`；正面范例 `CM-66 10:write-time-origin-channel`（`agentmemory/src/types.ts:37-52`，写时一次盖戳、`importOrigin` 已有就原样返回绝不覆盖）。
- 为什么不能用内容字符串匹配（`11:18-21`）：匹配已退役的单轮 prompt 字符串 `'You are a skill extraction engine for the `distill` tool.'`，生产现发 `'You are a workflow detection engine'`，Round 1 原话 `has no test to catch the drift`。
- 现成防线挡不住的部分（`11:47`）：`CM-09 self-generated-evidence-exclusion` = **2 个项目 / OPTIONAL**，「只覆盖部分（自产物识别本身），且 tier 低到可以被跳过」。
- DC-SP-1 闸 1 的实现要求（`12:517-519`）：「按解析后绝对路径 + 内容哈希匹配；每条被采纳证据都要断言其来源不在排除集内；谓词失效或不可判定 ⇒ fail-closed 为「本轮无证据」，不得静默继续。」owner 标为 CM-09，实现 = S03。
- 簇事实（`02-FINAL-MECHANISMS.md:497`）：CM-09 cp=2 / members=2 / worker 02,09 / **needs_llm=False** / CORE。
- tier 缺陷登记（不修正）：`12:763-765` 待核第 3 条——「`CM-09` tier 需第三轮重裁（`11` §0.3 第 1 条）；…… CORE 判定不依 tier，但 tier 记录须如实修正」。

## 6. occurrences 由确定性代码持有（11 §0.3 第 4 条）

`11:63` 原文：

> **occurrences 由确定性代码持有**（append-only 事件计数），**LLM 输出的计数字段只作参考**。

- 证据标注与反例（`11:64`）：`RT-02 required_guard`；反例「`09 skills.py#_parse_distill_response` 不做 `occurrences` 数值过滤（`min_occurrences` 只在 prompt），LLM 返回 `occurrences:1` 照样入 store，且 `occurrences = max(old, new)` 不累加 ⇒ 该加的不加、该拦的不拦」。
- 与之配套的合流方案（`11:59-60` §0.3 第 2 条，属 R15 的判定范围，此处只标接口）：计数分母用 **DISTINCT 任务 / 会话数**，不用行数；分桶键为 `(scope × pattern_key)`。

## 7. 本契约涉及的其它 CORE 簇（本文只登记事实，不重裁）

| 簇 | stage / Round1 tier / disposition | cp / members / worker | 出处 |
|---|---|---|---|
| CM-04 evidence-inventory-and-ingest | evidence-intake / MUST / CORE | 4 / 7 / 05,07,09,12 | `02:51`（stage 行）、`02:495`（计数行） |
| CM-08 secret-redaction-before-retention | evidence-intake / MUST / CORE | 5 / 6 / 04,06,07,10,15 | `02:62`（stage 行）、`02:496` |
| CM-49 untrusted-instruction-boundary | validation / MUST / CORE | 4 / 6 / 04,09,12,14 | `02:290`（stage 行）、`02:513` |
| CM-42 code-enumerates-llm-decides-split | validation / SHOULD / CORE | 4 / 4 / 05,09,10,11 | `02:187`（stage 行）、`02:510` |

- CM-08 与 CM-49 属 `11:144` 「攻不动」7 条之列，且 `11:148` 记录二者「同时出现在 `agent_10_control_plane.E4 脱敏/信任边界` 的 `source_evidence`」（`06:dual-egress-rule-redaction`；`15` invariant #6；`04:transcript-untrusted-instructions-fence`；`15 AGENTS` 不可信散文）。
- CM-04 的成员级 carve-out（不得把死字段当承重证据）：`02:445`「CM-04 保 CORE 但加成员级 carve-out：死字段成员不得作承重证据；不改 Round 1 成员归属。」
- CM-49 的入库侧含义：进入 store 的散文一律按不可信历史数据处理，`12:552` 行「排除/作用域/身份谓词不可判定　fail-closed ⇒ 本轮无证据（退出码 2），禁止静默继续　DC-SP-1」。

## 8. SUPPORTING / reference 实现位置（不得当门机制）

本文按 `.distill/round-4/_dispatch/w4c.json:5` 的指派，只把下列三条列为**参考实现位置**，不列为契约：

- `CM-03` durable-capture-ingress-failsafe、`CM-12` fail-closed-field-normalization、`CM-15` stage-gated-workflow-contracts —— 均为 SUPPORTING / reference：「`CM-01` 是 `CM-03` 的校验者（`synth_d.CORE_clusters.CM-01.reason`：饱和静默丢弃仍可满足 CM-03）；故 CM-03 只作参考形态，硬拒由 CM-01 + S18 承担」`_dispatch/w4c.json:280`。
- `CM-10` bounded-evidence-windowing —— 作 reference：「触发可用 S02 的有界轮询替代（`CM-10` bounded-evidence-windowing 同理作 reference）」`_dispatch/w4c.json:194`。

## 9. S01 / S03 的契约落点（脚本为准，本文不重述行为）

- S01 `kd_ingest`：契约列在 `_dispatch/w4c.json:93`（scripts_present 表），管线步 1–8（`04:95-100`）。
- S03 `kd_selfsource_filter`：`12:111` 原文——inputs `evidence.jsonl` + 排除集（解析后绝对路径 + 内容哈希）；outputs `evidence.filtered.jsonl`、`excluded_report.json`；exit「**2=排除谓词不可判定，禁止静默继续**；0=无自产物」；cluster「CM-09（DC-SP-1 闸 1）」；位置「步 3 与 8 之间 / 行 17」。
- S02 `kd_inventory` 的有界输入集属 CM-04，退出码语义以脚本为准。

## 待确认与暂缓事项
- `DEFERRED id D11-1`（`11:218`）：**自产物不可伪造标记的写入机制**无参考项目实现（`CM-09` 2P/OPTIONAL，且 02 今天是靠内容字符串匹配）。需补：任一项目的「会话来源记录 / harness 事件 id」写入 + 读侧过滤实现，及「注入自产物必须被排除」的对抗测试形态。本文不关闭它。
- `DEFERRED id D11-2`（`11:219`）：身份 key 的规范化派生算法未定 —— 属 R07 / DD-2 范围，本文件不代答。
- `DEFERRED id DD-1-sub01 … DD-5-*`：入库侧涉及的全部未定参数收录在 `.distill/round-3/DEFERRED-PARAMETERS.yaml`（52 条），本文**一条都不关闭**；规则见该文件头「关闭任一条目必须提供 evidence_needed_to_close 要求的证据，并回填至本文件」。
- `UNKNOWN`：`worker-11`（agent-memory）的 `license_notes` 在第一轮为空数组，其许可类型 **UNKNOWN**（`04:212`、`11:161`）。§4/§5 引用的正面范例分布于该项目与 `02` distill（**无根 LICENSE 文件**，`11:162`），复用形态时须带此标注。
- Round 2 未定且本文件不得替其拍板：`CM-09` 的 tier 重裁（`12:765` 待核第 3 条）。

## 历史源码对照
- `../scripts/kd_ingest.py:133-155` `scrub_then_truncate()`：脱敏循环（`:137-139`）在字节预算截断（`:141-154`）**之前**执行，二者在同一函数体内，无「先截后脱敏」的第二条代码路径 —— **与 §3 一致**。
- `../scripts/kd_ingest.py:13`、`:134`：脚本 docstring 自陈顺序契约并回指「04 row 1 line 47 / row 17 line 63」，与本文引用的行号相同 —— **一致**。
- `../scripts/kd_ingest.py:111-121` `normalize_excerpt()`：注释记「Applied BEFORE hashing and BEFORE scrub/truncate」，即 normalize → scrub → truncate 三级次序；`04:47` 只列出 `normalize_excerpt` 与顺序契约两项，未规定 normalize 与 hash 的先后 —— **代码比文档更具体，无冲突**。
- `../scripts/kd_provenance.py:95-123` `is_self_generated()`：docstring 自称「Three independent signals, any one is sufficient」（`:99`），实际分支为 **4 条排除分支 + 1 条 fail-closed 兜底**：`source_class ∈ DERIVED_CLASSES`（`:106`）、`produced_by.kind ∈ {distiller, model}`（`:111`）、locator 落在 store 内（`:117`）、`record_type ∈ ARTIFACT_RECORD_TYPES`（`:120`），最后 `return cls not in INDEPENDENT_CLASSES`（`:123`）。**数字不一致：注释说 3，代码有 4+1。** 本文按当时代码实况转录为「多项独立排除条件（任一命中即排除）+ 默认拒绝」，当时未修改代码。
- `../scripts/kd_selfsource_filter.py:15-20`：该脚本自陈**不是第二个过滤器**——「`kd_provenance.is_self_generated` stays the single authority for *what counts as self-generated*; this script contributes only the ingestion-side mechanics … plus the report and the fail-closed exit」，与 §5「一个业务语义只有一个 Owner」一致 —— **一致**。
- `../scripts/kd_selfsource_filter.py:90-119` `evaluate()`：先问内核（`:98-99`），内核未排除才查路径/哈希集合（`:107-117`）；locator 缺失/空白或哈希不可得 ⇒ `"undecidable"`（`:102-104`、`:111-113`），内核抛错亦 fail-closed（`:100-101`）—— **与 `12:111` 的「2=排除谓词不可判定」一致**。
- `../scripts/kd_ingest.py:49-51`：`EXIT_OK=0 / EXIT_PARTIAL_DROP=10 / EXIT_CAPTURE_FAILED=2`，与 §1 引用的 S01/S03 退出码 10/2 相符 —— **一致**。
- 未核对（超出本文件范围）：S04 的 scope 消费者断言（属 R15 / DC-SP-1 闸 2），S05 的身份键守卫（属 R07）。

## 10. 当前 S01 的清单绑定快照（本轮实现补记）

本节记录当前实现，不改写上文引用的冻结政策。S01 `load_raw_lines` 对单个来源只读取一次原始字节，用同一份字节核对 S02 清单中的长度及 SHA-256，再从该快照解析 JSONL。禁止先校验一次文件、再重新打开它解析；两次读取之间的替换不能成为旧清单下的新材料。

实际读取失败、字节长度或摘要不匹配仍沿 `CaptureFailure` 返回退出码 2 和可见的无证据标记；坏 JSON 行仍按既有逐行丢弃协议报告，CRLF、CR、LF 保留文本流的行号语义。每次只缓存一个来源文件，未新增磁盘副本、第二写入 Owner 或格式字段。

这里的“清单匹配”只证明解析内容与观察清单绑定，不认证来源身份、语义正确性或运行结果。采集产物仍是 `UNVERIFIED`；S03 排除、Scope、独立 Eval、G1 和 S12 正式写入条件不变，也不声称对正在恶意修改的整个目录提供文件系统快照隔离。

研发回归：`tests/knowledge-compiler/test_w1a_ingest.py` 中 `test_s01_parses_the_same_bytes_that_passed_inventory_verification`、`test_s01_snapshot_read_error_is_visible_capture_failure`、`test_s01_snapshot_preserves_universal_newlines_and_partial_drop`。这些测试位于开发仓而不是安装包的运行依赖；执行结果和前后差异由本次逐仓对标报告保存，不在 Reference 中复制发布状态。
