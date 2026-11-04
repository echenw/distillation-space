# sources.md — 来源索引与审计

批次：16-类型小说专项/06-历史架空/批次-02（A-07-B02）
阅读方式：Main-03 SOLO 全文实读，无子代理、无抽样；逐本 ledger（批锚点+覆盖自检）与证据卡见 `rounds/round-01-2026-10-25/notes/evidence/main-solo/`
权威清单：`distill/分类蒸馏/_来源批次/16-类型小说专项/06-历史架空/批次-02/批次来源清单.json`（source_count=15；o200k_tokens 合计 2,686,878，与本表逐项相加一致）

| PGID | 书名 | 作者/年代 | o200k | 批数 | SHA256(reading) 前后段 |
|---|---|---|---|---|---|
| PG271 | Black Beauty | Anna Sewell, 1877 | 76,097 | 5 | 6630d911f45f…7765 |
| PG324 | A Knight of the Cumberland | John Fox Jr., 1906 | 28,313 | 4 | 06d0799f3fac…0a93 |
| PG1036 | Joe Wilson and His Mates | Henry Lawson, 1901 | 115,547 | 7 | 589fe138f6bc…e9a7 |
| PG1678 | An Historical Mystery / The Gondreville Mystery | Honoré de Balzac, 1842 | 104,681 | 7 | a1251e0439b1…2d90 |
| PG2609 | The Vicomte de Bragelonne（前 75 章） | Alexandre Dumas, 1847-50 | 268,537 | 22 | 3aacfdc880c3…af8b |
| PG3350 | The Wandering Jew — Complete | Eugène Sue, 1844-46 | 742,406 | 51 | 2faa614ded67…097c |
| PG5709 | La Vendée | Anthony Trollope, 1850 | 240,136 | 14 | 331b84a02e52…1d9d |
| PG6407 | The Abbot | Sir Walter Scott, 1820 | 254,809 | 16 | 9fd5cd027ed1…d963 |
| PG79489 | The grandmothers | Glenway Wescott, 1927 | 139,029 | 9 | 3c694d420be1…fda1 |
| PG10046 | Salute to Adventurers | John Buchan, 1915 | 122,371 | 8 | 8d259c3e8222…2cf8 |
| PG1461 | A Legend of Montrose | Sir Walter Scott, 1819 | 125,376 | 8 | 0399b92660e0…36e8 |
| PG24789 | "Unto Cæsar" | Baroness Orczy | 149,018 | 11 | 8fc24acd42d5…075d |
| PG33208 | The Laughing Cavalier | Baroness Orczy, 1924 | 174,474 | 13 | 3128baeff082…1f06 |
| PG46345 | Sir Quixote of the Moors | John Buchan, 1895 | 35,945 | 3 | a9968a9c07db…7c42 |
| PG56562 | Kidnapped (Illustrated) | R. L. Stevenson, 1886 | 110,139 | 8 | 37a6b44de7df…df46 |
| **合计** | 15 源 | 1842-1927 | **2,686,878** | 184 批 | 读前逐本 hashlib 实算与清单一致 |

审计要点：

1. 每本读前以 hashlib 实算整本阅读版.txt 的 SHA256，与批次来源清单的 sha256_reading 逐字符比对通过后方可开读。
2. 每本按 1,200 行/批连续 Read（批数=ceil(行数/1200)），ledger 记录批锚点（行区间+章节位置+内容要点）；读毕填写覆盖自检（批数×行数=总行数、SHA 已核、无抽样、EOF 验证）。
3. 子类型分布：苏格兰历史罗曼司 3、Buchan 系冒险 2、法兰西历史冒险 3、法兰西社会史诗 3、边疆/殖民地罗曼司 3、美国家族编年史 1（见 fusion-matrix.md 第一节）。
4. 时代语料降级条款（RE-22）覆盖 PG24789/PG1036/PG3350/PG79489 的殖民、阶级与种族语料；技法可吸收、立场 REFUSE-UNCONDITIONAL。
