# S06a2 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S06a2（fiction-planning：v0 `fiction-craft` a2 段 = diagnosis / drafting / planning / examples 四文件）｜代理：Agent 4｜轮次：W3 主体轮第 5 批｜日期：2026-11-05
- 范围：`output/fiction-planning-and-diagnosis/` 全部 27 个文件。本片改写其中 **4 个**：`references/diagnosis.md`（含合同 2.3 #3 的 ：411 替换）、`references/drafting.md`、`references/planning.md`、`examples/planning-cases.md`。其余 23 个：5 个为 S06a1 已修文件（SKILL.md＋四个 rules-*，命中沿用 a1 自检判定），18 个为未动基线文件（命中按归属登记待对应分片）。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目录>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。#6 另加弯引号变体（`“[A-Z][a-z]+( [a-z]+){4,}`）；#9 另加 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 结论：**11 类共 73 条命中；本片落点 4 文件的命中 7 条全部判允许、零违规；其余 66 条按归属登记（a1 已修 5 文件 20 条引用 a1 自检；S06a3 落点 17 条、S06b 落点 6 条、S06c 落点 23 条，待对应分片）**。逐类见下。

## 一、全 11 类复扫计数（本片改写后最终值）

| # | 目标 | 全包命中 | 本片 4 文件 | a1 已修 5 文件（判 allowed） | 待对应分片 |
|---|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 | 0 |
| 2 | 来源编号与残片 | **4** | 0 | 0 | 4（revision.md ×2、scope-and-conflicts.md ×2 → S06a3） |
| 3 | 来源数量与年代 | **3** | 0 | 0 | 3（scope ×2 → S06a3；self-check-modern-and-zh ×1 → S06b） |
| 4 | 指向学习材料的说法 | **3** | 0 | 0 | 3（research-and-verification ×2 → S06c；self-check-character ×1 → S06b） |
| 5a | 作家/大师类词 | **13** | 2（planning ×1、diagnosis ×1，判允许） | 7（rules-revision ×6、SKILL ×1） | 4（scope ×1 → S06a3；rule-examples ×3 → S06a3） |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | 0 | 0 | 0 | 0 |
| 6 | 英文原句（直引号＋弯引号变体） | 0 | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 | 0 |
| 8 | 改动痕迹 | **7** | 0 | 2（SKILL ×2，「文本版本」子串误报） | 5（revision ×1 → S06a3；research ×3 → S06c；self-check-contract ×1 → S06b） |
| 9 | 审计词（含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | **0** | 0 | 0 | 0（基线原命中 diagnosis.md:411 已由本片按合同 2.3 #3 清除） |
| 10 | 删除后的残迹 | **43** | 5（diagnosis ×4、planning-cases ×1，判允许） | 11（SKILL ×5、rules-premise ×3、rules-revision ×3） | 27（rule-examples ×3、revision-sheet ×1、scope ×1、revision ×1 → S06a3；research ×15、reader-feedback ×3 → S06c；self-check-language/contract/character ×3 → S06b） |
| 11 | 分档词和禁用说法（夯／拉完了／硬规则／用户明确要求） | 0 | 0 | 0 | 0 |

合计 **73 条**（4+3+3+13+7+0+43+3 类零命中不计）。与 S06a1 自检的对账：a1 分类明细之和为 74（本片 20＋基线 54），其摘要行的「79/59」与明细之和不符，系汇总行算术 slips；本片复扫逐类计数与 a1 分类明细一致，唯一实质变化是 **#9 由 1→0**（diagnosis.md:411 已替换），供 Agent 1 汇总 ledger 时以本表为准对齐。

## 二、本片 4 文件命中逐条判断（7 条，全部允许）

### #5a（2 条，「大师」）

| 位置 | 原句要点 | 判断 |
|---|---|---|
| `references/planning.md:305` | 例外说不清代价 → 不登记为「有意违反」…不要用「大师也这样」当理由 | 允许。「大师也这样」是 FC-21 例外登记机制**禁止使用**的借口话术（禁令的对象），无具体人物、无作品名、非背书。与 S06a1 selfcheck 第二节 #5a 判法一致（a1 移交节已预先指名本行按该判法处理）。 |
| `references/diagnosis.md:364` | 「好文体」不可立法，不承诺「改了就像某大师」 | 允许。否定式承诺（不承诺达到某大师水平），「某大师」为泛称对象，恰是防止借来源背书的措辞。 |

### #10（5 条，`据[，。；]`／`见[，。；]` 误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `references/diagnosis.md:14` | 据， | 「作证据，但要说明方法」 |
| `references/diagnosis.md:292` | 见。 | 「并让代价可见。」 |
| `references/diagnosis.md:323` | 据； | 「各找证据；无证据」 |
| `references/diagnosis.md:393` | 据。 | 「先找文本证据。」 |
| `examples/planning-cases.md:3` | 据。 | 「演示用虚构数据。」 |

全部是完整句、主语明确、语义通顺的正常词（证据/可见/数据），不是删除来源后悬空的「见／据」。允许。`（\s*）`、`\(\s*\)`、`与\s*同` 三个子模式在本片 4 文件零命中。

## 三、B.2 允许情形（本片 4 文件层面）

- **本包内部编号**：FC-01–21、S1–S9、DR-01–12/DR-SUM、SP-01–12、NP-01–14、RV-01–12、L0–L4、K-15/K-16（指向包内 scope-and-conflicts §2）、字段名 `切换账本` 四格（trigger/benefit/marker/cost）。符合 B.2 第 3 条。
- **用户稿件版本号**：`draft-v3`（示范 3 DR-02）、`serial-v1/v2-outline/v2/v3`（示范 4 RV-02/RV-11）——均为示例中作者稿件的版本，非本包版本。符合 B.2 第 2 条（B.2 原文即以 `draft-v3`、`serial-v2-outline` 为例）。
- **示例中的年份**：示范 1「凌晨两点」、示范 2「1976 年／2024 年」——演示用虚构设定（v0 头部即明示），非来源年代（#3 正则未命中；`1976`/`2024` 不落在 `(1[5-9]|20)[0-9]{2}` 的市场/手册/杂志/出版/建议语境）。
- **自建示例声明**：planning-cases 头部「人物、情节、字数均为演示用虚构数据」「不是真实客户稿、不是真实运行记录」——规范性禁令与免责声明，不指向学习材料。
- **「设计示例（编写的示范）」**：中文术语，英文审计词 DESIGN_EXAMPLE 已在 v2/v3 改题时消失（#9 零命中佐证）。
- **示范 4「该类型超出本 Skill 已核对证据的覆盖」**：本片由「超出 28 本证据覆盖」改来（LI-FP-059）——「来源篇数→覆盖范围」的通用化改写，无数字、无「本/材料/书」指涉。

## 四、B.3 人工判断（逐文件回读本片改写的 4 份文件）

1. **与 v0 来源案例的骨架比对**：本片**没有新增自创例**——全部改动为（a）残留清除 10 处（艺名、作品人物名、来源篇数、漏译残词、年代指涉、空格残迹），（b）合同 ：411 替换，（c）「picaresque/tale→流浪汉式」与「28 本→已核对证据」两处通用化改写。无新人物、新地点、新事件、新年代进入成品。planning-cases 四个示范是 v0 自带的演示用虚构数据（v0 头部明示，经 v1/v2/v3 逐轮沿用），不属「v0 来源案例」（即 28 本学习材料中的真实作品案例）；与任何真实作品就「人物关系＋关键事件＋时代地点」做两项以上比对均对不上（护士/信/锁、双时间线纸样、侦探中段塌、超长连载删减均为通用创作情境）。
2. **具体作品的标志性情节元素**：v3 基线残留的 Oedipus（diagnosis §9）已删；复扫确认「命运/天意」句保留通用判断后语义完整。#1/#5b 零命中佐证无书名、无人名残留。
3. **借来源背书的说法**：回读四文件无「经典做法是……」「很多名作都……」式句子；两处「大师」均为禁令对象/否定式承诺（见第二节）；「28 本证据覆盖」改为覆盖范围表述后无背书语义。
4. **删除来源后语义**：diff 逐处复查（10/2/6/12 行变更，共 15 处编辑点）无主语悬空、无空括号、无表格空列；「（如 Oedipus）」删除后「除非前文已建立命运框架」句意完整；「picaresque/tale」改写后分支 C 与「改验每站是否改变主角处境」衔接通顺；:411 新句与三问回归节、SKILL.md §9 四词口径一致。
5. **全包辅助复扫**：来源特征词（行号 `L[0-9]{3,5}`、`kd32`、`ledger`、Gutenberg、公版、英译、`source-index`、`version-and-provenance`）全目录零命中；`28 本`、`Oedipus`、`picaresque`、`历史默认`、`hierarchy` 在本片 4 文件复扫零命中。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 合同 2.3 #3 复扫（#9 全模式＋PASS/FAIL/BLOCKED/NOT_APPLICABLE） | 全包零命中；:411 现文为四词口径、无状态码清单、无「中文五态」联动句、回执统一一份（同一份回执的留底字段） |
| 改动痕迹（#8 全模式＋补回/续排/编号续排/上一版/融合版） | 本片 4 文件零命中；无「本版补回」类自述 |
| 四词状态词 | :411 使用「已完成/依据/未能核实/待作者决定」并锚定 SKILL.md §9；「未证实」（诊断/起草/示例的效果免责声明）为包内既有通用措辞（a1 在 FC-17 适用范围同样保留），不属交付状态词，不改 |
| 相对链接 | 本片 4 文件 `](...)` 引用（SKILL.md、templates/*、references/*）未触碰、全部可解析；本片编辑未增删链接 |
| GFM 表格分隔行 | 本片编辑涉及的表（diagnosis §1/§2、planning §0/§10/§11、planning-cases 三张判断表）分隔行均在；全包逐表复核无「有数据行缺分隔行」 |
| 写入范围 | 本片仅改 4 个文件（diff vs v3 共 15 处编辑点：diagnosis 5、drafting 1、planning 3、planning-cases 6）；未动 a1 的 5 文件、a3 范围文件、S06b/S06c 落点、`skills/` 本体、git 历史、log.md、checklist.md、raw 表、desourcing-ledger.md、suite-contract.md、slice-prep.md |

## 六、待对应分片处理的登记（本片未动的命中，按归属）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `references/revision.md`（S06a3） | #2 ×2（:123 `-1328`、:169 `-3143`）；#8 ×1（:151「上一版」，用户稿件版本语境方向）；#10 ×1 | 沿用 a1 selfcheck 第六节登记 |
| `references/scope-and-conflicts.md`（S06a3） | #2 ×2（:74/:76）；#3 ×2（:74「1890 年代英国市场」、:75「1911 年前的手册、1900 年的杂志分类」）；#5a ×1（:140「大师这样做」禁令对象，允许）；#10 ×1 | 沿用 a1 登记；另见本片 LI-FP-048 对 r2 `K-16` 行计量假象的核实结论（勿按 SHRUNK;BLOCK_LOST 补内容） |
| `examples/rule-examples.md`（S06a3） | #5a ×3（:151–153）；#10 ×3 | 「大师」为示范中泛称（a1 预判允许）；文件头「见FC 规则的正文」空格残迹与本片同款，a3 顺手修 |
| `templates/revision-sheet.md`（S06a3） | #10 ×1 | 读原句判误报 |
| `references/research-and-verification.md`（S06c） | #4 ×2（:121/:142，核验语境 B.2 第 5 条方向）；#8 ×3（:48/:52/:192）；#10 ×15 | 沿用 a1 登记 |
| `references/reader-feedback.md`（S06c） | #10 ×3 | 读原句判误报 |
| `references/self-check-modern-and-zh.md`（S06b） | #3 ×1（:32「1884 年的出版建议」） | **本片已核实谱系**：该文件按 CL 编号对齐 v0 `fiction-craft-and-language`（r2 modern-and-zh 两行），归 S06b，非 a2 段 |
| `references/self-check-character.md`（S06b） | #4 ×1（:55「出自」子串误报）；#10 ×1 | 沿用 a1 登记 |
| `references/self-check-contract.md`（S06b） | #8 ×1（:75，用户稿件版本语境）；#10 ×1 | 沿用 a1 登记 |
| `references/self-check-language.md`（S06b） | #10 ×1 | 读原句判误报 |

（a1 已修 5 文件的 19 条命中——#5a ×7、#8 ×2、#10 ×11——判定沿用 `s06a1-desourcing-selfcheck.md` 第二节，本片未改动该 5 文件，diff 复核为零变化。）

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S06a2／fiction-planning-and-diagnosis：附录 B 全 11 类正则（#6 含弯引号变体、#9 含 PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫）＋ B.3 人工判断已跑完，范围 `output/fiction-planning-and-diagnosis/` 全部 27 文件。全包 73 条命中：#1/#5b/#6/#7/#9/#11 零命中；#2=4、#3=3、#4=3、#5a=13、#8=7、#10=43。本片落点 4 文件（diagnosis/drafting/planning/planning-cases）命中 7 条，逐条判允许、零违规（「大师」2 条为禁令对象/否定式承诺；「据/见」5 条为证据/可见/数据类正常词误报）。本片清除残留 10 处：英文艺名 picaresque/tale、作品人物名 Oedipus、来源篇数「28 本证据」、漏译残词 hierarchy、年代指涉「历史默认」、「不把 评论」空格残迹、文件头「见FC/只在FC」空格 ×3、译名间距残迹 5 处；并按合同 2.3 #3 完成 diagnosis.md:411 替换（四词、删状态码清单、删「中文五态」联动句、回执统一一份），**#9 复扫全包零命中**。r2 `K-16` 行经核实为脚本按 ID 去重的计量假象（v0 量 drafting §7、v2/v3 量 scope §2 表行），无真实丢失。基线其余命中 66 条按归属登记（S06a3 17、S06b 6、S06c 23、a1 已修 5 文件 20 条沿用其自检判定），本片未动。B.3 逐文件回读本片 4 份：无新增自创例、无背书、无残迹；相对链接与表格分隔行完好。**本片落点零违规，可交 W4 独立隔离回读。**
