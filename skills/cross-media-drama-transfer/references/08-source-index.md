# R8 来源索引与边界

## R8.1 规则来源：7 部作者训诫手册

| PG | 书名 / 作者 / 年代 | 原文（整本阅读版） | reading_sha256（前 16 位） | 台账 |
|---|---|---|---|---|
| PG17903 | Writing the Photoplay — J. Berg Esenwein & Arthur Leeds | `distill/有原始正文/19-漫画漫剧与跨媒介叙事/PG17903-Writing-the-Photoplay/整本阅读版.txt` | 见附表 | `rounds/round-perbook/notes/reading/ledger-PG17903-full.md`（PASS） |
| PG13029 | The Art of the Moving Picture — Vachel Lindsay | 同目录 `PG13029-The-Art-of-the-Moving-Picture/` | 见附表 | `rounds/round-shard-dfm/notes/reading/ledger-PG13029-s1-6000.md`、`-s6001-6310.md`（PASS） |
| PG70937 | The Photodrama — Henry Albert Phillips (1914) | 同目录 `PG70937-The-photodrama/` | 见附表 | `rounds/round-shard-dfm/notes/reading/ledger-PG70937-s1-4851.md`（PASS） |
| PG76829 | How To Write Photoplays — Embrie Zuver | 同目录 `PG76829-How-to-write-photoplays/` | 见附表 | `rounds/round-kd32-r01/notes/reading/ledger-PG76829-s1-2123.md`（PASS） |
| PG66049 | Pictorial Beauty on the Screen — Victor Oscar Freeburg | 同目录 `PG66049-Pictorial-Beauty-on-the-Screen/` | 见附表 | `rounds/round-shard-dfm/notes/reading/ledger-PG66049-s1-5546.md`（PASS） |
| PG53117 | Motion Picture Directing — Peter Milne | 同目录 `PG53117-Motion-Picture-Directing/` | 见附表 | `rounds/round-shard-dfm/notes/reading/ledger-PG53117-s1-4893.md`（PASS） |
| PG39973 | How to Produce Amateur Plays — Barrett H. Clark (1923) | 同目录 `PG39973-How-to-Produce-Amateur-Plays/` | 见附表 | `rounds/round-kd32-r02/notes/reading/ledger-PG39973-s1-3787.md`（PASS） |

## R8.2 案例基座：82 部戏剧文本

角色核账与逐本证据见 `notes/source-synthesis.md` §3 与附表。要点重申：

- 它们是**案例**，不是规则来源。**不得把单部小说的情节设计直接变成所有作品都必须遵守的规则**——本轮据此 REJECT 了"禁止旁白""必须快乐结局""必须正面演出"三条候选规则。
- 一手阅读（本轮亲读）：PG4963 L2601-2800、PG1109 L2745-2874、PG4906 L380-700、PG29682 L2040-2139，证据在 `notes/reading/`。
- 改编实例：PG40729、PG41750（各自从狄更斯《圣诞颂歌》改编的舞台本）、PG43304（能乐英译，`未证明`）。

## R8.3 覆盖与证据可信度

- P2 区间覆盖 **89/89＝100%**；`sources_not_full = 0`。
- 每本至少一条可被 `distill/_tools/kd32_ledger_gate.py` 回源校验的逐字引文。
- 台账门禁（本轮重跑，113 份 `.md`）：109 PASS、1 INCOMPLETE（PG4963，本轮补齐）、3 FABRICATED（PG1109 / PG4906 / PG29682，逐条回源后判为**格式或行号错误、内容真实**，本轮各补一份 PASS 替证）。
- 89/89 份 `整本阅读版.txt` 的 sha256 与各自 `书籍信息.json` 的 `reading_sha256` 一致（本轮实算）。

## R8.4 引文行号的两处已知错位（必须按更正引用）

- PG1109：台账标 `行 3623-3625` 的 "All haile, the richest Beauties on the earth" **真实位置 L2764**（`grep -n` 核实）。
- PG4906：台账的 `行 389-391`、`1016-1018`、`2700-2702` 三条引文均为**跨说话人拼接**——真实行分别是 389 / 392、1016 / 1019、2700（2700 行原文无 "Slice:" 前缀）。
- 早期印刷体含 `_斜体_` 标记与换行，行号实测有 ±1 行偏差。

## R8.5 边界（负触发的根据）

| 主题 | 状态 | 说明 |
|---|---|---|
| 漫画/漫画剧分镜、格序、页数节奏 | `NOT_PROVEN` | 89 本来源中 0 本涉及 |
| 有声片对白、现代剧本格式、现代分镜软件 | `NOT_PROVEN` | 0 本涉及 |
| 网文/短视频/现代剧集体例 | `NOT_PROVEN` | 0 本涉及 |
| 现行版权与授权 | `NOT_PROVEN` | 只有 1919/1923 年美国口径 |
| 能乐等东洋形态的可迁移规则 | `未证明` | PG43304 未做专项融合 |
| 用 89 本给具体主张背书 | **禁止** | 具体主张必须回到单本台账与行号 |

## R8.6 附表：89 本 SHA 与角色（机器生成）

见下表（reading_sha256 为本轮实算，与 `书籍信息.json` 一致）。

| PG | 题名 | 角色 | 行数 | reading_sha256（前 16） | 台账数 |
|---|---|---|---:|---|---:|
| PG1104 | The Comedy of Errors | 不适用 | 2583 | `6143427da1dcba2f` | 1 |
| PG1107 | The Taming of the Shrew | 不适用 | 3686 | `a56c14baa70c164b` | 1 |
| PG1108 | The Two Gentlemen of Verona | 不适用 | 3156 | `e4cd32a6b13b774f` | 4 |
| PG1109 | Love's Labour's Lost | 支持+反例（一手） | 3923 | `eb0fce1a7845b128` | 2 |
| PG1113 | A Midsummer Night's Dream | 不适用 | 2829 | `49ad9cbf9b017093` | 2 |
| PG1114 | The Merchant of Venice | 不适用 | 3460 | `099571c38d0ad34e` | 1 |
| PG11759 | The Bicyclers and Three Other Farces | 反例（aside 约定） | 3954 | `278240cdb0d96e13` | 2 |
| PG12110 | The Scornful Lady | 不适用 | 4406 | `b5a322c285d9f605` | 2 |
| PG12141 | The Spanish Curate: A Comedy | 不适用 | 6720 | `1d60fddef4cac2d1` | 2 |
| PG12472 | Bataille de dames | 不适用 | 8814 | `c05a5d36f9e0e783` | 1 |
| PG13029 | The Art of the Moving Picture | 支持（作者训诫） | 6310 | `1409dc41d21fd26b` | 2 |
| PG14246 | Mercadet: A Comedy in Three Acts | 补充（叙事层） | 5009 | `62e6874dca71828c` | 1 |
| PG15007 | The belles of Canterbury | 不适用 | 971 | `2da71e992c1dc63c` | 1 |
| PG15744 | The Gay Lord Quex: A Comedy in Four Acts | 不适用 | 8879 | `cde4111e6e609e18` | 1 |
| PG17903 | Writing the Photoplay | 支持（作者训诫） | 12792 | `d49f18c5f1af7db8` | 1 |
| PG1929 | The School for Scandal | 反例（aside 约定） | 4779 | `11df21931a10aeac` | 1 |
| PG2027 | Tartuffe; Or, The Hypocrite | 不适用 | 3957 | `11fcf1cbca56da57` | 1 |
| PG20890 | Bussy D'Ambois and The Revenge of Bussy D'Ambois | 补充（叙事层） | 12309 | `52cec54c87c86a70` | 1 |
| PG21570 | The Squire: An Original Comedy in Three Acts | 补充（叙事层） | 4010 | `3047f993564e9279` | 1 |
| PG2232 | The Duchess of Malfi | 反例（aside 约定） | 5196 | `7f79e8806c5831bb` | 1 |
| PG2467 | Ghosts: A Domestic Tragedy in Three Acts | 补充（叙事层） | 3479 | `05d112da935a0bcb` | 1 |
| PG24917 | Mariucha | 补充（叙事层） | 15082 | `b557feff09c383d6` | 1 |
| PG2506 | The Sleeping-Car: A Farce | 不适用 | 1119 | `fb7256ad54f58254` | 1 |
| PG2536 | Amphitryon | 不适用 | 2224 | `5acd0c72e8aff140` | 1 |
| PG2663 | Minna Von Barnhelm | 补充（叙事层） | 5258 | `534852372d2bfa75` | 1 |
| PG2829 | Fanny and the Servant Problem | 不适用 | 3304 | `2a5a91bec3ac5593` | 1 |
| PG29682 | Erdgeist (Earth-Spirit): A Tragedy in Four Acts | 支持+反例（一手） | 3873 | `79495020127dc5ca` | 2 |
| PG30934 | Venice Preserved: A Tragedy | 不适用 | 2624 | `e438b7ac0fdd45fa` | 1 |
| PG31463 | The Orphan; Or, The Unhappy Marriage. A Tragedy, in Five Acts | 不适用 | 2835 | `db3d9a0283e936a2` | 2 |
| PG33415 | Pandora's Box: A Tragedy in Three Acts | 不适用 | 2815 | `65e4641be3bbbd64` | 1 |
| PG33957 | The Cabinet Minister: A farce in four acts | 不适用 | 8435 | `105c589514549409` | 1 |
| PG3401 | The Elevator | 不适用 | 1411 | `6d80507e39b45175` | 1 |
| PG3402 | The Parlor Car | 不适用 | 875 | `dd290bd8f808b312` | 1 |
| PG3403 | The Register | 不适用 | 1436 | `886f3b8cfc39a3e7` | 1 |
| PG35961 | The Inconstant | 不适用 | 2914 | `f3748d0382c8c32b` | 2 |
| PG36570 | The Heiress; a comedy, in five acts | 反例（aside 约定） | 3572 | `a33269f5ee88b520` | 1 |
| PG36984 | Fifty Contemporary One-Act Plays | 不适用 | 47078 | `c43876be23900820` | 2 |
| PG37140 | A Proposal Under Difficulties: A Farce | 不适用 | 1288 | `2a90e0c3aadfddaf` | 1 |
| PG3735 | The Inspector-General | 不适用 | 4292 | `aa2a19237f249c08` | 2 |
| PG37503 | Gammer Gurton's Needle | 不适用 | 3301 | `1d10e98fd0886b89` | 1 |
| PG37970 | Contemporary One-Act Plays | 不适用 | 15077 | `eed19436178214ed` | 1 |
| PG39243 | Six One-Act Plays | 不适用 | 3810 | `29eb0dd048cf10a1` | 1 |
| PG39973 | How to Produce Amateur Plays: A Practical Manual | 支持（作者训诫） | 3787 | `140ad4ed1a0ab826` | 1 |
| PG4011 | Epicoene; Or, The Silent Woman | 补充（叙事层） | 9839 | `bccf3b15472978ab` | 1 |
| PG40729 | "Old Scrooge": A Christmas Carol in Five Staves.  Dramatized from Charles Dickens' Celebrated Christmas Story. | 支持（改编实例） | 2247 | `075b95133a2e9b26` | 1 |
| PG41033 | The Silver Shield: An Original Comedy in Three Acts | 不适用 | 3604 | `6ac04b1eb91154b5` | 1 |
| PG41739 | A Christmas Carol; Or, The Miser's Warning!  (Adapted from Charles Dickens' Celebrated Work.) | 不适用 | 1523 | `714036fb0e8d3d11` | 1 |
| PG41750 | The Magistrate: A Farce in Three Acts | 支持（同题异改） | 7162 | `229e09ca61e1dec6` | 1 |
| PG42523 | Box and Cox: A Romance of Real Life in One Act. | 不适用 | 1329 | `c4e057b7252520cc` | 1 |
| PG43304 | The Nō Plays of Japan | 未证明 | 12098 | `d1410c613b402092` | 1 |
| PG45628 | A Desperate Game: A Comic Drama in One Act | 不适用 | 1508 | `8bc8a1fee168f570` | 1 |
| PG46044 | A Little Change: A Farce in One Scene | 不适用 | 1204 | `e09e61f2c7c04392` | 1 |
| PG46138 | A Rough Diamond: A Comic Drama in One Act | 不适用 | 1211 | `3dfcfb1621623ba1` | 1 |
| PG46420 | Married Life: A Comedy, in Three Acts | 不适用 | 2933 | `d021538855fa8592` | 2 |
| PG4683 | Socrates | 不适用 | 1394 | `6258b4d1a10ec7b1` | 1 |
| PG46918 | Single Life: A Comedy, in Three Acts | 补充（叙事层） | 3500 | `6eca0a2549000cc2` | 1 |
| PG4700 | The Unforseen Return | 不适用 | 1449 | `fb13ce3f56b1f808` | 1 |
| PG47379 | A Bold Stroke for a Husband: A Comedy in Five Acts | 反例（aside 约定） | 3151 | `ef3878e1e4b99a40` | 3 |
| PG47559 | The Prude's Progress: A Comedy in Three Acts | 不适用 | 5051 | `1533f617498511e5` | 1 |
| PG47560 | The Schoolmistress: A Farce in Three Acts | 不适用 | 6143 | `d82200f924d2509e` | 2 |
| PG47561 | Trelawny of The "Wells": A Comedietta in Four Acts | 不适用 | 9095 | `d5153d8a83eb4880` | 1 |
| PG47604 | The Belle's Stratagem | 不适用 | 3644 | `911e25b34ced1150` | 1 |
| PG47826 | A Tender Attachment: A Farce | 不适用 | 1217 | `dcb8e32464ad52f7` | 1 |
| PG48707 | Gentlemen of the Jury: A Farce | 不适用 | 1160 | `7db377960f922180` | 1 |
| PG4906 | The Lucky Man | 支持+反例（一手） | 4068 | `4f4994054dab5267` | 2 |
| PG4963 | Moral | 支持+反例（一手） | 3858 | `2121be8958406448` | 2 |
| PG53117 | Motion Picture Directing: The Facts and Theories of the Newest Art | 支持（作者训诫） | 4893 | `94d371f909d2ec43` | 1 |
| PG554 | The Contrast | 不适用 | 4333 | `3c912ff4514459ff` | 2 |
| PG59210 | Comediettas and Farces | 反例（aside 约定） | 7661 | `51e16d08a9c71baf` | 1 |
| PG60523 | The Torch-Bearers: A Satirical Comedy in Three Acts | 不适用 | 7026 | `aeca0bfe0627f382` | 2 |
| PG65519 | The Escape; Or, A Leap For Freedom: A Drama, in Five Acts | 不适用 | 2404 | `4537ce7032b6abb0` | 1 |
| PG66049 | Pictorial Beauty on the Screen | 支持（作者训诫） | 5546 | `72bfa82b1216fc23` | 1 |
| PG6742 | The School for Husbands | 不适用 | 2068 | `82e3ddfebb4d2589` | 1 |
| PG6782 | The Robbers | 补充（叙事层） | 6172 | `d514605c8275cbe5` | 2 |
| PG6784 | Love and Intrigue: A Tragedy | 补充（叙事层） | 4457 | `008789ce67832604` | 3 |
| PG70635 | Lively plays for live people | 反例（aside 约定） | 11658 | `542aefe01cbbf14f` | 1 |
| PG70884 | French without a master | 不适用 | 968 | `6db390d8aca0773b` | 1 |
| PG70937 | The photodrama | 支持（作者训诫） | 4851 | `31b3d609179d5fab` | 1 |
| PG7108 | A Trip to Scarborough; and, The Critic | 反例（aside 约定） | 6459 | `b399f7c4879ce0ef` | 2 |
| PG7487 | Count Alarcos; a Tragedy | 不适用 | 5380 | `64511555f9c9d1eb` | 1 |
| PG75451 | The play's the thing | 不适用 | 3976 | `049eaaf61273a2cf` | 1 |
| PG76829 | How to write photoplays | 支持（作者训诫） | 2123 | `25f4b49e0f30a618` | 1 |
| PG76872 | Tragedies of sex | 不适用 | 11248 | `885fee9affd3ef8f` | 1 |
| PG7798 | The Village Coquette; Or, The Supposed Lottery | 不适用 | 1972 | `a5325c57cad38f6b` | 1 |
| PG8121 | Ghosts | 不适用 | 3656 | `a8ba3b28b2315756` | 1 |
| PG8606 | The Blue Bird: A Fairy Play in Six Acts | 不适用 | 5938 | `186854df23fc8537` | 1 |
| PG875 | The Duchess of Padua | 不适用 | 5477 | `2b582a5232d16256` | 1 |
| PG8776 | The Impostures of Scapin | 不适用 | 2534 | `f8ebf968659acf59` | 1 |
| PG885 | An ideal husband | 不适用 | 4465 | `13a6329bd5745e93` | 3 |

合计 89 本；角色计数：支持（作者训诫）7 / 支持（改编·同题异改）2 / 支持+反例（一手）4 / 反例 8 / 补充 10 / 未证明 1 / 不适用 57。

