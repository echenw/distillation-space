# 05 · 来源索引（PG / Token / SHA-256 / 台账 / 覆盖 / 门禁）

本文件由脚本从 `_来源批次/16-类型小说专项/02-言情爱情/批次-01/批次来源清单.json` 与各轮阅读台账实算生成，不是手抄。

生成命令（本轮实际执行）：`python3` 脚本调用 `distill/_tools/kd32_ledger_gate.py` 的 `check_ledger()`，对每本按 `[1, len(Source.lines())]` 全书区间核验。

| PG | 作品 | o200k tokens | sha256_reading（前16位） | 台账（相对 `rounds/`） | 行覆盖 | 分块 | 逐字引文 | 门禁 |
|---|---|---:|---|---|---|---:|---:|---:|---|
| PG471 | The Bride of Lammermoor | 175,294 | `891fe7f89df8e6d3` | `round-perbook/notes/reading/ledger-PG471-full.md` | L1-13556 / 13556 | 34 | 33 | **PASS** |
| PG821 | Dombey and Son | 495,072 | `30fbb4b4d653d6f8` | `round-perbook/notes/reading/ledger-PG821-full.md` | L1-39707 / 39707 | 89 | 88 | **PASS** |
| PG969 | The Tenant of Wildfell Hall | 232,553 | `c240eef53537a997` | `round-perbook/notes/reading/ledger-PG969-full.md` | L1-18477 / 18477 | 31 | 31 | **PASS** |
| PG1839 | Other Things Being Equal | 89,496 | `462571947a21e43d` | `round-perbook/notes/reading/ledger-PG1839-full.md` | L1-8478 / 8478 | 15 | 168 | **PASS** |
| PG1917 | The Queen of Hearts | 188,445 | `c06cdd297e87b9dd` | `round-perbook/notes/reading/ledger-PG1917-full.md` | L1-14905 / 14905 | 30 | 58 | **PASS** |
| PG3719 | The Mistletoe Bough | 12,602 | `3cfaf3045a2ca868` | `round-kd32-r01/notes/reading/ledger-PG3719-s1-1004.md` | L1-1004 / 1004 | 15 | 20 | **PASS** |
| PG3724 | The House of Heine Brothers, in Munich | 13,650 | `75328934279e6e89` | `round-kd32-r01/notes/reading/ledger-PG3724-s1-1076.md` | L1-1076 / 1076 | 13 | 12 | **PASS** |
| PG4275 | Ruth | 215,189 | `c7a856420ae97fd7` | `round-perbook/notes/reading/ledger-PG4275-full.md` | L1-17036 / 17036 | 31 | 11 | **PASS** |
| PG4398 | The Tides of Barnegat | 129,174 | `06876badecd4a7fe` | `round-perbook/notes/reading/ledger-PG4398-full.md` | L1-10608 / 10608 | 22 | 68 | **PASS** |
| PG4961 | Our Mr. Wrenn: The Romantic Adventures of a Gentle Man | 113,177 | `98b2563ff62958ad` | `round-perbook/notes/reading/ledger-PG4961-full.md` | L1-9629 / 9629 | 22 | 22 | **PASS** |
| PG11640 | Love and Mr. Lewisham | 93,413 | `ce1ddcaebae6d1c6` | `round-perbook/notes/reading/ledger-PG11640-full.md` | L1-8376 / 8376 | 17 | 34 | **PASS** |
| PG13180 | The Tracer of Lost Persons | 77,166 | `6073dd82c19244b3` | `round-perbook/notes/reading/ledger-PG13180-full.md` | L1-7576 / 7576 | 15 | 27 | **PASS** |
| PG15252 | Victorian Short Stories: Stories of Successful Marriages | 48,718 | `64d4911d537a05fe` | `round-kd32-r02/notes/reading/ledger-PG15252-s1-4045.md` | L1-4045 / 4045 | 34 | 34 | **PASS** |
| PG15473 | Love Stories | 98,282 | `d57013c49d4a92ea` | `round-perbook/notes/reading/ledger-PG15473-full.md` | L1-9318 / 9318 | 16 | 65 | **PASS** |
| PG15766 | The Claverings | 271,940 | `0b6d75946d978392` | `round-perbook/notes/reading/ledger-PG15766-full.md` | L1-22228 / 22228 | 41 | 39 | **PASS** |
| PG20533 | Jill the Reckless | 157,541 | `20e67cbcb6c8957b` | `round-perbook/notes/reading/ledger-PG20533-full.md` | L1-14973 / 14973 | 30 | 15 | **PASS** |
| PG21847 | Dr. Wortle's School | 105,543 | `9d978bb4a653bbc7` | `round-perbook/notes/reading/ledger-PG21847-full.md` | L1-8385 / 8385 | 18 | 96 | **PASS** |
| PG49282 | The Chronicles of the Imp: A Romance | 60,751 | `88f25d660ced79c9` | `round-shard-dfm/notes/reading/ledger-PG49282-s1-5796.md` | L1-5796 / 5796 | 11 | 16 | **PASS** |
| PG68273 | Love's bitterest cup | 131,830 | `068df2b8df1afb34` | `round-perbook/notes/reading/ledger-PG68273-full.md` | L1-12401 / 12401 | 25 | 50 | **PASS** |

- 合计：**19 本 / 2,709,836 o200k tokens**；全书覆盖且门禁 PASS：**19 本**；未达 FULL：**0 本**。
- 完整 SHA-256 见批次清单 JSON；本索引只列前 16 位以便阅读，核验以清单为准。
- 废弃台账不参与：`ledger-PG1917-full.rejected.md`、`ledger-PG4275-full.rejected.md`、`ledger-PG4398-full.rejected.md` 均为历史被拒稿，未计入上表。
- `ledger-PG471-s11601-13556.md`（round-kd32-r13）是 PG471 已覆盖区间的冗余重读，未改变 PG471 由 `ledger-PG471-full.md` 支撑 FULL 的结论。

## 引用格式

```
[F] PG3724:816-817 "They must either be earned or purchased."
[H] 登记不同，同一动作的观感完全不同。
[P] Rp2 给否决者一句信条、一次真实干预、一次失效。
```
