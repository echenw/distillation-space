# 分片丢失清单与逐条决定 · genre-fiction-craft（G06-a4 · 历史架空 两谱系合片 93047 B）

- 片名：**G06-a4**（重派席：上一实例报 ERROR、盘上零落盘，本件为整范围重做）｜代理：W3 主体轮第 15 批 G06-a4 子代理｜轮次：**W3 主体轮第 15 批**｜日期：2026-11-05
- 范围：**谱系一 `historical-fiction-plot-forge` 14 文件＝60392 B**（主语义域：情节锻造，六域＝忠诚信物／谶语歌谣／心理困局／文书司法／地形信号／血亲婚约，另附反例集、死法诊断、六域正例、来源合同）＋**谱系二 `historical-immersion-and-stakes` 13 文件＝32655 B**（主语义域：临场感与赌注，H01–H17 十五条条件规则、拒绝边界、三层权限、因果核验表与三个静态自检例）。两片合计 **27 文件＝93047 B**。
- **编号段**：**LI-GE-1271 至 LI-GE-1320**（50 号可用）；本片实得决定 **46 条**：**谱系一占 LI-GE-1271–1307（37 条）**，**谱系二占 LI-GE-1308–1316（9 条）**；**LI-GE-1317 至 1320 为未用余量，非空号遗漏**（简报第 9 节体量纪律按 30–55 条，一个概念一行，不为凑数拆号）。
- 依据：计划附录 A.1／A.2／A.3、§2.3–§2.8／§5.1／§6.1／第 6 节 P3／附录 B／附录 C／附录 F／附录 G.1；`notes/slice-prep-2026-11-04.md` 第 39 行（题材 06 用默认阈值 **30% 或 >1.5 KB**）、第 110 行（`UNALIGNED?` 是待精读信号不是丢失清单）、第 169 行（来源类「不可拆」不等于「应恢复」）；计划 2.8 节题材 06 行（v1 103k→v2 104k→v3 81k，删 `source-cases.md` 32.6 KB，relationships-and-belief −4.5／institutions-and-documents −3.6／livelihood-and-action −3.4／history-contract −2.4／narration-and-period −2.0 KB）；`notes/source-synthesis/line-editing-and-proofreading.md` 第二节写法口径；格式范例 `genre-fiction-craft-G05-a4.md`；`genre-fiction-craft-G04-a1.md` D1「先读盘上实况再决定」。

## 一、开工前盘上实况自判（简报第 7 节三条；结论：基线不是 v3 原态，简报该条与盘上不符）

1. **逐文件 `wc -c` 对 `git show 2a10c07:skills/genre-fiction-craft/references/06-historical-alternate/<f>` 等长比对**（实测 2026-11-05 14:05）：`examples.md` 13654＝13654｜`guide.md` 5915＝5915｜`historical-fiction-patterns.md` 25836＝25836｜**`history-contract.md` 9452 vs v3 4802**｜**`institutions-and-documents.md` 7811 vs 4823**｜**`livelihood-and-action.md` 8528 vs 5558**｜**`narration-and-period.md` 7715 vs 4811**｜**`relationships-and-belief.md` 5540 vs 4679**｜**`settlement-and-revision.md` 4574 vs 3125**｜**`templates.md` 11236 vs 10472**。盘上十件合计 **100261 B**，v3 合计 83675 B，**净增 16586 B**。
2. **实证：同批三席的补丁已经落盘。** 把 `genre-fiction-craft-G06-a1/a2/a3.md` 里 `- 新文：` 行的前 36 字节逐个 `/usr/bin/grep -rqF` 回查 06 目录，实测 **a1 14/14、a2 17/17、a3 24/24 全部命中盘上现文**；`diff` 复核 `history-contract.md`、`settlement-and-revision.md` 亦可见三席句子按各自行末串接。简报「它们的补丁尚未写入 `output/`」「06 目录仍是 v3 原态（mtime 03:59:01）」与盘上实况不一致，本片按盘上态处理。
3. **对本片的两条后果**：① **定位锚全部从当前盘上文件重取**，未从提交内容抄锚；30 个锚逐条 `/usr/bin/grep -Fc` 实测＝1（见 selfcheck 第一节）。② **去重面扩大到三席成品**：本片不再写三席已写的语义（已放宽的铁律、已落的八问自问句、已落的 HI-61 先小后大句等），并按简报第 6 节在受影响行标 `可能同点`（本片两处真实同点：`livelihood-and-action.md` HI-44 与 `institutions-and-documents.md` HI-25，两处均改为串在已落文本之后）。
4. **mtime 异常登记（只登记不猜成因）**：`history-contract.md`／`institutions-and-documents.md`／`livelihood-and-action.md`／`narration-and-period.md`／`relationships-and-belief.md`／`templates.md` 六件 mtime ＝ **2026-11-05 14:01**；`settlement-and-revision.md` mtime＝03:59 但内容已含 a1 P12/P13、a2 P12、a3 P24 四段串接文本，与 14:01 组不同步；`examples.md`／`guide.md`／`historical-fiction-patterns.md`＝03:59 且与 v3 等长。本片自检时点系统时间 **2026-11-05 14:22**。
5. **操作纪律**：写盘仅本片白名单两份记录；未写 `output/`、`notes/source-synthesis/`、`checklist.md`、`log.md`、`notes/desourcing-ledger.md`、`notes/lineage-map.md`、任何 `SKILL.md`、任何 `agents/openai.yaml`、`docs/plans/`、`skills/`；未跑测试／lint／构建；未 `git checkout／switch／reset／clean／stash／add／commit／push`；未对仓库内任何文件用重定向或 `-i` 改写。
6. **并发写入复核登记（实测 2026-11-05 14:26–14:39）**：本片交回后 06 目录再次变动——`history-contract.md` 9452→**10485**、`institutions-and-documents.md` 7811→**11222**、`livelihood-and-action.md` 8528→**10967**、`narration-and-period.md` 7715→**8027**、`settlement-and-revision.md` 4574→**4889**（mtime 全部＝14:25；`relationships-and-belief.md`、`templates.md` 仍 14:01），同轮 `11-identity-revenge-intrigue/` 六件 mtime 亦＝14:25，属主代理串行落笔的第二波，本片不判归属。**本片 30 个锚在该状态下逐个 `/usr/bin/grep -Fc` 复测仍全部＝1**（复测清单见 selfcheck 第一节 3 项），且本片 30 条新文**均不在盘上**（P01 首句、P30 首句 `grep -c` 实测＝0）；本片恢复语义的关键字（守恒、成链、无词之拒、托管人、断喝、职业语言、解封、台阶、圣物）在 06 目录**除 `institutions-and-documents.md` 一处「四格」（a3 P13 动机四格）外零命中**，无同点撞车。**本片全部锚与落点按 14:26 盘上态仍然可执行；若主代理在落笔本片前先重铺基线，请按 selfcheck 存疑项 2 重新核对 P04、P08 两处的串接先后。**

## 二、r2 单元覆盖（自数；简报数字不作数）

- 输入：`notes/loss-inventory/raw/genre-fiction-craft-2026-11-04-r2.md` 题材 06 段＝第 2491–2969 行；段内 `^| ` 数据行实测 **444 行**（第 2523–2966 行；2967–2969 为非表行），与第 2518 行「规则单元数 444；v3 对齐成功 0；UNALIGNED? 444」一致；段内 `SOURCE_ONLY` 标记行实测 **55 行**，与第 2519 行一致。
- **本片行段（实测）**：**第 2797–2866 行＝70 行**（`historical-fiction-plot-forge`，具名 66＋裸编号 4：`RE-22`、`B02`、`PG324`、`PG271`；其中 `SOURCE_ONLY` 9 行）**＋第 2936–2966 行＝31 行**（`historical-immersion-and-stakes`，具名 28＋裸编号 3：`PG840`、`PG864`、`PG388`；`SOURCE_ONLY` 4 行）＝**101 个 r2 行**。
- **同段内他谱系的边界行号（不越界不遗漏）**：第 2712 行为 `historical-contract-and-legitimacy-craft` 末行（G06-a3 自述）；**第 2713–2796 行＝84 行属 `historical-fiction-craft-b03`**；**第 2867–2935 行＝69 行属 `historical-fiction-power-machine`**；第 2966 行后本段无数据行。b03 与 power-machine 两段**不在本片两谱系文件清单内，且本批 a1／a2／a3 三份记录均未认领**（a1 取 2523–2608、a2 取 2531–2551 与 2609–2631、a3 取 2632–2712），合计 **153 行无席**——已登记 selfcheck 移交项与回传存疑项，本片不越界议案。
- **一行不漏的核对方法（双向）**：① 正向：取两段行按行内文件前缀分桶到 14＋13 个 v0 文件，与 `git ls-tree -r -l d23c461` 的本片文件清单（60392＋32655＝93047 B）双向对号，14／13 件全部有行或有补判登记；② 反向：逐件回读 v0 原文的小节标题与编号，对 r2 未单列单元做**补判**——谱系一补 3（`SKILL.md` frontmatter、P4 顶部「先分清＋例」、同段「交付」）＝**73 单元**；谱系二补 10（`SKILL.md` frontmatter、顶部定位声明、`references/06-source-index.md` 2、`examples/` 三件各 1、`templates/historical-causality.md` 3）＝**41 单元**；两片 **114 单元**。裸编号行逐个回置：`RE-22`→`anti-examples.md` 附节（v1 起为「时代语境」条款）、`B02`→`references/source-contract-and-decisions.md` 批次标记（0 B）、`PG324`／`PG271`／`PG840`／`PG864`／`PG388`→各自 `source*` 索引表行。
- **r2 两处失真修正登记**：① `historical-immersion-and-stakes` 的 3 个 `examples/` 文件、`references/06-source-index.md`、`templates/historical-causality.md` 在 r2 **整件无行**（不是零字节），本片按 v0 原文补判；② `sources.md` 的 15 个 PGID 表行与 4 条审计要点在 r2 只以 `PG324`／`PG271` 两行代表，本片判整件 SOURCE_ONLY 不恢复，不逐本计数。

## 三、定性次序与口径

- 次序：**先核 v1（`d2003e4` 中文名 `06-历史架空/` 十件）→ 再核 v2（`3c1cb5f` 英文目录十件，含 `source-cases.md`）→ v2→v3 视为去来源轮**。实测证据：v1 已把六个 v0 谱系融合重写为 H01–H88＋T01–T12＋案例库；v2 改英文目录、H→HI 改号并删 `source-cases.md`；v3 相对 v2 的动作是六个执行文件各删 2.0–4.5 KB 的 `**交付与依据**：` 行，**`**怎么做**：` 行逐字不变**（本片对 `livelihood-and-action.md` 做 v2／v3 逐行比对：HI-31–HI-48 十八条 `怎么做` 行完全相同，消失的只有 `交付与依据` 行）。故 v2 那些行里**不带专名的通用限制句、检查项与反例**属「删来源时连带删掉的规则本体」，按找回处理；含人名、地名、章序与 PG 行位的只作语义线索。
- **后版有意调整判据（不回退）**：v1 已带反制句的一律判调整——「不以缺信物或没有痛苦代价判忠诚无效」「物件不必三次易手」「无四制度／三个底层视角／全员受伤配额」「没有三回合上限」「不强制一次高光配一次失败」「不存在固定注释数或前言≤5%」「无『指挥官离开必崩溃』铁律」「不要求每卷都设悬崖」「情感诗句可安抚而不必证明身份」「无需一次小验再一次大验」「HI-T08 以人物经历替代主角悲剧／对手可治／配角一场的旧分级」「不默认女性永远等待营救」。凡 v0 的绝对铁律、固定次数、固定分级、固定词数，除改写成条件句外**一律不恢复**。
- **红线禁项**：制毒与慢毒发作时间表、仿钥与开锁工序、伪造与规避追查的工艺、现实医疗与法证与遗传结论——不恢复成品；v0 自身与 v2 均限定「只迁移叙事链」，该限定已在 `livelihood-and-action.md` HI-47 末句、`historical-fiction-patterns.md` HI-C34 边界、`templates.md` HI-T06 末句在位，判**已在位**（见 LI-GE-1296）。
- **口径遵守**：`MISSING ≠ 丢失`（本片 101 行全为 `UNALIGNED?` 信号，0 条按 MISSING 处理）；`覆盖率 ≠ 内容保留率`（题材 06 v3÷v0≈20% 只说明融合重组）；`raw 表是信号不是结论`（每条恢复都有 v0／v2 原文回读＋盘上 `/usr/bin/grep` 实测）；`SOURCE_ONLY`（r2 标记行 13：谱系一 9＝`historical-provenance.md` 2＋批次标记 1＋`source-contract-and-decisions.md` 4＋`sources.md` 代表行 2；谱系二 4＝`source-index.md` 具名 1＋裸 PG 3；再加按来源性质归类的 `examples.md` 7 行、`SKILL.md` 来源与审计 1 行、`06-source-index.md` 2 补判、A07-H16／H17 2 条，合计 **25 单元**）**不恢复、不建新文件**，逐轴通用语义承接写在各行理由列；**不新增编号**（30 条恢复／合并全部并入既有 HI-11／21／22／25／34／37／39／44／48／50／51／52／53／54／56／57／58／60／63／68／84／85／86／90 与 HI-C13／C22／C34／C35／C43／C46，不造 HI-91、不造 HI-C49、不恢复 F／R／C／M／H／A07 旧编号）。

## 逐条决定（九列）

| 片 | 编号 | 来源位置 | 丢失类型 | v3 现状 | 决定 | 理由 | 成品落点 | 状态 |
|---|---|---|---|---|---|---|---|---|
| G06-a4 | LI-GE-1271 | v0 `plot-forge/SKILL.md` frontmatter、P4 段「交付」清单、主决策表＋`agents/openai.yaml`（r2 2797 前置未列＋2799＋2804；4 单元） | 模板字段（触发／路由／输出合同）＋整个文件 | 无 | 移交 | 题材 `SKILL.md` 路由与 `agents/openai.yaml` 按简报第 4／6 节不议案；P4 段输出合同九项 Owner 在 fiction-planning（附录 C.1） | 无（移交 G00／W4 与 Agent 4） | 已回读 |
| G06-a4 | LI-GE-1272 | v0 `SKILL.md` P4 顶部「先分清真实历史与架空罗曼司＋例」、返工后的优先证据与叙事分流、六域导航（r2 2797＋2800＋补判 1；3 单元） | 规则小块（三分栏与文件结构） | 改写后在位 | 不恢复 | 可查事实／作者虚构／人物信念三分已在 `history-contract.md` HI-02、HI-08、HI-61、HI-65 与 `templates.md` HI-T01；「架空只检世界内一致性」在 HI-01 末句与 HI-16；六域语义分落 HI-21／61／56／C13／34／50，不复建平行文件结构 | 无 | 已回读 |
| G06-a4 | LI-GE-1273 | v0 `SKILL.md`＋使用须知先读（r2 2798）＋`anti-examples.md`＋附：时代语料红线（裸 `RE-22`，r2 2810；2 单元） | 规则小块（立场重铸两动作） | 部分在位 | 合并（P05） | 编号语义与 PGID 等级属来源侧；HI-75／HI-C30 只有判定侧，缺「让得利者自己把道理讲圆、给被压迫者一个能行动的位置」两条动作，落 `livelihood-and-action.md` HI-48。拍卖标记制、殖民官僚学等包装不搬 | `livelihood-and-action.md` HI-48 | 未处理（补丁 P05 待主代理写入） |
| G06-a4 | LI-GE-1274 | v0 `SKILL.md`＋三条铁律、失败出口（r2 2801–2802）＋`failure-modes.md`＋自检顺序、与三条铁律的对应（r2 2823、2831；4 单元） | 规则（绝对表述与诊断权重次序） | 已放宽 | 不恢复 | v1 起逐条改条件句（HI-21 不以缺信物判无效、HI-61 无必误读通则、HI-41 物件不必三次易手、HI-C22 不强制一种解释、HI-C14 不强迫以牺牲保持清白）；「代价＞凭证＞误读＞收束」权重属铁律体制；症状入口已由 HI-87 八问（a1 P13 已落盘）承担，本片不再向该行追加 | 无 | 已回读 |
| G06-a4 | LI-GE-1275 | v0 `SKILL.md`＋来源与审计（r2 2803）＋`examples.md` 六域正例与反例警示（r2 2816–2822；8 单元） | 例子／来源计量 | 无 | 不恢复（SOURCE_ONLY） | 15 源索引、token 账目、GQ 状态与六域正例的 PG 行位与人名按 2.8 节不恢复；通用承接＝guide「依据分五种」＋HI-88＋HI-C32；六域正例的机制已分落 HI-21／63／57／C13／34／50 | 无 | 已回读 |
| G06-a4 | LI-GE-1276 | v0 `anti-examples.md`＋1 机械应验谶语（r2 2805）＋`prophecy-song.md`＋1 谶语即提纲（r2 2848；2 单元） | 反例＋检查项＋规则小块 | 部分在位 | 合并（P24） | 「每个分句能否改写出两种以上应验读法」与「反抗即应验路径要逐点咬合」补到 `historical-fiction-patterns.md` HI-C22；红衣坠马、雨中应验等场景不搬 | `historical-fiction-patterns.md` HI-C22 | 未处理（补丁 P24 待主代理写入） |
| G06-a4 | LI-GE-1277 | v0 `anti-examples.md`＋2 无价忠诚（r2 2806）＋`oath-token.md`＋1 忠诚票据化（r2 2843；2 单元） | 反例＋规则小块（凭证三态／测试机关） | 部分在位 | 合并（P06） | 出示／内容／行为三态与「先诱他违令、另一处领赏，两头都报即破」落 `institutions-and-documents.md` HI-21；票据双向性在 HI-41／HI-C09 在位；记忆遗族侧改落 HI-53（P12） | `institutions-and-documents.md` HI-21 | 未处理（补丁 P06 待主代理写入） |
| G06-a4 | LI-GE-1278 | v0 `anti-examples.md`＋3 裸告白求婚（r2 2807）＋`kinship-love.md`＋1 求婚力学四式（r2 2832；2 单元） | 反例＋规则小块 | 部分在位 | 合并（P09） | 四式改写成可组合姿态并补无词之拒、沉默不等于同意，落 `relationships-and-belief.md` HI-50；跨门第宣言的固定时序不搬（v2 已写「不要求跨阶爱情终须贵族证明」） | `relationships-and-belief.md` HI-50 | 未处理（补丁 P09 待主代理写入） |
| G06-a4 | LI-GE-1279 | v0 `anti-examples.md`＋4 掉书袋判词（r2 2808；1 单元） | 反例＋检查项 | 部分在位 | 合并（P28） | 「删掉判词后半句是否更有力」与「撑场面的数字要被内行戳破一次」补到 HI-C46；固定 12 词阈值不搬（HI-C46 已写不设固定词数） | `historical-fiction-patterns.md` HI-C46 | 未处理（补丁 P28 待主代理写入） |
| G06-a4 | LI-GE-1280 | v0 `anti-examples.md`＋5 无规-map 逃亡（r2 2809）＋`terrain-signal.md`＋1 地形规则引擎（r2 2862；2 单元） | 规则小块（成链与守恒两条动作） | 部分在位 | 合并（P01＋P02） | ①「脱险须消耗先前展示过的资源或规则、不可连续靠运气」与「被认为神圣不可犯不等于物理进不去」落 `livelihood-and-action.md` HI-34（P01）；②地形规则引擎里的限载渡运与军算侧，把 v2 HI-37 `交付与依据` 被整行删除的守恒核对与交接断档落 HI-37（P02）；双出口与指挥官离场必崩溃两条判后版已放宽（HI-C10 边界、HI-37 现有句） | `livelihood-and-action.md` HI-34、HI-37 | 未处理（补丁 P01、P02 待主代理写入） |
| G06-a4 | LI-GE-1281 | v0 `document-plot.md`＋1 构陷的文书链（r2 2811；1 单元） | 规则小块（成链／诱供细节／保管人） | 部分在位 | 合并（P30） | HI-C13 现有只讲档案层级，缺「成链才像机器」「伪信细节须有窥得来源」「谜面保管人要先立一景」；翻册破局与告解封印分别在 HI-C13 边界与 P07 承接 | `historical-fiction-patterns.md` HI-C13 | 未处理（补丁 P30 待主代理写入） |
| G06-a4 | LI-GE-1282 | v0 `document-plot.md`＋2 真相的释放与判词（r2 2812；1 单元） | 规则小块（记忆合法性自审） | 无 | 合并（P29） | 回忆中段被在场者审问、以缴械换继续讲述的许可，HI-11／HI-73／HI-C27 均无该动作；三段身世披露判在位（HI-42 与 HI-C12 已把线索与证明分两层）；最短判词在 HI-C46 在位 | `history-contract.md` HI-11 | 未处理（补丁 P29 待主代理写入） |
| G06-a4 | LI-GE-1283 | v0 `document-plot.md`＋3 史料接口（r2 2813；1 单元） | 规则小块（遗物逐件激活 exposition／告解封印） | 部分在位 | 合并（P13） | 家族史铺陈由遗物逐件激活、每件配一句持有者判词，落 `relationships-and-belief.md` HI-54；「双层说法」机制已在 HI-C21 在位；虚构优先自注与改编自注的次数限制已被 HI-07 放宽，判不回退；告解封印侧由 P07 承接 | `relationships-and-belief.md` HI-54 | 未处理（补丁 P13 待主代理写入） |
| G06-a4 | LI-GE-1284 | v0 `document-plot.md`＋4 文书的美学（r2 2814；1 单元）＋`prophecy-song.md`＋1 内 1-5 圣化即流放（v0 子条，r2 未单列，不另计单元） | 规则小块（分散遗嘱／祷文两解／圣化除名） | 部分在位 | 合并（P26） | HI-C35 只写「有不同证据地位」，缺三种可执行写法；产权各执一词并入 HI-54（P13）；配比数字的戳破检查并入 HI-C46（P28） | `historical-fiction-patterns.md` HI-C35 | 未处理（补丁 P26 待主代理写入） |
| G06-a4 | LI-GE-1285 | v0 `document-plot.md`／`madness-mind.md`／`oath-token.md`／`prophecy-song.md`／`terrain-signal.md` 五个「收束技法」节（r2 2815、2842、2847、2852、2866；5 单元） | 模板字段（五式与线别判准） | 改写后在位 | 不恢复 | 五式与前置条件已被 HI-83／HI-84／HI-86／HI-C31／HI-81 吸收；「换装线禁悬置、身世线禁悬置、逃亡线禁账目结清、妒杀线禁邀请新生直收」类硬禁令按 v3 口径只留「不伪称闭合」的条件句（P23 已写） | 无 | 已回读 |
| G06-a4 | LI-GE-1286 | v0 `failure-modes.md`＋五类常见死法（标题行＋死法一至五，r2 2824–2829；6 单元） | 规则小块（症状与修复指向） | 部分在位 | 合并（分承 P01／P06／P09／P24／P28，不另出补丁） | 六行与 `anti-examples.md` 五节同源，症状句已在各卡以条件句在位；本片只在对应补丁里补动作，本行不重复计补丁 | 见 LI-GE-1276／1277／1278／1279／1280 各行落点 | 已回读 |
| G06-a4 | LI-GE-1287 | v0 `failure-modes.md`＋快速诊断问答（r2 2830；1 单元） | 检查项（五问） | 部分在位 | 合并（P08） | 「反派为什么不动手→须有可点名的成本，否则是作者之手」落 `institutions-and-documents.md` HI-25；疯人／家史／换名／结局四问分别由 P14／P13／P27／P22 承接 | `institutions-and-documents.md` HI-25 | 未处理（补丁 P08 待主代理写入） |
| G06-a4 | LI-GE-1288 | v0 `kinship-love.md`＋2 保护性驱逐（r2 2833；1 单元） | 规则小块（解读误差作燃料） | 部分在位 | 合并（P10） | HI-51 只写「受方是否知情、能否拒绝」，缺被逐者误读与保护者的混合动机 | `relationships-and-belief.md` HI-51 | 未处理（补丁 P10 待主代理写入） |
| G06-a4 | LI-GE-1289 | v0 `kinship-love.md`＋2 内 2-3 交棒／2-4 拒绝的尊严清单（v0 子条，r2 未单列，不另计单元） | 规则小块（遗训与清单式告别） | 无 | 合并（P11） | HI-52 只有授权范围与退出方式，缺交棒须留实物与训示并在终章被遵守或违反、离开时清点该还与只取项 | `relationships-and-belief.md` HI-52 | 未处理（补丁 P11 待主代理写入） |
| G06-a4 | LI-GE-1290 | v0 `kinship-love.md`＋3 血亲妒杀线（r2 2834）＋`madness-mind.md`＋3 义举反噬律（r2 2840；2 单元） | 规则小块（逼迫台阶／当场被记录／旧谊杠杆） | 部分在位 | 合并（P15） | HI-57 只写「善举可能被利用」，缺当场被第三者记录估价、不在场者注视需具体旧谊、逼迫按台阶升级并在每两级间给一次未遂自救；暗线蓄力的可回溯检查由 HI-42／HI-C36 承担；双生镜像的价值相反要求判后版已放宽 | `relationships-and-belief.md` HI-57 | 未处理（补丁 P15 待主代理写入） |
| G06-a4 | LI-GE-1291 | v0 `kinship-love.md`＋4 动物与物作道德参照（r2 2835；1 单元） | 规则小块（非人叙述禁读人心／负荷／圣物之死） | 部分在位 | 合并（P16） | HI-58 只写认知界限，缺叙述禁令、负荷入账与被神化物件之死的转折功能；训马伦理作对照组属案例包装，写成一般类别即可 | `relationships-and-belief.md` HI-58 | 未处理（补丁 P16 待主代理写入） |
| G06-a4 | LI-GE-1292 | v0 `kinship-love.md`＋5 死亡收束的形式实验（r2 2836；1 单元） | 规则小块（形式闭环／赋格终句） | 部分在位 | 合并（P22） | 「收束可用形式完成而不必再死一个人」「形式闭环可与因果闭合分离」落 `settlement-and-revision.md` HI-86；俗意象只物理化一次并入 HI-69 侧判在位；以年为期完成死亡的身体机制按 HI-C45 边界不写 | `settlement-and-revision.md` HI-86 | 未处理（补丁 P22 待主代理写入） |
| G06-a4 | LI-GE-1293 | v0 `kinship-love.md`＋5 内 5-5 主仆泪权审计（v0 子条，r2 未单列，不另计单元） | 规则小块（哀悼资格与问责） | 无 | 合并（P21） | HI-85 只写谁要求记住与拒绝的权利，缺哭泣资格、旁人问责与问责后的回应方式 | `settlement-and-revision.md` HI-85 | 未处理（补丁 P21 待主代理写入） |
| G06-a4 | LI-GE-1294 | v0 `kinship-love.md`＋收束技法（r2 2837；1 单元） | 模板字段（拒述与一喝两读） | 部分在位 | 合并（P23） | 停在未兑现的实物、两读断喝与「不给正解不得自称闭合」落 HI-84；婚礼葬礼对切、物证传灯在 HI-C31／HI-86 在位 | `settlement-and-revision.md` HI-84 | 未处理（补丁 P23 待主代理写入） |
| G06-a4 | LI-GE-1295 | v0 `madness-mind.md`＋1 「疯」标签的叙事功能（r2 2838；1 单元） | 规则小块（筹码级／触发物） | 部分在位 | 合并（P14） | 三级功能（主角悲剧／对手可治／配角一场）判已被 v1 拒绝（HI-T08 以人物经历替代旧分级），不回退；保留病症作筹码后的长期偿付、触发物必须是读者已知事件两样可迁移项 | `relationships-and-belief.md` HI-56 | 未处理（补丁 P14 待主代理写入） |
| G06-a4 | LI-GE-1296 | v0 `madness-mind.md`＋2 毒杀线的证言、误导与取证（r2 2839；1 单元） | 规则小块（试毒人／调包／慢毒时间表） | 无 | 不恢复（红线禁项） | 移除试毒人、上游换药、发作时间表、毒物学列举均属现实危害工艺；该限定已在 HI-47 末句、HI-C34 边界、HI-T06 末句在位；装死戏的破功风险由 HI-C10 现有句与本片 P25 的物件链承担；「演说越雄辩判词越短」并入 HI-C46（P28） | 无 | 已回读 |
| G06-a4 | LI-GE-1297 | v0 `madness-mind.md`＋4 攻心与守心（r2 2841；1 单元） | 规则小块（守心者自认／解绑论留怀疑） | 部分在位 | 合并（P17） | HI-60 只写信念与行为的分层，缺规劝者的自我牵连与被教唆者保留一句怀疑；hare／hound 修辞不搬；弱者诡智的对称反驳已在 HI-57／HI-C30 在位；改宗时机律判后版已放宽（HI-C44） | `relationships-and-belief.md` HI-60 | 未处理（补丁 P17 待主代理写入） |
| G06-a4 | LI-GE-1298 | v0 `oath-token.md`＋2 换名与换装的分工（r2 2844；1 单元） | 规则小块（伪装行为清单） | 部分在位 | 合并（P03） | 长期伪装者的可执行行为规则与「换装不长新本事」落 `livelihood-and-action.md` HI-39；换名三律的贴身残存与可应答性落 HI-C43（P27）；真话欺骗悖论在 HI-C09／HI-40 在位 | `livelihood-and-action.md` HI-39 | 未处理（补丁 P03 待主代理写入） |
| G06-a4 | LI-GE-1299 | v0 `oath-token.md`＋2 内 2-1 换名三律／＋1 内 1-4 谱系武器战（v0 子条，r2 未单列，不另计单元） | 规则小块（新名来历／第二击叫停） | 无 | 合并（P27） | HI-59／HI-C20 只分层身份，不写换名来历与借手后的可核对身体细节；HI-C43 只写家史攻击的受众与伤害，缺第二击之前收住的时机 | `historical-fiction-patterns.md` HI-C43 | 未处理（补丁 P27 待主代理写入） |
| G06-a4 | LI-GE-1300 | v0 `oath-token.md`＋3 双重承诺的化解（r2 2845；1 单元） | 规则小块（解封规则／拒信任当众） | 部分在位 | 合并（P07） | HI-22 已放宽「物理机智不是每次都能两全」；本片只补保密义务不因死亡自动解除、解封动作要写成可核对规则；每卷悬崖戏判后版已放宽（HI-C43 边界） | `institutions-and-documents.md` HI-22 | 未处理（补丁 P07 待主代理写入） |
| G06-a4 | LI-GE-1301 | v0 `oath-token.md`＋4 信号工程四件套（r2 2846）＋`prophecy-song.md`＋3 预兆与物候（r2 2850；2 单元） | 规则小块（协议交代／物候配额／死亡窗口） | 在位 | 不恢复 | HI-38 与 HI-C10 已写编码、认证、噪声、误读、预备与合作、破功风险；HI-69 已写景物承担时间与情绪、a3 P17 已落旧物承担时间深度；死亡时刻窗口属本作死亡观，HI-C45／HI-85 已覆盖；每卷三次上限与心停自摇机制判配额与红线 | 无 | 已回读 |
| G06-a4 | LI-GE-1302 | v0 `prophecy-song.md`＋2 歌谣五职（r2 2849；1 单元） | 规则小块（引语来历／双功能铺垫） | 部分在位 | 合并（P18） | HI-63 已放宽「不硬凑三次」；本片补引语须在故事内有来处、一物双职先铺联结、文学疗法不当现实建议；诗句口令的旧断言判 v2 已改正 | `relationships-and-belief.md` HI-63 | 未处理（补丁 P18 待主代理写入） |
| G06-a4 | LI-GE-1303 | v0 `prophecy-song.md`＋4 禁忌与反用（r2 2851；1 单元） | 规则小块（禁忆律反用／改口私语） | 部分在位 | 合并（P12） | 虚构一条禁止记住或讲述的规矩并让它有后果，落 HI-53；不敢反祷的改口写法属案例细节，判并入 HI-C35（P26）侧不另出补丁；应验特写与物证收束在 HI-84／HI-C31 在位 | `relationships-and-belief.md` HI-53 | 未处理（补丁 P12 待主代理写入） |
| G06-a4 | LI-GE-1304 | v0 `references/historical-provenance.md`（r2 2853–2854）＋`references/source-contract-and-decisions.md`（r2 2855–2859，含裸 `B02`）＋`sources.md`（r2 2860–2861，裸 `PG324`／`PG271`；9 单元） | 整个文件／来源计量与返工判定过程 | 无 | 不恢复（SOURCE_ONLY） | 按 2.8 节来源类与旧元数据不恢复；A／B 案分派、单源登记、许可与替代关系属来源裁决侧。逐轴通用语义承接：真实与虚构先分档→HI-01／HI-02；人物信念不当史料→HI-61／HI-65；观察行为分层→HI-C16；文书只是机制不当史证→HI-C13；地形双方同约束→HI-34；经历层与世代层对照→HI-53／HI-C36；公共历史语言风险→HI-75／HI-C30；不可核时缩小主张→HI-12 末句与 HI-88；最小交付→HI-T12 与 guide「写可审阅成果」 | 无 | 已回读 |
| G06-a4 | LI-GE-1305 | v0 `terrain-signal.md`＋2 账房声部（r2 2863；1 单元） | 规则小块（职业隐喻贯穿决策） | 部分在位 | 合并（P04） | HI-37／HI-C37 已写军算分层与守恒；本片补「一种职业语言贯穿其全部台词并真的进入他的决定，算错处留后果」落 HI-44；非志愿兵账房侧在 HI-C37 在位；守备算术在 HI-C46 在位 | `livelihood-and-action.md` HI-44 | 未处理（补丁 P04 待主代理写入） |
| G06-a4 | LI-GE-1306 | v0 `terrain-signal.md`＋3 换锁与潜入工程（r2 2864；1 单元） | 规则小块（钥匙政治学／弃证代价） | 部分在位 | 合并（P20） | 备钥、做旧、异响遮掩等工序属现实侵入工艺不恢复；可迁移的两样是「门禁持有结构即权力结构，羞辱执行者反而让其收紧权限」落 HI-68、「弃证同时断掉自己凭据」落 HI-C34（P25）；工序伪装的小样赠好奇者写成一般类别后判在位（HI-C18 新增资源要写获取难度） | `narration-and-period.md` HI-68 | 未处理（补丁 P20 待主代理写入） |
| G06-a4 | LI-GE-1307 | v0 `terrain-signal.md`＋4 单景配角与行进群像（r2 2865；1 单元） | 规则小块（一景一职能／谐角不解救） | 部分在位 | 合并（P28） | HI-C46 已有相册小传与向导盲区，缺一次性配角闭环与谐角不得在关键处解围；马背地理学在 HI-37／HI-58 在位；迷路作时间纵深装置判 HI-C45／HI-C40 已覆盖 | `historical-fiction-patterns.md` HI-C46 | 未处理（补丁 P28 待主代理写入） |
| G06-a4 | LI-GE-1308 | v0 `immersion/SKILL.md` 任务路由、输入权威、可执行流程五步、冲突与失败出口、交付格式与顶部定位声明（r2 2936–2940＋补判 1；6 单元） | 规则小块（流程与出口） | 改写后在位 | 不恢复 | 五步流程与四类出口已被 `guide.md` 工作顺序七条、依据分五种、做不下去时表逐条承接；H 编号在成品里已改写成 HI 卡，旧编号不进成品；「不伪造引文、无正文不装已修改」在 guide 工作顺序第 1、7 条在位 | 无 | 已回读 |
| G06-a4 | LI-GE-1309 | v0 `SKILL.md`＋本批来源与许可边界（r2 2941）＋`references/source-index.md`（r2 2963–2966）＋`references/06-source-index.md`（2 补判；7 单元） | 整个文件／来源计量 | 无 | 不恢复（SOURCE_ONLY） | 17 本清单、SHA、行位与兼容入口按 2.8 节不恢复；承接＝HI-88、HI-C32、HI-10；「旧 FULL 声明已排除」属改动痕迹，不进成品 | 无 | 已回读 |
| G06-a4 | LI-GE-1310 | v0 `SKILL.md` frontmatter＋`agents/openai.yaml`（r2 2942＋补判 1；2 单元） | 整个文件／模板字段 | 无 | 移交 | 同 LI-GE-1271；display_name、short_description、default_prompt 只作线索 | 无（移交 G00／W4） | 已回读 |
| G06-a4 | LI-GE-1311 | v0 `references/01-time-institution-and-power.md` H01／H02／H04（r2 2943–2945；3 单元） | 规则小块（两轴对齐／授权者／姓名表） | 在位 | 不恢复 | HI-03 已写事件顺序、消息时差与两套承诺的分派（a1 P01、a3 P02 已在盘上），HI-14 已写执行者／授权者／时效／申诉处，HI-06 与 HI-T02 已写姓名、来源等级与告知方式；本片不再向 HI-03 追加第三句 | 无 | 已回读 |
| G06-a4 | LI-GE-1312 | v0 `references/01` H05（r2 2946；1 单元） | 规则小块（政治经私物与公职入家） | 无 | 合并（P19） | HI-90 只写权力进入日常安排，缺远方政局借一件私物或一个公职身份进门、谁听见、传到哪、并限定为说话人观点 | `narration-and-period.md` HI-90 | 未处理（补丁 P19 待主代理写入） |
| G06-a4 | LI-GE-1313 | v0 `references/02-space-objects-and-livelihood.md` H03（r2 2947；1 单元） | 规则小块（关键物件四格登记） | 无 | 合并（P25） | HI-C18／HI-C34 已写视线与保管链，但没有「原本状态→谁能看见→何时被用→谁付代价」的可填四格；纯氛围不强制机关先铺在 HI-C10／HI-69 在位 | `historical-fiction-patterns.md` HI-C34 | 未处理（补丁 P25 待主代理写入） |
| G06-a4 | LI-GE-1314 | v0 `references/02` H06／H07／H12＋`references/03` H08／H09／H11／H14＋`references/04` H10／H13／H15（r2 2948–2957；10 单元） | 规则小块（生计记录／证物登记／世仇分层／多层讲述／语域／后果清算） | 在位 | 不恢复 | 逐条对位：HI-31／HI-32、HI-41／HI-C18、HI-46／HI-69（景物不折算成本，P20 之外由 a3 P17 与 HI-69 现有句覆盖）、HI-49（家族主张→可执行权利→能否拒绝）、HI-42／HI-C12、HI-18（转手链）、HI-C16（意图／行为／证据／推断／评价五层）、HI-C27／HI-73、HI-70／HI-76（a1 P09、a2 P13、a3 数条已在盘上）、HI-81／HI-83／HI-84；判改写对齐后在位，重复追加会让同一卡叠三层同义句 | 无 | 已回读 |
| G06-a4 | LI-GE-1315 | v0 `references/05-antipatterns-and-boundaries.md` 旧模式拒绝边界＋三层权限＋修订回归五问＋A07-H16＋A07-H17（r2 2958–2962；5 单元） | 规则（拒绝清单／三层登记／回归问／批次归属） | 改写后在位 | 不恢复（含 SOURCE_ONLY 侧） | A01–A08 与 C1–C7 的拒绝项已被 v1 逐条编入各卡反制句；三层权限与 HI-02／HI-C21／guide 依据分五种重合；回归五问入口由 HI-87 八问（a1 P13）与 HI-T12 字段承担；F_literary／USER_CANON／F_historical 字母已中文化写出，状态字母不进成品；作品分组不改变题材属来源批次观察，按 2.8 节不恢复 | 无 | 已回读 |
| G06-a4 | LI-GE-1316 | v0 `examples/worked-example.md`＋`conflict-missing.md`＋`normal-design.md`（3 补判）＋`templates/historical-causality.md` 十字段与 A／B 分支（3 补判；6 单元） | 例子／模板字段 | 改写后在位 | 不恢复 | 三个例子的通用结果已在本题材 `examples.md` HI-X01–X06 全部在位（HI-X02 交换妻子与城镇、HI-X03 关系帮他到门口不帮他越权、HI-X04 互斥签署年份、HI-X06 无正文时的诊断路径）；A07-D01–D10 已被 HI-T01–HI-T12 拆分且逐格可填「未知／不适用＋原因」，分支与回归证据在 HI-T01 出口行、HI-T12 末列在位；DESIGN_EXAMPLE 属审计词不进成品 | 无 | 已回读 |

**单元覆盖求和式（谱系一 `historical-fiction-plot-forge`＝73）**：`SKILL.md` 10（具名 7＋补判 3）＋ `agents/openai.yaml` 1 ＋ `anti-examples.md` 6（具名 5＋裸 `RE-22`）＋ `document-plot.md` 5 ＋ `examples.md` 7 ＋ `failure-modes.md` 9 ＋ `kinship-love.md` 6 ＋ `madness-mind.md` 5 ＋ `oath-token.md` 5 ＋ `prophecy-song.md` 5 ＋ `references/historical-provenance.md` 2 ＋ `references/source-contract-and-decisions.md` 5 ＋ `sources.md` 2 ＋ `terrain-signal.md` 5 ＝ **73 单元**（＝实测 r2 70 行＋补判 3）。三个 v0 子条（`kinship-love.md` 2-3／2-4、5-5 与 `oath-token.md` 2-1、`prophecy-song.md` 1-5）在补丁 P11、P21、P27、P26 里单列为决定行，**标「不另计单元」以免与所在小节重复计账**；实得单元数不受影响。
**单元覆盖求和式（谱系二 `historical-immersion-and-stakes`＝41）**：`SKILL.md` 8（具名 6＋补判 2）＋ `agents/openai.yaml` 1 ＋ `references/01` 4 ＋ `references/02` 4 ＋ `references/03` 4 ＋ `references/04` 3 ＋ `references/05` 5 ＋ `references/source-index.md` 4 ＋ `references/06-source-index.md` 2 ＋ `examples/` 3 ＋ `templates/historical-causality.md` 3 ＝ **41 单元**（＝实测 r2 31 行＋补判 10）。
**两片合计 114 单元**；决定 **46 条**（谱系一 37＋谱系二 9）＝**合并 30 条**（逐条对应 P01–P30，其中 LI-GE-1280 一行支撑 P01 与 P02，P28 由 LI-GE-1279 与 LI-GE-1307 两行共同支撑，条数与补丁数仍各 30／30）＋**分承 1 条**（LI-GE-1286，不另出补丁）＋**不恢复 13 条**＋**移交 2 条**。

## 补丁清单（30 条＝P01–P30，供主代理统一落笔）

> 定位锚全部取自本轮 `Read`／`/usr/bin/grep -Fn` 读到的**当前盘上** `output/genre-fiction-craft/references/06-historical-alternate/` 原文（含同批三席已落笔的行末追加文本），逐字摘录，30 个锚在其落点文件内 `/usr/bin/grep -Fc` 实测命中均为 **1**（逐项实测值见 `notes/quality/genre-fiction-craft/g06a4-desourcing-selfcheck.md` 第一节）。本片落点行全部是散文行（HI 卡的 `**怎么做**：` 段、卡片正文段、patterns 的 `**怎么做：**`／`**边界：**` 段），一律用 `行内追加`；**零表格行改动**，故无 `精确替换（子串）`；不新增小节、不新增编号、不改任何小节标题，不动 `templates.md`／`guide.md`／`examples.md` 的表列。建议落笔顺序：`livelihood-and-action.md`（P01→P05）→`institutions-and-documents.md`（P06→P08）→`relationships-and-belief.md`（P09→P18）→`narration-and-period.md`（P19→P20）→`settlement-and-revision.md`（P23→P21→P22）→`historical-fiction-patterns.md`（P24→P25→P26→P27→P28→P30）→`history-contract.md`（P29）。

补丁 **P01**（LI-GE-1280）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/livelihood-and-action.md`
- 定位锚：`事后解释不能凭空增设通路。`（HI-34 追捕双方按同一时空规则行动，怎么做段末）
- 动作：行内追加
- 新文：`一处地方被众人认为神圣不可犯，不等于它物理上进不去；圣地只改变守卫会不会松懈、谁敢在那里动手，追逃双方用的仍是同一套地形。脱险要消耗先前展示过的资源或规则——潮窗、岔路、一把钥匙、一匹马的余力；连着几次靠天黑、起雾、追兵马失前蹄，读者会判定追兵在放水。`
对应记账：LI-GE-1280

补丁 **P02**（v2 连带删除；v0 侧归属见 LI-GE-1280 地形 §1）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/livelihood-and-action.md`
- 定位锚：`指挥者可以亲守要点，也可以有效授权。`（HI-37 运输与指挥靠容量、节奏和交接，段末）
- 动作：行内追加
- 新文：`运力要做守恒核对：每阶段装得下多少人马、耗掉多少牲畜、损失之后是延程、减载还是改任务，前后要接得上数；不能因为需要就临时多出一批船马。指挥者离场时写明哪条规则跟着停、停多久、谁趁这段时间动了手。`
对应记账：v2 `livelihood-and-action.md` HI-37 的 `**交付与依据**：` 行（8987→5558 去来源轮整行删除）中不带专名的通用半句；v0 侧见 LI-GE-1280、LI-GE-1305

补丁 **P03**（LI-GE-1298）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/livelihood-and-action.md`
- 定位锚：`不按时代预设唯一成本。`（HI-39 伪装成本由角色与社会规范决定，段末）
- 动作：行内追加
- 新文：`换上一身衣裳不会自动带来新本事，人物的能力仍要从他原本会做的事里来；长期顶一个新名字则会牵动他的自我陈述和日常习惯。长期伪装可以写成一份可执行的行为规则——不遮脸以免显得有东西可藏、用自嘲代替遮掩、故意结交不合身份的人、超额许诺再逐一兑现、让真性子一年年失实——这份清单能直接当章节议程用。`
对应记账：LI-GE-1298 ＋ v2 HI-39 `交付与依据` 行被整行删除的通用半句

补丁 **P04**（LI-GE-1305）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/livelihood-and-action.md`
- 定位锚：`越具体越能解释他凭什么赢。`（HI-44 能力通过具体结果与限制显现，a2 P08 已落笔后的段末）
- 动作：行内追加
- 新文：`也可以让某个人物全程只用一种职业语言理解公共事务，账目、货单、工期或矿脉都行；这套说法要真的进入他的决定——先算成本再动手——并在他算错的地方留下后果，只当点缀就删掉。`
对应记账：LI-GE-1305
可能同点：`livelihood-and-action.md` HI-44 段末已有 G06-a2（P08）落盘文本；本片句请串在其后——a2 写能力由别人眼里到场，本片写贯穿性职业隐喻，两句互补不重叠。

补丁 **P05**（LI-GE-1273）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/livelihood-and-action.md`
- 定位锚：`区分报道、亲见、宣传和叙述者夸张。`（HI-48 制度化伤害呈现命令、见证与后果，段末）
- 动作：行内追加
- 新文：`受害者的处境要落到一件他此后不得不做的事上，不能只用来给主角加筹码或替反派加深度。呈现压迫结构时，让从中得利的人自己把道理讲圆，比旁白谴责更能显出机制；同时给被压迫者留一个能采取行动的位置，只让他受苦不算写完了。`
对应记账：LI-GE-1273 ＋ v2 HI-48 `交付与依据` 行删除的「不以受害者仅为主角奖惩工具」

补丁 **P06**（LI-GE-1277）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/institutions-and-documents.md`
- 定位锚：`不以缺信物或没有痛苦代价判忠诚无效。`（HI-21 忠诚通过选择也可成立，段末）
- 动作：行内追加
- 新文：`凭证不止能出示的物件一种：能复述的内容、能当众拒绝的行为同样算数。验证忠诚可以设一处机关——先诱他违令，再看另一处给的回报定赏罚；被测者若两头都报，机关就自己破了。说出口的承诺也可能被误读或撤回，不写成一出口便永不可改。`
对应记账：LI-GE-1277 ＋ v2 HI-21 `交付与依据` 行删除的通用半句

补丁 **P07**（LI-GE-1300 ＋ LI-GE-1283 内 3-4）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/institutions-and-documents.md`
- 定位锚：`物理机智不是每次都能两全。`（HI-22 双重承诺按范围与优先关系解决，段末）
- 动作：行内追加
- 新文：`由保密职责持有的人数，不因持有人死亡就自动开口；什么动作才算解封——当事人自己说出、持有人在有权场合交代、文书出土——要写成这个世界里可核对的规则，没有依据就别借现实宗教法或执业规范背书。`
对应记账：LI-GE-1300 ＋ v2 HI-22 `交付与依据` 行删除的「告解保密不得因人死了自动解除」

补丁 **P08**（LI-GE-1287）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/institutions-and-documents.md`
- 定位锚：`只写他恨主角填不上这四格。`（HI-25 反对者的目标决定高潮措施，a3 P13 已落笔后的段末）
- 动作：行内追加
- 新文：`对手迟迟不动手也要有可点名的成本：人手不足、程序未走完、舆论会反噬、他自己误判了信息；只写他在等时机，读者看到的是作者之手。`
对应记账：LI-GE-1287
可能同点：HI-25 段末已有 G06-a3（P13）落盘文本；本片句串在其后——前者管动机落到措施，本片管按兵不动的成本。

补丁 **P09**（LI-GE-1278）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`浪漫姿态不自动解决资源和同意问题。`（HI-50 求婚方式显示双方对未来的想象，段末）
- 动作：行内追加
- 新文：`可以直接问、可以等、可以由两家签约、可以先立功再提亲；四种姿态能混用，不是四种人物类型。沉默不等于答应；拒绝的一方也未必不愿答，而是确实没有答案可给——这种无词之拒比一句干脆的拒绝更能推动后文。`
对应记账：LI-GE-1278 ＋ v2 HI-50 `交付与依据` 行删除的「沉默不自动等于同意」

补丁 **P10**（LI-GE-1288）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`善意动机不自动使强制合理。`（HI-51 保护性驱逐要接受被保护者的检验，段末）
- 动作：行内追加
- 新文：`被赶走的人把这次驱逐读成保护还是读成厌弃，就是下一段的燃料；出面保护的人可以同时有深情和利益，这份混合不自动给他奖赏，也不自动判他有罪。`
对应记账：LI-GE-1288 ＋ v2 HI-51 `交付与依据` 行删除的「家人干预也可兼有欲望与利益」

补丁 **P11**（LI-GE-1289）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`离开也不自动意味着忘恩。`（HI-52 代理照护、恩义与离开有可协商边界，段末）
- 动作：行内追加
- 新文：`接位常借长辈或导师之死完成，但要留下一件实物和一句训示，并让这句训示在结尾被遵守或被违反；离开提携者时清点真正相关的那几项——该还什么、只取什么——清单式的告别会让日后折返成为悲剧而不是反转。`
对应记账：LI-GE-1289

补丁 **P12**（LI-GE-1303）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`不要求所有家庭成员最终达成单一版本。`（HI-53 家史允许遗忘、不同重点和兼容叙述，段末）
- 动作：行内追加
- 新文：`查不到不等于没有发生过；家里活得最久的那位常常成了记忆的托管人，他的讲述欲、收藏癖和对旧墓的照料就是叙述者的来历，也让他天然偏心。还可以反过来虚构一条禁止记住或禁止讲述的规矩，让讲述本身成为越界；这条规矩要有后果——确实有人因回忆受罚——否则只是标语。`
对应记账：LI-GE-1303 ＋ v2 HI-53 `交付与依据` 行删除的「资料未查到不是事件必不存在」＋ LI-GE-1277 的记忆遗族侧

补丁 **P13**（LI-GE-1283）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`物件存在不自动证明身份、所有权或超自然因果。`（HI-54 遗物既能说明事实，也能暴露解释分歧，段末）
- 动作：行内追加
- 新文：`家族往事的铺陈可以逐件由遗物带出，每件配一句持有者的判词，比连续两段旁白铺家谱省力；来历各执一词的实物——他说他先发现、她说她收到过——本身就是一部关系史，不必判谁对。只被作者点过名而没人关心的物件要补上关系动作；只作象征的物件不要求过堂认证。`
对应记账：LI-GE-1283 ＋ v2 HI-54 `交付与依据` 行删除的通用半句

补丁 **P14**（LI-GE-1295）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`叙述者不能把推测当诊断。`（HI-56 病痛与精神困扰不按角色等级分配结局，段末）
- 动作：行内追加
- 新文：`人物把自己的病症当筹码时，写另一方为此长期做出的回避——改称谓、换座位、不敢再用某件旧物；这些调整比病因本身更能显示谁在让步。触发他失态的东西必须是读者已经知道的那件事，不能在崩溃现场才新补一件。`
对应记账：LI-GE-1295

补丁 **P15**（LI-GE-1290）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`不把受害者的选择归咎于其品格。`（HI-57 胁迫、仁善反噬与心智博弈保留选择空间，段末）
- 动作：行内追加
- 新文：`一时善行要变成日后被人拿住的把柄，得当场有第三个人把它记下或估出价。阻止恶行可以搬来一位不在场者的注视，但这个人要和作恶者有具体的旧谊，只写抽象的名誉落不了地。家族或组织内部的逼迫可以按台阶升级——造谣、禁足、断资源、动手——每两级之间给被逼迫者一次没成功的自救；只有台阶没有自救，读者会感到有人按着人物的头。`
对应记账：LI-GE-1290

补丁 **P16**（LI-GE-1291）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`动物行为不自动证明某种超自然解释。`（HI-58 动物有身体需要和有限认知，段末）
- 动作：行内追加
- 新文：`用动物或非人视角开口时，禁它读人心，只写它闻到的、听到的、疼痛的和学会回避的那些事；地位滑落可以由身体损伤与劳动条件一环环推下去。牲畜的负重、疲惫和替换要算进行动账，也不能让它替缺失的证据说话。一只被全家当成圣物的动物或旧物，它的死亡或被挪用可以成为家族转折点。`
对应记账：LI-GE-1291 ＋ v2 HI-58 `交付与依据` 行删除的「避免让动物代替必要证据」

补丁 **P17**（LI-GE-1297）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`宗教话语不自动证明世界规则。`（HI-60 宗教辩词与人物伦理不可省为真理标签，段末）
- 动作：行内追加
- 新文：`一句反驳不足以销掉整部作品的预设，被反驳之后还要有制度或生活层面的后果跟上。劝人节制或守心的人，要让他承认自己也没忘情，否则规劝就成了伪善；有人用世道变了、约束都散了来劝人背弃忠诚时，被劝的人至少留一句自己的怀疑。`
对应记账：LI-GE-1297 ＋ v2 HI-60 `交付与依据` 行删除的「反驳声不能独自消除全书所有偏见」

补丁 **P18**（LI-GE-1302）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/relationships-and-belief.md`
- 定位锚：`不把一首歌固定成唯一含义。`（HI-63 歌谣、乐器与诗句有多种关系功能，段末）
- 动作：行内追加
- 新文：`引用的诗句、歌词和所谓古调要能在故事世界里找到它的来处——家传的册子、市集上唱的句子、庙里念的调子；由作者临时冒充古作，读者会在出处那一处失去信任。同一支曲子要承担两种作用（安抚与拦下动手）时，先铺它与旧事的联结，第二次出现才不突兀；文学里写成的疗法不能当现实医疗建议。`
对应记账：LI-GE-1302 ＋ v2 HI-63 `交付与依据` 行删除的「旧小说的疗愈情节是文学写法，不是现实疗法」

补丁 **P19**（LI-GE-1312）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/narration-and-period.md`
- 定位锚：`不把所有日常细节都写成阴谋。`（HI-90 权力清洗会进入日常安排，怎么做段末）
- 动作：行内追加
- 新文：`远方的政治争执也可以借一件私人物件或一个公职身份走进家门——一份报纸、一幅地图、一桩差事；写清谁先听到、传到哪里、对这家人日常的约束造成什么变化，人物对局势的预测只算他的观点。`
对应记账：LI-GE-1312

补丁 **P20**（LI-GE-1306）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/narration-and-period.md`
- 定位锚：`关系能让人提出请求，不必自动赋予批准权。`（HI-68 接近权力的通路需要资源与身份，段末）
- 动作：行内追加
- 新文：`接近权力多半靠日常特权——谁在席上、谁端早餐、谁被许进内院——不是靠一条秘密通道；这条通路没写明权限时就改路线或推迟，别在需要时突然送给人物一份没人批准的身份。羞辱看门人反而会让他把权限攥得更紧，先处理他对自己处境的理解，再谈物理方案。`
对应记账：LI-GE-1306 ＋ v2 HI-68 `交付与依据` 行删除的「是宫廊与早餐的特权接近，非秘密地下工程；无入口就改路径／推迟」

补丁 **P21**（LI-GE-1293）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/settlement-and-revision.md`
- 定位锚：`司法救济也不要求宽恕。`（HI-85 纪念与宽恕保留幸存者的自主，段末）
- 动作：行内追加
- 新文：`谁有资格公开哀悼、谁能被允许哭泣，也可以是权力问题：让旁人追问领袖为什么只哭自己人，他回答的方式——听从、发怒、宣告——就把末路写出来了。失常状态下的亲和、死者的遗愿和家族的荣誉，都不能自动算作当事人的同意。`
对应记账：LI-GE-1293 ＋ v2 HI-85 `交付与依据` 行删除的「不要把失常、死者遗愿或家族荣誉当自动同意」

补丁 **P22**（LI-GE-1292）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/settlement-and-revision.md`
- 定位锚：`没有三次/五次公式。`（HI-86 母题回收检查意义变化，不凑出现次数，段末）
- 动作：行内追加
- 新文：`用开篇的形式在结尾完成收束是一类独立做法——同一串物件、同一段结构、同一支调子——它可以只闭合形式而不闭合因果；押上同一个意象不等于所有人物的账都结了。收束的分量也可以来自形式而不是再让一个人死去。`
对应记账：LI-GE-1292 ＋ v2 HI-86 `交付与依据` 行删除的「形式闭环可与因果闭合分离」

补丁 **P23**（LI-GE-1294）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/settlement-and-revision.md`
- 定位锚：`悬而未决不等于所有因果空白。`（HI-84 开放结局须清楚留下什么问题，段末）
- 动作：行内追加
- 新文：`也可以停在一份没兑现的实物上——没修完的路、没填的年份、没数完的房间——让沉默承担结构，剩下的部分由讲述者明说自己是补上来的。结尾处一句两读的断喝，能把人物是否回头留给读者；不给唯一正解可以，但不能自称已经闭合。`
对应记账：LI-GE-1294 ＋ LI-GE-1282 的停笔点侧 ＋ v2 HI-84 `交付与依据` 行删除的「不给唯一正确解则不伪称闭合」

补丁 **P24**（LI-GE-1276）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`若误读，要让当时的理解合理；若失败，写清信念如何变化。`（HI-C22 怎么做段末）
- 动作：行内追加
- 新文：`也可以让说法靠知情者的应对自我实现：他躲避它的每一步恰好是应验的路径，两处要逐点咬合才成立。关键句写成能够两读的，听者被迫先选一种并按它行动，这个选择就把他的性格交代完了。写下每条说法后自问：它能不能改写出两种以上的应验读法；只有一种读法的，谜底在第一节就钉死了。`
对应记账：LI-GE-1276

补丁 **P25**（LI-GE-1313 ＋ LI-GE-1306 弃证侧）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`把人物推断与观察分开，给误判留下可解释的原因。`（HI-C34 怎么做段末）
- 动作：行内追加
- 新文：`关键物件可以按四格登记：原本什么状态、谁能看见它、什么时候被用上、谁为此付出；四格都在场，物件才承重，只写那里放着一样东西的通常只是气氛。用完之后把物件毁掉或丢进深水，会同时断掉别人顺着它追来的路，也让持有者自己永久失去凭据——两头都要写。`
对应记账：LI-GE-1313、LI-GE-1306 ＋ LI-GE-1296 的装死破功侧

补丁 **P26**（LI-GE-1284）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`梦可以是愿望、恐惧或事后重构。`（HI-C35 怎么做段末）
- 动作：行内追加
- 新文：`被家里人抬成圣人的死者，等于被从记事里除名——这份理想化可以当作生者施加的压力来写，别让她复活发言。共同诵念的文本可以各怀两解，两边默诵时落在不同的句子上，一段祷文同时是停战和宣战。遗嘱也可以不写总册而散记在各件遗物背面，清点遗物就成了回顾全书。`
对应记账：LI-GE-1284 ＋ LI-GE-1303 的改口私语侧

补丁 **P27**（LI-GE-1299）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`对家史攻击记录受众认识和实际伤害。`（HI-C43 怎么做段末）
- 动作：行内追加
- 新文：`拿对方家族的旧污点当辩论弹药，杀伤力停在第二击之前；接着数下去就降级成互相揭短，需要在场第三人当场打断才收得住。借别人的手完成一次近距离接触后，事后揭示要能指回当时一处可核对的身体细节。`
对应记账：LI-GE-1299 ＋ LI-GE-1277 的谱系武器战侧

补丁 **P28**（LI-GE-1279 ＋ LI-GE-1307）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`守卫计算也不必只有一种回应。`（HI-C46 边界段末）
- 动作：行内追加
- 新文：`行进线上的一次性配角可以一人只担一职——控诉、警告、施恩或救场——在这一景内闭环，不留待接的钩子。负责解说的谐角只降格气氛、说出市侩的算盘，不让他在关键处替主角解围。戳破谎言的判词命中当下这一处就够了，删掉后半句如果更有力就删；吹牛者拿来撑场面的具体数字，要让内行一句话戳破一次。`
对应记账：LI-GE-1279、LI-GE-1307 ＋ LI-GE-1296 的判词侧

补丁 **P29**（LI-GE-1282）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/history-contract.md`
- 定位锚：`未接触的私事可通过限定的转述、推断或全知叙述说明。`（HI-11 讲述者的接近条件决定所知，段末）
- 动作：行内追加
- 新文：`回忆写到中段，可以让一个在场的人审问讲述者哪些部分毫无疑问是真的，让他承认有不知道的地方；主动交出一部分可信度，才换得继续讲下去的许可，哪些是补写的也要一并交代给读者。`
对应记账：LI-GE-1282

补丁 **P30**（LI-GE-1281）：
- 落点文件：`output/genre-fiction-craft/references/06-historical-alternate/historical-fiction-patterns.md`
- 定位锚：`把档案内容与人物解释分栏。`（HI-C13 怎么做段末）
- 动作：行内追加
- 新文：`构陷要成链才像机器：一条伪信、一件形似凶器或衣料的物件、一道看起来正当的程序、一个认错人的证人各占一环，只有单件时读者读到的是巧合。伪信要引用只有同党才知道的细节，并交代设局者从哪儿窥到这个细节——这一环补不上，剩下的只是作者安排。谜底要延迟多年或一代人时，写清这段时间谁保管谜面——旧仆、档案、墓碑或一件没人再动的遗物——保管人在揭晓前要有一景立住。`
对应记账：LI-GE-1281 ＋ LI-GE-1282 的解谜延迟侧

---

## 可能同点清单（供主代理串行合流）

| 落点行 | 本片补丁 | 与他席关系 |
|---|---|---|
| `livelihood-and-action.md` HI-44（段末） | P04 | **真实同点 1**：该行末已有 G06-a2 P08 落盘文本；本片句请串在其后，语义互补（能力展示位置／贯穿职业隐喻） |
| `institutions-and-documents.md` HI-25（段末） | P08 | **真实同点 2**：该行末已有 G06-a3 P13 落盘文本；本片句串在其后，前者管动机四格，本片管按兵不动的成本 |
| `relationships-and-belief.md` HI-61（段末） | 0 条（不议案） | a1 P08 与 a2 P11 已在该行末串成两段语义几乎相同的「先放可核对的小说法再放大说法」；本片判**不在该行追加**，重复处置建议见 selfcheck 存疑项 |
| `livelihood-and-action.md` HI-47／HI-43／HI-36 | 0 条 | 三行已各带 2–3 席落盘文本（a1 P11、a2 P16／P04／P10、a3 P14／P21）；本片改落 HI-34／37／39／48 空行，避免同一行第四次叠加 |
| `history-contract.md` HI-01／03／05／07／09／12／13 | 0 条 | 七行已被三席写满；immersion 侧 H01／H02／H04 判在位（LI-GE-1311），本片改落 HI-11（P29，该行无他席文本） |
| `narration-and-period.md` HI-69／70／73／75 | 0 条 | 已带 a3 P17／a1 P09＋a2 P13／a2 P15／a1 P10＋a2 P17 文本；本片改落 HI-68、HI-90（两行均无他席文本） |
| `settlement-and-revision.md` HI-81／82／87 | 0 条 | 已带 a1 P12＋a2 P12／a3 P24／a1 P13；本片改落 HI-84／85／86 |
| `historical-fiction-patterns.md` 七处落点 | P24、P25、P26、P27、P28、P30 | 三席对该文件**零补丁**（各自记录明示「0 条，判已覆盖」），本片七处全部独占，无同点 |
| `templates.md`／`guide.md`／`examples.md`／题材 `SKILL.md`／两个 `agents/openai.yaml` | 0 条 | 按简报第 6 节只走移交项（下节）；本片不新增 HI／HI-T／HI-C 编号、不改小节标题与表列 |

---

## 附录 B 扫描（对 P01–P30 全部新文跑 11 类；逐类计数见 `notes/quality/genre-fiction-craft/g06a4-desourcing-selfcheck.md`）

`/usr/bin/grep -h '^- 新文：'` 实测本片 **30 条新文行**，对 11 类（拆成 18 条模式）逐类单跑，**每类命中 0**；B.3 骨架比对本片做 **10** 处（HI-34 圣地、HI-21 忠诚机关、HI-50 四式、HI-54 遗物铺陈、HI-57 逼迫台阶、HI-58 非人叙述、HI-C13 构陷链、HI-C35 三样、HI-86 形式闭环、HI-84 停在实物），人物关系／关键事件／时代地点三项相符数均为 **0–1**，无一处需重写；锚唯一性 **30/30** 实测＝1。详见 selfcheck 第二、四节。

---

## 移交项（登记，本片不动笔）

| # | 对象 | 事项 | 归属 |
|---|---|---|---|
| 1 | 题材 `SKILL.md`（06 路由行）＋两个 `agents/openai.yaml` | plot-forge 的触发（六域问题式）、负触发（史料裁定、现实危害工艺、非小说任务）、主决策表四档文类×六域、六域导航；immersion 的任务路由五行、输入权威、`allow_implicit_invocation: false`、display_name 等三字段 | G00／W4 |
| 2 | `output/genre-fiction-craft/references/06-historical-alternate/guide.md` | 「从任务进入」表可增一行「情节卡在哪一域」入口（plot-forge 主决策表的现成位置）；「做不下去时」表已有反派全知、道具只剩标签两行，本片语义改落 HI-25／HI-C10 在位句，不动表 | G00／W4 复核 |
| 3 | `scene-conflict-and-rhythm`（Agent 2） | 单景配角闭环、谐角不解救、章内节拍与收束节奏属场景单位层；本片只在 HI-C46 补 genre 侧判据 | Agent 2 |
| 4 | `character-and-narrative-control`（Agent 3） | 非人叙述者禁读人心、多层讲述的知情权限、回忆者自审属视角合同与心理落动作层 Owner；本片落点仍为 genre 卡 | Agent 3 |
| 5 | `story-architecture-and-longform-planning`（Agent 3） | 谶语分句绑定应验、谜面保管人、跨卷延迟揭示属跨章记账；本片只保留 genre 侧做法句 | Agent 3 |
| 6 | `fiction-planning-and-diagnosis`（Agent 4） | plot-forge P4 段「交付」九项与 immersion A07-D01–D10 核验表字段族的通用输出规范 Owner 在 fiction-planning；本题材由 HI-T01–HI-T12 承接 | Agent 4 |
| 7 | `notes/desourcing-ledger.md`／`lineage-map.md`／`log.md`／raw 表下版 | 本片 25 个 SOURCE_ONLY 单元的逐轴承接、30 条补丁的落笔行号与复扫需求、r2 谱系二 5 文件整件漏列的修正、`historical-fiction-craft-b03`（2713–2796）与 `historical-fiction-power-machine`（2867–2935）共 153 行本批无席认领的覆盖缺口 | 共享文件本片不写；已列存疑项 |

---

## G06-a4 决策链（附录 G.1 格式；主代理收口时串行并入 `notes/source-synthesis/genre-fiction-craft.md`）

### D1 简报给的盘上实况与盘上不符：按 v3 原态还是按已落笔的盘上态取锚

1. **情境**：简报断言 06 目录仍是 v3 原态、三席补丁未落盘；实测七件大于 v3、五十五段新文全部能在盘上现文里 `grep -F` 命中（第一节 1–2 项）。确实拿到的是当前盘上文本与 v0／v1／v2／v3 四个提交。
2. **区分信号**：以逐件字节差与 `diff` 判定，不按 mtime 推断（`settlement-and-revision.md` mtime 03:59 却含四段他席文本，证明 mtime 不足以判基线）。判错的代价是锚失效或覆盖他席已写文本。
3. **两条分支**：A（照简报）按 v3 抄锚——会在 HI-44、HI-25 等行末与 a2／a3 文本撞在同一位置串成同义重复；B（照盘上，本片采用）逐件重取锚，并主动让开三席已写满的行（HI-47／43／36／03／05／61／69／70／75／81／82／87），把语义改落到同文件里最贴近且未被写的行。停下请作者裁决的情形：无（属本片判断范围）。
4. **反例与修复**：若主代理最终落笔顺序让本片先写、三席文本未落，本片每句仍独立可读（全部为追加、不引用他席句）；若三席某句被回退，需重查 HI-44、HI-25 是否留下语义缺口。复查项＝补丁落点后逐行通读是否仍是两个独立句子。
5. **成品落点**：P01–P30 所列八件文件的行末；让位规则见「可能同点清单」。

### D2 一张 HI 卡叠了几层追加之后还要不要写：落点改行而不是叠句

1. **情境**：06 十件里六件是四席共用文件，本片要在同一张卡上补一句，但部分行已经串了两席文本。
2. **区分信号**：看该行现有追加层数与语义是否互补；反信号是同一行出现两段近义句（HI-61 已是实例）。代价是成品臃肿、读者读到重复。
3. **两条分支**：A 直接追加到语义最自然的行末（本片仅 P04、P08 两处，且都写明串在他席之后）；B 把语义改落到同文件另一张未被写的卡（P29 从 HI-73 改落 HI-11、P08 从 HI-C03 改落 HI-25、P19 从 HI-46 改落 HI-90、P20 从 HI-14 改落 HI-68）。何时停下请作者裁决：若必须两处都落才完整，则记存疑不自行拆写。
4. **反例与修复**：若他席后续删掉了原本承接的那句，本片的改落点可能变孤句；预防措施是每句自带适用条件，不依赖行内前文。复查＝主代理落笔后回读该行。
5. **成品落点**：见「可能同点清单」九行。

### D3 v2 `**交付与依据**：` 行的分拣：通用限制句找回，专名与阈值丢弃

1. **情境**：v1／v2 的 `怎么做` 行与 v3 逐字相同，v3 只删了 `交付与依据` 行。这些被删行里既有作品名、章序、人名，也有一批不带来源名的通用限制句与检查项。
2. **区分信号**：句内是否出现专名、行位或次数阈值——出现即只作线索；不出现且 v3／盘上无等价表述的判连带删除找回。判错代价是把来源残留写回成品（附录 B 违规），或把后版已放宽的口径重新收紧。
3. **两条分支**：A（找回，17 例）——HI-34 神圣不可入、HI-37 守恒、HI-39 换装无新本事、HI-42 借来物件、HI-43 抽象阵营名、HI-48 受害者不作工具、HI-50 沉默不等于答应、HI-51 混合动机、HI-53 查不到不等于没有、HI-54 无人关心要补动作、HI-58 动物代替证据、HI-60 反驳不足以销预设、HI-63 疗法不可当现实建议、HI-68 无权限就改路、HI-84 不给正解不伪称闭合、HI-85 遗愿不当同意、HI-86 形式闭环与因果闭合分离；按语义合并成 P01–P05、P09–P13、P16–P18、P20–P23。B（丢弃）——人名、章序与 PG 行位，以及已被 v1 放宽的次数与配额句（「画可复用简图」只保留在 HI-T06 字段侧；各类「三处／两次／一次」阈值不写）。
4. **反例与修复**：若某通用句其实已被 v3 以另一张卡承接（HI-42 借来物件与 HI-59 相貌相似、HI-43 抽象阵营名与 a2 P04），本片改判在位或改落他行——本片实测把 HI-42／HI-43 两例改判不追加，只保留 HI-44、HI-48 等真空位。复查＝落笔后 grep 该卡是否出现两处同义。
5. **成品落点**：`livelihood-and-action.md` HI-34／37／39／44／48；`relationships-and-belief.md` HI-50／51／53／54／58／60／63；`narration-and-period.md` HI-68；`settlement-and-revision.md` HI-84／85／86。

### 不适用（简单而无分支，按附录 G.1 写一句）

- 现实危害工艺（制毒与发作时间表、仿钥与开锁工序、伪造与规避追查）与医学、法证、遗传结论：v0 自身与 v2 均已限定「只迁移叙事链」，盘上 HI-47／HI-C34／HI-T06 三处已在位，本片无分支可写，直接判红线不恢复（LI-GE-1296、LI-GE-1306）。

---

## 完成标准自证

1. **单元覆盖**：本片自测 r2 题材 06 段第 2491–2969 行、表体 2523–2966＝444 行（与第 2518 行声明一致）；**本片行段＝第 2797–2866 行（70 行）＋第 2936–2966 行（31 行）＝101 行**，另补判 13 单元，两片实得 **114 单元**（谱系一 73、谱系二 41）；一行不漏的核对方法（正向分桶＋反向逐件回读）、b03（2713–2796）与 power-machine（2867–2935）两段的边界行号、r2 两处失真修正全部写在第二节；两段共 153 行不在本片清单，登记为存疑与移交。
2. **九列齐全**：46 条决定全部按 A.2 八项内容列齐（另加「片」列成九列）；编号连续 **LI-GE-1271–1316**，谱系一 1271–1307、谱系二 1308–1316，段内**无空号**；**LI-GE-1317 至 1320 为未用余量、非空号遗漏**。
3. **三条口径**：`MISSING ≠ 丢失`（0 条按 MISSING）；`覆盖率 ≠ 内容保留率`（20% 只说明融合重组）；`raw 表是信号不是结论`（每条恢复都有 v0／v2 回读与盘上 grep 支撑）；**SOURCE_ONLY 合计 25 单元**（r2 标记行 13：谱系一 9＝`historical-provenance.md` 2＋批次标记 1＋`source-contract-and-decisions.md` 4＋`sources.md` 代表行 2；谱系二 4＝`source-index.md` 具名 1＋裸 PG 3；另按来源性质归类的 `examples.md` 7 行、`SKILL.md` 来源与审计 1 行、`06-source-index.md` 2 补判、A07-H16／H17 2 条）**不恢复、不建新文件**，逐轴通用语义承接写在 LI-GE-1275／1285→见 1304／1309／1315／1316 各行理由列。
4. **恢复／合并全部有补丁块或有列归属**：合并 30 条对应 P01–P30（一行两补丁见 LI-GE-1280，两行一补丁见 LI-GE-1279＋1307）；**2 条判移交**（LI-GE-1271 与 LI-1310，内含 SKILL 路由行、两个 `agents/openai.yaml`、输出合同九项与 guide 表事项，另 5 项跨 skill 归属列在移交项表）；1 条分承（LI-GE-1286）；其余 13 条不恢复逐条写明判据（在位／后版有意调整／红线禁项／SOURCE_ONLY）。
5. **附录 B**：30 条新文对 11 类（拆 18 模式）逐类计数**全部为 0**；B.3 骨架比对 **10** 处，相符数 0–1，无重写；四项通用检查（标志性情节元素、借来源背书、删除来源后语义不通、表格与空列）见 selfcheck 第四节。
6. **验证范围**：本轮 Verification Authority＝**static**，未运行测试／lint／构建／冒烟，未启动应用，未做任何 git 写操作；结论均为源码与盘上文本的静态核对，不等于效果已验证。

## 断点

- 本片交付：`notes/loss-inventory/genre-fiction-craft-G06-a4.md`（本件）＋`notes/quality/genre-fiction-craft/g06a4-desourcing-selfcheck.md`。
- 待主代理：按 P01–P30 串行落笔（建议顺序见补丁清单前言，两处真实同点按标注先后）；落笔后回读 06 目录逐件字节并复跑附录 B；处置 HI-61 盘上重复句；裁定 b03（2713–2796）与 power-machine（2867–2935）两段共 153 行的席位归属。

round-complete G06-a4
