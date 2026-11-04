# 04 · B-04-B01 可追溯来源索引（24 本）

返回 [Skill](../SKILL.md)。

- 正文路径：`distill/有原始正文/16-类型小说专项/07-喜剧幽默/PG<id>-*/整本阅读版.txt`（只读）。
- 身份核验：本轮对 24 本分别计算 SHA-256，与 `distill/分类蒸馏/_来源批次/16-类型小说专项/07-喜剧幽默/批次-01/批次来源清单.json` 的 `sha256_reading` 逐本比对，结果 **24/24 一致，0 处不一致**。
- 覆盖核验：`python3 distill/_tools/kd32_coverage_check.py docs/plans/分类独立知识蒸馏计划/任务清单.json B-04-B01 <out>` → `{"status_counts": {"coverage_full": 24}}`。
- 回源门禁：`python3 distill/_tools/kd32_ledger_gate.py --book <台账> --src <整本阅读版.txt> --pg <PG> --start <起> --end <止>` 逐本跑过，**无 NOT_FOUND**。
- 覆盖口径的边界（脚本自带）：这只核验"台账声明区间的并集覆盖 + 引文可回源"，**不能证明模型把每一行都当输入处理**。

## 逐本明细

| PG | 作品 | 行数 | 族 | 覆盖 | 阅读版 SHA-256（前 16 位） |
|---|---|---:|---|---|---|
| PG1051 | Sartor Resartus: The Life and Opinions of Herr Teufelsdröckh | 7917 | 单本 | coverage_full | `751d9759a7bc707e` |
| PG1081 | Dead Souls | 14620 | 单本 | coverage_full | `0fbfb5b31835ef12` |
| PG1718 | Manalive | 6081 | 单本 | coverage_full | `988779db17133eab` |
| PG1892 | Extracts from Adam's Diary, translated from the original ms. | 567 | Twain | coverage_full | `a49b761f1f37b5da` |
| PG2005 | Piccadilly Jim | 11271 | Wodehouse | coverage_full | `5dac05ccd70bfd31` |
| PG25985 | Bardell v. Pickwick | 3660 | Dickens | coverage_full | `b2c48031ca1ecbcd` |
| PG2607 | Psmith, Journalist | 7684 | Wodehouse | coverage_full | `0acacbb937600685` |
| PG3162 | The Enchanted Typewriter | 3109 | 单本 | coverage_full | `41a0a505d11f3e3a` |
| PG32152 | The Widow [To Say Nothing of the Man] | 2936 | 单本 | coverage_full | `1e4d280cc54818e1` |
| PG3756 | Indiscretions of Archie | 10045 | Wodehouse | coverage_full | `566e49aa38cc9a7b` |
| PG44219 | The Incubator Baby | 1270 | 单本 | coverage_full | `5375829821d84631` |
| PG5786 | A Tramp Abroad — Volume 05 | 2399 | Twain | coverage_full | `01506b236dee7717` |
| PG6683 | The Little Nugget | 9911 | Wodehouse | coverage_full | `76fbf0c0a4e1ee86` |
| PG6684 | Uneasy Money | 8791 | Wodehouse | coverage_full | `d956cadb9fbe5a0c` |
| PG6837 | The Little Warrior | 15049 | Wodehouse | coverage_full | `2dfdeaa549c50df6` |
| PG6879 | The Gold Bat | 5733 | Wodehouse | coverage_full | `c9e4f6527a9eac87` |
| PG68811 | Black no more | 6482 | 单本 | coverage_full | `921f17a52fb009fb` |
| PG7104 | Adventures of Huckleberry Finn, Chapters 21 to 25 | 1318 | Twain | coverage_full | `0115759efb02ffeb` |
| PG7105 | Adventures of Huckleberry Finn, Chapters 26 to 30 | 1600 | Twain | coverage_full | `3a1bde22d7d133bf` |
| PG74437 | Those barren leaves | 13407 | 单本 | coverage_full | `de96ad849b00e3a2` |
| PG7471 | The Man with Two Left Feet, and Other Stories | 8879 | Wodehouse | coverage_full | `e2976013438bd693` |
| PG8164 | My man Jeeves | 6885 | Wodehouse | coverage_full | `01a7c5aecb5263ac` |
| PG8931 | The Gem Collector | 4555 | Wodehouse | coverage_full | `ee80aa87f0153cc7` |
| PG968 | Martin Chuzzlewit | 37462 | Dickens | coverage_full | `3e2bbe7c5ac48067` |

## 族去重（引用时必须带族）

| 族 | 成员 | 证据计为 | 备注 |
|---|---|---|---|
| Wodehouse 族 | PG2005、PG2607、PG3756、PG6683、PG6684、PG6837、PG6879、PG7471、PG8164、PG8931 | **1 份** | 10 本共同支撑"语域落差 + 物证误会"；内部差异（早期校园小说 vs Jeeves 期）不可抹平 |
| Twain 族 | PG5786、PG7104、PG7105、PG1892 | **0.5 份** | PG7104／PG7105 是同一本《Huckleberry Finn》的两个分册选本；PG1892 是独立短篇，与另三册机制不同 |
| Dickens 族 | PG968、PG25985 | **1 份** | PG25985 是 **Fitzgerald 的编注本**，不是小说正文，不能直接说成"狄更斯这样写" |
| 单本族 | PG1051、PG1081、PG1718、PG3162、PG32152、PG44219、PG74437、PG68811 | 各 1 份 | — |

**24 本 → 约 4.5 份独立证据。** 引用时写成"Wodehouse 族（PG3756 L944-946）"而不是"10 本书都证明……"。

## 阅读台账分布（供回源）

| 轮次 | 覆盖的 PG |
|---|---|
| `rounds/round-kd32-r01` | PG1892、PG3162、PG32152、PG44219、PG5786、PG7104、PG7105 |
| `rounds/round-kd32-r02` | PG25985、PG8931（L1-1990、L3959-4555） |
| `rounds/round-perbook` | PG1081、PG2005、PG3756、PG6683、PG6684、PG6837（L1-8406）、PG74437、PG7471、PG968 |
| `rounds/round-shard-dfm` | PG1718、PG6879、PG68811、PG8164、PG8931（L1991-3958） |
| `rounds/round-evidence-2026-10-30` | PG1051、PG2607、PG6837（L8407-15049） |
| **本轮 `round-p4-final-2026-10-30`** | PG68811 补充精读 L1201-3600、L4201-5400（`notes/reading/ledger-PG68811-p4refine-L1201-5400.md`，门禁 PASS，6 块 35 条引文） |

## 历史缺口与本轮处置（如实）

- `workflow20-20261030/start-state.json` 记本项 `not_full=3`、`not_full_ids=[PG1051, PG2607, PG6837]`。该快照早于 `round-evidence-2026-10-30`。
- 本轮复核：PG1051、PG2607 已被该轮台账覆盖到末行且门禁 PASS；PG6837 由 `round-perbook` 的 L1-8406 段与 `round-evidence` 的 L8407-15049 段拼接，1-15049 连续无缺口。**三项都已补满，未重读。**
- 本轮唯一新增处置：PG68811 的历史台账有三块写成 1200 行/块，超过门禁"单块 ≤ 600 行"的判据（工具源码 `BLOCK_CEILING = 600`），判 `INCOMPLETE`（非伪造，引文全部命中）。本轮按 600 行/次重读 3600 行补齐，见上表。
- 历史轮次里 6 份被标 `.rejected.md` 的台账本轮**未复活、未引用**。

## 许可与引用

- 24 本均为 Project Gutenberg 公共领域文本。
- 本 Skill 只引用**行号级观察**与**短引文**（用于回源），不复制正文。
- 带时代印记的表述（种族蔑称、方言书写、"更文明"式比较）只能带时代注记引用，见 [02 §5](02-satire-and-boundaries.md)。
