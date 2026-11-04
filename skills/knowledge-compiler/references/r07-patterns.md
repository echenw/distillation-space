# R07 — 提炼可复用的规则

把具体经验写成别人能用的规则：说清怎么做、为什么做、何时适用和何时不适用。名称可由 AI 建议，正式身份由代码确定；单次成功不自动代表普遍有效。

历史来源： `.distill/round-2/04-DETERMINISTIC-VS-LLM.md` 行 6（`:52`）、行 7（`:53`）及其裁决 C3（`:79`）/ C4（`:80`），`11-FAILURE-MODES.md` §0.3 第 3 条（`:61`）与 §8 D11-2（`:219`），`02-FINAL-MECHANISMS.md` 的 CM-18（`:152-160`）/ CM-19（`:163-171`），CM-19 的过度泛化判据原文取自 `_distill` 输入侧引用（见 §3 逐条出处）；生成 2026-10-06，wave 4。
状态说明：本文说明正式知识流程的设计依据，历史检查仅供追溯，不替代本轮证据；普通材料整理和源码维护按 R06 执行。具体行为以 `../scripts` 为准。

---

## 1. Pattern identity：唯一归属 = 代码派生的 canonical key（04 行 6）

`04:52` 原文（行 6 Pattern identity，Deterministic 列 = **唯一**）：

> `canonical key 由代码从归一化字段派生（trim / strip .md / lowercase / _+空格→- / kebab slug / scope 三元组 / hash）`

Small LLM 列（同一行）：**「◐ 只允许提案一个人类可读名字，且必须被代码 canonicalize 后才存在」**；Judge / Human = 无。
归一化算子的**顺序**在管线里固定：`04:104`「10 身份键归一化　det」。

## 2. C3 裁决：为什么必须写成「模型可以命名」这一显式约束

`04:79` 原文（裁决列，说明整理）：

> **采 09 的形式化表述**。二者结论等价（唯一判据 = 代码 key），但 06 未写出「模型可以命名」这一合法剩余位置；写成显式约束才可在实现上校验（L1 见 `05-DATA-MODEL.md`）。

- 口径对照（同表 Agent 06 / Agent 09 两列，`04:79`）：06 = `deterministic`；09 = `deterministic + 「模型只准提案名字，随后必须被代码 canonicalize」`。
- 含义：C3 的产出**不是**把命名权给模型，而是给「模型可提名 + 代码必归一」这个组合一个可校验的形状。模型给出的名称不能直接充当身份或计数依据（I-1，`04:15`）。

## 3. Abstraction：主力在模型，判据在 judge（04 行 7 + C4）

`04:53` 原文（行 7 Abstraction）：

> Deterministic 列：`◐ 边界与量闸（候选体积/来源数门）+ 最低层落地阶梯（零 LLM 时的落点）`
> Small LLM 列：`**主力**：根因泛化是语义操作，无确定性算子`
> Judge 列：`◐ **高风险过度泛化判据**：用「维护者会不会写这条」替代两两重叠评分；动作优先级 + 出生即伞形 + 同轮强制 reconcile`
> Human 列：`无`

C4 裁决原文（`04:80`，逐字）：

> **加入 judge 列**（06 无）。理由：CM-19 簇的最弱与最强实现形态都是同一条 prompt-instruction 机制（`09:anti-overgeneralization-prompt-rules`，n_ev=5），即语义侧不可替代；而过度泛化是唯一能污染常驻层的写作错误，故高风险分歧升 judge。judge 判据采用 `06:reflector-compare-first-reconcile` 的**动作优先级 + 同轮 reconcile**，**不引入评分器**（这是有证据的形态，非本 Agent 发明）。

判据三件的出处转录（本轮可读到的原文，非本文发明）：
1. **「人类维护者会不会写这条」替代两两重叠评分**：`.distill/round-2/_inputs/synth-b-policies.json:461`（DD-6 的 judge 列原文）「需要（仅高风险）：过度泛化判据用『人类维护者会不会写这条』替代两两重叠评分，autoharness 用动作优先级 + 出生即伞形 + 同轮强制调和而非评分器」。
2. **出生即伞形**：同一句；并见 `_inputs/worker-caveats.json:538` 的四条 prompt 不变量清单「比较优先序、出生即伞形、同轮强制调和、只报提案不报结果」，其限定同样转录：「价值高，但 action 枚举、工具名与 level 语义必须换成目标层契约。」
3. **同轮强制 reconcile**：`.distill/round-2/agent-11-lifecycle.json:53`「同轮强制 reconcile：凡本次新陈述取代旧陈述，必须同批 stage patch 并引用本集证据」；其强制形态见同文件 `:36`「…否则整批拒绝」。吸收门（`absorbed_into` 缺失或指向不存在的伞形 ⇒ 整条 intent fail-closed 拒绝）见 `agent-11-lifecycle.json:260`。
- 禁止评分器：`04:80` 末句「**不引入评分器**」。这与 `04:86`（C10）禁止「同一把尺子既做循环又做验收」、`08:79` 禁止以 `> 0` 作阈值同族。

## 4. CM-19 的断裂论证与实现口径

`02:167`（CM-19「去掉它之后的断裂 / 裁决过程」）原文：

> 过度泛化的规则不可执行、被忽略，下轮同类问题再写一条新规则，指令文件单调增长。本簇与 CM-31/CM-51 是膨胀的唯一前置闸门。采纳 Agent 14 的诚实限制作为实现口径：**抽象质量不可自动验证，所以 lint 只能是代理指标不能当权威**（该分界由 CORE CM-42 承载）。

簇事实：CM-19 stage=abstraction ｜ Round1 tier=MUST ｜ needs_llm=True ｜ det_candidate=True ｜ CORE（`02:165` 的 stage 行）；cp=5 / members=7 / worker 03,04,05,09,10（`02:501`）。
最简实现参照（`02:172`）：`09:anti-overgeneralization-prompt-rules`（VERIFIED，最弱实现形态=prompt-instruction，n_ev=5，项目=memsearch）——**注意**：该簇最弱与最强形态同为 prompt-instruction，这正是 C4 升 judge 的理由（`04:80`）。

## 5. CM-18 的复发工作流判据

`02:156`（断裂论证）的历史摘述：

> 没有复发门，一次性动作也会被固化成 skill，技能库爆炸无法靠再加规则收回。拒绝 Agent 15 ATT-04 对本簇的降级：默认关是对无人监督自动改写长期资产的防御（属 CM-14/CM-35 议题），不能证明提炼重复工作流这个动作可省；该历史论证把重复工作流视为 Skill 提炼的主要对象。Agent 14 指出输入受限时实现有界（80-150 行脚手架 + 每候选 1-2 次模型调用）。

- 簇事实：CM-18 stage=pattern-detection ｜ MUST ｜ needs_llm=True ｜ det_candidate=True ｜ CORE（`02:154`）；cp=4 / members=5 / worker 01,09,10,14（`02:500`）；依赖 `CM-04`、`CM-19`、`CM-27`（`02:157`）。
- **正式知识晋升的复发判据不是模型说的**：计数门在代码侧 —— 管线 `04:96`「13 复现计数 + 阈值门　det　← 模型无权裁决」，且 `04:95`「12 根因抽象/umbrella 提案　llm　← 必须排在计数门之后」。即 **先门后抽象**，抽象只为已达标模式花钱（`04:110` 第 3 条省钱事实）。
普通材料整理、规则提案和已授权的 Skill 源码维护按 R06 执行；不限定为重复工作流这一种输出，也不要求先达到正式知识晋升的计数门。单次材料仍需写清局限，不能假装为重复证据。

- ATT-04 对 CM-18 的攻击与其判定转录在 `11:122`（判定＝**需第三轮**），本文不改判。

## 6. 身份分层的三条（05 §5.1，供 schema 接线用）

`_dispatch/w4c.json:53`（SC03 行）转录：`05` §5.1 identity 分层 = 「L0 精确等值 / L1 nearMatch 仅提示 / L2 embedding 不采用」，且 canonical key「由 S05（代码派生 canonical key）」产出。
L2 不采用 embedding 的裁决在 `12:213`（O07）：「DD-2 判定 L2 不采用 embedding 自动聚类；`07` §3.1 使零模型最坏结果是「不合并」而非「错合并」」。

## 7. 零模型下的抽象出口（不得猜）

本节说明包内模型接口没有 responder 时如何处理正式管线，不能据此假定当前宿主 AI 不可用。宿主直接阅读材料并提出有来源的候选，按 R06 执行；提案不能自行批准。

`04:119` 统一降级规则：「**每个模型插入点在零模型下的正确出口都是「不裁决 + 保留 + 标记」，绝不是猜一个**」。
`04:123`（#12 抽象）具体落点：「抽象 → 落 `04:lowest-tier-promotion-ladder` 的最低层（注释/引用/文档），不泛化」。
`04:128`：不可被零 LLM 替代的只有两件事——**跨措辞判重**与**根因泛化**；二者都只产提案、不写盘。

## 待确认与暂缓事项
- `DEFERRED id D11-2`（`11:219`）：**身份 key 的规范化派生算法未定**（`ATT-06`：05 的派生算法未定义 ⇒ 机制即虚构；`CM-25` 的 `simplest_impl` 被记为 anti-pattern）。需补：≥1 个项目的 NFKC/slug 规范化实现 + 规范化测试向量集。本文 §1 列的算子清单是 `04:52` 的转录，**不等于**派生算法已定案。
- `DEFERRED id D6-a`（`04:192`）：Pattern identity 的 **canonical 字段选择**与 **hash 位置**未定；「缺该实测 → 维持 canonical+hash 严格等值」。`04:196` 明文「**本文不把 D6-a/b/c 用默认值填满**」。
- `DEFERRED id DM-1`（`05-DATA-MODEL.md` §7，经 `../scripts/kd_identity_key.py:114` 的 `IMPLEMENTATION_GAP: canonical field list / DEFERRED id DM-1` 转录）：最终 canonical 字段清单仍未定。
- `DEFERRED id DD-2`（`_dispatch/w4c.json:220` O08）：`CM-26` exact-vs-similarity-dedup **禁入 Core**，等跨仓真实近重复样本（含中文/语序变化，以 `11` 的 8 组对抗用例为起点）；「提前实现等于替 Round 2 拍板」。
- `DEFERRED id DD-6-b`（`04:193`）：冲突解决的低风险/高风险量化门槛无第一轮证据。
- Round 1 元数据缺陷登记（不回改）：`11:179` M-8「`CM-25` 的 `simplest_impl` form 记录为 **anti-pattern**，却作为该簇最简实现存在；`CM-24`/`CM-25` 同语义两簇」；`02:533` 亦记 CM-25「区分两层：必须有确定性 identity key 属必要性；key 的具体语义属 DD-2 未定」。
- 52 条未定参数收录在 `.distill/round-3/DEFERRED-PARAMETERS.yaml`，本文一条都不关闭。

## 历史源码对照
- `../scripts/kd_identity_key.py:67` `PIPELINE_OPS = ("nfkc", "trim", "strip_md", "lower", "underscore_space_to_hyphen", "kebab_slug")` —— 与 `04:52` 括注的六项算子**一一对应且顺序一致**（文档写 `trim / strip .md / lowercase / _+空格→- / kebab slug / scope 三元组 / hash`，其中 scope 三元组与 hash 在代码里是键合成阶段，不算子）。`:65-66` 注释：「Anything outside this set is refused rather…」，即允许清单外算子拒绝执行 —— **一致**。
- `../scripts/kd_identity_key.py:64` `TRIM_ONLY_OPS = frozenset({"strip","trim"})` + `:314-316` `if len(fields) == 1 and op_set <= TRIM_ONLY_OPS: … "code": "TRIM_ONLY_IDENTITY"` + `:324-325` `TRIM_ONLY_PIPELINE` —— `12:522` 闸 3「禁止单字段 strip/trim 作身份」在代码里是可执行守卫，非文档承诺 —— **一致**。
- `../scripts/kd_identity_key.py:386-391` `derive_key` 先过 `audit_derivation`，违例 `raise IdentityGuardViolation`（`:141`）而非返回 key；退出码 `:56` `EXIT_IDENTITY_GUARD = 2`，与 `12:113`（S05「2=出现单字段 strip/trim 作身份」）一致 —— **一致**。
- `../scripts/kd_identity_key.py:88-90`：NUL 分隔的 canonical 字段 join 与 `||` 分隔的显式 Pattern-Key 轴，对应 `:13` 转录的 `05:122`「identity = sha256( canonical 字段 NUL-join )[0:40] || 显式 Pattern-Key 字段」—— **一致**。
- `../scripts/kd_identity_key.py:103-115`：字段清单自标 `PROVISIONAL-CANONICAL-FIELD-SET`「this list is the adjudicated MINIMUM, not a decision about which fields are canonical forever」并登记 `IMPLEMENTATION_GAP: canonical field list / DEFERRED id DM-1` —— 与 §「D6-a / DM-1 未定」**一致**（代码没有把未定参数写成已定案）。
- `../scripts/kd_identity_key.py:115-118`：`cohort.path` 明确**不是** canonical 字段，而是 DISTINCT-COHORT 轴 —— 与 `11:61` §0.3 第 3 条「多源相加必须**先按 key 去重再计数**」及 `:59-60` 的分桶键 `(scope × pattern_key)` 相容 —— **一致**。
- `../scripts/kd_dedup_exact.py:75` `SUPPORT_SEMANTICS = "distinct_cohorts_x_distinct_content_hash"` + `:166-185` `support_of()` 只数 DISTINCT 队列 × DISTINCT content_hash —— 与 `11:59-60` §0.3 第 2 条、`04:96` 步 13 一致 —— **一致**。
- `../scripts/kd_dedup_exact.py:63` `EXIT_SUPPORT_REFUSED = 3` + `:104-138` `audit_counters()`：未登记写者或裸整数计数器一律拒绝（`:23` 注释「REFUSED (exit 3)」），且 `:27`「no merge operator at all, and an input that asks for one is refused」—— 对应 `11:61`「**禁止 N 份计数实现**」—— **一致**（代码用拒绝而非约定表达）。
- `../scripts/kd_dedup_exact.py:201-206` `canonical_of()`：canonical = 字典序最小 locator，回指 `05` §5.2「canonical = 字典序最小文件名」；`04:50`（行 4）亦为「normalize → 全文相等分组 → 字典序最小为 canonical」—— **一致**。
- `../scripts/kd_dedup_exact.py:62` 继承 S05 的 `EXIT_IDENTITY_GUARD = 2`，`:208` `identity_of()` 对 trim-only 身份 `raise IdentityGuardViolation` —— 判重层不另建第二套身份守卫，Owner 仍是 S05 —— **一致**。
- 本文件**未核对**（不在本切片范围）：`04:52` 提到的「规范化测试向量集全通过」是否已由测试覆盖 —— 该断言在施工图里的落点是 `12:727`（§16 自检清单第 **10** 行），而 `../scripts/kd_identity_key.py:15` 把同一要求引作「`12-SKILL-DESIGN-BRIEF.md:725 item 10`」（`:725` 实为清单第 8 行）——**行号相差 2、条目号一致**，核对归 R15 / 集成方，本文只登记数字。
