# 06 · 来源索引与编号约定

## 1. 来源总表（26 部 / 23 族，全部 `FULL_TEXT_VERIFIED`，SHA-256 26/26 PASS）

| PG ID | 标题 | 作者/年 | 族 | 行数 | o200k tok | 覆盖 | 版本注记 |
|---|---|---|---|---|---|---|---|
| PG3268 | The Mysteries of Udolpho | Radcliffe, 1794 | 单本族 | 29,900 | 402,462 | FULL | — |
| PG3781 | The Jewel of Seven Stars | Stoker, 1903 | 单本族 | 8,848 | 119,511 | FULL | 1912 修订结局版 |
| PG14168 | Widdershins | Onions, 1911 | 单本族 | 8,965 | 107,551 | FULL | 九篇集 |
| PG10624 | Three John Silence Stories | Blackwood, 1908 | **Blackwood-Silence** | 7,094 | 86,926 | FULL | 系列首集 |
| PG10659 | Three More John Silence Stories | Blackwood, 1912 | **Blackwood-Silence** | 5,138 | 63,138 | FULL | 题献真人原型 |
| PG45964 | Day and Night Stories | Blackwood, 1917 | **Blackwood-Silence** | 7,666 | 99,215 | FULL | 收录版（含 Silence 案） |
| PG35517 | The Three Impostors | Machen, 1895 | 单本族 | 5,567 | 76,931 | FULL | 马赛克嵌套 |
| PG10002 | The House on the Borderland | Hodgson, 1908 | 单本族 | 5,261 | 69,850 | FULL | — |
| PG6781 | The Ghost-Seer | Schiller, 1787–89 | 单本族 | 4,743 | 60,057 | FULL | 英译拼合本 |
| PG5083 | The Man of Feeling | Mackenzie, 1771 | 单本族 | 3,796 | 50,983 | FULL | 边界反例（感伤） |
| PG9909 | Nightmare Abbey | Peacock, 1818 | 单本族 | 3,732 | 39,832 | FULL | 元文献（类型讽刺） |
| PG459 | The White People | Frances Hodgson Burnett, 1917 | 单本族 | 2,207 | 27,577 | FULL | **非 Machen 同名作**（R30 撞名警示） |
| PG1190 | The Jolly Corner | Henry James, 1908 | 单本族 | 1,325 | 19,562 | FULL | — |
| PG1710 | La Grande Bretèche | Balzac, 1832 | 单本族 | 871 | 11,195 | FULL | 活埋原型（R49） |
| PG23220 | The Gray Nun | Eschstruth | 单本族 | 606 | 6,535 | FULL | 德式 Schauer |
| PG18508 | Arthur Mervyn | C. B. Brown, 1799 | 单本族 | 15,675 | 201,073 | **FULL** | 原 PARTIAL 84%；2026-10-25 补读行 13201-15675 至 EOF（片12：Maurice 交割余波、Achsa 往事、梦魇、求恕式求婚、收束留白），卡增 F16-F23/H4-H5/P59-P62 |
| PG5164 | The Beetle: A Mystery | Richard Marsh, 1897 | 单本族 | 13,807 | 153,922 | FULL | 与 Dracula 同年多叙事者 |
| PG24879 | Curious, if True | Gaskell | 单本族 | 9,141 | 131,193 | FULL | 五篇集 |
| PG72421 | The Room in the Tower | E. F. Benson, 1912 | 单本族 | 9,062 | 113,241 | FULL | 十六篇集 |
| PG46363 | Her Dark Inheritance | Mrs. E. Burke Collins, 1892 | 单本族 | 6,883 | 81,504 | FULL | dime novel |
| PG5182 | The Old English Baron | Clara Reeve, 1778 | 单本族 | 6,276 | 73,629 | FULL | 哥特第二作 |
| PG43 | The Strange Case of Dr. Jekyll and Mr. Hyde | Stevenson, 1886 | **Stevenson** | 2,552 | 34,682 | FULL | 成语化经典（R83） |
| PG19750 | The Waif Woman | Stevenson, 1893/1916 | **Stevenson** | 740 | 9,652 | FULL | 遗稿；Eyrbyggja Saga 改写（R89/R90） |
| PG1210 | Kwaidan | Lafcadio Hearn, 1904 | 单本族 | 4,311 | 52,586 | FULL | 含 Notes 注释层（R79） |
| PG79427 | The Libertine, Vol. III | Charlotte Dacre, 1807 | 单本族 | 3,330 | 43,264 | FULL | 四卷本第三卷；零超自然（R81） |
| PG11610 | Madam Crowl's Ghost & The Dead Sexton | LeFanu, 1871 | **LeFanu-Golden Friars** | 1,551 | 19,438 | FULL | 两篇；方言全篇（R86） |

- 总计：169,053 行 / 2,155,509 o200k tok；实读 **100%**（2026-10-25 PG18508 片12 补读后 26/26 FULL）。
- 历史逐片台账与 26 张证据卡已在 P2 审计中核验；它们是收口证据，不是本 Skill 的运行时依赖。消费者从本来源表、规则行锚和版本页追溯来源身份。
- 族计权声明：Blackwood-Silence 3 本 = 1 族（R67/R73）；Stevenson 2 本 = 1 族（D3）；LeFanu = 1 族（R88，与《The House by the Church-Yard》同宇宙）。**融合权重按 23 族计，引文仍可逐本行号引用。**

## 2. 规则编号约定（重要）

P/R 编号存在两段式历史；为避免历史编号碰撞，本包采用以下复合 ID 约定：

- **全局链**：PG10624 卡（P1–P8 / R1–R6）为锚点 → PG35517（P9–P15 / R7–R11）→ … → PG19750（P155–P163 / R89–R90）连续到 P163 / R90。
- **局部编号卡（与本 Skill 引用消歧）**：PG3268（P1–P6 / R1–R4）、PG3781（P1–P6 / R1–R4）、PG14168（P1–P7 / R1–R5）——引用时一律写复合 ID：`PG3268·P1`、`PG3781·P2`、`PG14168·P3` 形式。
- 本 Skill references 中出现的一切 `P##`/`R##`（无前缀）均指全局链；带 `PGxxxx·` 前缀者指该卡局部编号。
- 若后续修订证据卡，应将三张早期卡重编号并更新本节——当前版本以复合 ID 消歧为准。

## 3. 融合决策摘要

| 决策 | 条数 | 清单 |
|---|---|---|
| KEEP | 13 | M03 不可描述之恶、M04 感官受限、M05 物证对账、M06 文档链、M08 见证代价、M09 接力、M10 侦探双引擎（单族）、M13 自然因果审判（条件路线）、M15 潜伏者、M16 空间双重性、M18 喜剧区间（条件路线）、M19 无鬼之恐、M20 调性纪律 |
| REVISE | 7 | M01 入场路线、M02 解释轨、M07 揭底/收束、M11 关系解咒、M12 干预代价、M14 誓约公平性、M17 时间装置 |
| REJECT | 1 | M21 "恐怖必须怪物显形"通则 |
| NOT_PROVEN | 1 | M22 载体最优长度/密度 |

最终消费者裁决已同步到 `01`–`05` references 与 `p4-field-guide.md`；历史融合记录不作为运行时依赖。

## 4. 跨 Skill 接口

本 Skill 与其他 Skill **无共享运行时接口**（GQ3 口径：明示无接口）。单向引用锚点（供其他类 Skill 反查）：

- **C-05 非线性叙事**：PG5182·F2、PG10002·P16/P19、PG43·F3/P144、PG1210·P115/F8、PG72421·P79、PG11610·P145/P154、PG35517·P9、PG18508·P58、PG5164·P59、PG24879·P73
- **B-01 长篇连载**：PG79427·P125/P126、PG5164·P59
- **B-03 言情**：PG1210·F12/F7/O-Tei 线、PG79427（反向参照）、PG23220·P50–P53
- **B-04 喜剧**：PG10659·P100/P106、PG9909 全卡
- **B-05 儿童**：PG1210 Riki-Baka/Hi-Mawari（边界参考）
- **B-07 身份复仇权谋**：PG43·P141/F9、PG79427·P122、PG46363 夺产五步

## 5. 引用与验证路径

任何本 Skill 的规则引用可按以下链条验证：

```
SKILL.md / references 规则
  → 复合规则 ID（如 P148 或 PG3268·P2）
  → `06-source-index.md` 的 PG 身份/版本/FULL 状态
  → 规则条目中的 PG ID + 行号短引文
  → 工作区原始整本底本（P2 审计已核 SHA/行数）
```

抽查示例：规则“P148 幽灵携钥”应回到 PG11610 L578–594；P2 已确认该底本 SHA/行数与可信 FULL 身份一致。


### P4 返工修订：实际使用边界

逐源证据角色及本轮实际阅读可信度见 version-and-provenance.md。M21 原有怪物必须显形为 REJECT，M22 最优长度/密度 NOT_PROVEN，不能在其他索引中重新赋予有效规则地位。
