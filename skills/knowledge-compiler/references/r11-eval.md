# R11 — 独立评测与结果判断

判断验证结果能支持什么结论。格式、预算和测试文件只能说明各自检查范围；实际效果需要可复现的执行或独立评测。生成候选的人不能替自己做独立验收。

历史来源： `.distill/round-2/08-EVAL-STRATEGY.md` §1.1–1.6（行 20–68）、§2（行 72–81）、§3 含 §3.2（行 85–109）、§5（行 131–135）、§8 DEFERRED（行 165–171）。生成于 2026-10-06，wave 4。
状态说明：本文供参考；具体行为以 `../scripts/`（`kd_eval_freeze.py`、`kd_eval_score.py`）与 `../schemas/eval-bundle.schema.json` 为准。
引用约定：`[08:N]` = `.distill/round-2/08-EVAL-STRATEGY.md` 第 N 行，行号保留原整理时点的定位。

---

## 阅读导航

- 1. 分层可证伪口径（Tier-0..Tier-4）
- 2. 被否决的口径（6 条，逐条带原因）`[08:74-81]`
- 3. 硬禁令 P-01 .. P-12（全 12 条）`[08:85-103]`
- 待确认与暂缓事项
- 历史源码对照

## 1. 分层可证伪口径（Tier-0..Tier-4）

核心原则原文：**「每一层的能力上限不同，不得跨层借用。结构与预算门只能*阻断*，永远不能*授予 verified*；只有可复现的执行结果或冻结独立 holdout 才能授予。」** `[08:18]`

| Tier | 对象 | 语义 | 能否授予 verified | 出处 |
|---|---|---|---|---|
| **Tier-0** 结构 / 预算门 | 尺寸、增长、非空、frontmatter、schema | **只阻断，不授予**；支撑 `CM-31` + `07:artifact-budget-constraint-gate`、`04:skill-token-budget-gate`、`11:memory-md-budget-projection` 等 | **不能**：「Tier-0 通过**不产生**任何 `verified` 记录」；DD-3 `positions.D` 自陈「作唯一口径会误报通过」；CM-31 无一条证据声称能证「更好」 | `[08:20-24]` |
| **Tier-1** 默认口径 | 重跑那条最初失败的样本并转绿，且测试必须**咬得住**（把被宣称的门删掉，测试必须变红） | 默认口径。EVIDENCE-SUPPORTED（`CM-50`, tier=MUST, consensus_projects=5, needs_llm=False, deterministic_script_candidate=True） | 能（样本可复现时） | `[08:27-29]` |
| **Tier-2** 冻结独立 holdout | **仅限可泛化文本资产**（prompt / Skill 正文 / 指令）的 before/after 裁决；`CM-46` MUST/5P、`CM-40` SHOULD/4P | 能，但**必须带四条前置**（见 §1.2），缺一即无效并退回 Tier-1 或 Tier-4 | 能（仅四条前提全部成立的冻结独立对照；其他情形不授予） | `[08:38-40]` |
| **Tier-3** 确定性廉价代理与 LLM 分 | **只作排序信号**：「永不构成 verified，永不进入晋升记录」 | 确定性代理与模型分只作排序和候选提示，不形成独立可复现结论 | 不能 | `[08:49-51]` |
| **Tier-4** `UNVERIFIED` / `pending-verify` | 无可验证样本时**必须**显式记；**禁止晋升**，**禁止以 README / 报告 / PDF 叙述替代运行证据** | 明确记录没有符合来源和执行要求的可复现实测证据，作为待验证状态 | 不能（但它是合法存储态，不是失败） | `[08:55-57]` |

Tier-1 之所以是默认口径（原文三条理由）：与本编译器的证据模型同构（输入本身就是一条失败）、成本最低、是 Round 1 唯一 MUST-tier 且纯确定性的口径 `[08:36]`。支撑机制：`01:verify-before-persist-heal-loop`、`04:self-tested-reject-fixtures`、`04:mutation-lite-test-proves-bite`（bite 判据的直接原型）、`14:read-before-write-enforcement`、`06:validate-before-write-admission` `[08:31-35]`。

### 1.1 Tier-2 的四条强制前置 `[08:41-45]`

| 前置 | 原文要求 | 出处 |
|---|---|---|
| **(a) 量具分离硬断言** | 裁决所用 metric 的 id **必须 ≠** 循环内优化所用 metric 的 id，且**写成断言而非约定** | `[08:42]` |
| **(b) floor / ceiling 双参照** | 同时报告 `baseline-noop`（floor）与 `oracle`（ceiling）；支撑 `01:floor-ceiling-bench-corpus`（实测 0/3→3/3、0/4→4/4） | `[08:43]` |
| **(c) 最小改进量 + 重复次数 + 容差** | 且**变差即 FAILED / 阻断**（不允许「只警告不阻断」） | `[08:44]` |
| **(d) 泄漏与归因前置** | 新纠正不得只进 train；验收标准（`expected`）不得被静默改写 | `[08:45]` |

成本事实（EVIDENCE-SUPPORTED，来自 `01:skill-ab-trigger-evals`）：一轮实测 tokens **+15322**、时间 **+66.1s** ⇒ **Tier-2 不得作为全局默认口径** `[08:47]`。
LLM-as-judge 只有在同时满足两条时可用于裁决：① 与 (a) 的独立量具配对；② 同屏至少有一个可证伪检查（Tier-1 或 Tier-2）`[08:52]`。

### 1.2 `verified` 落库定义与五元组 `[08:62-68]`

```
verified := Tier-0 ∧ ( Tier-1（若样本可复现） ∨ Tier-2（若为可泛化文本资产） )   [08:65]
```

每条 `verified` 必须携带五元组：**（量具 id、样本/数据集 id、阈值、运行结果、该量具是否同时被用于优化）** `[08:67]`。
原文对第 5 项的定位：「最后一项是本文全部硬禁令的落点：没有它，§3 的所有反例都无法在数据层被检出。」`[08:68]`

Tier-4 与生命周期字段的接口：`validation_state ∈ {pending, verified, unresolved}`；证据缺失或冲突记 `unresolved`，**禁推进 `last_validated_at`、禁把提案当已验证**，review 不是生命周期事件（不加 Recurrence-Count、不刷 Last-Seen）`[08:60]`。

---

## 2. 被否决的口径（6 条，逐条带原因）`[08:74-81]`

| # | 被否决口径 | 否决原因（保留原始数字） | 出处 |
|---|---|---|---|
| 1 | 仅结构 / 预算 lint 即 verified（`positions.D` 单用） | CM-31 无「更好」证据；`07:artifact-budget-constraint-gate` 的门只在最终产物跑一次、按**字符**而非 token 量、frontmatter 不计入 15 KB；误报通过形态由 `generate_report.py:406-411` 把未接线门标 `Implemented` 直接印证 | `[08:76]` |
| 2 | LLM 评分 / GEPA fitness 作唯一裁决（`positions.C` 单用） | judge 零调用（`evolve_skill.py:24` import 后无使用点）、实际阈值 `improvement > 0`（`:287`）、非确定性可翻转结论、模型判分可被长度与措辞欺骗 | `[08:77]` |
| 3 | before/after holdout 作默认全局口径（`positions.B` 无限定推广） | 成本最高（evals × config × N，实测 tokens +15322 / +66.1s）、`01` 的 bench solvers 未落地（README 自认 Spike）、`04` 的 premium 配额会耗尽且模型换代后分数不可比；对可复现 bug 比 Tier-1 贵且不更严格 | `[08:78]` |
| 4 | 以 `> 0` 或「文档说通过」作阈值 / 记录 | `evolve_skill.py:287-291` 的非阻断路径、`README.md:19,26` vs `DEFAULT_CONSOLIDATE=False`、`.evals/cases` 为空，三处共同证明：**以叙述为验证记录会把造假制度化** | `[08:79]` |
| 5 | 把 `proxy-metric-in-loop` 当独立验证口径 / 把 CM-41 整簇与 CM-31 整簇纳入 DD-3 证据主体 | CM-41 主题是成本分层（4/6 成员属预算议题；`15:session-recall-keyword-router` 为 UNVERIFIED/OPTIONAL）；CM-31 主体是上下文预算 | `[08:80]`，剔除义务详见 R14 §5 |
| 6 | 以 survey 材料（worker 13 / CM-21 命中项）支撑任一 Option | SPEC §9 与 §7 缺陷 5：worker 13 = awesome-Self-Improving-Agents **全仓无可执行代码**，不能支撑任何裁决 | `[08:81]` |

---

## 3. 硬禁令 P-01 .. P-12（全 12 条）`[08:85-103]`

适用范围原文：**「以下 12 条为*硬禁令*：候选架构若出现同一形态，直接判 FAILED，不允许「已实现待接入」。」** `[08:87]`
标注含义：`[本轮核实]` = DD-3 本轮源码回读；`[Round 1 记录]` = 仅引用 Round 1 登记的 risks / caveats，本轮未逐行回读 `[08:88]`。

| id | 禁令（原文粗体句转写） | 关键出处（照录路径与数字） | 分类 | 核实标注 |
|---|---|---|---|---|
| **P-01** | 禁止优化目标与 holdout 用同一把尺子。集合独立不等于量具独立；必须有量具 id 不等的断言。 | `evolution/skills/evolve_skill.py:157,170`（`metric=skill_fitness_metric`，优化目标）与 `:217,221`（`baseline_score`/`evolved_score` = 同一函数，验收判据）；`evolution/core/fitness.py:107-136` | 自我证明的评分 | `[本轮核实]` `[08:92]` |
| **P-02** | 禁止 `improvement > 0` 当阈值。阈值不可证伪；变差必须阻断并标 FAILED，不得只打黄色警告。 | `evolve_skill.py:226`（`improvement = avg_evolved - avg_baseline`）、`:287`（`if improvement > 0:`）、`:291`（仅 `[yellow]⚠ Evolution did not improve skill`）；`PLAN.md:79` 显著性检验与 `PLAN.md:289` ≥10% 提升**均未实现** | 阈值不可证伪 | `[本轮核实]` `[08:93]` |
| **P-03** | 禁止用关键词集合重叠 `score = 0.3 + 0.7*overlap` 冒充语义评分。该函数只能作 Tier-3 排序信号。 | `fitness.py:107-136`，源码注释原文 `# Simple keyword overlap as a fast proxy`；`:119` 空判 `return 0.0`；`:136` clamp | 自我证明的评分 | `[本轮核实]` `[08:94]` |
| **P-04** | 禁止把被 import 但零使用的评分器写进架构图 / 报告。`LLMJudge` / `FitnessScore` import 后无使用点即为死量具。 | `evolve_skill.py:24` import 之后除 import 外无使用点；`fitness.py:11-31`（三维加权和 `max(0.0, raw - self.length_penalty)`）、`:95-98` length_penalty；`FitnessScore.feedback` 主路径恒空 ⇒ `README.md:15-26` 宣传的 GEPA 读轨迹**在本仓无数据通道** | 量具与宣称不一致 | `[本轮核实]` `[08:95]` |
| **P-05** | 禁止宣称有测试门而函数零调用点。 | `evolution/core/constraints.py:55-93`（`run_test_suite` 零调用点）；`README.md:71-73`；`autoharness/hook/promoter.py`（`config.py` 注释自认「Tests assert only relationships, never absolute values」，见 RT-12）⇒ README 的「全量 pytest 通过」guardrail 不成立，且 `--run-tests` 写进 `config.run_pytest` 后该字段无读取点，用户显式授权也无法启用 | 量具与宣称不一致 | `[本轮核实]` `[08:96]` |
| **P-06** | 禁止报告数字是被记录对象自己的字面量。报告内的任何数字必须能反查到产生它的调用点。 | `generate_report.py:145,345-347`（明确保留 `0.408 -> 0.569 +39.5%`、`0.374 -> 0.374 0.0%`、`Average 0.391 -> 0.472 +20.7%`）、`:269`（称 `['Optimizer','DSPy BootstrapFewShot']` 而 `evolution/` 代码零出现）、`:371` 叙述；`reports/phase1_validation_report.pdf` 实际存在 | 结果数字非测量产物 | `[本轮核实，归属见 §3.2]` `[08:97]` |
| **P-07** | 禁止未接线的门标 `Implemented`。`Implemented` 只能由「存在调用点」产生；仅设计承诺只能标 `By design` 且不得计入完成度。 | `generate_report.py:406-411`（`Implemented` / `By design` 标签） | 未接线门被当已存在 | `[本轮核实，归属见 §3.2]` `[08:98]` |
| **P-08** | 禁止测试借别人的阈值蹭过（假性通过）。测试断言必须引用被宣称的那个常量；构造值必须相对于**真正生效的门**。 | `autoharness/tests/test_validate.py::test_description_over_length_rejected` 用 `'x'*(SKILL_DESC_MAX_CHARS+1)` = **1025** 构造并断言 `not ok` + family `description`，而真正的拒绝门是 `INDEX_DESC_MAX_CHARS=60`（`src/autoharness/lib/validate.py`；`1024` 只在 `config.py:42` 定义、`README:111` 宣称、测试里作字符串构造）⇒ **1025 > 60 使测试绿，而 1024 语义从未被任何代码路径实现** | 假性通过的测试 | `[本轮核实]` `[08:99]` |
| **P-09** | 禁止以 README 叙述把默认关闭的闭环说成默认全开。默认态必须来自运行时常量。 | `repos/hermes-agent/agent/curator.py:35` `DEFAULT_CONSOLIDATE = False`（`:148` `return bool(_load_config().get('consolidate', DEFAULT_CONSOLIDATE))`）vs `README.md:19,26` 的 `built-in learning loop` / `nudges itself` / `Autonomous skill creation after complex tasks` | 默认态造假 | `[本轮核实]` `[08:100]` |
| **P-10** | 禁止以「机制规格存在」代替「机制运行过」。 | worker-caveats `01.doc_vs_impl_gaps`：README / 外循环宣称 `eval-creator` 产回归用例，实际 `.evals/cases/` **为空**、`EVAL_INDEX.md` 仅表头；`.learnings/` 根目录无 `HEALS.md`。本轮仅静态阅读，未运行任何 eval | 以机制存在代替机制运行 | `[Round 1 记录]` `[08:101]` |
| **P-11** | 禁止验收标准可被静默改写、新纠正永不独立验收。`DO UPDATE SET expected` 改写历史验收；验证集取 `times_applied` 最高一批 ⇒ `times_applied=0` 的新纠正只进 train；`expected` 源自同一条 learning（**用规则证明规则**）。 | `CM-46` + `08:frozen-heldout-correction-evalset` risks（`repos/pro-workflow/src/optimizer/store.ts`、`validate.ts`） | 循环论证 + 标准漂移 | `[Round 1 记录]`（本轮未回读源码逐行核实）`[08:102]` |
| **P-12** | 禁止把「有量具」当成「可证伪」。① gate 以 REGEX 识别 mock 输入 ⇒ 只证明管道与阈值效应，不证明真实语义判别；② 数据集与逐 query 输出私有 ⇒ 评测本身无法在本仓复现，且 `recall_at_k` 用 `sum(hits)/len(gold)` 混合定义与同名指标不同义。另：口径被 CI 脚本局部忽略同样无效——`tests/waza-spec.sh` 只取 `waza check` 的 spec/schema/link 三类 `passed:false`，主动忽略 compliance score 与风格建议并豁免 `disable-model-invocation`。 | `CM-46` + `02:labeled-fixture-scan-eval-gate` risks（`distill/scripts/mock_codex_scan_agent.py`）；`CM-46` + `09:frozen-candidate-rerank-eval` risks（`memsearch/evaluation/README.md` 自陈）；worker-caveats `04.doc_vs_impl_gaps` | 可证伪验证的形式化替代 / 通过范围被缩窄 | `[Round 1 记录]` `[08:103]` |

### 3.1 归属更正（SPEC §9 第 3 条，权威版本，覆盖任务书旧表述）`[08:105-109]`

- 「reports PDF 数字是 `generate_report.py` 里的字面量、未接线的门标 `Implemented`」属 **worker 07 = hermes-agent-self-evolution**，路径 `repos/hermes-agent-self-evolution/generate_report.py:145,345-347,406-411` `[08:107]`。
- **不是 worker 13。** worker 13 = awesome-Self-Improving-Agents，**全仓无可执行代码**，依 SPEC §9 / §7.5 **不能支撑任何裁决**（包括本条反例，也包括任何 Option 的支撑计数）`[08:108]`。
- DD-3 的 `dangling_ref_recheck.additional_attribution_correction` 与本轮独立复核一致：**内容属实、归属错误** `[08:109]`。

### 3.2 与 R14 的边界 `[08:131-135]`

- 「**08 §1.1 Tier-0 与 09 §1.1 是同一批门，但职责不同**：09 决定「门限是多少、在哪一层拒」；08 决定「这个门能不能给出 verified 结论」——答案是不能，只阻断」`[08:133]`。
- 「08 P-06 / P-07（报告造假）与 10 §1.1 是同一失效的两个方向」`[08:134]`。
- 「**单位与阈值数值不在本文**：本文只裁决口径分层，不含任何阈值。DD-3 的 `verified` 定义中「阈值」一项的具体数一律引用 `09-CONTEXT-BUDGET.md` §4」`[08:135]` 这是历史来源的转述，不能用于当前效果判定。

当前边界：R14 / SC10 只规定阅读与产物预算，超限可以阻断，但不能证明效果改善。S16 从独立冻结的 SC09 `prerequisites.c_min_improvement_repeats_tolerance.thresholds` 读取 `min_improvement`、`repeats`、`tolerance`，并核对五元组、独立性和实际结果；不得从预算上限推导评测阈值，缺失阈值不能取得 verified。

---

## 待确认与暂缓事项

`08` §8 的 3 条 DEFERRED，原样转述，**本文件不予关闭** `[08:165-171]`：

- `DEFERRED id D08-1`：`07` 的 `$2-10 per run` 成本区间**仍无代码依据**（实际成本 UNKNOWN）`[08:167]`。
- `DEFERRED id D08-2`：三口径对照样本（Tier-1 重跑 vs Tier-2 holdout vs Tier-0 lint 在同一缺陷上是否一致）**本轮不存在** `[08:168]`。
- `DEFERRED id D08-3`：Round 3 candidate 的主体形态（可复现执行样本 vs 纯 prompt 资产）**未定**，而 Tier-1 的主口径地位依赖该形态 `[08:169]`。
- 另有一条本文自标的非定论判断：「若 candidate 绝大多数是纯 prompt 资产则 Tier-1 失主口径」= ENGINEERING-INFERENCE（依赖 DD-1/DD-7 结论，合流后复核）`[08:151]`。
- `UNKNOWN`：`reports/` 内 PDF 是否与当前 `generate_report.py` 输出一致，仍是 worker 07 的 open_question（因缺 poppler 未渲染核对）`[08:158]`。

## 历史源码对照

以下保留历史构建时点的只读观察（python3 stdlib；当时未运行测试套件），不作为当前覆盖面或本轮验证证明：

1. **verdict 词表确实没有「黄色 / warning」成员**（对应 P-02 `[08:93]`）。`schemas/eval-bundle.schema.json` → `/properties/verdict/properties/status.enum` = `["NOT_RUN","PASSED","FAILED","UNVERIFIED"]`（4 元，无 warning / review / yellow / needs-attention）；`kd_eval_score.py:29` 的模块注释亦声明该枚举是 schema 级强制。**与 Wave 3 的声称一致。**
2. **五元组确实是 schema 必填**。`eval-bundle.schema.json` 顶层 `required` 含 `five_tuple`；`/properties/five_tuple.required` = `["instrument_id","dataset_id","threshold","run_result","instrument_also_optimised_against"]`（5 列，逐条 `[08:67]` 一一对应）；`threshold` 再要求 `["min_improvement","repeats","tolerance"]` ⇒ 与 (c) 前置 `[08:44]` 对齐。
3. **四条前置在 schema 里是四个具名字段**：`a_instrument_separation` / `b_floor_ceiling` / `c_min_improvement_repeats_tolerance` / `d_leakage_and_attribution`，各含 `status ∈ {satisfied, unsatisfied}` ⇒ 与 `[08:42-45]` 的 (a)(b)(c)(d) 命名对应，无缺项。
4. **`verified` 在 schema 里是派生位而非输入位**：`/properties/verdict/properties/verified` 描述为「Computed by kd_eval_score from THIS document's fields, never copied from the bundle」；`kd_eval_score.py:32-36` 亦注明 `08:65` 公式由 `_verified_claim` 实现、bundle 里存了 `verified: true` 会被忽略 ⇒ 与 P-06 / P-07 `[08:97-98]` 同向。
5. **blocking 不变量**：`verdict.required` = `["status","blocking","reasons","verified","regression_detected"]`，`reasons` 为闭合词表且 `minItems: 1`（13 个 reason，含 `regression_vs_baseline`、`below_min_improvement`、`repeats_below_declared`、`self_grading_collision`）⇒ 「FAILED 必带可命名原因」，与 P-02「变差即 FAILED」一致。
6. **不一致项（只报数，两边都不改）**：P-01..P-12 是 12 条禁令，`eval-bundle.schema.json` 只机器化承载其中与 eval bundle 直接相关的形态（P-01/P-02/P-03/P-12 的判据位）。P-04、P-05、P-06、P-07、P-08、P-09、P-10、P-11 在本仓库**没有对应的 schema 字段或脚本检查点**（历史构建时点在 `scripts/` 与 `schemas/` 内 grep `Implemented`、`DEFAULT_CONSOLIDATE`、`INDEX_DESC_MAX_CHARS`、`times_applied`、`expected` 改写位均无命中的强制实现）。这与 `05` §2.1 D5 与 `08` §1.5 的口径不冲突（禁令是判 FAILED 的裁决依据，不是必须逐条落 schema 的字段），但如实登记为覆盖面差。
