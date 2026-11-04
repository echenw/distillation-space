# 06 · 单源索引、REJECT / UNRESOLVED 与证据边界

返回 [SKILL.md](../SKILL.md) · [01](01-mechanics-and-punctuation.md) · [02](02-sentence-revision.md) · [03](03-paragraph-and-emphasis.md) · [04](04-word-choice-and-concision.md) · [05](05-workflow-and-failure-modes.md) · 示例 [worked-example](../examples/worked-example.md)

**本文件是索引与边界说明，不是规则文件**。规则卡在 01–05；这里只回答：每条规则从哪来、哪条被拒绝、哪条未决、哪些是 1918 过时项、哪些本轮没有证明。为避免重复计数，本文件不设 `R13-CLAIM` 锚点；所有 claim 锚点都在 01–05 的规则卡上。

## 1. 唯一来源身份

| 项 | 值 | 证据/说明 |
|---|---|---|
| source_id | `PG37134` | manifest 中唯一来源 |
| 作者 | William Strunk, Jr. | 扉页 L28–35 |
| 书名 | *The Elements of Style* | L28 |
| 版本线索 | 版权 1918、1919（作者）；1920（Harcourt, Brace and Howe） | L41–45；**版次沿革 `NOT_PROVEN`** |
| 出版地/社（扉页） | New York / Harcourt, Brace and Company | L37–38；与 1920 版权行社名不一致，属印本组合线索 |
| 文件 | PG37134《The Elements of Style》固定转录阅读版；用下列SHA与原文行号回查 | 单源全文 |
| 字符数 | 86,114 | 原Skill记录，数值不构成效果证据 |
| 行数 | 2,369 | `wc -l`；书末更正表 L2339–2369 |
| o200k token | 19,842 | manifest |
| SHA-256 | `c250e04d20dea1bd0312fbbeb9fe71faa3b83396389ab4f7c1ca5d0dee1409e9` | 固定源版本的内容摘要 |
| manifest 状态 | `FULL_TEXT_VERIFIED` | 单源全文 |
| 证据族 | **1** | 5 位 reader 是 5 个透镜，不是 5 份独立来源 |
| 覆盖率 | **100%**（单源全文） | 不代表现代语料覆盖 |
| 现代适用性 | **全部 `H/NOT_PROVEN`** | 本轮未用现代语料/外部风格指南取证 |
| 身份边界 | 不是 Strunk & White（1959）；不是现代风格权威；不是多来源共识 | 书内无 White 修订、无版次说明 |

**引用写法**：`Strunk 1920 印本（PG37134 转录）`。不写“初版”“第一版”“Strunk & White”。书内没有版次说明，扉页社名与版权行社名不一致只能证明印本组合，不能编写版次史。

**两个引用注意**：Rule 10 含 George McLane Wood *Suggestions to Authors* 的材料（L140–141），引用 Rule 10 时不把每一句都归给 Strunk；L125–127 的 “nineteen sentences out of twenty” 是 `in the belief`，是作者信念，不是语料统计，不得写成覆盖率或效应量。

**转录中介**：PG 转录保留原书拼写/连字符不一致（L11–23）；书末更正表实际是 **9 对**（L2342–2367），不是 10 条。任何“见 Rule N”的交叉引用都要回查正文，例如 L1101 已由转录者改为 “Rule 9”，原书行在 L2348–2349。

## 2. 规则 → 行号索引

计数口径：**29 条书内规则卡（C01–C29）+ 9 条流程/裁决卡（C30–C38，全部 `H`）= 38 个 claim**。`F` = 书内明说；`P` = 书中直接给出的动作/判据；`H` = 本 Skill 的编排/迁移；`NOT_PROVEN` = 书内无法验证或本轮未取证；`UNRESOLVED` = 条件区分后仍不能同时满足；`REJECT` = 不得作为现代规则。

| ID | 规则 | 文件 | PG37134 行号 | 书内条目 | 身份/裁决 |
|---|---|---|---|---|---|
| C01 | 插入语逗号成对 | 01 | L220–244 | Rule 3 | `F + P`；ADOPT（F03） |
| C02 | 限制/非限制关系从句 | 01 | L261–298 | Rule 3 | `F + P`；ADOPT（F03）；`which/that` 分工为 `H` |
| C03 | 逗号粘连 | 01 | L388–441 | Rule 5 | `F + P`；ADOPT（F04） |
| C04 | 句子碎片 | 01 | L444–464 | Rule 6 | `F + P`；ADOPT（F04） |
| C05 | 并列从句前的逗号 | 01 | L315–385 | Rule 4 | `F + P`；ADOPT（F04） |
| C06 | 单数所有格 | 01 | L173–198 | Rule 1 | `F + H`；CONDITIONAL（F02）；现代体例 `NOT_PROVEN` |
| C07 | 系列逗号 | 01 | L201–217 | Rule 2 | `F + H`；CONDITIONAL（F02）；现代体例 `NOT_PROVEN` |
| C08 | 括号的标点 | 01 | L1384–1397 | Ch. IV | `F + P`；CONDITIONAL（F13） |
| C09 | 引号按语法角色 | 01 | L1399–1433 | Ch. IV | `F + P`；CONDITIONAL（F13） |
| C10 | 拼写与连字符 | 01 | L2104–2105、L2116–2122、L2193–2195、L2197–2201 | Ch. VI | `F + H`；CONDITIONAL（F16）；1918 形式 `REJECT as modern rule` |
| C11 | 句首修饰语主语匹配 | 02 | L471–513 | Rule 7 | `F + P`；ADOPT（F05）；绝对结构边界 `H/NOT_PROVEN` |
| C12 | 双重被动去嵌套 | 02 | L744–755 | Rule 10 | `F + P`；CONDITIONAL（F07 子规则） |
| C13 | 按段落主语选语态 | 02 | L711–742、L757–771、L776–781 | Rule 10 | `F + H`；CONDITIONAL（F07 子规则）；标题按正文明确例外解释 |
| C14 | 肯定式但不改强度 | 02 | L800–858 | Rule 11 | `F + H`；CONDITIONAL（F08）；第三例 `UNVERIFIABLE` |
| C15 | 平行结构 | 02 | L1088–1161 | Rule 15 | `F + P`；ADOPT（F10）；bullet 应用 `H` |
| C16 | 相关词靠近与 `only/not/all` 辖域 | 02 | L1164–1253 | Rule 16 | `F + P`；CONDITIONAL（F11 子规则） |
| C17 | 句末强调 | 02 | L1303–1322、L1338–1361 | Rule 18 | `F + H`；CONDITIONAL（F11 子规则）；段末按C22条件选择 |
| C18 | 摘要时态 | 02 | L1256–1286 | Rule 17 | `F + H`；CONDITIONAL（F12）；现代领域惯例 `NOT_PROVEN` |
| C19 | 松散句连排 | 02 | L1051–1085 | Rule 14 | `F + H`；CONDITIONAL（F09）；3+ 阈值为 `H` |
| C20 | 一段一题 | 03 | L521–536、L538–579 | Rule 8 | `F + P`；CONDITIONAL（F06）；网页短段 `H` |
| C21 | 主题句默认，不是通例 | 03 | L593–608、L684–708 | Rule 9 | `F + H`；CONDITIONAL（F06） |
| C22 | 段末回扣 vs 新意 | 03 | L593–594、L607–611 对 L1320–1322、L1359–1361 | Rule 9 vs 18 | F（原文）+H（条件整合）；实际相斥时才未决 |
| C23 | 单句段与过渡句 | 03 | L581–585、L613–620 | Rule 8/9 | `F + H`；CONDITIONAL（F06） |
| C24 | 对白分段 | 03 | L587–590 | Rule 8 | `F + H`；CONDITIONAL（F06）；现代小说细节 `NOT_PROVEN` |
| C25 | 删无需之词，不是越短越好 | 04 | L946–953、L1028–1048 | Rule 13 | `F + P`；CONDITIONAL（F09） |
| C26 | 固定冗语可改但要复检 | 04 | L955–1022 | Rule 13 | `F + H`；CONDITIONAL（F09）；`every sentence` 绝对条款不采纳 |
| C27 | 具体、确定、具象 | 04 | L861–864、L909–922 | Rule 12 | `F + H`；CONDITIONAL（F09）；`significant` 判定为 `H` |
| C28 | 套话整句重写 | 04 | L1506–1519、L1836–1848 | Ch. V | `F + H`；CONDITIONAL（F14） |
| C29 | 1918 词表：历史记录 | 04 | L1615–2201 选段（见 §5） | Ch. V/VI | `F + REJECT as modern rule + H/NOT_PROVEN` |
| C30 | R0 范围冻结与台账 | 05 | L119–136、L159–165（仅锚点） | Intro | `F`（范围）+ `H`（流程） |
| C31 | R1 段落层 | 05 | L521–590、L593–611、L684–708（锚点） | Rules 8–9 | `F + P` + `H`（编排） |
| C32 | R2 句法层 | 05 | L220–312、L315–468、L471–513（锚点） | Rules 2–7 | `F + P` + `H`（编排） |
| C33 | R3 简洁层 | 05 | L946–1048、L1051–1085（锚点） | Rules 13–14 | `F + P` + `H`（编排） |
| C34 | R4 用词层 | 05 | L861–922、L1503–1519（锚点） | Rules 12–13 + Ch. V | `F + P` + `H`（编排） |
| C35 | R5 标点/机械层 | 05 | L173–217、L1366–1498、L2101–2201（锚点） | Rules 1–6 + Ch. IV/VI | `F + P` + `H` + `H/NOT_PROVEN` |
| C36 | R6 誊清与复核 | 05 | L466–468（仅类比，不是流程） | 无 | `H` |
| C37 | 条件裁决与局部待决 | 05 | L593–611 对 L1359–1361；L711–742 对 L746–752；L821–823 | Rules 9/10/11/18 | F（来源）+H（条件裁决）；实际冲突为UNRESOLVED |
| C38 | 七种失败出口 | 05 | L119–133、L225、L435–441、L457–464、L589–590、L1457、L2104–2105（锚点） | Intro / Ch. III/IV/VI | `F`（边界）+ `H`（出口编排） |

**行号阅读法**：`Lxxx–Lyyy` 是 PG37134 转录本的行号，不是原书页码。引文必须 ≤25 words；本 Skill 的规则卡只给短句或短例，不整段抄书。原书页码/版次/52 页推断均不作为证据。

## 3. 十条 REJECT 命题（不得写成硬规则）

以下十条是从 16 个规则族中明确拒绝的“常见误读”。它们不得以“Strunk 说必须”的形式进入 Skill；只能作为历史记录、房规选项，或反面教材。

| # | REJECT 命题 | 书内反证/边界 | 本 Skill 的处理 |
|---|---|---|---|
| 1 | “所有被动都错 / 禁用被动 / 被动句计数扣分” | 被动 `frequently convenient and sometimes necessary`（L729–731）；双重被动的“改正”仍是被动（L746–752） | C12/C13 只做去嵌套与按段落主语选语态；C37依明确例外和实际语义判断 |
| 2 | “所有句子都必须短 / 每句不超过 N 词” | 书明说不是要求所有句子都短（L951–953） | C25/C33 只删不承载意义的词；不设词数上限 |
| 3 | “必须避免分裂不定式” | 书自认有 14 世纪先例，只是 `in disfavor`（L1955–1962） | C29 列为 1918 偏好，`REJECT as modern rule` |
| 4 | “所有否定都必须改成肯定 / hedging 一律是 evasion” | Rule 11 是 `as a rule`；第三例自认只是 guess（L821–823）；`not X, but Y` 很强（L850–854） | C14 只在不改强度且原文蕴含时替换；否则保留并标 query |
| 5 | “每段都必须有主题句” | 叙事/描写可无主题句（L684–708）；`As a rule`（L593） | C21 只对说明/论辩默认；叙事不强制 |
| 6 | “具体 = 细节越多越好” | 书要 `all the significant details`，不是 every detail（L915–918） | C27 只加能改变读者图像且原文支持的细节 |
| 7 | “简洁 = 越短越好” | 书明说不是所有句子都短、不是所有细节都删（L951–953） | C25/C33 以“每个词都起作用”为标准 |
| 8 | “套话用同义词替换即可” | Chapter V 要求整句 recast（L1516–1518） | C28 先分档，再整句重写；禁止 one-word substitution |
| 9 | “1918 的 shall/will、data 复数、单数 they、to-day、any one 等是现代硬规则” | Chapter V/VI 是 1918 用法记录；拼写靠 general agreement（L2104–2105） | C29 整体 `REJECT as modern rule`；只作历史/房规选项 |
| 10 | “段末必须回扣开头”或“段末必须放新意”作为唯一规则 | Rule 9 与 Rule 18 两说并存（L593–611 对 L1359–1361） | C22先分主题关系；目标实际相斥时由C37处理 |

**补充禁止**：不得把“多来源支持/多书共识/多方证据”写进本 Skill。证据族 = 1；5 位 reader 读的是同一本书，一致不等于独立佐证。不得把 S3 的 R0–R7 写成“Strunk 的校对流程”；流程是 `H` 编排。不得把 S4 的 AP/Chicago/APA/MLA 比较写成书内 `F`；本轮未核验，统一 `H/NOT_PROVEN`。

## 4. 两组条件已核对，避免伪冲突

U1：主题内的重要后果可同时满足段末主题统一与末位强调，详C22；无关新主题不因“新意”获得放在段末的许可。叙事或有意转向按作者目的处理。

U2：L729–742明确允许且有时要求被动，标题Use the active voice是默认倾向，不是绝对禁令。没有可计算公式不是冲突证据；以原稿主题和主语选语态。

次级张力保留：周期句例外L1191–1193按节奏/强调目的使用；L1327–1331的长句不能被简洁原则无条件砍短；删by me前须检验施事能否从上下文唯一恢复（L721–727）。

## 5. 历史词表的唯一规则落点

完整十二项条目、各自原文行号、适用条件、反例和处理统一见[用词参考C29](04-word-choice-and-concision.md#c29--1918-词表历史记录不是现代硬规则)。本索引不重复维护第二张表。不以历史泛用he抹除用户确定的代词或性别指称。

## 6. UNVERIFIABLE / 本轮更正项

本节把“书内无法验证”“本轮未取证”“审计发现引用错误”分开，避免把 NOT_PROVEN 伪装成已证。

| 项 | 状态 | 事实 | 本 Skill 的处理 |
|---|---|---|---|
| **EV-S1-013 行号** | 审计 `MISMATCH`（任务清单称 UNVERIFIABLE） | 引文 “Use the word not as a means of denial or in antithesis, never as a means of evasion.” 文本逐字正确，但实际在 **L803–804**，不是 L802；L802 是 “Make definite assertions…” | 本 Skill 引用 Rule 11 时用 L800–858 / L803–804；**不引用 L802** |
| **EV-S5-002 更正表数量** | 审计 `MISMATCH`（任务清单称 UNVERIFIABLE） | 书末更正表实际是 **9 对**（L2342–2367），不是 10 条；引文 “including inconsistencies in spelling and hyphenation” 本身正确 | 本文件与 SKILL 一律写 **9 对**；不写“10 条/至少 10 处” |
| EV-S1-022 | `UNVERIFIABLE` | 仅核了 L1373 数字句；书名、移行细节未逐条复核 | 01 的 C10 只把移行列为“Markdown/网页不适用”；不细引未核条目 |
| EV-S2-033 | `UNVERIFIABLE` | 书末练习无答案键；不能核“标准答案” | 不把练习答案当证据；不虚构答案 |
| EV-S4-040 | `UNVERIFIABLE` | 1918 标题/引注排版细节未逐条复核 | 01 的 C08/C09 只保留括号/引文的角色逻辑；排版细节不写成规则 |
| EV-S5-021 | `UNVERIFIABLE` | 未逐字核对 L1191–1193 周期句例外 | C16 把周期句当“书内例外”的 `H` 提示，不细引未核句 |
| Rule 11 第三例 | `UNVERIFIABLE` | 书自认改写 `simply a guess at the writer's intention`（L821–823） | C14 只把它当反例，不当“标准改写” |
| “nearly all careful writers” | `NOT_PROVEN` | 书内无统计/语料证据 | C29 明写 `nearly all` 未证；不写成统计事实 |
| 版次/52 页 | `NOT_PROVEN` | 版权页只能证明 1920 印本组合；页码是目次推断 | 不写“初版/第一版/52 页已证” |
| GQ5 真实任务 | `NOT_PROVEN` | 原Skill历史记录未用真实客户稿跑完整流程 | 本包示例仍为DESIGN_EXAMPLE；本次独立任务证据另存最终审核，不继承旧结果 |

**另外两处跨行引文的小问题**（审计 §5.2）：EV-S1-021 的引文实际跨 L1387–1388，EV-S5-020 跨 L1099–1100。本 Skill 不依赖这两个单行号；如引用则用跨行范围。

## 7. 证据与效果边界

来源族只有一本书。旧稿记录的五位reader、157张卡、16个族及全文覆盖属于历史过程，已独立归档，不能当作本轮独立来源或真实效果。本轮完整读了原Skill全部文件和不同历史版本的差异，并定向回查上述条件原文；不宣称本轮又通读整本原书。现代房规与模型实际效果需对应证据，未核验为NOT_PROVEN。

## 8. 引用合同

1. **每条 finding 带 ID 与行号**：`Cxx` + `PG37134 Lxxx`。没有行号的建议，标“书外-人工”。
2. **区分身份**：`F` 书内明说；`P` 书中直接动作；`H` 本 Skill 编排/迁移；`NOT_PROVEN` 书内无法验证或本轮未取证；`UNRESOLVED` 书内冲突；`REJECT` 不得作现代规则。
3. **引文 ≤25 words**：只引能核对规则的短句；不整段抄书，不用长引文代替分析。
4. **单源措辞**：写“PG37134 说/书内说”，不写“多来源共识/多方证据/研究表明”。
5. **不把 1918 写成现代**：Chapter V/VI 的用法条目只作历史记录；除非房规明确要求，否则按当代词典/项目体例。
6. **不把流程写成原文**：R0–R6、失败出口、finding 台账都是 `H`；书内没有校对流程专章。
7. **不把示例当验证**：`examples/worked-example.md` 的两个 `DESIGN_EXAMPLE` 只演示用法，不是 GQ5 运行结果。

## 9. 本索引不声称什么

- 不声称“现代英语唯一正确”。
- 不声称“多来源共识”或“多书互证”。
- 不声称“小说叙事技巧”——本书没有情节、人物、视角、场景、对话内容的系统规则。
- 不声称“Strunk & White”——这是 1918/1920 Strunk 原书，不是 1959 修订版。
- 不声称“自动化/评分/批量改稿”——本 Skill 是人工编辑工作流。
- 本索引与示例不证明运行效果；以当前最终版独立任务回执为准。
