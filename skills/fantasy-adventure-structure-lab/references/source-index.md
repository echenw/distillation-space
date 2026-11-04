> **Agent1 最终 P2 核验**：26/26 `TRUSTED_FULL`。PG364、PG500、PG5245 的旧缺口已由 2026-10-30 连续分块补读闭合；以下“旧覆盖”只保留证据演进历史。版本与许可证见 version-and-provenance.md。

# 来源索引（批次-02 / A-05-B02 全部 26 份）

> 用途：核对"某条规则出自哪本书、哪一行"。覆盖数据由本轮实算得出，不是沿用旧账。
> 实算方法：读取 `rounds/round-01-2026-10-25/notes/evidence/MAIN/<PGID>.ledger.md`，
> 取所有以 `#` 开头的分段标题中的 `L<a>-<b>` 区间，与 `materials/2026-10-25/manifest.yaml` 的
> `total_lines` 求并集与缺口。
> 卡/台账文件位置：`rounds/round-01-2026-10-25/notes/evidence/MAIN/`。

## 汇总

| 项 | 值 |
|---|---|
| 来源总数 | 26 |
| 来源去重后族数 | 20（Burroughs 4→1、Haggard 2→1、MacDonald 2→1、London 2→1；其余各为单本族） |
| 当前可信全文 | 26/26 TRUSTED_FULL |
| 当前缺口 | 0 |
| 当前行数覆盖 | 179,094 / 179,094 = 100%（旧 175,984 为历史台账并集） |
| o200k Token（manifest 全批值） | 2,144,825 |
| 证据卡（`<PGID>.md`）落盘 | 24 份；**PG16 与 PG500 无卡**，仅有 ledger + 断点/完成确认文件 |
| 台账（`<PGID>.ledger.md`）落盘 | 26/26 |

**关于 PG16 的一处账目不一致（如实登记）**：`PG16._resume.md` 第 4 行称「证据卡 `PG16.md` 已存在（前实例基于 L1-2400 写就，标 PARTIAL）」，但本轮目录扫描中 `PG16.md` **不存在于磁盘**，只有 `PG16.ledger.md` 与 `PG16._resume.md`。因此 PG16 的规则只能引 ledger（L1-6259 全覆盖，B001–B462），**不引"卡"**。

---

## 逐书索引

| # | PGID | 书名 / 作者 | 行数 | 覆盖 | 台账分段 | 证据卡 | 本 Skill 中的痕迹 |
|---|---|---|---|---|---|---|---|
| 1 | PG5245 | Tales from the Arabic — Complete / John Payne（译） | 22,298 | **TRUSTED_FULL** 1–22298（历史：PARTIAL） | 旧台账 + 2026-10-30 补读 | ✅ | R032 忠仆/恩人层；R061 镜像刑罚 |
| 2 | PG3155 | She / H. Rider Haggard | 11,623 | FULL | 20 段 | ✅ | R001 边界声明；R005 重浴反噬；R006 威慑经济学；U-03/U-17/U-18 |
| 3 | PG54068 | Hearts of three / Jack London | 13,284 | FULL | 23 段 | ✅ | R083 撒径计；U-19/U-20；02 R020 反例 |
| 4 | PG6051 | Stella Fregelius / H. Rider Haggard | 10,875 | FULL | 19 段 | ✅ | R007 通灵成瘾模型；R143 蒙面真理；R144 反高潮宣言 |
| 5 | PG72901 | By the Gods Beloved / Baroness Orczy | 10,495 | FULL | 18 段 | ✅ | R030 司法奇观；R031 废刑立法；R050 唯一不信者；R051 双画像；U-21 |
| 6 | PG364 | The Mad King / Edgar Rice Burroughs | 10,734 | **TRUSTED_FULL** 1–10734（历史：PARTIAL） | 旧台账 + 2026-10-30 补读 | ✅ | R020/R021 行政化作恶；R040-R046 错认族；R145 清算清单；U-15/U-16 |
| 7 | PG78 | Tarzan of the Apes / Edgar Rice Burroughs | 11,003 | FULL | 19 段 + 段 4b + 收束段 | ✅ | R047 档案链五级；R082 恩义四级对账；R107/R108 恐惧与周期；R074 迟到赦免；U-22 |
| 8 | PG70815 | Tarzan at the Earth's Core / Edgar Rice Burroughs | 8,877 | FULL | 15 段 | ✅ | R087 硬机制交接与擦肩；R095 身体计时 |
| 9 | PG28725 | Harding's Luck / E. Nesbit | 8,289 | FULL | 14 段 | ✅ | R130 官方叙事三件套；R131 系列缝合约；R132 元小说（第二例）；R149 诱惑外化；R023 反例（让位三要素） |
| 10 | PG325 | Phantastes / George MacDonald | 7,122 | FULL | 12 段 | ✅ | 06 影叙事与"内心恶外化"母题的早期范本（PG325→PG78/PG70815 源流标注） |
| 11 | PG70589 | Tarzan and the Lost Empire / Edgar Rice Burroughs | 8,072 | FULL | 14 段 | ✅ | R022 群体换挡；R023 让位三段式；R024 承诺可验证；R084-R086 藏身/混乱/缴获；R094 声纹识人；U-08 |
| 12 | PG3495 | The King of Ireland's Son / Padraic Colum | 7,146 | FULL | 12 段 | ✅ | R048 名字三层；R060 契约字面主义；R072 誓言绑定；R090-R093 逃脱道具/怪物家宅/妖婆/劳役 |
| 13 | PG26451 | A Stable for Nightmares; or, Weird Tales / J. S. Le Fanu 等 | 6,251 | FULL | 11 段 | ✅ | R049 化名戳穿；R062 誓言字面兑现；R074 迟到赦免；R105 物证链；R109 二手痕迹；U-14 |
| 14 | PG708 | The Princess and the Goblin / George MacDonald | 6,043 | FULL | 10-11 段 | ✅ | R089 指引物张力；R102-R104 机制灵异/可耗弹药/恨其所无；R114 逻辑醒悟；R133 软化归化 |
| 15 | PG16 | Peter Pan / J. M. Barrie | 6,259 | FULL（ledger 11 段，B001–B462） | 11 段 | ❌ **无卡** | R146 世代循环条件句；R147 信念衰减律 |
| 16 | PG500 | The Adventures of Pinocchio / Carlo Collodi（英译 C. Della Chiesa） | 5,841 | **TRUSTED_FULL** 1–5841（历史：PARTIAL） | 旧台账 + 2026-10-30 补读 | ❌ **无旧卡**（补读台账提供本轮全文证据） | R150 谎言的双向物理规则 |
| 17 | PG310 | Before Adam / Jack London | 3,788 | FULL | 3 块 | ✅ | R012/R073 心智阶段与半成品；R027 语言上限解释不起义；R028 艺术起源；R095 身体计时；R106 生物学反派；U-11/U-13/U-14 |
| 18 | PG10463 | The Little House in the Fairy Wood / Ethel Cook Eliot | 3,775 | FULL | 3 块 | ✅ | R033 准入测"不伤害"；R112 信念准入与可见性衰减；R113 不信的习得；R116 解放反例；R139-R142 判词/守护者/环形/主题歌；U-05/U-09/U-10 |
| 19 | PG50658 | The Feather / Ford Madox Hueffer（Ford Madox Ford） | 4,293 | FULL | 8 段 | ✅ | R002-R004 法器三件套/字面漏洞/信息优势；R008 荒谬规程；R009 命运界面化；U-12 |
| 20 | PG3527 | The Blue Moon / Laurence Housman | 2,976 | FULL | 8 段（含棒 3/4/5 重叠区间） | ✅ | R029 守门人；R063-R066 禁语/破戒/资质/自残；R070 同一性禁令；R096 双计时器；R134-R138 推源论/代价归还/按本质受罚/对称驱逐/沉默赦免；R148；U-01/U-04/U-06/U-07/U-09 |
| 21 | PG1087 | Baartock / Lewis Roth | 2,819 | FULL | 6 段（+他棒并行段） | ✅ | R012 教学边界；R025 禁令重译；R026 权威降格不失位；U-04/U-26 |
| 22 | PG592 | The Chinese Nightingale, and Other Poems / Vachel Lindsay | 3,080 | FULL | 6 段（棒 5 + 棒 6） | ✅ | R117 排版承载音量与停顿；U-23 |
| 23 | PG5590 | The Greylock: A Fairy Tale / Georg Ebers | 1,572 | FULL | 3 块（+细分区间） | ✅ | R010 护佑可失效条款；R011 名号由伤痕；R115 敌人受约束；R054 镜功能（侦查型）；U-02/U-05 |
| 24 | PG1667 | My Aunt Margaret's Mirror / Sir Walter Scott | 1,402 | FULL | 2 块（+细分区间） | ✅ | R052 渐进显像与自陈代价；R053 保留不利证据；R074 信息延迟；R100/R101 去魅先行与讲述者瑕疵；U-05/U-07 |
| 25 | PG52545 | The Princess Nobody / Andrew Lang | 780 | FULL | 1 块（+细分区间） | ✅ | R067 语义空转契约；R068 管辖权转移；R069 消失式保护；R080/R081 引荐链与恩义三件套；R088 求援链与比例赦免；R132 元小说；U-01/U-02/U-03 |
| 26 | PG70879 | The mirrors of Tuzun Thune / Robert E. Howard | 397 | FULL | 5 段 | ✅ | R001 三段去魅问答与边界声明；R054 镜功能（本体论开放）；R110 本体论悬置；R111 系统空转；R112 信念准入；U-05/U-06/U-07 |

## 旧缺口闭合说明

- **PG5245**：新补读分四段连续覆盖 L1–22298，旧缺口 L7172–8135 与 L20736–22298 均落入实质记录；抽查 L7604-7605、L8118-8119、L20504-20505、L21671、L22298 与原文一致。
- **PG364**：新补读连续覆盖 L1–10734；旧碎片缺口全部被包含。抽查 L1497-1499、L3593-3595、L9383-9384、L10307-10320 与原文一致；一处补读引文起始行有 1 行漂移，按相邻原文核验后不影响覆盖判断。
- **PG500**：新补读连续覆盖 L1–5841；旧缺口 L5001–5841 包含 Geppetto 重逢、返岸、劳动赡父、仙女回报与“真实男孩”结尾，抽查 L5262-5264、L5830-5831、L5840-5841 与原文一致。

## 去重说明（来源族）

族去重只在**跨书升格**时生效：同一作者/同一系列的多部作品，在把单本观察升为"跨书共识"时按一族计数，避免把同一作者的个人习惯误当类型规律。本批 26 → 20 族：

1. **Burroughs 族**：PG78、PG364、PG70815、PG70589（4 本）
2. **Haggard 族**：PG3155、PG6051（2 本）
3. **MacDonald 族**：PG325、PG708（2 本）
4. **London 族**：PG54068、PG310（2 本）
5–20. 其余 16 本各为单本族：PG5245、PG72901、PG28725、PG3495、PG26451、PG16、PG500、PG10463、PG50658、PG3527、PG1087、PG592、PG5590、PG1667、PG52545、PG70879（16 本）

**族内互证（已用于升格）**：
- Burroughs 族："身份错位 + 档案证真"两演（PG78 ↔ PG364，PG78 技法族明写）；"收束政治学"三型（PG78 让位/清算/不流血、PG70589 B296-B298、PG70815 不流血解放）。
- Haggard 族：代价结构互证（PG3155「Ayesha 须再浴即死」↔ PG6051「Morris 精炼感官即死」，PG6051 §4 明写）；水镜 ↔ aerophone（同为"物质手段无法达成超越性目的"的主题装置，PG6051 观 2）。
- London 族：均为"以论证支撑设定"（PG310 B09 幸存者偏差、H02），但 PG54068 为闹剧节奏、PG310 为史前论证，**基调相反，不作跨书共识**。
- MacDonald 族：PG325 影叙事 → PG708 机制灵异；PG325 的证据卡明写"本书为后世'内心恶外化'母题的早期范本，融合时须标注方向性"。

**不作跨书共识的项**（即使同族）：见 `08-conflicts-and-redlines.md` 的 U 系列。
