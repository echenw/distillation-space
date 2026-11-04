# 05 来源索引、族去重与历史规则裁决

返回 [SKILL](../SKILL.md)。本文件是来源核对与规则裁决的落点：任何规则主张都要能在这里找到"哪一本、哪一行、属哪一族"。

## 1. 24 本逐本定位（行数 = `整本阅读版.txt` 实际行数；SHA-256 前 16 位）

| PG | 作品 | 行数 | SHA-256(16) | 族 | 主要支撑的规则 |
|---|---|---|---|---|---|
| PG1026 | The Diary of a Nobody（Grossmith） | 4286 | f08ccd515e43b99d | Grossmith | M1、M6 |
| PG119 | A Tramp Abroad（Twain） | 16947 | 28684a8d55110c67 | Twain-A | M4、M12③ |
| PG1696 | The Club of Queer Trades（Chesterton） | 5027 | ce4b59ca07febcdc | Chesterton-1 | M10、M7、S1(例证) |
| PG2042 | Something New（Wodehouse） | 10008 | cd8f99cc87e4d667 | Wodehouse | M3、M4、M12① |
| PG2233 | A Damsel in Distress（Wodehouse） | 10315 | 28d870c2805ebd74 | Wodehouse | M4、M6、M11、M12② |
| PG28149 | Her Ladyship's Elephant | 5634 | cd989dd096d3bb59 | 单列 | M10、M2 |
| PG30343 | A Discourse concerning Ridicule and Irony (1729) | 3265 | ace0cde13bceb605 | 理论 | S1（唯一理论来源） |
| PG308 | Three Men in a Boat（Jerome） | 7396 | 64828bd3a254461d | Jerome | M1、M3 |
| PG3189 | Sketches New and Old（Twain） | 10332 | 34bc5493778e26d3 | Twain-B | M2、M3、M5、M6、M9、M11、M12② |
| PG4558 | Barry Lyndon（Thackeray） | 11717 | 96416050a8cd1517 | Thackeray | M1、S1(自嘲解法) |
| PG5166 | The Poetaster（Jonson，含编者绪论） | 9669 | 252b41f8515df282 | Jonson/编者 | H 级依据：单一主导气质（L193-215） |
| PG5265 | The Ball and the Cross（Chesterton） | 8573 | 381f81498e6032ca | Chesterton-2 | 冲突记录：论证型喜剧（M8/M11 不适用） |
| PG5784 | A Tramp Abroad Vol.03（Twain） | 2246 | 9f24b2711df1b484 | Twain-A | M2（反语式伪精确） |
| PG6753 | Psmith in the City（Wodehouse） | 6422 | a4b1f4bc26809ecf | Wodehouse | M5、M6（冷面台词） |
| PG6768 | The Man Upstairs and Other Stories（Wodehouse） | 13251 | 598cdbdbd76d21fc | Wodehouse | M2、M4 |
| PG6836 | Three Men and a Maid（Wodehouse） | 7548 | e02f44575a8408bc | Wodehouse | M2、M4、M5、M6、M7、M8、M9、M11、M12①③（主证据） |
| PG6955 | The Prince and Betty（Wodehouse） | 8999 | 9a85d9bf2a91e44e | Wodehouse | M4、M6 |
| PG7100 | Huckleberry Finn Ch.01-05（Twain） | 862 | a1587924546e8369 | Twain-C | M6（开场告示）、反例记录 |
| PG7102 | Huckleberry Finn Ch.11-15（Twain） | 1278 | 0846973cc33bd60b | Twain-C | 天真叙述与舆论反讽 |
| PG7107 | Huckleberry Finn Ch.36-末（Twain） | 1855 | da628e932184c28a | Twain-C | 反例记录：笑点服务于道德判断 |
| PG844 | The Importance of Being Earnest（Wilde） | 3884 | c89baeb2febea37c | Wilde | M5、M9；**M1/M11 不适用（戏剧）** |
| PG8525 | Eve's Diary（Twain） | 676 | bb68e74cf72b5ae4 | Twain-B | M5、M12 |
| PG8713 | A Man of Means（Wodehouse/Bennett） | 3455 | 227c19702dc7caf4 | Wodehouse | M10 |
| PG883 | Our Mutual Friend（Dickens） | 38654 | 711758d25de16dd7 | Dickens | M4、S1(边界例证) |

## 2. 族去重与覆盖档位

- **族去重**：同作者多本只算 1 条独立证据线。Wodehouse 7 本 = 1 条；Twain 7 本中 Huck Finn 三个分章重刊（PG7100/7102/7107）合为 1 条，故 Twain 共 5 条线（PG119/PG5784 同属 Tramp Abroad，合为 1 → 实际 4 条：PG119+PG5784、PG3189+PG8525、Huck Finn、另见 PG119 独立）；Chesterton 2 本 = 2 条；Dickens、Thackeray、Wilde、Jonson、Jerome、Grossmith、PG28149、PG30343 各 1 条。
- **覆盖档位**：24/24 全本（100% 行数）有台账并通过 `kd32_ledger_gate`（分块覆盖 + 每块 ≥2 要点 + 逐字引文可在原文 ±3 行内找到）。未 FULL 来源数 = 0。
- **门禁不证明什么**：它只验证引文可回源与分块覆盖，**不证明模型真实阅读深度**。台账是代理写的要点，本 Skill 只对其中可回源部分负责。
- **已作废台账**（不计入证据）：`ledger-PG3189-full.rejected.md`、`ledger-PG6836-full.rejected.md`（历史门禁判定引文查无出处）。
- 本轮新增的一手阅读证据：`ledger-PG6836-p4-L1-2360.md`（4 块 / 17 引文）、`ledger-PG6836-p4-L4201-4760.md`（2 块 / 10 引文），均 PASS。

## 3. 对历史规则集 C1–C10 的裁决（完整记录）

被裁决对象 = 同类别已交付的 `批次-04/results/skills/comic-engine-craft`（任务 B-04-B04 的产物，本轮只读、未修改）。它自述"10 条规则全部单族深读-derived、置信低、无全文本"；本批 24 本全文本构成对它的独立复核。

| 规则 | 裁决 | 依据（来源 + 行号 + 它是什么意思） |
|---|---|---|
| C1 合诵者引擎（叙述者只反应不造笑） | **REVISE** | 支持：PG6836 L667-678（Sam 期待 Eustace 做"派对的生命与灵魂"，眼前这人"在俄国小说家聚会上也难担此角色"）；PG6753 L1037-1039（Psmith"带着朴素的尊严"需要 Mike 的反应位）。反对：PG6836 L916-925、L1836-1837、L1700-1701 与 PG308 L141-142 的笑点**出自叙述者自己**。→ 断言过窄，修订为"反应位是默认配置，允许叙述者兼造笑的第二配置（插话必须短、且必须与角色合谋而非嘲弄角色）"。 |
| C2 第三者信件预介，登场只演不述 | **KEEP** | PG6836 L96-99（舅舅来信说 Sam 将至并附"她从未看好他"的判断）；Sam 在 L126-146 登场即用动作演。断言与条件均成立。 |
| C3 荒诞前提 + 伪精确论证 | **KEEP（置信 低→中）** | 本批扩到 4 族：PG1696 L816-817；PG28149 L568-570；PG8713 L73-108；PG6836 L768-789。 |
| C4 称谓通胀签名 | **NOT_PROVEN** | 本批未读出"对最高身份者照样使用同一称呼语"的实例；PG2233 L455、PG6768、PG6955 的固定应答属**应答签名**（标记说话者）而非**称谓签名**（标记被称呼者），机制不同，不并入 C5。该规则不进入本 Skill。 |
| C5 和声位（两句式应答者打节拍） | **KEEP（换证据族）** | PG6836 的 "Hello?" 五次（L1298、1363、1712、1733、2219）；PG2233 L455/L485-487 的"空壳变体"。证据族由 Leacock 系换为 Wodehouse 系，断言不变 → 并入 M6。 |
| C6 字面化术语讽刺 | **KEEP（置信 低→中）** | PG6836 L4424（tort）、L2349（猪倌）、L4263-4265（"as of course you know"）；PG8525 L51-52。跨 Wodehouse/Twain 两族 → 并入 M5。 |
| C7 倒置框架（崇高旧框架装讽刺现实） | **KEEP** | PG4558 L196-198 + L704；PG8525 L22-23；PG3189 L451-471 + L883-891。三族独立支持。 |
| C8 双版本陈述（叙述者补"他真正想说的是"） | **REJECT（本 Skill 不采纳）** | 本批 24 本未读出该形态的任何实例。相邻但不同的机制是**机制自陈**：PG6836 L4736-4738、L1818-1837，PG2233 L36-38。以 M11 取代。保留 C8 会误导执行者去找不存在的手法。 |
| C9 画面外兑现 | **KEEP + 条件细化** | 支持：PG6836 L1818-1837（电影字幕套话只在叙述者/读者视野内）、PG2233 L36-38。**反例**：PG6836 L4470-4528 → L4568-4572 → L4612-4618，谎言的后果以"持枪者推门而入"进入角色视野。→ 加条件：**宣言的反例走画面外；行动的后果走画面内**，不可互换。 |
| C10 通感冷开场 | **REVISE** | 本批开场主力是伪精确清单（PG6836 L30-39、PG2042 L35-37）与元叙述声明（PG2233 L36-38、PG3189 L451-471）；通感句只在 PG6836 L30-32、PG119 L336-337 出现且依附于另两型。→ 修订为 M12"开场三型"，通感句不作为通则。 |

**汇总**：KEEP 4（C2、C3、C5、C7），KEEP + 条件细化 1（C9），REVISE 2（C1、C10），REJECT 1（C8），NOT_PROVEN 1（C4）。置信升级：C3、C5、C6、C7 由"低（单族）"升为"中（2–4 族全文本）"。

## 4. 单部作品的情节设计 ≠ 通则（本 Skill 明确拒绝的推广）

- PG6836"母亲偷走全部裤子以阻止婚礼"（L768-789）→ 不是"喜剧必须有一个荒诞障碍物"。
- PG3189《Political Economy》的推销员打断（L213-422）→ 不是"幽默必须有一个打断者"。
- PG844 的虚构弟弟 Ernest（L446-449）→ 不是通则（该剧情节）。
- PG5265 的"决斗＝论辩"→ 不是"概念喜剧必须写决斗"。
- 批次只是工作量切分（任务清单 `batch_is_workload_partition_not_new_semantic_genre: true`），本批 24 本不构成"喜剧幽默类型"的完整画像。
