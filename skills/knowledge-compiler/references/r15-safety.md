# R15 — 识别风险与防护

排查证据重复计算、错误泛化和未经批准的知识写入等风险时使用。后文保留历史攻击与检查记录，用于定位问题；它们不能单独证明当前版本已经安全。普通工作区还需检查生成的 `AGENTS.md` 等规则文件是否被宿主按目录自动加载；仅在 README 声明它是候选产物，并不能保证隔离，未确认生效范围前不得将其当作已安全暂存。

历史来源： `.distill/round-2/11-FAILURE-MODES.md` §0.1（`:13-41`）、§0.2（`:43-53`）、§0.3（`:55-66`）、§2 判定表（`:80-108`）、§3 判定表（`:112-136`）、§4.1（`:142-149`）、§7 汇总（`:197-213`）、§8（`:216-224`）与 `.distill/round-2/12-SKILL-DESIGN-BRIEF.md` §12 的 DC-SP-1 三闸门（`:513-524`）；Round 3 证据取自 `.distill/round-3/wave-0/mutation-evidence.json`、`.distill/round-3/wave-1/run_wave1_spine.py` 与 `tests/knowledge-compiler/`；生成 2026-10-06，wave 4。
状态说明：本文供参考；具体行为以 `../scripts` 为准。**本文是 Round 2 判定的转录与历史构建时点证据指针，不重判任何 verdict。**

---

## 阅读导航

- 0. 本文为什么存在
- 1. 头号风险：三条既有缺陷相乘（11 §0.1）
- 2. 为什么现成防线挡不住（11 §0.2 表，逐行转录）
- 3. 四条方案（11 §0.3）与 DC-SP-1 三闸门
- 4. Round 2 判定计数（照录，不重判）
- 5. §4.1「攻不动」7 条（不得删）
- 6. 未挡住 / 需第三轮 各行在历史构建时点的实际处置（可见即证据，无证据即空白）
- 7. top3 无防线风险（§6）与「绿色状态下坏」

## 0. 本文为什么存在

`11` 的角色是自陈「唯一主输入 = `_inputs/synth-c-quality.json` → `agent_13_red_team`（20 条 finding + top3 无防线 + 4 条共识攻击）、`agent_15_attacks`（15 条）、`agent_10_control_plane`」（`11:4`）。它的结论**不是全挡住**：§2/§3 显式留下 3 条未挡住的 finding 与 1 条未挡住的攻击。把这些写成「已覆盖」就是 `11:189-190` 记录的失败模式本身（「绿色状态下坏」）。

## 1. 头号风险：三条既有缺陷相乘（11 §0.1）

`11:12` 定性：「**三条既有缺陷相乘，不是新 bug**」，来源 `agent_13_red_team.top3_unguarded[0]` + `RT-05` + `RT-02` + `RT-13`，全部 EVIDENCE-SUPPORTED（`11:13`）。

1. `[1] 02 distill 的自产物过滤器今天就是坏的`（`11:16-23`）：排除匹配已退役的单轮 prompt 字符串 `'You are a skill extraction engine for the \`distill\` tool.'`，生产现发 `'You are a workflow detection engine'` ⇒ 过滤器不再匹配新建的 scan session；Round 1 原话 `has no test to catch the drift`。出处 `worker-caveats[02].doc_vs_impl_gaps`（engine.rs:1411-1426 vs 2152）。
2. `[2] 聚合 / 去重 / 晋升是全局作用域`（`11:25-29`）：`02 SessionDescriptor.project / cohort_key 被计算但**无消费者**`，`cohort_key 只被渲染进 timeline 文本` ⇒ pattern 聚合、去重、晋升计数全部跨项目相加。
3. `[3] 身份 key 只用 .trim()`（`11:31-38`）：同一模式两种拼法永远分两个 key ⇒ 真模式永不晋升（静默漏报）；反向 `jq -s 'add'` 合并全局层 + 项目层且不去重 ⇒ 同一 skill 两处各一份被计成 2 ⇒ 2+ skills 晋升门被单个 skill 满足（误晋升）。

后果原文（`11:41`）：「错误**单调放大而非随机发生**——每轮证据数量真实增长、置信度随之上升，**且不需要任何新 bug**，只要今天已记录的两条不修。」

## 2. 为什么现成防线挡不住（11 §0.2 表，逐行转录）

| 现有防线 | Round 1 元数据 | 为什么挡不住 | 出处 |
|---|---|---|---|
| `CM-09 self-generated-evidence-exclusion` | **2 个项目 / OPTIONAL** | 只覆盖部分（自产物识别本身），且 tier 低到可以被跳过；Round 2 架构把它当可选项 | `11:47` |
| `CM-24 content-addressed-idempotent-upsert` | 5P MUST | **只管同 key 幂等，管不了 key 永不碰撞** | `11:48` |
| `CM-54 typed-scope-partition` | MUST | Round 1 记录的是作用域**被建模**，不是**被消费**（`cohort_key` 无消费者正好是反证） | `11:49` |
| `CM-25 deterministic-identity-key` | 6P | 其 `simplest_impl` 是 `02:cohort-scoped-session-identity`，**form 记录为 anti-pattern**（ATT-06 实测） | `11:50` |
| `CM-36 recurrence-count-promotion-threshold` | 4P | `min total 3` 建立在两个坏前提（全局计数 + 无规范化 key）之上 | `11:51` |

结句（`11:53`）：三者**没有一个能产生「我扫到了自己的输出」这个信号**。

## 3. 四条方案（11 §0.3）与 DC-SP-1 三闸门

四条原文要点（第 1 条全文已转录在 R04 §5，此处给形状）：
1. 自产物识别不用内容字符串匹配，改用**写入时不可伪造标记** + 读侧按标记过滤；需 CORE 而非 OPTIONAL；「删掉排除逻辑必须变红」（`11:57`）。
2. 晋升计数只能来自去重后的唯一生成集合，分桶键 `(scope × pattern_key)`，分母用 **DISTINCT 任务 / 会话数**（`11:59`）。
3. 身份 key 用**规范化后的内容寻址**（NFKC + 大小写/空白/标点归一 + 确定性 slug），**而非只有 trim**，并附**规范化测试向量集**；禁止 N 份计数实现（`11:61`）。
4. occurrences 由确定性代码持有，LLM 计数字段只作参考（`11:63`）。

DC-SP-1 三闸门（`12:517-523` 转录，owner 与实现一一对应）：
- 闸 1 排除谓词自身可验证 — owner `CM-09`（stage=evidence-intake, tier=OPTIONAL, unaided=True）— 实现 S03（`12:517-519`）
- 闸 2 作用域谓词有消费者 — owner `CM-54`（MUST）— 实现 S04；「全局作用域字段（cohort_key）若无消费者即须删除，不允许算了不用」（`12:520-521`）
- 闸 3 身份键多字段归一化 — owner `CM-25`（SHOULD, unaided=True）— 实现 S05；「键至少含 归一化模式身份 + scope + 来源 worker，禁止单字段 strip/trim 作身份」（`12:522-523`）
- 配套两条：可见性（CM-01，S01/S03 退出码 10/2，`12:524`）与独立对账（CM-47，S14/S16，`12:525`）
- DC-SP-1 的 basis 自标 **ENGINEERING-INFERENCE**，「现有 67 簇中无一条同时覆盖三腿，本文不假装已解决」（`12:513-515`）；`round3_handoff` 第 4 条明文「**本轮只登记约束，不声称已解决**」（`12:531`）。

## 4. Round 2 判定计数（照录，不重判）

**§2 Agent 13 的 20 条 finding**（`11:108`，同 §7 表 `11:201-204`）：
- 已挡住 **9**：RT-01、RT-04、RT-06、RT-07、RT-09、RT-10、RT-11、RT-12、RT-18
- 未挡住 **3**：RT-02、RT-05、RT-13（= §0.1 三因子的三个方向，`11:203`）
- 需第三轮 **8**：RT-03、RT-08、RT-14、RT-15、RT-16、RT-17、RT-19、RT-20
- 合计 **20**；severity 分布 CRITICAL 13 / HIGH 6 / MEDIUM 1（`11:82`）；全部 `basis = EVIDENCE-SUPPORTED`，仅 RT-16 内含一条明示 `INFERENCE`（`11:83`）

**§3 Agent 15 的 15 条攻击**（`11:135`，同 §7 表 `11:206-208`）：
- 已挡住 **4**：ATT-05（判据层）、ATT-08、ATT-11、ATT-13
- 未挡住 **1**：ATT-06
- 需第三轮 **10**：ATT-01、ATT-02、ATT-03、ATT-04、ATT-07、ATT-09、ATT-10、ATT-12、ATT-14、ATT-15
- 合计 **15**；强度分布 STRONG 7 / MODERATE 7 / WEAK 1 / FAILED 0（`11:114`）
- 括号保留：「ATT-05 的规范化 key 子项另计入 §0 的未挡住族，不重复统计」（`11:136`）；ATT-05 本身是「**已挡住**（判据层）」而规范化部分「⇒ **未挡住**」（`11:123`）

**其它计数**：「攻不动」保留 **7**（`11:144`/`11:209`）；Round 1 元数据缺陷登记 **9**（`11:210`，M-2 转述未回读、M-9 为「磁盘无证据」的反向登记）；无根 LICENSE 项目 = **4**（`11:211`，旧计数 5 **作废**）；本文 DEFERRED = **5**（`11:212`）。

## 5. §4.1「攻不动」7 条（不得删）

`11:144` 原文：`CM-47`、`CM-65`、`CM-32`、`CM-25`、`CM-31`、`CM-08`、`CM-49`。
必须随行的两条限定（原文，`11:145`、`11:149`）：
- 来源限定：「该清单由任务书转述 Agent 15 记录；`agent_15_attacks` 的 15 条原文中未逐条以「攻不动」标签出现 ⇒ **第三轮合流时按原文复核**」（另见 `11:221` D11-4）。
- `CM-65` 的「攻不动」仅限其 **kernel**（证据字段必须可再验证）；其 enforcement 侧被 ATT-13 攻击，`CM-47`/RT-17 记其指针会断——「两者并存，不是矛盾」。

## 6. 未挡住 / 需第三轮 各行在历史构建时点的实际处置（可见即证据，无证据即空白）

### 6.1 三条「未挡住」——Wave 0–3 做了什么

| Round 2 verdict | 缺口 | 历史构建时点处置 | 证据指针（可回查） |
|---|---|---|---|
| **RT-05 未挡住**（`11:91`：第三轮需「写入时不可伪造标记 + 读侧按标记过滤 + 对抗测试」） | 自产物过滤器写过且无测试捕获漂移 | 内核改为**多信号 + 默认拒绝**（非内容字符串匹配），S03 做读侧路径/哈希过滤并 fail-closed，S19 夹具真跑，Wave 0 做变异证明 | `../scripts/kd_provenance.py:95-123`；`../scripts/kd_selfsource_filter.py:90-119`；`tests/knowledge-compiler/test_s19_self_reference.py::test_s19_self_generated_never_counts`；`.distill/round-3/wave-0/mutation-evidence.json`（`guard_switch=SELF_GENERATED_EXCLUSION_ENABLED`、`cycle=GREEN -> RED -> GREEN`、`mutation_red=true`、`test_bites=true`、`verdict=PASS`、`kernel_sha256=d7d4add8…c6e8`、`kernel_hash_restored=true`） |
| **RT-02 未挡住**（`11:88`：分桶计数属 DD-1/DD-2） | `cohort_key` 算了无消费者 ⇒ 跨项目相加 | S04 把「消费者」做成可执行断言：无消费者即退出码 2；计数语义改为 DISTINCT cohort × DISTINCT content_hash，且自产物永不入分母 | `../scripts/kd_scope_resolve.py`（契约见 `12:112`「2=scope 字段算了无消费者」）；`../scripts/kd_dedup_exact.py:75`、`:166-185`；`tests/knowledge-compiler/test_w1a_scope.py::test_s04_exit2_when_scope_is_computed_but_has_no_consumer`、`::test_s04_never_defaults_a_missing_scope_to_global`、`::test_s04_does_not_rederive_cohort_identity`；`tests/knowledge-compiler/test_w1b_identity.py::test_support_counts_distinct_cohorts_times_distinct_content_hash`、`::test_self_generated_evidence_never_becomes_support`；`.distill/round-3/wave-1/run_wave1_spine.py`（docstring：「checks S04's scope-consumer verdict both ways: exit 2 with a named pending consumer is the Wave 1 branch, exit 0 requires `scope.layer` to be read by the real promotion tree」） |
| **RT-13 未挡住**（`11:99`：规范化 + 去重后计数两条污染都无代码级防线） | trim-only 身份 + 不去重的相加 | S05 把 trim-only 做成**机械不可能**（守卫 + 退出码 2），S06 继承同一守卫而非另建 | `../scripts/kd_identity_key.py:64`、`:314-316`（`TRIM_ONLY_IDENTITY`）、`:324-325`（`TRIM_ONLY_PIPELINE`）、`:386-391`；`../scripts/kd_dedup_exact.py:62`、`:208`；`tests/knowledge-compiler/test_w1b_identity.py::test_trim_only_spec_is_rejected_by_the_predicate`、`::test_s05_cli_exits_2_on_trim_only_candidate`、`::test_normalisation_vectors_all_pass`、`::test_cjk_identity_stays_distinct`、`::test_bookkeeping_fields_never_change_the_identity`、`::test_dropping_an_axis_cannot_disable_the_sensitivity_probe` |
| **ATT-06 未挡住**（`11:124`：规范化 + 唯一定义算法本轮无门；簇合并交 16a） | 派生算法未定义处机制即虚构 | 同上 S05 路径；**簇合并（CM-24/CM-25）不属历史构建时点权限**，仍交 16a 记录 | 同 RT-13 行的指针；簇侧登记见 `11:179` M-8、`02-FINAL-MECHANISMS.md:533` |

诚实边界（这三条不等于「已闭合」）：
- `11:218` **D11-1 仍未闭合**：它要的是「任一项目的『会话来源记录 / harness 事件 id』写入 + 读侧过滤实现」——即**参考项目形态**；历史构建时点的实现是本仓库自有机制，不能替代「Round 2 缺的是外部范例」这一登记项。本文不把它标为已解决。
- `11:219` **D11-2 仍未闭合**：本文 §6.1 的规范化算子有测试向量集（`test_normalisation_vectors_all_pass`），但 D11-2 的关闭条件是「≥1 个项目的 NFKC/slug 规范化实现 + 规范化测试向量集」，前半项（**外部项目**实现）历史构建时点不产生。
- DC-SP-1 的 tier 重裁（`CM-09` OPTIONAL → ？）与 Round 1 元数据登记（`11:166-181` 九条 M-*）**未回改**，历史构建时点亦不回改。

### 6.2 「已挡住」判据所依赖的门，历史构建时点是否有实现（只列可指认的）

`11:154` 的要求：「本文所有『已挡住』判定都必须能落到 `F*/E*/R-*` 之一」。可指认的实现：E1 写盘前门 → `../scripts/kd_validate.py`、`../scripts/kd_write_txn.py`、`tests/knowledge-compiler/test_w1c_write_txn.py`、`test_w1b_store_validate.py`；E2 渲染/加载预算门 → `../scripts/kd_budget.py`（`--check-write` 硬拒 = 退出码 2；见其 `--help`）、`tests/knowledge-compiler/test_w3d_budget.py`；E3 缩减/淘汰扫描 → `../scripts/kd_lifecycle.py` + `tests/knowledge-compiler/test_w3b_lifecycle.py`；E4 脱敏/信任边界 → `kd_ingest.py` 的 scrub 阶段 + `tests/knowledge-compiler/test_w1a_ingest.py`；F3 惰性候选隔离 → `../scripts/kd_quarantine.py` + `tests/knowledge-compiler/test_w2c_quarantine.py`。

### 6.3 历史构建时点**未**闭合的「需第三轮」项（登记，勿称覆盖）

`11` 判为需第三轮的 8 条 finding + 10 条攻击，本切片只核到与本文直接相关的两条防线：
- RT-03 / ATT-10（`11:89`、`11:128`）：「run ledger 落盘为门的前置条件**未实现**」——历史构建时点的账本落点为 `../scripts/kd_write_txn.py` 与 `../schemas/lifecycle-event-ledger.schema.json`；本文**未验证**「未落账即拒绝晋升」这条链是否真咬，故不声称 RT-03 已闭合。
- RT-17 guard ②（`11:103`）：「`provenance schema` 与 `provenance verifier` **拆两簇分别 disposition**，有 schema 无 verifier 不得记 VERIFIED」——历史构建时点两者皆在（`../scripts/kd_provenance_stamp.py`、`../scripts/kd_refs_audit.py`、`tests/knowledge-compiler/test_w1c_provenance_refs.py`），但 **CM-47/CM-65 的簇级 disposition 不在历史构建时点权限内**，本条按「防线件已到位、簇判定仍未回裁」登记。
- 其余 RT-08、RT-14、RT-15、RT-16、RT-19、RT-20 与 ATT-01/02/03/04/07/09/12/14/15：本切片**未找到**对应的 Round 3 证据可指认，一律保持 Round 2 的「需第三轮」原判定，不改判、不粉饰。

## 7. top3 无防线风险（§6）与「绿色状态下坏」

`11:189-190` 转录：67 簇里没有任何一簇负责「宣称阈值 ↔ 运行时生效阈值 ↔ 实际拒绝行为」三者一致性；`CM-63 doc-claim-without-mechanism` 恰是这条防线而其 disposition 是 **REJECT** ⇒「**一条真实失败模式被当成非机制剔除了**」；历史构建时点处置 = `09` §3 定为**核心约束** + `08` P-01..P-08 硬禁令 ⇒「判据层已挡住」，`CM-63` 的 REJECT「需第三轮重读（不因本文断言簇归属，只指出『REJECT 该簇 ≠ 放弃该检查』）」。后果原文：「**系统在绿色状态下坏**——测试绿、报告写 Implemented、门在配置里存在、阈值写在 README，而实际拒绝发生在另一个数上或根本没发生」。
`11:192`（top3 第 3 条）原文：链上每段 Round 1 都实测断裂 ⇒「**格式合法的幻觉可穿过全部三道关**」；「事后无法区分哪些来自真实代码、哪些来自 agent 的一次自信陈述，因为它们在同一个 schema 里长得一模一样」。

## 待确认与暂缓事项
- `DEFERRED id D11-1`…`D11-5`（`11:218-224`）全 5 条保持未闭合，逐条原文即本文转录内容；小计 **5**（`11:224`）。
- `DEFERRED id D11-3`（`11:220`）：`known_failure_modes` 与 `default_config_reachable` **不在 SPEC §4 disposition 字段清单内**，「本文只能提出追加要求，不能替用户决定字段」——历史构建时点未扩列，本条仍开放。
- `DEFERRED id D11-4`（`11:221`）：「攻不动」7 条与「通胀质疑 9 条」**未在本唯一主输入中逐字复现**；本文件按 `11:144`/`11:168-181` 转录，M-2 仍标「转述，需复核」（`11:173`）。
- `DEFERRED id D11-5`（`11:222`）：许可门归属未定；`worker-11` 许可类型 **UNKNOWN**（`11:161`）。
- 52 条未定参数收录于 `.distill/round-3/DEFERRED-PARAMETERS.yaml`（其头注「头号未闭合风险（非参数、属未证防线）：RT-02 / RT-05 / RT-13 … residual_gap_declared=true；承载簇 CM-09 仅 2 项目 + OPTIONAL」），本文**不关闭其中任何一条**。

## 历史源码对照
- **§6.1 的三行是本文件唯一依赖运行证据的部分。** 引用的 `mutation-evidence.json` 字段实际读自磁盘（`fixture=self-reference-contamination`、`baseline_green=true`、`mutation_red=true`、`restored_green=true`、`kernel_hash_restored=true`、`test_bites=true`、`verdict=PASS`、`steps` 长度 **3**：`1_baseline` / `3_after_removing_protection` / `4_restored`）。**注意：`steps` 里没有名为 `2_mutation` 的步**，编号跳号，`cycle` 字段仍写 `GREEN -> RED -> GREEN` 三段 —— 数字层面存在「步序标签与 cycle 段数不一致」，本文只报数不修。
- `mutation_failure_assertion`（同文件）实际抛出的泄漏 cohort 共 **8** 个（`ws-alpha` 5 + `ws-beta` 2 + `ws-gamma` 1）——与「删掉排除逻辑必须变红」（`11:57`）方向一致，且证明红的是**断言**而非崩溃。
- `11:57` 要求「写入时不可伪造标记」：代码侧对应 `kd_provenance.is_self_generated` 的 `produced_by.kind`（`:109-111`，注释「signal 2: produced by this distiller version」）。**但 Round 2 判定的原形态是「写入时一次盖戳、不可覆盖」（`CM-66 10:write-time-origin-channel`，`11:58`）**；历史构建时点「盖戳唯一写者」的落点是 `kd_provenance_stamp.py` 与 `12` 的 SC06 行。本文核到的是**契约存在**（脚本 + schema），未核「不可覆盖」是否被测试锁定 —— 不写成已覆盖。
- 计数一致性：`11:108` 与 `11:201-204`、`11:135` 与 `11:206-208` 两处（§2/§3 末行 与 §7 汇总表）**数字完全相同**（9/3/8 与 4/1/10），本文两处均按同一组数转录，无内部矛盾。
- 「规范化测试向量集」在 Round 2 施工图里的落点是 `12-SKILL-DESIGN-BRIEF.md:727`（§16 自检清单**第 10 行**）。`../scripts/kd_identity_key.py:15` 把同一要求引作「`12-SKILL-DESIGN-BRIEF.md:725 item 10`」，而 `:725` 实际是清单第 **8** 行（自引用三闸夹具）。**行号相差 2，条目号一致** —— 本文按 `:727` 转录，并登记该脚本注释的行号偏差，不改脚本。
- `11:154` 的可落点要求：历史构建时点可落到 E1/E2/E3/E4/F3 的核对见 §6.2，均为**文件存在性 + 测试函数名**级别；本文**未运行任何测试**（权限 static），因此 §6.2 不构成「运行已验证」。
