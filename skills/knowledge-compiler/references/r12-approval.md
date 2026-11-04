# R12 — 审核与批准入库

候选要进入正式知识库时，按项检查证据、适用范围、独立评测和人工批准。目录中的阅读顺序不能替代写入顺序；执行前以当前脚本和入口 §2.2 为准。

历史来源： `.distill/round-2/06-PROMOTION-POLICY.md` §1（行 26–50，主干与节点计数表）、§3（行 135–172，Stage 1）、§4（行 175–205，Stage 2）、§5 + §5.1（行 209–272，Stage 3 与落点），生成于 2026-10-06，wave 4. Citation prefix: `06:` = `.distill/round-2/06-PROMOTION-POLICY.md`，`04:` = `04-DETERMINISTIC-VS-LLM.md`，`07:` = `07-LIFECYCLE-POLICY.md`。
状态说明：本文供参考；具体行为以 ../scripts 为准（本树的执行者是 `kd_gate_tree.py` 的 `NODE_TABLE`/`EDGE_TABLE` 与 `kd_gate.py`/`kd_human_gate.py`）。
范围切分：**Stage 0（N00–N09b，八诊断 D1–D8）不在本文件**，在 R10 `r10-diagnose.md`；本文件只在 §1 主干里保留它的位置。 `[06:30]`

---

## 阅读导航

- 1. 主干、全局不变量与节点计数
- 2. Stage 1 — 确定性准入（A'；模型在此 Stage 无裁决权） `[06:135]`
- 3. Stage 2 — 惰性候选隔离（C 的实现要求：漏一项即退化为无效检查） `[06:175-177]`
- 4. Stage 3 — 按写入风险分层的人工确认 + 唯一写事务 `[06:209]`
- 5. 终态落点（10 个，含两个「什么都不做」变体） `[06:256]`
- 6. 待确认与暂缓事项
- 7. 历史源码对照

## 1. 主干、全局不变量与节点计数

```text
ENTER(candidate)
 └─ STAGE 0  FAILED_RULE 前置路由          ← 必须先于任何阈值计数   [06:30]
     └─ STAGE 1  确定性准入                                          [06:31]
         └─ STAGE 2  惰性候选隔离                                    [06:32]
             └─ STAGE 3  按写入风险分层的人工确认                    [06:33]
                 └─ TERMINAL（动作 × 落点）                          [06:34]
```

三条不可协商的全局不变量（承 `04` §1 的 I-1/I-2/I-3）： `[06:14-19]`

```text
P-1  模型无写权。任何节点的模型输出只能进入 Stage 2 的候选文件，不得触盘常驻层。 [06:17]
P-2  approve 与 apply 是同一个事务。不存在「已批准但未落盘」或「已落盘但未批准」的中间态。 [06:18]
P-3  门挂在唯一写路径上。若存在第二条写路径（含 --apply-json / 直接写文件 / agent 自写页面），本树全部失效。 [06:19]
```

P-3 **不是修辞**：DD-1 立场 B 的 failure_modes[0] 实测 `02` 的 JSON 路径无等价门，且 distill 自己的 `AGENTS.md` 建议优先 JSON 流；因此 P-3 是实现阶段的**验收项**，不是设计声明。 `[06:22]`

判定者图例：`[DET]` 确定性代码 · `[LLM]` 便宜模型（只产提案，无写权） · `[JUDGE]` 强模型（仅不可调和） · `[HUMAN]` 人工门。 `[06:13]`

**计数规则**（原文，避免口径漂移）：节点 = 带**判定者**与**可判定条件**的分支点（含子节点 N\*a/N\*b）；`D1–D8` 是 Stage 0 的**条件维度**，其路由实现为节点 `N01–N08`，不重复计数；分支 = 节点出边。 `[06:39]`

| Stage | 节点区间 | 节点数 | 分支（出边）数 | 引用 |
|---|---|---|---|---|
| Stage 0：入口 + 八诊断路由 | `N00`；`N01–N08`（对应 D1–D8）；子节点 `N05a N05b N06a N06b N07a N08a`；`N09` `N09b` | **17** | **36（现行）**：历史 35 + `N00.lifecycle_requested`；`N03` 也有 3 出边 | `[06:43]`（历史 35） |
| Stage 1：确定性准入 | `N10–N18` | **9** | **19**（`N18` 为 3 条落点类别；其余各 2 条） | `[06:44]` |
| Stage 2：惰性候选隔离 | `N19 N20 N21 N22 N22b` | **5** | **9** | `[06:45]` |
| Stage 3：风险分层与写前意图 | `N23–N28` | **6** | **12** | `[06:46]` |
| 终态落点分派 | `N29` | **1** | **11**（10 个必需落点，其中「什么都不做」分 `L-NOTHING` / `L-NOTHING+账` 两个物理出口） | `[06:47]` |
| **合计** | — | **38 个节点** | **87 条分支**（历史 86；当前代码新增 N00 入口） | `[06:48]` |

全部 38 个节点均给出可判定条件 + 判定者；现行 `EDGE_TABLE` 为 **87 条分支**（Round 2 原始设计为 86）。现行全部分支终止于 §5.1 的 11 个落点之一或一个显式拒绝出口（无悬空分支）。Stage 0 的六个处置动作（MOVE / UPDATE / MERGE / AUTOMATE / SUPERSEDE / DELETE）**不是落点**，它们复用 §5.1 的落点集合，故不另计出口。 `[06:50]`

## 2. Stage 1 — 确定性准入（A'；模型在此 Stage 无裁决权） `[06:135]`

```text
N10 [DET] scope 合法且非空？（05-DATA-MODEL §5.3 的 S1 fail-closed）                    [06:138-140]
      no → EXIT: 拒绝入库 + 写 lifecycle_event(actor=?, reason 无) → L-NOTHING
      理由：02 的 cohort_key/project 算了无消费者 → 跨项目语料上开门（DD-6 重开条件 5 必须先修）
N11 [DET] identity L0 canonical key 可解析？                                            [06:141-142]
      no → **本裁决重开**（见 §7 依赖条款）。禁止降级为「用模型产出的 key 继续」。
N12 [DET] refs_integrity 无悬空引用？（可重跑 auditor，fail-on-unresolved）              [06:143-144]
      no → quarantine（不产提案、不计数）→ L-NOTHING + failed 账
N13 [DET] 全部 evidence_refs resolver 通过 + 至少一条 runner 写入的 PASS？（05 §2.1 D2）  [06:145-146]
      no → 不得晋升为 MUST/常驻层条目；降级为 reference → L-NOTHING（保持 Pattern 计数）
N14 [DET] support_count >= MIN 且满足单调重试条件？                                      [06:147-151]
      可判定条件：matches.len() > last_attempted_count
      —— 即重试必须是**新增第 N+1 条证据**，而不是时间流逝。 [E] distill/src/scanner/state.rs:161 + :194,206 .max(count)
      参照常量：MIN_WORKFLOW_MATCHES_FOR_PROPOSAL = 3（engine.rs:125，用于 :1128/:1347）
      no → 保持 candidate 计数，EXIT → L-PATTERN
N15 [DET] distinct_occurrence_count >= 最小独立来源数？（按 scope 去重后）                [06:152-156]
      反例（必须挡住）： [E] CM-36 05:layered-global-project-scan —— scan-skills.sh:91-114 用 jq -s 'add'
      拼接全局层与项目层、无去重、条目无 layer/source 字段 → 同一 skill 的两份副本把 1 个来源伪造成 2+；
      以及 DD-1 F4「05 无最小时间/任务跨度约束，一次安装 20 个同源 skill 即满足 2+」
      no → L-PATTERN（只计数，不产提案）
N16 [DET] 最小任务/时间跨度门：来源跨越 >= 2 个 distinct task 且 >= 1 个非本次会话？      [06:157-160]
      no → L-PATTERN。理由：同一次安装/同一轮批量导入不构成复发。
      参照 [E] CM-17 01:canonical-occurrence-aggregation：不同路径 ≠ 独立证据；legacy 无 provenance 时
      unknown-lineage 合计最多算 1 个 distinct task，且有对应 eval（「legacy provenance 不能证明 2 distinct tasks」）
N17 [DET] 到期门：input digest 未变 或 min_interval_hours 未过？                          [06:161-164]
      yes（未到期）→ 整条管线不进入，模型 0 次，EXIT → L-PATTERN
      [E] 09:due-gate-input-digest-and-lock（memsearch/src/memsearch/maintenance.py::_input_digest,
      _is_due, _file_lock O_CREAT|O_EXCL, _record_failure_state：失败不写 digest → 下轮自动重试）
N18 [DET] 机械可判性预判 → 决定 Stage 3 后的落点类别                                      [06:165-168]
      可判定条件：该 candidate 的谓词是否可在 CI/hook 里当场求值（是→L-TEST/L-LINT/L-SCRIPT；
      否但可断言结构→L-EVAL；纯行为约束→L-RULE/L-SKILL）
      依据 [E] 04 的 Promote tiers（取最高能兜住的一层）+ D4 判据。
```

Stage 1 的已知天花板（原文，「不许假装它不存在」）：DD-1 立场 A 的 F7「确定性是局部事实：门确定但输入身份不 canonical、上游清单不去重、部分实现根本不执行阈值（`05`/`09`），端到端确定性不成立」。本树用 N10/N11/N13/N15 四道门分别封堵 F3/F2+F7/F1/F4；**N13 的 PASS 要求是封堵 `09` 型「有代码库却没执行阈值」的直接对策**。 `[06:171]`

`N14` 的 `MIN = 3` 是**参照常量**（`engine.rs:125`），不是本树裁决出的配置值；`N15`/`N16` 的最小独立来源数与最小跨度均只给出判据、未给出数值 → `DEFERRED id DD-1-sub01..sub08 未覆盖该三项；历史构建时点观察由 `kd_gate_tree.py` 的 `requires` 字段承载，数值权威在配置 Owner`。本文不补数值。 `UNKNOWN（06 未写数值）`

## 3. Stage 2 — 惰性候选隔离（C 的实现要求：漏一项即退化为无效检查） `[06:175-177]`

DD-1 立场 C 的 failure_modes[0] 原文：**「实现成本最高且漏一项即退化为无效检查：`15` 的五要素（pending storage + artifact hash + 冲突拒绝 + approve/apply 同事务 + Rejected 与 Failed 分离记账）任一缺失，C 退成 B 或 A」**。本 Stage 的五要素逐一对应节点。 `[06:177]`

```text
N19 [DET] 写候选文件到 inert store：_pending/<id>.md + sha256 + artifact hash（五要素 1+2）   [06:180-186]
      [E] 15:auto-improve-proposal-state-machine（AutoImproveProposalStatus/approve/reject/fail，n_ev=6，
          form=runtime-enforcement，簇内最强）；CM-32 09:git-backed-inert-candidate-store
          （memsearch/src/memsearch/skills.py::skills_root/_git_blob_hash/_pending_reason/list_candidates，
          code_reuse=direct —— 候选天然躺在 git 里，未生效即可 diff）；CM-32 07:evolution-output-quarantine-directory
      未闭合（如实记，DEFERRED-2 见 §6）：15 的 _pending/ 文件被人工编辑后 sha256 失配的处理路径未读到
                                      （worker-caveats 15）。本树要求：失配 → fail-closed 拒绝 apply + 写 failed 账。
N20 [DET] 同 target 已有 pending → 拒绝新建（冲突拒绝，五要素 3）                              [06:187-189]
      已知副作用 [E]：「15 同 target 已有 pending 即拒会挡掉合法连续修正」。
      处置：不放宽为覆盖；改由 lifecycle_event 记 suppressed_by_pending，人工可读。
N21 [DET] 幂等与水位：per-item 幂等水位（防重放）+ 提案文件有过期通道（防无界堆积）              [06:190-194]
      必须修的已知缺陷 [E]：02 的 proposed=true **无 reset 路径**、scan-state.json **无 cap/compaction/GC**、
      record_session_findings 整份覆盖可丢证据（F5）；02/15 的 snooze/quit 只丢内存选择、提案文件永久留盘无过期；
      07 的 evolved_FAILED.md 不带 timestamp 会覆盖最有信息量的失败样本、output/ 未进 .gitignore。
      并发 [E]：06 队列无跨进程锁、无 per-item 幂等水位，promoter docstring 自认 whole-run clear 有重放窗口。
N22 [DET] Rejected 与 Failed 分离记账（五要素 5）+ 被拒留痕（反沉默）                           [06:195-201]
      [E] 15：AutoImproveProposalEvent / rejected_candidates_json / AutoImproveTelemetry.rejected_targets；
             06:run-account-anti-silence（被拒绝的提案必须留痕，否则操作者以为管道在工作）；
             11:governed-sleep-proposal-ledger（proposals/_caps/decide/_apply/_commit + DecisionLedger；
             tests/redteam/test_poisoning.py::test_a_captured_reasoner_is_bounded_by_the_menu_and_the_per_sleep_cap）
      rejected = 人的决定，**无新证据不得再提**（防重复提交与假成功）；failed = 尝试出错，可重试。
      语义差别是决策性的 [E]：worker-15 核查原文记录 Failed 与 Rejected 分离且 rejected_targets 可查询。
N22b [LLM] 唯一允许的模型介入点：为已达标候选生成 draft + 建议 tier + 把 size 报出来            [06:202-204]
      约束：P-1 模型无写权；draft 必须是**可执行断言的候选**，不得只是给人读的散文
      反例 [E]：DD-1 立场 B 的 failure_modes「批准≠正确：05 的 draft 是给人读的散文而非可执行断言，批准后无回归/eval」。
```

`N19` 的 sha256 失配处理路径在 Round 2 即记为未闭合（`UNKNOWN`）→ `DEFERRED id DD-1-sub02`（对应 `06` §6 的 DEF-2） `[06:185]` `[06:282]`

## 4. Stage 3 — 风险分层、写前验证与 S12 唯一事务准备 `[06:209]`

```text
N23 [DET] 该动作是否触碰常驻层（AGENTS.md / CLAUDE.md / rules / skills / 项目文档）？   [06:212-213]
      no → N24   yes → N25
N24 [DET] 历史 R0 三条件（现行满足时也拒绝无人权威提交）：                                   [06:214-223]
      (a) 机械可判定  (b) 可逆  (c) 幂等，且不越 ownership 边界（只动 self-authored 条目）
      历史来源 [E]：11 的 T0 仅对可逆、幂等的归一化自动写盘；删除仍需人工 gc（`test_gc_is_the_only_road_to_physical_removal`）。这曾支持 R0 的设计，但当前 S12/G1 **不采纳无人权威写入**；R0 保持未启用。
      yes → R0（历史设计分支；当前实现一律 DEFERRED/REFUSE，不得进入 N26/S12）
      no  → R1/R2 → N25
N25 [HUMAN] 人工确认（B 收敛到此层；按写入风险分三档）                                   [06:224-242]
      R1 常驻层写入（Project Rule / Global Rule / Skill）→ 人审，且逐条 verdict（不糊批）
      R2 不可逆（任何 delete、以及会销毁内容的 merge）→ 人审 + 确认 flag 是契约本身 + 门票与 grace（见 07）
      分层依据 [E]：14 的 attended/unattended 对 actor 采用 fail-closed（skill_provenance.py / skill_manager_guards.py / write_approval.py）；02 的 remove 需确认（review/mod.rs）。
      四项已观察到的失效 [E]：
        · 审批疲劳（05/08/04）：可批量确认，但必须保留每条 verdict（CM-27）。
        · 审批不落盘（05/03）：approve 必须与 lifecycle_event 原子入账（N22）。
        · 假强制（08：require_approval/auto_update_claude_md 无读取点）：没有真实调用点就拒绝。
        · 05 全量注入造成静默截断，Already Covered 误判（worker-05.md:293）：注入预算由确定性层强制（04 #19）。
N26 = staged intent only [DET]：校验准入并生成提交意图束；本节点**不**执行原子权威写入。真正的 S12 先核验 N28/S16、G1、来源事实，再由唯一 Writer 原子写入，ledger commit point 最后持久化。 [06:243-246]（历史写序目标）
      [E] 06:validate-before-write-admission（repos/autoharness/src/autoharness/lib/validate.py,lib/skills_guard.py：
          唯一写者/写序/escape 预检/absorbed_into）；CM-23 atomic-write-transaction（MUST/DET_ONLY，strongest
          11:write-path-lock-and-stale-write-guard runtime-enforcement）；15 不变量 #10 原子写、#3 索引同事务
N27 [DET] 检查 approve/apply 组合证据，返回 intent_ready 或 intent_incomplete（不再把暂存意图误报 committed/rolled_back）；S12 唯一 Writer 才将批准和 apply 在同一事务落盘。 [06:247-249]
      [E] 15:auto-improve-proposal-state-machine#approve(同事务 apply)；
          该形态必须与记录缺失同样 fail-closed（Agent 11 的 ADD.rollback 原文）
N28 = before S12 commit [DET]：独立 S16 先核验冻结 Eval 和主体绑定；没有受信回执即拒绝生产提交。 [06:250-253]
      付费运行前仍要求 dry-run preflight，真实宿主 Eval 不可由本节点假造。
      [E] CM-48 regression-eval-for-promoted-rule（01:promoted-rule-eval-regression, 07:root-cause-regression-test-trio,
          04:mutation-lite-test-proves-bite）、CM-40 before-after-holdout-verdict、CM-45 07:dry-run-preflight-for-paid-runs
```

提交后的额外回归只属于 **after commit, not the first independent Eval**；不能把补充的后置检查拿来替代 N28 的写前验证。

当前**权威生产写入绝不允许无人值守**：N24 的 R0 仅保留为未启用的历史设计分支；`kd_gate_tree._ev_n24` 在三条件都满足时也 fail-closed（`DEFERRED id DD-1-sub01`/`DD-1-sub03`）。若未来裁决纯本地、可逆、非权威维护操作，必须另列其 Owner 与门禁，不能由 R0 自动获得 S12 提交权。 `[06:300]` `[06:302]`
N25 的 R1/R2 具体边界（哪些 intent 类型需要确认）→ `DEFERRED id DD-1-sub07`（DEF-7） `[06:306]`
N26 的碰撞分支（候选 slug 与人工同名时的覆盖/拒绝语义）→ `DEFERRED id DD-1-sub06`（DEF-6） `[06:305]`

## 5. 终态落点（10 个，含两个「什么都不做」变体） `[06:256]`

下表保留 Round 2 的用途与人工分类，不是当前写入授权表。所有权威写入（包括 ARCHIVE/RESTORE）仍须新的 S16 PASSED、G1 逐项批准与 S12 三通道绑定回执；表中“否”不能批准无人值守提交。当前可运行边界见 R02 §8 与 R16 §5。

| 终态 | 何时落这里 | 写入者 | 是否需要人工 | 引用 |
|---|---|---|---|---|
| **`L-PATTERN`（Pattern）** | N14/N15/N16/N17 任一未达标：**只累计数、只留身份，不产提案、不落常驻层** | `[DET]` | 否 | `[06:260]` |
| **`L-NOTHING`（什么都不做 · 静默）** | N18 判定「默认值已能解决」或「无具体场景」；04 的 Candidate 规则原文：**`Name who hits this again, in which file, on what change. No such scenario, nothing to propose.`** `[E]` | `[DET]`/`[LLM]` | 否 | `[06:261]` |
| **`L-NOTHING+账`（什么都不做 · 留痕）** | N10/N12/N13 拒绝、N06b/N05b 判不出、Stage 3 suppressed：**必须写 lifecycle_event，不得沉默消失**（`06:run-account-anti-silence`）`[E]` | `[DET]` | 否 | `[06:262]` |
| **`L-SCRIPT`（Script）** | D4/N18 判「可在 CI 当场求值且需要副作用」→ 出可执行脚本 | `[DET]` 写，`[LLM]` 提案 | R1 | `[06:263]` |
| **`L-LINT`（Lint）** | D4/N18：机械可判的静态谓词（结构/命名/字段存在），**不锁措辞**（04 §7.4）`[E]` | `[DET]` | R1 | `[06:264]` |
| **`L-TEST`（Test）** | D4/N18：行为断言可写；D7 命中且「规则已在场仍被违反」→ 把规则降为断言；必须能识别原缺陷（`04:mutation-lite-test-proves-bite`）`[E]` | `[DET]` | R1 | `[06:265]` |
| **`L-EVAL`（Eval）** | N18 纯行为约束但可测：晋升规则的题面 + before/after holdout；零 LLM 时只跑结构断言并如实标 `eval_status: partial` `[E]`（CM-46/CM-48） | `[DET]` 冻结语料，`[LLM]` ◐ 题面 | R1 | `[06:266]` |
| **`L-SKILL`（Skill）** | Stage 0 偏好序落到 create 且 born-as-umbrella；或 MOVE/AUTOMATE 的落点是文档层 `[E]`（CM-61 投影 + CM-22 umbrella） | `[DET]` 唯一写者 | **R1**（删除性归并升 R2） | `[06:267]` |
| **`L-RULE-PROJECT`（Project Rule）** | scope=project 且 N16 通过：repo-specific 内容判据 `[E]`（Agent 11 的 ADD 前置：目标 scope 由内容判据决定，repo-specific→project） | `[DET]` | **R1** | `[06:268]` |
| **`L-RULE-GLOBAL`（Global Rule）** | scope=global：用户/团队**standing 偏好**（技术选择、代码风格、个人约定）；门槛高于 project（常驻层 × 跨仓影响）`[E]`（`repos/ai-memory/AGENTS.md` §When you write a project rule） | `[DET]` | **R1 + 显式第二人门**（本文 `[I]`：无参考项目实现「project/global 双档人工」，仅由 DD-1 的「常驻层写入需人」+ B 的层级划分外推） | `[06:269]` |
| **`L-ARCHIVE`（Archive）** | 淘汰路径的自动上限；以及 SUPERSEDE/MERGE 的旧条目离场位（**永不 delete**）`[E]`（CM-55 14:curator-…，`never deletes — archive is the maximum`） | `[DET]` | 否（可逆） | `[06:270]` |
| **`L-MOVE / L-UPDATE / L-MERGE / L-AUTOMATE / L-SUPERSEDE / L-DELETE`** | Stage 0 的六个处置动作；其**落点**仍是上面十项之一（MOVE→改 scope/位置；MERGE→伞形条目；AUTOMATE→L-TEST/L-LINT/L-SCRIPT；DELETE→只产提案，走 R2，见 07） | `[DET]` 执行 | MERGE/DELETE 升 R2 | `[06:271]` |

`L-RULE-GLOBAL` 的「R1 + 显式第二人门」在 Round 2 自标为 `[I]`（ENGINEERING-INFERENCE），无参考项目实现支撑 → 不得当作已证实策略。 `[06:269]`

## 6. 待确认与暂缓事项

- Stage 0 全部节点（N00–N09b）与 D1–D8 判据 → 不在本文件，见 R10。 `[06:54]`
- `06` §6 的 8 项 DEFERRED（DEF-1..DEF-8）逐条对应本树节点：DEF-1→N25 的 R0/R1 分界、DEF-2→N19/N26/P-3、DEF-3→N24 的 (a)(b)(c)、DEF-4→整树、DEF-5→N11、DEF-6→N26 的碰撞分支、DEF-7→N25、DEF-8→N17。 `[06:298-307]` Registry id 映射：`DEFERRED id DD-1-sub01 … DD-1-sub08`（`.distill/round-3/DEFERRED-PARAMETERS.yaml` 已核对该 8 条 parameter 文本与 `06:280-293` 逐条一致）。
- `06` §7 的 REROOT 条款（若 DD-2 定案为「确定性 canonical 身份不可得」→ N11 无法成立 → Stage 1 整体失效 → 本裁决必须重开）仍未消解，残余风险由 DEF-5 承担 → `DEFERRED id DD-1-sub05`（DEF-5）/ 重开条件 `DD-1-sub13`。 `[06:316-323]`
- N14 的 `MIN=3`、N15/N16 的最小来源数与跨度、N17 的 `min_interval_hours` → Round 2 只给判据与参照实现常量，未给本项目的配置数值 → `UNKNOWN（06 未裁决数值，本文件不填）`。 `[06:150]` `[06:152]` `[06:157]` `[06:161]`
- 另有三项参数缺口同域列在 `04` §9（D6-a/b/c），`06:309` 明文「不在此重复计入」。

## 7. 历史源码对照

对照对象：`../scripts/kd_gate_tree.py` 的 `NODE_TABLE` / `EDGE_TABLE`。计数由历史构建时点自行推导（`collections.Counter` 按 `node['stage']` 与出边 `e[0]` 归属统计），非引用代码注释。

| Stage | 06 节点数 `[06:43-48]` | NODE_TABLE 实测 | 06 分支数 | EDGE_TABLE 实测 |
|---|---|---|---|---|
| 0 | 17 | 17（N00,N01–N08,N05a,N05b,N06a,N06b,N07a,N08a,N09,N09b） | 35 | **36**（新增 `N00.lifecycle_requested`） |
| 1 | 9 | 9（N10–N18） | 19 | 19 |
| 2 | 5 | 5（N19,N20,N21,N22,N22b） | 9 | 9 |
| 3 | 6 | 6（N23–N28） | 12 | 12 |
| 终态分派 | 1 | 1（N29） | 11 | 11 |
| **合计** | **38** | **38** | **86（历史）** | **87（当前）** |

- 3 出边节点：历史 `06` 声明 `N03`、`N18` 为 3 条；当前 `N00=3`（多出 `lifecycle_requested`）、`N03=3`、`N18=3`；`N22b=1`。因此 86→87 是一个明确的 Stage 0 扩展，不是测试统计错误。
- 判定者分布（代码侧，`06` 未给总数）：`NODE_TABLE` 的 `judge` 计 DET 29 / LLM 7 / JUDGE 1 / HUMAN 1 = 38。人工门 = 1 个节点，与 `04:69`「同一个人类闸门」及 `06` N25 单点一致。
- 落点集合：`kd_gate_tree.LANDINGS` 实测 11 项 = `L-PATTERN, L-NOTHING, L-NOTHING+LEDGER, L-SCRIPT, L-LINT, L-TEST, L-EVAL, L-SKILL, L-RULE-PROJECT, L-RULE-GLOBAL, L-ARCHIVE`；N29 出边实测 11 条一一对应。与 `06` §5.1 的「10 个必需落点 + 『什么都不做』两个物理出口」= 11 个终态目标一致。
- 命名差异（非数值差异）：`06` 写作 `L-NOTHING+账`（`[06:262]`），代码与 SC12 词汇写作 `L-NOTHING+LEDGER`。同一落点两种拼法；本文件按 Round 2 原文保留「+账」，读代码时按 `L-NOTHING+LEDGER` 检索。
