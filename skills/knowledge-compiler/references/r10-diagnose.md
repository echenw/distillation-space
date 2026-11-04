# R10 — 诊断已有规则的问题

已有规则没有解决问题时，先找原因，再决定修订、合并、停用或补充。不要默认再加一条规则。这里列出八种诊断，后续正式审核见 R12。

历史来源： `.distill/round-2/06-PROMOTION-POLICY.md` §2（行 54–131，含 §2.1 八诊断表与 §2.2 诊断→动作映射与硬禁令）+ `.distill/round-2/07-LIFECYCLE-POLICY.md` §2.1（行 131–146，MOVE/AUTOMATE 是受限特例）+ `.distill/round-2/ROUND2-SPEC.md` §6（行 115–127），生成于 2026-10-06，wave 4. Citation prefix: `06:` / `07:` / `SPEC:` = 上述三文件的行号。
状态说明：本文供参考；具体行为以 ../scripts 为准（Stage 0 的执行者是 `kd_gate_tree.py` 的 `N00–N09b` 节点行与 `kd_gate.py` 的 exit-2 契约）。
范围切分：Stage 1/2/3 与终态落点在 R12 `r12-approval.md`；本文件只覆盖 Stage 0 与它派生的两个受限动作。

---

## 阅读导航

- 1. 来源要求（为什么必须先跑诊断）
- 2. 入口节点与硬禁令
- 3. 八种诊断：4 种可确定性判定 + 4 种需模型判定 `[06:69]`
- 4. 诊断 → 处置动作的映射（禁止 ADD NEW RULE 作为默认出口） `[06:84]`
- 5. MOVE 与 AUTOMATE：FAILED_RULE 派生的**受限特例**，不是第 9/10 个动作 `[07:131]`
- 6. 待确认与暂缓事项
- 7. 历史源码对照

## 1. 来源要求（为什么必须先跑诊断）

派发方硬要求：Candidate 所代表的问题若**已有 Rule / Skill**，禁止默认 `ADD NEW RULE`，必须转入 Rule Failure Analysis，分析维度 `[SPEC:117-121]`

```text
not loaded | wrong trigger | wrong scope | ambiguous | conflicting instruction
| ignored | not mechanically enforceable | outdated
```

再决定 `UPDATE | MERGE | MOVE | AUTOMATE | SUPERSEDE | DELETE`。「这条必须体现在 `06-PROMOTION-POLICY.md` 与 `07-LIFECYCLE-POLICY.md` 的设计里。」 `[SPEC:125-126]`

为什么在阈值计数之前：SPEC §6 + DD-1 明文。若 candidate 所代表的问题已有 Rule/Skill，先计数再发现重复 = 用一次误晋升换一条冗余规则；而 `06:reflector-compare-first-reconcile` 的 F1 duty 原文把这件事定性为缺陷而非贡献：**`A new skill that silently duplicates or opposes an old one is a defect, not a contribution.`** `[E]` `[06:56]`

## 2. 入口节点与硬禁令

```text
N00 [DET] 该 candidate 的问题是否已有 Rule / Skill / Doc 覆盖？                        [06:59-66]
    可判定条件（三条同时成立才算「已有」）：
      (a) identity L0 等值命中或显式 Pattern-Key 相同（见 05-DATA-MODEL §5.1）
      (b) scope 谓词命中（路径片段 / applyTo glob / level ∈ {project,global} 一致）
      (c) trigger 锚点集合非空交集（hook 配置可枚举：PreToolUse(Skill)、PreToolUse(Read)、
          on_session_start、on_stop、CLI 启动 / gateway housekeeping / ticker）
    yes → 进入 D1..D8 八诊断，禁止 ADD
    no  → 跳到 Stage 1（N10）
```

**Stage 0 的一条硬禁令（写进实现验收）**：任何实现若能在未跑 D1–D8 的情况下产生 durable 写，即违反本树。`06` 的 reflector 是**先比较再 reconcile**，其唯一允许动未接触技能的情形是两个既有技能明显同类 → 更宽者吸收 + 更窄者 delete 且**必须带 `absorbed_into=幸存名`**。 `[E]` `[06:131]`

## 3. 八种诊断：4 种可确定性判定 + 4 种需模型判定 `[06:69]`

**执行顺序即优化**：先跑四个 `[DET]` 诊断（零模型成本），任一命中即定型并路由；四个全落空才跑四个 `[LLM]` 诊断。八种全部落空才允许 ADD。 `[06:71]`

| # | 诊断 | 判定者 | 可判定条件（signal） | 证据 | 引用 |
|---|---|---|---|---|---|
| **D1** | `not loaded` | **[DET]** | 该 rule/skill 的路径**从未出现在读/注入账本**（`use`/`view` 计数与 `last_viewed_at` 为空）；或装配层可直接判定文件根本不在加载集 | `[E]` `14:curator-deterministic-inactivity-lifecycle`（`repos/hermes-agent/tools/skill_usage.py` 的 use/view/patch 与 `last_*_at`）；`14:read-before-write-enforcement`；`repos/ai-memory/AGENTS.md` §When you write a project rule —— 同一份 `AGENTS.md` 在只读 `CLAUDE.md` 的宿主里从未被载入，需要一个 `@AGENTS.md` 导入行，否则规则在 session start 缺席 | `[06:75]` |
| **D2** | `wrong trigger` | **[DET]** | 触发描述里**只有周期/频度词而无事件锚点**。判据原文：**`Periodically is not a trigger an agent can act on; the file being open is.`** 事件锚点集合由 hook 配置枚举；「该事件在失败发生的那次会话里是否出现过」在有事件账本时是确定性 join | `[E]` `04:prune-on-open-audit`（`repos/agent-skills/skills/agents-md/SKILL.md`）；`06:use-view-patch-split-instrumentation`（`hook/dispatch.py`）；`14:curator-…` 的 trigger 段列出四个真实锚点 | `[06:76]` |
| **D3** | `wrong scope` | **[DET]** | 失败样本的文件路径/项目**不匹配**规则声明的作用域字段（路径片段谓词或 `applyTo` glob）；反向信号同样可判：候选与现有条目的 `level`（project/global）归属不一致 | `[E]` `05:archived-rules-exclusion`（`scan-rules.sh`）+ 其 risks：谓词是**路径片段而非 frontmatter 状态字段**，命名不一致（`archived/` vs `_archived/`）会让谓词**静默失效** → 谓词必须带自检；`06:reflector-compare-first-reconcile`（level 判据写成内容判据）；CM-27 `Too Specific` 下沉通道 | `[06:77]` |
| **D4** | `not mechanically enforceable` | **[DET]** | 该 rule id 是否绑定 `assert`/`lint`/`type`/`test`。静态判据：**阈值字面量只出现在提示文本、而不出现在 config 常量或测试断言 → 判定为未强制** | `[E]` `01:decay-type-maintenance-contract` risks 原文「无脚本强制全靠 agent 纪律」；`14:umbrella-consolidation-distillation-pass` —— prompt 里的「SKILL.md body over ~24k chars 即归并目标」与「fewer than 10 archives 说明停太早」在代码里**没有对应常量或断言**（worker-14 doc_vs_impl_gaps），且该下限会**施压制造假归并**，移植时不可当阈值；`repos/agent-skills/AGENTS.md` §Prevent Recurrence 的 Promote tiers | `[06:78]` |
| **D5** | `ambiguous` | **[LLM]**（DET 仅预筛） | 需读上下文才能判「这句话是否覆盖本场景」。确定性预筛：同一 identity key 下存在 **≥2 条 active 条目**、或触发词被描述窗口截断吃掉（14 侧 60/57 字符窗口**是可判定的**） | `[E]` `05:six-verdict-merge-router`（`repos/ECC/skills/rules-distill/SKILL.md`，`Already Covered` 明确包含即使措辞不同）；切分标准原文：「脚本能穷尽且无歧义得到 → 脚本；需读上下文才能判 → LLM」 | `[06:79]` |
| **D6** | `conflicting instruction` | **[LLM]** + `[JUDGE]`（不可调和时） | 确定性只能抓**同形重复**；真矛盾必须模型判。第一轮唯一诚实的做法是**显式暴露而非静默解决** | `[E]` `10:auto-forget-ttl-contradiction`（`agentmemory/src/functions/auto-forget.ts`）把 `Jaccard>0.9` 当冲突弃旧，其自身 risks 明写「高相似 ≠ 矛盾」，语义相反的两句 Jaccard 通常很低检不到，概念索引使跨概念冲突漏检；`14:trust-weighted-fact-store-feedback-and-decay` 的 `contradiction_score=entity_overlap*(1-content_sim)` 依赖英文实体正则，CJK/命令行文本命中率低；`15:ttl-pinned-priority-and-forget-sweep`（`crates/ai-memory-consolidate/src/lint.rs`）：pinned + 即将过期、timestamp 冲突 → lint **只报告不删除不编辑** | `[06:80]` |
| **D7** | `ignored` | **[LLM]**（可升级） | 要判「规则已在场但行为仍违反」需要**在场证据 + 违规证据**。`use==0 && view==0` 只能说明没有已记录的使用/查看，不能证明规则已加载；在场须有可信加载或查看事件，**违规侧第一轮无任何机械实现** | `[E]` `06:adherence-rate-probation-capacity`（`lib/lifecycle.py`，view 仅作保留依据，不计入分子）；`08:times-applied-reinforce` 计数器无写入者 → 今天连在场证据都不完整，**故不能声称确定性可判**；可量化性由 `14:read-before-write-enforcement` 先例证明：拒绝读造成两天约 **142 次 denial + 约 204 次 read-before-write 拒绝**、几乎没有 patch 落地（#61521/#39996）→ 「未被遵守」能被账本统计出来。**升级条款**：一旦 `05-DATA-MODEL §5.4` 的 counter_invariant 五条满足，本诊断的预筛部分升为 `[DET]` | `[06:81]` |
| **D8** | `outdated` | **[LLM]**（authority 为机器制品时降为 [DET]） | **第一轮材料一致反对用年龄判过时**。判定必须是对 authority 重验（`.nvmrc` / 依赖版本 / 用户指示） | `[E]` `01:decay-type-maintenance-contract` 三条原文禁令：`Age alone proves neither that context is wrong nor that it should be removed` / `Never retire solely because a learning is old or has not recurred` / `Lack of use alone does not justify removing a rare safeguard`；`14` 需要 `reanchor_clock` 回滚被旧 bug 误标的 stale 就是反例代价；`15:retention-decay-formula` 把 stale 阈值改为从 λ 推导（default λ 复现历史 30 天，λ=0.008 时阈值变 75 天）→ **「过时」是参数不是事实** | `[06:82]` |

D7 的机械可判性至今不成立（违规侧第一轮无任何机械实现）`[06:81]`，其「预筛部分升为 `[DET]`」是一条**未触发的升级条款**，不是当前判定者 → 本文件按 `[LLM]` 呈现。 `UNKNOWN（升级前置条件未满足）`

## 4. 诊断 → 处置动作的映射（禁止 ADD NEW RULE 作为默认出口） `[06:84]`

```text
N01 [DET] D1 not loaded 命中？                                                        [06:87-89]
      yes → 动作 = MOVE（装配层修复，非新增规则）→ 落点见 §5 的 L-MOVE
      条件可判：加载集枚举差集非空。   no → N02
N02 [DET] D2 wrong trigger 命中？                                                     [06:90-92]
      yes → 动作 = UPDATE（只改触发描述，把频度词换成事件锚点）→ L-UPDATE
      先决：patch 本集实际加载过的技能 > patch 既有 class-level 技能（06 偏好序）。 no → N03
N03 [DET] D3 wrong scope 命中？                                                       [06:93-95]
      yes → 动作 = MOVE（scope 重挂；project ↔ global 升降）→ L-MOVE
      附加门：谓词自检失败（命名不一致）时不得 MOVE，须先修谓词 → L-NOTHING + failed 账。 no → N04
N04 [DET] D4 not mechanically enforceable 命中？                                       [06:96-102]
      yes → 动作 = AUTOMATE（层级下沉阶梯，取**最高能兜住的一层**）→ L-TEST / L-LINT / L-SCRIPT / L-EVAL
      阶梯（原文，04 的 Promote tiers）：enforce it (assert/type/test) with its size quoted
        → else a comment at that site → else an agent-facing doc（合并既有主题文档，
        else docs/agents/<topic>.md，else docs/agents/lessons-learned.md）
        with one backtick-path line + one sentence on why the tiers above cannot hold it
      no → N05
N05 [LLM] D5 ambiguous 命中？（须先过 ≥2 active 条目的确定性预筛）                       [06:103-105]
      yes → N05a [LLM] 能靠改写一句消歧？ yes → UPDATE(澄清)  /  no → N05b [LLM] 与既有条目是同一条？
             yes → MERGE（必带 absorbed_into，见 07）/ no → 记 unresolved_ambiguity → L-NOTHING + 人工队列
N06 [LLM] D6 conflicting instruction 命中？                                           [06:106-109]
      yes → N06a [DET] 两条能由 scope/trigger 划界共存？ yes → MOVE/UPDATE（各自收窄）
             no → N06b [JUDGE] 哪条是权威？ 判得出 → SUPERSEDE（输方可达，见 07）
                  判不出 → [HUMAN] 记 unresolved_conflict，交人类批处理（**零 LLM 时的正确出口**）
N07 [LLM] D7 ignored 命中（在场且仍违反）？                                             [06:110-114]
      yes → N07a [DET] 该规则机械可判？（复用 D4 判据）
             yes → AUTOMATE（把它从「文档里的话」降为断言）→ L-TEST/L-LINT
             no  → 动作 = MOVE（换到实际会被加载的位置）或 UPDATE（一句 why）
             禁止：「再加一条同样没人遵守的规则」= ADD 在此路径上是**明确禁止**的
N08 [LLM] D8 outdated 命中？                                                          [06:115-117]
      yes → N08a [DET] authority 是机器制品（文件/版本/schema）→ 重验通过则 SUPERSEDE；不通过则 DELETE 提案
             no  → [HUMAN] 由人判：UPDATE / SUPERSEDE / DELETE 三选一（DELETE 只产提案，走 Stage 3 的 R2）
N09 [DET] 八诊断全部落空？                                                              [06:118-120]
      no  → 回到对应 Dn 分支（不得因「计数已达标」跳过诊断）
      yes → N09b
N09b [DET] ADD 前置三条件全部成立？（全部 [DET] 可判）                                    [06:121-128]
      (a) born as an umbrella —— 先问「这是哪一类的实例」，今天的教训作为**第一个 case**
          [E] 06:reflector-compare-first-reconcile 偏好序 FORK_INSTRUCTION：
              patch 本集实际加载过的技能 > patch 既有 class-level 技能（带 files）> create
      (b) 偏好序未落到 create
      (c) identity key 已解析且 content_hash 不等（相同则短路，不产生新版本/假链）
      yes → 打 ADD 标记，进入 Stage 1（N10）
      no  → 改走 UPDATE / MERGE 分支；三者皆不可则 EXIT → L-PATTERN
```

## 5. MOVE 与 AUTOMATE：FAILED_RULE 派生的**受限特例**，不是第 9/10 个动作 `[07:131]`

```text
MOVE：只改 scope/挂载位置/加载路径，不改内容、不改状态、不产新版本。                        [07:134-138]
  合法入口：仅 Stage 0 的 D1(not loaded) 与 D3(wrong scope)。
  受限条款：谓词自检失败（如命名不一致 archived/ vs _archived/ 使谓词静默失效 [E] 05:archived-rules-exclusion）
           时禁止 MOVE，必须先修谓词 → 走 L-NOTHING + failed 账。
  它复用 A3 的写门与账本，因此不构成独立生命周期语义。 [E] 06:reflector-compare-first-reconcile 的 level 判据
AUTOMATE：把「文档里的一句话」降为断言（assert/type/test/lint/script），即层级下沉阶梯。      [07:139-143]
  合法入口：仅 Stage 0 的 D4(not mechanically enforceable) 与 D7(ignored 且机械可判)。
  受限条款：产物落点是**代码/CI 面**（06-PROMOTION 的 L-TEST/L-LINT/L-SCRIPT），不进入条目的 6 个存储态；
           它不淘汰任何条目，只是把该条目的权威载体换掉 → 随后对该条目执行 UPDATE 或 ARCHIVE。
  [E] repos/agent-skills/AGENTS.md §Prevent Recurrence 的 Promote tiers（04 型；SPEC §9.2 归属更正）
```

**动作集守恒**：8 个动作 + 2 个受限特例（复用既有写门），无第 9 个动作。任何新动作（如 split、rename、reindex）都必须重开本裁决。 `[07:146]`
Stage 0 的六个处置动作（MOVE / UPDATE / MERGE / AUTOMATE / SUPERSEDE / DELETE）**不是落点**，它们复用 §5.1 的落点集合，故不另计出口。 `[06:50]`

## 6. 待确认与暂缓事项

- D6 的「低风险/高风险量化门槛」（哪类冲突可留在 small LLM 自决、哪类必须升 judge/人工）在 Round 2 **无任何量化门槛**，保守取「所有会销毁内容的合并一律升 judge」→ `DEFERRED id DD-6-sub45`（04 §9 的 D6-b，原文「第一轮**无任何量化门槛**」`[04:193]`）。本文件不填阈值。
- D7 的升级条款前置（`05-DATA-MODEL §5.4` counter_invariant 五条是否满足）→ 历史构建时点观察：`kd_lifecycle.py` 记「3 of 4 counters fail admission」（`.distill/round-3/SCRIPTS-CONTRACT-MAP.md:31`），即**未满足**，D7 仍为 `[LLM]`。这不是本文件能推进的结论。
- D1–D8 的**判定阈值**（加载集枚举、锚点集合、字符窗口 60/57、≥2 active 条目）Round 2 只给判据与参照实现，未给本项目配置数值 → `UNKNOWN（06 未裁决数值）`。
- `06` §2.2 里 N09 的 `no → 回到对应 Dn 分支` 未写出「回到哪一个 Dn」的选择规则（哪个诊断优先、是否重跑全部）→ 本文不补，见 §7 的代码侧处理方式。 `UNKNOWN（06 未写选择规则）`
- 本文件与 R12 共享 `06` §6 的 8 项 DEFERRED 中影响 Stage 0 的条目：DEF-5 / REROOT（N11 的 canonical key 是否可得）→ `DEFERRED id DD-1-sub05`、`DD-1-sub13` `[06:288]` `[06:316-320]`；影响 ADD 前置 (c) 的 identity 判据 → `DEFERRED id DD-6-sub40`（D6-a） `[04:192]`。
- `04` §3 的 #9 行（Conflict resolution）已把 FAILED_RULE 八维中的 4 维归入确定性检测半 `[04:55]`；矩阵左侧 C1–C12 的逐条裁决不在 R10 范围内。

## 7. 历史源码对照

对照对象：`../scripts/kd_gate_tree.py`（`NODE_TABLE` / `EDGE_TABLE`，Stage 0 = `stage==0` 的 17 个节点）。以下仅保留历史构建时点的结构观察，不是本轮运行证据；当前规模须核对实际源码。

| 项 | Round 2 值 | 代码实测值 | 结论 |
|---|---|---|---|
| Stage 0 节点数 | 17 `[06:43]` | 17（N00, N01–N08, N05a, N05b, N06a, N06b, N07a, N08a, N09, N09b） | 一致；全树仍为 38 节点 / 87 出边（R12 §7） |
| Stage 0 出边数 | **35（Round 2 历史值）** `[06:43]` | **36（当前）**；`N00` 新增 `lifecycle_requested` 第三出口，`N03` 仍 3 条（`hit_and_predicate_ok` / `hit_predicate_selfcheck_failed` / `miss`） | 历史 35 ≠ 当前 36；新增边明确计入 |
| 判定者分布 | D1–D4 `[DET]`、D5–D8 `[LLM]`（N06b `[JUDGE]`） `[06:75-82]` | Stage 0 节点 judge 计数：DET 10 / LLM 6 / JUDGE 1。逐个对应：DET = N00,N01,N02,N03,N04,N06a,N07a,N08a,N09,N09b；LLM = N05,N05a,N05b,N06,N07,N08；JUDGE = N06b | 一致（含 §3 的「4 个 `[LLM]` 诊断」被展开成 6 个 `[LLM]` 节点这一结构，Round 2 与代码同一读法） |
| 动作词汇表 | MOVE / UPDATE / MERGE / AUTOMATE / SUPERSEDE / DELETE + ADD `[06:88-127]` `[SPEC:125]` | Stage 0 出边上实际出现的动作标签：`MOVE`×3、`UPDATE`×3、`AUTOMATE`×2、`MERGE`×1、`SUPERSEDE`×2、`DELETE`×1（共 12 条带动作出边）；`ADD` 不在 Stage 0 出边上，出现在 N18→N19（3 条）与 N22b→N23（1 条），共 4 条 | 一致，但**位置不同**：06 在 N09b 写「打 ADD 标记，进入 Stage 1」，代码把 `ADD` 标签打在 Stage 1 末端（N18）与 Stage 2（N22b）的出边上；N09b 的 yes 边是 `('N09b','add_preconditions_hold','N10')`（无动作标签）。标签语义相同（ADD 是标记而非落点），落位不同 → 两侧均未改 |
| 受限动作不是落点 | `L-MOVE/L-UPDATE/L-MERGE/L-AUTOMATE/L-SUPERSEDE/L-DELETE` 不是落点 `[06:271]` | `kd_gate_tree.LANDINGS` 11 项中不含上述 6 个标签；Stage 0 的动作边一律指向 `N23`（Stage 3 风险分层），终态由 `N29` 分派 | 一致 |
| 谓词自检失败 | `L-NOTHING + failed 账` `[06:95]` `[07:137]` | `('N03','hit_predicate_selfcheck_failed','N29','L-NOTHING+LEDGER')` | 一致（拼法差异见 R12 §7） |
| N09 的 no 分支 | `回到对应 Dn 分支` `[06:119]` | `('N09','diagnosis_unrouted','R-STAGE0-INCOMPLETE')` —— 代码把「有诊断命中但未路由」导向一个显式拒绝汇点，而不是重入某条 Dn 边 | **不一致（实现选择）**：Round 2 未写选择规则（本文件 §6 已标 `UNKNOWN`），代码选择了 fail-closed 拒绝而非回环。未「修正」任一侧 |
| 硬禁令（未跑 D1–D8 不得 durable 写） | `[06:131]` | 三重落地：① Stage 0 节点带 `requires=("known_coverage",)`（`kd_gate_tree.py:92,96,100,105,109,125,138,147,151` 共 9 个节点）；② `kd_gate.py:58-59` 的 exit-2 契约写明「Stage 0 was skipped / refused」；③ `kd_gate.py:87-97` 的 `apply_mutation` 要求 `decision.promotable` 且模型产出无 `human_approved` 即拒 | 一致（禁令在代码里有可指认的执行点） |
