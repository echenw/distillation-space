# W4 复核与待裁队列（Agent 1 汇总，2026-11-05 14:41）

- 用途：把 checklist §九～§二十六 各节「登记项／W4 复核清单／待裁／存疑」逐条归位成一份**可打勾的队列**，防止跨节丢失。计划 22.4 第 7 项（累积待裁项销项）以本文件为清单。
- 口径：本文件**不重新判定**任何一条的语义，只登记事项、来源节、当前盘上实况与判定人。状态词只用 notes 级词汇。
- 判定人分三类：**K4**＝按 D3-C 另派的只读审查子代理（只看成品包、不看 notes）；**主代理**＝Agent 1 裁决（归属、口径、台账类）；**补派席**＝需再开一片定向精读才能定的材料类问题。
- 分两表：**A 未处置**（阻塞 K5 冻结的项排在前面）与 **B 已销项**（保留证据，防重复提出）。

## A. 未处置（26 条）

| # | 事项 | 来源 | 落点／证据 | 判定人 | 是否阻塞冻结 |
|---|---|---|---|---|---|
| W4-01 | genre `SKILL.md` 定稿与 G00 混合题材一节（含路由表「补读／出口」两列） | §六／§十八／§二十五 | `output/genre-fiction-craft/SKILL.md`（未开工片） | 补派席＋主代理 | **是**（G00 未完成则 22.4 第 2 项不成立） |
| W4-02 | **P-2 genre 侧双向转介缺失**：preset-card 转给 genre，genre 全包 0 次提及 preset-card | §二十五 P-2 | `preset-card-generation/SKILL.md:40` 与 `:199` 承诺；实测反向 6／7 | 主代理（G00 定稿时补） | **是** |
| W4-03 | 03 目录 v3 基线四处残留：`testimony-and-information.md:84`「小说家」、`:100`「书内」、`:126`「本版」、`guide.md:17`「硬规则」 | §二十四／§二十五 | 复扫实测仍在（14:40 复核四命中）；已双重复测为 v3 既有 | G03-c5 出议案，主代理裁 | **是**（2.4 交付物含全套附录 B 清零） |
| W4-04 | `historical-fiction-patterns.md` 标题声明 **HI-C01–HI-C46**，盘上实存至 **HI-C48** | §二十一／§二十四 | 14:40 实测：`sort -u \| tail` 出 C46/C47/C48，标题行仍写 C46 | 主代理裁（改声明或拆表） | 是 |
| W4-05 | 同文件「使用时的总检查」首项**缺序号**（现为 305 行裸句「这张卡描述的是…」，次行才是 `2.`） | §二十一 | 14:40 `sed -n '304,306p'` 复核成立 | 主代理裁 | 否（格式类） |
| W4-06 | **G-1** 逐条清单三套列名：`SKILL.md:138` 五列／`workflow.md:77` 四列「理由」／`worked-example.md:119` 五列「复查」 | §二十三 | line-editing 包内实测三处不一致 | K4＋主代理 | 否 |
| W4-07 | **G-2** 台账「每个编号独占一行」与「编号与规则一一对应」在读法上冲突（例三 SR-10 两行） | §二十三 | `workflow.md:21`／`:27`、`worked-example.md:105` | 主代理裁措辞 | 否 |
| W4-08 | **P-1** preset-card 无空白模板；推进卡与表达约束卡小节只在散文里串行声明；固定字数带（600–750／≤300）与「不为填满模板延长输出」的张力 | §二十五 | `style.md:99–101`、`expression.md:96`、`SKILL.md:132` | K4 判必要性，主代理裁 | 否 |
| W4-09 | `delivery-preflight-spec.json` 的 **99 个 field_ids 未冻结**：须先按 `inputs/requirements.md` 判定哪些族真要求逐项可填 | §二十六 | `notes/delivery-preflight-spec/field-id-matrix.md` 双档计数 | K4（非作者）＋主代理 | 是（22.4 第 4 项） |
| W4-10 | matrix 取词式只覆盖两段式；genre 另有 **616 个三段式**（`AT-D01`／`HI-C01`／`RO-K121`／`WX-T01`）未捕获，且 genre 仍在并行落笔 ⇒ 中途快照须重跑 | §二十六 更正节 | 14:39 实测两档计数 | 主代理（W4 重跑） | 是 |
| W4-11 | scene 包两个模板**首列 0 行**（`scene-workbook.md` 仅标题式 5 行）、cross-media 两模板首列 0 行（AD 族 40 个全未成行） | §二十六 | `scratchpad/specgen.py` 可复跑 | K4 判是否属枚举需求 | 是 |
| W4-12 | story `serial-tables.md` 首列 0 行／标题式 10 行（SV 族 16 个未成独立行） | §二十六 | 同上 | K4 | 否 |
| W4-13 | S06a1 自检算术 slip：以 a2 逐类计数 **73／66** 为准并读 | §十二 | `notes/quality/fiction-planning-and-diagnosis/` | K4 | 否 |
| W4-14 | FC-21 `confidence` 字段中文化是否与包内其它字段一致 | §十二 | fiction-planning 包 | K4 | 否 |
| W4-15 | probability／latent／`scène à faire` 三个术语保留英文的判定是否站得住 | §十二 | fiction-planning 包内出现处 | K4 | 否 |
| W4-16 | S06c 新增 §10「逐条核查记录表」与路由承诺口径是否一致；定位卡交叉引用与 `SKILL.md` §3 一致性；`self-check-scenes` 立场短语 4 处；自建示例声明对账 | §十三 | fiction-planning 包 | K4 | 否 |
| W4-17 | D6 三条细则须对照 v1 原文再判（计划 2.4 曾写「仍缺」，S05a2 实测十一项已在） | §十四 | `story/references/plot-diagnosis.md` 一带 | 补派席（材料判定） | 否 |
| W4-18 | `preflight-spec` 取材三模板的口径 | §十四 | story 模板 | K4 | 否 |
| W4-19 | GQ3 双向依赖三处交叉复核（line-editing／cross-media／preset-card 互指） | §九 | §二十五 已实测 6／7 对上，仅缺 genre | K4 | 是 |
| W4-20 | 04 目录 `guide.md` 路由两列、包根 `SKILL.md`／`agents/openai.yaml` 措辞、04 两条负触发是否升格、`guide.md:53`「未核实」词形 | §十八 | genre 04 目录 | 主代理（G00 一并） | 是 |
| W4-21 | a4 模板族四件（power-system-canvas／diagnosis-report／power-arc-state／design-and-diagnosis）判已被 WX-T01–T12 吸收，**是否补一行包内档名对照**未定 | §十八 | genre 04 目录 | 主代理裁 | 否 |
| W4-22 | LI-GE-789「罚则重置／累积／部分恢复」三态只在 WX-T05 出现，如需落卡另开补丁 | §十八 | genre 04 目录 | 补派席 | 否 |
| W4-23 | a2 判「v2 删块」的书面理由无仓内文档，属**推断** | §十八 | G05-a2 记录 | K4（按证据重判） | 否 |
| W4-24 | b03 的 `agents/openai.yaml` `default_prompt` 含「按来源核账」字样；`workflow.md` 缺出口两列 | §二十 | genre 包根与 05 目录 | 主代理（G00／包根片） | 是 |
| W4-25 | G02-a4 残余 **RO-K117–119**（v2 三卡未进 v3）是否按 RO-K122 起补回，需过 B.3 | §十八末段／§二十一 | `02-romance/mechanisms.md` | 补派席＋K4 | 否 |
| W4-26 | K1 下版 raw 表须补：`references/03` 编号并掉、`references/01` 误标 `SOURCE_ONLY`、`version-and-provenance.md` 漏项、同单元重复具名行与 SF-01–08 误对齐 | §二十一／§二十 | `notes/loss-inventory/raw/*-r2.md` | 主代理（另起带日期文件，A.3 不覆盖） | 否 |

## B. 已销项（保留证据，不得重复提出）

| 事项 | 销项依据 |
|---|---|
| fiction-planning `references/diagnosis.md:411` 审计词替换 | §十二（S06a2 落地，#9 全包复扫零命中，主代理独立复核一致） |
| `self-check-modern-and-zh.md:32` 来源年代 | §十三（S06b 清除后 #3 全包清零） |
| `serial-zh-webnovel:9` 的 #4 全包唯一命中 | §十五（S05b2 改写后 #4 归零） |
| S04b 两处命中（「书里明写」「小说家」） | §十（三处移交全部销项） |
| G06-a1 与 a2 的裸 `Fnn` 认领口径 | §二十一 待裁①（采 a2「按文件切」口径） |
| G11-b2 的 `B01`／`B-07` 边界行（r2 4135–4136） | §二十四（b4 闭合矩阵，判归 b2；4080–4134 与 4017–4044 待 b3） |
| G06-a4 与 a5 的 r2 2713–2796 行号争议 | §二十四（采 a5 文件归属，a4 起点应为 2797） |
| b2 声明「craft 自 4563 起」 | §二十四（主代理整行复测：裸 `T1`–`T10` 无 craft 侧命中、architecture 有 templates ⇒ 起点 4573 归 b4） |
| lineage-map 两处「待核」 | §二十（已改写为已裁结论，待核数 0） |
| `character-and-narrative-control/character-and-narrative-control/` 空目录 | §二十四实况复核（14:40）：**盘上已不在**。主代理本轮未执行任何删除，成因未追溯（空目录不入 git 跟踪，可能随某席文件操作消失）。登记为已销项，仅保留「成因未溯」一句。 |
| S07 移交的 preset-card 侧转介接收行 | §十一（S07 已落地 D2=A 双向两表） |
| RO-K121–166 与 RO-K116–120 的整批恢复问题 | §十八末段（46/46 已有落点，恢复 0） |

## C. 队列使用规则

1. **不新增维度**：W4 每轮只消本队列已有条目；若审查中发现新问题，追加进 A 表并给新 W4-nn 号，不在别处另立清单。
2. 每条判定后把结论写回**对应包的** `notes/quality/<skill>/` 与 checklist 追加节，本文件只更新「状态」列（A.3 只追加，不删条目）。
3. A 表中标「是」的条目共 **10 条**（W4-01、02、03、04、09、10、11、19、20、24），另有**队列外两项**同样阻塞 K5：`output/` 整树 SHA 冻结、`quality/*` 16 份按真实产物重做。**求和：10＋2＝12 项阻塞**（不含 GQ5，GQ5 按授权边界长期 NOT_PROVEN）。
4. 本文件不构成任何验收结论：**GQ1–GQ4 未执行、GQ5 未授权、两个 SHA 为 null**。


## 队列更正（追加，2026-11-05 14:51；不改写 A 表历史行，以本节为准）

- **W4-11 判据更正**：原条「scene／cross-media 模板首列 0 行」中的**主台账部分为取词假象**。四档复测显示 `scene-workbook.md` 与 `adaptation-workbook.md` 均有「每个编号独占一行」声明＋四列表头＋**占位行**（`<规则编号，如 SU-02 / SU-06 / SU-19>`、`AD-01 / AD-07 / AD-19`）。**该条收窄为**：scene `action-checklist.md`（AF 族 18 无台账）与 cross-media `interactive-branch-sheet.md` 两处待判；判定人仍为 K4（须先按 `inputs/requirements.md` 确认是否要求逐项可填）。阻塞标记由「是」降为**否**（主台账在位）。
- **W4-12 维持**：story `serial-tables.md` 四档全 0（声明／表头／占位／真 ID 行），SV 族 16 个编号在包内但模板无台账，仍待 K4 判。
- **W4-10 追加一句**：genre 六个题材目录（03／04／05／06／09／11）模板的真 ID 行＝0，但其卡号多以 `###` 标题或第二列承载，**首列判据对 genre 不适用**；下版 matrix 须按形态分列，不得以「0」发布。
- 计数更正：A 表实际条目 **26 条**（W4-01…W4-26），本轮更正后其中**阻塞 K5 的由 10 条降为 9 条**（W4-11 撤销阻塞标记），队列外两项不变 ⇒ **阻塞合计 9＋2＝11**。


## 队列新增（追加，2026-11-05 14:53）

| W4-27 | 01 目录 v3 既有**非正则残迹**：`该书`、`solve/prove`、`Monday/Tuesday`、「原例：」等来源侧字样（附录 B 十一类不覆盖） | §三十一（G01-a4 移交项） | `01-mystery` 多处 | K4（P4 语义回读） | 否 |
| W4-28 | **a5 与 a4 的重复记账协调**：01 题材的 `R1–R12`／`REJECT-1..7` 批次标记若被 a5 当作「被推翻的丢失」再记一次，须并到 a4 已判条目、不重复落笔 | §三十一 | `notes/loss-inventory/genre-fiction-craft-G01-a5.md`（待回传）对 a4 记录 | 主代理（a5 回传落笔时核） | 否 |
| W4-29 | **来源未追溯写入**：07／11 两目录九件在 14:54:55 同秒被写入，内容与 G07-a3（18 条）／G11-b3（20 条）补丁逐字全等，无 `prepatch` 备份、无台账与 log 记录，两席自述零写入 | §三十二 | `references/07-survival-disaster/`、`references/11-identity-revenge-intrigue/` | K4（逐文件隔离回读并追认）＋主代理（成因） | **是** |
| W4-30 | a1 存疑③ 疑似与 a2 重复的「复述复原」句：主代理实测全包命中 **1**、`A1` **0** ⇒ **未复现**，保留记录供 K4 复核语义相邻度 | §三十二（G01-a1 存疑③） | `01-mystery/evidence-identity-testimony.md`、`investigation-and-institutions.md` | K4 | 否 |
| W4-31 | 03 题材 r2 段两处行段争议：① 1056–1057 两行（裸 `B05`／`P4`）现无席认领，属 b05 谱系但在 c3 声明起点 1058 之外；② c2 记录把 c1 段写作「991–1057」与 c1 自述「991–1055」矛盾 | G03-c5 收官任务 1／§二十四 | `raw/genre-fiction-craft-...-r2.md` 1056–1057、G03-c1／c2 记录 | 主代理（归属裁定）＋K1 下版 | 否 |
| W4-32 | 03 目录 v3 基线四处残留的处置议案已交（Y03-1「书内」→改叙述顺序、Y03-2「小说家」→「我并非在编故事」、Y03-3「本版」判 B.2 允许、Y03-4「硬规则」→「成文条款」），待裁后落笔 | G03-c5 收官任务 2 | `03-horror/testimony-and-information.md:84/100/126`、`guide.md:17` | 主代理 | 否 |
| W4-33 | G07-a3 与 G11-b3 的 38 条恢复／合并行状态列仍写 `未处理（补丁 Pnn 待主代理写入）`，与盘上实况不一致；须按 W4-29 追认结果统一回写 | §三十二 | 两席记录的状态列 | 主代理 | 否 |
| W4-34 | G12 待裁四项：r2 第 4662 行 `P4` 段首归属（a1 只登记不认领）＋`more-examples.md:22`「虎变黄油」＋`mechanisms.md:22` 缺行首竖线＋`templates.md:31` CY-T23 措辞；a1 已交 a2 与主代理合并裁 | G12-a1 存疑①／移交项 | `12-children-youth/` | 主代理（a2 回传后） | 否 |
| W4-35 | 题材 09 两项待处理：① v3 基线残留 8 处（`premise-and-ledger.md:7/21/29`、`beats-and-payoff.md:27`、`language-and-rhetoric.md:17/27`、`satire-and-limits.md:25` 等旧作桥段字样）＋`satire-and-limits.md:9` 英文残迹「said/meant」需收官席出议案表；② r2 枚举缺口：`01-partner-engines.md` 9514 B 整张表**零枚举**、6 个 0 字节壳行、5 个字节相同的批次／书目伪行 | G09-a1 移交③④ | `09-comedy/`、`raw/...-r2.md` | 主代理＋K1 下版＋K4 | 否 |
| W4-36 | 状态词两处定义不一：「未能核实」「待作者决定」在 `SKILL.md:201-202` 与 `references/interactive-adaptation.md:56-57` 各多／少一种情形，同一词两个口径（建议 SKILL §10 为唯一权威） | 合同 X-1 | cross-media 包 | 主代理＋K4 | 否 |
| W4-37 | cross-media workbook §7 逐编号台账只有 1 个占位行（40 个 AD 编号无逐项可填行），且 8 个编号（AD-14、AD-31–33、AD-36–39）在 §4 速查只以区间出现 | 合同 X-2 | `templates/adaptation-workbook.md:53-57`、`SKILL.md:73-96` | W4（与 §三十 占位行待裁同判） | 否 |
| W4-38 | cross-media 有 `templates/` 但按 X-2 现状不进 spec；若采纳编号化模板须先冻结 40 编号全集再补 spec，顺序不可颠倒 | 合同 X-3 | `notes/delivery-preflight-spec/` | 主代理 | 否 |
| W4-39 | `08-adventure-treasure/templates.md:34`「书内规则」＝v3 基线既有、附录 B #4 真命中，G08-a1 移交③与 a2 存疑②同指，改写归属未裁 | G08-a1／a2 | `08-adventure-treasure/templates.md:34` | 主代理（判改写归属）＋K4 | 否 |
| W4-40 | 题材 07 求生红线：v0 含可照做操作细节（造秤与砝码、帆布接雨储水工序），a1 判不落成品；K4 须复测 07 目录（含他席已落文本）是否仍有可照做的现实求生步骤 | G07-a1 存疑 Q1／Q2 | `references/07-survival-disaster/` | K4 | 否 |
| W4-41 | 07 目录 `见、`／`依据`／`出处` 类基线既有命中约 16 处（席位逐处判为词尾假阳性，非本片新文），改写归属未裁，交 P4 或 07 收官席 | G07-a1 移交 T3 | `07-survival-disaster/rules.md` 等 | 主代理＋K4 | 否 |
| W4-42 | 题材 10 跨谱系同号与 r2 错归收口：`02-rulings.md` R1–R16 落进 a1 段 3655–3668、`06` 的 P4／E1–E6 落进 profession 段 3692／3766–3773（字节与原行不符），a1 的 LI-GE-2701 段内 `R16` 与 a2 的 2781／2796 属同一发生；按「行序＋v0 路径」双档合流，行号回置归 K1 下版 | G10-a1 边界／G10-a2 跨席结论 | `raw/...-r2.md` 3614–3984、G10 各席记录 | 主代理（a3／a4／a5 回传后） | 否 |
| W4-43 | 10 目录 v3 基线残留三处真命中（`guide.md:38`「用户明确要求」#11、`competition-and-failure.md:33`「来源是」#4、「更正」#8 两处）＋ #10 类 13 处字节级误报判允许；两席同指、均不代改 | G10-a1 移交／G10-a2 移交⑦ | `10-profession-competition/` | 主代理＋K4 | 否 |
| W4-44 | scene 包三处：状态词四行判据表在 `SKILL.md:253-258` 与 `references/rhythm-diagnosis.md:74-79` 逐字重复（建议 rhythm 侧改引用，保 SKILL 为唯一权威）；53 个编号无逐项可填行；AF-01／AF-09／AF-15 只有交叉引用无卡体，K5 空洞判据须按定义形态取词 | 第四份合同 X-1…X-3 | `scene-conflict-and-rhythm/` | 主代理＋K5（冻结判据） | 否 |

- 计数随之更新：A 表 **28 条**；阻塞 K5 仍为 **9 条＋队列外 2 项＝11**（两条新增均不阻塞）。


- W4-45｜genre-fiction-craft｜`references/10-profession-competition/worksheets-and-cases.md` PR-06A 是「工作表／字段／何时使用」三列思考工具表，无 R18 §2a 要求的「编号独占一行＋值／状态／稿件证据位置」列形。｜裁决二选一：新增 §2a 列形填写表，或在 `delivery-preflight-spec/genre-fiction-craft.md` 记保留理由；与占位行裁项同批裁决。｜阻塞 delivery-preflight-spec 冻结｜来源 G10-a4 移交项 4（15:36）


- W4-46｜character-and-narrative-control｜`SKILL.md:175` 用区间行「TM-06 至 TM-09」承载四张卡，ID 级字面取词在 SKILL 层缺 TM-07／TM-08（卡体在 `references/time-mechanisms.md:63/:69` 均在位）。｜K5 冻结判据须双档回显（卡体档 18/18 vs 索引字面档 16/18）并写明取词范围；是否把区间行拆成逐 ID 行属成品改动，需作者或 G00 裁。｜阻塞 K5 判据口径｜来源 合同 X-3（15:41）
- W4-47｜character-and-narrative-control｜`templates/narrative-workbook.md:3`「按任务只填用得上的那几节」与 `:134`「每个编号独占一行」在同一次交付里存在先后取舍；§1／§3 空值行已判为可填字段（R18 §2a 通过）。｜需在 `delivery-preflight-spec/character-and-narrative-control.md` 记两者适用边界（整册交付 vs 单场交付）。｜阻塞 delivery-preflight-spec 冻结｜来源 合同 X-2（15:41）


- W4-48｜genre-fiction-craft｜`references/10-profession-competition/`（01-scope 谱系件）标题写「入场策略四型」，正文实有 E1–E7 七型（G10-a3 存疑，v0 侧为 0 B 声明行）。｜待裁＝改标题为七型／改正文归并为四型／保留并在题材 guide 注明两层口径；三案代价不同，属成品一致性缺陷。｜阻塞 K5 冻结｜来源 G10-a3（15:46）
- W4-49｜genre-fiction-craft｜G10-a3 判 T6 不恢复，同时声明「如主代理认为需显式句可并入 P12」。｜主代理本轮按席位判定落笔、未并入；若 G00 复核认为该判据需要显式句，走 P12 追加（锚已核）。｜不阻塞｜来源 G10-a3（15:46）
- W4-50｜genre-fiction-craft｜基线残留（v3 既有文本命中附录 B，按 B.2 不代改）清单：`10-profession-competition/` 内 #10c 同型 13 处（a3 报）＋ `guide.md:38`「用户明确要求」＋ `competition-and-failure.md:33`「来源是」＋ `roles-and-recognition.md:15`「蓝花瓶测试」（a5 报）＋ `case-notes.md:20`「分开记录假设与证据。」（a5 P17 锚原文）。｜K5 冻结时须按「新增违规／基线残留」分档回显，并给出处置建议；不在本轮改字。｜阻塞 K5｜来源 G10-a3／a5（15:46）
- W4-51｜genre-fiction-craft｜G10-a5 报段级 343 行 vs 简报声明 336 行，差 7 行不属本片；与 W4-42「r2 错归按双档合流」并案处理。｜待 G00 或主代理按行序＋v0 路径双档归位。｜不阻塞｜来源 G10-a5（15:46）


- W4-52｜genre-fiction-craft｜14 件题材模板**无一具备** R18 §2a 的「编号独占一行＋值／状态／稿件证据位置」列形（宽式实测 ID 独占表行首列合计 189 行、分布在 02/07/08/12/13/14 六件，另 8 件为 0；六件的表头列数为 3 列／4 列／5 列／6 列，均非 §2a 的「值／状态／稿件证据位置」列形；另有 4 件模板的编号整列为空待用户填。初稿误记「14 件全 0」，15:52 更正）。｜裁决二选一：① 把已有 189 行的 6 件表头统一为 §2a 三列形并给另 8 件补行（动 14 件，与各件「按任务选择、不强制填满」声明冲突）；② 按 R18 §6 判 genre 属「无枚举模板」不建 spec 并在 `delivery-preflight-spec/` 索引写理由。与 W4-45（PR-06A 表形）、W4-47（工作表 §3 vs §8 取舍）同批裁决。｜阻塞 22.4 第 4 项（spec 冻结）｜来源 genre 递归复测（15:50）


- W4-53｜scene-conflict-and-rhythm｜「单元」两口径不一致：`SKILL.md:177`（长篇＝章或场景）vs `intensity-and-rhythm.md:11/:28`（场／章／卷／整篇，高潮是全篇标尺）。｜影响 SU-10 强度排布与 SU-02 峰值判定的适用范围；需裁「单元」定义以哪一侧为准，另一侧加限定语。｜来源 K4-r1-scene（非作者，15:56）
- W4-54｜scene-conflict-and-rhythm｜「已发表／已锁定」没有规则句要求先核对这一外部事实，仅 `examples/scene-cases.md:69` 由作者自陈。｜建议在负触发或失败出口处补一句「锁定状态属外部事实，未经作者确认前不得据以改写」；属成品改动，待裁。｜来源 K4-r1-scene
- W4-55｜scene-conflict-and-rhythm｜`SKILL.md:48`「另找资料核实」未写执行者；`agents/openai.yaml:6`「材料不全时给出标明假设的草案」与 `SKILL.md:267`「先要正文」方向相反，包内无优先级声明。｜裁项＝谁负责核实与两者优先级（yaml 入口句 vs SKILL 失败出口）；属成品一致性，待裁。｜来源 K4-r1-scene
- W4-56｜scene-conflict-and-rhythm｜SC-07 长谈三问无「题材信息交代」独立问句，转 `genre-fiction-craft`（`SKILL.md:42`）的交接点靠推断；另：失败出口表双承载（`SKILL.md:264-274` 9 行 vs `rhythm-diagnosis.md:92-100` 7 行）。｜裁项＝是否在 SC-07 加第四问；rhythm 侧失败出口表改引用还是补两行（与 X-1 状态词双承载同族，建议一并处置）。｜来源 K4-r1-scene


- W4-57｜character-and-narrative-control｜`SKILL.md:268` 定义「已完成＝检查已执行且有稿件内可核的证据支持」，但包内唯一完整示范 `examples/pov-cases.md:92` 声明「只有构思，没有正文」，`:110-111` 与交付表 `:136` 仍记「已完成」＋位置「未知」。｜三案：示范改标「依据」或「未能核实」／在 §9.1 加「纯设计交付的『已完成』豁免句并写明边界」／保留并在例五注明为反例。属示范与定义互斥，需作者或 G00 裁。｜阻塞 22.4 第 7 项与 spec 冻结｜来源 K4-r1-character（非作者，15:57）
- W4-58｜character-and-narrative-control｜四词交付状态与五档可信度（`SKILL.md:105`、`boundaries-and-ethics.md:83-91`）并存且无映射，**「超出范围」在四词里没有落位**；导致输入 3（现实健康请求要退出）无状态词可挂。｜建议在 §9.1 加一行映射（超出范围 → 未能核实＋转出说明）或明确两者分层用途；属成品改动，待裁。｜来源 K4-r1-character
- W4-59｜character-and-narrative-control｜全包无「疑似即时危险时如何建议求助」条文（关键词 `热线／急救／紧急／求助／就医／危机` 仅命中 `boundaries-and-ethics.md:14`，而该条是把危机分级划出范围），也缺「怎样识别请求其实是现实健康问题」的前置判据。｜这是安全相邻缺口，建议加：识别句＋一句「不判断严重性、建议由有资格的渠道处理」的固定出口；措辞需作者定，本轮不自拟进成品。｜优先级高于其余 W4 项｜来源 K4-r1-character


- W4-60｜套件（工具侧）｜`scan_dirs.py` 的 `REF` 与参数拼接对「整条相对路径」静默失配，glob 命中 0 文件仍打印「合计 0」并通过正控制判断 ⇒ 任何整目录「零命中」回执在收口前须重跑并回显**输入文件数**（本轮已复现：旧拼法 0／basename 8）。｜K5 判据补一条「扫描类脚本必须断言输入非空」；受影响的既往回执仅 §四十四 一条（已作废），新文体扫描不受影响。｜阻塞 K5｜来源 P4 首跑（16:00）
- W4-61｜套件（工具侧）｜P4 注入型正控制仅覆盖十一类中的 10 类：`#6 英文原句` 要求 `"＋大写开头＋四个以上小写词`，我的合成串用小写开头未命中 ⇒ 该类检测有效性未证，整树 1 命中只作下界。｜收口前补一条符合该模式的正控制并复跑；`line-editing-and-proofreading/references/en-mechanics-and-punctuation.md:92` 是否记 B.2 允许理由一并由 K5 定档。｜阻塞 K5｜来源 P4 首跑（16:00）


- W4-62｜genre-fiction-craft｜F1 合并裁决追记：`ethics-and-interruption.md` 行 11 的 a5-P10 与 a3-P24 已由主代理删除（同一机制由行 9 的 a4-P16 完整承载，实测 −429 B、行数不变）。｜G00 复核两席的 LI-GE 单元应记「合并入 a4-P16」而非丢失；若作者认为三步句过长，改为「行 9 拆两段」方案（代价：段落节奏变）。｜不阻塞｜来源 B3-r1-genre10＋主代理裁决（16:05）
- W4-63｜genre-fiction-craft｜`training-and-systems.md:28`（a3-P18）与 `:33`（a4-P23）跨行写同一机制（上下游同级各撞一次＋低阶岗位改动主线），各自成句、无残片。｜待裁是否合并为一句及保留哪一侧；本席不代改。｜来源 B3-r1-genre10（16:05）
- W4-64｜套件（工具侧）｜落笔守卫 `scan_newtext.py` 的 #4 类模式集只含 `来源是`，不含裸 `来源`／`引文` 全称，导致 B3 抓到的新增违规（F2，`competition-and-failure.md:23`）在落笔时未被拦下。｜收口前把落笔守卫的十一类模式对齐附录 B.1 全 token 表，并对历史 627 条补丁新文复跑一次；复跑结果按「真命中／词尾假阳性」分档回显。｜阻塞 K5 与 P4 收口｜来源 B3-r1-genre10＋主代理复算（16:05）

- W4-65｜story-architecture-and-longform-planning｜本包 `SKILL.md` **未集中定义交付四词**（「未能核实」在 SKILL.md 出现 0 次），四词各自成表散在 9 份 references 与 4 份 templates（字面出现合计 24 处／12 文件），草稿另记「10 处／4 套」。｜裁决＝是否在 `SKILL.md` 增一张统一状态词表并让各表改为引用（与 scene X-1、character X-1 同族，三包对照可给套件级惯例判断）；同时统一「占位行」判据（草稿 30 vs 主代理 67）。｜阻塞 delivery-preflight-spec 冻结与 K5 口径｜来源 主代理采纳注（16:06）


- W4-64（改判，覆盖 16:05 那条）｜套件（工具侧）｜红线 `#4/#9` 类需要**语义判据**而非更宽的字面模式：626 条新文复跑得 19 条裸 `来源`／`出处`／`页码`，逐条为题材内普通名词用法，无一条指向包外出处。落笔守卫的拦截条件改为「同行同时出现书名号／作者／页码引用／`notes/` 路径」才判违规；单凭裸 token 不判（否则误伤 15 条）。｜K5 收口时按此判据复跑 P4 并分档回显｜来源 宽表复跑＋主代理裁决（16:07）
- W4-66｜套件（工具侧）｜宽表正控制中 `原著` 与 `著` 两类零命中（合成串与模式要求行末 `著` 不合），检测有效性未证；连同 W4-61 的 `#6 英文原句`，两类判据在 K5 前须各补一条必命中控制并复跑。｜阻塞 K5｜来源 宽表复跑（16:07）

- W4-67｜套件（管线）｜接行末合并的**锚后缀包含关系**未检查：a3 锚是 a5 锚的后缀，两条各自 grep 命中 1 次通过唯一性，结果背靠背写进同一行末造成三席撞车（他席已在「可能同点清单」预告同源）。｜`append_lineend.py` 落笔前须对同一目标行做「A 锚 endswith B 锚或反之」判定，命中即视为同点、先合并再落；并把该判据写进席位任务书。｜阻塞 K5（管线判据）｜来源 B3 终版（16:11）
- W4-68｜genre-fiction-craft｜台账可检出性例外四条（本席处置造成）：`a1-P03`（来源→来路）、`a3-P24`／`a5-P10`（删除后经合并）、`a4-P16`（并入「当时实际生效」后文本变长）四条新文在成品不可**原样**检出；逐席「99/99 LANDED 命中＝1」自 16:10 起只对 95/99 成立。｜收口对账按「逐席求和 63,555 −399 ＝ 现值 63,156」读；G00 汇总时把这四条记为「主代理处置例外」而非席位漏写，不回改席位回执。｜来源 B3 终版 §9 F5／F6＋本席复测（16:11）
- W4-69｜套件（工具侧）｜`#3 来源数量与年代` 模式 `[0-9]+ ?本(材料|书|手册)` 只认阿拉伯数字，中文数词（`三本材料`／`两篇样本`）不命中；非作者已补跑中文数词型得 0。｜模式集扩为阿拉伯数字＋中文数词两型并复跑全树；连同 W4-61／W4-66 两条未证类一并处理。｜阻塞 K5 与 P4 收口｜来源 B3 终版（16:11）
- W4-67（补记限定）｜守卫输出是**待检清单**不是合并清单：实测 3 对同点中仅 `ethics:11` 为语义重复，`roles:27`／`:33` 两侧各写不同机制，按结构同点删除会误删两席独立知识。第二道判定＝是否同一机制的同一操作步骤，需逐对精读。｜16:12 补记
- W4-70｜story-architecture-and-longform-planning｜`SKILL.md` §10 参考表第 17、19、20、21 行（`:384、:386、:387、:388`）「缺料或冲突出口」列写「同上」：K4 席判为**弱填充**（形式非空、内容需回看上一行）。22.4 第 2 项的两列子句按「非空」判已达标，是否要求逐行独立成句交用户或 G00 裁。改法代价：四行各补一句需回读对应模板与示例文件的实有出口，避免把别的包的出口抄过来。
- W4-71｜套件（口径）｜模板「空行」定义未统一：story 侧三口径并存——席按「整行各格皆空」得 30（3/3/17/7），本席按「ID 行去掉首列后的空数据格」重算得 39（14/17/0/8），本席早前登记的 67（9/9/23/26）**口径已不可复现**。⇒ `delivery-preflight-spec` 与本账中所有「空行数」在冻结前必须写明判据（行级全空／格级空／含占位符三档分列），否则该指标不可跨席比较。本席旧数 67 就地标为「口径未定」，不下结论。
- W4-72｜preset-card-generation｜brief 的 `peer_receiving_refs` 用裸文件名（`SKILL.md:312`、`examples/pov-cases.md:102`、`references/rhythm-diagnosis.md:100`、`examples/scene-cases.md:82`、`examples/worked-example.md:93` 等 19 处）指向别的包，按本包根解址 15 处行号越界、4 处文件不存在。⇒ 跨包引用一律加包名前缀（承 W4-36 与记忆里「裸文件名＋行号不可解址」那条）；本席不改席内容，登记给后续 review 席作判。
- W4-73｜套件（管线）｜brief 冻结时序缺陷两处：preset-card 草案在 16:25 采纳后于 16:29 继续补写（16:31 重采纳，47,609→48,379 B）；story 草案 16:29 才补齐 10 条 gaps，我 16:25 采纳的是 gaps 为空的快照（**待重采纳**）。另本席在采纳后向 fiction-planning `SKILL.md` 插入 1 行，使 19 处 `SKILL.md:>=336` 锚位移，已按插入点精确 +1 修回。⇒ K5 冻结前置两道检查：(a) `brief-draft.json` 的 sha 是否等于采纳件 `draft_source_sha256`；(b) 采纳件锚点对当前成品的行号一致性。顺序原则：**成品改动完成 → 再采纳 brief → 再算 SHA → 再派 review**。
- W4-74｜跨包（状态词权威位）｜状态词四词的**集中定义在 SKILL 层缺失**两处新证：story 侧全文只在 `:385` 表格出口格出现「未知不当成已完成」，「未能核实」「待作者决定」在 SKILL 层 0 命中，含义级定义唯一挂在 `references/serial-platform-migration.md:52`（迁移专用文件）；fiction-planning 侧定义在 `SKILL.md:330-335` 但模板另用第五值（已由本席补句闭合）。与 character 包 X-1（唯一正样本：定义在 `SKILL.md:266-273`）构成三档对照。⇒ 属「同一业务语义只有一个承载处」的跨包一致性问题，改法与落位交用户或 G00 裁，本席不擅自搬表。
- W4-75｜story-architecture-and-longform-planning｜`SKILL.md:385-387` 用区间写法压掉扩展编号族，导致 **PA-02…PA-11（10 个）、ST-02…ST-23（22 个）、DR-02…DR-09（8 个）共 40 个编号在 SKILL 层字面缺位**，`T1–T6`（定义在 `serial-platform-migration.md:7-27`）整族 6 个不出现在 SKILL 层；另 SV-16 在 SKILL §5 无卡体、定义在 `serial-chapters-and-installments.md:54`（包内 32/32 齐）。分档报数 1／40／6，不做单一合计。与 character X-3、scene X-3 同族（索引压缩形态）。
- W4-76｜套件（归属未明）｜preset-card 的 `brief.json` 在 16:25 由本席写入 47,609 B，16:29:26 实测变为 67,385 B，而该席回执声明「未写 brief.json」；16:31 本席按最终草案重采纳得 48,379 B（内容与草案逐字等，缩进不同）。⇒ 67,385 版来源未明；现行采纳件已由本席覆盖为可追溯状态，但该差额（67,385 vs 48,379）与写入者仍待查，不得记为「本席写入」。若并发会话存在，应确认是否有别的实例在写 quality 目录。

- W4-77｜cross-media-drama-adaptation｜状态词集合三处不一：`SKILL.md:204`（四词＋未知）／`templates/interactive-branch-sheet.md:41`（四值）／`templates/adaptation-workbook.md:57`（五值），而判据侧 `references/interactive-adaptation.md` 全文 0 处「未知」⇒ 分支表按判据推不出「未知」。需作者定唯一权威侧。（K4-r1-crossmedia F1；同族 W4-46／character X-1）
- W4-78｜cross-media-drama-adaptation｜同一缺输入项归档相反：`SKILL.md:201` 判「未能核实」（要求检查已执行）vs `references/interactive-adaptation.md:57` 判「待作者决定」，且 interactive `:56` 允许「本轮未执行也记未能核实」⇒ §10 四词表（`SKILL.md:195` 自称唯一）缺「本轮未执行」的档位；`SKILL.md:168` 又把判据让给 interactive。（F2／F3 侧）
- W4-79｜cross-media-drama-adaptation｜`templates/adaptation-workbook.md:53` 声明「每个编号独占一行、三列齐全」，实测表头四列（`:55`）、只有 1 行占位（`:57`），AD 全集 40 编号无逐项行 ⇒ 交付清单 `SKILL.md:67` 的「采用的规则编号」不可逐条落稿。需定占位行是否算可填。（F1b；同族 W4-52）
- W4-80｜cross-media-drama-adaptation｜AD-40 的两项检查（`SKILL.md:189` 节点可达／结局条件可满足／无孤立路线／无解释的状态冲突，`interactive-adaptation.md:50` 同一时点互斥状态）在 `templates/interactive-branch-sheet.md:43-48` 无对应检查行 ⇒ 停下点不可判定，需补行。（F3）
- W4-81｜cross-media-drama-adaptation｜`SKILL.md:54` 把四类复杂取舍交给 `conflicts.md`「五个分歧」，实测五分歧＝披露量 `:5`／快切 `:14`／结尾形态 `:23`／导演示范 `:34`／长度 `:44`，4 类中 3 类无条目（通道互斥也只能自造备忘）。需定是否扩列。（F4）
- W4-82｜cross-media-drama-adaptation｜分支节点编号规则缺失：`interactive-adaptation.md:55` 以「分支表的节点编号」为「依据」档举证坐标，但全包无节点命名／编号／跨路线重编规则（`scenes-and-continuity.md:8` 只覆盖镜头与场次）。（F5）
- W4-83｜cross-media-drama-adaptation｜裁决主体两版：`references/conflicts.md:42`「请导演或作者选择」vs `SKILL.md:202`／`:212` 只承认作者裁决 ⇒ 落到导演时状态词无法归档（全包「导演」8 处无交接档）。（F6）
- W4-84｜cross-media-drama-adaptation｜`SKILL.md:236` 称「转介行与 §12.2 两表互为逆关系」，实测 §12.2 只有两条 bullet（`:231`、`:232`）而无「两表」⇒ 双向自检只覆盖 preset-card 一对，余 5 对无成文接收行。（F7）
- W4-85｜cross-media-drama-adaptation｜音频专属载体的限制全包唯一落点 `references/transferability.md:46`，§4 速查无音频行、§9 互动段不提音频，走 `SKILL.md:182`→interactive 一条路径取不到该限制 ⇒ 用例边界档判**部分 FAIL**（会误判为「音频按通用通道规则即可」）。需定：限制上浮到 §4／§9，还是加转介行。（XQ-K4-09）
- W4-86｜preset-card-generation｜字数带的计量单位未定义：`style.md:101`／`progression.md:125` 给 500-700 与 600-750，`SKILL.md:132`／`card-diagnosis.md:40` 亦引用，但「字」全包零定义且 `card-diagnosis.md:33` 改用「字符」；示例卡实测纯汉字 482／含标点 607／含小节标题 654 ⇒ 三种读法两 PASS 一 FAIL，边界差 7 字。正好命中本包缺陷目录 `card-pitfalls.md:29-33`（「换两个人来数结果是否一致」＝不一致）。需定单位并回改两处。
- W4-87｜preset-card-generation｜`SKILL.md:150`「只用这四个词」与 `:155` 自述相冲（「依据」写明不是固定答案也不是来源背书，属附件而非状态）⇒ 实为三状态＋一附件；另缺记录「为满足宿主格式主动违反本包缺陷目录第 18 条」的降级槽。
- W4-88｜preset-card-generation｜`references/expression.md:95-96`「正文第一句以『正文』二字开头」紧接「正文不超过 300 字」，同一词同时指卡内正文与被辖小说正文 ⇒ 命中本包 `terminology.misused-word`，需改名消歧。
- W4-89｜preset-card-generation｜本包有意无 `templates/`（字段名、顺序、上下限、禁项齐全可产出卡），但下游把「找不到模板」当缺口；建议在 `SKILL.md` §3 明写「不提供空白模板，格式以三处『写成卡』小节为准」。与 P-1／W4-03 同族。
- W4-90｜story-architecture ↔ line-editing｜`story-architecture/SKILL.md:51` 把「翻译」转给 line-editing，而 line-editing `SKILL.md:19-33` 无接或拒翻译的行；`story-architecture/SKILL.md:3` 的 description 未列 line-editing（其余 6 包均列）。另 `preset-card/SKILL.md:199` 把单侧转介缺口自我豁免。⇒ 与 W4-02／W4-19 同批交 G00 处置。
- W4-91｜line-editing-and-proofreading｜英文线编号触达不齐：`SKILL.md:119` 关键词入口只到 EN-28 一类，`workflow.md:45-79` 六轮无 EN-30／EN-16／EN-31／32／33／36／37 的槽位 ⇒ 40 条里 26 条只能靠整读文件触达；中文线规则一律无「出口」字段（`zh-sentence-and-wording.md:89-98` 只有不适用／对应），两侧停下点不对称。
- W4-92｜套件（quality 层）｜`brief.json` 的 LE-T12 正文锚 `en-word-choice-and-concision.md:34`（实为 EN-25 表格行）与其 `anchors` 列的 `en-sentence-revision.md:34`（EN-13）不一致，正文锚不支撑该断言；另 `SKILL.md:175`「（按套件合同）」在包内无定义处，核原文须出包读 `notes/suite-contract.md`（席位禁读）⇒ 建议包内一句定义或改称「§10.1／§10.3 自表」。

- W4-29／W4-33（状态更新，2026-11-05 16:37）｜genre-fiction-craft｜**内容归属已证实销项，执行者身份保持未销**：G07-a3 18/18 与 G11-b3 20/20 整串命中且 v3 基线 0 命中，写入落在 14:54:55 批次，字节算术与两片预期完全闭合（07 +4,657 B／11 +5,913 B）；同族 G03-c1/c2/c3 核对无差额。⇒ K5 阻塞解除。详见 checklist §六十五（含对 §三十二 三处表述的覆盖更正）。取证席为只读、未落盘。

- W4-93｜line-editing-and-proofreading｜全包“”与「」并存 **167 对**（`SKILL.md` 25、`worked-example.md` 31、`workflow.md` 10、四份 en 件 29／21／24／17、`zh-mechanics.md` 1、`zh-sentence-and-wording.md` 0），K4-r2 逐处判为**术语与条目名的 meta 提及**、不与 SR-13 冲突；但本包没有写下这条约定。建议在 `zh-mechanics.md:22` 或 `SKILL.md:102` 加一句「本包用「」标记术语与条目名，稿件引号仍按 SR-13」。需作者定词形。
- W4-94｜line-editing-and-proofreading｜`worked-example.md:109、:110、:113` 用「」引中文稿件片段，同文件 `:27、:28、:34` 用“”引同类片段 ⇒ 同功能两种符号（正文对白 `:11-15`、`:38-42`、`:81` 一律“”，与 SR-13 一致）。属自洽性问题，需作者定是否统一。
- W4-95｜line-editing-and-proofreading｜B.3 待裁项：`worked-example.md:79「每句都更有力」`、`:89「方言和意识流照原样留着」` 与 brief 用例 LE-T3 近逐字对应，**机械规则会判「需重写」**，复验席判为不须重写（故事文本自创、无来源正文）；另该席对「来源侧」骨架相符只能记 NOT_PROVEN 子项（来源原文不在其可读面）。需作者或后续席定档。
- W4-96｜line-editing-and-proofreading｜`zh-mechanics.md:7` 保留 **GB/T 15834-2011／15835-2011** 标准号，同行已写「没有逐条对照标准原文」。附录 B 第 10／18 类的 24 与 16 处命中经逐条判读均指向此语境（无包外出处编号同行共现），判 0 违规；是否应把标准号也一并去引用化，属口径取舍，交作者定。
- W4-97｜套件（判据差异）｜K4 各席的附录 B 均为**自建等价 11 类／18 子模式**（原附录文本在其禁读面），与主代理的 P4 模式集不必然同形；第 17 类「长行>150」在 `LC_ALL=C` 与 `LC_ALL=en_US.UTF-8` 两档差 **280 vs 19**（BSD grep 在 C 档按字节计），该席以 UTF-8 档为准。⇒ 整树 P4 报告必须声明 locale 与两档数字，否则跨席计数不可比（承 W4-61／64）。

- W4-98｜套件（口径更正）｜附录 B 的 B.1 实为 **19 条子模式**，此前全包与 spec 均按「18 条」引用 ⇒ 已按 19 更正并在 `notes/suite-contract.md` §4.2bis 留痕。
- W4-99｜套件（判据缺档）｜六条补档已写入 §4.2bis（#8 `旧例|原例`、#2 标准号式、#3 中文数词、#6 弯引号起点、#5b 排除表、#10 语义判据）⇒ 已修；但**生效需重跑整树**（本席未跑第二遍全树扫描，登记为遗留动作）。
- W4-100｜套件（覆盖诚实线）｜19 条子模式中 **13 条检测有效性未证**（1a、2b、3a、4a、5a、5b、6a、8a、10a–10e），仅 6 条已证且只有 11a 有真实正例 ⇒ P4 报告与任何「附录 B 清零」表述必须带这条限定。**未闭合**：需要真实正例来源或作者确认这些类在本套件不适用。
- W4-101｜genre-fiction-craft ＋ fiction-planning-and-diagnosis｜本轮写入的三行残留已修：`12-children-youth/rules.md:51`「旧例中…」改为不依赖旧例的表述、`01-mystery/motive-and-resolution.md:45`「三段/五死法是原例」改为「只是示例」、`fiction-planning/references/scope-and-conflicts.md:19` 英文原句改中文表述。复测：`旧例|原例` 全包只剩基线 4 处、`probability not called for` **0 命中**。⇒ 已修。
- W4-102｜line-editing-and-proofreading｜P4 新证：`zh-mechanics.md:7`、`SKILL.md:102`、`:106` 含 **GB/T 15834-2011／15835-2011＋国家通用规范汉字表／异形词整理规范／规范现代汉语词典**，属真实包外出处且现判据全不检（补档前）。本席判为**本包主题语料**（标点与字形规范本身是这门手艺的规范对象），保留不动，与 W4-96 一并交作者裁。
- W4-103｜genre-fiction-craft｜基线同档 4 行（`01-mystery/investigation-and-institutions.md:9`、`01-mystery/time-space-impossibility.md:9`、`11-identity-revenge-intrigue/templates-and-examples.md:50`、`:117`）用「旧例／原例」措辞，v3 既有 ⇒ 按 B.2 登记不代改（与 W4-50 同批在册）。
- W4-104｜跨包（待裁 8 行）｜P4 判据外新证：`该书` 2 行、`某书／这部书` 2 行、`谱系` 4 行 ⇒ 需作者定是否属「题材内语义」（本套件多处把「谱系」用作版本血缘术语）；本席不代删。
- W4-105｜套件（工具陷阱）｜`LC_ALL` 未设时 BSD grep 按字节解释中文括号类（121 vs 59、366 vs 224）；UTF-8 下 `grep -oE 'A|B' | sort | uniq -c` 会把不同中文串并组（「书里」被算进「出自」）⇒ **既往走过 `sort|uniq` 的逐 token 回执需重取**，本席的 B.1 逐类计数与 quality 里引用过该口径的行均在待重取范围。

- W4-106｜genre-fiction-craft｜G12-a2 五补丁已落笔并复测：P01/P03/P05（`rules.md` 三处段末行内追加，+798 B／0 行）、P06（`more-examples.md:24` 精确替换去「虎变黄油」「该书」）、P07（`mechanisms.md:22` 补首尾竖线，+4 B，正文一字不动）。P02/P04 由该席自撤（G12-a1 已于 16:50 承接同轴，避免双写）。行数 79/48/42 不变 ⇒ genre brief 的 228 个去重锚仍全部在范围内，但**行内容已变**，凡逐字引用这三行的 brief 条目需内容级复核（不只行号）。
- W4-107｜genre-fiction-craft｜整树 SHA 迁移：`bc6e91756cb13bc2…`（17:01 基线，101 件／1,052,159 B）→ `2b81923927f0067c9c41c2079bbd23851b362a283805bddcebe1539303f583e9`（101 件／1,053,030 B，净 +871 B）。⇒ `/tmp/k5-bindings-2026-11-05.tsv` 的 genre 行已过期，任何 genre review 席必须在**全部剩余处置落笔之后**重算再绑定；其余 7 包未受影响。
- W4-108｜genre-fiction-craft｜「某书」两处判**不改**并留证：`rules.md:7`「不能从某书的出版社自述推定现代孩子能力」、`more-examples.md:24`「不能以某书反例阻止用户选定一种结局」——均为不定指代的反向禁令，无真实书目／编号，与 K4 已认的 `05-science-fiction/examples.md:85` 同档（该席亦判不改）。判据口径：`某书` 属被禁词形，但当该行同时是「不许据此推定」的否定式条款时按 B.2 语义放行。
- W4-109｜genre-fiction-craft｜G12-a2 残留议案 R-01…R-08 **只登记未改**：R-02 本席已修（即 P07）；R-01 `more-examples.md:22` 四版透传残留（该席证 v0 带入、非 v3 回归，A/B/C 三案）；R-03「母牛讲者」；R-04「材料收录完整…」；R-05 `templates.md:31`「来源出处/独立族」；R-06 `mechanisms.md:40` 版本痕迹句；R-07 `mechanisms.md:33` 五个未译英文分类词；R-08 两处个案标记列。该席建议与 R-01 同批裁以免口径分裂 ⇒ 待裁（部分涉作者取舍）。
- W4-110｜genre-fiction-craft｜`mechanisms.md:19`「成人喂鸟或**举枪**是孩子观察到的行为模型」列为**低优先存疑**：句子属观察级、无可照做步骤，但涉未成年人可模仿器具。同段正向防口已由 G12-a1 落在 `rules.md:43`（CY-07 不补写可照做的自救做法）。是否把「举枪」抽象为「危险器具」属内容取舍 ⇒ 交作者。
- W4-111｜genre-fiction-craft｜题材片闭合矩阵守恒（该席实测）：行数 33＋47＋77＋53＝210、单元 1＋47＋77＋50＝175；分歧点在第 4662 行 `P4`（1498 B）是单元行而非表头行（表头在 4660–4661），该席裁定行段并入 a1（4662–4709＝48 行）⇒ 并集闭合；但 a1 侧**决定号仍差 1 条**未落（移交 T6）。
- W4-112｜套件（判据陷阱）｜P07 首落被自写门禁挡住：动作＝「精确替换（子串）」且新文为 `| `＋原行＋` |` 的**包裹式修复**时，「新串不得含旧串」恒不成立 ⇒ 幂等断言须按动作形态分档（包裹式改判「新串命中 0 且 旧串命中 1」），不得对全部精确替换一刀切，否则会误报「无法安全落笔」。
- W4-113｜genre-fiction-craft（**结论冲突，待统一**）｜同 4 行「旧例／原例」（`01-mystery/investigation-and-institutions.md:9`、`01-mystery/time-space-impossibility.md:9`、`11-identity-revenge-intrigue/templates-and-examples.md:50`、`:117`）：W4-103（P4 席）按 B.2「登记不代改」，K4-r1-genre 判「包外残留、GQ4 FAIL 须处置」。⇒ 需裁 B.2 的适用条件（措辞级「原例」指涉是否属被禁来源引用）。本批未动这 4 行。

- W4-114｜genre-fiction-craft ＋ cross-media-drama-adaptation｜K4 的两条单向转介已闭合（主代理落笔）：`genre/SKILL.md` 转给表新增第 7 行「生成或修订推进模式卡、文风卡、表达约束卡，或按推进／文风／表达三轴审章节 → `preset-card-generation`」；`cross-media/SKILL.md` 尾部新增 §12.4 与 genre 的双向两行。复测：`grep -c preset-card-generation genre/SKILL.md`=1（前 0）、`grep -c genre-fiction-craft cross-media/SKILL.md`=3（前 0）。preset-card 侧无需改：其 §9.2 既有接收行「生成／修订／诊断推进模式卡…」「按三轴审章节」已覆盖该请求形。
- W4-115｜套件（SHA 迁移）｜genre 树 `bc6e9175…`→`59ffd6ab…`（101 件／1,053,170 B），genre brief `434bcac0…`→`7872b791…`（锚点位移修复），cross-media 树 `973bda30…`→`77269b54…`（13 件／76,222 B）⇒ **cross-media 的 review-draft 绑定已过期**，采纳前须由席重算并复核 `interfaces[]`；scene／story 两份草稿绑定仍有效；其余 5 包零漂移。绑定表已重算回写 `/tmp/k5-bindings-2026-11-05.tsv`。
- W4-116｜genre-fiction-craft（新证缺陷）｜brief 内 4 个裸 `SKILL.md:NNN` 现指 :148／:189／:290／:308，超出本包 SKILL.md 117 行 ⇒ 该席写的应是他包 SKILL.md 但丢了包名前缀（与 W4-72 裸文件名不可解址同族）。**主代理不代猜解址**：交 genre review 席按条目上下文判定归属后，再由主代理补前缀。
- W4-117｜genre-fiction-craft｜brief 另有 12 处解址失败，形态为 `01-mystery/guide.md`（缺 `references/` 前缀）与 `case-notes.md`／`notes/...` 元数据引用 ⇒ 与 W4-116 同批由席定档；本轮只做行号位移，未动这些串。
- W4-118｜套件（落笔分档）｜落笔是否需修锚取决于**是否增行**：本批 P01/P03/P05/P06/P07＋「19世纪式」共 6 处全为行内型 ⇒ 0 行漂移、锚仍有效；而转给表补 1 行使 genre SKILL.md ≥30 行的锚全体 +1（实测移 175 处）。⇒ 判据应写成两档，不得一律重算或一律不修。

- W4-119｜story-architecture-and-longform-planning（**台账更正**）｜正式合同自 16:06 起只有「§七 主代理采纳注」，§一–§六 正文未落（草稿一直在 `_draft/`）⇒ 该包合同此前按「已交付」计是错的；19:4x 已重建为 §一–§七（57,060 B／126 行，备份 `.note-only-2026-11-05`）。教训：采纳草稿时**必须整件替换正文**，把采纳注追加进一个尚未写入正文的文件，等于交付一节注释。⇒ 后续任何「采纳」验收判据加一条：`^## ` 标题序列须等于草稿标题序列＋采纳注节。
- W4-120｜套件（批次 30 派单实况）｜19:3x–19:4x 九席在跑：GR-1／GR-2／GR-3／GR-4（genre 去来源补丁清单，上一批全被击杀零落盘，任务书首步均要求「盘上实况自判」并声明 `12-children-youth` 三件属禁改）、RV-character／RV-fictionplanning／RV-lineediting／RV-presetcard（K5 review 正式重建，绑定 `/tmp/k5-bindings-2026-11-05.tsv` 实测值，不符须停手）、OC-genre（最后一份运营合同）。待办队列：scene／story 两份 review-draft 待采纳（story 草稿有 7 行非法档 `partial` 须由非作者席改档）、cross-media 草稿因树迁移（`973bda30…`→`77269b54…`）须重绑。

- W4-121｜genre-fiction-craft（**裁定**）｜W4-113 判为**取改案**：「旧例／原例」族所指的那一版例子在包内不存在（GR-2/GR-4 均实测全包该族词命中处无对应正文），B.2「有理由保留」不成立；且本包已有两处同族被代改的先例（`motive-and-resolution.md:45`、`12-children-youth/rules.md:51`，见 W4-101），"登记不代改"不是普适口径。GR-4 席另给一条否证：同一 17 行集合里只有 5 行落在附录 B 正则内，其余 12 行只在语义回读里 ⇒ **两席数的不是同一集合**，这才是分叉根因。本条同时作废 `notes/desourcing-ledger.md:389`／W4-27 那句「『原例：』附录 B 十一类不覆盖」（W4-99 的 #8 补档已覆盖它）。
- W4-122｜genre-fiction-craft｜GR-1 20 条、GR-2 18 条、GR-3 13 条（P14 不执行）、GR-4 存活 4 条＋1 处附行，共 **55 条已落笔，全部行内型、0 行漂移** ⇒ genre brief 的 228 个去重锚无需位移。我实测的逐文件增量与四席各自预测逐项相符（GR-1 +369/+33/+608；GR-2 +803/+1022；GR-3 +975/+410/+75/−3；GR-4 +494/−75/+36），可作落笔正确性的第二证据。GR-4 的 P02/P03/P08/P09 因我并发落 GR-2 而锚 0 作废（该席自己在回传里预警过），未重试。
- W4-123｜genre-fiction-craft（清零复测）｜全包 101 件（正控制断言）复测：`旧例|原例|原案例` **0**、`该书` **0**、`《` **0**、`notes/|inputs/` **0**、Monmouth／Somerset／Sedgemoor／Jeffreys／Bridgewater／Lyme／Hale **各 0**、`天津` 0、`英格兰` 0。保留并给口径：`英国` 2、`滑铁卢` 1、`绸缎` 1、`买办` 1 属公史地名词与行业名，红线对象是**来源指涉**（书名／作者／页码／注号／原例／出处），不是题材内通用史实词；`某书` 2 处为不定指代的反向禁令（承 W4-108）。⇒ 若作者持相反口径，这四行是一行的事。
- W4-124｜genre-fiction-craft（假阳性档）｜`../` 32 处全为包内相对链接（`../NN-x/guide.md`、`../../SKILL.md`），跳出包外实测 0；`出处|参考文献` 9 处与 `页码|第N页` 3 处按 GR-4 的 A.3 账属自创声明／反向禁令档（其三分：外部引用 6／自创声明 7／反向禁令 4，6 行已由本轮补丁吃干净）。⇒ 判据词表命中只作下界，不得当违规数发布（承 W4-100 的 13 条检测有效性未证）。
- W4-125｜genre-fiction-craft（范围外新证）｜`07-survival-disaster/workflow.md:12` 含「所列作品／代表性样本」同形外指，GR-1…4 四席范围均未覆盖 ⇒ 待下一席定向处置；`02-romance/examples.md:108`（绸缎庄／买办）与 `:138`（RO-E10 范式句，GR-1 标「按词面严格式可读成 2/3」）交裁。
- W4-126｜genre-fiction-craft ＋ genre 运营合同｜OC-genre 席交付 `notes/operations-contract/genre-fiction-craft.md`（201 行／46,065 B，§一–§六 齐，末行 `draft-complete genre-fiction-craft-oc`）⇒ **合同 8/8 补齐**。其六问档：Q1–Q5 STATIC_CHECKED、**Q6 FAIL**——`SKILL.md:99-102` 承诺 guide 有「读哪个文件」实测 10/14、「该题材的触发与负触发」**0/14**。这是 genre 唯一还挂着的结构性缺口，两种改法待裁：改 §6 承诺措辞（行内型、不动锚）vs 给 10 篇 guide 补栏目（增行、会位移该文件后续锚）。取数时刻 19:41:22（101 件／8,074 行／1,053,170 B），成品后续已改动 ⇒ §四 数字待按 W4-118 两档复测。
- W4-127｜K5（正式件进度）｜review.json 正式重建 **3/8**：preset-card 132,916 B（GQ1 pass／GQ2 fail／GQ3 fail／GQ4 pass）、line-editing 60,786 B（GQ1 STATIC／GQ2 FAIL／GQ3 NOT_PROVEN／GQ4 STATIC，fail 仅 LQ-R14）、fiction-planning（GQ1 STATIC／GQ2 FAIL／GQ3 FAIL／GQ4 STATIC，52 行＝pass 43／fail 8／not_proven 1）。三份均自数五组条数与 brief 逐组相等并回读可解析。余 5 包：scene／story／cross-media 重派在跑，character 在跑，genre 须等 K4-r2 复验与冻结。
- W4-128｜fiction-planning-and-diagnosis（**Owner 冲突，交作者**）｜RV-fp 实测「类型/题材契约」双 Owner：本包 `SKILL.md:32`、`:147` 把它转给 genre，而 `:213`、`diagnosis.md:309`、`self-check-diagnosis.md:31` 又留在包内，对端 genre `SKILL.md:17` 亦主张同一职责 ⇒ 同一业务语义有两个承载者。修法要选唯一 Owner，属责任归属裁定 ⇒ 交作者（已并入 `notes/user-decisions-2026-11-05.md` 的第 10 条）。
- W4-129｜fiction-planning-and-diagnosis（新证）｜`scope-and-conflicts.md` 一带另有真实人名 `Genette／Booth`（RV-fp 补出，前席未列）⇒ 与 genre 同族的专名清算在 fp 包也有残留；另 `SKILL.md:336` 所称「台账」在包内零对应物，赛道缺项三处分别记 暂定／未定／未知。
- W4-130｜套件（绑定连锁）｜genre 树一路在动：`bc6e9175`（17:01）→`2b819239`→`59ffd6ab`→`54fa7905`→`07d638e5`（20:1x，101 件／1,058,179 B）。凡 `peer_tree_sha256` 指 genre 的 review 行即刻过期：RV-presetcard 的 genre 值（它读到 `59ffd6ab`／1,053,170）与 RV-lineediting（已如实记 1053170→1057703 的时效）都需重绑。⇒ 结构教训：**genre 未定稿前不要派跨包接口的 review**；接口行是跨包耦合点，边改边审必然返工。绑定表 20:1x 已第三次刷新。
- W4-131｜套件（自写工具缺陷两条）｜①落笔器的「任一未决即整批拒绝」判据按全局 report 取数，导致 A 文件的作废项拒写 B 文件的合法补丁（实测只写进 1 个文件，修成逐文件切片后才对）；②作废（锚 0）应属非终态，须与 LANDED/ALREADY 同列可写档，否则并发场景下整批白跑。⇒ 并发落笔期一律带 `--drop-missing` 并按文件切片判拒绝。
- W4-132｜genre-fiction-craft（复验进行中）｜K4-r2-genre 席在跑：只读、非作者、禁读 GR-* 清单与 brief，任务是**否证**主代理的清零宣称（19 子模式两档自跑＋注入型正控制＋B.3 八位点逐处判＋GQ3 三节互逆核对）。我宣称与它宣称不一致处以它的盘上实测为准；它读不到 v0 的一侧只能记 NOT_PROVEN 子项，不得外推。

- W4-133｜preset-card-generation（**主代理归一，非席位过错**）｜该席交付的 review.json 里 gq[] 用了 pass/fail（契约对 GQ1–GQ4 只允许 FAIL/STATIC_CHECKED/NOT_PROVEN，见 v0 骨架与本包 GQ 段），sections[] 的五组状态则合规。133,304 B 文件已做**档名字面归一**（pass→STATIC_CHECKED、fail→FAIL），并在件内加 `gq_status_note` 声明判定与证据未动、sections 未动（写后断言两组状态分布逐值相等）。⇒ 后续 review 席任务书要把 gq 档名与 sections 档名分别写清，别只说「三档」——两组三档的字面集不同。

- W4-134｜character-and-narrative-control｜RV-character 交付正式 `review.json`（91,627 B，20:01:17）。主代理抽查：可解析、五组条数 brief|review ＝15|15 11|11 7|7 8|8 12|12 逐组相等、状态仅三档（pass 45／fail 7／not_proven 1）、gq 档名合规（GQ1 STATIC_CHECKED／GQ2 FAIL／GQ3 FAIL／GQ4 STATIC_CHECKED／GQ5 NOT_PROVEN）、绑定树 `f32f4dca…` 与 tsv 全等、`anchor_census` 480 去重锚＝支撑 477／不支撑 3／无法解址 0、寻址缺陷 3、findings 18、limits 12。⇒ review 正式件 **4/8**。
- W4-135｜套件（决定件增条）｜`notes/user-decisions-2026-11-05.md` 由 9 条增至 **11 条**（8,040 B）：第 10 条＝题材契约唯一 Owner（W4-128），第 11 条＝genre §6 承诺与 guide 栏目 10/14 的两种修法（W4-126）。答复格式已同步为 `1A…11A`。这 11 条未答前，成品仍可能改动 ⇒ SHA 冻结与 genre review 都在其后面。


## 队列新增与更正（追加，2026-11-06；GR-fix 落笔席，依 K4-r2-genre 最小返工集＋在册议案；A.3 只追加，不改历史行）

- W4-125（更正注，原条不改）｜genre-fiction-craft｜原登记落点 `07-survival-disaster/workflow.md:12`「所列作品／代表性样本」同形外指经 K4-r2 与本席先后实测**在盘上不存在**（该文件全文 12 行无 样本／所列／作品／参考 命中；mtime 11-05 14:54 早于登记时点；brief 无锚指向该文件 :12）⇒ **误登记**，非越权写入。同形外指实位为 12 行族（11 个题材 guide 的「案例只是样本」＋`12-children-youth/mechanisms.md:40`「所列案例」），已由 W4-137 定档并落笔。原条后半（`02-romance/examples.md:108`／`:138` 交裁）维持不变。｜来源 K4-r2-genre §5＋GR-fix 落笔席复核（2026-11-06）
- W4-123（补记，不改原条）｜genre-fiction-craft｜保留档「不定指作品指涉」由 2 处补记为 **3 处**：`references/11-identity-revenge-intrigue/disguise-and-reveal.md:31`「不是从某部小说推出的通用法律程序」——反向禁令性质、无真实书目，与 W4-108 已认 2 处「某书」同档，不改字。落点以盘上实测为准在 **11 目录**（派单初拟的 06 目录无 disguise 文件，属笔误，以此为准）。｜来源 K4-r2-genre §4＋GR-fix 落笔席复核（2026-11-06）
- W4-136｜genre-fiction-craft｜裸 `PG`（附录 B #2a 去数字盲区；G11-b1 移交项 5 登记在先、定档失落，W4 队列原无对应条目）落笔清除：`references/11-identity-revenge-intrigue/templates-and-examples.md:5`「不冒充PG原剧情」→「不冒充既有案例的原剧情」（G11-b1 建议句，K4-r2 §7.1 转载），行内型、行数不变。复测：全包裸 `PG`（后无数字）0、`PG[ -]?[0-9]+` 0。⇒ **已修**。｜来源 K4-r2-genre §3.1＋GR-fix 落笔席（2026-11-06）
- W4-137｜genre-fiction-craft｜「案例只是样本」12 行族族级定档（承 GR-4 P06「示例／自创」口径）并落笔：01／03／04／06／07／08／09／10／11／13 十目录 `guide.md:8` 与 05 `guide.md:9`「案例只是样本」→「案例只是示例」（各 1 处，行内型）；`12-children-youth/mechanisms.md:40` 末句「所列案例只适用于明确列出的作品与情节范围。」→「所列案例都是自创示例，只适用于明确写出的情节条件与范围。」14 个落点文件行数改前后逐一相等（锚零位移）。复测：guide 内「案例只是样本」0、「案例只是示例」12（含 14-period-realism GR-4 已改 1）。⇒ **已修**。｜来源 K4-r2-genre §3.2＋GR-fix 落笔席（2026-11-06）
- W4-138｜genre-fiction-craft｜W4-32 议案落地（03-horror）：Y03-2 `testimony-and-information.md:84`「我不是小说家」→「我并非在编故事」、Y03-4 `guide.md:17`「硬规则」→「成文条款」，均已落笔（行内型）；Y03-3 `testimony-and-information.md:126`「本版」实为「文本版本不一」子串、域内语义，判 **B.2 允许不改**（K4-r2 #8a 同判）；**Y03-1「书内」停手记录**：登记 token 在 03 目录 0 命中（:100 现文「作品内页码先后不等于故事内时间」，无 书内 字样；K4-r2 #4a 全包 书内 仅 08 两处），非本席工作期间并发改动（开工指纹与 K4-r2 收工值同），议案目标词形已不在盘 ⇒ 记「已不在，无需改字」。复测：03 目录 书内／小说家／硬规则 0。⇒ **部分落地＋一条停手记录**。｜来源 W4-32／G03-c5 议案＋GR-fix 落笔席（2026-11-06）
- W4-139｜genre-fiction-craft｜W4-43 落地（部分）：`10-profession-competition/guide.md:38`「用户明确要求」→「作者要求」（S03a LI-SC-021 先例措辞，行内型）。同条在册其余残留（`competition-and-failure.md:33`「来源是」、10 目录「更正」两处、`roles-and-recognition.md:15`「蓝花瓶测试」、`case-notes.md:20`）维持 W4-43／W4-50 在册待裁，本席未动。复测：全包「用户明确要求」0、「来源是」1（原位未动）。⇒ **部分落地**。｜来源 W4-43＋GR-fix 落笔席（2026-11-06）

- 计数：队列唯一编号 135 → **139**（无空洞）。本轮六条均不新增阻塞项：成品行内改写已完成、0 行漂移，genre 新树摘要 `ef3668e4ca8c1934d1df98feb828580e3fe7ae53f2127797c95a7595cc38dabc`（101 件／1,058,213 B）待主代理单笔更新绑定表（本席不改 tsv）。
