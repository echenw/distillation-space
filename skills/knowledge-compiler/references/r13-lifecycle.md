# R13 — 更新与维护知识

正式知识需要更新、合并、归档或恢复时，查对应动作。状态检查与实际保存分开；归档和恢复仍需新的独立评测与人工批准。历史设计中的自动路径不代表当前可以自动执行。这里的 S12 生命周期只适用于正式知识库；普通工作区的轮次状态与 `results/` 更新分别按 R01 §2.1 和 R06 §4.13，不能混用状态或权限。

历史来源： `.distill/round-2/07-LIFECYCLE-POLICY.md` §1（行 9–36，含 §1.1）、§2 A1–A8 与 §2.1（行 40–146）、§3.1–§3.7（行 150–239），生成于 2026-10-06，wave 4. Citation prefix: `07:` = `.distill/round-2/07-LIFECYCLE-POLICY.md`，`06:` = `06-PROMOTION-POLICY.md`，`05:` = `05-DATA-MODEL.md`，`04:` = `04-DETERMINISTIC-VS-LLM.md`。
状态说明：本文供参考；具体行为以 ../scripts 为准（状态集与边的权威是 `kd_lifecycle.py` 的 `TRANSITIONS` + SC05 `schemas/lifecycle-record.schema.json` 的 `lifecycle_state.enum`，两者在调用时被读取，见 `kd_lifecycle.py:82-97`）。
列命名与 `05-DATA-MODEL.md` 一致（`tombstoned_at` 为统一名，`15` 原列名 `superseded_at` 见 05 的 M4 裁决） `[07:5]`；`[E]` = EVIDENCE-SUPPORTED、`[I]` = ENGINEERING-INFERENCE 的标注沿用原文 `[07:4]`。

---

## 阅读导航

- 1. 状态集：6 个存储态 `[07:9]`
- 2. 8 个动作 `[07:40]`
- 3. 必须明确保留的设计约束 `[07:150]`
- 4. 待确认与暂缓事项
- 5. 历史源码对照

## 1. 状态集：6 个存储态 `[07:9]`

以下图表是历史设计及来源论证，不授予自动执行权限。当前 S17 只验证/提议转换，权威落盘仍由 S12 唯一执行；ARCHIVE/RESTORE 也须新的 S16 PASSED、G1 与三通道绑定回执。真实 use/view/opportunity 遥测尚未准入，相关计数保持 NULL，不据历史自动路径启动 DECAY/ARCHIVE；当前 S12 拒绝物理 DELETE，历史设计中的人工删除入口也未交付。当前能力见 R02 §8、R16 §5。

```text
candidate ──accept(人审,同事务)──► active ──SUPERSEDE──► superseded ──tombstone──► (门票) ──人工 gc──► hard-deleted
    │                                  │                                          ▲
    │                                  └──DECAY线索 + ARCHIVE门──► archived ──restore──┘（回 active）
    ├──reject(人审)──► rejected ──新的真实证据──► candidate
    └──执行出错────► failed ──重试成功──► (按动作的终态)      failed ──人判定不重试──► rejected
                                                              [07:12-16]
```

| 存储态 | 为什么必须是存储态 | 进出转换 | 证据 | 引用 |
|---|---|---|---|---|
| `candidate` | 自治系统必须先有「**不生效的暂存态**」，否则 ADD 与 durable 写之间没有可审计缓冲 | `+人审 accept 且同事务落盘 → active`；`reject → rejected`；`执行出错 → failed`；`丢弃 → 无副作用退出` | `[E]` `06` reflector 只报提案；`15:auto-improve-proposal-state-machine`（`_pending/<id>.md` + sha256、approve 与 apply 同事务、stage 期冲突拒绝）；CM-32 `inert-candidate-quarantine` + CM-35 `manual-approval-before-durable-write`；`09:git-backed-inert-candidate-store` | `[07:21]` |
| `active` | 它是权威可见集；没有它就没有「当前真相」的单一口径 | `SUPERSEDE → superseded`；`ARCHIVE 门 → archived`；`MERGE 作为幸存伞形 → active(内容前进)`；`人审 reject → rejected` | `[E]` `15` 的 `is_latest=1`、`11` 的默认召回面 `invalid_at IS NULL`、`14` 的 `usage state=active` | `[07:22]` |
| `superseded` | 「**减少而不销毁**」的唯一实现形式；旧版本保持可达是并发正确性与审计的前提 | `decay 驱逐或 reconcile 安全网写 tombstoned_at → superseded(门票)`；`同 path 重新写入 → superseded(普通链成员，门票清除)`；`门票 + 年龄达标 + 人工 gc → hard-deleted` | `[E]` `15:page-supersession-chain`、`11` 的 `invalidate()` 是唯一离场路径且从不 unlink、`10:supersession-cascade-stale`；CM-28 `supersede-never-destroy`（5 成员 / **3 distinct projects** / `needs_llm=False`） | `[07:23]` |
| `archived` | 它是**自动路径的破坏上限**；缺它就必须让 DECAY 直接连到 DELETE，而 DELETE 不可逆 | `restore → active`；`再次活动 → active`（`14` 的 `reactivated` 语义）；`显式 purge + 人工 → hard-deleted` | `[E]` `14:curator-deterministic-inactivity-lifecycle`（`skills/.archive/` + `curator restore`，`never deletes — archive is the maximum`）、`06` `archive/restore` 成对 API（整目录 `os.replace`）、`11:gc-only-human-physical-deletion`（`Manage._delete` 只 invalidate） | `[07:24]` |
| `rejected` | **必须与 `failed` 分离**，因为语义差别是决策性的：rejected = 人的决定，**无新证据不得再提**（防重复提交与假成功） | `新的真实证据 → candidate`；`人工彻底放弃（仅由人）→ 可选 DELETE 资格，仍须门票 + gc` | `[E]` worker-15 核查原文：Failed 与 Rejected 分离且 `rejected_targets` 是可查询遥测（`AutoImproveTelemetry.rejected_targets` / `rejected_candidates_json`） | `[07:25]` |
| `failed` | 承载「机制**尝试过但没成功**」这一事实 → 不产生假成功、不重复写入；也是 REINFORCE/DELETE 的幂等依据 | `重试成功 → 按动作终态`；`人判定不重试 → rejected` | `[E]` `15` 的 Failed/Rejected 分离要求；`06` 归档失败由下次 pass 重试、`15` 失败由下次 sweep 重试；`09:due-gate…:: _record_failure_state`（失败不写 digest → 自动重试） | `[07:26]` |

### 1.1 显式论证：**3 条不作为存储态** `[07:28]`

| 候选状态 | 裁决 | 论证与代价 | 引用 |
|---|---|---|---|
| `stale` | **只作只读派生视图，不物化** | `[E]` 反例代价：`14` 确实把 stale 存进 `~/.hermes/skills/.usage.json`，结果**必须由 `reanchor_clock` 回滚被旧 bug 误标的记录**（artifact #79295，并专门有 `test_preseeded_never_used_builtin_is_reanchored_not_staled` 兜底）。`11` 明确反对：用 status 字段表达「已过期/已替换」会引入**第三种状态（partial stale）并覆盖历史**，其解法是有效性只由 `invalid_at` 推导、status 只是只读派生视图。`10` 的 stale-session 同样是推导（`age>30d && !summary`）。**定案**：只存计数器 + 时间戳 + 门票列，stale 每次读时计算，永不成为权威 —— 以免出现「stale 但仍在召回」的第二权威。派生标签只是 REINFORCE/重验的线索，**不是 ARCHIVE 的充分条件** | `[07:32]` |
| `tombstone` | **折叠为 `tombstoned_at` 列（`15` 原列名 `superseded_at`），不建独立状态** | `[E]` `15` 已给出最省形式：`tombstone 判定 = superseded_at 非空`，**它是列不是状态**；且「hard-delete pass 只吃 tombstone（因为普通 supersession 行没有这一列），所以 reconcile 安全网的误判不会永久销毁一个又出现的文件」。本文改 `15` 的一个刻意设计：不采纳「两类门票来源故意不可区分」（其自身 risks 承认这会让 reconcile 误判连坐 decay tombstone，只能靠复活路径兜底），而把**产生原因写进 `lifecycle_event.reason`** —— 不增加权威面，只增加可解释性 `[I]`（形状有 `[E]` 支撑：`10:strength-and-confidence-decay` 每条变更写 reason、`14` 的账本 actor） | `[07:33]` |
| `probation` / `dormant` | **不物化** | `[E]` `06:adherence-rate-probation-capacity` 的 probation 是纯推导：`opportunities < MATURITY_THRESHOLD` 时照常召回、不淘汰、不计入容量池，且**决策只读累积水位**（不读本会话所见，使任何仓的 SessionStart 得出同一结论）。物化成状态会引入需要迁移与失效的第二权威 `[I]`（「第二权威」的判据取自本文 §1.1 stale 行的同一理由） | `[07:34]` |

**状态守恒声明**：6 个存储态 + 1 个 `hard-deleted`（物理移除，非状态而是行消失）= 条目生命周期无悬空出口；任何未列出的状态一律**不得新增**，新增即需重新裁决（对照 SPEC §4 的 67 簇严格守恒原则，状态集同样守恒）。 `[07:36]`

## 2. 8 个动作 `[07:40]`

### A1 `ADD` `[07:42]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **FAILED_RULE 前置检查已完成**（`06-PROMOTION-POLICY.md` Stage 0）：八种诊断全部落空才允许 ADD，**禁止默认 ADD NEW RULE**；② 走 06 reflector 偏好序：patch 本集实际加载过的技能 > patch 既有 class-level 技能 > update 带 files > create；③ 若仍 create，**必须 born as an umbrella**（先问「这是哪一类的实例」，今天的教训作为第一个 case）；④ identity key 已解析；`content_hash` 相同则短路，不产生新版本/假链；⑤ 目标 scope 由内容判据决定（repo-specific→project；用户/团队 standing 偏好→global）；⑥ durable 写之前有人审 accept（candidate→active 的**唯一通道**） `[07:46]` |
| 后置状态 | `candidate` → 人审 accept 后 `active` `[07:47]` |
| 可逆性 | true `[07:48]` |
| 执行者 | `[LLM]` 提案，`[DET]` 落盘（P-1：模型无写权） `[07:49]` |
| 失败回滚 | proposal 丢弃即可，不产生权威写入；approve 与 apply 同事务，失败则整批不落；**禁止留下 `created_by=null` 的半记录**——该形态必须与记录缺失同样 fail-closed `[07:50]` |
| 证据 | `[E]` `06:reflector-compare-first-reconcile`（`repos/autoharness/src/autoharness/hook/promoter.py` + `agents/reflector.md` FORK_INSTRUCTION）；`15:page-supersession-chain`（内容相等短路）；`14:autonomous-write-provenance-optin-gate`（`repos/hermes-agent/agent/background_review.py`）；CM-32 + CM-35 `[07:51]` |

### A2 `MERGE` `[07:53]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **每条被删 sibling 必须带 `absorbed_into`，且 promoter fail-closed 校验：目标伞形不存在 → 整条 intent 拒绝**；② `destinations` 必须是真实存在或本次新建的名字；③ 每条 `removed` 恰好落进 `consolidated` 或 `pruned` 之一（由**集合差校验**，任何「消失」都是缺陷 —— 这正是 SPEC §4 簇守恒的机制原型）；④ **提炼为可复用规则**：采用祈使句，并用一句话说明原因，丢弃事故叙述/PR 号/日期，禁止把文件原样存入 `references/`；⑤ 包完整性硬步骤：有支撑文件或相对链接时只能三选一（保持独立 / 完整重迁并改写路径 / 整包原样归档）；⑥ `pinned` 完全豁免；候选列表过滤 `bundled` 与 `disabled`（fork 只能被提供它**能读能写**的东西）；⑦ `consolidate` **默认关闭**（需显式开启）；⑧ 同轮强制 reconcile：被取代的旧陈述在同一次运行里 stage patch，否则**整批拒绝** `[07:57]` |
| 后置状态 | sibling → `superseded` + `archived`（带 `absorbed_into` 指针）；umbrella → `active`（内容被原地改写） `[07:58]` |
| 可逆性 | true（**但代价最高**：需双层回滚；见失败回滚） `[07:59]` |
| 执行者 | `[LLM]` 判「是否同类 + 合成正文」，`[DET]` 校验与写序，`[HUMAN]` 删除性归并（`06-PROMOTION` 的 R2） `[07:60]` |
| 失败回滚 | 双层：① 逐变更**内容寻址账本**（`rollback_entry` 是模块里**唯一 fail-closed** 的路径；其余账本异常吞掉并记录 —— 账本定位是遥测不是门）；② 整树 `tar.gz` 快照（**只有内容被原地改写的归并 pass 才做**，prune-only 只跑 `prune_old_snapshots`，keep 默认 2）。回滚前先对当前树快照，使**回滚本身可撤**；快照必须排除 `.archive/`、账本、`.locks`、`.git`、`.hub` `[07:61]` |
| 采信顺序（冲突时谁说了算） | `[E]` `14:consolidation-vs-prune-reconciliation-audit` 的权威等级：`delete 调用里的 absorbed_into`（目标存在→consolidated，空串→显式 pruned，缺失→fall-through）> **校验过的模型声明**（仅当 `into` 在 destinations）> tool-call 审计启发式 > 无证据 fallback→`pruned`。模型点名不存在的 umbrella 时，**采用审计真目标**并保留 `model_claimed_into` 且在报告打警告行 `[07:62]` |
| 证据 | `[E]` `14:umbrella-consolidation-distillation-pass`（`repos/hermes-agent/agent/curator.py`：`DEFAULT_CONSOLIDATE=False`、候选过滤、`absorbed_into` fail-closed、`tools/skill_manager_guards.py::_curator_consolidation_delete_guard`）；`06:reflector-compare-first-reconcile`；`14:skill-library-audit-ledger-and-two-layer-rollback`（`tools/skill_ledger.py` `_VALID_ACTORS`/`TRANSIENT_DIRS`/`_delta`）；CM-22（簇级 Round 1 判语 `needs_llm=false, det=true`） `[07:63]` |

### A3 `UPDATE` `[07:65]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **read-before-write**：写前必须已读过该确切路径；「transcript 里此前引用过内容」**不算读过**；② 同轮强制 reconcile：凡本次新陈述取代旧陈述，必须同批 stage patch 并引用本集证据；③ **措辞/补充可就地 update；事实本体改动必须走 SUPERSEDE**（比较只在 `body.strip()` 粒度，abstract 是索引面、不受本体保护）；④ actor 显式记录（账本三值 `{curator, agent, user}`），**归属是声明的，永不从活跃度推断**；⑤ 被拒后的循环有界：拒绝 → view 一次 → 重试一次 → 不再循环 `[07:69]` |
| 后置状态 | `active`（同 id，版本前进，账本一条含 before/after） `[07:70]` |
| 可逆性 | true `[07:71]` |
| 执行者 | `[LLM]` 写正文，`[DET]` 写门与账 `[07:72]` |
| 失败回滚 | 账本按 `_delta()` **只对变化路径回写**（不回写整树，否则每次 patch 变成全文件重写）；未先读而写出的错误 patch 属**设计违规**，应在写前门就拒绝而非事后修 `[07:73]` |
| 证据 | `[E]` `14:read-before-write-enforcement`（代价实测：两天约 142 次 denial + 约 204 次 read-before-write 拒绝、几乎没有 patch 落地 #61521/#39996）；`06:reflector-compare-first-reconcile`（F1 duty）；`11:update-versus-supersede-boundary`（`agent-memory/packages/core/src/agent_memory/core/record.py`）；`14:skill-library-audit-ledger-and-two-layer-rollback` `[07:74]` |

### A4 `SUPERSEDE` `[07:76]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① 新行 `is_latest=true`；旧行置 `is_latest=false` 并通过 `supersedes` 链指向新行；② 不变量校验：有 `superseded_by` **必须有 `invalid_at`**；不能自指；两者必须是合法 slug/ISO（写坏应在 `validate()` 阶段拒绝，而不是事后修）；③ **只有 decay 驱逐与 reconcile-delete 安全网两类动作写删除门票列 `tombstoned_at`**；普通 supersession 行不写该列；④ 并发分歧写**只能 supersedes 不得 destroy**（不变量 16，由 `multi_session.rs` 守卫；**单测一次一个 session 的形状看不见该缺陷**）；⑤ `content_hash` 相等走短路，不产生新版本 `[07:80]` |
| 后置状态 | `superseded`（旧行仍可达：默认召回面过滤，`as_of` 时间旅行查询可取） `[07:81]` |
| 可逆性 | true。**两个字段两种可逆性**：删除门票 `tombstoned_at` **可被复活清除**；语义替换链 `invalid_at`/`superseded_by` **单调不可清空** `[07:82]` |
| 执行者 | `[DET]`（唯一由确定性独占的「内容关系」动作） `[07:83]` |
| 失败回滚 | 不需要应用层 undo —— 其失败模式已被「旧版本永不消失」消除。复活路径：同 path 重新写入时把新行 `supersedes` 挂回旧链并清掉旧行的门票列，旧版本从 hard-delete 候选变回**受保护的链成员** `[07:84]` |
| 证据 | `[E]` `15:page-supersession-chain`（`repos/ai-memory/crates/ai-memory-store/src/{writer,reader,admin}.rs` + `AGENTS.md` invariant 16）；`11:validity-interval-lifecycle`（`core/{record,manage}.py`）；`10:supersession-cascade-stale`（agentmemory/src/functions；路径省略 `repos/` 前缀，见 SPEC §7.3）；CM-28 `[07:85]` |

### A5 `DELETE`（历史设计中的物理删除动作） `[07:87]`

| 项 | 内容 |
|---|---|
| 前置条件（全部同时成立） | ① 目标处于 `superseded` 且**门票列 `tombstoned_at` 非空**，门票年龄 ≥ `deletion_grace_days`（参照值 180）；② 判据是「**已失效**」，**不看 age/weight**；③ **先补救再删**：无 summary 的陈旧会话先触发 summarize，失败则 `continue` **不删** —— 若自动保存可能静默失败，宁可阻止这个会销毁证据的动作（fail-closed）；④ `dryRun` 先出 `wouldDelete + ids`；**批量删除无 filter 拒绝执行**（`BULK_FILTER_KEYS` / `BATCH_SIZE=50`）；⑤ 级联清理派生态：显式删 retention 分数行与 access 行，避免**幽灵分数继续驱逐**；⑥ **只有人类执行**：`gc` 是唯一物理删除入口，任何自动路径（`Manage`）不可达 `unlink`；⑦ 目标已被内容寻址账本或整树快照**覆盖**（否则不存在回滚路径，只允许 ARCHIVE） `[07:91]` |
| 后置状态 | `hard-deleted`（行 + 文件消失），仅剩 git / 快照历史 `[07:92]` |
| 可逆性 | **false** `[07:93]` |
| 执行者 | `[HUMAN]` `[07:94]` |
| 失败回滚 | **没有应用层 undo**（`15` 风险原文：`hard_delete` 之后只剩 git；git 目录丢失即历史不可恢复）。因此 DELETE 必须运行在**有界可撤窗口**内：账本 `ledger_max_bytes` 默认 5 MiB、快照 keep 默认 2，超出窗口即不可撤。**未闭合项（必须留为未闭合）**：`worker-11` 承认永久删除仍缺显式确认与 host 级授权（CLI 标签不能识别人类） `[07:95]` |
| 证据 | `[E]` `11:gc-only-human-physical-deletion`（`core/store.py::gc` + `tests/unit/test_manage.py::test_gc_is_the_only_road_to_physical_removal`）；`15:page-supersession-chain`；`10:stale-session-evict-recovery`（`agentmemory/src/functions/evict.ts`）；`10:retention-score-eviction`；`14:memory-preservation-checkpoint-before-compaction`（四种失败全部 fail-closed，不允许压缩继续）；`15:ttl-pinned-priority-and-forget-sweep`（TTL>pin；**解析失败语义 UNKNOWN**） `[07:96]` |

### A6 `REINFORCE` `[07:98]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **字段必须有写入者**：明确的事件锚点 + 调用点（谁在什么事件 +1），并在实现清单里列出该文件与符号；② **三分信号不得混用**：只有 `use` 进存活率分子；`view` 仅作为试用期结束评估中的保留依据；`patch` 不加分、只标记被改进；③ **分母是机会数不是时间**：`opportunities = max(0, request_count - anchor)`，`opportunities < maturity` 走 probation（照常召回、不淘汰、**不计入容量池**）；④ 有界与自愈：`recent[<=20]`、`count = max(count, recent.length)`、对异常数据按保守规则解析；⑤ 零侵入：只给 self-produced 条目记账；**child 会话任何路径都不计数**；计数器随目录 rename 原子迁移；⑥ **使用计数不得与可重建索引同生命周期存放**（索引可删，计数不得随之归零） `[07:102]` |
| 后置状态 | 计数与 `last_activity_at` 前进；**不产生新行、不改状态**。**review 不是生命周期事件**：不加 `Recurrence-Count`、不刷 `Last-Seen`、不建平行 registry `[07:103]` |
| 可逆性 | true（单调累加，无 undo 语义） `[07:104]` |
| 执行者 | `[DET]` `[07:105]` |
| 失败回滚 | 无。**丢失增量必须如实上报**：`06`/`08` 的 bump 是 read-modify-write 且 docstring 承认跨进程非原子 → 计数偏低会**系统性提前归档**。定案：决策门要么有**锁证明**，要么把「偏低」写进零使用判定（对照 `use==0 && view==0` 双条件） `[07:106]` |
| 证据 | `[E]` `06:use-view-patch-split-instrumentation`（`repos/autoharness/src/autoharness/hook/on_skill_call.py` + `lib/sidecar.py`，三锚点 + 四道闸）；`06:adherence-rate-probation-capacity`（`lib/lifecycle.py`）；`10:access-reinforcement-log`（`agentmemory/src/functions/access-tracker.ts`，有界环形 + keyed lock）；`11:read-telemetry-weight-settling`（一次读只结算一次 + 6 条行为测试）；`08:times-applied-reinforcement` **[VERIFIED 缺口]**（`repos/pro-workflow/src/db/{schema.sql,store.ts}`，无写入者 → 恒 0）；`01:decay-type-maintenance-contract` `[07:107]` |

### A7 `DECAY` `[07:109]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **唯一口径**：跨层分数不同口径不得进同一决策；`stale` 阈值应从衰减参数推导而非固定天数；② 锚点式幂等：`anchor = max(lastAccessedAt\|\|updatedAt, lastDecayedAt\|\|-inf)`，写 `lastDecayedAt=now`，只回写 `\|Δ\|>epsilon` 的已变化记录；③ **零使用不是陈旧**：`use_count==0 && anchor 晚于 stale_cutoff` → 判为**证据缺失**，不归档并回滚误标；从未访问时访问项恒 0，既不加分也不额外扣分；④ **播种时钟**：首次出现无持久记录 → 时钟从现在起；**新装机/更新的首个 tick 绝不动库**（只播种并推迟一个周期）；⑤ 参数钳制与 fail-closed：阈值下限钳到 1（`<1` 会让 cutoff 落到 `now` 之后，从而一次批量迁移整棵树且无确认）；非法 lambda 拒绝非正值；非法可选系数**只关掉加成，不降低历史保留分**；⑥ 每个豁免轴都要有出口（`pinned` / 被 cron 引用 / 「未强化才软删」这类条件可静默变永久） `[07:113]` |
| 后置状态 | **派生分数或权重变化（不是权威态）**；越阈值只产生 `stale` 派生标签与重验线索，**不直接进 `archived`** `[07:114]` |
| 可逆性 | true `[07:115]` |
| 执行者 | `[DET]` `[07:116]` |
| 失败回滚 | 不写盘即无副作用；已写派生分数在记录删除时**必须同删派生行**；对被旧 bug 误标 stale 的记录用 `reanchor_clock` 拉回 active（该回滚本身有专门测试） `[07:117]` |
| 证据 | `[E]` `10:strength-and-confidence-decay`（`agentmemory/src/functions/consolidation-pipeline.ts`）；`15:retention-decay-formula`（`crates/ai-memory-store/src/decay.rs` + `ai-memory-consolidate/src/{sweep,lint,curator}.rs`）；`14:curator-deterministic-inactivity-lifecycle`；`11:read-telemetry-weight-settling`（`test_decay_is_reversible_by_an_explicit_boost`）；worker-10 open_questions（四套衰减数学互不校准） `[07:118]` |

### A8 `ARCHIVE` `[07:120]`

| 项 | 内容 |
|---|---|
| 前置条件 | ① **归档是自动路径的最大破坏动作上限：永不 delete，只移入 `.archive/`**；② **排除谓词必须同时作用于召回面与判重面**（`05` 只做到了召回面，其成本被 DD-4 立场 C 原文承认：过时规则仍会参与未来判重 → 把「已覆盖」误判带下去）；③ 写侧配套：谁移入 + 移入原因必须记录（`05` 的 `_archived` **无任何代码写入者**、SKILL.md 全文未提及，故只是半个约定）；④ 碰撞安全：整目录 `os.replace` 到 `.archive/<name>`，`ledger` 与 sidecar 随目录**原子迁移**；⑤ 顺序：**index built after archiving**（归档完成后才构建 recall_index）；⑥ 归档目录与账本**不进**整树快照；⑦ 豁免轴齐备：`pinned`、被 cron 引用（等同 pin）、非 self-authored（原生/用户条目永不进池）；⑧ **必须可熔断**：`paused` / `GRADUATION_REVIEW_SUSPENDED` —— 召回面已知坏掉时按零使用归档会**掩埋 surfacing 自身的失败** `[07:124]` |
| 后置状态 | `archived`（文件仍在磁盘、历史完好、默认召回面不可见、**判重面亦排除**） `[07:125]` |
| 可逆性 | true `[07:126]` |
| 执行者 | `[DET]` `[07:127]` |
| 失败回滚 | `restore` 移回即复活、历史完好（`14 curator restore` / `06 restore` / `15 restore-page`）；目录改名自身可逆，因此 **prune-only pass 不做整树快照**；部分成功必须显式报告 `{archived:{layer:[names]}}` `[07:128]` |
| 证据 | `[E]` `14:curator-deterministic-inactivity-lifecycle`（`repos/hermes-agent/agent/curator.py::archive_skill/restore_skill` + pinned/cron 豁免）；`06:adherence-rate-probation-capacity`（`lib/skill_store.py::archive/restore/_collision_safe_dest`）；`05:archived-rules-exclusion`（`repos/ECC/skills/rules-distill/scripts/scan-rules.sh`）；`11:gc-only-human-physical-deletion` `[07:129]` |

`MOVE` 与 `AUTOMATE` 是 Stage 0 派生的**受限特例**（不新增动作、不进 6 个存储态），其完整条款在 R10 `r10-diagnose.md` §5。 `[07:131-146]`

## 3. 必须明确保留的设计约束 `[07:150]`

### 3.1 历史设计的归档上限与人工删除入口 `[07:152]`
- `[E]` `repos/hermes-agent/skills/AGENTS.md § Curator 不变量`：**`never deletes — archive is the maximum`**；`pinned` 豁免每一个 auto-transition 与 LLM review；`skill_manage(action="delete")` 对 pinned 拒绝，而 patch/edit/write_file 仍可用（所以「不能删」不等于「不能改进」）。 `[07:154]`
- `[E]` `11`：物理 `unlink` 只有 `store.py#gc` 一条、由人跑、且被测试锁死（`test_gc_is_the_only_road_to_physical_removal`）；`Manage._delete` 只 `invalidate`，从不 unlink。 `[07:155]`
- `[E]` 理由（DD-4 `why_selected[1]`）：**只要库存在自动删除路径，恶意内容污染或受恶意指令影响的推理模块 就能造成不可逆损失**；五家 distinct projects（06/10/11/14/15）都实现了可撤销删除状态或降级不删。 `[07:156]`
- `[E]` destructive operations（`purge-project` / `reset` / `restore` / `reindex` / `uninstall --purge-data`）**必须保留 confirmation flags 与 live-process check**（`repos/ai-memory/AGENTS.md` 不变量 9；`backup` 保持 online，用 SQLite online backup API 让 writer 仍活着）。 `[07:157]`

### 3.2 删除资格是**可撤销状态位**（`15` 的实现范式） `[07:159]`
见 A4 的可逆性行与 `05-DATA-MODEL §5.6`。核心一句（`15` 原话）`[E]`：**把「安全网可能误判」编码成可撤销状态位，而不是另建 undo 系统。** 复活即撤销资格（`upsert_page_in_tx` 清掉旧行门票列）。 `[07:161]`
DD-4 的定案句（原文）`[E]`：**「删除资格编码成可撤销状态位 `tombstoned_at`（复活即清空）」**。 `[07:162]`

### 3.3 `SUPERSEDE` 与 `DELETE` 语义分离 `[07:164]`
- `[E]` `repos/ai-memory/AGENTS.md` invariant #16 原文：**`A divergent concurrent write supersedes, never destroys`** 与 **`"Last write wins" must not come to mean "the other version is gone"`**，由 `crates/ai-memory-store/tests/multi_session.rs` 与 active-project 指针测试守卫；该文件明说**单测一次一个 session 的形状看不见并发缺陷**。 `[07:166]`
- Agent 11 `supersede_vs_delete` 三条规则全部采纳：① 旧行 `is_latest=false` + `supersedes` 链，输的一方仍可达（`as_of` 可取）；② **门票只有一张、发门票的动作只有两个**的形式化（普通 supersession 行不写门票列，所以 hard-delete pass 天然碰不到它们）；③ 复活撤销删除资格。 `[07:167]`
- 硬边界（原文）`[E]`：**SUPERSEDE/MERGE 的可撤销承诺绝不能延伸成 DELETE 的可撤销承诺。** `[07:168]`

### 3.4 `MERGE` 必须带 `absorbed_into` 且 fail-closed `[07:170]`
缺 `absorbed_into` 或指向不存在的伞形 → **整条 intent 被 promoter fail-closed 拒绝，不允许先删了再说**。真实事故编号被记录在案：`#29912`（「归档了一簇但没归并」不可检测）。 `[07:172]`
第二条守恒（对应 SPEC §4 的 67 簇严格守恒）：`每条 removed 必须恰好落进 consolidated 或 pruned 之一，由集合差校验，任何「消失」都是缺陷`。 `[E]` `[07:173]`

### 3.5 主淘汰判据 = **机会数分母**；零使用 = 证据缺失 `[07:175]`

```text
主判据（唯一）：rate = use / opportunities，opportunities = max(0, watermark − anchor)      [07:178-188]
  · 分母是机会数，不是墙钟 → 使「从未被召回」不被判陈旧，且判定不读时钟
  · 零使用（use==0 且 view==0 且 anchor 晚于 cutoff）→ 判为【证据缺失】，不归档，且必须回滚误标
  · view > 0 仅作为试用期结束评估中的保留依据，【不进分子、不加分】
  · patch 单独记录，不加分
[E] 判据本体：CM-56 06:adherence-rate-probation-capacity（repos/autoharness/src/autoharness/lib/lifecycle.py::
    evaluate,_rate + lib/counters.py::request_count,bump_request）
[E] 零使用三条独立禁令：CM-57 14:curator-…（零使用豁免 + reanchor）、01:decay-type-maintenance-contract
    （Lack of use alone does not justify removing a rare safeguard）、11:gc-only…、06 的 use==0&&view==0 双条件
[E] 墙钟两用的保留方式：保留 14 的调度门（168h interval + idle 2h）与工程装置（跨进程 claim、首次播种、坏值钳位），
    【不保留它作为去留理由】；墙钟只留「最低驻留」兜底 —— 阈值数值 DEFERRED（见 §4 DEF-1，即本文件 §4.1）
[E] 反例（为什么不能只用墙钟）：06 的两类误伤（惩罚从未被给机会者、离线时全体老化）+ 14 自己在实现里
    内建了同一批评的补丁（零使用豁免、播种时钟、reanchor）→ 【纯墙钟判据的作者也不信纯墙钟】
```

### 3.6 拒绝 A2 连续分数作判据；拒绝自动 TTL 硬删 `[07:193]`

```text
拒 A2（连续 retention score 作去留判据）理由（DD-4 原文，[E]）：                                [07:196-203]
  · λ 取值互不校准：15 = 0.02，10 = 0.01（worker-10.json:2811），且【均未经离线评测验证】——
    worker-caveats.json[10].open_questions[2] 记为 UNKNOWN
  · 5 系数 × 4 tier = 高维调参面；cold_threshold 一旋钮两效果（decay 驱逐与 dedup 输入共用）
  · 分数落库 = 制造第二权威
  · 15 的公式本身改编自 10 → 不是「独立两家验证」
  保留其【数学纪律】作为将来若引入容量排序时的实现规范：fail-closed、默认全 None 可复现旧行为、
  access_count 与 distinct_actors 分离、纯函数 + property tests。

拒「自动 TTL 硬删（15 Pass2 原样）」理由（[E]）：                                                [07:205-213]
  · 与 14 的 pin 无条件豁免直接冲突
  · expires_at 解析失败是 fail-closed 还是 fail-open 【UNKNOWN】（worker-caveats.json[15].open_questions[1]），
    而该 pass 删行【不可逆】；15 自己的 lifecycle 承认：过期时间一旦被错误写入 frontmatter，pin 救不回来
  采纳其【结构】（明示到期 → 标记）而非【后果】（自动硬删）；并采纳两条工程条款：
    ① 矛盾由 lint 显式暴露（pinned + 即将过期）而非代码消解；
    ② 读侧过滤片段【不得】复用于 sweep walk（两条路径各自显式作用域）。
  重开条件：若 15 确认 expires_at 解析为 fail-closed 并给出测试，才允许考虑明示 TTL 自动硬删，
    且门票 + grace 条件仍保留。

另外明确拒绝的三种形态（[E]，DD-4 rejected_alternatives）：                                     [07:215-221]
  · 让 LLM 判定谁过时/谁该删 —— 14 问题陈述原文：让 LLM 决定谁过时风险高且【不可复现】；
    prompt 里的 24k 字符与「少于 10 个归档说明停太早」在代码里没有对应常量或断言，且该下限会施压制造假归并
  · C 的极端形态：永不淘汰、库只增 —— 05 承认过时规则仍参与未来判重；_archived 只在读侧、无写侧，
    命名不一致时谓词静默失效；08 无衰减无淘汰导致库只增不减
  · 纯人工 gc 而无任何自动标记 —— gc 判据是 is_active() 为假，仍需上游有人/有机制把它置为失效；
    11 自身不产生该状态，需要本设计的状态机供料
```

### 3.7 其他已固定的实现约束（从 DD-4/DD-6/Agent 11 汇总） `[07:224]`

```text
L-1 每次迁移写审计：before/after + reason + actor；报告有界；dry-run 只计数。 [E] DD-4 selected_design 末句  [07:227]
L-2 淘汰判据与 decay_type 失效原因【正交】，两者都不得单独推出 delete。 [E] 同上 + 01 三禁令                    [07:228]
L-3 三信号严格分离：每个进判据的计数器必须有可指认的 (事件 → 写入者 → 消费者) 三段，缺任一段【禁止进判据与展示模板】。
    [E] DD-4 selected_design + Agent 11 counter_invariant（08 的 times_applied 为反例，详见 05 §5.4）        [07:229-230]
L-4 无调度 vs 无门槛的取舍必须写明：10 的 decay/retention/auto-forget/evict 全部只响应显式 REST/MCP、
    【未发现内置定时】→「不调用就完全不驱逐」；14/06 相反，进程启动/SessionStart 即自动改库。
    本编译器采纳 14/06 的「常驻调度 + 熔断开关」，并强制 L-8 的可观测性。 [E] DD-4 contradictions[6]        [07:231-233]
L-5 归档必须同时进【召回排除面】与【判重排除面】。 [E] L-2/§3.5 + 05 的自认缺口                              [07:234]
L-6 并发计数正确性：keyed lock + count = max(count, recent.length) 自愈；无锁证明则把「偏低」写进零使用判定。 [E] A6  [07:235]
L-7 生命周期字段的清理必须显式：账本清扫有字节上限时必须告警（14 的 ledger_max_bytes=5MiB 可能删掉审计证据）；
    transient 目录排除表（TRANSIENT_DIRS）必须显式声明。 [E] 05 §2 字段 8 风险行                              [07:236-237]
L-8 熔断与状态可见：paused / GRADUATION_REVIEW_SUSPENDED 必须可查询；召回面已知坏掉时禁止按零使用归档。 [E] A8⑧  [07:238]
```

## 4. 待确认与暂缓事项

Round 2 明文「本轮**未**用默认值填满」的三处 DEFERRED，逐条原样保留 `[07:245]`：

| 编号 | 未定内容 | Round 2 的处置 | DEFERRED id（registry） |
|---|---|---|---|
| DEFERRED-1 | 墙钟兜底阈值（最低驻留天数）：需至少一仓真实使用统计；14 的 14d/30d 是**未配真实分布的经验常数** | §3.5 的墙钟兜底只写「存在这一用途」，不写数值；数值留给实现阶段作为配置项且必须带来源标注 | `DEFERRED id DEFERRED-1` `[07:248-251]` |
| DEFERRED-2 | 机会数分母在 Compiler 侧是否成立（06 的 use 来自宿主 `PreToolUse(Skill)`/`Read`；本编译器是否有等价真实消费事件接口**未证**）；另需 06 的跨进程原子性与 worktree 场景两项 | 仅在埋点闭环（事件 → 写入者 → 消费者 → 测试）可指认时 §3.5 主判据才成立 | `DEFERRED id DEFERRED-2` `[07:253-258]` |
| DEFERRED-3 | probation + capacity 在无人值守下的稳定性（本轮无任何仓提供无人值守运行结果） | 历史设计仅通过容量机制淘汰试用期结束后的条目 `[E]`，**不把容量数值写进策略**；保留 L-8 熔断作为兜底而非解法 | `DEFERRED id DEFERRED-3` `[07:260-264]` |

重开条件三条（非参数，一并保留以免丢失）`[E]`： `R-L1` 15 确认 `expires_at` 为 fail-closed 并给出测试 → 重议明示 TTL 自动硬删（门票 + grace 仍保留）→ `DEFERRED id DD-4-sub30` `[07:270]`；`R-L2` 若引入任何浮点分数判据，前提三条（唯一 Owner、系数经离线评测、容量旋钮与其他效果解耦）→ `DEFERRED id DD-4-sub31` `[07:271]`；`R-L3` 若条目量级始终远小于容量上界（06 的 project 50 / global 20 属技能池尺度），通过容量竞争淘汰条目的机制可能不必要 → `DEFERRED id DD-4-sub32` `[07:272]`。

本文件未消解、且 Round 2 自身即标 UNKNOWN/参数未定的条目（原文照录）：
- `deletion_grace_days` 只有**参照值 180**（来自 `15:retention-decay-formula`），本项目未裁决 → 代码侧 `kd_lifecycle.py:124-140` 直接返回 `"UNKNOWN"`，并在 docstring 里标 `DEFERRED id DEFERRED-3`，schema 的 enum 固定为 `[None]`。 `[07:91]`
- λ 数值（15 = 0.02 / 10 = 0.01）互不校准且未经离线评测 → `UNKNOWN`，本文件不采信任一值。 `[07:197]`
- `expires_at` 解析失败语义 = `UNKNOWN`。 `[07:207]`
- 永久删除缺显式确认与 host 级授权，Round 2 写「未闭合项（必须留为未闭合）」。 `[07:95]`
- `hard-deleted` 不是状态：本文件 §1 图中它是行消失，不物化（`[07:36]`）。
- 容量数值（project 50 / global 20）在 Round 2 只作为「属技能池尺度」的参照出现，未裁决给本编译器 → `UNKNOWN（07 未裁决数值）`。 `[07:272]`

## 5. 历史源码对照

以下保留历史构建时点的只读观察，不是本轮验证结果。对照对象：`../scripts/kd_lifecycle.py` 的 `TRANSITIONS` / `ACTIONS` / `NOT_ACTIONS` / `ACTION_POST_STATE`，以及 SC05 `schemas/lifecycle-record.schema.json` 的 `lifecycle_state.enum`（模块在调用时读 schema，见 `kd_lifecycle.py:96-97`）。均为只读 import 推导，未运行测试。

| 项 | Round 2 | 代码实测 | 结论 |
|---|---|---|---|
| 存储态集合 | 6 个：`candidate, active, superseded, archived, rejected, failed` `[07:9-26]` | SC05 `lifecycle_state.enum` = 同 6 项，同序（`kd_lifecycle.state_enum()` 返回 `['candidate','active','superseded','archived','rejected','failed']`）；`kd_lifecycle.py:67 EXPECTED_STATES = 6` | 一致 |
| `stale` 不是状态 | 只作只读派生视图，不物化 `[07:32]` | 不在 enum 中；`check_field_set()` 对 `stale/tombstone/probation/dormant/deleted/hard-deleted` 六个名字做 `FORBIDDEN_STATE` 拒绝（`kd_lifecycle.py:158-161`，理由串引 `07 §1.1, 07:36`）；`kd_gate.py:73-78` 记录 Wave 0 曾物化 `stale` 并已改由 S17 单一权威供边 | 一致 |
| `failed` 存在且与 `rejected` 分离 | `[07:25-26]` | enum 含 `failed` 与 `rejected` 两项，各自独立成态；`rejected → candidate` 需「新的真实证据」`[07:25]`、`failed → rejected` 需「人判定不重试」`[07:26]`，代码两条边分别在 `TRANSITIONS[("rejected","candidate")]` 与 `TRANSITIONS[("failed","rejected")]` | 一致 |
| 边的条数 | Round 2 未给总数（只给 §1 表的进出转换列 + 图 `[07:12-16]`） | `len(TRANSITIONS) = 11`，逐条：`candidate→active/rejected/failed`(3)、`active→superseded/archived/active/rejected`(4，其中 `active→active` = A2 的 MERGE「幸存伞形 → active」`[07:22]`)、`superseded→superseded`(1，复活清门票，仍是同一状态 `[07:23]`)、`archived→active`(1 `[07:24]`)、`rejected→candidate`(1 `[07:25]`)、`failed→rejected`(1 `[07:26]`)。每条边自带 `07:2x` 引用串 | 一致（11 条边可全部回查到 §1 表的转换列） |
| `tombstone` 不建状态 | 折叠为 `tombstoned_at` 列 `[07:33]` | 不在 enum；`TRANSITIONS` 注释写明「a tombstone is NOT a state: `07:23` keeps the row inside superseded and writes the column」（`kd_lifecycle.py:189`） | 一致 |
| 8 动作 + 2 受限特例 | A1–A8 + MOVE/AUTOMATE 不算第 9/10 个动作 `[07:40]` `[07:131]` `[07:146]` | `ACTIONS` = `('ADD','MERGE','UPDATE','SUPERSEDE','DELETE','REINFORCE','DECAY','ARCHIVE')` = 8；`NOT_ACTIONS` = `('MOVE','AUTOMATE')`，`assert_transition()` 对二者抛 `NOT_AN_ACTION`（`kd_lifecycle.py:207-209,244-248`） | 一致 |
| 可逆性 | A5 DELETE 为 false，其余 true `[07:93]` `[07:48]` 等 | `ACTION_REVERSIBLE` 中仅 `"DELETE": False`，其余 7 项 True（`kd_lifecycle.py:221-224`） | 一致 |
| 执行者 | DELETE = `[HUMAN]` 唯一人工动作 `[07:94]` `[07:91]` ⑥ | `HUMAN_ONLY_ACTIONS = ("DELETE",)`（`kd_lifecycle.py:226`） | 一致 |
| 后置状态 | 各动作文本的「后置状态」行 | `ACTION_POST_STATE`：ADD=active `[07:47]`、MERGE=superseded `[07:58]`、UPDATE=active `[07:70]`、SUPERSEDE=superseded `[07:81]`、DELETE=None `[07:92]`、REINFORCE=None `[07:103]`、DECAY=None `[07:114]`、ARCHIVE=archived `[07:125]`。`None` 即 A6「不产生新行、不改状态」与 A7「派生分数变化，不是权威态」 | 一致 |
| 未裁决数值 | grace 天数未定 `[07:91]`；容量池数值未定 `[07:272]` | `deletion_grace_days()` 在 SC05 enum ≠ `[None]` 时抛 `DEFERRED_VALUE_ADOPTED`，否则返回 `"UNKNOWN"`（`kd_lifecycle.py:124-140`） | 一致（代码没有替 Round 2 拍板） |
| 新出现的缺口（代码侧自报，非 Round 2 文本） | Round 2 §1 的转换列未写 `active→failed`，也未写 `superseded→archived` | `assert_transition()` 的拒绝文案内嵌 `/ IMPLEMENTATION_GAP: active->failed and superseded->archived have no adjudicated edge (07:22, 07:23)`（`kd_lifecycle.py:269-270`） | 两侧一致：Round 2 确实未裁决这两条边，代码选择拒绝而不是补边。本文件不补 |
| 行号引用漂移（不影响行为） | — | `kd_lifecycle.py:127` 把参照值 180 标为 `07:87`，实际该行是 `### A5 DELETE` 标题；值在 `07:91`。SC05 `$comment` 把状态守恒声明标为 `07:35`，实际在 `07:36`；另标 `07:12-33` 指 §1 表，表体实为 `07:19-26` | 不一致（仅引用行号偏差 1–6 行，正文语义无冲突）。两处均未改动，交由 integrator 决定是否收敛 |

预算：本文件是四份里最长的一份（尺寸与 `kd_budget.py` 实测见 `.distill/round-4/W4-A-REPORT.md`）。`kd_budget.py --ladder` 的 level 2（单份 reference 全文）`caps: []` 且 `unbudgeted` 明写「no byte/line cap was adjudicated for a single reference file: see compiler_prompt_max_chars (D09-3)」→ 本文件的尺寸检查为 **unbudgeted**，不得称 passed；历史项目指令链门槛不再应用于本 Skill 的按需参考资料；历史报告只供对比，不作为当前拒绝依据。
