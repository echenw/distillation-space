# R05 — 记录来源与可信程度

核对每条结论来自哪里、适用于哪个版本，以及证据能证明什么。AI 自述、自动检查和人工批准各有不同作用；出处由负责记录的工具保存，当前保存与读取方式见文末。

历史来源： `.distill/round-2/05-DATA-MODEL.md` §2（行 26–52，含七问表 30–38）与 §2.1（行 54–72）、`10-PROVENANCE-MODEL.md` §1 总表（行 15–27）与 §1.1–1.6（行 29–84）、§2.2–2.3（行 106–115）、§3（行 119–128）、§10 DEFERRED（行 235–244）。生成于 2026-10-06，wave 4。
状态说明：末节说明当前出处接口；前文保留设计依据与历史观察，不把旧缺口当成当前事实。本文供参考；具体行为以 `../scripts/`（`kd_provenance_stamp.py`、`kd_refs_audit.py`、`kd_write_txn.py`）与 `../schemas/provenance-record.schema.json` 为准。
引用约定：`[05:N]` = `05-DATA-MODEL.md` 第 N 行；`[10:N]` = `10-PROVENANCE-MODEL.md` 第 N 行。行号保留原整理时点的定位。

---

## 阅读导航

- 1. 七问与现状 `[05:28-38]`
- 2. 11 条 provenance 字段（`05` §2 表逐行转写）`[05:40-52]`
- 3. provenance 参与决策的 5 条分支 `[05:54-70]`
- 4. 信任强度按**断言类别**分派（L1–L5 + 自报口）`[10:15-27]`
- 5. 承载者规则：出处记录**不得**放在被记录对象自己手里 `[10:119-128]`
- 待确认与暂缓事项
- 历史源码对照

## 1. 七问与现状 `[05:28-38]`

| 问 | 内容 | Round 2 记录的现状 | 出处 |
|---|---|---|---|
| Q1 | 这条知识为什么存在？ | **可答**（形状存在，无 schema 强制） | `[05:31]` |
| Q2 | 来自哪些 Evidence？ | **不可答**（出处存在但机器不可解析） | `[05:32]` |
| Q3 | 由哪些 Issue/Session/Fix 支持？ | **不可答**（本轮产物完全没有该字段） | `[05:33]` |
| Q4 | 哪轮提炼产生？ | 全局可答（tag `distill-round-1-baseline` / commit `9bc2a0c`），**逐条不可答** | `[05:34]` |
| Q5 | 哪个 Compiler Version 产生？ | **不可答**（无版本/模型/配置指纹字段） | `[05:35]` |
| Q6 | 哪些 Eval 验证过？ | **不可答**（validation 是自由文本，大量写「本轮未运行」） | `[05:36]` |
| Q7 | 为什么被修改或删除？ | **不可答**（无 append-only 变更账） | `[05:37]``

采纳结论（`10` §4 转述 Agent 12）：现状「严格机器可答仅 **1/7（Q1）**」，采纳 11 字段集后 **7/7 可答** `[10:135-136]`。
**注意 `10` 自己的对账声明**：「`dd_04_fields` 提供的是 DD-4 生命周期 / 归属字段 14 条，**不是** Agent 12 的 11 字段出处集。⇒ 「11 字段」的逐条清单**不在本唯一主输入内**」`[10:139]` — 本文件的逐条清单取自 `05` §2（该文档承担了合流），不是取自 `10`。

---

## 2. 11 条 provenance 字段（`05` §2 表逐行转写）`[05:40-52]`

| # | 字段（表.列） | 答哪一问 | **谁写入** | **何时失效** | **无它则哪问答不了** | 依据要点 | 出处 |
|---|---|---|---|---|---|---|---|
| 1 | `origin.problem` / `origin.why`（两个非空文本） | Q1（并为 Q7 的 reason 基线） | 产生该条的 Worker；**schema validator 拒空** | **不可就地改写**；改写必须以新 `lifecycle_event` 承载，原值留账 | Q1 无法答 | CM-65 `04:evidence-cited-provenance`、`05:skill-backlink-rule-provenance`、`01:rule-provenance-tracker-id` | `[05:42]` |
| 2 | `origin.source_refs[] {kind∈issue\|session\|fix\|dd\|run, id}` | Q1、Q3 | Worker **只填自己实际打开过**的 id；referential-integrity auditor 判可解析性 | 引用对象不存在 → 整条自动降 stale，**并阻断晋升** | Q3 完全无法答（Round 1 现状即如此） | CM-66 `15:git-checkpoint-plus-audit-log-provenance`、CM-65 `01:rule-provenance-tracker-id`、CM-64 `02:decision-history-tag-weighting-injection`；DD-3 悬空引用（`DESIGN-DECISIONS.md:215`）证明有 id 引用而无完整性校验同样不可答 | `[05:43]` |
| 3 | `evidence_refs[] {project, path, symbol, kind, status}`；**path 必须为规范仓库相对路径，禁 brace/通配简写** | Q2 | Worker 填，**resolver 校验，解析失败即拒绝入库** | resolver 失败（路径不存在或注册根缺失）**即刻**失效；不靠事后备注 | Q2 退化为「人肉重开仓库」 | 实测：`round-1/worker-10.json` 的 **132/132 条 path 缺 `repos/` 前缀**、3 条花括号简写、仅 **66/132** 能直接解析（SPEC §7.3）；`09:transcript-anchor-provenance-comment`；CM-47 `02:claimed-inspection-audit-trail-gate` | `[05:44]` |
| 4 | `evidence.status ∈ {VERIFIED, UNVERIFIED, UNKNOWN}` + `status_basis`（指向一次真实运行记录） | Q2、Q6 | **只能由 eval/audit runner 写**，非 Worker 手填；无运行记录时只能是 UNVERIFIED | 对应运行记录消失或 `artifact_sha` 变化 → 自动回落 UNVERIFIED | Q6 无法答，且 07/13 型伪造可行 | CM-63 `07:hand-authored-narrative-pdf-report`（`generate_report.py:406-412` 把未接线门标 Implemented、`:269` 称 DSPy BootstrapFewShot 而代码零出现、`:257` 的 `$2-10 per run` 无代码依据）；正例 `02:labeled-fixture-scan-eval-gate` | `[05:45]` |
| 5 | **`provenance.actor`** ∈ {human, `agent:<name>`, curator, import, shared}；缺省 **fail-closed** | Q3、Q5、Q7，**并决定写入权** | 写入网关/装配层（**不由被记录对象自报**） | 归属变更**只有人类 adopt 路径可改** | Q7 无法归因；自动化写入会按位置或活跃度误推断权限，改掉人类内容 | CM-35 `14:autonomous-write-provenance-optin-gate`（`_write_origin`、`_background_review_write_guard`、`is_curation_eligible/adopt`；adopt 明确拒绝 hub/external/bundled/protected）；`06:self-authored-only-membership-boundary` | `[05:46]` |
| 6 | `generation {round_id, pass_id, compiler_version, model_id, config_sha, created_at}` | Q4、Q5 | 装配层**写盘时盖戳**，**Worker 不可自填** | **不可变**；任何改写产生新条目并由 `lifecycle_event` 链接 | Q4 与 Q5 同时无法逐条答，版本失配无从判 stale | CM-66 `15`（一个 consolidation pass = 一个 git commit）、CM-64 `10:month-sharded-audit-log`、CM-62 `14`。`{provider,model,dim}` mismatch 即忽略的形状来自 `15` 不变量 8 `[E]`；**把该形状外推到 `compiler_version`/`config_sha` 为 `[I]`**（Agent 12 自标：参考项目未提供该直接实现） | `[05:47]` |
| 7 | `verification[] {eval_id, verdict, run_at, run_evidence_hash, artifact_sha}` | Q6 | eval runner **追加**；**正文不得编辑既有 verdict** | `artifact_sha` 与当前产物不符 → 该 verdict 视为过期 | Q6 无法答；MUST 晋升失去证据 | `02:labeled-fixture-scan-eval-gate`（`build_codex_scan_fixture.py` + `check_scan_perf.py`）；CM-47 `04:claim-versus-workspace-antifabrication` | `[05:48]` |
| 8 | `lifecycle_event[]` append-only `{at, op, actor, reason, supersedes \| superseded_by}`；**一次 batch op 只写一行；detail 不作权威** | Q7 | audit writer | 只追加；账本按字节上限清扫时**必须显式告警** | Q7 无法答，且被拒绝/被删的提案会沉默消失 | CM-66 `15`（`detail` 不作为事实来源，代码注释显式声明）、CM-64 `10:month-sharded-audit-log`、CM-62 `14`、`06:run-account-anti-silence`。风险 `[E]`：`14` 的 `ledger_max_bytes=5MiB` 可能删掉审计证据 | `[05:49]` |
| 9 | `derived_from[]`（派生谱系） | Q7、Q1（派生知识为何失效） | 派生计算层 | 上游失效即向下传导 | 派生条目失去失效路径 | `10:supersession-cascade-stale`（该成员 tier=OPTIONAL）。**列本身按 07 的裁决折叠为只读派生视图，不落独立存储列**（`05` §4 M9） | `[05:50]` |
| 10 | `record_locator`（正文只存 store 侧账本引用 / oid；**权威出处不落正文**） | 全部七问的**承载前提** | 账本 Owner（安装方 / 真相层持有者） | 账本被清扫或 git 真相层丢失 → **整体**失效 | 所有出处都可被被记录对象自己改写 | Agent 12 `provenance_holder_rule`：`14` 的 catalog provenance 落在安装方持有的 `.install-metadata.json`（sha = checked-out commit），树内 `.hermes-catalog.json` 只是便利副本、**Python 从不信任它**；`15` 把可编辑的 `_prompts/consolidation.md` 降为不可信项目数据。反例 `[E]`：`05:distill-run-record-results-json`（UNVERIFIED）把 results.json 放在 skill 安装目录本身（升级即丢、污染只读安装物、slug 派生算法未定义 ⇒ 同一原则两次运行得到不同 id，去重失效） | `[05:51]` |
| 11 | `refs_integrity`（由可重跑 auditor 脚本写入的引用完整性结果位，每轮重算） | Q2、Q3、Q4 的可信前提 | provenance auditor（deterministic script） | 每轮提炼结束重算；**fail-on-unresolved** | 悬空引用静默存活 | 实测：`DESIGN-DECISIONS.md:215` 的 DD-3 `clusters` 含不在 67 簇集合内的 `proxy-metric-in-loop`，靠 SPEC §7.1 散文修补；本轮复核其映射 CM-41 唯一匹配成员 `07:cheap-keyword-overlap-proxy-metric` **在成员层成立**，但形态不可接受。按 SPEC §9：**CM-41 其余 5 个成员属成本分层，不得把整簇当 DD-3 依据** | `[05:52]` |

字段 1 与 2 在 schema 里同属一个 `origin` 对象（`origin.required = [problem, why, source_refs]`），其余每条一个顶层属性 ⇒ **11 条字段 ↔ 10 个顶层属性**，见文末核算。

---

## 3. provenance 参与决策的 5 条分支 `[05:54-70]`

口径对齐注（`05` §2.1 原文，Round 2 审计补注）`[05:56-59]`：本节数的是**设计分支 5 条**；`10` §2.1 数的是**其中具备第一轮实现支撑的 4 类**，二者不是矛盾。另注意 **D1 是离散 authority 层级排序**，与 DD-7 明确 DEFERRED 的「按 `origin.channel` **数值**降权」不是同一件事（后者第一轮 0 实现，`10` 的 `origin.channel` 只记录不决策）。**Round 3 实现 D1 时不得顺手把它做成数值降权，那会越过 DEFERRED 边界。**

| 分支 | 规则（照录） | 出处 |
|---|---|---|
| **D1** | 注入排序按 authority 层级 `human > user-corrected > agent-inferred > import/shared > raw-unverified`；verification 为空则**不进 always-on 注入**，只进可展开证据区。支撑：`15:rrf-multi-stream-retrieval(belief_authority_weight)`、`11:bounded-trace-evidence-read`（Raw sessions do not enter Recall ranking）、`14:trust-weighted-fact-store-feedback` | `[05:62-63]` |
| **D2** | 晋升需 `evidence_refs` 全部 resolver 通过 + `refs_integrity` 无悬空 + **至少一条 runner 写入的 PASS**。正例 `02/04`；反例 `07/13` | `[05:66]` |
| **D3** | `provenance.actor` 不匹配 owner 即**拒绝自动化写入（fail-closed）**；归属只经人类 adopt 变更。支撑 `14/06` | `[05:67]` |
| **D4** | 来源失效、出处不可解析、`artifact_sha` 与验证记录不符 → **标 stale 并降权，不删**。支撑 `15 page_evidence` / `10 cascade-stale` | `[05:68]` |
| **D5** | 报告里每个数字与状态位都从 lifecycle/verification 账本算出；**无记录渲染 UNKNOWN，禁止字面量与「Implemented」类推定**。反例 `07:generate_report.py:406-412/269/257` | `[05:69-70]` |

未闭合项（`[I]` + DEFERRED，原文）：「**按 `origin.channel` 具体数值降权**的映射与阈值、verification 缺失时的降权幅度 —— 第一轮唯一相近实现 `10` 自身明示无消费端，无任何参考项目实现过 channel→权重系数映射。DD-7 有对照样本后定。」`[05:71-72]`

---

## 4. 信任强度按**断言类别**分派（L1–L5 + 自报口）`[10:15-27]`

原文：**「不是「全局取最强的一档」，而是按断言类别分派：四类断言的可观测面本就不同（读取事件 / 文件状态 / 类型构造 / 归属键），强行统一强度会*同时*得到 02 的假阳性与 03 的无出处。」** `[10:18]`

| 断言类别 | 分派强度 | 主实现 | 出处 |
|---|---|---|---|
| 「我读过」（可读性 / 检视声明） | 事件流反查 **+ fail-closed 硬门**（档 4 + 档 0） | `02` 骨架，**必须修 §4.1 三处缺陷** | `[10:22]` |
| 「我改了」（写入 / 变更声明） | read-before-write 路径集合记账 + `created_by` 多出口谓词 + 能力面锁权（档 2 + 档 3） | `14` + `06` + `02` 上游锁权 | `[10:23]` |
| 不可信文本入库 | newtype / 类型层强制（档 1，**最强但孤证**） | `15:typed-sanitizer-boundary` | `[10:24]` |
| 产物强标识符（邮箱 / handle / ID） | 证据逐字集合差（档 0 排除式） | `11:evidence-grounded-identifier-check` | `[10:25]` |
| 不可逆语义归类（归并 / 归档 / 分类） | 分层权威对账 + 可见降级（档 2/4 的事后变体） | `14` + `15` + `06` | `[10:26]` |
| 自报采集口 | **保留，但明确不构成证据等级** | `08` / `03` / `09` | `[10:27]` |

### 4.1 L1 骨架必须修掉的三处已核实缺陷 `[10:35-41]`

| 缺陷 | 02 原形态 | 后果 | 修法（02 自己的 `code_reuse` 建议） |
|---|---|---|---|
| **子串假阳性** | 子串 `haystack` / `contains_audit_keyword` 匹配 | **可绕过的假阳性**：文本里出现关键词即算读过 | rewrite 为**结构化 tool-call 参数解析**（不是字符串包含） |
| **mode 静默退化** | coverage 判定 **mode-gated** | 某些 api_mode 下覆盖检查**静默不生效**，看起来通过 | mode 无关的采集口，或显式记 `coverage=unobserved` 并加强制人工 review |
| **整批重试** | **全量恰好相等**（缺一个就整批拒） | **整批重试死循环**，一条幻觉让整批反复重跑 | 按项拒 / 部分通过 + 差额清单；重试上限显式化 |

L1 骨架（`02:claimed-inspection-audit-trail-gate`）的硬门语义：`run_scan` 返回 `Err` 且 `last-scan.json` 水位**不前进** `[10:33]`。

### 4.2 L3 孤证声明（照录，不得升格）`[10:51-57]`

原文：「`独立项目数 = 1（全仓仅此一处用类型系统承担信任边界），故本 DD 不能宣称该级已跨项目复现`」`[10:55]` ⇒ 本档只覆盖「不可信文本入库」这一条边，**不得**当作整条防线；仅当出现 ≥3 个 VERIFIED 项目的 newtype 强制实现，才升为该类别默认强度 `[10:56]`、`[10:231]`。

### 4.3 L5 采纳形态 `[10:66-70]`

权威等级 **`delete` 声明 > 校验过的模型声明 > 审计启发式 > fallback**；`destinations` 必须**真实存在或本次新建**才采信模型声明；可见降级三形态（`source='tool-call audit'` / 采用审计并保留 `model_claimed_into` + `REPORT.md` 打 ⚠ 行 / 归 `pruned` 并写 fallback 原因）`[10:68-69]`。
它不能替代 L1 的原因：14 的对账是**事后分类、不阻断任何写入**，对不可逆写入**无止损点**；采纳形态 = 「事后对账 + 不可逆那一步显式前置硬门」`[10:70]`。

### 4.4 L6 / 自报采集口的边界 `[10:77-84]`

`08:learn-tag-correction-capture` risks 自陈「依赖模型自愿输出标记，**漏采完全不可见**」「`dist/` 未构建时静默丢数据」`[10:79]`；`03:explicit-slash-capture-command` 以反向 grep 证明全文**无** `timestamp/provenance/confidence` 字段、**无回读无校验** `[10:80]`；自报口唯一可接受的失败形态是**显式降级行，不是静默**（`09:turn-lossy-summarize-capture`：失败写固定降级行，绝不落原始 transcript）`[10:81]`。
`01:dual-source-trace-learnings` **不得计入 VERIFIED 独立取证项目数**（UNVERIFIED，且实现完全依赖外部 Entire CLI）`[10:83]`。

---

## 5. 承载者规则：出处记录**不得**放在被记录对象自己手里 `[10:119-128]`

- **安装方持有的记录**：`hermes-agent/plugin-catalog` 的 provenance 活在 **installer-owned `.install-metadata.json`**（`catalog` 块，`sha` = 实际 checkout 的 commit）`[10:122]`。
- **树内副本只是副本**：`.hermes-catalog.json` 是给 Desktop 读的便利副本；**Python 从不信任它**——`a repo can ship a forged one` `[10:123]`。
- 第三处同形：`06` 的权威在 `.sidecar.json` 的 `created_by:'agent'`，而 README 宣称的 `.ledger.jsonl` 条目形状**不含该字段**（RT-09）`[10:124]`。
- **通用规则**：**声明方不得持有判定自己是否可信的那份记录**。推广到 Distiller：每轮产物的出处账本必须由**产生器之外**的装配步骤写（对应 `11-FAILURE-MODES.md` §2 的 RT-08）`[10:125]`。
- 配套两条 `[10:126-128]`：① **provenance 写时一次盖戳、不可覆盖**（`10/15`）——「把 provenance 字段当作可后补的元数据」已被否决（`10:importOrigin` 证明必须写时盖戳且绝不覆盖，事后补会被派生记录覆盖）；② **回写原始会话路径**（`02` 的 `staged_to_original`）⇒ 产物天然带可反查出处，而不是带一个自描述字符串。

两条方向相反、必须写成两条独立条款的规则 `[10:114-115]`：`author_id` **永不得**成为读过滤（`ai-memory` invariant 16：按操作者收窄页面读会在团队协作下**静默失效而所有单用户测试仍通过**）；采纳的并存前提是「**成员资格可以按归属过滤；可读性与排名不可以按作者过滤**」。

---

## 待确认与暂缓事项

- `DEFERRED id D10-1` = `05` §2.1 的未闭合项：**「按 `origin.channel` 数值降权」第一轮 0 实现** ⇒ 不得写入 Core `[10:237]`；`10` §2.2 亦判 DD-7b 为 DEFERRED，**不得写成 CORE 条款** `[10:110]`。
- `DEFERRED id D10-2`：newtype 强度为**孤证（1 项目）** `[10:238]`。
- `DEFERRED id D10-3`：**档 4 的参数全部未定**（恰好相等 vs 至少一次、是否抽样、失败重试上限、无观测面宿主如何降级）——「足以定方向但不足以定参数」`[10:239]`。
- `DEFERRED id D10-4`：**Agent 12 的 11 字段清单与第 7 条自引用失败**不在 `10` 的唯一主输入内；`10` 只能按任务书转述 1/7→7/7，并引用可回读的 6 条 `dd_04_fields` `[10:240]`。（本文件的逐条清单来自 `05` §2，不来自 `10`；**这不等于 D10-4 已关闭**。）
- `DEFERRED id D10-5`：「Agent 16 自述数字需独立审计」本轮**未找到磁盘证据**，按**待核**登记，不作已证实依据 `[10:241]`、`[10:169]`。
- `DEFERRED id D10-6`：`13:citation-key-provenance-rule` 仅可作文案参考，不得作机制依据 `[10:242]`。
- `DEFERRED id D10-7`：**`created_by` 的语义漂移**（docstring 自陈它实为 curator 接管策略标志 #67140）⇒ 字段最终命名与语义归属需合流确定，历史构建时点不擅自改名 `[10:243]`；`05` 侧同一裁决记为 M2（保留两列、职责不同）`[05:106]`。
- `DEFERRED id DM-2`（`05` §7）：`provenance.actor` 的具体数值如何映射为降权系数（D1 排序的权重表）——当前只定到「层级顺序 + verification 为空即不进 always-on 注入」这一保守形状 `[05:262]`。
- `UNKNOWN`：`10` §5 表中 SR 第 7 条自引用失败「**历史构建时点无法逐字枚举**」，标 DEFERRED 不编造 `[10:164]`。
- 共识度修正（引用本簇时必须用修正值）：`CM-47` 名义 `consensus_projects=6`，按 VERIFIED distinct projects 实为 **4**（计入 02/04/11/14，**剔除 01 与 13**）`[10:175-178]`。

## 历史源码对照

以下保留历史构建时点的只读观察（python3 stdlib；当时未运行测试套件），不是本轮验证结果；当前出处接口见下一节：

1. **字段数**：`schemas/provenance-record.schema.json` 顶层 `properties` = **10 个**（`origin`、`evidence_refs`、`evidence`、`actor`、`generation`、`verification`、`lifecycle_event`、`derived_from`、`record_locator`、`refs_integrity`），`required` 同为这 10 个，`additionalProperties: false`。`05` §2 的表是 **11 行**：行 1（`origin.problem`/`origin.why`）与行 2（`origin.source_refs[]`）在 schema 里折叠进同一个 `origin` 对象（其 `description` 分别自称 `Field 1`/`Field 1`/`Field 2`，其余自称 `Field 3`…`Field 11`）⇒ **11 字段 ↔ 10 顶层属性，命名与行号一一对应，无缺项、无增项。**
2. **子字段与 `05` 原文对齐**：`generation` 的 6 个 required 恰为 `{round_id, pass_id, compiler_version, model_id, config_sha, created_at}` `[05:47]`；`verification[]` 恰为 `{eval_id, verdict, run_at, run_evidence_hash, artifact_sha}` `[05:48]`；`evidence_refs[].kind` 与 `origin.source_refs[].kind` 为闭合枚举（后者 = `["issue","session","fix","dd","run"]`，逐字等于 `[05:43]`）；`evidence.status` 与 `evidence_refs[].status` 枚举 = `["VERIFIED","UNVERIFIED","UNKNOWN"]` `[05:44-45]`。
3. **actor 的 fail-closed**：schema 用 `anyOf: [enum ["human","curator","import","shared"], pattern "^agent:[A-Za-z0-9._-]+$"]` 表达 `05` 的 5 成员集 `{human, agent:<name>, curator, import, shared}` `[05:46]`；schema 描述原文：**「there is no default and no 'unknown', because absence must fail closed」**⇒ 与「缺省 fail-closed」一致，且 `required` 含 `actor`（缺失即 schema 违规）。
4. **谁写 ≠ 谁声明**（对应 `[05:51]`、`[10:125]` 的承载者规则）：`kd_provenance_stamp.py` 只产出 **2 个** provenance 字段——`generation` 与 `actor`——包成 `record["provenance"] = {generation, actor, subject_digest, stamp_digest}`；其 `SELF_DECLARED_KEYS` 把 `provenance`、`generation`、`actor`、`stamp_digest`、`verification`、`status_basis`、`refs_integrity` **7 个键**列为「提案里自报即 exit 2」。其余字段的写者按 grep 落在：`refs_integrity` ← `kd_refs_audit`/`kd_write_txn`（schema 描述亦写「Written by the re-runnable S14 auditor and recomputed every round」）、`evidence_refs` ← `kd_ingest`/`kd_proxy_candidates`/`kd_model_step`/`kd_refs_audit`/`kd_write_txn`、`record_locator` ← `kd_ingest`/`kd_lifecycle`/`kd_write_txn`、`verification` ← `kd_gate_tree`/`kd_proxy_candidates`。**未发现任何脚本写 `lifecycle_event` 顶层键**（grep `lifecycle_event` 在 `scripts/*.py` 内 0 命中；账本行由 `kd_write_txn` 经 SC07 `lifecycle-event-ledger.schema.json` 落盘）⇒ 与「audit writer」职责一致，但字段名不同名，登记为命名差异。
5. **一次盖戳、不可覆盖已被实现**：`kd_provenance_stamp.py` 在 `existing` 已带 `generation`/`stamp_digest` 且 digest 不同时抛 `stamp overwrite refused: ... immutability means a new entry linked by lifecycle_event, never a rewritten stamp (05-DATA-MODEL.md:47)` ⇒ 直接对应 `[05:47]` 与 `[10:127]`。
6. **L1–L5 分派在 schema 里是可枚举对象**：`provenance-record.schema.json` 的 `$defs.note_l1_l5_dispatch.assertion_classes` 共 **6 条**，与 `10` §1 总表的 6 行逐一对应（`我读过`=L1、`我改了`=L2、`不可信文本入库`=L3 并照录「**孤证, 独立项目数 = 1**」、`产物强标识符`=L4、`不可逆语义归类`=L5、`自报采集口` 标 **「kept, but NOT an evidence grade (10 §1.6)」**）；每条带 `carried_by`（本 schema 的字段）与 `enforced_by`（`kd_refs_audit`/`kd_provenance_stamp`/`kd_write_txn`/`kd_gate_tree`）⇒ 承载者规则与分派表都进了契约，不只是文档。
7. **不一致 / 缺口（只报数，不改任何一方）**：
   - S13 实际**只盖 2 个字段**，另外 8 个字段由别的脚本或另一条路径写；`provenance-record.schema.json` 要求 10 个全在 ⇒ 单独调用 `kd_provenance_stamp` 的产物**不是**合法 provenance-record，必须由 `kd_write_txn` 组装。这是责任分工不是矛盾，但从文件名字（`provenance_stamp`）读会误以为它产出整份记录。
   - `subject_digest` / `stamp_digest` 存在于脚本产出的 `provenance` 块，**不在 `05` §2 的 11 行内**；`provenance-record.schema.json` 的顶层也不列它们（顶层 10 个属性、`additionalProperties: false`）⇒ 二者是脚本内部的绑定摘要字段，若把该块直接当 SC06 实例校验会失败。脚本自身的 `IMPLEMENTATION_GAP` 注释已声明：digest 是完整性绑定、**不是签名机制**，并挂 `DEFERRED id DD-7-sub49`。
   - `refs_integrity.status` 的枚举为 `["PASS","FAIL_UNRESOLVED","FAIL_SHORTHAND","EMPTY_REF_SET","SCANNED_SET_INCOMPLETE"]`：`FAIL_SHORTHAND` 与 `EMPTY_REF_SET` 两位对应 `[05:44]` 的 brace/通配简写与 `[10:158-160]` 的 SR-1/SR-2/SR-3，**`05` §2 行 11 本身只写了 fail-on-unresolved** ⇒ 代码比文档多两类拒收形态（正向差异，如实登记）。

## current-implementation — 当前出处接口

上文 历史源码对照 是构建时点观察，不回改历史。当前 S13 的纯函数 `provenance_record` 接受 S12 已验证的最终 SC04、同 Scope 完整 SC01 和实际分配的 SC07，生产 SC06 全部 10 顶层键 / 11 字段，并调用随包 Schema 拒绝缺项。它没有批准权，也不写文件。

S12 `kd-file-transaction/3` 将 SC06 存入现有不可变 transaction history，与 records、SC05、SC07 绑定同一提交点；正文仍只带内部 stamp 子集。`read_provenance(store_dir, artifact_id, transaction_id=...)` 是完整记录的公开消费者：只读已索引提交，核验摘要、来源观察、Eval、正文版本和 SC07，篡改或未提交历史拒绝并保留。UPDATE / RESTORE 产生新出处，旧出处字节不变；`derived_from` 是同批观察所得的派生记录，不成为第二谱系写入权威。

本地 synthetic 三通道场景证明机械边界，不认证真人或真实任务测量；生产渠道仍由调用方接入。旧协议不自动迁移，缺真实生命周期事件时 NULL 不填 0。历史 Deferred 不因新增 API 自动关闭。
