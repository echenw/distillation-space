# 来源索引、已读范围与降权纪律（A-06-B03）

## 基线

| 项目 | 值 |
|---|---|
| 任务 | A-06-B03 ｜ `16-类型小说专项/05-科幻未来/批次-03` |
| 来源数 | 28 本（与 `任务清单.json.source_ids` 一致） |
| 行号基准 | 每本 `整本阅读版.txt`（与 `批次来源清单.json.sha256_reading` 对应） |
| SHA 核验 | 28/28 MATCH（逐本 `sha256(整本阅读版.txt)` 比对清单） |
| 台账 | 39 份（历史 38 + 本轮补 1） |
| 台账门禁 | PASS 38 ／ FABRICATED 1（历史件 PG1329 L1-6000，已隔离，见下） |
| 覆盖 | 97814 行，未读 0 行 |

## 降权纪律（引用前必读）

同作者/同系列按**一组**计，不按本数计：

| 组 | 成员 | 计为 |
|---|---|---|
| Bellamy | PG624、PG7303 | 1 组 |
| Wells | PG35、PG36 | 1 组 |
| Harry Harrison | PG21873、PG29204 | 1 组 |
| Basil Wells | PG64350、PG79464 | 1 组 |
| William W. Stuart | PG31038、PG51460 | 1 组 |

**→ 28 本 = 22 个独立作者组。** 任何"N 本都这样"必须换算到 22。

## 逐本已读范围与角色

| PG | 作品 | 行数 | 覆盖区间 | 独立组 | 角色 | 门禁 |
|---|---|---:|---|---|---|---|
| PG35 | The Time Machine | 3174 | L1-931 / L932-1832 / L1833-2719 / L2720-3174 | Wells | 支持（核心） | PASS ×4 |
| PG36 | The War of the Worlds | 6370 | L1-6000 / L6001-6370 | Wells | 支持 | PASS ×2 |
| PG624 | Looking Backward | 7766 | L1-6000 / L6001-7766 | Bellamy | 支持（核心） | PASS ×2 |
| PG7303 | Equality | 15532 | L1-15532 | Bellamy | 支持 | PASS |
| PG1329 | A Voyage to Arcturus | 12232 | L1-4873 / **L4874-6000（本轮）** / L6001-12000 / L12001-12232 | Lindsay | 支持 + 冲突 | PASS ×3 ＋ 1 历史件 FABRICATED |
| PG13944 | After London | 8223 | L1-6000 / L6001-8223 | Jefferies | 支持（核心） | PASS ×2 |
| PG20869 | The Skylark of Space | 9968 | L1-6000 / L6001-9968 | E. E. Smith | 反例 | PASS ×2 |
| PG21873 | Planet of the Damned | 6517 | L1-6000 / L6001-6517 | Harrison | 支持 | PASS ×2 |
| PG29204 | Arm of the Law | 794 | L1-794 | Harrison | 支持 + 冲突 | PASS |
| PG27595 | Eight Keys to Eden | 6579 | L1-6000 / L6001-6579 | Clifton | 支持 + 补充 | PASS ×2 |
| PG4340 | The British Barbarians | 3673 | L1-3673 | Grant Allen | 支持（核心） | PASS |
| PG30963 | A Knyght Ther Was | 2155 | L1-2155 | R. F. Young | 支持 | PASS |
| PG51344 | Voyage to Far N'jurd | 2241 | L1-2241 | Neville | 支持 | PASS |
| PG22512 | The Stutterer | 1347 | L1-1347 | Merliss | 支持 | PASS |
| PG22559 | The Day of the Boomer Dukes | 980 | L1-980 | Pohl | 支持 + 补充 | PASS |
| PG59438 | Avoidance Situation | 1812 | L1-1812 | McConnell | 支持（核心） | PASS |
| PG31976 | Derelict | 801 | L1-801 | Nourse | 支持（核心） | PASS |
| PG51588 | Security Plan | 456 | L1-456 | Farrell | 支持（核心） | PASS |
| PG51623 | Always a Qurono | 665 | L1-665 | Harmon | 支持（核心） | PASS |
| PG64350 | Among the Scented Ones | 805 | L1-805 | Basil Wells | 补充 | PASS |
| PG79464 | Monster No More | 929 | L1-929 | Basil Wells | 补充 + 支持 | PASS |
| PG31215 | A World Apart | 869 | L1-869 | Merwin | 支持 | PASS |
| PG31038 | The Real Hard Sell | 730 | L1-730 | W. W. Stuart | 支持 + 补充 | PASS |
| PG51460 | A Husband for My Wife | 646 | L1-646 | W. W. Stuart | 支持 | PASS |
| PG59558 | Your Servant, Sir | 624 | L1-624 | Boren | 支持（核心） | PASS |
| PG29976 | Weak on Square Roots | 382 | L1-382 | Burton | 支持 | PASS |
| PG32636 | The Salesman | 172 | L1-172 | Boyd | 支持（核心） | PASS |
| PG31519 | Narakan Rifles, About Face! | 1372 | L1-1372 | Jan Smith | 支持 + 反例 | PASS |

## 已知证据缺陷（引用时必须同时说明）

1. **PG1329 历史台账 `ledger-PG1329-s1-6000.md`**（`round-shard-glm`）
   门禁判定 FABRICATED：覆盖缺口 L4874-6000 ＋ 2 条引文失配。
   - 缺口已由本轮 `ledger-PG1329-s4874-6000.md` 补齐（门禁 PASS）。
   - 2 条失配引文经 `grep -n` 回源确认**行号与内容均真实存在**，
     但台账删去了对话提示语并改写标点，故不构成逐字引文。
     涉及 L2473-2475 与 L3619-3623 的证据降为**概述级**，详见 `notes/pg1329-quote-correction.md`。
2. **大部头的结构化摘录**：PG7303、PG20869×2、PG624×2、PG13944×2、PG1329×2、PG59438
   这 10 份台账体量 >60KB，本轮融合采用"分块标题 + 每块首条要点 + 已过门禁引文"的结构化摘录，
   未做逐行二次重读。其**章级叙事节奏**的证据强度低于标注为"支持（核心）"且逐行读过的来源。

## 引用格式

- 位置：`PGXXXX L起-止`（行号基准 = `整本阅读版.txt`）。
- 逐字引文：英文短引 ≤25 词，且必须是台账中已通过门禁回源核验的片段。
- 未经台账覆盖的行号一律不得引用；需要时写 `NOT_PROVEN`。
