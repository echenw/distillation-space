# SOURCE — 来源索引、元数据与规则裁决

## 本 Skill 的身份

- skill_id：`historical-fiction-power-machine`（目录名与 frontmatter `name` 一致）
- 任务：A-07-B01｜类别：16-类型小说专项/06-历史架空/批次-01｜Owner：Main A
- 轮次：`distill/分类蒸馏/16-类型小说专项/06-历史架空/批次-01/rounds/round-p4-final-2026-10-30`
- 与相邻批次的关系：本类别已存在 A-07-B02 `historical-fiction-plot-forge`（忠诚信物／谶语歌谣／疯狂毒药／文书司法／地形信号／血亲婚约六域 + 三条铁律）。
  **本包不是它的副本**：本批 15 源里"地形信号""谶语歌谣""疯狂毒药"三域均为 NOT_PROVEN 或 REJECT（见下），
  因此本包另立八域（FIN／HUNT／REP／RUMOR／MARRIAGE／PERF／DISG／JUST）。
  两包互补：需要地形追逐或谶语主线时，转 B02 包。

## 15 源索引（行数与 SHA 均在本机核对过）

`sha256_reading` = `整本阅读版.txt` 的 SHA-256；核对结果 **15/15 全部匹配**（`批次来源清单.json`）。

| PG | 书目 | 正文行数 | o200k tokens | SHA-256（前 16 位） |
|---|---|---:|---:|---|
| PG1290 | Salammbo | 11663 | 146086 | d73e11dcefd980b4… |
| PG135 | Les Misérables | 73206 | 801770 | d005a0c4b44d6a2c… |
| PG2681 | Ten Years Later | 25216 | 267853 | 2bc7f8957a03ae06… |
| PG2785 | The Elusive Pimpernel | 10023 | 114976 | df261d42f311f791… |
| PG31484 | Works of R. L. Stevenson, Swanston Ed. Vol.08 | 10104 | 121178 | e65f875e69833cf2… |
| PG34660 | Petticoat Rule | 11965 | 138052 | ec533b0bc44d981d… |
| PG35117 | Lord Tony's Wife | 10457 | 124423 | ad082ca96ef45f1a… |
| PG3942 | Confession of a Child of the Century — Complete | 8458 | 109096 | 54df8262f4fab7bd… |
| PG411 | The King's Jackal | 3068 | 40191 | bfc28686caab356f… |
| PG5202 | The Golden Lion of Granpere | 7153 | 92722 | 08e099a8a45d92ca… |
| PG53549 | I Will Maintain | 24502 | 212412 | a67339d486512df6… |
| PG60253 | The Noble Rogue | 14233 | 169554 | 425df346de30d7e2… |
| PG6668 | Annette, the Metis Spy | 5375 | 63583 | 64aeed2a0294161b… |
| PG78024 | The woman of Andros | 2350 | 29286 | f58e9274010884e6… |
| PG7987 | The Fair Maid of Perth | 19160 | 251499 | a1718c7b77cbc669… |
| **合计** | 15 部 | **236,933** | **2,682,681** | — |

原文绝对路径根：`distill/有原始正文/16-类型小说专项/06-历史架空/<PG>-<Title>/整本阅读版.txt`（只读，未改）。

## 阅读证据状态

- 台账覆盖：15/15 = FULL（`## L起-止` 分块并集 vs 实际行数）。
- 门禁：20 份非 rejected 台账逐个跑 `distill/_tools/kd32_ledger_gate.py`，**20 PASS / 0 FAIL**。
- 本轮独立复核抽样（新增，文件名含 PG 与区间）：
  - `notes/supplement-PG5202-L1-1500.md`（3 块、5 条带行号引文，PASS）
  - `notes/supplement-PG135-L24001-24500.md`（1 块、3 条带行号引文，PASS；该区间旧 partial 台账从未覆盖）
- 历史作废台账：`rounds/round-perbook/notes/reading/ledger-PG135-full.rejected.md`，未计入覆盖。
- 融合笔记：`notes/source-synthesis.md`；覆盖核账：`notes/source-coverage.md`。

## 规则裁决（对照本类别既有核心规则，用本批 15 源重审）

| 规则 | 裁决 | 依据 |
|---|---|---|
| R1 代价原则（承重选择须解释可见代价） | **KEEP＋限定**：代价须写在该作品自己的规范单位（财产／名声／性别体面／职务），不许统一写成身体性代价 | PG135 L24124-24141、L24315-24332；PG411 L2242-2248、L2650-2660；PG6668 L2754-2756；限定依据 PG5202 L255-259、L294-331 |
| R2 可验证原则（不可验证的宣称不可作支点） | **REVISE**：降级为"模式 A／模式 B"两条互斥工作模式 | 支持 PG135 L24047-24057、L24107-24110、L24117-24121；PG31484 L4093-4130；PG60253 L3108-3238。反例 PG411 L2589-2593 vs L2645-2648、PG2785 L3100-3146 |
| R3 误读原则（误读应验须写清过程） | **KEEP（弱版本）**；"应验皆误读"强版本在本批 NOT_PROVEN | PG78024 L831-840；PG3942 L495 |
| R4 地形／信号域 | **NOT_PROVEN，本包不设** | 本批无一部以地形规则引擎＋信号四件套驱动情节 |
| R5 谶语／歌谣域 | **NOT_PROVEN，本包不设** | PG1290 的预兆（L676-678、L947-958）是氛围配件，不是提纲 |
| R6 疯狂／毒药／攻心域 | **REJECT 作通用域** | PG3942 写的是世纪病与代际幻灭，不是毒杀攻防链 |
| R7 历史接口 | **KEEP，细化成档 A／档 B** | PG411 档 A；PG78024 L39-41、PG7987 L149-351 与 L357-367、其余 11 部档 B |
| R8 时代语料降级条款 | **KEEP（必须保留）** | PG6668 L1958-1990、L2172-2222；PG1290 L1980-1989、L947-958 |
| R9 "求婚必胜／誓言定局"的隐含规则 | **REJECT** | PG5202 L7097-7113、L7108-7112；PG2681 L5153-5179 vs L14973-14981 |

## 单源与未证明（不得误用）

- **PG7987**（替代取证：bier-right、champion、定制服装证据链）：**单源 + 该源台账引文密度低** → `justice-without-forensics.md` 只作候选域，输出须标"待核对"。
- **PG1290**（宗教／仪式与圣物政治）：单源支持，不作跨类别推广。
- **本包效果**：未在真实宿主任务中验证（P5 层级），本轮不声称效果提升。

## 许可与替代关系

- 来源均为 Project Gutenberg 公共领域文本；本包不复制原文大段内容，只给带行号的短引文与观察。
- 本包不替代 B02 `historical-fiction-plot-forge`；两包在本类别下并列，按需求选一。
- 本包不提供史学鉴定；涉及真实历史事件与人物时，只给创作方案并标明"未核对"项。
