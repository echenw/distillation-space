# 原文来源索引（round-p4-final-2026-10-30）

本表由本轮重新生成：逐本读取 `distill/分类蒸馏/_来源批次/16-类型小说专项/09-职业与竞技/批次-02/PG*/整本阅读版.txt`，行数与 SHA 均为本轮实测，并与 `批次来源清单.json` 的 `sha256_reading` 逐本比对（23/23 一致）。
路径相对于项目根目录 `knowledge-distillation-workspace/`。

**证据强度说明（必须一起看）**
- `区块型台账·本轮通过门禁`：本轮产出或修正，已用 `distill/_tools/kd32_ledger_gate.py --book … --src … --start 1 --end <总行数>` 逐条回源通过。
- `区块型台账·门禁 PASS（非本轮实读）`：历史台账，本轮用同一门禁复核通过，但本轮未重读。
- `表格型证据·前轮按行验证`：前轮 `p2-source-verification.json` 的 `RECOVERED_RICH_TABLE_LEDGER` 判定（逐行记录 quotes_total / verified_quotes）；**区块型门禁要求 `## L起-止` 分块，对这批文件报"无分块/无引文"，本轮未能用同一把尺复核**。它们不阻断 P4 收口，但不得称为"本轮实读"。

| PG | 书名 | 可信/总行数 | 状态 | 证据强度 | 阅读版 SHA-256 | 本轮说明 |
|---|---|---|---|---|---|---|
| PG154 | The Rise of Silas Lapham | 14557 | FULL | 区块型台账·门禁 PASS（非本轮实读） | 4d5305b710ff9b22c54c9fbd19ceee3c68e1abe94d44f13a8b175a7a4ad4e4bb | 37 块 |
| PG717 | Chita: A Memory of Last Island | 2848 | FULL | 区块型台账·本轮通过门禁 | 03df148e36e044248912514046fd1910c558804277c4458cecd28a389836055e | 本轮全文实读 5 块/15 引文 |
| PG1449 | The Valley of the Moon | 18988 | FULL | 区块型台账·门禁 PASS（非本轮实读） | e9c6f65c093f31646491afc58678c26647fe425039d38ead8300ec2cb28f2ecb | 39 块 |
| PG2153 | Mary Barton | 18012 | FULL | 区块型台账·门禁 PASS（非本轮实读） | 40096f6ac739b618b5a0e6fd6ee3e799171a6df4a9937402709635980c5e5aba | 40 块 |
| PG2715 | The Real Thing and Other Tales | 6760 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | f4992c5c1a6f992fc630d58bff51ceedafb48f078af4d72219547f8f57917999 | — |
| PG3016 | What Diantha Did | 7032 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 1a0f30c0408d0c84662cb1c0ebc819e405503ea38a289508f2230a887ea6758e | — |
| PG3659 | The Rosary | 11627 | FULL | 区块型台账·本轮通过门禁 | 89e0da49165406372de1aee75179e7b377e5190751f604c03b3b94fe1e1a5f3d | 继承台账＋本轮引文修正（37 块/58 引文） |
| PG4217 | A Portrait of the Artist as a Young Man | 9870 | FULL | 区块型台账·本轮通过门禁 | f8ca722507d5eff29c484ecd8bf5cb35e22c1ed892b05bf576f40c1058474b34 | 继承台账＋本轮引文修正（30 块/90 引文） |
| PG4274 | Wives and Daughters | 28838 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 820e2aa9765940201855d0ba8b158154519ea54975c59690aabd08284fb2f4d4 | — |
| PG4353 | Five Thousand an Hour: How Johnny Gamble Won the Heiress | 7582 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | ea86eba95802c0c2a79ec3393afce1863b33c9d8938b67cd0ae5bb5c8da9847b | — |
| PG4645 | The Landlord at Lion's Head — Complete | 12947 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | c011a44e8fb141f31dc5669e7dee3ea3ec5e6e3361387331befd4e653efecc09 | — |
| PG6884 | Sleeping Fires: a Novel | 6108 | FULL | 区块型台账·本轮通过门禁 | 5ce758437bb2bfa80e8c1feb8e61e2f911d4c20573f47c6f8cbcf716e2724743 | 继承表格台账→结构改写＋本轮 8 处窗口实读，11 块/11 引文 |
| PG8374 | Alton Locke, Tailor and Poet: An Autobiography | 18467 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 7bdabd6cfdff428c2d4382569c7de4499c53459fe6c36ad86e1009574d544443 | — |
| PG9385 | The Incomplete Amorist | 12361 | FULL | 区块型两段：L1-1500 本轮实读 PASS（两份独立台账：wave 补证 5 块/14 引文＋2026-10-31 台账补齐 run 3 块/6 引文）+ L1501-12361 继承 perbook PASS | c79bd896a3adfb81c8a12a6badf220d3d483c57900687768ee9f1ab2aa9a619e | 5 块/14 引文 + 3 块/6 引文 + 22 块/157 引文 |
| PG10911 | Buried Alive: A Tale of These Days | 6976 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 32130cdcdf7980dcaf6d479606fdaad4138c63746feccf37c4823df0dce04000 | — |
| PG11715 | The Eyes of the World | 12718 | FULL | 区块型台账·门禁 PASS（非本轮实读） | 7849a26753e5d8f1d0a2c22f6a9bdc6c2c4f81aae610b5bff9e6ca32ad1d2b21 | 32 块 |
| PG17020 | The False Gods | 2171 | FULL | 区块型台账·本轮通过门禁 | d3c695e8a1ac88451487bdf296b866d0b0e6082c3e1f52d1b77fb79c37502103 | 本轮全文实读 4 块/10 引文 |
| PG17647 | The Strange Case of Cavendish | 10311 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 17c73955cbccb3123a46563c2641b329cd9f733f18ec528706844c56c5b02834 | — |
| PG23701 | The Man In The High-Water Boots | 554 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 360ce578889b50f52e02afb9a8f3d433a16632097c5c673f5184d481f6a029ce | — |
| PG25017 | A Son of the Immortals | 8789 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | 2cc29be43846602f9066372dc886e156617070d553cca1a36331247bb60c28ca | — |
| PG41154 | The Walking Delegate | 11195 | FULL | 区块型台账·本轮通过门禁 | 8191e5f45bb89f5e35d0400b761ac61a08819a8913b737c67cc14ea433780f57 | 继承台账＋本轮引文修正＋实读 L4935-5334（28 块/146 引文） |
| PG64840 | Healing Rays in Space | 1135 | FULL | 表格型证据·前轮按行验证（本轮未能用区块门禁复核） | cf0c27ea154180399ed177f700915bbbc0f236df540d5a49cdf41de500cfe494 | — |
| PG78245 | The Mudfog papers, etc. | 3199 | FULL | 区块型台账·本轮通过门禁 | cc33ab2b588b80dea282b827be254443e23535e8fe8ca2d914bc61ab39d2756f | 本轮全文实读 6 块/27 引文 |

## 证据路径（本轮新增／变更的 7 本）

- **PG17020** — 原文 `distill/分类蒸馏/_来源批次/16-类型小说专项/09-职业与竞技/批次-02/PG17020-The-False-Gods/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG17020-L1-2171.ledger.md`（本轮全文实读）。**正文止于 L1729**，L1731-2171 为出版商广告页，不得当情节证据。
- **PG717** — 原文 `…/PG717-Chita-A-Memory-of-Last-Island/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG717-L1-2848.ledger.md`（本轮全文实读）。
- **PG78245** — 原文 `…/PG78245-The-Mudfog-papers-etc/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG78245-L1-3199.ledger.md`（本轮全文实读）。
- **PG6884** — 原文 `…/PG6884-Sleeping-Fires-a-Novel/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG6884-L1-6108.ledger.md`（继承 round-05 表格台账 → 结构改写 + 本轮 8 处窗口实读）。
- **PG4217** — 原文 `…/PG4217-A-Portrait-of-the-Artist-as-a-Young-Man/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG4217-L1-9870.inherited-fixed.md`。
- **PG41154** — 原文 `…/PG41154-The-Walking-Delegate/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG41154-L1-11195.inherited-fixed.md`。
- **PG3659** — 原文 `…/PG3659-The-Rosary/整本阅读版.txt`；本轮证据 `rounds/round-p4-final-2026-10-30/notes/reading/PG3659-L1-11627.inherited-fixed.md`。

## 其余来源的证据路径（沿用前轮，未改动）

- PG11715 / PG1449 / PG154 / PG2153：`rounds/round-perbook/notes/reading/ledger-PG<id>-full.md`。
- PG9385：`rounds/round-p4-final-2026-10-30/notes/reading/ledger-PG9385-1-1500.md`（L1-1500，wave 补证，5 块/14 引文 PASS）+ `rounds/round-p4-final-2026-10-30/notes/reading/ledger-PG9385-L1-1500.md`（L1-1500，2026-10-31 台账补齐 run 全本实读、门禁 PASS，3 块/6 引文；两份独立台账覆盖同一区间，引用时任一行号在两份中均可回源）+ `rounds/round-perbook/notes/reading/ledger-PG9385-full.md`（L1501-12361，22 块/157 引文 PASS）。
- **2026-10-31 台账补齐 run 追记**：PG9385 L1-1500（此前唯一缺口段）自此有两份互为印证的门禁 PASS 台账；本 Skill 0.3.1 新增的 F（R2/R4/R6/R9/R12 及例 B）全部挂 `ledger-PG9385-L1-1500.md` 与 `ledger-PG9385-1-1500.md` 的行号，均为 L1-1500 区间证据，不得外推至 L1501-12361。
- PG10911 / PG25017 / PG2715 / PG3016 / PG4353：`rounds/round-05-2026-10-25/notes/evidence/PG<id>.ledger.md`。
- PG17647：`rounds/round-05-2026-10-25/notes/evidence/PG17647.ledger.md` + `rounds/round-p4-wave4-agent3-final-2026-10-30/notes/reading/PG17647-gaps.md`。
- PG23701：`rounds/round-p4-wave4-agent3-final-2026-10-30/notes/reading/PG23701-full.md`。
- PG4274 / PG4645 / PG8374：`rounds/round-perbook/notes/reading/ledger-PG<id>-full.md` + `rounds/round-p4-wave4-agent3-final-2026-10-30/notes/reading/PG<id>-gaps.md`。
- PG64840：`rounds/round-p4-wave4-agent3-final-2026-10-30/notes/reading/PG64840-full.md`。

## 未完成的验收

- **23/23** 按旧口径有可回源覆盖证据；PG9385 新实读 L1-1500（wave 补证 + 2026-10-31 补齐 run 两份台账）与历史 perbook L1501-12361 分别 PASS。8 本有全本区块门禁证据；15 本依赖表格型或继承证据，不能视为本轮全文重读。
- P5/GQ5 真实宿主任务未执行，不得把静态结构检查称为真实验收。
- 体育赛制、青训、经纪合约、现实医疗/法律条款在本批无来源，一律 `UNRESOLVED`。
