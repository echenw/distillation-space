# R02 — 确认工作边界

先分清谁负责哪件事：AI 阅读材料并提出方案，脚本做可重复的检查，人工批准正式知识写入。普通任务看入口说明；正式入库或排查执行问题时，再读本文件相应节，当前运行细节在 §8。**特别区分**：工作区 `results/` 是经用户授权维护的当前综合成果，不是 S12 的 `store/records`；下文模型不得直写权威记录的约束针对正式知识库，不取消正常工作区的受控文件编辑权限，也不自动授予该权限。

历史来源： `.distill/round-2/04-DETERMINISTIC-VS-LLM.md` §3（行 41–70）、§5（行 92–111）、§6（行 113–129）、§7（行 131–170），生成于 2026-10-06，wave 4. Citation prefix map: `04:` = `.distill/round-2/04-DETERMINISTIC-VS-LLM.md`，`06:` = `06-PROMOTION-POLICY.md`，`07:` = `07-LIFECYCLE-POLICY.md`，`12:` = `12-SKILL-DESIGN-BRIEF.md`。行号保留来源整理时点的定位，不代表本轮工作树行号。
状态说明：本文供参考；具体行为以 ../scripts 为准。 本文件是转写稿，不是新裁决；Round 2 未定的参数在文末原样列出，未被本文件补齐。

---

## 阅读导航

- 1. 骨架与三条硬不变量
- 2. 边界矩阵（16 个必需 operation + 4 个附加行）
- 3. 历史 23 项职责清单与现行执行顺序（18 确定性 / 4 模型插入点 / 1 人工门）
- 4. 零 LLM 降级出口
- 5. 必须内嵌的四条反例
- 6. 待确认与暂缓事项
- 7. 历史源码对照
- [8. 当前运行边界（按需）](#8-当前运行边界按需)

## 1. 骨架与三条硬不变量

三层：**确定性代码拥有事实与门；便宜模型拥有语义判断与写作；judge/人工只拥有不可逆或高风险分歧。** `[04:11]`

```text
I-1  模型产出的任何标识符，未经代码 canonicalize + 内容寻址派生，不得进入任何计数器或门。 [04:15]
I-2  模型无写权：只有只读/提案通道；durable 写与删除只有一条由代码持有、人批准的事务入口。 [04:16]
I-3  模型解析失败不得换一套 schema 重解释同一份输出；失败保留原输出并如实标失败（retried / unresolved / failed），
     不产生假成功，不绕过证据门。 [04:17-18]
```

违反 I-1 或 I-3 的实现形态判 **REJECT**（不是 SUPPORTING）。 `[04:21]`

**当前运行契约对齐（R12/S10/S12）：** 人工 G1 与独立 S16 Eval 必须在 S12 权威提交前成为可信输入；R12 的 N26/N27 仅形成提交意图，N28 写前验证，S12 才是唯一权威 Writer。R12 的历史 R0 无人分支当前 `DEFERRED/REFUSE`，不得凭“机械可判、可逆、幂等”获得任何权威持久写权限；独立用户授权的普通 Skill 源码维护也不是 S12 的知识晋升。

## 2. 边界矩阵（16 个必需 operation + 4 个附加行）

图例（原文）：每格只有一个答案；`唯一` = 该行只允许确定性执行；`◐` = 允许但非默认。 `[04:43]`

| # | operation | Deterministic | Small LLM | Judge | Human | 历史出处 |
|---|---|---|---|---|---|---|
| 1 | Evidence parsing | **唯一**：JSONL 逐行 parse + 事件允许清单 + `normalize_excerpt` + **scrub 早于 truncate 的顺序契约** | 无 | 无 | 无 | `[04:47]`
| 2 | Hashing | **唯一**：sha256 + 定长前缀 + 内容寻址 id + scope 三元组 + keyed-lock 幂等 | 无 | 无 | 无 | `[04:48]`
| 3 | Schema validation | **唯一发证人**：每阶段独立契约（detection/proposal 两套）+ 有限枚举 + fail-closed 归一 + 结构 lint + escape 预检 | ◐ 仅「校验失败后一次有界修复重试」，重试后必须再走同一确定性门 | 无 | 无 | `[04:49]`
| 4 | Dedup（精确） | **唯一**：normalize → 全文相等分组 → 字典序最小为 canonical → pending remove 即幂等 | 无（这层的价值就是故意的盲：paraphrase 永不检出） | 无 | 无 | `[04:50]`
| 5 | Similarity | **候选生成层唯一负责**：Jaccard / keyword overlap 便宜 proxy，阈值可测，把 O(n²) 压到常数级；命中为空即跳过语义判定 | **判定层**：只在 candidate 内判「是否同一条」（Already Covered 含不同措辞，属语义） | ◐ 仅当合并会销毁内容 | 无 | `[04:51]`
| 6 | Pattern identity | **唯一**：canonical key 由代码从归一化字段派生（trim / strip `.md` / lowercase / `_`+空格→`-` / kebab slug / scope 三元组 / hash） | ◐ 只允许提案一个人类可读名字，且必须被代码 canonicalize 后才存在 | 无 | 无 | `[04:52]`
| 7 | Abstraction | ◐ 边界与量闸（候选体积/来源数门）+ 最低层落地阶梯（零 LLM 时的落点） | **主力**：根因泛化是语义操作，无确定性算子 | ◐ **高风险过度泛化判据**：用「维护者会不会写这条」替代两两重叠评分；动作优先级 + 出生即伞形 + 同轮强制 reconcile | 无 | `[04:53]`
| 8 | Promotion | **唯一裁决**：常量阈值 + 单调计数 + `last_attempted_count` 条数比较（重试必须是新增第 N+1 条证据）+ 到期门（input digest + `min_interval_hours` + `O_CREAT\|O_EXCL`）+ 阈值 AST 防漂移 | **无裁决权**（只有提案权，见 I-1） | 无 | **需要**：durable 写的批准门（CM-35） | `[04:54]`
| 9 | Conflict resolution | **检测半唯一**：supersede 链 + `is_latest` + validity interval + scope/trigger 重叠 + 同形重复 + 唯一匹配 delta 约束；FAILED_RULE 八维中 4 维在此 | **调和半**：wrong trigger / ambiguous / ignored 的语义归因、conflicting instruction 的意图调和 | ◐ **仅不可调和时** | ◐ 不可调和时交人类批处理 | `[04:55]`
| 10 | Rule merge | **准入与写序唯一**：原子写（tmp+rename+fsync）+ 唯一写者 + stale-write guard + 写前全量准入 + `absorbed_into` fail-closed | **内容半**：两条规则正文合成一条是文本语义工作；有界打补丁循环 | 无 | **需要**：写盘批准 | `[04:56]`
| 11 | Skill merge | **剪枝半，且是必需半**：CM-22 簇级 Round 1 判语 `needs_llm=false` + `det=true`（不是本轮推断）；`absorbed_into` 缺失即拒；候选过滤；整目录快照归并 | ◐ 提炼半，**默认关闭**（14 的 LLM umbrella pass 是 gated/opt-in） | ◐ 仅当合并会删除 | **需要**：删除性归并 | `[04:57]`
| 12 | Eval generation | **唯一**：语料冻结 + split 契约 + exam isolation gate + labeled fixture + 生成后再过 schema 校验 | ◐ 题面生成：**每次晋升一次**，不随语料规模放大；从已有 artifact 自举合成 | 无（rubric 落成 schema 后回到 #13） | 无 | `[04:58]`
| 13 | Eval scoring | **唯一主判**：before/after holdout 差值、floor/ceiling bench corpus、mutation-lite「测试会咬」、触发命中、flaky/unavailable 分类、失败累积一次性退出、changed-path 选择、付费跑前 dry-run preflight | ◐ 仅散文质量类 rubric 项（该列证据为 OPTIONAL 级） | **DEFERRED**（见 §6 第 3 项，即本文件 §5） | 无 | `[04:59]`
| 14 | Lifecycle | **唯一**：计数器 + 时间锚点（显式排除 `created_at`）+ 状态机 + 零使用=证据缺失 + 播种时钟 + 坏配置回落默认 + 跨进程 claim + adherence 分母门 | 无 | 无 | 无（`pinned` 由人设置，转换本身自动） | `[04:60]`
| 15 | Deletion | **执行与回滚唯一**：唯一删除通道 + 归档优先 + 整目录 rename + 双层回滚 + 活进程检查 + 幂等 + dry-run | 无 | 无 | **授权门唯一持有者**：确认 flag 是契约本身 | `[04:61]`
| 16 | Provenance verification | **唯一且为主**：从 agent 自己的事件流旁路取证 + 与模型自报清单 **exact set equality** + 拒批外引用 + citation 回写原始 session path + 写时 origin channel + 分片审计日志 + git checkpoint | ◐ **仅用于定位证据**（「这条主张可能对应哪段 transcript」），从不用于证明 | 无（集合等式可判定） | ◐ 抽样审计 | `[04:62]`
| 17* | Capture / ingress gating（附加） | **唯一**：类型化边界 `Sanitized<T>` 唯一构造函数（无其他 ingress）+ scrub 早于 truncate + 硬编码模式 + 长度锚定 + spool 不丢 + 自产证据排除 | ◐ 仅残余歧义（某段文本是否敏感） | 无 | 无 | `[04:63]`
| 18* | Retrieval / ranking（附加） | **唯一且为主**：FTS5 + 词法 entity match + link-neighbor RRF + typed scope 三元组 + fail-closed scope 解析 + progressive disclosure + 只认 `is_latest` | 排序**不得**交给模型；查询扩展可选 | 无 | 无 | `[04:64]`
| 19* | Budget / truncation（附加） | **唯一**：count+bytes 双上限（单条超限仍放行，队列不可卡死）+ 水位仅成功时推进 + 显式 token 估算 + 整块跳过不截断 + 阈值 AST 防漂移 + 禁止调高数字 | 无 | 无 | 无 | `[04:65]`
| 20* | Projection / publish（附加） | **唯一**：单一 canonical 源 + 多目标投影 + 投影与源失配即 fail（`render-roles.sh --check`）+ 不加 generated-by 头（避免改变进入模型的 prompt 字节）+ catalog parity | 无 | 无 | ◐ 仅 catalog 准入的语义分类（`shared`/`runtime`/`drift`） | `[04:66]`

行 17–20 为 Agent 09 超出 SPEC §5 的 4 个附加 operation，一并纳入。 `[04:68]`
`#`8 的 human 列与 `#`10/#11/#15 的人工门在实现上是**同一个**人类闸门（管线第 22 步），不是四道门。 `[04:69]`
冲突裁决总则：**门与写序归代码，语义判断归便宜模型，不可逆与高风险分歧归 judge/人工；两个口径冲突时，取「约束更多但成本不升」的那一侧，并要求写出可判定的失败出口。** `[04:90]`
矩阵左侧的 12 条 06/09 口径冲突逐条裁决（C1–C12）不在本 reference 的 `content_sources` 内 → 见 `04:71-89`，本文件不转写。 `UNKNOWN（未列入 R02 范围）`

## 3. 历史 23 项职责清单与现行执行顺序（18 确定性 / 4 模型插入点 / 1 人工门）

以下编号是 Round 2 `[04:95–106]` 的**职责编号，不是现在可执行的时间顺序**；尤其 #16 不能早于 #18/#20/#22 执行，#13 的证据计数门实际也先于 #12 的模型抽象。不得按编号直接调度或把这份历史分解当作成功运行记录。

```text
 1 触发捕获(钩子/水位轮询)      det    12 根因抽象/umbrella 提案     llm   ← 必须排在计数门之后  [04:95-96]
 2 逐行 parse + 事件允许清单        det    13 复现计数 + 阈值门          det   ← 模型无权裁决       [04:95-96]
 3 scrub 早于 truncate + 类型门    det    14 Judge：高风险分歧          llm   ← 仅报警触发，常态 0 次 [04:97]
 4 sha256 + scope 三元组 → key     det    15 确定性 lint（六类结构门）  det                        [04:98]
 5 spool + 重试（双路 id 幂等）    det    16 唯一写者原子落盘           det   ← 仅 S12；必须晚于 #18/#20/#22 及 N28 写前核验 [04:99]
 6 到期门（digest+interval+锁）    det    17 provenance 自证 + 账本      det                        [04:100]
 7 schema 校验                    det    18 eval 语料冻结 + split       det                        [04:101]
 8 精确去重                        det    19 晋升规则的 eval 题面        llm   ← 每次晋升一次       [04:102]
 9 近似 proxy 产 candidate pairs   det    20 before/after holdout 打分   det                        [04:103]
10 身份键归一化                     det    21 生命周期 inactivity 状态机  det                        [04:104]
11 语义判重（candidate 级）        llm    22 人类批准：durable 写与删除   human                     [04:105]
                                        23 归档（非删除）+ 双层回滚       det                       [04:106]
```

**当前唯一可执行时序**：采集/净化与身份 Scope → 精确判重/证据计数准入（#13）→ 必要的模型候选/抽象（#11/#12/#14/#19，只产提案）→ S15 冻结、独立运行与 S16 Eval（#18/#20）→ S10 确定性预检与 G1 逐项人审（#22，N25）→ S10 N26/N27 形成提交意图、N28 写前复核完整独立 Eval → **仅 S12 在三通道可信校验后原子提交**（#16，commit point 最后写入）→ 提交后读回/投影、生命周期处理（#17/#21/#23）。N26/N27 没有权威持久副作用；未取得真实 G1/Eval/来源回执时必须拒绝 S12，不能调换先后或以补做事后 Eval 抵销。实际 S10 可能先经 N25 人工门再至 N26/N27；表中的前置关系以 S10 状态边和 S12 写前校验为准。见 R12 §4、`scripts/kd_gate_tree.py` 与 `scripts/kd_write_txn.py`。

历史 Round 2 的**结构拆解**为 23 项职责、18 项确定性、4 个潜在模型插入点（#11/#12/#14/#19）、1 类人工关口（#22），**不是本版运行调用次数的实测**；模型是否实际调用、人工身份及提交结果需要宿主证据，不能从静态拆分推断。 `[04:109]`
成本优化仅为条件性机制：#6 digest 无变化可跳过生成、#9 候选为空可跳过 #11；先过 #13 计数门再进行 #12 的语义抽象。真实模型次数和费用仍待宿主证实。 `[04:110]`
按 stage 的 det_only 占比（Agent 09）：cross-agent-publish 4/4、merge-dedup 5/8、provenance-audit 3/5、validation 4/11、evidence-intake 3/9，而 pattern-detection 0/2、learning 0/4、retrieval-preflight 0/4（这些是 both 集中区，即模型插入点所在）。 `[04:111]`

## 4. 零 LLM 降级出口

三重独立证据（EVIDENCE-SUPPORTED）：`15` ai-memory 把 Zero-LLM default path 写成跨切面不变量 #13（`the system fully works with no provider`） `[04:115]`；`10` agentmemory `zero-llm-synthetic-compression`（原话「默认不花钱、opt-in 才花钱 + 确定性归一化是 capture→learning 的最小可行落地，不依赖模型」） `[04:116]`；`14` hermes-agent 确定性 inactivity walk 常驻、LLM 归并 pass gated/默认关（`DEFAULT_CONSOLIDATE=False`），不变量 `never deletes — archive is the maximum` 使零模型时最坏结果是「不合并」 `[04:117]`。

统一降级规则（**ENGINEERING-INFERENCE**，由三条证据外推）：**每个模型插入点在零模型下的正确出口都是「不裁决 + 保留 + 标记」，绝不是猜一个。** `[04:119]`

| 插入点 | 零模型出口 | 引用 |
|---|---|---|
| #11 语义判重 | 保留双条目 + `possible_duplicate` 标记，永不自动合并 | `[04:122]` |
| #12 抽象 | 落 `04:lowest-tier-promotion-ladder` 的最低层（注释/引用/文档），不泛化 | `[04:123]` |
| #14 冲突 | 记 `unresolved_conflict`，交人类批处理 | `[04:124]` |
| #19 eval | 只跑结构断言与 before/after 的确定性部分，如实标 `eval_status: partial` | `[04:125]` |

不可被零 LLM 替代的只有两件事：**跨措辞判重**与**根因泛化**；二者都只产提案、不写盘，提案还要过 #13/#15/#17/#20/#22。 `[04:128]`
因此模型不可用时系统唯一损失是**新规则产出速度**，不是正确性。 `[04:129]`

## 5. 必须内嵌的四条反例

### 5.1 `02` distill：trim-only 的模型字符串被当作确定性门控身份（违反 I-1） `[04:133]`
门本身完全确定性：`distill/src/scanner/engine.rs:125 MIN_WORKFLOW_MATCHES_FOR_PROPOSAL=3`、`state.rs:159-163`（`matches.len() <= last_attempted_count`）、`.max(count)`、三条单测。 `[04:134]`
但聚合 key 是模型产出的 `workflow_key` 自由字符串：`engine.rs:2927 candidate.workflow_key.trim().to_string()`、`engine.rs:3058` 非空检查；**grep `sha|hash|fingerprint` 在 scanner 身份路径无任何内容哈希**；唯一稳定性保障是 prompt 里一句 `Use stable kebab-case for workflow_key`（`engine.rs:2164`）。 `[04:135]`
后果：同一模式两种拼法各自 <3，门**看起来在工作、实际在系统性否决**，且 Round 1 open_question 原话「The repo has no metric for missed groups」——漏报不可观测。 `[04:136]`
防御（正面实现，全部 VERIFIED）：内容寻址 id，模型不提供 key（`cap_ + sha256(project\0sessionId\0eventId)[0:40]`、`sha256(text)`、双路事件 id `evh_/evc_`）；类型层强制 `Sanitized<NewObservation>` 无 `sanitize()` 之外的构造路径；顺序契约 scrub 早于 truncate；显式 key + 每条规范化规则配行为 eval；系统签发 handle，只有只读工具 recall/read，写永远走回 `_apply`。 `[04:137-148]`

### 5.2 `02` distill：解析失败后换一套 schema 重解释同一输出以绕过 3-证据门（违反 I-3）— **判 REJECT** `[04:150]`
`engine.rs:1278` 的 else 分支用另一套 proposal schema（`RawScanResponse`）**重新解释同一份 `invocation.final_output` 并直接 `write_proposals`**，绕过 `ready_workflows(3)`。 `[04:151]`
致命细节：该分支对应的生产 prompt `build_prompt` **实测已是 `#[cfg(test)]`（engine.rs:2311）**——这条 fallback 服务的输入形态在生产中不存在。 `[04:152]`
聚类归属：CM-43 `dangerous-fallback-antipattern`（REJECT，`needs_llm=false`, `det=false`）。 `[04:153]`
采纳的失败纪律：失败**保留原输出**并标 `retried:true`；超预算**整体放弃**而非降级解释（`summarize.ts:25-41 MAX_SKIP_RATIO=0.5`）；两遍各用自己的 schema；短路要用断言锁住。 `[04:154]`

### 5.3 `05` ECC/skills/rules-distill：全部裁决在 prompt（违反「门必须在代码」） `[04:156]`
实地复核：`repos/ECC/skills/rules-distill/scripts/` **只有 `scan-rules.sh`(1604B) 与 `scan-skills.sh`(3893B) 两个文件**，全文仅命中 `wc -l` 与 `jq length`，对 `sha|hash|key=|similar|dedup|promot` **零命中**。 `[04:157]`
`2+ skills` 门槛、`Already Covered` 语义去重、跨批 dedup **全部只存在于子 agent prompt**；`~800 lines` 总量判据无确定性断言（`scan-rules.sh` 的 `total` 是**文件数**，不是行数）。 `[04:158]`
结论：**只由模型执行的阈值不是阈值，是建议。** `[04:159]`
保留的正确部分：`deterministic-scan-llm-verdict-split` 的分层本身是对的；`Already Covered` 含「不同措辞」的语义判重**确实不可确定性化**——反例针对**计数与门槛**，不针对判重。 `[04:160]`

### 5.4 `04` agent-skills：grep 短语锁散文被结构投影 + `--check` 取代 — **判 REJECT 的确定性形态** `[04:162]`
CM-39 里 `04:reject-phrase-locks-on-prose` 的 form **直接标 anti-pattern**：60 条 grep 断言锁 prompt 措辞的失败教训。 `[04:163]`
替代形态（采纳）：`roles/` 是权威，`agents/*.md` 与 `codex-agents/*.toml` 是投影且**永不手改**，`scripts/render-roles.sh --check` 在投影与源失配时立即失败；工件**故意不带 generated-by 头**；所有权改为带外标记（文档 + `.gitattributes linguist-generated=true` + 会失败的 check）。 `[04:164]`
语义分类放在 `shared.role` 里声明 `id` + `class ∈ {shared, runtime, drift}`，**不合并措辞**。 `[04:165]`
规则：**确定性一侧只断言结构与行为（字段存在、枚举值、投影一致性），永不锁措辞。** `[04:166]`

### 5.5 另两条（已在矩阵中固化，非 dispatch 所指的四条内嵌反例）
阈值漂移：正例用 **AST** 从运行时源码读常量并**禁止调高数字**；**一个阈值只有一个权威来源，且必须被读取而非被复制**。 `[04:169]`
把 provenance/反幻觉交给模型自律：采旁路取证 + 精确集合等式；模型可用来定位证据段，**不得用来证明读过**。 `[04:170]`（详见 `#16` 行，本文件 §2）

## 6. 待确认与暂缓事项

本文**不补齐**任何 Round 2 明文未定的参数。以下 3 项在 `04` §9 以 DEFERRED 移交，且在 `.distill/round-3/DEFERRED-PARAMETERS.yaml`（52 条）中有对应条目：

| Round 2 编号 | 未定内容 | 本轮已收敛 | DEFERRED id |
|---|---|---|---|
| D6-a | Pattern identity 的 canonical 字段选择与 hash 位置 | 唯一归属 = 确定性；scope 三元组必须参与 | `DEFERRED id DD-6-sub40`（另见 `DD-6-sub43`、`DD-6-sub45`） `[04:192]` |
| D6-b | Conflict resolution 的低风险/高风险量化门槛 | 检测归确定性、调和归模型、不可调和归 judge+人工 | `DEFERRED id DD-6-sub45`（三项子参数合并在同一条目中） `[04:193]` |
| D6-c | Eval scoring 是否真正把 judge 放进验收 | 主判 = 确定性；禁止同一把尺子既做循环又做验收 | `DEFERRED id DD-6-sub41`、`DD-6-sub45` `[04:194]` |

其余 UNKNOWN（Round 2 原文即标 UNKNOWN，本文件不消解）：
- 矩阵 #13 行的 Judge 列为 **DEFERRED**，非「无」也非「有」。 `[04:59]`
- `04` 明确：「本文不把 D6-a/b/c 用默认值填满。」 `[04:196]`
- R02 的 `content_sources` 未含 `04` §2（67 簇分布）、§4（C1–C12 逐条裁决）、§8（被拒方案）、§10（重开条件）、§11（许可边界）→ 这些**不在本 reference 内**，需要时读原文件；本文件不转写即不重复其结论。 `DEFERRED id 无（范围切分，非参数缺口）`

## 7. 历史源码对照

对照对象：`../scripts/kd_model_step.py`、`../scripts/kd_gate_tree.py`、`.distill/round-3/SCRIPTS-CONTRACT-MAP.md`。全部为只读 import / 文本解析，未运行测试。

| 项 | Round 2 文本值 | 代码实测值（历史构建时点自行推导） | 结论 |
|---|---|---|---|
| 管线步数 | 23 `[04:109]` | 解析 `04:94-107` 代码块得到 23 个编号步 | 一致 |
| 确定性步 | 18 | 同一次解析中 `det` 计数 = 18 | 一致 |
| 模型插入点 | 4（#11 #12 #14 #19） | `kd_model_step.STEP_CONTRACTS` = 4 条，`pipeline_step` 分别为 `#11 #12 #14 #19`；`kd_model_step.py:284` 的拒绝文案写明「Round 3 adds no fifth」 | 一致 |
| 人工门 | 1（#22） | `SCRIPTS-CONTRACT-MAP.md:62-66` 的 Human gate G1 = 1 条，contract 为「管线 `#22` 人类批准（唯一人工门）」 | 一致 |
| 模型插入点的降级纪律 | #11/#14 只产标记/记录不裁决 `[04:122-124]` | `STEP_CONTRACTS` 中 M1(#11) 与 M3(#14) 的 `advisory_only=True`；M2(#12) 的 effect 为「proposal text only」；M4(#19) 只产题面 | 一致 |
| 模型步数（另一处口径） | 4 `[04:109]` | `.distill/round-3/_inputs/contracts.json` 的 `model_steps` 有 **5** 条（M1, M2, **M2b**, M3, M4），M2b = 「Pattern 命名」即矩阵 #6 行的 ◐ `[04:52]`；`kd_model_step.py` 未给它 STEP_CONTRACTS 键，`kd_gate_tree.py:494` 只在 `NotLandedYet` 文案里提到它 | **不一致（计数口径）**：04 的 4 个插入点 vs Round 3 contract 输入的 5 行。行为面无冲突（M2b 状态即 NOT IMPLEMENTED，提案权），但「4」这个数字在两份 Round 3 产物里不成立。两侧均未按本文件修改 |

预算实测见 `.distill/round-4/W4-A-REPORT.md`；一句话：本文件所在的 level-2「单份 reference 全文」在 `kd_budget.py --ladder` 中 `caps: []`，并在 `unbudgeted` 里明写「no byte/line cap was adjudicated for a single reference file: see compiler_prompt_max_chars (D09-3)」→ 本文件的尺寸检查是 **unbudgeted**，不是 passed。


## 8. 当前运行边界（按需）

审查 S09/S12/S14 或诊断输入与子进程边界时加载本节；普通提炼流程按 SKILL.md 与对应任务 Reference 逐步加载。

S12 写路径审计递归扫描正式 `scripts/` 下所有可发布 Python 源码（含子目录与 `test_` 前缀），并对单文件、扫描总量和目录读取异常实施有界 fail-closed；`SCANNED_SET_INCOMPLETE` 不是 GREEN。发布包与 S12 扫描均明确拒绝 `.so/.dylib/.dll/.pyd` 等原生扩展，以及 `.pyz/.zip/.egg/.whl/.pex` 等可执行 Python 归档；macOS `._*` AppleDouble 附属文件依照正式包规则排除。高风险星号导入、`shutil.copyfileobj`、`os.dup2/dup3`、`zipfile.ZipFile/PyZipFile` 写入模式与 `writestr` 等副作用、外部进程及裸/别名 `getattr` 间接调用均进入 AST 保守检查；合法只读归档与 S06 目录 fd 的 `os.dup` 不因此被误判。原有 R03 外部提取与 S14 历史见证启动、已认证源码向子进程 stdin 管道传输仅有精确 AST 例外；S14 见证与 R03 PDF 管道执行函数**整体 AST**还要通过独立摘要核对，不能保留 `os.write` 语句同时改写其 fd 目标。`prepare_commit` 与 `commit_batch` 在调用依赖之前先检查来源；生产 `commit_batch` 必审 S12 执行源码目录，并核对实际持有的安全依赖对象与模块注册表和来源一致；调用方 `--scripts-dir` 只能追加扫描。**S12 AST GREEN 不保证任意 Python 或外部程序绝无持久写入**，仍需要独立 OS 最小权限、G1/N28/独立 Eval、宿主隔离与正式发布审计。 PDF 提取只向可信本机转换器传递本次来源字节快照；正文上限 12 MiB、诊断及版本输出上限 8 KiB，超时与清理失败受控拒绝。

S14 常规证据引用审计只读；`--against-round1-auditor AUDIT_PY` 是**会执行 Python 的高信任历史对照模式**，必须同时提供从可信独立来源确认的 `--auditor-sha256 EXPECTED_SHA256`。不匹配、未提供、链接或超限文件在执行前拒绝。见证只执行已校验的不可变字节快照（经子进程 stdin 传递），不按原路径重新加载源码；运行上限 20 秒、输出最多 256 KiB，非零退出、超时或清理失败均拒绝 MATCH。见证在 POSIX 独立进程会话中启动，结束时清理该进程组（含仍留在组内的后代进程），而非只终止父 PID；主动脱离该进程组的程序仍需通过 OS 权限隔离控制。摘要、进程组与资源限制**不是任意代码沙箱**，调用者必须确认历史脚本可信、宿主权限受控，禁止直接执行模型建议的脚本路径/摘要。

校验入口 `scripts/kd_validate.py --kind <kind> --input <file>`；完整文档而非一个 `verified` / `approved` 位进入门禁。缺 Schema 返回 `SCHEMA_MISSING`，不当通过。S09 单次 JSON/JSONL 输入（含重试文件）上限 **32 MiB**、单份 Schema 上限 **4 MiB**；超限受控拒绝，不发放 PASS。若同时指定 `--report` 和 `--out`，报告先保持非成功状态，只有合格 `--out` 已写入后才更新为成功报告；输出失败不能留下本次成功回执。 指定 `--report` 时，S09 在路径保护与来源隔离校验完成后、读取输入之前，就为**本次调用**写入 `exit_code=4` 的非成功回执；读取失败也不得让旧成功报告冒充本轮结果。已有 `--out` 文件不会因本轮失败被擅自删除，调用方仍须检查本次退出码与报告。报告的 `schemas_dir` 字段为脱敏标记，不泄露宿主绝对路径。直接 Python API 只接受 Python 原生 JSON 类型（对象键须为原生字符串，容器须为原生 dict/list，拒绝可自定义复制协议的子类），首次输入与通过的修复候选均须复制成独立快照再校验；修复回调抛出异常时保留首轮失败载体并返回 `RETRY_EXHAUSTED`，不会回显回调异常原文或误发 PASS。

正式事务/投影必须显式提供已审政策与 decision_id，并绑定摘要。首发可选择用户批准的 `references/runtime-policy.json`：3 cohort / 3 evidence / 2 task（至少 1 非本会话），间隔与 pending TTL 均 24h。它不是实证最优值，不关闭历史 52 Deferred；`promotion-config.json` 的旧 provisional 基线保留，不自动选择或批准。

单项 CLI 裁决使用 `kd_gate_tree.py --adjudicate CANDIDATE_JSON --policy POLICY_JSON`，不自动选政策；结构查看不需要政策。CLI 与 S12 共用政策文件解析和形状校验，重复字段、非有限数与资源超限受控拒绝；S12 仍另外核对真实来源事实、完整政策摘要和三通道回执。传入政策文件不授予批准或写入权限。

本 Skill 为按需 task。SC10 目前只对已明确归类的特定写入和注入场景保留对应预算，**不提供统一的参考资料加载链硬阈值**。Reference 按任务选择所需标题和内容，按宿主真实容量分段；R12 先读 §1–4，R13 只读所需 action。未确认的限制不得从其他项目推断或强制应用。

projector 从 S12 `locked_snapshot` 生成原样正文、manifest、不可变 generation，仅切换受管 `current.json`。未知/人工修改/Scope/预算/陈旧冲突拒绝并保留。切换后 fsync 失败报 `SWITCHED_NOT_DURABLE`。固定版本 reader 可读完整旧活动版本而保留未引用失败残留；publisher 对残留仍拒绝。两者不安装宿主、不回灌 records、不认证调用方伪造的快照。
