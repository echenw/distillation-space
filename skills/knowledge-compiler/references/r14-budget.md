# R14 — 控制阅读量与上下文预算

控制 AI 实际读取的内容量。只加载当前任务需要的节，按真实宿主容量和阶段管理上下文。已删除从其他项目借用的固定加载链硬阈值；`kd_budget.py --measure-content` 只提供文件大小统计，不限制阅读或任务执行。不能假装旧消息已释放。

历史来源： `.distill/round-2/09-CONTEXT-BUDGET.md` §1.1–1.5（行 17–63）、§2（行 67–78）、§3（行 82–98）、§4（行 102–123）、§5（行 127–137）、§6（行 141–150）、§7 末条与 §10 DEFERRED（行 161、191–201）。生成于 2026-10-06，wave 4。
状态说明：本文供参考；具体行为以 `../scripts/`（`kd_budget.py`）与 `../schemas/budget-config.schema.json` + `budget-config.json` 为准。
引用约定：`[09:N]` = `.distill/round-2/09-CONTEXT-BUDGET.md` 第 N 行，行号保留原整理时点的定位。

---

## 阅读导航

- 1. 分层三处置（**不是 A/B/C 三选一**）`[09:12-15]`
- 2. 三维矩阵（对象 × 单位 × 处置）`[09:67-78]`
- 3. 阈值同源：AST 属 IMPLEMENTATION_DETAIL，「同源 + 被测试锁定同一个数」属核心约束 `[09:82-98]`
- 4. `09` §4 的 14 条 `recommended_defaults`（带出处与采纳状态）`[09:102-123]`
- 5. 引用 `CM-31` 时的剔除义务（虚假共识警告）`[09:127-137]`
- 6. 被否决的备选（8 条）`[09:141-150]`
- 待确认与暂缓事项
- 历史源码对照

## 1. 分层三处置（**不是 A/B/C 三选一**）`[09:12-15]`

判据原文：「**处置方式是「谁是该产物 Owner」的函数**，因此 A / B / C 不是互斥竞品；把它们当三选一本身是 Round 1 的建模误差。」`[09:15]`

| 层 | 对象 | 单位 | 处置 | 关键约束 | 出处 |
|---|---|---|---|---|---|
| **历史候选：单文件写入尺寸门（默认未启用）** | **单文件**（slot 内容、`SKILL.md` 正文、evolved body、根 `AGENTS.md`） | **真 UTF-8 字节为主 + 行数为辅** | **仅在调用方明示限额时硬拒**；默认不以他人项目数字限制 Rule/Skill | ① **双闸并存**：绝对上限 + 相对增长上限（只禁增长不禁收缩）`[09:22]`；② 门必须**量整份产物（含 frontmatter）**，并在**每个候选、每次迭代**上跑，而不是只对最终产物跑一次 `[09:23]`；③ 部署产物路径必须不可被版本控制收录（未过门样本落点需在路径级排除）`[09:24]` | `[09:17-21]` |
| **历史候选：外部项目指令链（未采用）** | **适用宿主的项目规则文件**（该目录及其祖先实际加载的项目指令字节和；不是参考资料的累计读取） | 真 UTF-8 字节 | 把 `12` 的 warn **升级为 `14` 的 CI 非零退出**；同时保留 `12` 的降噪经验（每条超预算链**只在最浅超预算目录报一次**），逐条打印 `path: size chars > cap` | **新增约束：加载链上限 ≤ 单文件上限**（消除 `14` 的 30k 链 / 32k 文件不对称）；原文标注：该修正「**数值本身 EVIDENCE-SUPPORTED**」，修正动作在 DD-5 `recommended_defaults` item4 标 **ENGINEERING-INFERENCE** `[09:38]` | `[09:33-37]` |
| **可选调用方注入规划** | 注入 block 序列 | 调用方明示的字节预算 | **确定性丢弃 + 可见 marker** | 优先级严格固定 `[09:44-46]`：`整块跳过 > 行边界字节前缀 > head + tail + 可见 marker` | `[09:41-53]` |
| **第 4 层 写作规范（定性）** | 每行测试类规范 | — | **只用于决定「谁该被丢」**（价值/资格排序），数值上限**用于决定「何时停」** | **「定性预算一律不作为阈值」**；`03:instruction-budget-rules` 的 decision_rules 原文：grep 确认全文不存在 `max/limit/size/char/bytes/count` 任一预算字段，validation 原文：**无**；仅 1 个项目且为负控制 `[09:55-58]` | `[09:55-58]` |

第 3 层的六条细则（逐条照录）`[09:47-52]`：
1. **整块跳过优先**（`10`：`if (usedTokens+block.tokens > budget) continue`，不切碎任何块）。
2. **必须截断则落在行边界**（`11`：`data.rfind(b'\n', 0, budget)`，测试名断言「不含半行」），并带**可见 marker**（`14`：`_truncate_content` / `_omitted_headings` / `drain_truncation_warnings`；`09`：`[older journal entries truncated]`）。
3. **advisory 预算不足则整体不渲染，绝不挤掉证据**（`15`：`saturating_div(2)` + `render_instructions_block` 的 `minimum_chars` 整体放弃）。
4. **从尾取整行，且最新一整行放不下时不回退更旧并显式标记不可用**（`09`：返回码 2，不静默降级）。
5. **双预算投影**（行 + 字节，按 `weight` 从最低价值 break）：`11:memory-md-budget-projection`。
6. **新增：单 block 上限**，防止某个块永久不被注入（→ §4 item 10，**ENGINEERING-INFERENCE**）。

### 1.1 warn-only 的唯一合法例外 `[09:60-63]`

原文：**「warn-only 仅适用于「生成器不是产物 Owner」的场景**（`12` 无权改写用户产物，所以只能提示）。对 Distiller 自身产物，**我们就是 Owner，无理由采用最弱处置**。」** `[09:62]`
佐证与剔除：`12` 自记「告警不阻断，CI 不接等于没有」；`12:instruction-budget-truncation` 是**负证据**（UNVERIFIED，证明该仓不存在按预算截断），**不得当作已证实机制引用**——ATT-12 实测它仍被 DD-5 stance B 当 `supported_by` 引用 ⇒ **本轮予以剔除** `[09:63]`。

---

## 2. 三维矩阵（对象 × 单位 × 处置）`[09:67-78]`

| 维度 | 候选 | 本轮采纳 | distinct projects 与出处 |
|---|---|---|---|
| **计量单位** | 真 UTF-8 字节 / 行数 / 字符 `len` / token 估算 / 外部工具定义 | **真 UTF-8 字节为主**，行数辅助 | **3 项目独立选字节**：`09`（`len(context.encode('utf-8')) <= 1800` 写进测试断言）、`11`（`budget_bytes=8192`，`test_memory_md_budget_is_a_hard_ceiling` 也是字节断言）、`12`（`Buffer.byteLength(...,'utf8')`）。失真自记：`10` 的 `ceil(len/3)`、`15` 的 flat multiplier、`12` 的「以字节近似 token」——**作者自己标注对 CJK / 代码失真**。token 单位仅 `04`（外部定义）与 `10`（自记失真），故**不作硬上限判定单位** `[09:73]` |
| **超限处置强度** | 硬拒 / CI 红 / 整块跳过 / 行边界前缀 / marker / warn / 静默丢弃 | **历史观察：写侧硬拒 + CI 红（5 项目）** | `10` 拒写并回显 `currentSize/sizeLimit` + remedy；`14` CI 非零退出逐条打印；`04` 绝对+相对双闸失败即红；`07` 不部署但写 `evolved_FAILED.md` 保留样本；`01` 有界评审；`10` skills:check `DRIFT + exitCode=1` `[09:74]` |
| **丢失承担方** | 宿主静默丢弃 / 本方主动确定性丢弃 | **注入侧确定性丢弃且必须可见（5 项目）** | `09`/`10`/`11`/`14`/`15` 主动丢，但要求确定性次序 + 可见 marker。`12` 的 warn 让宿主静默丢弃 ⇒ `14` problem 原文：膨胀后运行时静默截断会让规则丢失且**没人知道丢了哪条**。**「这不是强度差，是失败归属差」** `[09:75]` |

最有支撑的组合：`真 UTF-8 字节` × `写侧硬拒 / CI 红（5 项目）` × `注入侧确定性丢弃且必须可见（5 项目）` `[09:77]`。
另两个关键形状各有 ≥2 独立项目：链式测量（`12` 用真字节 + `14` 用字符，两项目**独立实现祖先链求和**）；绝对 + 相对双闸（`04` 的 3000+10% 与 `07` 的 15_000+20%）`[09:78]`。

---

## 3. 阈值同源：AST 属 IMPLEMENTATION_DETAIL，「同源 + 被测试锁定同一个数」属核心约束 `[09:82-98]`

- **`threshold_binding_has_multi_project_support = False`**：AST 阈值绑定这一具体机制**经独立检索仅 1 家支撑 ⇒ IMPLEMENTATION_DETAIL**，不得按共识度引用它 `[09:84]`。
- **其上位原则判为核心约束**：「**阈值必须与真正执行的门同源，且被测试锁定同一个数**」，依据是五个项目的**同型失效**证据 `[09:85]`：

| 项目 | 声称的预算 | 真正执行的门 | 后果 | 出处 |
|---|---|---|---|---|
| `06` autoharness | `README:111` 称 `AUTOHARNESS_SKILL_DESC_MAX_CHARS=1024` 是硬上限且「超限被拒绝」 | 常量只在 `config.py:42` 定义、`README:111` 宣称、`test_validate.py:160` 的字符串构造中出现；**实际拒绝门是 `INDEX_DESC_MAX_CHARS=60`** | 测试构造 `1025` ⇒ `1025 > 60` ⇒ **假性通过**；1024 语义从未被任何代码路径实现 | `[09:89]` |
| `07` hermes-agent-self-evolution | `PLAN.md:668` 称每候选都被门控、失败即丢弃 | 门只在 `evolve_skill.py:188` 对**最终产物**跑一次；量的是 `len(evolved_body)`（**字符**），部署产物却是 `reassemble_skill(frontmatter, body)` | **frontmatter 不计入 15 KB**；循环内无门 | `[09:90]` |
| `14` hermes-agent | 根 `AGENTS.md` 把 12k / 30k 说成一对 cap | 单区域文件实际受运行时 `_MAX_HINT_CHARS = 32_000` 约束；prompt 的 `truncated to 57 chars` 实为 `desc[:60-3]+'...'`（57 + 省略号 = 60 总长） | 链 30k 与文件 32k **不对称**；文档数字与生效数字不同 | `[09:91]` |
| `10` agentmemory | 五层预算（slot `sizeLimit` 默认 2000、`coreBudget=floor(budget*0.3)`、`MEMORY.md lineBudget`、`SKILL.md MAX_LINES=100`） | 无统一读取源 | worker-caveats `10.open_questions` 原文：**「无全局协调」** | `[09:92]` |
| `04` agent-skills | `.waza.yaml` 的 3000 与 `docs/agents/verification.md` 的 3000 | **两份定义、无一致性测试** | 任一处改动即静默漂移 | `[09:93]` |

采纳的三条可执行防线 `[09:95-98]`：
1. **每个预算数字只有一个定义点**，且被**写入路径与测试同时读取**（RT-07 的 `required_guard`）。
2. **lint 规则**：文档中出现的每个数值上限，必须能 grep 到**同名运行时常量**；反之每个运行时常量必须有读侧。
3. **阈值入架构时必须附「谁写计数器 / 哪行代码读它」的实证答案**（RT-10 `required_guard`），否则不得记 VERIFIED。

与 R11 的接口：「本文全部阈值**只产生阻断信号，不产生 verified**」`[09:161]`。

---

## 4. `09` §4 的 14 条 `recommended_defaults`（带出处与采纳状态）`[09:102-123]`

下表按 `09` §4 的 14 项顺序整理，**不是逐字转录**：将一般说明统一为当前的上限和知识提炼术语，并增加机器处置列；数值、关键限定与风险理由必须依照冻结原文理解。`authority_token` 是需要与冻结出处逐字核对的机器字段，因此仍保留原文的「帽」，不可据本表改写。**「采纳状态」列保留历史构建时点的机器处置**，见文末历史对照。当前数值与处置须读取 `budget-config.json` 并核对 `kd_budget.py`，不能把本表当成新的预算定义点。凡 `09` 标 ENGINEERING-INFERENCE 或未给数值的，一律**不得**当作已定案阈值。

| # | scope（现行措辞） | 值（按原文整理） | 出处 | `09` 标注 | 当前机器处置 |
|---|---|---|---|---|---|
| 1 | 常驻索引投影 | `max_lines=120` 且 `budget_bytes=8192` 双预算；超出按 `(-weight, updated, name)` 降序 break，丢最低价值行 | `agent-memory/packages/core/src/agent_memory/core/config.py` + `core/memory_md.py` + `tests/unit/test_indexer.py` | EVIDENCE-SUPPORTED `[09:108]` | **现行不采用**：索引尺寸不限制完整 Rule 正文 |
| 2 | SessionStart 注入侧字节上限 | `injection_budget_bytes=8192`，截断必须落行边界（`data[:rfind(b'\n',0,budget)]`） | `agent-memory/.../core/injection.py` | EVIDENCE-SUPPORTED `[09:109]` | **现行不采用**：注入规划由调用方显式设置预算并按正文真实 UTF-8 字节检查 |
| 3 | 冷启动 hook inline context | `RECENT_MEMORY_MAX_LINES=40` / `RECENT_MEMORY_MAX_BYTES=1800` / 文件数 2；最新一整行放不下则**不回退更旧文件** | `memsearch/plugins/claude-code/hooks/session-start.sh`（断言见 `tests/test_claude_hooks.py`） | EVIDENCE-SUPPORTED `[09:110]` | **拒绝执行**（`value: null`）：`cold_start_max_lines` / `cold_start_max_bytes` / `cold_start_max_files`。理由：这三个数是**二手经验值**，`09` §10 D09-1 明说宿主真实截断行为未实测 |
| 4 | 外部宿主项目指令链历史例子（Codex 类宿主，非所有 Reference 的累计读取） | `32 * 1024 = 32768 bytes` | `rulesync/src/constants/codexcli-paths.ts#CODEXCLI_PROJECT_DOC_MAX_BYTES` | EVIDENCE-SUPPORTED `[09:111]` | **现行不采用**：该值仅是来源示例，未进入预算配置或写入门禁 |
| 5 | 外部项目根指令及区域链（仅历史） | `ROOT_MAX_CHARS=12_000`；`CHAIN_MAX_CHARS=30_000`；**采用时另加「加载链上限 ≤ 单文件上限」** | `repos/hermes-agent/scripts/ci/check_agents_md_size.py` | 数值 EVIDENCE-SUPPORTED / **修正 ENGINEERING-INFERENCE** `[09:112]` | **拒绝执行**（`value: null`）：`root_instruction_max_chars` 保留为未启用的参考条目，另外两项已从现行配置删除 |
| 6 | `SKILL.md` 行数上限（分档） | 常驻 / 索引型 **100 行硬顶**；任务型 **500 行软警 + 600 行硬限**；细节一律下沉 `references/` | `agentmemory/scripts/skills/check.ts:10`；`pskoett run-tests.sh:83-91`；`agent-skills/CONTRIBUTING.md` | EVIDENCE-SUPPORTED `[09:113]` | **现行不采用**：100/500/600 行仅为历史参考，不能当成所有 Skill 的宿主硬门 |
| 7 | 绝对 + 相对双闸门 | 绝对按**整份产物字节**；相对增长 **>20% 失败**（`07` 口径），**10%** 作更严格备选（`04` 口径）；**只禁增长不禁收缩** | `evolution/core/config.py:28-33`（`max_prompt_growth=0.2`）；`agent-skills/.waza.yaml` + `docs/evals/waza.md` | EVIDENCE-SUPPORTED `[09:114]` | **现行不采用**：不对合法的大版本改动施加通用增长百分比硬拒绝
| 8 | 写入即校验的配额槽上限（借语义不借分层表） | `sizeLimit ∈ [1,20000]`，默认 **2000**；append 前算 `next.length > sizeLimit` 即返回错误，附 `currentSize/sizeLimit` 并提示先 replace 压缩 | `agentmemory/src/functions/slots.ts:13-98,149-154` + `src/types.ts:275-285` | EVIDENCE-SUPPORTED `[09:115]` | **拒绝执行**（`value: null`）：`slot_quota_default_size`。`09` §6.8 已把「直接沿用 agentmemory 的 8 个预置槽尺寸表」列为被否决备选，只借语义 |
| 9 | 注入侧 token 估算（**仅用于整块跳过的相对排序，不作硬上限**） | `estimateTokens = ceil(len/3)`；`TOKEN_BUDGET=2000`；`coreBudget = floor(budget*0.3)` | `agentmemory/src/functions/context.ts` + `config.ts:223`；`coreBudget` 见 `worker-caveats.json` 的 `10.open_questions` | 数值 EVIDENCE-SUPPORTED / **降级为排序用途 ENGINEERING-INFERENCE**（作者自记 `len/3` 对 CJK 与代码失真）`[09:116]` | **拒绝执行**（`value: null`）：`token_estimate_budget`；`unit_policy.not_adopted = ["tokens"]` |
| 10 | **单个注入 block 上限**（防「永久不被注入」失效） | **注入字节上限的 1/4**（`8192` 时取 `2048`），保证任一 block 至少可达 | **无来源**（`10` 自记「未对单 block 设上限」；借 `distill/src/scanner/engine.rs#select_session_batch` 的「超大首项仍允许以免队列卡死」原则迁移） | **ENGINEERING-INFERENCE** `[09:117]` | **拒绝执行**（`value: null`）：`single_block_max_bytes`；`--deferred` 的 disposition 原文：`refused to derive a quarter-cap number` |
| 11 | 编译器自身 maintenance / 提炼 prompt 上限 | `80_000 chars` **不可直接沿用**，需按自家模板与语料另定；可迁移的是反向扣除次序「预算 = 总上限 − 模板 − 现有正文 − 预留(512)」，以及 `max_files=12`、单条现有正文 2000 chars | `memsearch/src/memsearch/maintenance.py#_read_recent_journals` + `skills.py#_render_existing_block`（次序 EVIDENCE-SUPPORTED，**具体数值 UNKNOWN**） | **ENGINEERING-INFERENCE** `[09:118]` | **拒绝执行**（`value: null`）：`compiler_prompt_max_chars`（数值 UNKNOWN，见 D09-3） |
| 12 | advisory 注入分配 | advisory ≤ 可选预算的 **1/2**（`saturating_div(2)`）；低于 `minimum_chars` 则**整体不渲染，绝不挤掉证据**。`minimum_chars` 具体值 Round 1 **未取到，须自行定** | `repos/ai-memory/crates/ai-memory-consolidate/src/consolidator.rs#render_instructions_block` | 次序与放弃策略 EVIDENCE-SUPPORTED / **具体值 ENGINEERING-INFERENCE** `[09:119]` | **拒绝执行**（`value: null`）：`advisory_share_fraction`、`advisory_minimum_chars` |
| 13 | 截断可见性（marker 契约） | marker 必含 `kept {head}+{tail} of {total} chars`、被跳过项清单（omitted headings）、可回读路径，并**累计到可 drain 的告警队列** | `repos/hermes-agent/agent/prompt_builder.py#_truncate_content` / `#_omitted_headings` / `drain_truncation_warnings` | EVIDENCE-SUPPORTED `[09:120]` | **契约字段而非上限值**：`budget-config.json` 顶层 `marker_contract`；`--caps` 不计入 9 个执行上限 |
| 14 | 技能索引描述上限（**创建期拒绝**） | 描述 **≤60 字符**（渲染侧 57 + `'...'`），超位在创建 / PR 期由 `tests/skills/test_authoring_standards.py` 直接拒绝。**注意 `06` 的 1024 是文档数字，真正的门是 60** | `repos/hermes-agent/skills/AGENTS.md` § Authoring standards 第 1 条 + `agent/skill_utils.py#SKILL_PROMPT_DESC_LIMIT`；反例 `repos/autoharness` `README:111` vs `lib/validate.py` 的 `INDEX_DESC_MAX_CHARS=60` | EVIDENCE-SUPPORTED `[09:121]` | **现行不采用**：外部 UI 长度限制不能限制通用 Skill 描述，当前配置已删除

**当前注入规划接口**：`python3 <SkillRoot>/scripts/kd_budget.py --plan-injection /safe/blocks.json --budget-bytes <本次明确许可的正整数>`。输入块必须带真实 `text`，可选 `bytes` 必须与 UTF-8 字节数相等；相同 ID、重复 JSON 字段和非有限数均拒绝。脚本不读取或核验原始来源文件，因此 `marker.readable_path` 为 `null`，`unverified_source_locators` 仅保存调用方声称的定位符，不能当成已验证的可回读路径。不可将现行退出码或能力误写成上表历史实现。

`09` 自己的出处审计结论（照录）：**「14 条中 11 条 EVIDENCE-SUPPORTED，3 条含 ENGINEERING-INFERENCE 成分（item5 的加载链上限修正、item10 的单块内容上限、item11 的自家 prompt 上限数值），item12 的 `minimum_chars` 具体值同属 ENGINEERING-INFERENCE。无任何一条被允许「无出处直接采用」。」** `[09:123]`

---

## 5. 引用 `CM-31` 时的剔除义务（虚假共识警告）`[09:127-137]`

`CM-31 context-budget-hard-limit` 名义 **consensus_projects=6**，但其中**混入了工作批次预算成员**，按上下文 / 指令预算读会构成**虚假共识**。必须剔除：
- `02:bounded-backlog-and-cost-budget-per-invocation` — `distill/src/scanner/engine.rs#select_session_batch`，对象是 **session raw bytes 批次（20 条 / 64 MiB）**，属**工作预算**，不是上下文 / 指令预算 `[09:130]`。
- `01` 的 `diff% / 次数` 预算成员 — 同为工作批次预算 `[09:131]`。

剔除后 `CM-31` 的**上下文预算成员**为 `07`/`04`/`10`/`11`/`01:bounded-review-budget`；**引用时按 distinct projects 重述，不复用 6 这个数** `[09:133]`。
**只允许迁移两条原则、不允许迁移数值**：① dual cap（绝对 + 相对）；② 「超大首项仍允许，以免队列卡死」（该原则用于 §4 item 10 的 ENGINEERING-INFERENCE 依据）`[09:134]`。
`07` 的 `SyntheticDatasetBuilder`、`13` 的任何条目**均不得**用于支撑本簇（SPEC §9）`[09:135]`。
同族提醒：`CM-33 injection-budget-truncation` 的审计强度不均——其两条最关键成员来自 `worker 11`，而 worker-caveats `11.coverage.read` **为空数组**、无 `doc_vs_impl_gaps`；路径与测试名具体可证伪故仍算 EVIDENCE-SUPPORTED，但**审计置信低于 09/10/14**；`CM-33` 的 `strongest_evidence` 是 `10:token-budget-context-injection`，因此裁决**不单独依赖 11** `[09:137]`。

---

## 6. 被否决的备选（8 条）`[09:141-150]`

| # | 备选 | 否决原因 | 出处 |
|---|---|---|---|
| 1 | 纯 B（全局只 warn 不截断） | 仅 1 项目支撑，且该项目的处置对象是「生成器无权改写的用户产物」；对 Distiller 自身产物无理由采用最弱处置 | `[09:143]` |
| 2 | 纯 A（只有写侧硬上限、无注入侧预算） | 无法封顶每轮运行时成本；`14` 明确 `_load_agents_md` 在合并链之后再截一次 ⇒ **单文件合规 ≠ 不丢内容** | `[09:144]` |
| 3 | 以 token 估算作硬上限判定单位 | 仅 `04`（外部 Waza 定义、模型换代后含义变化）与 `10`（`ceil(len/3)` 自记 CJK/代码失真）两例，均不可断言稳定；`09` 的宿主 2KB 经验值说明**字节才是宿主可核对的量** | `[09:145]` |
| 4 | 链超预算仅打印 warning | 保留 `12` 的「最浅目录报一次」降噪，但处置必须换为阻断 | `[09:146]` |
| 5 | 按 token「即到即止」把块 / 行切碎截断 | **无任何项目实现**（`10` 整块跳过、`09`/`11` 截整行、`14` 截 head+tail 块），且违反 `09`「不切碎多字节」与 `11`「不含半行」两条**已被测试锁定**的判据 | `[09:147]` |
| 6 | `03` 的四条定性预算作为约束形式 | 零数字、零验证，worker 03 自评「作为 MUST 不合格」 | `[09:148]` |
| 7 | 把 `02:bounded-backlog-and-cost-budget-per-invocation` 计入上下文预算共识 | 见 §5 | `[09:149]` |
| 8 | 直接沿用 agentmemory 的 8 个预置槽尺寸表（persona 1000 / project_context 3000 等） | 属该项目专有形状，只借「每类知识一个有上限的槽 + 超限先压缩」语义 | `[09:150]` |

---

## 待确认与暂缓事项

`09` §10 的 **7 条 DEFERRED**，原样转述，**本文件不关闭任何一条** `[09:191-201]`：

- `DEFERRED id D09-1`：**宿主真实截断行为未实测**。各家 inline hook context 上限及超限处置目前**只有 `09` 的二手经验值**（注释引用 issue #676/#684 的 ~2 KB）。若与 1800/8192 显著不符 ⇒ 注入侧上限值**全部重定** `[09:193]`。
- `DEFERRED id D09-2`：`14` 的 CI 红**是否真能拦住一次真实膨胀未验证**（worker 14 记「本轮禁止运行，未实跑」）`[09:194]`。
- `DEFERRED id D09-3`：编译器自有 maintenance / 提炼 prompt 上限的**具体数值 UNKNOWN** `[09:195]`。
- `DEFERRED id D09-4`：`15` 的 `minimum_chars` 具体值 Round 1 **未取到** `[09:196]`。
- `DEFERRED id D09-5`：预算**层间仲裁次序**（slot vs 常驻索引 vs 注入 vs `SKILL.md` 冲突时谁先让步）在全部参考项目中无实现 `[09:197]`。
- `DEFERRED id D09-6`：单 block 上限（建议注入上限 1/4）**无任何项目实现**，纯 ENGINEERING-INFERENCE `[09:198]`。
- `DEFERRED id D09-7`：`worker-caveats.11.coverage` 为空 ⇒ 所有 `11:*` 条目的独立复核缺位 `[09:199]`。
- 另有 §9 的 5 条条件性重审（第 2 项目绑定阈值 ⇒ AST 升 CORE；token 变仓内可控依赖 ⇒ 重评单位；出现跨层仲裁表 ⇒ 补第 3 层规则；单块内容上限反例 ⇒ 回 `02` 原则；补齐 worker 11 ⇒ `CM-33` 置信上调）`[09:183-187]` — 本文件不预设结果。
- `UNKNOWN`：`09` §4 item 12 的 `minimum_chars`、item 11 的自家上限值，Round 2 明确「未取到 / UNKNOWN」，本文件保持 `UNKNOWN` 字面 `[09:118-119]`。

## 历史源码对照

以下保留历史构建时点的只读观察（python3 stdlib + `kd_budget.py --caps/--deferred`；当时未运行测试套件），不作为本轮验证证明：

**现行配置**：已移除借用的六项默认执行的产物/注入尺寸限制（索引两项、Skill 三项、注入一项），现保留 **10 个历史未采用条目，0 项默认执行的尺寸门槛**。下文 21、9、12 等数字仅是历史构建记录；需要限制时由调用方显式给出。

1. **历史构建记录（非当前配置）**：`references/budget-config.json` 的 `caps` 共 **21 条**；`value` 非 null 的 **9 条**（执行），`value: null` 的 **12 条**（拒绝）。`kd_budget.py --caps` 输出 `caps`（9 项）与 `refused`（12 个 id）两个数组；`--deferred` 输出 `refused_caps` + `deferred_linkage` + `enforced_cap_count: 9` + `status: "provisional"`。⇒ **与 Wave 3 报告的 9 executed / 12 refused 一致（9+12=21，无第三种状态）。** 被拒的 12 个 id：`cold_start_max_lines`、`cold_start_max_bytes`、`cold_start_max_files`、`root_instruction_max_chars`、`area_chain_max_chars`、`chain_le_single_file_invariant`、`single_block_max_bytes`、`advisory_share_fraction`、`advisory_minimum_chars`、`compiler_prompt_max_chars`、`slot_quota_default_size`、`token_estimate_budget`。**与 Wave 3 报告的 9 executed / 12 refused 一致（9+12=21）。**
2. **历史 9 个执行上限逐一对应 §4 的 EVIDENCE-SUPPORTED 行**：item1(×2 列)、item2、item4、item6(×3 列)、item7、item14 ⇒ 覆盖 §4 的 1、2、4、6、7、14 六行；12 个 null 上限覆盖 §4 的 3、5、8、9、10、11、12 七行（其中 item5 拆成 3 个 null、item3 拆成 3 个 null、item12 拆成 2 个 null）。⇒ **「Round 2 明确不采纳的数值」没有被代码悄悄采纳。**
3. **历史单位策略**：曾借用通用增长百分比及独立描述长度规则；现行配置不再用这些单位对 Skill 设置自动硬拒绝，保留字节、行数等真实测量能力。
4. **阈值同源防线 1 的落地（历史构建时点运行该只读断言）**：`kd_budget.py --verify-source-lock` 退出码 **0**，输出 `rows_parsed: 14`、`mismatches: []` ⇒ 配置里的 14 行数值仍与 `09` §4 表格逐行相符，`[09:96]` 防线 1（每个预算数字只有一个定义点，且被写入路径与测试同时读取）在代码侧有读侧。`budget-config.json` 的 `authority` 字段亦声明每个数取自 `09` §4 表格行，`verify_source_lock` 在 token/数值不再匹配时拒判（退出码 4）。⇒ 与 `[09:84]` 的「AST 仅 IMPLEMENTATION_DETAIL」不冲突（代码走「单一配置点 + 读侧断言」，未把 AST 当共识度依据）。
5. **历史退出码（不再作为当前指令）**：加载链溢出退出码已删除。现行 `--measure-content` 只统计输入大小，成功返回 0，不再以外部项目硬编码限制拒绝任务。
6. **不一致 / 缺口（只报数，不改任何一方）**：
   - `09` §4 item 13 的 marker 契约在配置里是**顶层 `marker_contract` 对象**，不是 `caps` 成员 ⇒ 它不进 9/12 的计数，也**没有任何上限值可断言**；`--caps` 无法证明 marker 内容被生产（该检查未被预算覆盖）。
   - `09` 第 3 层「advisory 不足整体不渲染」的**次序**在 `ordering` 字段里，但 item 12 的两个上限值为 null ⇒ 代码可执行「放弃」而无法执行「1/2 份额」判定。
   - `budget-config.json` 的 `status` 与 `--deferred` 输出均为 `provisional`，未出现 `final` / `decided`；`must_not_be_cited_as` 列出 `final policy`、`decided threshold`、`evidence-backed constant` ⇒ 与 D09-* 未被关闭的状态一致。
   - 本 `references/*.md` 文件自身**没有预算类别**：`kd_budget.py --check-write` 的 `--class` 只接受 `index_projection | skill_resident | skill_task | skill_description | compiler_prompt | quota_slot`，**无 `reference` 类别** ⇒ 对 R11、R14、R05、R08 这四个 Markdown 而言「上限未预算」（不是通过）。详见交付报告。
