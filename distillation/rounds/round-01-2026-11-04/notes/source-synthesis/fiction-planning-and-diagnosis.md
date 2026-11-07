# R17 §4a 决策链 · fiction-planning-and-diagnosis（S06a1，W3 主体轮第 4 批）

- 分片：S06a1｜代理：Agent 4｜轮次：W3 主体轮第 4 批｜日期：2026-11-05
- 依据：`notes/suite-contract.md`（K2 定稿）；`notes/loss-inventory/raw/fiction-planning-and-diagnosis-2026-11-04-r2.md`（K1 r2 表）；`notes/slice-prep-2026-11-04.md` §1.1/§3.1/§3.2；`notes/source-synthesis/line-editing-and-proofreading.md` 第二节（W3 统一写法口径）；计划第 6 节 P3 第 6 条 / §6.1 / 附录 A / B / C / E / F / G.1。
- 性质：本文件属 `notes/`。**出处只写在每条决策链第 5 项的「来源」小项，不进成品**；成品在 `output/fiction-planning-and-diagnosis/`。
- 逐条决定与九列记账见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06a1.md`（LI-FP-001 至 023）；附录 B 扫描与 B.3 回读见 `notes/quality/fiction-planning-and-diagnosis/s06a1-desourcing-selfcheck.md`。
- 本片只覆盖 v0 谱系 = `fiction-craft/references/rules.md`（RC-01–21＋附）的落点与 SKILL.md 合同类；同 skill 的 a2/a3 段与 S06b/S06c 谱系的决策链由后续分片续写本文件（追加，不覆盖）。

---

## 一、决策链（R17 §4a：情境 / 区分信号 / 两条分支 / 反例与修复 / 成品落点）

### D1 r2 表 `UNALIGNED?` 的 22 个 rules.md 单元怎么对齐到 v3

1. **情境**
   - 已知：r2 表里 rules.md 谱系的单元全部 `UNALIGNED?`（RC-01–21，`1 1 0 0`）或 `RENUMBERED?`（附 1 行）；机械对齐失败，待定向精读。
   - 推断：v0 `fiction-craft/references/rules.md`（101960 B）正文即 RC-01–RC-21 加导航附表；v1 在 `fiction-planning-and-diagnosis/references/01–04-*.md` 内仍用 RC 编号；v2/v3 改号 FC-01–FC-21 并按主题拆成四个文件。
   - 用户要求：按分片口径只处理 rules.md 谱系；UNALIGNED? 是待精读信号，不是丢失清单。
   - 拿不到的：v2 分拆时的取舍说明；按内容核定，不猜。

2. **区分信号**
   - 走「改号对齐」的信号：v0 RC-01 标题「先判赛道：篇幅 / 媒介 / 类型 / 交付」与 v3 FC-01 标题逐字相同，且 v3 四文件文件头自述「FC-01 至 FC-21」覆盖 21 条——编号族整体改名、无缺号。
   - 反信号（判 MISSING）：无——21 条标题一一对上，不满足「无相似标题」条件，不记 MISSING。
   - 判错的代价：把改号对齐当缺失会整批重写，覆盖 v3 现行口径；把真缺块当对齐会漏恢复。

3. **两条分支的做法**
   - **A（采用）**：逐条按「标题一致 + 块结构（层级/规则/用在/看什么/分支/怎么做/交付/反例/适用范围/卡住时）」比对 v0↔v1↔v3；v0、v1 都有而 v3 没有的块记连带删除走合并；v1 才有的不补；v1 软化而 v3 回 v0 口径的记有意选择不回退。逐条决定记 LI-FP-001–022。
   - **B**：按 r2 的 UNALIGNED? 当整批缺失重写。判为错：会撤销 v1/v2/v3 的有意改号与条件化，且成体会带回 v0 的来源锚点结构（PG 锚点、独立来源数、置信度）触发红线。
   - 停下请作者裁决：无——P1 口径（先核 v1 再定性）已定。

4. **反例与修复**
   - 推翻判断的情况：某条标题相同但内容已被 v3 换成另一套（如 FC-06 规则句缩窄）；修复方式不是回退整条，而是只把 v0+v1 共有、v3 缺失的块并入现行写法（见 D3）。
   - 修复后复查：每条 FC 卡仍有「卡住时」出口；无「旧版/本版/更正」类改动痕迹；v3 的条件化措辞未被回退。

5. **成品落点**
   - `output/fiction-planning-and-diagnosis/references/rules-premise-and-structure.md`（FC-01–06）
   - `.../references/rules-units-and-endings.md`（FC-07–10）
   - `.../references/rules-drafting.md`（FC-11–16）
   - `.../references/rules-revision-and-method.md`（FC-17–21＋附）
   - **来源**：v0 `d23c461:skills/fiction-craft/references/rules.md`；v1 `d2003e4:skills/fiction-planning-and-diagnosis/references/01-contract-and-conception.md`、`02-structural-diagnostics.md`、`03-character-and-credibility.md`、`04-language-and-revision.md`；r2 表 RC-01–21 与附各行。

### D2 四个落点文件的来源残留怎么清（原句、引文、-NNNN、人名、年代、来源角色词）

1. **情境**
   - 已知：v3 四文件是 v1→v2 去编号化改写的产物，规则本体保留但残留大量来源痕迹：12 条英文原句、5 处中文经典引文、作者人名（Montgomery/Stribling/Hardy）、`-NNNN` 残片 16 处、年代/市场说法 4 处、「编者判词」「一本手册」「书级」等来源指涉词、文件头「28 本材料标称 1808–1929 年」（三个文件第 8 行）。
   - 推断：这些是截断锚点时留下的残迹（如 PG30776 L2421-2430 只剩「-2430」），规则本体两侧完好。
   - 用户要求：红线禁止原句、来源编号残片、人名、年代；§3.1 指名第 8 行与 rules-drafting 五个行号、rules-revision-and-method:148。

2. **区分信号**
   - 走「清除并改写」的信号：引文只承担「这个判断存在」的背书功能，判断本身可写成通用陈述（如「短词不是唯一标准」）。
   - 反信号（保留）：自创例年份（本片无）、用户稿件语境（本片 rules 文件无）、`1–5`/`3–5 个`/`2–3 个` 这类已条件化的操作默认（v1 起有意去数值化，保留数字但保留「非硬门」限定）。
   - 判错的代价：把「操作默认 + 非硬门」的数字也删掉会丢可操作性；把原句翻译成判断句时若添新断言会自创规则。

3. **两条分支的做法**
   - **A（采用）**：先改写后删出处——每处原句/引文译成不带主语来源的通用判断（S01 口径 §5 通读四查），`-NNNN` 残片直接删除（判断内容已在句内），人名/年代删除后补「特定时期/特定市场」类限定；三个文件的第 8 行统一采用第四个文件既有的去来源口径句。逐处记入 LI 行理由。
   - **B**：整段重写规则卡。判为过：v3 现行卡片结构完好，重写会引入无意改动。
   - 停下请作者裁决：无——红线已明确。

4. **反例与修复**
   - 推翻判断的情况：翻译原句时添出新断言（如把「最高艺术」译成程度词）→ 改为只保留判断方向（「细节可以多职」），不评价高度。
   - 修复后复查：全四文件复扫 11 类（原句、`-NNNN`、人名、年代、硬规则、残迹）零违规；通读无主语悬空、无空括号。

5. **成品落点**
   - 四个 rules-* 文件（逐处落点见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06a1.md` 各行「成品落点」列）
   - **来源**：v0 `d23c461:skills/fiction-craft/references/rules.md` 各条「反例（≥2）」块与文件头「全域边界」；`notes/slice-prep-2026-11-04.md` §3.1。

### D3 v0 有而 v3 没有的块级合并（7 条）怎么定性与落笔

1. **情境**
   - 已知：逐块比对出 7 条规则有 v0（且 v1 多数也有）而 v3 缺失的块：FC-02 探索式分支与出口、FC-06 等权主线/照应联系/三案出口、FC-07 机械扩写豁免、FC-08 宁静停顿豁免、FC-13 喜剧寓言另审、FC-17 急稿条件、FC-18 有条件日课。
   - 推断：v1（有意重写轮）保留了这些块，v2/v3 的收紧属连带而非口径宣言——v3 对同类收紧（如 FC-13 的「按最严写实处理」）在别处反而保留 v0 硬口径，说明不是一致的收紧方针。
   - 用户要求：恢复内容须能在 v0 找到对应；不把有意调整当丢失。

2. **区分信号**
   - 走「合并」的信号：块在 v0 与 v1 都在、v3 无、且与 v3 现行分支不冲突（补入后是放宽选项，不是推翻现行规则）。
   - 反信号（不补）：只有 v1 有的（如 v1 RC-03 的四分法、RC-09 的「不强制四职」）；v1 软化被 v3 明确反转的（如 v1「不自动按最严写实处理」vs v3 保留 v0 硬口径）。
   - 判错的代价：把 v3 的有意硬口径当丢失恢复，会撤销现行决策；把连带删除当有意收紧，会继续缺可用的失败出口。

3. **两条分支的做法**
   - **A（采用）**：按 v0 语义以现行文风并入现有块（规则句或卡住时），不用 v0 原句，不带 H 标记与来源词；每条记 LI 决定（002/006/007/008/013/017/018）。
   - **B**：恢复 v0 原文。判为错：v0 原句带来源锚点与「用户明确要」类措辞，触发红线。
   - 冲突时停下请作者裁决：无——两可处按「v0+v1 共有即连带删除」的既定口径落地，逐条记决定。

4. **反例与修复**
   - 推翻判断的情况：补入后与现行分支矛盾（如 FC-08 豁免与「长篇/连载要暂解+钩子」并列会读成两套要求）→ 用分号分层并把豁免放在量词前（「宁静过渡、氛围篇章或已完成的段落可以不设钩子」先于「长篇/连载要……」）。
   - 修复后复查：每条 FC 卡块结构不变；「卡住时」仍是最后一块；SKILL.md §5 卡片与规则文件无矛盾（卡片为摘要，规则文件为准的声明在四文件文件头）。

5. **成品落点**
   - `.../references/rules-premise-and-structure.md` FC-02 规则/卡住时、FC-06 规则/怎么做/卡住时
   - `.../references/rules-units-and-endings.md` FC-07 规则、FC-08 规则
   - `.../references/rules-drafting.md` FC-13 规则
   - `.../references/rules-revision-and-method.md` FC-17 规则、FC-18 规则
   - **来源**：v0 `d23c461:skills/fiction-craft/references/rules.md` RC-02/06/07/08/13/17/18；v1 同名 RC 各节。

### D4 SKILL.md 合同类怎么落地（C.3 第 1–3 条、四词回执、审计词清除）

1. **情境**
   - 已知：本片是该 skill 首片，基线 SKILL.md 为 v3 原文：description 列 5 个兄弟 skill 缺 preset-card-generation；§1 转介表 6 行无预设卡、无接收向、无 C.2 归属行；§6 路由表 3 列缺「需要时补读／缺料或冲突时的出口」；§3 六个操作无失败出口；§9 五态回执（已核实/未执行/证据不足/受阻/不适用）并残留 `PASS`。
   - 推断：五态与 `PASS` 是 v3 沿用的旧状态体系，与合同四词冲突；diagnosis.md:411 的「中文五态一一对应」句依赖 SKILL.md §9，须两处一致（SKILL.md 归本片，diagnosis.md 归 S06a2）。
   - 用户要求：按套件合同第七节第 1–3 条与第二节 2.1/2.2 落地。

2. **区分信号**
   - 走「本片改」的信号：合同指派给 SKILL.md 合同类的内容（description/适用与转介/路由表两列/失败出口）与红线明令的审计词（`PASS` 在红线清单内）。
   - 反信号（不动）：SKILL.md 的内容性正文（§4 症状速查、§5 规则卡）属 a2/a3 的内容单元；§7「标『未证实』」与 scope-and-conflicts.md 联动，留给对应分片同步（移交项）。
   - 判错的代价：越界改 §5 会与 a2/a3 冲突；漏改 `PASS` 会在红线检查上挂掉。

3. **两条分支的做法**
   - **A（采用）**：description 补第 6 个兄弟名；§1 补预设卡行、「重叠请求的归属」表（C.2 相关行：帮我规划一本书/写这一章/审这一章/去 AI 味）与「从 preset-card-generation 转入」接收向（D2=A 双向）；§6 21 行全补两列（出口内容逐个锚定到各文件现有出口）；§3 六个操作各补一行「缺料或冲突时」（锚定 FC 卡卡住时与附录 E 用例）；§9 五态收敛为四词、回执模板改四词字段、`PASS` 句改写。
   - **B**：等 a2/a3 一起改。判为不合规：合同指派 SKILL.md 合同类给首片，且路由表两列是 8 个 skill 的统一动作。
   - 停下请作者裁决：无——C.1/C.2/D2=A 已定稿。

4. **反例与修复**
   - 推翻判断的情况：路由表出口写成各文件没有的内容（编造）→ 逐个 grep 落点文件核实后才写（planning.md 六项输入、drafting.md 场景卡四项、diagnosis.md 诊断前置、revision.md 介入级别、research 的「尚待原件核对」等均在文件内核实）。
   - 修复后复查：双向转介与 scene 包的写法对齐（scene 已含「整体诊断、选题与读者反馈转 fiction-planning-and-diagnosis」的接收向）；`PASS`/五态在 SKILL.md 零命中。

5. **成品落点**
   - `.../SKILL.md`（description、§1、§3、§6、§9）
   - **来源**：`notes/suite-contract.md` 第一节 C.1/C.2 与 D2=A 两表、第二节 2.1/2.2、第七节第 1–3 条；计划 2.6 节、附录 E（FP-T2 梗概层诊断）。

### D5 §3.1 指名残留的归属核对与片界（哪些本片改、哪些移交）

1. **情境**
   - 已知：slice-prep §3.1 指名 7 组残留，散在 rules-*（本片）、scope-and-conflicts（a3）、self-check-modern-and-zh（S06b）、diagnosis.md（a2，另由合同 2.3 #3 指派）。
   - 用户要求：逐行核对落点文件是否由 rules.md 谱系对齐而来，属本片的逐条改写并记决定，不属本片的登记移交、不动。

2. **区分信号**
   - 走「本片」的信号：落点文件的四文件头自述覆盖 FC-01–21，且 r2 表 RC 单元与之对应。
   - 反信号（移交）：scope-and-conflicts.md 对齐 v0 同名文件（r2 表 scope 各行）、self-check-* 对齐 fiction-craft-and-language（r2 表 CL 各行）、diagnosis.md 对齐 v0 fiction-craft/references/diagnosis.md（r2 表 diagnosis 各行）——均非 rules.md 单元。

3. **两条分支的做法**
   - **A（采用）**：本片改 rules-* 三处第 8 行、rules-drafting 五处指名残片＋复扫新增同类残片、rules-revision-and-method:148；scope/self-check/diagnosis 逐项登记移交（LI 文件「§3.1 逐项核对结果」表）。
   - **B**：顺手全改。判为越界：会动其他分片的独占文件，破坏分片账。

4. **反例与修复**
   - 推翻判断的情况：复扫发现指名五处之外同文件还有 11 处同类 `-NNNN` 残片——同谱系同文件，扩为本片责任一并清除，并在 LI 记录里写明「复扫新增」，不留待 P4 才发现。
   - 修复后复查：移交项在本片成品中保持基线原样（diff 仅 5 个本片文件变化）。

5. **成品落点**
   - 本片落点见 LI-FP-001–022；移交清单见 LI 文件「移交项」
   - **来源**：`notes/slice-prep-2026-11-04.md` §3.1；r2 表 scope/self-check/diagnosis 各行的谱系列。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **v0 `source-index.md`、`version-and-provenance.md`、`p4-field-guide.md`**：不适用。三者不属本片（a2/a3 段），且 source-index/version-and-provenance 在 r2 表标 `SOURCE_ONLY`，按 2.8 节不直接恢复。
- **v3 `examples/rule-examples.md`**：不适用。对齐 v0 同名文件（a3 段），r2 表无该文件带信号的单元；本片仅复扫登记其既有命中，未改动。
- **templates/ 四张表**：不适用。对齐 v0 templates（a3 段）；模板规范（R18 §2a）的逐编号核查由 a3 分片做。
- **`agents/openai.yaml`**：不适用。基线无来源字段与审计词，无两可分支。
- **GQ5 真实任务**：不适用。D3-C 授权范围为静态交付；效果验证不在本片，静态通过不写成效果已证明。

---

# S06a2 决策链（R17 §4a）· v0 fiction-craft a2 段（diagnosis / drafting / planning / examples）

- 分片：**S06a2**｜代理：Agent 4｜轮次：W3 主体轮第 5 批｜日期：2026-11-05
- 依据：`notes/suite-contract.md`（重点第二节 2.3 替换表第 3 行）、`notes/slice-prep-2026-11-04.md` §1.1/§3.1、`notes/source-synthesis/line-editing-and-proofreading.md` 第二节（W3 统一口径）、r2 表本片四文件 41 单元、S06a1 移交节。
- 逐条决定见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06a2.md`（LI-FP-024–067，44 条：合并 1、不恢复 43、恢复 0）；附录 B 结果见 `notes/quality/fiction-planning-and-diagnosis/s06a2-desourcing-selfcheck.md`。
- 出处只写在各链第 5 项「来源」小项，不进成品；成品在 `output/fiction-planning-and-diagnosis/` 本片 4 文件。

### D1 四个工作流文件的「找回边界」怎么定（LI-FP-024–064）

1. **情境**
   - 已知：v0 diagnosis（19417 B）/drafting（16449 B）/planning（17761 B）/examples（21235 B）共 74.9 KB；r2 表 41 个单元（diagnosis 23、drafting 4 含 K-16、examples 11、planning 3），flag 为 RENUMBERED?/UNALIGNED?/SHRUNK;BLOCK_LOST/—；v1 把三工作流融合为 `07-workflows.md`（12464 B，§5 明写「旧失败出口的重新裁决」），v2/v3 拆回三个同名文件并把 examples 改题「示范 1–4」。
   - 推断：v0→v1 是按决策对象融合的有意重写，不是丢失事件；v2/v3 的差异另有来路（合规增补与字段中译），须逐条对 v1 定性。
   - 用户要求：按 r2 找回丢失项；缩减幅度是信号不是应补回的量；P1 三类不算丢失逐条排除。
   - 拿不到的：v1/v2 融合与拆分时的取舍说明；不猜，以文本证据定性。

2. **区分信号**
   - 走「不恢复（v3 已有）」的信号：v3 落点逐块含 v0 的小块（证据/分支/验证/建议/严重度、表行、模板字段），或 v3 是超集。
   - 走「有意调整、不回退」的信号：v1 文本明写新口径（「场景卡未填满仍可写」「片段只诊断片段」「首段不必四项齐全」）；v1 软化而 v3 回到 v0 口径的（S5 四职），判后版有意选择。
   - 反信号（须查）：v0 有、v1 有、v3 无的块——本片逐单元核对后**零命中**，无一条触发合并/恢复。
   - 判错的代价：把有意调整当丢失补回 → 回退后版口径、破坏合同；把连带删除当有意调整 → 知识缺失。本片两者的原始风险都低（41 单元全有落点），主要风险在残留漏清。

3. **两条分支的做法**
   - **A（采用）**：41 单元逐块比对（S1–S9 表行、九个症状节、诊断前置/严重度/报告写法/纪律、起草 §0/§7(K-16)/§11/§12、示范 1–4 与附、规划 §0/§10/§11），全部记「不恢复」；把比对中发现的残留（艺名、作品人物名、来源篇数、漏译残词、年代指涉、空格残迹）折入所属单元一并清除。
   - **B**：按 r2 字节差（如 K-16 的 1449→348）补内容。判为错误：字节差是脚本按 ID 去重的计量假象，逐块比对证明内容在位。
   - 停下请作者裁决：无——差异全部可定性。

4. **反例与修复**
   - 推翻判断的情况：任一单元在 v3 缺块、或清除后句子不通、或 v3 措辞与 SKILL.md 路由/模板不一致。
   - 修复：发现即并入对应 LI 行处理（如「28 本证据覆盖」折入 LI-FP-059、「hierarchy」折入 LI-FP-063）；修完复查 diff 仅 4 个本片文件变化、相对链接与表格分隔行完好。

5. **成品落点**
   - `.../references/diagnosis.md`、`.../references/drafting.md`、`.../references/planning.md`、`.../examples/planning-cases.md`
   - **来源**：v0 `d23c461:skills/fiction-craft/references/{diagnosis,drafting,planning,examples}.md`；v1 `d2003e4:…/references/07-workflows.md`；v2 `3c1cb5f`／v3 `2a10c07:skills/fiction-planning-and-diagnosis/` 同名落点；r2 表 41 行。

### D2 合同 2.3 #3：diagnosis.md:411 状态码清单怎么替换（LI-FP-065）

1. **情境**
   - 已知：基线 ：411 段（v3 新增的「验证回执字段」）含状态码清单 `VERIFIED/NOT_PROVEN/NOT_RUN/BLOCKED/NOT_APPLICABLE`＋`PASS/FAIL`＋「与 SKILL.md §9 的中文五态一一对应（已核实/未执行/证据不足/受阻/不适用）」联动句＋「两者不并列成两份回执」表述；SKILL.md §9 已被 S06a1 改为四词与「交付回执模板」。
   - 用户要求：合同 2.3 #3 改四词、删内部状态码清单、删五态联动句、回执统一为四词不并列两份；改后 #9 复扫零命中。

2. **区分信号**
   - 「替换合格」的信号：段落仍承担原功能（工作记录字段清单＋历史回执不继承），状态只用四词并锚定 SKILL.md §9，全段无审计词、无两份回执的自述。
   - 反信号：为躲正则把「状态」删成空话；或保留任何一枚状态码/五态对照。
   - 判错的代价：#9 复扫不零命中 → 合同 2.3 不闭合；删掉字段清单 → 工作记录失去留底口径。

3. **两条分支的做法**
   - **A（采用）**：整段重写为「状态只用 SKILL.md §9 的四个词填写：已完成、依据、未能核实、待作者决定。对作者交付按 SKILL.md §9 的交付回执模板声明；本字段清单是同一份回执的留底字段，不并列成两份回执」，保留字段清单与「历史回执不自动继承」句，删状态码清单与五态联动句。
   - **B**：只删审计词保留句式。判为不够：「五个状态码…一一对应」句仍在，四词口径仍被架空。
   - 停下请作者裁决：无——合同已写死。

4. **反例与修复**
   - 推翻判断的情况：新句引入新的枚举/对照（又造一份口径）；或「留底字段」与 §9 模板字段冲突。
   - 修复：字段清单只列记录项不再枚举状态；修完跑 #9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫，全包零命中。

5. **成品落点**
   - `.../references/diagnosis.md`「三问回归：结构、证据与不交付 → 验证回执字段」段
   - **来源**：`notes/suite-contract.md` 第二节 2.1/2.2/2.3 第 3 行、第七节 C.3 第 6 条；S06a1 移交节第 2 条。

### D3 残留清除的口径与「大师」判法（LI-FP-036/042/044/059/063/067）

1. **情境**
   - 已知：比对与复扫发现 v3 基线残留——「picaresque/tale」（来源语汇艺名）、「（如 Oedipus）」（作品人物名）、「28 本证据覆盖」（来源篇数，正则 #3 查不出）、「长篇补 hierarchy」（漏译残词，与同文件「主次」不一致）、「8–9 段是历史默认」（与 a1 在 FC-18 清除的同一措辞同源）、「不把 评论…」「见FC/只在FC」「压成 概述」等空格残迹；#5a「大师」在本片 2 处（planning:305、diagnosis:364）。
   - 用户要求：B.2/B.3 口径；自创例过骨架比对；不为躲正则改坏语义。

2. **区分信号**
   - 清除的信号：指向具体作品/人物/来源数量/年代的词，以及删除/替换后留下的空格残迹。
   - 保留的信号：「大师」出现在禁令对象或否定式承诺里（「不要用『大师也这样』当理由」「不承诺『改了就像某大师』」），无具体人物、无背书——沿用 a1 selfcheck 第二节判法（a1 移交节预先指名）。
   - 判错的代价：误删禁令对象会把规则改空；漏删「28 本」则来源篇数残留到 P4。

3. **两条分支的做法**
   - **A（采用）**：艺名/人名/篇数删除或通用化（判断语义原样保留）；「历史默认」对齐 a1 FC-18 口径改「常见默认」；「hierarchy」统一为「`主次`」；空格残迹修顺。
   - **B**：为「大师」另造措辞躲正则。判为不必要：命中实质不违规，S01 口径明言「不要为了零命中而改坏语义」。
   - 停下请作者裁决：无。

4. **反例与修复**
   - 推翻判断的情况：清除后句意变化（如「28 本」句去掉数字后限定语义丢失）。
   - 修复：改写保留限定（「超出本 Skill 已核对证据的覆盖…不证明类型规则」）；修完逐句回读＋全 11 类复扫确认归零。

5. **成品落点**
   - `.../references/diagnosis.md` §3 分支 C、§9 建议、§11 建议、§13；`.../references/planning.md` 文件头、§9、§10；`.../references/drafting.md` 文件头；`.../examples/planning-cases.md` 头部、NP-07/NP-14（两处）、RV-03、附-5
   - **来源**：v0 同名文件对应行（`examples.md` 示范 4 输入段的「28 本」句；`planning.md` §5 的「PG30776 单来源」（v2 已清）与 §9「历史默认」）；附录 B.2/B.3。

### D4 v0「P4 修订使用说明」三处元说明怎么定性（LI-FP-066）

1. **情境**
   - 已知：v0 在 diagnosis/planning/examples 文末各有「P4 修订使用说明」块引（revision/scope 两处归 a3 谱系）；v1/v2/v3 全部无（git grep 四版零命中于 v1 起）。
   - 推断：v0→v1 有意删除的上一轮元说明（标签本身含审计词「P4」），不是 v3 连带删除——但须核实质是否被承接。

2. **区分信号**
   - 实质承接的信号：逐句能在 v3 找到等价物——diagnosis 之「不能以没有场景卡为由拒绝写作」→ drafting §0 假设路径＋SKILL.md §1「写这一章」路由；planning 之「群像等权主线、探索式先试写、固定段数不当硬门」→ a1 已修 FC-02/FC-06；examples 之「固定数字不作跨作品标准」→ 示例头部声明＋附-4。
   - 反信号：任何一句在 v3 找不到落点 → 升级为合并项。本片逐句核完：全部有落点。

3. **两条分支的做法**
   - **A（采用）**：不恢复三处块引；定性记 LI-FP-066，逐句写明承接位置。
   - **B**：补回（去审计词版）。判为不必要：内容重复，且元说明不属交付正文。
   - 停下请作者裁决：无。

4. **反例与修复**
   - 推翻判断的情况：任一承接句被后续分片改动导致落点失效（本片核查时均在位；承接位置分属本片 drafting §0、a1 的 FC-02/FC-06 与 SKILL.md §1，后续分片收口时须避开这些句的语义）。
   - 修复：若 W4 发现失效，按本链第 2 项升级为合并项补回通用句。

5. **成品落点**
   - 无新增落点（承接位置见第 3 项）
   - **来源**：v0 `d23c461:skills/fiction-craft/references/{diagnosis.md:402, planning.md:350, examples.md:217}`；v1 `07-workflows.md`；a1 `fiction-planning-and-diagnosis-S06a1.md` LI-FP-002/006。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **r2 `K-16` 行（SHRUNK;BLOCK_LOST）**：不适用（无内容决策）。经核实为脚本按 ID 去重的计量假象：v0 按 drafting §7 定对话功能计量（1449 B，块标「检败」与该节「可观察检查/失败出口」吻合），v2/v3 按 scope-and-conflicts §2 的 K-16 表行计量（348 B）；drafting §7 逐块在位，scope 的 K-16 条目本体归 S06a3。结论已写进 LI-FP-048 与移交项，防 a3 误补。
- **`templates/` 四张表、`references/revision.md`、`examples/rule-examples.md`、`references/scope-and-conflicts.md`、`source-index`/`version-and-provenance`**：不适用。均属 a3 段（派发说明明定），本片未动。
- **S06b/S06c 落点**（self-check-*、examples/self-check-cases.md、examples/research-and-feedback-cases.md、research-and-verification、reader-feedback）：不适用。对齐 fiction-craft-and-language / reader-experience-and-critique / research-fact-verification 谱系；命中按归属登记待对应分片。
- **GQ5 真实任务**：不适用。D3-C 授权范围为静态交付；静态通过不写成效果已证明。

---

# S06a3 决策链（R17 §4a）· v0 fiction-craft a3 段（revision / rule-examples / scope-and-conflicts / templates / 来源类两件＋p4-field-guide）

- 分片：S06a3｜代理：Agent 4（a3 段子代理）｜轮次：W3 主体轮第 5 批｜日期：2026-11-05
- 依据：`notes/suite-contract.md`（K2 定稿：第二节四状态词、第三节模板规范、第四节附录 B/B.2/B.3）；`notes/loss-inventory/raw/fiction-planning-and-diagnosis-2026-11-04-r2.md`（revision 22 行、scope 9 行、source-index 3 行 SOURCE_ONLY、templates 8 行、P4 单元）；`notes/slice-prep-2026-11-04.md` §1.1/§3.1；`notes/source-synthesis/line-editing-and-proofreading.md` 第二节（W3 统一写法口径）；a1 分片记录的定性口径与移交节；a2 决策链的片界声明（上方不适用节：a3 段文件 a2 未动，与本片互核一致）。
- 逐条决定与九列记账见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06a3.md`（LI-FP-101 至 144）；附录 B 扫描与 B.3 回读见 `notes/quality/fiction-planning-and-diagnosis/s06a3-desourcing-selfcheck.md`。本节只写五条复杂决策链；下接「不适用」节声明片界。

## 二、决策链

### D1 四谱系的 r2 信号（RENUMBERED?/UNALIGNED?）怎么对齐到 v3 落点

1. **情境**
   - 已知：本片四个内容谱系在 r2 表共 40 个单元（revision 22、scope 9、templates 8、P4 1），flag 全为 `RENUMBERED?` 或 `UNALIGNED?`，无 MISSING、无 SHRUNK、无 BLOCK_LOST；rule-examples 与 version-and-provenance 无独立单元行。
   - 推断：v0→v1 是按决策对象融合的重写（revision→07-workflows §3、scope→08-conditions、rule-examples→craft-rule-examples、templates→planning-diagnosis-workbook），v1→v2/v3 按文件还原并改号（RC→FC、DESIGN_EXAMPLE→「编写的示范」、CONDITIONAL/UNRESOLVED→「有条件/两说」）；r2 的 UNALIGNED? 集中在节名改写的位置（scope §3/§3.1/§4.1/§4.3、revision §2.1），不是内容缺失。
   - 用户要求：UNALIGNED? 是待精读信号；按分片口径只处理本片谱系；不把缩减幅度当应补回的量。
   - 拿不到的：v2/v3 改号与节名改写的取舍说明；按内容核定，不猜。

2. **区分信号**
   - 走「改号/改写对齐」的信号：revision §0–§11 与 v0 章节一一对应；scope §1 15 行条件表、§2 K-01–19、§3 19 参数行、§3.1 12 条目、§4.2 12 域表、§4.4 十条逐行在位；templates NP-01–14/DR-01–12+SUM/RV-01–12/SP-01–12 逐行在位；rule-examples FC-01–21 各一示例四行结构齐全。
   - 反信号（判缺失）：无——无任何 v0 单元在 v3 找不到标题或内容块对应；v0 独有的尾注（revision/scope 各一条「P4 修订使用说明」）逐句在包内有承接。
   - 判错的代价：把改号对齐当缺失会整批重写、带回来源锚点结构；把真缺块当对齐会漏恢复。本片按逐块比对排除了两种误判。

3. **两条分支的做法**
   - **A（采用）**：逐单元按「标题/行对应＋块结构」比对 v0↔v1↔v3；v0、v1 都有而 v3 没有的判连带删除走合并——实测为 0 块（三谱系规则本体全在位）；差异全部是来源残留、状态词词形与合同格式缺口，逐处记 LI-FP-101–144。
   - **B**：按 UNALIGNED? 当缺失重写。判为错：会覆盖 v1→v3 的有意改号与去来源改写，并触发红线。
   - 停下请作者裁决：无——a1 已定性「v0→v1 有意重写、先核 v1 再定性」的口径，本片沿用。

4. **反例与修复**
   - 推翻判断的情况：a2 决策链提示「K-16 表行本体归 S06a3」——复核 v3 scope §2 K-16 行在位且来源指涉（李渔宾白）已被 v3 清除，无需补块，只在 LI-FP-124 登记。
   - 修复后复查：44 条决定逐条有 v0 位置与 v3 落点；无一处新增自创规则。

5. **成品落点**
   - `output/fiction-planning-and-diagnosis/references/revision.md`、`references/scope-and-conflicts.md`、`examples/rule-examples.md`、`templates/`×4（对齐判定本身无新增落点，改动见 D2–D4）
   - **来源**：v0 `d23c461:skills/fiction-craft/references/{revision,scope-and-conflicts,rule-examples,p4-field-guide,source-index,version-and-provenance}.md` 与 `templates/`×4；v1 `d2003e4:skills/fiction-planning-and-diagnosis/references/{07-workflows,08-conditions-and-boundaries}.md`、`examples/craft-rule-examples.md`、`templates/planning-diagnosis-workbook.md`；r2 表各对应行。

### D2 scope §3 行 74–76 指名残留（残片＋年代）与同文件年代清除怎么改写

1. **情境**
   - 已知：§3.1 指名 scope-and-conflicts.md 74–76 行：`-2236`、`-2111` 残片与「1890 年代英国市场」「1911 年前的手册」（「1900 年的杂志分类」同句）；a1 复扫已把 #2/#3 命中登记为待本片处理。
   - 推断：v0 行 74 锚点是 `PG72910 L2235-2236`、行 76 是 `PG13589 L2107-2111`，v2→v3 去来源时截断留残片；同文件 §1/§4.2 的「1900–1926」「1916」「1911」「1920」是同轮漏清的同类残留（v2→v3 清了 §3.1 与 4.1 的来源清单，漏了表格行内的年代词）。
   - 用户要求：红线禁来源编号残片与年代；§3.1 指名项本片必做。

2. **区分信号**
   - 走「清除并改写」的信号：年代词只承担「这是历史惯例、别当现代标准」的限定功能，该限定可写成不带年代的陈述（a1 对 FC-01/FC-12/FC-20 的同型处理：「特定时期市场约定」「特定时期印刷市场的观察」）。
   - 反信号（保留）：表行的判断本身（「只作历史注；不进入规则」「不能用于当代字数判断」）与参数数字（5–8 万字、34 型）——数字是操作默认/历史条目名，不是来源年代；「历史约定」「历史默认」无具体年代，不在红线。
   - 判错的代价：把参数数字也当年代删掉会丢可操作性；保留年代词则在附录 B #3 与红线上挂掉。

3. **两条分支的做法**
   - **A（采用）**：行 74 残片＋年代→「特定历史时期的市场惯例，已过期」；行 75→「早期手册与杂志的历史分类」；行 76 残片→「商业剧场惯例」；同文件扩清 6 处：行 12（对齐 a1 FC-01 口径）、行 18/89/122（「早期无声片」）、行 45（对齐 a1 FC-20 口径）、行 118（「历史分类样本」＋「特定时期的市场偏好」）。逐处记 LI-FP-123/124/125/130。
   - **B**：整表重写。判为过：19 行参数与 15 行条件表的现行写法完好，重写引入无意改动。
   - 停下请作者裁决：无——红线已明确。

4. **反例与修复**
   - 推翻判断的情况：改写后句子承担不了原限定（如行 74 删「1890 年代英国」后「已过期」没了对象）→ 保留「特定历史时期的市场惯例」作主语，句子仍完整表达「历史注、不进规则」。
   - 修复后复查：全文件复扫 #2/#3 零命中；通读无主语悬空；术语（probability、latent、scène à faire）为 v2/v3 有意保留、11 类不命中，登记 selfcheck 供 W4 复核。

5. **成品落点**
   - `.../references/scope-and-conflicts.md` §1 行 12/14/18/25、§2 K-10、§3 行 74/75/76、§3.1 行 89、§4.2 行 118/122
   - **来源**：v0 `d23c461:skills/fiction-craft/references/scope-and-conflicts.md` §1/§2/§3/§4；`notes/slice-prep-2026-11-04.md` §3.1；a1 LI-FP-001/020 的同类改写口径。

### D3 「未证实」词形收敛到四词（scope 三处＋revision 两处＋rule-examples 括注）怎么与 SKILL.md 联动

1. **情境**
   - 已知：§3.1/移交指名 scope §3 三处「标 未证实」（行 14/25/67）；主代理已改 SKILL.md §7 为「作者自选时按交付状态词记“未能核实”（scope-and-conflicts §3）」；本片复扫另发现 revision.md 两处「未证实」（:177/:199，v0 `NOT_PROVEN` 的直译）与 rule-examples 文件头「不证明任何效果（未证实）」括注；a1 的 rules-revision-and-method.md 也有 3 处同词形（非本片文件）。
   - 推断：「未证实」是 v2/v3 替换审计词时用的过渡词形，不在合同四词内；行 67 的语境（作者自选参数）与 SKILL.md §7 联动句一一对应，行 14/25 是能力边界声明、:177/:199 是方法效果声明。
   - 用户要求：交付状态只用四词；与 SKILL.md:292 联动措辞对齐。

2. **区分信号**
   - 走「收敛为四词」的信号：三处语境都是「检查已执行/边界已声明，但结论依赖未覆盖数据」＝合同 2.1 的「未能核实」定义。
   - 反信号（不收敛）：「已发布版不改」「未知」「未覆盖」等非状态词——它们不是对交付项的状态标注（「未知」还是模板合法值）；rule-examples 括注在「不证明任何效果」句内属冗余，直接删括注而非替换词形。
   - 判错的代价：把「未知/未覆盖」也替换会破坏模板合法值与 DR-12 口径；不收敛「未证实」则四词口径在本包内分裂。

3. **两条分支的做法**
   - **A（采用）**：行 67 改「作者自选时按交付状态词记“未能核实”」（与 SKILL.md §7 逐字对齐）；行 14/25 改「相关交付按状态词记“未能核实”」；revision :177 改「修订的整体效果记“未能核实”：没有对照实验证明“改得多=更好”」、:199 改「本节方法的效果记“未能核实”」；rule-examples 删括注。逐处记 LI-FP-111/112/114/123/126/140。
   - **B**：统一改成一个固定句式。判为僵化：三处语境（自选参数/能力边界/方法效果）句式不同，生搬同一句会读不通。
   - 停下请作者裁决：无——四词口径与联动句已由合同与主代理定稿。

4. **反例与修复**
   - 推翻判断的情况：a1 文件的 3 处「未证实」（rules-revision-and-method :43/:78/:216）——同词形同问题，但属 a1 已修 5 文件，本片不得越界；改登记移交项，不动作。
   - 修复后复查：本片 7 文件「未证实」复扫零命中；a1/a2 文件的余量在移交项逐处列明（a2 的 drafting:320、diagnosis:399 同口径待其收口）。

5. **成品落点**
   - `.../references/scope-and-conflicts.md` 行 14/25/67；`.../references/revision.md` :177/:199；`.../examples/rule-examples.md` 文件头
   - **来源**：`notes/suite-contract.md` 第二节 2.1/2.2；SKILL.md §7（主代理已改的联动句）；`notes/slice-prep-2026-11-04.md` §3.1。

### D4 templates×4 的合同第三节落地（三列补齐＋四词文件头＋novel-plan 清理）怎么定列与措辞

1. **情境**
   - 已知：合同第三节要求有枚举编号的模板「每个编号独占一行、值/状态/稿件证据位置三列齐全、允许未知、证据位置只指用户当前稿件、有 GFM 分隔行」；四张 v3 模板每编号一行与分隔行已合规，「填写内容」即值列，缺「状态」「稿件证据位置」两列；SKILL.md §6 路由行已承诺「各表的填写行与『未知』的用法；证据位置只指当前稿件」；两个文件头教填写者写「未定/待补」「未授权」（非四词）；novel-plan 有「单来源参数」×3 与 NP-09「若干必要特征」同文件不一致。
   - 推断：四张表是交付模板（SKILL.md §6 路由「交付」行），三列缺失是合同缺口不是内容丢失；「单来源」是来源材料结构的指涉（scope §3 v3 已改名「操作默认与历史数值」）；NP-09 的「若干」是 v3 机械替换漏改（同文件说明 8、最低标准、FC-20 本体、scope K-10 均为「3–5」）。
   - 用户要求：派发说明把 templates 三列补齐列为本片必做口径。

2. **区分信号**
   - 走「在主表加列」的信号：SKILL.md §6 已按三列口径承诺四张表的用法，加列使承诺兑现；列序「填写内容→状态→稿件证据位置→依据规则→出口」保持「值在前、账在后」的填写动线。
   - 反信号（另建状态账表）：四表各加第二张表会重复编号、破坏「每个编号独占一行」的单一台账结构——判不采用。
   - 判错的代价：不动则 P5 preflight spec 无从核对字段；加错列序会打乱既有填写习惯与 SKILL.md 承诺的措辞。

3. **两条分支的做法**
   - **A（采用）**：四张主表各加「状态」「稿件证据位置」两列（空单元格待填），分隔行同步 6/7 列；四表说明/纪律各加一条三列用法（四词＋未知合法＋不得把未知写成已完成＋证据位置只指当前稿件＋无则填未知）；novel-plan 文件头「未定项写“未定/待补”」→「如实标“未知”或“待作者决定”」、scene-plan 同、revision-sheet「未授权项写“未授权”」→「未授权项记“待作者决定”」；novel-plan「单来源参数」×3→「操作默认值」、NP-09 统一回「3–5 必要特征」。逐条记 LI-FP-133–139/144。
   - **B**：只在 SKILL.md 写规范不动模板。判为不合规：合同第三节是对模板本体的落地要求，且派发说明指名 templates 落点按合同第三节执行。
   - 停下请作者裁决：无——模板规范 R18 §2a 已在合同定稿。

4. **反例与修复**
   - 推翻判断的情况：DR-03（证据定位字段）与「稿件证据位置」列疑似重复→区分后并存：DR-03 装证据本体（位置＋短引文），新列装该行交付状态账，语义不同层。
   - 修复后复查：全包表格列数校验脚本零差异（表头与数据行列数一致）；四表分隔行齐全；「未定/待补」「未授权」在四表文件头零残留；「单来源」全包复扫仅 scope §4.4 第 7 条的 v3 既有写法（已改「操作默认值」……复核：scope:142 现文为「不把操作默认值……写成硬门」，无「单来源」残留）。

5. **成品落点**
   - `.../templates/novel-plan.md`、`templates/diagnosis-report.md`、`templates/revision-sheet.md`、`templates/scene-plan.md`（主表两列＋说明条＋文件头）
   - **来源**：`notes/suite-contract.md` 第三节、第二节 2.1；SKILL.md §6 路由行既有承诺；计划验收第 5 条（模板可逐项填写）。

### D5 来源类三件（source-index / version-and-provenance / p4-field-guide）与 rule-examples 的「不恢复」判定

1. **情境**
   - 已知：source-index（17449 B，r2 三单元 `SOURCE_ONLY`）、version-and-provenance（4637 B，r2 无单元、v1 即删）、p4-field-guide（2705 B，r2 `P4` 单元 1166 B `UNALIGNED?`）三文件 v1 起在包内不存在；派发口径按 2.8 节「不可拆 ≠ 应恢复」；rule-examples 21 示例 v3 在位但带 2 处残留。
   - 推断：三件全部是来源台账/索引类（PG 清单、SHA 台账、锚点速查表）；「P4」单元的 8 条速查是 rules.md 对应 RC 条目的压缩索引，自述「不得把本文件中的例子直接升级为无条件指令」。
   - 用户要求：SOURCE_ONLY 不直接恢复；不建新文件。

2. **区分信号**
   - 走「不恢复」的信号：文件主体是来源身份、锚点、行号、台账——红线禁项；无超出规则本体的增量内容。
   - 反信号核对（有可通用语义才考虑）：逐件核实——source-index §3 谱系去重的通用语义（同源转述按一个来源算、条数不当可信度投票）在 `research-and-verification.md` RS-05/来源依赖节在位（S06c 谱系）；「不新增来源、不冒充依据」在 SKILL.md §6 与 rules 文件头在位；version-and-provenance 的「不分发原著」「静态验证不证明效果」在 SKILL.md §2/§9 与 scope §4.3 在位；p4-field-guide 八条的操作语义在 FC-01/03/04/05/09/10/11/19 规则卡在位。全部有落点，无遗留。
   - 判错的代价：恢复任何一件都会带回 PG 编号、人名、年代与审计词，P4 必挂；漏核通用语义会误删可用规则——已逐句核实排除。

3. **两条分支的做法**
   - **A（采用）**：三件不恢复、不建新文件，通用语义落点逐句写进 LI-FP-141–143 理由列；rule-examples 只清 2 处残留（文件头括注、latent image 术语不一致），「大师」×3 与「1900 年代」演示年份判允许（B.2 第 4 条＋a1 判法），B.3 骨架比对通过。逐条记 LI-FP-140–143。
   - **B**：把 p4-field-guide 改写成去来源速查卡补回。判为不必要：与四个 rules 文件、examples 全量重复，且「不可拆 ≠ 应恢复」（S04b 口径）。
   - 停下请作者裁决：无——2.8 节与红线已明确。

4. **反例与修复**
   - 推翻判断的情况：r2 `P4` 单元 `UNALIGNED?` 若对应 v3 缺失的通用内容则需恢复——精读确认 1166 B 全部是带 PG 锚点的速查表行，无独立规则；修复方式为在 LI-FP-142 写明八条与 FC 规则卡的对应关系，防后续误补。
   - 修复后复查：全包无 `source-index`/`version-and-provenance`/`p4-field-guide` 引用残留（a1 复扫与本片复扫双确认）；无新建文件。

5. **成品落点**
   - 无新增落点（判定与对应关系记 LI-FP-141–143；rule-examples 清残留落 `.../examples/rule-examples.md`）
   - **来源**：v0 `d23c461:skills/fiction-craft/references/{source-index,version-and-provenance,p4-field-guide}.md`；r2 表 PG492/P4/§3/§4 各行与 flag 语义表（SOURCE_ONLY 含 version-and-provenance）；计划 2.8 节。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **SKILL.md 合同类**：不适用。a1 已按合同 C.3 完成（LI-FP-023）；本片只复用其 §7 联动句口径（D3），未动 SKILL.md。
- **a2 段落点**（diagnosis、drafting、planning、examples/planning-cases、examples/self-check-cases、examples/research-and-feedback-cases）：不适用。派发说明明定归 a2；本片复扫发现的 a2 余量（drafting:320、diagnosis:399 的「未证实」）已列移交项，未动对方文件。
- **`agents/openai.yaml`**：不适用。基线无来源字段与审计词，无两可分支。
- **S06b/S06c 落点**：不适用。命中按归属登记（selfcheck 第六节），未动。
- **GQ5 真实任务**：不适用。D3-C 授权范围为静态交付；静态通过不写成效果已证明。
- **r2 `K-16` 行（SHRUNK;BLOCK_LOST）与「见FC」残迹**：不适用（无复杂分支）。前者经与 a2 交接确认为脚本按 ID 去重的计量假象，scope §2 K-16 行在位且已去来源化，按「计量假象、不恢复」记入 LI-FP-124；后者为 6 处文件头排版粘连（「见FC」→「见 FC」），纯修复记 LI-FP-145。

# S06c 决策链（R17 §4a）· v0 reader-experience-and-critique ＋ research-fact-verification 两谱系

- 片名：**S06c**｜代理：Agent 4（S06c 段子代理）｜轮次：**W3 主体轮第 6 批**｜日期：2026-11-05
- 逐条决定与九列记账见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06c.md`（LI-FP-201 至 LI-FP-232）；附录 B 扫描结果见 `notes/quality/fiction-planning-and-diagnosis/s06c-desourcing-selfcheck.md`。
- 定性口径沿用 a1：v0 与 v1 都有而 v3 没有的判连带删除并合并补回；只有 v1 有的不补；v1 改写而 v3 跟随 v1 的判后版有意选择，不回退。

## 一、决策链

### D1 两谱系逐块对齐判定（reader 24 行＋research 69 行）

1. **情境**
   - 已知：两谱系在 r2 表全部标 `UNALIGNED?`（reader 24 行）或 `UNALIGNED?`/`SOURCE_ONLY`（research 69 行，A 类同一块按 A/R 双族 ID 重记），机械对齐按编号（R01–R12、R06–R19、C-1…C-5、A1–A11/B1–B5）与文件名失败；v1 为融合稿（reader 谱系融进 `06-feedback-and-readers.md`，research 谱系融进 `05-research-and-verification.md`＋工作簿 §一–四），v2/v3 拆回 `reader-feedback.md`（RF-01–12）与 `research-and-verification.md`（RS-01–14）并把示例改为自建 Case A–D。
   - 推断：UNALIGNED? 主因是改号（R→RF/RS）与改题（DESIGN_EXAMPLE→示范/自建示例），不是内容丢失；但要防两类误判——把去来源改写误判成缺失，把连带删除误判成有意调整。
   - 用户要求：按 r2 内容对齐判定，不检出、不改 skills/ 本体；SOURCE_ONLY 不直接恢复。
   - 拿不到的：v0 示例 A 类案例的来源原书上下文；只按 v0 文件内引文与标注判断。

2. **区分信号**
   - 走「不恢复（对齐在位）」的信号：v0 的方法块（触发/怎么做/后果/交付字段）在 v2/v3 有逐块对应，差异只在标签体系（F/H/P→三块改写）、审计词（OBSERVED/NOT_PROVEN/DESIGN_EXAMPLE→中文类别）与来源标注。
   - 走「合并补回」的信号：v0 与 v1 都有、v3 没有的方法块（实测两处：C-2 成果目标维度；逐条核查记录表＋整体摘要＋核验范围头）。
   - 反信号（不恢复）：带原句、行号、PG 编号、真实人名书名的 A 类案例与两个 source-index；纯标签体系（F/H/P、CONFLICT/REJECT 登记表）。
   - 判错的代价：把去来源改写当缺失会重复补回并带回源类残留；把连带删除当有意调整会让核查记录没有固定格式、复核者无法逐条追查。

3. **两条分支的做法**
   - **A（采用）**：逐单元三方比对（v0→v1→v3），reader 谱系 8 条与 research 谱系 14 条记「不恢复（对齐在位）」并逐条写承接落点；两处连带删除以「§10 核查记录的固定格式」合并补回，不新建模板文件（research 文件已在 SKILL §6 路由内，同 RF-12 内嵌交付行先例，且 SKILL.md 属 a1 已修文件不可加路由）；C-2 维度按 v1 语义补 §7.2 一行＋§10.1 一项。
   - **B（否决）**：新建 `templates/verification-record.md` 并改 SKILL.md 路由——越界（SKILL.md 属 a1）；把 A 类案例改写后全部搬回——缩减幅度是盘点信号，v3 的 4 个自建 Case 已承接演示职能，v0 案例含原句与真实人名书名是红线禁项。
   - 停下请作者裁决：无，两处连带删除均有 v0＋v1 双证据。

4. **反例与修复**
   - 推翻判断的情况：source-derived-checks 若核出某条动作的触发/后果只存在于 F 块（来源数据）而无方法语义——精读核实 14 条全部有独立方法语义（含 v1 的四条修订），双核对通过，flag 的 SOURCE_ONLY 判为文件名所致。
   - 修复后复查：failure-modes 23 条逐条找承接落点（#1 判 v1 有意放宽，其余 22 条逐条对应）；r2 无行的文件不漏核。

5. **成品落点**
   - `output/fiction-planning-and-diagnosis/references/research-and-verification.md` §10（新增）
   - **来源**：v0 `d23c461:skills/reader-experience-and-critique/`（7 文件）与 `d23c461:skills/research-fact-verification/`（9 文件）；v1 `d2003e4:skills/fiction-planning-and-diagnosis/references/{05,06}-*.md`、`examples/{fact-check-examples,reader-feedback-examples}.md`、`templates/planning-diagnosis-workbook.md`；r2 表两谱系 93 行（同一块按双族 ID 重记的行随块同判）。

### D2 C-2 成果目标与核查记录表的连带删除怎么补

1. **情境**
   - 已知：v0 `SKILL.md` 输入第 6 项、conflict C-2 行、templates §一 第 5 行三处都出现「要说服/打动，还是要可复核/可复制」；v1 三处都保留（工作簿 §一、C-2 行「两者可以兼得、缺目标给合理默认」）；v3 全文件 grep「可复核/说服」零命中。
   - 推断：v2/v3 把工作簿拆回四模板时只保留了 diagnosis-report/novel-plan/revision-sheet/scene-plan 四张枚举表；核验记录三类（范围头/逐条记录/整体摘要）无枚举编号、未随拆回，属结构性连带删除，不是有意精简（v1 无任何删减声明，且 v3 §6/§8 仍引用「断言表」）。
   - 用户要求：找回丢失项，交付状态词用四词。
   - 拿不到的：v2/v3 拆表时的取舍说明；按 v0＋v1 双证据定性。

2. **区分信号**
   - 「方法内容」信号：字段清单、必填规则（核查时点、来源自陈边界原样保留）、摘要项（已核/待核条数、未执行的检查、不用全对全错替代逐条判断）都是可执行方法。
   - 反信号：v0 模板里的英文状态码（VERIFIED_FOR_SCOPE 等）与「Claim ID」英文形态——恢复时改用 v3 既有中文域词（§5 六种结论、「断言 ID」），不照抄。
   - 判错的代价：不补回则核验结果没有固定记录行，§6/§8「写回断言表」成悬空引用；照抄 v0 则带回英文状态码与审计词。

3. **两条分支的做法**
   - **A（采用）**：在 `research-and-verification.md` 文末新增「§10 核查记录的固定格式」三小节：范围头五项（含成果目标一行）、逐条断言记录一行（13 字段，允许空值或「未知」，「未实际打开」显式句）、整体摘要四项；修订记录不重复建表（§8 散文式已在位）；§7.2 补一行「叙述 vs 逐条回查」的非冲突处理。
   - **B（否决）**：并入 §2 或改写 §9——§2 是断言解剖（记什么），与交付记录格式（怎么交）是两层，混写会破坏现有编号引用；SKILL.md §9 已是四词回执，不动。
   - 停下请作者裁决：无。

4. **反例与修复**
   - 推翻判断的情况：新写文本若出现「这批材料」「未证实」或英文状态码即违规——自查时「这批材料」在草稿中出现一次，已改为「本次待核资料」；状态列统一引 §5 六种结论。
   - 修复后复查：改后复扫全 11 类，新增文本零命中；§7.2 表三列对齐、分隔行不动。

5. **成品落点**
   - `.../references/research-and-verification.md` §10.1–10.3、§7.2 末行
   - **来源**：v0 `templates.md` 四单元＋`SKILL.md` 输入第 6 项＋`conflict-and-versions.md` C-2 行；v1 工作簿 §一–四与 C-2 行；计划 2.8 节（删掉的来源文件不直接恢复，但方法内容找回）。

### D3 悬空指涉与移交命中复核

1. **情境**
   - 已知：v3 基线 §4.1 有「本 skill 的历史例文代替不了相应的专业证据」——该词组在 v1 指来源历史例文（A 类案例尚在），v3 示例已全为自建，指涉悬空（正则 11 类查不出）；a1/S06a3 移交 research 谱系 #4 ×2、#8 ×3、#10 ×15＋reader-feedback #10 ×3 共 23 条命中待复核。
   - 用户要求：必做移交逐条复核，属核验语境的按 B.2 第 5 条判允许并写明理由；属真残留的改写。
   - 拿不到的：无。

2. **区分信号**
   - 「允许」信号：命中的词指**被核资料**（用户要核的译本、作品情节、更正记录、版本差异）或为正常词尾误报；「违规」信号：指向学习材料、包自身改动痕迹或来源编号。
   - 判错的代价：把核验方法本体（更正链、著录层级、原型拆分）改掉会破坏方法；把真残留留下会触发 B.3 与红线。

3. **两条分支的做法**
   - **A（采用）**：#4 ×2（「出自意译本」「书里的情节」）判允许——均为 RS-06/RS-09 方法本体内对被核资料的指涉；#8 ×3（更正记录/旧版和新版/更正的链条）判允许——均指被核资料的更正与版本，非包的改动痕迹；#10 ×18 逐条读原句，全为「证据/依据/意见/数据」词尾误报；「历史例文」改「本 skill 文件里的示例」（边界语义保留）。
   - **B（否决）**：为躲正则改写 #4/#8 的核验措辞（如「书里的情节」改「作品情节」）——B.2 明令不为躲正则改写固定说法，且改写会弱化「被核资料」的指涉精度。
   - 停下请作者裁决：无。

4. **反例与修复**
   - 推翻判断的情况：若 #4 命中出现在非核验语境（如 §1 经验借材节讲研究过程用书）则需改写——精读确认两处分别在 RS-06/RS-09 条目内，语境成立。
   - 修复后复查：改后复扫 #3/#4 零新增；三落点文件 #9 与「未证实」附加扫零命中。

5. **成品落点**
   - `.../references/research-and-verification.md` §4.1 第 1 句（改写）
   - 判定登记：`notes/quality/fiction-planning-and-diagnosis/s06c-desourcing-selfcheck.md` 第二、三节
   - **来源**：S06a1/S06a3 移交节；`notes/suite-contract.md` 第四节 B.2 第 5 条；v1 同文件。

## 不适用（简单而无分支，按附录 G.1 写一句）

- **reader 谱系八条与 research 谱系对齐条**：不适用。逐块比对均「改号/改写在位」，无两可分支，承接落点逐条见 LI-FP-201–208、211、213、215–217、219–225。
- **`SKILL.md`、`agents/openai.yaml`、reader-feedback、research-and-feedback-cases**：不适用。本片对这四个文件零改动（SKILL.md/yaml 属 a1 合同类；reader-feedback 与示例文件改写后全部命中判允许，LI-FP-232）。
- **SOURCE_ONLY 三件（reader 05-source-index、research source-index/source-boundaries）**：不适用。红线明令不恢复，无分支；通用语义落点逐句核实（LI-FP-208/223/225）。
- **GQ5 真实任务**：不适用。D3-C 授权范围为静态交付；静态通过不写成效果已证明。

# S06b 决策链（R17 §4a）· v0 fiction-craft-and-language 全谱系（成稿自检线）

- 分片：S06b｜代理：Agent 4（S06b 段子代理）｜轮次：W3 主体轮第 6 批｜日期：2026-11-05
- 逐条决定与九列记账见 `notes/loss-inventory/fiction-planning-and-diagnosis-S06b.md`（LI-FP-151–198，48 条：恢复 1、合并 2、不恢复 45）；附录 B 扫描结果见 `notes/quality/fiction-planning-and-diagnosis/s06b-desourcing-selfcheck.md`。
- 追加说明：本节为并行轮追加（追加前重读文件尾确认 S06c 节在 409–500 行，无重叠冲突；S06c 用 LI-FP-201 起段，本片用 LI-FP-151–198 段，编号无冲突）。

## 四、决策链

### D1 v1 缺席、v2 重组的自检谱系怎么定性（覆盖 LI-FP-151–162、177–190）

1. **情境**
   - 已知：v0 `fiction-craft-and-language` 9 文件 72650 B；r2 表 66 个单元（SKILL.md 17、worked-example 2、CL-01–14、references 细则 22、source-index 4）；v1 `d2003e4` 无任何 self-check 类文件，全谱系缺席；v2 以 `self-check-*` 六文件＋`examples/self-check-cases.md` 重组回归；v3 基线与 v2 的 self-check 文件差异经逐行 diff 核对全部为去来源泛化、skill 名更新与增强。
   - 推断：v0→v1 的融合稿有意不收这组「成稿自检」内容（与 fiction-craft 主线定位重叠），v2 按测试编号（CL-01–14）重建并下沉细则——v2 的重组就是该谱系的「去来源有意改写轮」，等价于 a 段的 v1 融合稿。
   - 用户要求：按 r2 内容对齐判定，缩减幅度是盘点信号不是应补回的量；「1884 年的出版建议」指名残留必须清除并复扫。

2. **区分信号**
   - 走「不恢复（对齐在位）」的信号：v0 每个单元的做法／信号／不适用／检查块能在 v3 的「卡片＋细则」两层结构里逐块找到；v2/v3 差异均为泛化（人名、书例、年代、来源自述）或增强（补边界、补出口、扩症状表）。
   - 反信号（走「恢复」）：v3 有悬空引用或成块功能缺失——实测一处：定位卡五字段（v0 SKILL.md §6）全包无定义，而 self-check-diagnosis:27 与 self-check-character:25 两处引用「定位卡」。
   - 判错的代价：把泛化当丢失会成批补回来源语境；把悬空引用当合规会让作者查不到「定位卡」是什么（计划 6.6 F-1 指名项继续缺）。

3. **两条分支的做法**
   - **A（采用）**：66 单元逐块比对，45 条记「不恢复（细则在位）」并写明逐块落点；定位卡五字段按 v0 §6 原文＋计划 F-1 五项恢复进 self-check-contract.md §2.1（五项各一行表格＋两条纪律＋交叉引用），不动 SKILL.md（禁改）；r2 的 `CL-05 SHRUNK`／`CL-06 BLOCK_LOST` 精读闭环为信号误报（卡片压缩＋「做法：」标签改写，细则三节逐块在位），LI-FP-167/168 写明比对过程防后续误补。
   - **B**：把 v0 卡片全文塞回 SKILL.md §5 或新建定位卡模板文件。判为不采用：SKILL.md 属 a1 已修禁改文件；细则下沉是 v2 有意设计，回塞即回退后版结构；定位卡五字段不足以构成一张模板（无枚举编号），按 a3「不新建文件」口径并入既有落点。
   - 停下请作者裁决：无——F-1 五项字段计划已写死，恢复内容与之一致。

4. **反例与修复**
   - 推翻判断的情况：r2 `—` 行若在逐块比对中发现缺块则升级为恢复——实测仅 CL-01 的「每章回看」「删掉人物后论证仍成立」两句在 self-check-contract §2 无对应，向下追查发现在 self-check-diagnosis §1 行 1 与 CL-02「删掉后故事不变」检查有等价承接，维持不恢复并写明去向。
   - 修复后复查：66 单元覆盖核对（SKILL 17＋worked-example 2＋CL 14＋细则 22＋来源类 4＝66，另登记 r2 未列的例三）；self-check-diagnosis/language/scenes/self-check-cases 与 v3 基线 diff 为空（本片未越界）。

5. **成品落点**
   - `.../references/self-check-contract.md` §2.1（恢复定位卡）
   - 其余为既有落点核对登记（LI-FP-151–162、177–190 各行）
   - **来源**：v0 `d23c461:skills/fiction-craft-and-language/SKILL.md` §1–§10 及 references×4、examples/worked-example.md；v1/v2/v3 树（`git ls-tree`）；计划 6.6 F-1；r2 表各行的 bytes/flag 信号。

### D2 「1884 年的出版建议」（:32）与卡夫卡例两处残留怎么清

1. **情境**
   - 已知：self-check-modern-and-zh.md:32 是 §3.1 与计划 2.5 节指名的全包 #3 最后一个命中；其上游指涉（来源书的投稿建议三件套）在 v3 self-check-contract §4.1 已被整体替换为「不预测销量＋转专业流程」；self-check-character.md:141「卡夫卡的格里高尔」为 v0 自带现代例句，v2/v3 历次清扫未触及（#5b 正则只查拉丁字母人名）。
   - 推断：:32 的「1884 年的出版建议」是指向学习材料的悬空指涉（建议本体已删），属「删除来源后语义不通」的 B.3 类残留；卡夫卡例属「作者人名＋具体作品标志性元素」（B.3：没有书名也算违规）。
   - 用户要求：逐条记决定并复扫确认 #3 全包清零。

2. **区分信号**
   - :32 走「改写为边界声明」的信号：该行功能是回答「投稿、出版、平台签约」场景下本 skill 做什么——不预测市场、手艺项与市场项分开；两点在 §4.1 有现成落点，接通即可，无需保留年代。
   - 反信号（保留年代、改写为「特定时期出版条件类主张不当作规则」）：会留下无指涉对象的时代悬语，且与 §4.1 已有表述重复——判不采用。
   - 卡夫卡例的替换须同时满足：保留教学点（字面不可能＋心理可理解）、骨架与来源案例零项对应、不引入新的具体作品元素。
   - 判错的代价：只删年代会留下「出版建议一律不采用」的无主语禁令（读者不知道哪来的建议）；换成「变成虫」类例子会带上另一个标志性元素，违规原样重演。

3. **两条分支的做法**
   - **A（采用）**：:32 改「手艺项与市场项分开处理（`self-check-contract.md` §4.1）；本 skill 不预测市场」；卡夫卡例改自创例「一位能听见旧物件说话的叙述者，字面上不可能，但他面对老屋要被拆掉的反应可以理解（这是本 skill 加的自创例）」。逐条记 LI-FP-187/195。
   - **B**：整行删除或整句删例。判为不采用：行与例的功能（市场边界、双审教学）是 v0 就有的内容，删除等于丢功能。
   - 停下请作者裁决：无——红线与 B.3 已明确。

4. **反例与修复**
   - 推翻判断的情况：替换例若与 self-check-cases 的海边卖房演示形成骨架重合会混淆示范——核对后确认人物关系（叙述者对物件 vs 姐妹对房产）、关键事件（听见物件说话 vs 卖房抉择）、时代地点三项均不对应，保留。
   - 修复后复查：#3 全包复扫零命中（LI-FP-198）；#5b 与书名号复扫零命中；「自创例」措辞沿用合同 2.2 对 DESIGN_EXAMPLE 的成品写法（注明自创例）。

5. **成品落点**
   - `.../references/self-check-modern-and-zh.md` §2 行 32
   - `.../references/self-check-character.md` §5 例句
   - **来源**：v0 `fiction-craft-and-language/references/modern-and-zh.md` §2 投稿行、`character-and-experience.md` §5 例句；slice-prep §3.1；计划 2.5 节；a1/a3 移交节。

### D3 source-index（SOURCE_ONLY）四节与 v0 §8「不作为规则的历史主张」怎么处置

1. **情境**
   - 已知：v0 source-index 4 节全部 `SOURCE_ONLY;UNALIGNED?`（两本书台账、测试与来源对照、不作为规则的历史主张、引用注意事项），v1 起整文件不存在；v0 SKILL.md §8 的八条历史主张清单与分歧裁决同源。
   - 用户要求：SOURCE_ONLY（本谱系 source-index）不直接恢复。

2. **区分信号**
   - 走「不恢复」的信号：四节主体是 PG 编号、行号、SHA、英文原句、引用规程——红线禁项；「不作为规则的历史主张」的可保留部分（否定式规范）已在 v3 各 self-check 文件与 diagnosis §5 误用表逐条在位（LI-FP-160 逐条列落点）。
   - 反信号核对：「投稿前先写梗概」一条可通用，但其保守语义（手艺／市场两分、不预测销量）已被 self-check-contract §4.1 覆盖，单独恢复只增重复；「小说应以爱情为主」无通用操作内容，按 P1 第三类排除。
   - 判错的代价：恢复任何一节都会带回编号、原句与年代，P4 必挂；漏核可保留语义会丢「不预测市场」的边界——已逐句核实。

3. **两条分支的做法**
   - **A（采用）**：四节不恢复、不建新文件；八条主张的否定式规范落点逐条写进 LI-FP-160；谱系去重语义确认在 RS-05（S06c 落点）在位。逐条记 LI-FP-191–194。
   - **B**：把「不作为规则的历史主张」改写成通用反模式清单补进 scope §4.4。判为不必要：八条中七条的否定式规范已在成品，第八条（爱情为主）是来源材料专属描述；scope §4.4 属 a3 已结片，本片不越界。
   - 停下请作者裁决：第八条是否需要否定式规范，列移交项由 Agent 1 裁处（见 LI 记录移交项 3）。

4. **反例与修复**
   - 推翻判断的情况：若 W4 隔离回读认为「方言必然缩小读者」「好稿必被接受」类主张需要成文禁令——现行成品已有等价句（self-check-language §4、self-check-contract §4.1），无需新增。
   - 修复后复查：全包无 `source-index` 字样引用残留（附加扫零命中）。

5. **成品落点**
   - 无新增落点（判定与落点对应关系记 LI-FP-160、191–194）
   - **来源**：v0 `d23c461:skills/fiction-craft-and-language/references/source-index.md`；计划 2.8 节、P1 三类排除口径。

### 不适用（简单而无分支，按附录 G.1 写一句）

- **`examples/self-check-cases.md`**：不适用。与 v0 worked-example 同一 blob、原样保留；三例为 v0 编者所写演示，B.3 骨架比对通过，无残留。
- **试读问法**：不适用。v0 SKILL.md §7 的试读三问功能已由 `reader-feedback.md` RF-11（S06c 落点）承接，本片不重复落笔（LI-FP-159）。
- **a1/a2/a3 已修文件与 S06c 落点**：不适用。SKILL.md、四个 rules-*、diagnosis／drafting／planning／revision／rule-examples／scope／templates 与 reader-feedback／research-and-verification 本片一律未动；a 段移交的命中归属三项复核登记（LI-FP-196）。
- **agents/openai.yaml**：不适用。无 CL 相关内容，无两可分支。
- **GQ5 真实任务**：不适用。D3-C 授权范围为静态交付；静态通过不写成效果已证明。
