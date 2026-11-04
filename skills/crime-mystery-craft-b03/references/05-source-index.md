# 05 · 来源索引（30 份 / 23 个独立证据族）

原文只读路径统一为：
`distill/分类蒸馏/_来源批次/16-类型小说专项/01-推理悬疑刑侦/批次-03/<目录>/整本阅读版.txt`

覆盖与引文统计由本轮脚本重算（台账区间并集 + 门禁匹配器 `kd32_ledger_gate.py` 的 `Source.find_near()`）。**本表即为完整明细，只安装 skill 目录时以本表为准**；同批机器可读副本 `p2-source-verification.json` 位于轮次根目录（相对本文件为 `../../notes/p2-source-verification.json`，不在 skill 包内）。

`material_role` 30/30 = `FICTION_CASE`；`ENq`=英文逐字引文候选数，`OK`=回源命中数，`NF/NIR`=未命中/不在声明行号附近（多数为中文转述被当作引文登记所致，属登记格式问题，非伪造）。

| PG | 目录 | 书名 / 作者 | 行数 | 覆盖 | 块 | ENq | OK | NF | NIR | 可信度 | 角色 | 服务规则 |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|
| PG108 | `PG108-The-Return-of-Sherlock-Holmes` | The Return of Sherlock Holmes / Doyle | 13447 | 1.000 | 34 | 31 | 31 | 0 | 0 | TRUSTED_FULL | 补充 | R14（反例：baritsu 属不可迁移解法） |
| PG1685 | `PG1685-The-Mystery-of-the-Yellow-Room` | The Mystery of the Yellow Room / Leroux | 8806 | 1.000 | 23 | 292 | 166 | 14 | 112 | TRUSTED_FULL | 支持 | R7 R9 C1 |
| PG2019 | `PG2019-The-Bat` | The Bat / Benét | 8711 | 1.000 | 17 | 146 | 127 | 18 | 1 | TRUSTED_FULL | 补充 | R13 |
| PG2358 | `PG2358-The-After-House` | The After House / Rinehart | 6571 | 1.000 | 18 | 19 | 12 | 5 | 2 | TRUSTED_FULL | 支持 | R11b R1 |
| PG3803 | `PG3803-File-No-113` | File No. 113 / Gaboriau | 19960 | 1.000 | 37 | 39 | 34 | 1 | 4 | TRUSTED_FULL | 支持 | R6 R7 |
| PG46462 | `PG46462-Recollections-of-a-Policeman` | Recollections of a Policeman / Russell | 11362 | 1.000 | 31 | 51 | 51 | 0 | 0 | TRUSTED_FULL | 支持 | R5 R12 |
| PG55313 | `PG55313-The-Vanishing-of-Tera` | The Vanishing of Tera / Hume | 8204 | 1.000 | 16 | 142 | 135 | 6 | 1 | TRUSTED_FULL | 支持（反例） | R8 R1 |
| PG55617 | `PG55617-Monsieur-Judas-A-Paradox` | Monsieur Judas: A Paradox / Hume | 8262 | 1.000 | 17 | 243 | 227 | 15 | 1 | TRUSTED_FULL | 支持（反例） | R7 R9 C2 |
| PG55783 | `PG55783-Tracked-by-a-Tattoo-A-Mystery` | Tracked by a Tattoo: A Mystery / Hume | 10120 | 1.000 | 29 | 266 | 251 | 13 | 2 | TRUSTED_FULL | 支持 | R4 R10 |
| PG56087 | `PG56087-In-Queer-Street` | In Queer Street / Hume | 10735 | 1.000 | 26 | 204 | 199 | 5 | 0 | TRUSTED_FULL | 支持（反例） | R13 |
| PG56385 | `PG56385-Jonah-s-Luck` | Jonah's Luck / Hume | 12357 | 1.000 | 26 | 67 | 67 | 0 | 0 | TRUSTED_FULL | 补充 | R7 |
| PG56841 | `PG56841-The-Disappearing-Eye` | The Disappearing Eye / Hume | 11165 | 1.000 | 32 | 44 | 44 | 0 | 0 | TRUSTED_FULL | 支持 | R4 |
| PG56960 | `PG56960-The-Midnight-Guest-A-Detective-Story` | The Midnight Guest: A Detective Story / White | 9073 | 1.000 | 27 | 26 | 24 | 0 | 2 | TRUSTED_FULL | 补充 | R9 |
| PG57066 | `PG57066-The-Corner-House` | The Corner House / White | 8878 | 1.000 | 29 | 317 | 287 | 25 | 5 | TRUSTED_FULL | 支持 | R4 R7 C2 |
| PG58820 | `PG58820-Whose-Body-A-Lord-Peter-Wimsey-Novel` | Whose Body? A Lord Peter Wimsey Novel / Sayers | 7418 | 1.000 | 24 | 65 | 31 | 6 | 28 | TRUSTED_FULL | 支持 | R3 R10 C1 |
| PG59126 | `PG59126-Faulkner-s-Folly` | Faulkner's Folly / Wells | 7926 | 1.000 | 19 | 49 | 47 | 2 | 0 | TRUSTED_FULL | 支持 | R1 R2 R9 C2 |
| PG59369 | `PG59369-Murder-in-Black-Letter` | Murder in Black Letter / Anderson | 7443 | 1.000 | 15 | 73 | 65 | 4 | 4 | TRUSTED_FULL | 支持 | R9 |
| PG65790 | `PG65790-Under-the-Tiger-s-Claws-Or-A-Struggle-for-the-Right` | Under the Tiger's Claws; Or, A Struggle for the Right / Carter | 6637 | 1.000 | 21 | 39 | 35 | 3 | 1 | TRUSTED_FULL | 补充 | R10 |
| PG66756 | `PG66756-Dalrymple-s-Equation` | Dalrymple's Equation / Fairman | 648 | 1.000 | 5 | 6 | 6 | 0 | 0 | TRUSTED_FULL | 支持（反例） | R11 R13 C2 |
| PG67079 | `PG67079-The-Red-Lodge-A-Mystery-of-Campden-Hill` | The Red Lodge: A Mystery of Campden Hill / Bridges | 9425 | 1.000 | 28 | 256 | 235 | 20 | 1 | TRUSTED_FULL | 补充 | R13 |
| PG68153 | `PG68153-The-step-on-the-stair` | The step on the stair / Green | 11931 | 1.000 | 30 | 573 | 544 | 27 | 2 | TRUSTED_FULL | 支持 | R10 |
| PG68810 | `PG68810-The-nameless-man` | The nameless man / Lincoln | 8326 | 1.000 | 16 | 29 | 20 | 6 | 3 | TRUSTED_FULL | 不适用 | — |
| PG68951 | `PG68951-The-gray-brotherhood` | The gray brotherhood / Leverage | 1268 | 1.000 | 6 | 2 | 2 | 0 | 0 | FULL_MINQ | 补充 | R10 |
| PG69004 | `PG69004-The-Trevor-case` | The Trevor case / Lincoln | 7082 | 1.000 | 35 | 203 | 126 | 11 | 66 | TRUSTED_FULL | 支持 | R1 R7 R11a |
| PG70924 | `PG70924-The-adventures-of-Dora-Bell-detective` | The adventures of Dora Bell, detective / Corbett | 2745 | 1.000 | 9 | 4 | 4 | 0 | 0 | TRUSTED_FULL | 支持 | R13 |
| PG71037 | `PG71037-The-gamblers` | The gamblers / Le Queux | 9519 | 1.000 | 26 | 54 | 46 | 6 | 2 | TRUSTED_FULL | 支持 | R7 R9 R1 |
| PG71521 | `PG71521-The-horror-expert` | The horror expert / Long | 6484 | 1.000 | 16 | 2 | 2 | 0 | 0 | FULL_MINQ | 支持（冲突） | C3 R13 |
| PG72462 | `PG72462-The-rasp` | The rasp / MacDonald | 9103 | 1.000 | 81 | 388 | 354 | 28 | 6 | TRUSTED_FULL | 支持 | R4 R9 |
| PG72948 | `PG72948-Annihilation` | Annihilation / Ostrander | 9995 | 1.000 | 29 | 185 | 171 | 10 | 4 | TRUSTED_FULL | 支持（冲突） | R13 C3 R4 |
| PG807 | `PG807-Hunted-Down-The-Detective-Stories-of-Charles-Dickens` | Hunted Down: The Detective Stories of Charles Dickens / Dickens | 1034 | 1.000 | 5 | 1 | 1 | 0 | 0 | FULL_MINQ | 支持 | R9 R13 |

## 证据族去重

- **Fergus Hume 族**（PG55313、PG55617、PG55783、PG56087、PG56385、PG56841，6 本）= 1 个独立族；同一套"证词—误判—自白—反转"装置跨本复用，不叠加置信。
- **Fred M. White 族**（PG56960、PG57066，2 本）= 1 个独立族。
- **Natalie Sumner Lincoln 族**（PG68810、PG69004，2 本）= 1 个独立族。
- 其余 20 本各为 1 个独立族 → **23 个独立证据族**。

## 本轮补写/补读的部分

- `notes/reading/ledger-PG55617-pg8253-8262-gap.md`：历史台账止于 L8252（`THE END`），缺 L8253-L8262；本轮 Read 补读 L8230-L8262，确认缺口内只有 Gutenberg 尾注，无叙事内容。门禁 `--book … --start 8230 --end 8262` 判定 **PASS**（2 条引文全部命中）。
- 本轮 Read 直读原文复核的 **24 处**引文清单见轮次根目录 `../../notes/source-synthesis.md` §5（相对本文件的路径；该文件不在 skill 包内）；本表与 `06-adjudication-log.md` 已给出可独立核对的 PG+行号引文。

## 权利与许可（必须随 Skill 携带，不得丢失）

本 Skill 的全部来源为 Project Gutenberg 公共镜像／官方版本的**英文公版小说**；权利状态**逐书不同，且都不是法律结论**。

| 权利标签 | 原文措辞（来自各书 `书籍信息.json`） | 核验标记 | 本数 |
|---|---|---|---:|
| A | Project Gutenberg official edition; rights need per-work and jurisdiction verification before reuse | 未记录 | 14 |
| B | Gutenberg official catalog+public mirror; per-work and jurisdiction rights must be checked independently | HEADERS_AND_GUTENBERG_WRAPPERS_SCREENED_US_PD_NOT_LEGAL_CERTIFICATION | 8 |
| C | Project Gutenberg mirror source. Rights outside USA and individual permission exceptions require independent verification; text header screened. | MIRROR_HEADER_SCREENED_NOT_LEGAL_DETERMINATION | 5 |
| E | MIRROR_HEADER_SCREENED_US_PD_RULES_NOT_LEGAL_OPINION | 未记录 | 2 |
| D | Gutenberg official page: Public domain in the USA; no assertion for other jurisdictions. | 未记录 | 1 |

| PG | 权利标签 | PG | 权利标签 | PG | 权利标签 |
|---|---|---|---|---|---|
| PG108 | D | PG1685 | C | PG2019 | C |
| PG2358 | C | PG3803 | C | PG46462 | B |
| PG55313 | A | PG55617 | B | PG55783 | B |
| PG56087 | A | PG56385 | A | PG56841 | A |
| PG56960 | B | PG57066 | B | PG58820 | B |
| PG59126 | E | PG59369 | B | PG65790 | A |
| PG66756 | B | PG67079 | A | PG68153 | A |
| PG68810 | A | PG68951 | A | PG69004 | A |
| PG70924 | A | PG71037 | A | PG71521 | A |
| PG72462 | E | PG72948 | A | PG807 | C |

**使用者的义务（不可省略）**

1. 标签 A–E **均非法律意见**：来源侧标记明确写作 `NOT_LEGAL_DETERMINATION` / `NOT_LEGAL_CERTIFICATION` / `NOT_LEGAL_OPINION`。
2. 若要把本 Skill 的引文、书名或摘录用于**出版、商用、再分发**，须按目标司法辖区逐书独立核验权利状态。
3. 本 Skill 只输出**写作工艺判断与 PG+行号锚点**，不复制原文正文；引用示例中的引文均为短句（≤40 words 的英文原句），使用者仍需按上条自行核验。
4. 来源侧另有 `acquisition_screen` / `source_license_check` 等核验标记，完整逐书字段见各 `<PG>-*/书籍信息.json`（不在 skill 包内）。
