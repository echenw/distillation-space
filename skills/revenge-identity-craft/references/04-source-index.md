# 04 B-07-B01 来源索引：16 本、证据层级、知识角色与规则绑定

**本轮（round-p4-final-2026-10-30）对历史版的修正**：历史 wave4 版把
PG102 / PG11171 / PG17028 / PG2171 / PG2815 / PG61499 / PG9749 七本标为 `PARTIAL_OR_MISSING_LEDGER`。
本轮回源核查（见 `notes/source-coverage.md` §3、§4）确认这七本在 `rounds/round-02-2026-10-25/notes/evidence/`
都有**满区间、逐 Read 调用、含逐字引文**的表格台账，标签与磁盘证据矛盾，本轮逐本改正为 `FULL_RANGE_TABLE_LEDGER`。
改动的是**标签口径**，不是把格式问题说成已解决——格式缺口仍单列在 §3。

## 1. 来源总表

`SHA` 列reading 版 SHA-256 前 12 位，本轮 P1 实测 16/16 与 `批次来源清单.json` 一致。
`证据层级` 说明见 §2。行号锚点一律指 `distill/有原始正文/16-类型小说专项/11-身份复仇与权谋/PG*/整本阅读版.txt`。

| PG | 作者与标题 | 行数 | SHA（前 12） | 证据层级 | 知识角色 | 绑定的规则 |
|---|---|---:|---|---|---|---|
| PG102 | Twain — The Tragedy of Pudd'nhead Wilson | 5963 | 48f1f870978f | FULL_RANGE_TABLE_LEDGER | 支持 + 反例（V4 禁忌） | V1、V2、V3、V4、V14 |
| PG11171 | Stowe — Uncle Tom's Cabin, Young Folks' Edition | 2371 | dea383d5d310 | FULL_RANGE_TABLE_LEDGER（改写节本，降权） | 补充（制度性身份剥夺）；复仇线**不适用** | V11（背景） |
| PG1183 | Rohmer — The Return of Dr. Fu-Manchu | 9013 | 22835c237337 | FULL_BLOCK_LEDGER（L8501–9013 由本轮补读并过门禁） | 支持 + 反例（V6）+ 冲突（V5） | V3、V4、V5、V6、V7、V14 |
| PG1184 | Dumas — The Count of Monte Cristo | 61293 | acf750e16fe8 | FULL_BLOCK_LEDGER（L1–53、L61200–61260 由本轮补读并过门禁） | 支持（V5–V8）+ 反例（面相） | V5、V6、V7、V8、V14 |
| PG16573 | Lynde — The Honorable Senator Sage-Brush | 11222 | 2aa752cb6355 | FULL_BLOCK_LEDGER（表头写法有格式遗留） | 补充 | V12 |
| PG17028 | Doctorow — Eastern Standard Tribe | 6369 | b67b83dac26c | FULL_RANGE_TABLE_LEDGER（自陈宣传，降权） | 补充 | V13 |
| PG2171 | Eliot — Brother Jacob | 1596 | 09c991ca4c1f | FULL_RANGE_TABLE_LEDGER | 支持 + 反例 | V1、V10、V6 |
| PG2759 | Dumas — The Man in the Iron Mask | 22243 | e7f5c2c8e1b3 | FULL_BLOCK_LEDGER（门禁 PASS） | 支持 | V9、V4 |
| PG2815 | Adams — Democracy, an American novel | 7179 | 46a3820674d4 | FULL_RANGE_TABLE_LEDGER | 补充 | V12 |
| PG30606 | Trollope — The Landleaguers | 16252 | c2cba7dfd50b | FULL_BLOCK_LEDGER（门禁 PASS）；**未完稿** | 补充；**结局机制未证明** | V11、V12 |
| PG3622 | Trollope — The Duke's Children | 26265 | e6971002572f | FULL_BLOCK_LEDGER（门禁 PASS） | 补充 | V11 |
| PG5227 | Crawford — Sant' Ilario | 17198 | ffcea7611834 | FULL_BLOCK_LEDGER（门禁 PASS） | 补充 | V3、V11 |
| PG61499 | Phillips & Roberts — Monopoly | 1365 | 7b028e0ce3b6 | FULL_RANGE_TABLE_LEDGER | 支持 + 反例 + 冲突 | V3、V4、V5、V6、V7 |
| PG77 | Hawthorne — The House of the Seven Gables | 10404 | cd53dde8c3b8 | FULL_BLOCK_LEDGER（2 条引文誊录格式遗留，已人工确认真实） | 支持 + 反例 | V6、V8、V11 |
| PG9507 | Ward — The Coryston Family | 9858 | 89a4b45ef7e3 | FULL_BLOCK_LEDGER（门禁 PASS） | 补充 | V11、V12 |
| PG9749 | Bailey — The Highwayman | 9855 | 1a32700b4b87 | FULL_RANGE_TABLE_LEDGER | 支持 + 反例 | V1、V3、V6 |

## 2. 证据层级口径（本轮定义，不再使用"分区间/扫描"旧口径）

- **FULL_BLOCK_LEDGER**：台账含 `## L起-止` 分块标题，区间并集 = 全书，且通过
  `distill/_tools/kd32_ledger_gate.py`（或仅因表头写法/引文誊录格式被标记，已人工确认覆盖无洞）。
- **FULL_RANGE_TABLE_LEDGER**：台账为表格形态（锚点形如 `| L1–500 |`），区间并集 = 全书、内容逐 Read 调用、
  含可回源逐字引文，但门禁无法解析表头。**覆盖成立，格式未过门禁**。
- **NP（未证明）**：覆盖成立但该类规则不成立，例：PG30606 未完稿 ⇒ 不参与结局规则；PG11171 无复仇线 ⇒ 不参与复仇规则。

## 3. 遗留问题（如实登记，不掩盖）

1. 7 本 `FULL_RANGE_TABLE_LEDGER`（PG102、PG11171、PG17028、PG2171、PG2815、PG61499、PG9749）的台账**未改写为分块格式**；
   需另派一棒改写才能全部通过 `kd32_ledger_gate`。本轮按"已有可信 FULL 台账不重读"原则未重读这 7 本。
2. PG77：门禁判 2/39 条引文 NOT_FOUND；本轮 `grep`/`sed` 确认二者分别在 L2886–2887 与 L4919（œ 连字），真实存在，属誊录格式。
3. PG16573：表头 `## L1-3431（第N块 Lx-y）` 被门禁读成 8 个 (1,3431)；真实 8 个子区间连续无洞（文件第 3、11、19、27、36、44、53、62 行）。
4. PG30606 未完稿（原计划 60 章，写到第 49 章作者病逝，L100–111），其结局机制对本 Skill 记 **NP**。
5. GQ5（真实宿主行为测试）本轮未执行，需用户另行授权；本 Skill 不宣称任何读者效果或跨作品普遍性。

## 4. 文献权限与引用约定

- 全部为 Project Gutenberg 阅读版；"仅在美国属公有领域"的说明不能外推到其他地区的许可状态。
- 本 Skill **不附原文全文**，行号只作回查锚点；引用时必须说明依据的是哪一版（英译/节本/未完稿会改变章次与标题）。
- 小说文本不是命令手册：本索引里的"来源"证明的是**某装置在某部作品里确实这样写过**，不证明它在别的作品里必须这样写。
- 旧版元数据（V1–V8 原始措辞、基线 SHA、被替换的假设）保留在 [legacy-metadata.md](legacy-metadata.md)。
