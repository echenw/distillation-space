# R17 §4a 决策链 · story-architecture-and-longform-planning

- 依据：`notes/suite-contract.md`（K2 定稿）、`notes/loss-inventory/raw/story-architecture-and-longform-planning-2026-11-04-r2.md`（K1 r2 表）、计划第 3 节 / 第 6 节 P3 第 5 条 / §6.1 / 附录 A.2 / 附录 B / 附录 C / 附录 E / 附录 F / 附录 G.1。
- 性质：本文件属 `notes/`。**出处只写在每条决策链第 5 项的「来源」小项，不进成品**；成品在 `output/story-architecture-and-longform-planning/`。
- 记账结构：本 skill 的 v0 谱系为 `plot-architecture`（单本结构，→ PL 卡）与 `serialized-volume-planning`（分卷连载，→ SV 卡）。本文件由各分片**追加**各自决策链节：S05a1（plot-architecture a1：SKILL.md／openai.yaml／rules／planning／revision）、S05a2（plot-architecture a2：diagnosis／examples／scope-and-conflicts／decision-rework／source-index／historical-provenance／templates）、S05b1/b2（serialized-volume-planning）。逐条 9 列记账见 `notes/loss-inventory/story-architecture-and-longform-planning-S05a1.md`（LI-ST-001 起；a2 并行片预留 LI-ST-101 起段）；附录 B 扫描见 `notes/quality/story-architecture-and-longform-planning/s05a1-desourcing-selfcheck.md`。
- 写法口径：沿用 `notes/source-synthesis/line-editing-and-proofreading.md` 第二节（S01 校准样例，W3 全体复用）。

---

## S05a1 决策链（W3 主体轮第 7 批）

- 分片：S05a1｜代理：Agent 3｜轮次：W3 主体轮第 7 批｜日期：2026-11-05
- 分片口径：v0 `d23c461:skills/plot-architecture/` 的 SKILL.md（15838 B）＋agents/openai.yaml（663 B）＋references/rules.md（63537 B）＋references/planning.md（14979 B）＋references/revision.md（14862 B）＝109879 B。

### D1 PL-02／PL-04／PL-05／PL-08 的「硬门回潮」怎么找回（v0 裁决被 v3 反转的四组块）

1. **情境**
   - 已知：v0 在返工中把四条旧硬化规则撤销并直接修复进 `rules.md`（RC-01/02/04/05/08），并在 SKILL.md 优先裁决节明言「单线终点、第一段人物欲望、B 型同框结尾均非通用硬门」。r2 表这四条全部 `UNALIGNED?`。逐块比对发现 v3（PL-02/04/05/08）恰好把这四处软化改写回了硬口径：PL-02 规则句删 B 型豁免、步骤 4「标不出的删或并」、步骤 5 只剩「意外但唯一正确」；PL-04 规则句设「首个叙事单元必须」、C 分支「必须在同段…否则不合格」、步骤 1「写不出即不合格」；PL-05 规则句变「逐事件」、A 分支变「唯一合理出口｜通过」；PL-08 步骤 5 变「B 须在同一场/同一画面内并置」（与 v0「不要求同框」方向相反）。
   - 推断：v2→v3 是去来源扫除（比对 v2/v3 diff：改动集中在引文、`-NNNN` 残片、年代、来源锚点），这四处语义收紧不是去来源的必然结果，属去来源时的连带改写。
   - 用户要求：按 r2 与计划 P3 第 5 条找回丢失项，用通用写法；不把缩减幅度当应补回的量。
   - 拿不到的：v2→v3 改写者是否有意收紧的记录。以 v1 融合稿为定性佐证。

2. **区分信号**
   - 走「恢复」的信号：v0 与 v1 都有对应软化表述，且 v3 改写后与其自身其他条目矛盾——PL-02 的「唯一正确」与 v3 自身反例 3「『必然』是程度判断」相抵触；PL-04 的「写不出即不合格」与 PL-04 反例 2「框架/随笔体可另立契约」相抵触；PL-05 的「唯一合理出口」与 PL-05 反例 3 相抵触；PL-08 的「须同框」与 PL-01 反例 3（v3 自己已条件化的「短篇是否保留副线按阅读目标判断」）相抵触。
   - 反信号（走「不恢复」）：只有 v1 有而 v0 没有的表述（如 SP09「不能用新增异常支线强行给概率背书」）；v1 软化而 v3 回到 v0 口径的（判后版有意选择）。
   - 判错的代价：把有意的口径收紧改回去 → 覆盖后版决定；把连带删除当有意调整 → 四处硬门继续误伤开放型、环境开场、主题荒诞与对照并置作品。

3. **两条分支的做法**
   - **A 合并补强**（采用）：以 v0 措辞为底、按现行行文改写，逐处并入 v3 现有条目——PL-01 反信号补 B 型三项转查与「记待查不先删」；PL-02 规则句/步骤 2/4/5 补 B 型豁免、功能先查、开放不锁死；PL-04 规则句/C 分支/步骤 1 补时间范围、允许后置、环境或声音契约、标「需要后续段落」；PL-05 规则句/分支 A 补承重 scoping、充分可解释路径之一、主题荒诞契约；PL-08 反信号/步骤 5/失效条件 1 补 B 型照亮、不要求同框、副线禁令条件化。
   - **B 只在 SKILL.md 加说明、不动规则正文**：判为不够——`plot-rules.md` 是权威正文，流程文件以其为准；不改正文则矛盾保留。
   - 停下条件：无（四处均有 v0＋v1 双重佐证，非两可）。

4. **反例与修复**
   - 推翻判断的情况：恢复后与 v3 基线的其他段落冲突（如 PL-08 恢复「不要求同框」与 SKILL.md §5 PL-08 卡的旧表述冲突）→ 卡片同步改写；PL-04 恢复后 plot-planning §7 的「写不出 → 开篇不合格」出口变硬 → 出口同步加环境/声音契约先查。
   - 修复：改完逐条复查「恢复句无来源指涉、无年代、无审计词、与同卡反例一致」；流程文件出口与权威正文一一对照。

5. **成品落点**
   - `output/story-architecture-and-longform-planning/references/plot-rules.md`：PL-01 反信号、PL-02 规则句＋步骤 2/4/5、PL-04 规则句＋分支 C＋步骤 1＋适用边界、PL-05 规则句＋分支 A、PL-08 反信号＋步骤 5＋失效条件 1＋适用边界
   - `output/story-architecture-and-longform-planning/SKILL.md`：§5 PL-04/PL-05/PL-08 卡、§2 输出四件
   - `output/story-architecture-and-longform-planning/references/plot-planning.md`：§2/§4/§7/§8 出口对齐
   - **来源**：v0 `d23c461:skills/plot-architecture/references/rules.md`（RC-01/02/04/05/08）与 `SKILL.md`（P4 优先裁决节）；v1 `d2003e4:skills/story-architecture-and-longform-planning/references/02-whole-story.md`（SP03/SP04/SP05）、`03-causality.md`（SP08）、`04-opening-and-ending.md`（SP07）；v0 `references/decision-rework.md` §2/§4（只读佐证，实体归 a2）；r2 表 RC-01/02/04/05/08 行；计划 §2.4。

### D2 v0 SKILL.md 的负触发、输入权限与失败出口怎么落进合并版合同（C.3 第 1–3 条）

1. **情境**
   - 已知：v0 SKILL.md 有 10 条负触发、四行输入权限表、失败/退出表；v3 是与 serialized-volume-planning 合并后的合同（35201 B），有转介表与「冲突时」节，但无负触发清单、无输入权限表、路由表缺「缺料或冲突时的出口」列、无主要操作失败出口。
   - 用户要求：C.3 落地——description 补兄弟名、适用与转介写 C.1/C.2 相关行（含 preset-card 双向转介）、路由表两列、主要操作失败出口。
   - 拿不到的：preset-card-generation 成品侧的接收措辞（S07 已定稿，按其接口写双向）。

2. **区分信号**
   - 「合并版」的信号：负触发要同时覆盖单本与连载两侧边界；输入权限表要兼容 v3 的假设草案制（缺料时标「假设」而非拒绝）；失败出口要引用 v3 的 SV/PL 卡号。
   - 反信号：照抄 v0 的「拒绝」「标 H / NOT_PROVEN」句式——前者与 v3 有意改进的「列方案交作者」冲突，后者是审计词。

3. **两条分支的做法**
   - **A**（采用）：负触发 10 条逐条改写（非虚构核验、角色声音、润色翻译给出转介目标；影视类比、平台算法、互动引擎、设定集、排版出版、爆款保证、无素材代编写明不在范围）；输入权限四行表落 §2；「输出四件」（目标与已读范围、条件分支、另一方案代价、失败出口；无可判断文本只给空表）落 §2——此条来自 v0 优先裁决节的通用裁决；§8 加「主要操作的失败出口」五行表（规划/诊断/修订/排产/作者不答）；§10 路由表加「缺料或冲突时的出口」列，19 行逐行给出口并锚定卡号；description 补 `fiction-planning-and-diagnosis` 与 `preset-card-generation`；§1 补 preset-card 转介行、C.2 三行归属表与「从 preset-card 转入」接收向。
   - **B**：只在 description 加名字、不建表。判为不够：路由不可达、缺料行为不可预期，验收第 4 条不达标。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：负触发条目与 §1 转介表重复冲突（非虚构一段原有表述）→ 收拢为一条清单、删重复句；输入权限表与 v3 §2「只给一句想法也能做」冲突 → 表中「只有点子」行明确「三要素卡、形态判断、空白画布」与假设草案制衔接。
   - 修复：改完复查 GQ3 双向（本 skill 说转给 preset-card 的请求形态，与「从 preset-card 转入」互逆；与 fiction-planning S06a1 已写的归属行不矛盾）。

5. **成品落点**
   - `output/story-architecture-and-longform-planning/SKILL.md`：description、§1（转介表 preset-card 行、重叠归属表、转入向、负触发节）、§2（输入与权限表、输出四件）、§8（主要操作的失败出口）、§10（出口列）、§9（未核→未读）
   - **来源**：`notes/suite-contract.md` 第一节 C.1/C.2、第七节 C.3 第 1–3 条、第二节；v0 `plot-architecture/SKILL.md` §1/§2/§7 与优先裁决节；计划 P3 第 5 条、附录 E ST-T2。

### D3 措辞合规清扫（四词外状态词形与旧编号痕迹）

1. **情境**
   - 已知：v3 基线残留「未证实」（plot-rules PL-10、plot-planning §13、plot-revision §5/§7）、「未验证」（plot-revision §4）、「尚未验证／未验证」（plot-rules PL-04/06/07/08 边界句）、「设计推断」（PL-06）、「未核」（SKILL.md 三处、plot-revision §6）、「RC，即 PL 编号」旧编号痕迹（plot-revision §5）。
   - 用户要求：红线禁止四词外状态词形与改动痕迹；交付状态只用四词。

2. **区分信号**
   - 要清的是**状态词形**（未证实/未验证/未核/设计推断）与旧编号痕迹；「标‘推断’」「置信说明高/中/低」「冲突状态无/按条件/未定」是规则适用性元数据，不是对作者的交付状态，且为 v3 基线既有口径，保留。
   - 反信号：为躲正则把「没有依据，按作者判断」这类固定说法改掉（S01 口径禁止）——本片无此类改写。

3. **两条分支的做法**
   - **A**（采用）：逐处替换——效果类统一为基线既有口径「效果未证明」或「不保证作品效果」；「未核」改「未读」（纯范围标记）；「未验证」改四词「未能核实」的完整句式；「设计推断」改「推断」；「（`RC`，即 PL 编号）」改「（PL 编号）」。
   - **B**：保留原句，登记允许理由。判为不取：「未证实」与「未核」不在 B.2 任何允许情形内，属四词外状态词形。

4. **反例与修复**
   - 推翻判断的情况：替换后句义变化（如「未核」承担版本状态含义）→ 改写为「把版本限制与未读范围写进交付说明」，保留保护功能。
   - 修复：清扫后复扫 `未核实?证|未验证|未核|设计推断` 及审计词正则，本片四文件零命中。

5. **成品落点**
   - `plot-rules.md`（PL-04/06/07/08 边界、PL-10 触发情境）、`plot-planning.md`（§13）、`plot-revision.md`（§4/§5/§6/§7）、`SKILL.md`（§2/§7/§9）
   - **来源**：`notes/suite-contract.md` 第二节 2.1/2.2、第五节；计划附录 B #9。

### D4 不恢复的三处有意调整（逐条排除）

1. **PL-13「三段更长应是中段」**：v0 为单来源经验默认（v0 自评 MEDIUM）；v1 `08-capacity-and-revision.md` 已显式改「三部分可等长也可不等长」；v3 沿用 v1 并中性化。判后版有意选择，不回退（plot-rules PL-13 步骤 2、plot-planning §6）。
2. **plot-planning §0 缺料策略**：v0「用户没给原文时最多给检查清单与空白模板」；v3 改「标假设往下规划＋两三个可选方案」并与 v3 `openai.yaml` default_prompt 一致。判合并时的有意统一（套件缺料假设草案制），保护句（不把候选当已定事实、不对未读文本下诊断）保留，不回退。
3. **plot-planning §9「单行本被要求每章留钩」**：v0「拒绝」；v3「给阶段性收束方案＋代价＋更省替代，作者定」。判有意改进（与「冲突列方案交作者」的套件口径一致），保留 v3。
   - 另：v1 独有的补充（SP09「不能用新增异常支线强行给概率背书」、SP10「即时氛围和审美价值」细化）v0 没有，按「只有 v1 有的不补」处理；v1 已有而 v3 也有的（SP03 的「记待查不先删」）经 LI-ST-008 恢复。
   - **来源**：v1 `d2003e4:skills/story-architecture-and-longform-planning/references/08-capacity-and-revision.md`、v0/v3 `planning.md` §0/§9、计划 P1「以下情况不算丢失」。

### D5 A-01／P4 单元定界与移交

1. **情境**：r2 表 `P4`（1182B）与 `A-01`（369B）两行按文件归属不明；派发说明要求 a2 范围文件（diagnosis、examples、scope-and-conflicts、decision-rework、source-index、historical-provenance、templates）不得动。
2. **区分信号**：`git grep` 只读定位——`A-01` 是 v0 `decision-rework.md` 的标题＋用法段（a2 范围）；`P4` 是 v0 SKILL.md 的「P4 直接执行示例」（本片范围），其内容含裁决、示例、外链三类。
3. **分支做法**：裁决文字并入 D1 的恢复与 D2 的「输出四件」；两个执行示例的落点 `examples/plot-examples.md` 属 a2，移交 S05a2 判断是否补自创版；指向 `decision-rework.md`/`historical-provenance.md` 的链接不恢复（前者 a2、后者来源类按 2.8）。`A-01` 行登记移交，本片不决定其内容。
4. **反例与修复**：若 a2 判 P4 示例不补，其规则内容已由 PL 卡覆盖，无知识缺口；移交项在 loss-inventory 与本文件双登记，避免两片都写或都不写。
5. **成品落点**：无直接落点（移交）；**来源**：v0 `plot-architecture/SKILL.md` P4 节、v0 `decision-rework.md` 开头（只读定界）、派发说明的 a2 范围清单。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **`agents/openai.yaml`**：不适用。v3 合并版已合规（`allow_implicit_invocation: false` 在位、缺料口径与 §2 一致），无两可分支，原样保留。
- **PL-03/07/09/11/12/14/15/16 与 rules/planning/revision 其余结构单元**：不适用。逐块比对在位，v2→v3 的去来源改写已覆盖（引文、`-NNNN`、年代、锚点清零），无内容块丢失；个别措辞合规见 D3。
- **模板落点（templates/plot-*）**：不适用。属 a2 范围，本片未动；SKILL.md §10 对模板的出口列只写填写口径（未知/证据位置），不改动模板文件本身。

---

## S05a2 决策链（W3 主体轮第 7 批）

- 分片：S05a2｜代理：Agent 3（a2 段子代理）｜轮次：W3 主体轮第 7 批｜日期：2026-11-05
- 分片口径：v0 `d23c461:skills/plot-architecture/` 的 references/diagnosis.md（21678 B）＋references/examples.md（24761 B）＋references/scope-and-conflicts.md（17509 B）＋references/decision-rework.md（4485 B）＋templates×3（17446 B）＝85879 B；另 source-index.md（26357 B）与 historical-provenance.md（661 B）按 2.8 节判定入账。逐条 9 列记账见 `notes/loss-inventory/story-architecture-and-longform-planning-S05a2.md`（LI-ST-101–129 ＋本节移交闭环 130）；附录 B 见 `notes/quality/story-architecture-and-longform-planning/s05a2-desourcing-selfcheck.md`。

### D1 S-1「D6 全稿结构复核」十一项与三条细则怎么核定（slice-prep §2 ① 必做）

1. **情境**
   - 已知：计划 2.4 节记「S-1 结构审查十一项及三条细则：仍缺」；W2 修正疑其在 v3 `plot-diagnosis.md:317–327` 但缺三条细则，要求比内容核定、不盲信旧结论。逐版本检索：v0 只在 `scope-and-conflicts.md:114` 有一行指针（「11 项结构审查清单…可作可选诊断清单，不单独立规则」，未列本体）；v1 `references/12-decisions-and-boundaries.md`「补齐」节列了十一项全文＋同段三条细则（喜剧缓解、对白与动作关系、看似多余角色可防止过分人工）；v2 整体未迁移（全谱系零命中）；v3 `plot-diagnosis.md` §D6 有十一项改写版。
   - 推断：v3 的 D6 是按 v0 指针＋v1 清单的去来源恢复，恢复时漏掉同段三条细则；计划 2.4 的「仍缺」对十一项已过时。
   - 用户要求：逐条比内容核定，缺的补回，自创表述、不带人名。
   - 拿不到的：v2→v3 恢复 D6 时是否有意略去三条细则的记录；以 v1 全文为定性佐证（v1 明言它们是「审查维度、可为小说诊断提供参照」）。

2. **区分信号**
   - 走「恢复」的信号：v1 与十一项同段同源、v1 明确保留其诊断参照价值；v3 恢复了清单主体却无这三条，D1 证伪（类型惯例解释）排除不了——喜剧缓解/对白动作分工/配角防过巧都是通用可判断的检查维度，不属「只属于某部作品」。
   - 反信号（走「不恢复」）：三条细则若只是来源考据注记或与 D6 用法矛盾——实测不是，v1 已把它们从剧作语境泛化为小说诊断参照。
   - 判错的代价：把有意省略当丢失 → 重复补回打乱 v3 D6 结构；把连带删除当有意省略 → 三条可操作检查维度继续缺失。

3. **两条分支的做法**
   - **A**（采用）：十一项判定「已在、不重复补」；三条细则按 v3 D6 的行文风格补为清单后三条检查维度（喜剧缓解：高压段落间留换气处、检查与前后张力的衔接；对白与动作的关系：各承担一件事、互为复述记入未决项；看似多余的角色：删并前先查其是否在降低「情节安排过巧」痕迹），置于尾段「诊断清单不是计分表」之前，使尾段的非硬门槛与待验证限定同样覆盖三条。
   - **B**：只登记缺失不补。判为不够：与「找回丢失项」的派发口径相悖，且三条有明确 v1 佐证。
   - 停下条件：无（v1 佐证充分，非两可）。

4. **反例与修复**
   - 推翻判断的情况：补回句出现「该戏剧论」「作者自承」类来源指涉、或把三条写成计分项 → 实写时全部用通用陈述并保持「检查维度」定位。
   - 修复：补后复查 D6 整节零书名/人名/年代/编号、尾段限定句在三条之后仍然可读；B.3 骨架比对不适用（非情节示例）。

5. **成品落点**
   - `output/story-architecture-and-longform-planning/references/plot-diagnosis.md` §D6（第 11 项后、尾段前）
   - **来源**：v0 `plot-architecture/references/scope-and-conflicts.md:114`；v1 `d2003e4:skills/story-architecture-and-longform-planning/references/12-decisions-and-boundaries.md` 补齐节；slice-prep §2 ①；计划 §2.4。

### D2 diagnosis／examples 谱系的改号对齐与残留清扫

1. **情境**
   - 已知：v0 diagnosis 25 单元、examples 36 单元（含无前缀 RC 编号段落单元群）r2 标 `RENUMBERED?`/`UNALIGNED?`；v2→v3 已做 RC→PL 改号与去来源。开工扫描发现本片落点残留：「（未证实）」×2（examples 文件头、plot-canvas 文件头）、「用户明确要求」×1（plot-diagnosis §0，合同第五节禁用短语）、「语料」措辞 ×1（examples A2）。
   - 用户要求：找回丢失项＋去来源＋四词收敛。

2. **区分信号**
   - 走「不恢复（对齐在位）」：v0/v3 逐块 diff 无删段——diagnosis 八症状六件套、examples 例 A/B/C 全字段表与失败出口、E1–E5 逐条在位，差异只有改号、标记词泛化（UNREAD/UNRESOLVED/UNVERIFIED/标 H→未读/未定/未核/推断）与后版增强（§4.1 警示、章号前移标注、默认值限定）。
   - 走「合并（清残留）」：四词外状态词形与禁用短语无 B.2 允许情形；「语料」指向本 skill 之外的证据基础，与 v3 scope §3.2 的按作品验证口径不一致。
   - 判错的代价：把后版增强当丢失回退会打乱 v3；把残留留着会触发附录 B #9/红线。

3. **两条分支的做法**
   - **A**（采用）：登记对齐结论不回退；清四处残留——「效果未验证（未证实）」删括注、「（效果未证实）」删括注、「改写要用户明确要求并给范围」改「改写需用户授权并给出范围」、「语料中证据最薄」改「按当前作品验证」。
   - **B**：把「未证实」改写为「未能核实」。判为不必：两句的完整句义（效果未验证/不保证）已完整，删括注比再引入状态词更干净（同 S06a3 LI-FP-140 口径）。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：删括注后句子主语悬空或语义不完整 → 复查两处主句均自足；「用户明确要求」改写后授权语义弱化 → 对照同文件 §7「需用户授权范围」口径校准。
   - 修复：清扫后对 5 个落点文件复扫 #9/「未证实」/「用户明确要求」零命中。

5. **成品落点**
   - `examples/plot-examples.md` 文件头＋例 A2；`templates/plot-canvas.md` 文件头；`references/plot-diagnosis.md` §0；对齐登记见 loss-inventory LI-ST-102–109
   - **来源**：v0 `plot-architecture/references/diagnosis.md`、`examples.md`；`notes/suite-contract.md` 第二节/第五节；计划附录 B。

### D3 scope-and-conflicts §3/§4 替代节怎么定性

1. **情境**
   - 已知：v0 §3（证据边界：时间语言媒介/长篇多线证据最薄/单来源参数表/来源类型陷阱/置信度）与 §4（单来源条款清单）在 r2 标 `UNALIGNED?`；v3 改写为 §3「规则适用边界」（3.1 现实与虚构分开/3.2 按作品验证/3.3 数字只作默认值/3.4 重复案例≠多次验证/3.5 置信与效果验证）与 §4「参数和规则的安全用法」。
   - 用户要求：不恢复来源清单；不把有意调整当丢失。

2. **区分信号**
   - v0 §3.1 的年代/语言/媒介清点、§3.3/§4 的 PG 锚点与置信列属来源材料描述（红线禁项）；其规则侧语义（媒介不外推、长篇多线按作品验证、数字只作默认值、重复案例不增验证、无读者测试不称效果）v3 逐条承接。
   - 反信号：v0 §3.4 末条「来源中的偏见不继承」在 v1 也只存在于来源治理节——判随来源节有意去除；其创作侧通用语义属 character/genre 谱系，本 skill 无人物模板可继承。
   - 判错的代价：恢复来源清单必然带回年代/编号/书名；把 v3 的合并去重（§3.3 与 §4 重复）当丢失会造出重复表。

3. **两条分支的做法**
   - **A**（采用）：§3/§4 判后版有意替换，不恢复原表；v0 §3.3「11 项结构审查清单」行的去向单独登记（移 plot-diagnosis §D6，见 D1）；11 行参数逐行与 v3 §3.3 对照确认无语义缺失；「单来源」措辞 v3 已全部改「有限经验/默认值」。
   - **B**：恢复 v0 §4 五列条款表。判为不需要：与 v3 §3.3/§4 信息重复，且带回置信列与来源计数。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：v3 §3.3 对照发现某参数语义缺失 → 逐行核对 11 行（3/4、中点照面、分段预算、诊断阈值、章末问题、情境入口、恩惠付账、总括情境、场如缩影、口述降落、诗性正义）全部在位，未触发。
   - 修复：v2 残留「-922」行经复扫确认 v3 已清（LI-ST-128），只登记。

5. **成品落点**
   - 无改动落点（`references/plot-scope-and-conflicts.md` 本片零改动）；登记见 LI-ST-110–114、128
   - **来源**：v0 `plot-architecture/references/scope-and-conflicts.md` §3–§5；v1 `12-decisions-and-boundaries.md`；计划 2.8 节、P1 三类排除。

### D4 decision-rework 五单元与 A-01 用法段怎么承接

1. **情境**
   - 已知：v0 `decision-rework.md`（标题＋用法段＝r2 `A-01`，a1 定界归本片）五节是跨规则判定协议；v1 融合进 `12-decisions-and-boundaries.md` 与各 SP 文件；v3 分散承接于 plot-rules PL 卡与 scope。a1 的 D1 已恢复 PL-02/04/05/08 四处「硬门回潮」（其落点其文件），与本片 §2/§4 的判定协议互补。
   - 用户要求：逐单元判定恢复/合并/不恢复。

2. **区分信号**
   - 走「不恢复（已承接）」：§1 的 A/B/C 判型与三案→PL-01/02＋C-08（「独立成篇」v1 融合时已裁掉）；§2 终点与开篇两契约→PL-02 B 型/PL-04 首个叙事单元/PL-15/diagnosis §0；§3 偶然与场景功能→PL-06 三路径＋PL-07 三分支（「结果字段」表的 PG/行号列属来源定位残留）；§4 四条撤销→a1 D1 已按 v0 rules.md＋v1 双佐证恢复进 PL 卡，本片不重复动作；§5 独立性限制→纯来源治理（包外底册、映射账、NOT_PROVEN），通用语义在 scope §3.5；A-01 用法段的「评价以用户提供的文本范围为限」→diagnosis §0＋scope §3.5，F/H/P 标记→「推断」。
   - 反信号：某判定语义在 v3 无落点——逐条核对未发现。
   - 判错的代价：把 a1 已恢复的 §4 再写一遍会双重改动其文件；把 §5 的来源账恢复回来必触红线。

3. **两条分支的做法**
   - **A**（采用）：五节＋A-01 全部判「语义已承接、不恢复」，逐条写明落点；与 a1 D1 的分工在记账中写明（a1 管 PL 卡恢复，本片管判定协议其余单元的承接核对）。
   - **B**：为 §1 的「改挂/合并/独立成篇三案」补「独立成篇」。判为不补：v1 融合稿零命中，判 v1 有意取舍，PL-01 失效条件 1（集锦/框架＝容器）已覆盖独立成篇的结构位置。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：发现 v3 PL 卡与判定协议矛盾 → 以 a1 D1 恢复后的 PL 卡为准复读，无残留矛盾。
   - 修复：本片对 plot-rules.md/plot-planning.md/plot-revision.md 零改动（diff 核验写入范围无重叠）。

5. **成品落点**
   - 无直接改动落点；登记见 LI-ST-115–119 ＋ LI-ST-130（A-01）；**来源**：v0 `plot-architecture/references/decision-rework.md`、`SKILL.md` 优先裁决节（只读佐证）、v1 `12-decisions-and-boundaries.md`、本文件 S05a1 节 D1/D5（并行片交接）。

### D5 SOURCE_ONLY 两件与 P4 执行示例移交怎么处理

1. **情境**
   - 已知：v0 `source-index.md`（26357 B，PG 台账＋逐书注记＋使用硬约束）与 `historical-provenance.md`（661 B，旧入口 frontmatter 存档）r2 全部 `SOURCE_ONLY`；a1 D5 移交「v0 SKILL.md P4 节两个执行示例的落点 examples/plot-examples.md，判断是否补自创版」。
   - 用户要求：来源类按 2.8 节不直接恢复；移交项闭环。

2. **区分信号**
   - 两件来源文件的每一类内容（PG 编号、行号锚点、书名责任者、年代窗口、frontmatter 溯源）都属红线禁项，无规则本体；可通用语义（二手转述不增验证、证据分层、静态方法不证效果）在 scope §3.4/§3.5 已有落点。
   - P4 两个微示例（「双主线中段散帮诊断」与「只有一个悬疑点子」）是操作顺序的压缩演示：其每一步（DR-01 范围→症状→RC-01/08 判型→证据行交付；PA-02 三要素→问题先给→终点作者定→停在素材层）在 v3 例 B（诊断全流程）、例 A（判型）、PL-16/09/02、SKILL.md 输入权限「只有点子」行与输出四件（a1 已恢复）逐一有落点——补自创版会与例 A/B 重复。
   - 判错的代价：恢复来源文件必触红线；补重复示例稀释 v3 示例结构。

3. **两条分支的做法**
   - **A**（采用）：两件判「不恢复」并逐件写明通用语义落点；P4 微示例判「不补」，以 LI-ST-130 闭环 a1 移交。
   - **B**：把 P4 微示例改写成自创版并入 plot-examples.md。判为不需要：与例 A/B 的任务路由与判型内容重复，且「不冒充真实案例」的示例纪律已由文件头声明。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：发现微示例含例 A/B 未覆盖的新步骤 → 逐步核对操作顺序五拍（文本证据→条件分型→可选方案及代价→填表→失败出口）与 v3 SKILL.md §2 输出四件一一对应，未触发。
   - 修复：v3 全包对 `source-index`/`historical-provenance` 的引用复扫零命中（examples 共同限制处 v3 已改指 scope）。

5. **成品落点**
   - 无新建文件；登记见 LI-ST-126–127、130；**来源**：v0 `plot-architecture/references/source-index.md`、`historical-provenance.md`、`SKILL.md` P4 节；本文件 S05a1 节 D5。

### D6 三张模板的合同第三节落地与状态词收敛

1. **情境**
   - 已知：v3 三张模板（plot-canvas/plot-diagnosis-report/plot-scene-table）§1 字段清单的枚举行齐、GFM 分隔行齐，但缺「值/状态/稿件证据位置」三列中的不同列；plot-canvas 状态栏词形「部分」为四词外词形；v3 基线表格口径与 S06a3 已落地的 fiction-planning 四张模板（LI-FP-136–139）不一致。
   - 用户要求：合同第三节逐编号一行、三列齐全、允许「未知」、分隔行齐。

2. **区分信号**
   - plot-canvas §1 已有「填写＋状态」列 → 只补「稿件证据位置」；diagnosis-report 与 scene-table 的 §1 是「字段 ID/字段/填写口径/所属表」字典 → 补「填写/状态/稿件证据位置」三列（两者用法句本就要求「先填 §1 字段行」，补列后与用法自洽）。
   - 反信号：在 §2–§5 展开工作表逐行加状态列 → 会把按场/按发现的工作表与按 ID 的交付状态账混在一起，不合合同第三节的「编号与 reference 一一对应」口径。
   - 判错的代价：列加错表会破坏工作表结构；状态词形不收敛会在交付时出现四词外词形。

3. **两条分支的做法**
   - **A**（采用）：三表 §1 统一补列（canvas 补 1 列、report/scene 各补 3 列），表头/分隔行/数据行列数同步；三表用法段各加三列口径句（状态按四词填、未知合法、不得把未知写成已完成、证据位置只指当前稿件、不指向来源编号或包外路径）；plot-canvas 状态栏「已完成/部分/未知」收敛为四词＋未知；三表完成检查同步。
   - **B**：只在 SKILL.md 写口径、不动模板。判为不够：模板是交付格式本体（S06a3 同型先例 LI-FP-136–139 已按 A 口径落地）。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：加列后表头/分隔/数据行列数错位 → 脚本核验三表全部对齐（canvas 6 列、report/scene 7 列）；「稿件证据位置」与模板内既有的章/场/行定位字段（DR-02、ST-07）重复 → 前者是交付状态账、后者是诊断内容，并存不冲突（S06a3 同判）。
   - 修复：改完逐表回读＋全包分隔行核验。

5. **成品落点**
   - `templates/plot-canvas.md`（文件头/§1/状态栏/完成检查）、`templates/plot-diagnosis-report.md`（用法/§1/§7）、`templates/plot-scene-table.md`（用法/§1/完成检查）
   - **来源**：`notes/suite-contract.md` 第三节、第二节；v0 `plot-architecture/templates/`×3（对齐底本）；S06a3 LI-FP-136–139 先例。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **`plot-scope-and-conflicts.md`**：不适用。本片逐块比对零内容缺失、复扫零残留（v2 的「-922」残片已由 v2→v3 清除），零改动。
- **plot-diagnosis §1–§7 与 examples 例 A/B/C/E1–E5 的规则本体**：不适用。改号对齐在位、无删段（v0/v3 全文 diff 核实），只有去来源改写与后版增强，见 D2。
- **serial-\* 文件（S05b 范围）**：不适用。本片复扫发现的 `serial-zh-webnovel.md:9`「书里」命中按归属登记移交（语义指用户自己的连载作品，B.2 第 1 条方向），不动其文件。

### 移交闭环（LI-ST-130）

- **r2 `A-01`（v0 decision-rework 标题＋用法段）**：判「语义已承接、不恢复」——「本文件是 rules.md 的冲突消解与案例执行说明，不替代规则正文」由 v3 plot-rules.md「唯一权威版本」定位与各卡「冲突状态」段承接；「所有评价以用户提供的文本范围为限」由 diagnosis §0 与 scope §3.5 承接；F/H/P 标记体系属审计词，v3 以「推断」与「高/中/低只表示条件边界清楚」承接。落点：无（登记于 loss-inventory LI-ST-130）。
- **a1 D5 移交的 P4 两个执行示例**：判「不补自创版」——两例的操作顺序五拍与判型内容在 v3 例 A/例 B、PL-16/09/02、SKILL.md 输入权限与输出四件（a1 已恢复）逐一有落点，补写将与例 A/B 重复。落点：无（LI-ST-130）。


### S05a2 补记（四词外词形收敛与骨架比对闭环，LI-ST-131；2026-11-05 追加）

- 主代理 ledger 指名四项移交全部闭环：①plot-diagnosis:27「未核」→「未能核实」；②plot-scope:91「未核实」→「未能核实」、:140「未验证项」→「未能核实的项目」；③plot-examples:3「效果未验证」→「不保证实际效果」（a1「不保证作品效果」同族口径）；④The Salt Road/The Last Tram 骨架比对通过——两项虚构示例（制图师×走私船长双线汇合听证会；售票员×稽查员×罢工×记者法官巧合）与 v0 scope 所引真实作品案例的人物关系/关键事件/时代地点三项均无两项以上对应，无需重写。
- 本片自查扩大的同形收敛：plot-diagnosis D6 尾段「待验证」→「未能核实」、plot-scope §3.2「推断/待验证」→「标推断、记未能核实」、plot-diagnosis-report 用法三元组「未核」与 §7「待验证」→「未能核实」；「未读」（范围标记）、「未定」（冲突状态）、「推断」（证据级元数据）按 a1 D3 元数据口径保留。
- plot-scope-and-conflicts.md 由此由「零改动」更新为「内容层零补块＋3 处词形收敛」（D3 所述「零改动」以此补记为准）；逐处明细见 `notes/loss-inventory/story-architecture-and-longform-planning-S05a2.md` LI-ST-131 与 `notes/quality/story-architecture-and-longform-planning/s05a2-desourcing-selfcheck.md` 二.5 节。收敛后「待验证/未核实/未验证/未核」在本片 6 文件复扫归零。

---

## S05b2 决策链（W3 主体轮第 8 批）

- 分片：S05b2｜代理：Agent 3（b2 段子代理）｜轮次：W3 主体轮第 8 批｜日期：2026-11-05
- 范围：v0 `serialized-volume-planning` 的 `examples/worked-example.md`（12325 B）＋`references/05-production-constraints.md`（19702 B）＋`references/08-cross-volume-dependencies.md`（5409 B）＋`references/legacy-metadata.md`（1743 B）＝39179 B 实内容；另 `references/06-source-index.md`（47820 B）为 SOURCE_ONLY 来源类大件，按 2.8 节不直接恢复、十四块逐块判定入账。逐条决定见 `notes/loss-inventory/story-architecture-and-longform-planning-S05b2.md`（LI-ST-301–349，共 49 条：恢复 3、合并 9、不恢复 34、登记 3；LI-ST-251–300 为段间空号）；附录 B 扫描见 `notes/quality/story-architecture-and-longform-planning/s05b2-desourcing-selfcheck.md`。本节只追加，不重写上文（追加前已重读文件尾确认 b1 尚未写入）。
- 对齐判定：M01→SV-02、M02→SV-04/05、M03→SV-09、M04→SV-06、M05→SV-11、M07→SV-13、M08→SV-14、M11→SV-07、M12→SV-15、M13→SV-08、M14→SV-03、M15→SV-14、M16→SV-16、M17→SV-10；T1–T6 现代迁移→serial-zh-webnovel＋serial-platform-migration；worked-example 例 A/例 B→serial-examples 例 A/例 B；08 七节在 v3 无成块落点（SV-08 仅承接其 §3 台账语义）；legacy-metadata 为轮次溯源元数据、无规则本体。

### D1 08-cross-volume-dependencies 的层级表、正典权威与变更检查怎么找回（LI-ST-321/322/324/327）

1. **情境**：v0 08 全文 5409 B 七节，r2 全部 `UNALIGNED?`。已知 v3 只在 SV-08 承接了 §3 的台账语义，§1 层级表、§2 正典权威、§4 变更影响链、§7 版本冲突出口在 v3 无成块落点；v1（融合稿）将跨卷内容并入章节卷册文件，v3 重组为 SV 卡时未收拢。用户要求按 S-4「补层级依赖表等专表」找回，通用写法、自创例。
2. **区分信号**：走「恢复」的信号是「v0 与 v1 都有、v3 没有的可判断规则」（层级×应输出什么、权威分级、六步链、冲突暂停出口）——判连带删除；反信号是来源标记示例（§3 的 F/H/P 三行）、PG 样本句、审计词（NOT_OBSERVED），不恢复。判错的代价：跨卷大改动（换设定、回改前卷伏笔）没有任何最低范围约束，作者只能凭直觉全改或全不改。
3. **两条分支的做法**：A（采用）——在 serial-volume-and-closure 文件尾新增「跨卷承诺的层级、正典权威与变更检查」节（派发口径指定的跨卷落点），四块一次写入：五层表＋「低层不能替代高层」三禁句（第三句改引 SV-08，不重复）、正典权威段、六步链＋「不伪造已修正、冲突表交作者」收束句（并入 series-volume-dependency 模板的同族内核）、卡住时段（版本冲突暂停＋无前卷只给空表标未能核实）。B（否决）——只补 SV-08 或不改：层级表不是台账的字段问题，SV-08 装不下；不改则 S-4 仍缺。停下条件：无（S-4 为计划指名必做）。
4. **反例与修复**：推翻判断的情况——若写成「每卷必须填层级表」就成了新硬门。修复：写成「一笔承诺跨好几卷时」的条件触发＋应输出清单；修完复查：无编号来历说明、无「补回」字样、表格有分隔行。
5. **成品落点**：`references/serial-volume-and-closure.md` 跨卷节（文件尾追加，未触碰 b1 谱系的 SV-01–07 节）。**来源**：v0 `d23c461:skills/serialized-volume-planning/references/08-cross-volume-dependencies.md` §1/§2/§4/§7；v0 `templates/series-volume-dependency.md`「回归与结果」段（b1 范围，只取同族内核并在 LI-ST-347 登记其矩阵表本体移交 b1）；计划 2.4 S-4、P3 第 5 条。

### D2 05-production-constraints 的缺口怎么补（LI-ST-304/309/311/346 的合并面）

1. **情境**：v0 05 六个规则块中 SV-13/14/15/16 已承接本体；缺口四处：§3 联动（M01/M02/M05 三条）、§7「没有大纲」出口、§9 M17 的「人物扩充＋填充冲突表」、§5 M12 的「可核错误例外」（S-2 余项）与「备用结局不写成正典」保护。r2 全部 `UNALIGNED?`（M16 行被机械标 SOURCE_ONLY）。
2. **区分信号**：走「合并」的信号是规则本体在位、但某条可判断的区分条件或出口在 v3 缺失且 v0/v1 均有；反信号是 v3 有意去阈值化/去硬门化（每 3 章核对→按固定周期、缓冲 1 章→收束动作、无法裁决→给建议由作者拍板），判有意调整不回退。判错的代价：把 v3 的有意放宽当丢失补回，会重新引入硬门；把真缺口当有意调整漏掉，S-2 永远「部分补回」。
3. **两条分支的做法**：A（采用）——四处缺口按各自谱系落点合并：联动段入 SV-13（serial-production，本片文件）、没有大纲出口入 SV-13 卡住时、M17 填充来源与冲突表入 SV-10 篇幅段（serial-chapters 的 SV-10 节，内容谱系出自本片 v0 05 §9）、S-2 例外与备用结局保护入 SV-15 步骤 2/4。B（否决）——不动：S-2 是计划 2.4 指名余项，必做；联动与 M17 缺口是真实连带删除。全部写成 SV 卡号引用，不新增文件、不触碰 b1 节。
4. **反例与修复**：推翻判断的情况——「可核错误直接改」若写成无条件改稿，会与「已发表内容不回改」冲突。修复：补句写明「改不改、改在哪一版，仍按合同和已发表范围决定，并记进日志」；修完复查 SV-15 与跨卷节正典权威段口径一致。
5. **成品落点**：`references/serial-production.md` SV-13（联动段＋卡住时）、SV-15（步骤 2/4）；`references/serial-chapters-and-installments.md` SV-10 篇幅段。**来源**：v0 `d23c461:skills/serialized-volume-planning/references/05-production-constraints.md` §3/§5/§7/§9；计划 2.4 S-2；`notes/suite-contract.md` 第二节四词。

### D3 worked-example 的示例级失败出口怎么处理（LI-ST-316/319）

1. **情境**：v0 worked-example 例 A/例 B 各带一个失败出口块（A11 五条、B7 五条）；v3 serial-examples 重组后出口块消失，其规则侧语义分散进 SV 卡的卡住时，示例级演示缺失。R18 §2d 要求自创难例含失败出口。
2. **区分信号**：逐条核对五＋五条出口：规则侧已在位的不重复（卷 2 取消→备用结局已在例 A 正文；卷 4 未立项→分支 1 已有；没有大纲三问→SV-02 卡住时逐字在位；没有卷 3 稿→SV-08 卡住时在位），示例级演示缺失的才补。判错的代价：照搬 v0 五条会与 SV 卡重复、把示例写成规则堆；全不补则示例失去「计划赶不上变化时怎么交付」的演示。
3. **两条分支的做法**：A（采用）——例 A 补「计划赶不上变化时」四条（砍章删节拍保高潮、四条线选活动线、必须抓反派可抓但不写通则、备用结局启用路径），例 B 补「退出与拒绝」四条（没稿只给空表、主谋假死是回改不是开线、读者反应不下承诺），全部沿用例内既有事实，无新自创情节。B（否决）——整块照搬 v0：五条中两条与正文重复，且沿用 v0 的「保守上限」表述与 v3 的「不是硬上限」口径冲突。停下条件：无。
4. **反例与修复**：推翻判断的情况——出口句若出现「必须」「一律」即成新硬门。修复：全部写成条件分支句；修完复查出口块与 SV-04「三种都成立」、SV-08「不是硬上限」口径一致。
5. **成品落点**：`examples/serial-examples.md` 例 A「计划赶不上变化时」块、例 B「退出与拒绝」块（节内追加，未触碰 wave4 部分）。**来源**：v0 `d23c461:skills/serialized-volume-planning/examples/worked-example.md` A11/B7。

### D4 06-source-index（SOURCE_ONLY 大件）与 legacy-metadata 怎么判定（LI-ST-328–343）

1. **情境**：06-source-index 47820 B 是 103 本来源的 SHA/台账/族谱/逐书注记/覆盖等级/UNVERIFIED/不可引用项账；legacy-metadata 1743 B 是轮次溯源与基线保护声明。两者都无成块规则本体。
2. **区分信号**：「不可拆 ≠ 应恢复」：来源编号、书名、行号、SHA、覆盖百分比、年代、门禁词全部是红线禁项，判「不恢复」；但每块内的通用内核（同族不当独立证据、时代局限不当角色模板、发行装置不当创作顺序、单本装置不当通则、历史语料不是现代样本、未读不能当全文）逐块与 v3 已有落点核对——凡已有落点的登记承接，无落点且可通用的才考虑补。本片核对结论：十四块的通用内核均有既有落点，无需新写。
3. **两条分支的做法**：A（采用）——不建新文件、不恢复任何块；十四块逐块在 LI 表记「不恢复＋内核落点」。B（否决）——恢复成「通用证据规则」文件：会与 SKILL §11、plot-scope §3.4（a 段已落点）重复，且必然带入来源词形。legacy-metadata 同法：两节（头段、R04 追加条目）逐条判定为元数据残留（包外路径、SHA、覆盖口径、UNRESOLVED/REJECT 审计词、「取代/保留」改动痕迹），其裁决语义（M06/M08 未裁决、M09/M10 已否决）已由 v3 SV-12/SV-14/SV-04 有意吸收，不回退也不恢复声明。
4. **反例与修复**：推翻判断的情况——若某块通用内核在 v3 无落点而本片漏记，会误判「来源文件无知识可提」。修复：十四块逐块列内核与落点（M08 路线 C 的「先小规模验证再定出版方式」内核核对到 serial-production 风险检查表行）；修完复查没有把可进成品的规则误标为「无落点」。
5. **成品落点**：无（不建文件；内核落点为 SKILL §11、plot-scope §3.4、SV-03/04/08/11/16、serial-zh-webnovel §2/§3、serial-production 风险检查表等既有位置，逐条见 LI-ST-330–343）。**来源**：v0 `d23c461:skills/serialized-volume-planning/references/06-source-index.md`、`references/legacy-metadata.md`；计划 2.8 节；S04b/S05a2 来源类判定同口径。

### D5 移交三项与共写协议（LI-ST-344/345/346/347）

1. **情境**：a2 移交三项：① serial-zh-webnovel:9「一部书里的一卷」（#4 全包唯一命中）；② serial-platform-migration「已核实/未核实/不适用」三态列；③ serial-* 系「未核」词形 7 处。serial-volume-and-closure 与 serial-examples 为两片共写文件。
2. **区分信号**：归属判定按内容谱系而非文件名——①② 所在行/表的谱系是 v0 05 §6 现代迁移 T1–T6（本片 v0 文件），判属本片处理；③ 的 7 处中 serial-chapters:67（SV-16←05 §8）与 serial-zh-webnovel:40（迁移核验语义）属本片，其余 6 处（serial-open-lines ×2←03、serial-volume-and-closure:158←02、serial-tables ×3←templates）属 b1 谱系，登记移交不动。
3. **两条分支的做法**：① 按 B.2 第 1 条本可判允许，但按 S01 §5「可顺手消除的命中改掉更干净」改写为「同一部连载作品中的一卷」（LI-ST-345）；② 判对齐四词而非保留三态——「未核实」是四词外状态词形，且一行并写违反合同第三节「每编号独占一行」，改造为 T1–T6 六行三列表＋状态口径段（LI-ST-344）；③ 本片 2 处收敛「未能核实」，6 处登记移交 b1（LI-ST-346/347）。共写协议：写入前重读两文件确认 b1 尚未写入，写入限于本片谱系对应节（跨卷节尾追、例 A/例 B 节内追），写入后复核写入文件集与 a1 的 10 文件、b1 的范围文件无交集。
4. **反例与修复**：推翻判断的情况——若 b1 中途已写入同文件同节，编辑会撞车。修复：追加前重读文件尾与目标节，发现冲突即重读重追加并回报；本片两次重读（source-synthesis 与两个共写成品文件）均确认无并行写入。
5. **成品落点**：`references/serial-zh-webnovel.md` §1 第 1 行＋跨平台迁移段；`references/serial-platform-migration.md` 文件头、导语、迁移记录节；`references/serial-chapters-and-installments.md` SV-16。**来源**：`notes/quality/story-architecture-and-longform-planning/s05a2-desourcing-selfcheck.md` 第六节移交表、本片派发说明、`notes/suite-contract.md` 第二节/第三节/第四节 B.2。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **serial-production 的 SV-13/14 本体、serial-chapters 的 SV-16 本体、worked-example 的示例正文（例 A/例 B 输入与判断段）**：不适用。逐块对照在位（LI-ST-302/303/305/310/314/315/317/318），无两可分支；v3 的去阈值化与示例名中文化判有意调整，不回退。
- **`agents/openai.yaml`、SKILL.md、serial-rules/serial-open-lines/serial-formula/serial-tables**：不适用。均属 a1/b1 范围，本片只核对（serial-tables §2/§8/§9 字段核对通过）、不改动；SKILL 路由措辞移交见 LI-ST-349。

---

## S05b1 决策链（W3 主体轮第 8 批）

- 分片：S05b1｜代理：Agent 3（b1 段子代理）｜轮次：W3 主体轮第 8 批｜日期：2026-11-05
- 分片口径：v0 `d23c461:skills/serialized-volume-planning/` 的 SKILL.md（22717 B）＋agents/openai.yaml（519 B）＋examples/wave4-casebook.md（1855 B）＋references/01–04（15787＋12673＋13056＋11837 B）＋references/07-production-discipline.md（11167 B）＋templates/series-volume-dependency.md（1294 B）＝90905 B。逐条 9 列记账见 `notes/loss-inventory/story-architecture-and-longform-planning-S05b1.md`（LI-ST-201–247；并行片 S05b2 占 LI-ST-301 起段）；附录 B 见 `notes/quality/story-architecture-and-longform-planning/s05b1-desourcing-selfcheck.md`。

### D1 S-4「系列—卷—章依赖矩阵」专表怎么找回（LI-ST-244，唯一恢复项）

1. **情境**
   - 已知：计划 2.7 节与 2.4 节审计 S-4 记「层级依赖表等专表：仍缺」，P3 第 5 条指名「可参考 v0 的 series-volume-dependency 模板」；v0 模板（1294 B）为 13 列依赖矩阵说明＋「回归与结果」段；v1 SP17 输出仍列「开放线表与依赖矩阵」；v3 templates/serial-tables.md 只有 §1–§11 空白表，SKILL.md §7/§10 亦未列依赖矩阵——整表在恢复时漏掉。
   - 推断：v3 以「开放线台账＋预估章数列」承接了逐线记账，但跨卷层级核对的专表结构（正典版本/系列目标/人物与世界状态前后对照/依赖/回收候选/容量假设/作者决定）没有对应物；属恢复清单漏项，不是有意删表。
   - 用户要求：S-4 必做，补层级依赖表等专表，自创改写、不带来源词形。
   - 拿不到的：v2→v3 未收录该表的记录；以 v1 SP17 为定性佐证。

2. **区分信号**
   - 走「恢复」的信号：表结构是可填写的核对工具而非来源清单；13 列中 9 列（卷/章/人物状态/世界状态/开放线/依赖/回收候选/下一步/容量假设）在 v3 各 SV 卡均有规则侧语义，缺的只是集中核对面；「回归与结果」段的「拒绝以超过 2 条开放线、没有一章缓冲作为跨题材失败条件」与 v3 SV-08「不是硬上限」、SV-05「收束动作不必单独成章」口径一致。
   - 反信号：若表只是 v0 台账的重复——实测不同：台账按线记账，矩阵按「正典版本×卷×章」核对层级承诺与依赖。
   - 判错的代价：不补则 S-4 继续缺、接手旧稿/跨卷改动没有核对面；照抄 v0 则带回 F/H/P、NOT_OBSERVED 等审计词形与英文段名。

3. **两条分支的做法**
   - **A**（采用）：补为 `templates/serial-tables.md` §12——列说明表（13 行，逐列去英文段名与来源语境：proof 的 F/H/P 三分→「稿件内可核位置／推断／建议」，NOT_OBSERVED→「未知」，author_decision 四值→「已确认／未能核实／待作者决定／不适用」）＋空白 13 列矩阵表（GFM 分隔行齐）＋回归与结果段（去「≤2 条/一章缓冲」引述，改写为指向 SV-05、SV-08 的正向句）；路由指针两处：`serial-rules.md` SV-08 卡尾句、`serial-open-lines-and-continuity.md` SV-08 产物行。
   - **B**：新建 `templates/serial-volume-dependency.md`。判为不取：v3 已把 serial 侧模板集中在一个文件、SKILL.md §10 已路由到 serial-tables.md，新文件反而断路由。
   - 停下条件：无（v1 佐证充分，非两可）。

4. **反例与修复**
   - 推翻判断的情况：补表后与 §5 开放线台账列重复——对照后确认矩阵不含「当前状态/回收方式」逐线列，是层级核对面，两者并存不冲突；「证据类型」列与合同第三节「稿件证据位置」口径对齐（只指用户当前稿件或已发表章节）。
   - 修复：改完逐表回读＋分隔行核验；复扫 13 列说明零英文段名、零审计词形。

5. **成品落点**
   - `templates/serial-tables.md` §12；`references/serial-rules.md` SV-08 卡；`references/serial-open-lines-and-continuity.md` 产物行
   - **来源**：v0 `d23c461:skills/serialized-volume-planning/templates/series-volume-dependency.md`；v1 `d2003e4:skills/story-architecture-and-longform-planning/references/12-decisions-and-boundaries.md` 同源 SP17 节（佐证）；计划 2.4 S-4、2.7 节、P3 第 5 条。

### D2 六处合并补强怎么定性（LI-ST-209/217、220/221、225/226、235、242）

1. **情境**
   - 已知：逐块比对后确认 v3 serial 文件对 v0 b1 的规则本体已逐卡承接（M→SV 改号），缺口集中在六处边界与处置句——①发行装置边界（v0 SKILL §7＋01 §2.1 倒果为因；v1 SP15 保留）；②诊断修复窗口三阶段表（v0 01 §6）；③末章已写章末钩的处置（v0 02 §2.2/§5）；④钩子过强的处置动作（v0 02 §5）；⑤重复可为设计与同章多项保持因果清楚（v0 04 §2；v1 SP18 保留）；⑥偏离所选路线的破例记账（v0 07 §3/§4；v1 SP23 保留）。
   - 推断：六处均有 v0＋v1 双佐证而 v3 缺失，属去来源/改卡时的连带删除，不是有意省略（省略方 v1 与 v0 同向）。
   - 用户要求：找回丢失项，用通用写法；不把缩减幅度当应补回的量。

2. **区分信号**
   - 走「合并」的信号：缺的是边界条件或处置动作（区分条件/失败出口类），且能并入现有卡而不另立规则；与 v3 既有句无口径冲突。
   - 反信号：若某处与 v3 的去阈值化方向相反（如 v0 硬限）——六处均为条件句或记录纪律，无硬限回潮。
   - 判错的代价：漏补则诊断后无处置（③④）、跨卷改动无边界（①⑤⑥）、修复窗口只剩一句（②）；补错位置则破坏 SV 卡结构。

3. **两条分支的做法**
   - **A**（采用）：逐处并入现有卡——①→SV-02 步骤 1 尾句（目录/预告/排期只说明发行安排，入口栏只填作者确认过的计划）；②→SV-05 尾「修复窗口」三行表（开写前/写作中/已发表×能改×不能改×替代，措辞对齐 v3：缓冲章→收束动作、不 retcon→不回改）；③→SV-09 步骤 5 尾句（不叠加、二选一、优先卷末入口）；④→SV-09 卡住时尾句（降低为一个新事实或改成场景收束，不靠拉长悬念解决）；⑤→SV-11 步骤 2/3 尾句（同章多项检查因果清楚；重复可为仪式/喜剧/对照/角色困境，写明功能不按疲劳处理）；⑥→SV-14 步骤 5（偏离所选路线记场合、理由与后果进反馈日志，不为破例另立通则）。
   - **B**：为②另立独立节、为③④各立新卡。判为不取：SV 卡结构以「规则/用在/怎么做/产物/不用/卡住时」为骨架，边界句入既有块即可达（验收第 2 条），另立卡会稀释卡号体系。
   - 停下条件：无。

4. **反例与修复**
   - 推翻判断的情况：合并句与同卡「不用/卡住时」冲突——逐处复读：①与 SV-02 卡住时（故事列待定）互补；②与 SKILL.md §3「已发表的只在后文接」一致；④与卡住时首句同主语衔接；⑤与「第三次重复时删并」并存（设计性重复先于删并判断）；⑥与 SV-15 日志列衔接。
   - 修复：改完逐句回读无悬空主语、无「旧版/补回」类改动痕迹；六处与 a1/a2 已修文件零接触。

5. **成品落点**
   - `serial-volume-and-closure.md`（SV-02 步骤 1、SV-05 修复窗口）、`serial-chapters-and-installments.md`（SV-09 步骤 5、卡住时）、`serial-formula-and-escalation.md`（SV-11 步骤 2/3）、`serial-production.md`（SV-14 步骤 5）
   - **来源**：v0 `SKILL.md` §7、`01-volume-architecture.md` §2.1/§6、`02-chapter-hooks.md` §2.2/§5、`04-formula-and-variation.md` §2、`07-production-discipline.md` §3/§4；v1 SP15/SP17/SP18/SP23（定性佐证）。

### D3 有意调整逐条排除（不恢复的定性依据）

1. **情境**：v0 与 v3 的其余差异需逐条判「有意调整不回退」还是「连带删除」。本片核 v1 定性，排除十一组。
2. **区分信号**：v1 已调整而 v3 沿用的判有意；v1 与 v0 同有而 v3 独缺的判连带（进 D2/D1）。
3. **逐条结论**：①M08 路线 C——v1 SP23 显式拆为「后续出版」独立轴（「不把委托出版误作第三种开载时点」），v3 两路线＋发行风险表承接，不回退（LI-ST-241）；②回顾长度数值（1–2 页/3,000–5,000 字符/8,000 反例）——来源语料测量值，v1 SP12 已改「长短按实际负担」，去数值为有意（LI-ST-227）；③「同卷内可整段复述」v3 收紧为「可以很短」——v1 无宽限句，判有意收紧（LI-ST-227）；④「至少 1 个不可逆配角变化」v3 弱化为检查项——v0 自注最弱半句，判有意（LI-ST-229）；⑤M13 活动线 2 条硬限 v3 泛化为初始提醒——与 SV-11 去阈值同构，判有意（LI-ST-230）；⑥M15 存稿 1–3 部个人经历去数值化——判有意（LI-ST-240）；⑦M07 配额数值（250 词/页等）去数值化留四件套结构——判有意（LI-ST-239）；⑧「1 章缓冲」放宽为「收束动作」——v1 无 1 章要求，判有意（LI-ST-218）；⑨M17 十二词对话阈值删除——个人风格参数，判有意（LI-ST-228）；⑩章长 1,500–3,000 词删除——语料测量值，判有意（LI-ST-223）；⑪M10 直觉式构思并 PL-15 工序、终卷手法 v1 软化 v3 取中——判有意综合（LI-ST-237/219）。
4. **反例与修复**：推翻判断的情况——若某组在 v1 仍保留 v0 原句而 v3 独缺，应转「合并」。逐组核 v1 后未触发（①③④⑤⑥⑦⑧⑨⑩⑪ v1 均已同向调整；② v1 明言「没有真实反馈不能声称必然厌烦」）。
5. **成品落点**：无改动落点（定性登记见 LI-ST-218/219/223/227/228/229/230/237/239/240/241）；**来源**：v1 `d2003e4:skills/story-architecture-and-longform-planning/references/05/06/07/08/09/10/11/12-*.md`；计划 P1「以下情况不算丢失」。

### D4 移交三项的分工闭环与共写协调（LI-ST-245/246/247）

1. **情境**：a2 移交三项落在本片与 S05b2 的共同落点文件；b2 并行在写。本片开工复扫发现 b2 已先行处理其中三处（zh-webnovel:9、migration 三态列＋文件头两处、chapters:67）。
2. **区分信号**：按内容谱系归属——①② 的迁移语义谱系 v0 05 §6 属 b2、v0 SKILL §9 属本片，b2 落笔后由本片复核；③ 的 6 处（open-lines ×2←03、volume-and-closure:158←02、serial-tables ×3←templates）谱系属本片 v0 文件，由本片落笔。
3. **两条分支的做法**：本片复核 b2 三处（改写「同一部连载作品中的一卷」符合 B.2 第 1 条方向且清全包唯一 #4 命中；迁移记录表 T1–T6 六行三列＋口径段符合合同第二、三节）；本片收敛 6 处词形——判断/核对/信息缺失语境「未核」→「未能核实」5 处，serial-tables:3 范围标记→「未读」（与 SKILL.md §2 一致）；「未读」（范围标记）、「未定」（冲突状态）、「推断」（证据级）按 a1/a2 元数据口径保留。
4. **反例与修复**：推翻判断的情况——若 b2 的改写引入四词外词形或改坏语义，则退回其分片。复核未触发（三态列口径段含四词＋未知＋不适用，与 serial-tables §3「不适用」口径一致）；共写文件（volume-and-closure/chapters/production）编辑前均重读，写入节段互斥（本片 SV-01–07/SV-09，b2 尾部追加节/SV-10 篇幅段），diff 无同行冲突。
5. **成品落点**：`serial-open-lines-and-continuity.md`（2 处）、`serial-volume-and-closure.md`（1 处）、`serial-tables.md`（3 处）为本片落笔；`serial-zh-webnovel.md`、`serial-platform-migration.md`、`serial-chapters-and-installments.md` SV-16 为 b2 落笔、本片复核登记。**来源**：`notes/quality/story-architecture-and-longform-planning/s05a2-desourcing-selfcheck.md` 第六节；b2 决策链 D5（本文件前节）；派发说明移交清单。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **v0 SKILL.md §0–§6/§8/§10 与 rules 索引**：不适用。改号/改写对齐逐块在位（v3 SKILL.md §1–§11＋serial-rules 卡组），只有词形与去来源差异已由 a1 处理，见 LI-ST-201–210。
- **agents/openai.yaml 与 wave4-casebook 五例**：不适用。合并版合规（a1 保留）；五例的判型语义由 serial-examples 例 A/B/C 与 SV 卡承接，补写重复（LI-ST-212–215）。
- **serial-zh-webnovel 适配表与 serial-platform-migration 六检查节本体**：不适用。属 b2 已落笔范围，本片仅复核移交闭环（LI-ST-245/246），未改动其规则正文。
