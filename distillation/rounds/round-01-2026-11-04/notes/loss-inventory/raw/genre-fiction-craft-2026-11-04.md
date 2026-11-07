**genre 全表覆盖率**：已对齐 16 / 610 = **2.6%**；flag 计数：BLOCK_LOST=11；MISSING=594；RENUMBERED?=4；SHRUNK=4；—=1

# K1 机械盘点 raw 表 · genre-fiction-craft（按 14 类题材分组）

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 按 D4-A：14 类全部机械盘点；**热门三类 04 武侠仙侠玄幻 / 02 言情 / 05 科幻** 与 v0 全文对照由 W2 起定向精读执行，本表只出机械盘点信号。
- 阈值：默认缩减 >30% 或 >1.5 KB；**01 推理 / 07 求生灾变 / 10 职业竞技收紧到 20%**（第 5.1 节、附录 A.1）。
- v1 题材目录为中文名、v2/v3 为英文名，均按 `NN-` 数字前缀定位对应题材目录。
- 字段与 flag 含义见各分节表头；`blocks` 简写：规/怎/例/反/检/适/败/∅。
- 编号改号对照：`IDP→IR`、`COM→CO`、`RM/RD→RL` 等按 2.3 节，用「新旧前缀 + 标题」对齐。

---

## 题材 01 推理（阈值 20%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 01 推理

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；本题材按第 5.1 节收紧到 20%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`crime-mystery-craft-b03`、`mystery-clue-fairplay`、`mystery-detection-craft-b04`、`mystery-detective-plot-forge`、`mystery-evidence-chain-designer`

**覆盖率**：已对齐 0 / v0 文件 52 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=52

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `crime-mystery-craft-b03/SKILL.md [无编号]` | `1 0 0 0` | `规怎例反适败` | `14738 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/agents/openai.yaml [无编号]` | `1 0 0 0` | `规适` | `2851 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/examples/worked-example.md [无编号]` | `1 0 0 0` | `规检` | `4484 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/01-information-and-clues.md [R1,R2,R3,R4]` | `1 0 0 0` | `怎例反适` | `11229 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/02-scene-and-space.md [R11A,R11B,R12,R5,R6]` | `1 0 0 0` | `怎反适` | `8471 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/03-resolution-and-conflicts.md [C1,C2,C3,R7,R8,R9]` | `1 0 0 0` | `规怎例反适` | `13951 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/04-investigator-and-entry.md [R10,R13]` | `1 0 0 0` | `规怎例适` | `6642 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/05-source-index.md [无编号]` | `1 0 0 0` | `∅` | `9044 / — / — / —` | `MISSING` |
| `crime-mystery-craft-b03/references/06-adjudication-log.md [无编号]` | `1 0 0 0` | `∅` | `6148 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/SKILL.md [无编号]` | `1 0 0 0` | `规例适败` | `5863 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `153 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/examples/worked-example.md [无编号]` | `1 0 0 0` | `检` | `2682 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/anti-patterns.md [R12]` | `1 0 0 0` | `规例反适` | `2060 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/clue-placement.md [R1,R1–R2,R2]` | `1 0 0 0` | `检` | `2513 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/corpus-synthesis.md [无编号]` | `1 0 0 0` | `规怎例反检` | `3994 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/evidence-design.md [R6,R6–R8,R7,R8]` | `1 0 0 0` | `适` | `2866 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/misdirection-frames.md [R3,R3–R5,R4,R5]` | `1 0 0 0` | `例适` | `2676 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/source-index.md [无编号]` | `1 0 0 0` | `例` | `6144 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/structure-and-narration.md [R10,R11,R9,R9–R11]` | `1 0 0 0` | `例` | `2184 / — / — / —` | `MISSING` |
| `mystery-clue-fairplay/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `例反适` | `2055 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `14573 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/agents/openai.yaml [无编号]` | `1 0 0 0` | `规怎例` | `1759 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/examples/worked-example.md [无编号]` | `1 0 0 0` | `怎检` | `5106 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/references/clue-identity-misdirection.md [无编号]` | `1 0 0 0` | `规怎例反检适` | `9303 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/references/evidence-timing-closedlist.md [无编号]` | `1 0 0 0` | `规怎例反检适` | `10567 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/references/locked-room-reveal-conflicts.md [无编号]` | `1 0 0 0` | `规例反检适` | `8965 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/references/rule-adjudication.md [R1,R10… 共9]` | `1 0 0 0` | `规怎例反检适` | `11865 / — / — / —` | `MISSING` |
| `mystery-detection-craft-b04/references/source-index-and-evidence-tiers.md [无编号]` | `1 0 0 0` | `∅` | `6065 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/SKILL.md [P4]` | `1 0 0 0` | `规例败` | `8772 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `184 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/counterexamples.md [无编号]` | `1 0 0 0` | `规例适` | `3639 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/examples.md [无编号]` | `1 0 0 0` | `规败` | `3823 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/failure-modes.md [无编号]` | `1 0 0 0` | `败` | `3203 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/atmosphere-and-cast.md [P1,P2… 共23]` | `1 0 0 0` | `规怎` | `12393 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/counterexamples.md [无编号]` | `1 0 0 0` | `∅` | `1482 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/detection-and-process.md [I1,I2… 共18]` | `1 0 0 0` | `怎反` | `9731 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/examples.md [无编号]` | `1 0 0 0` | `怎适败` | `1537 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/failure-modes.md [无编号]` | `1 0 0 0` | `例` | `3931 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `728 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/identity-and-mastermind.md [F1,F2… 共18]` | `1 0 0 0` | `怎例适` | `10021 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/impossible-crime.md [A1,A2… 共18]` | `1 0 0 0` | `规怎适` | `11486 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/motive-and-justice.md [L1,L2… 共20]` | `1 0 0 0` | `规怎例适` | `11094 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/source-index.md [无编号]` | `1 0 0 0` | `例` | `8424 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/references/timeline-and-evidence.md [C1,C2… 共16]` | `1 0 0 0` | `怎例` | `9073 / — / — / —` | `MISSING` |
| `mystery-detective-plot-forge/sources-index.md [无编号]` | `1 0 0 0` | `∅` | `6891 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `9365 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/agents/openai.yaml [无编号]` | `1 0 0 0` | `规反检适` | `1553 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/references/checklists.md [L1,L2,L3,L4,L5,L6]` | `1 0 0 0` | `检` | `5344 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/references/counterexamples-conflicts.md [无编号]` | `1 0 0 0` | `规怎例` | `6591 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/references/examples.md [无编号]` | `1 0 0 0` | `反检` | `7058 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/references/rules-core.md [A1,A2… 共22]` | `1 0 0 0` | `怎例适败` | `22195 / — / — / —` | `MISSING` |
| `mystery-evidence-chain-designer/references/source-ledger.md [无编号]` | `1 0 0 0` | `规` | `9426 / — / — / —` | `MISSING` |

---

## 题材 02 言情（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 02 言情

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`courtship-conflict-craft`、`romance-craft-b03-b07`、`romance-craft-b06`、`romance-emotional-arc`、`romance-obstacle-and-cost`、`romance-obstacle-delay-craft`、`romance-social-cost-craft`

**覆盖率**：已对齐 1 / v0 文件 59 = **1.7%**（v1/v2/v3 各版本有对应：1 / 1 / 1）

**flag 计数**：BLOCK_LOST=1；MISSING=58

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `courtship-conflict-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `13427 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `469 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `4915 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/references/01-courtship-engines.md [R1,R2,R3,R4,R5,R6]` | `1 0 0 0` | `反检适` | `10688 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/references/02-settlement-and-closure.md [R7,R8,R9]` | `1 0 0 0` | `例反` | `7371 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/references/03-derivative-and-formats.md [R10]` | `1 0 0 0` | `反` | `2655 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `规例检` | `6190 / — / — / —` | `MISSING` |
| `courtship-conflict-craft/references/05-cross-source-decisions.md [无编号]` | `1 0 0 0` | `例反检适` | `7541 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/SKILL.md [无编号]` | `1 0 0 0` | `规怎例反适败` | `10678 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `3991 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/references/conflicts-and-anti-patterns.md [无编号]` | `1 0 0 0` | `规反` | `5005 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/references/evidence-index.md [无编号]` | `1 0 0 0` | `∅` | `5585 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md [无编号]` | `1 0 0 0` | `∅` | `5160 / — / — / —` | `MISSING` |
| `romance-craft-b03-b07/references/source-roles-b03b07.md [无编号]` | `1 0 0 0` | `∅` | `5190 / — / — / —` | `MISSING` |
| `romance-craft-b06/FREEZE.md [无编号]` | `1 0 0 0` | `∅` | `796 / — / — / —` | `MISSING` |
| `romance-craft-b06/SKILL.md [P4,R01… 共17]` | `1 0 0 0` | `规怎例反检适败` | `30068 / — / — / —` | `MISSING` |
| `romance-craft-b06/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `155 / — / — / —` | `MISSING` |
| `romance-craft-b06/counterexamples.md [无编号]` | `1 0 0 0` | `反败` | `6649 / — / — / —` | `MISSING` |
| `romance-craft-b06/examples.md [无编号]` | `1 1 1 1` | `规适` | `4979 / 19045 / 22917 / 22858` | `BLOCK_LOST` |
| `romance-craft-b06/failure-modes.md [FAILURE-MODES]` | `1 0 0 0` | `规` | `4746 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/p4-field-guide.md [B-03-B06,R01… 共10]` | `1 0 0 0` | `规怎例反检适` | `6748 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/r1-meet-and-obstacle.md [R1]` | `1 0 0 0` | `例检` | `7813 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/r2-beats-and-delay.md [R2]` | `1 0 0 0` | `规怎例败` | `5800 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/r3-rivals-and-market.md [R3]` | `1 0 0 0` | `规例检适` | `8243 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/r4-confession-and-endings.md [R4]` | `1 0 0 0` | `例反检败` | `7733 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/r5-pov-and-interiority.md [R5]` | `1 0 0 0` | `怎检适` | `6290 / — / — / —` | `MISSING` |
| `romance-craft-b06/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `3253 / — / — / —` | `MISSING` |
| `romance-craft-b06/sources-index.md [R01,R02… 共17]` | `1 0 0 0` | `∅` | `8754 / — / — / —` | `MISSING` |
| `romance-emotional-arc/SKILL.md [无编号]` | `1 0 0 0` | `规例适败` | `4873 / — / — / —` | `MISSING` |
| `romance-emotional-arc/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `165 / — / — / —` | `MISSING` |
| `romance-emotional-arc/examples/worked-example.md [无编号]` | `1 0 0 0` | `检` | `3037 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/01-refusal-and-vow.md [R1,R3]` | `1 0 0 0` | `规例反检` | `3545 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/02-obstacle-carriers.md [R2,R4]` | `1 0 0 0` | `规例` | `3358 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/03-reversal-and-vacancy.md [R5,R9]` | `1 0 0 0` | `规检` | `2948 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/04-confession-scenes.md [P4,R6,R8]` | `1 0 0 0` | `规例检` | `2904 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/05-ending-and-cost.md [C2,C3,C5,C6,R10,R7]` | `1 0 0 0` | `规例` | `4534 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/source-index.md [无编号]` | `1 0 0 0` | `规例` | `4250 / — / — / —` | `MISSING` |
| `romance-emotional-arc/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `规怎例反适` | `1768 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/SKILL.md [无编号]` | `1 0 0 0` | `规例检适败` | `9849 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `1550 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/references/01-obstacle-ownership.md [无编号]` | `1 0 0 0` | `反检适` | `6801 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/references/02-ending-and-cost.md [无编号]` | `1 0 0 0` | `规反检适` | `8086 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/references/03-social-pressure-and-pov.md [无编号]` | `1 0 0 0` | `例反检` | `5285 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/references/04-source-index.md [无编号]` | `1 0 0 0` | `例` | `7725 / — / — / —` | `MISSING` |
| `romance-obstacle-and-cost/references/05-adjudication-and-conflicts.md [无编号]` | `1 0 0 0` | `规适` | `6638 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `7704 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `2465 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/references/coercion-and-consent.md [无编号]` | `1 0 0 0` | `检败` | `2729 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/references/conflicts-and-exceptions.md [无编号]` | `1 0 0 0` | `规例适` | `5178 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/references/rules-obstacle-delay.md [R1,R2,R3,R4,R5,R6]` | `1 0 0 0` | `反检` | `10566 / — / — / —` | `MISSING` |
| `romance-obstacle-delay-craft/references/source-index.md [无编号]` | `1 0 0 0` | `规例适` | `5080 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/SKILL.md [无编号]` | `1 0 0 0` | `规例败` | `10746 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `814 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/examples/worked-example.md [无编号]` | `1 0 0 0` | `规例适` | `3683 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/references/01-source-roles.md [无编号]` | `1 0 0 0` | `例反适` | `6273 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/references/02-social-cost-rules.md [RP1,RP2,RP3,RP6,RP9]` | `1 0 0 0` | `例` | `6120 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/references/03-stigma-and-boundaries.md [B1,B2,B3,RP5]` | `1 0 0 0` | `规例反检` | `4127 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/references/04-confession-documents-ending.md [RP4,RP7,RP8]` | `1 0 0 0` | `怎例反` | `4513 / — / — / —` | `MISSING` |
| `romance-social-cost-craft/references/05-source-index.md [无编号]` | `1 0 0 0` | `∅` | `4489 / — / — / —` | `MISSING` |

---

## 题材 03 恐怖（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 03 恐怖

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`gothic-weird-horror-craft`、`horror-dread-and-revelation`、`horror-gothic-suspense-b05`、`horror-supernatural-craft`、`horror-thriller-craft-b04`

**覆盖率**：已对齐 0 / v0 文件 55 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=55

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `gothic-weird-horror-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎反检适败` | `10207 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `189 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/01-attribution-and-fear-objects.md [A1,A2,A3,A4]` | `1 0 0 0` | `∅` | `4702 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/02-contracts-and-switches.md [无编号]` | `1 0 0 0` | `检` | `4690 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/03-technique-catalogue.md [T1,T10… 共10]` | `1 0 0 0` | `规检适` | `6420 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/04-conflicts-and-counterexamples.md [无编号]` | `1 0 0 0` | `规例反适` | `5055 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/05-diagnostic-checklist.md [无编号]` | `1 0 0 0` | `例检` | `3690 / — / — / —` | `MISSING` |
| `gothic-weird-horror-craft/references/06-source-index.md [无编号]` | `1 0 0 0` | `规怎例` | `10315 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `17048 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `188 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/examples/worked-example.md [无编号]` | `1 0 0 0` | `规例检败` | `5128 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/01-frames-and-witnesses.md [R1,R2,R21,R3,R4]` | `1 0 0 0` | `怎例反检适` | `9453 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/02-dread-staging.md [R22,R30,R5,R6,R7,R8]` | `1 0 0 0` | `规怎例反适败` | `11940 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/03-revelation-positions.md [R10,R11,R12,R23,R28,R9]` | `1 0 0 0` | `怎例反适` | `13230 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/04-rules-and-rituals.md [R13,R14… 共7]` | `1 0 0 0` | `规怎例检适` | `11880 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/05-endings-and-ethics.md [R17,R18,R19,R20,R26,R27]` | `1 0 0 0` | `例反检` | `12827 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/06-evidence-conflict-and-ambiguity.md [无编号]` | `1 0 0 0` | `反适败` | `5914 / — / — / —` | `MISSING` |
| `horror-dread-and-revelation/references/source-index.md [A-04-B03]` | `1 0 0 0` | `规例适` | `9124 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/SKILL.md [P4]` | `1 0 0 0` | `规怎例反检适败` | `5435 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `157 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/examples.md [P4]` | `1 0 0 0` | `例反适` | `5399 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/p4-field-guide.md [A-04-B05,RG-01… 共9]` | `1 0 0 0` | `规怎例反适败` | `5708 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/rules.md [RG-01,RG-02… 共20]` | `1 0 0 0` | `规怎检` | `12974 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/scope-and-conflicts.md [C1,C2,C3,C4,C5,P4]` | `1 0 0 0` | `例反适` | `5461 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/source-index.md [S1,S2]` | `1 0 0 0` | `∅` | `4689 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/techniques.md [无编号]` | `1 0 0 0` | `适` | `3474 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `4055 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/templates/dread-scene-planner.md [P4]` | `1 0 0 0` | `∅` | `1553 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/templates/haunting-designer.md [P4]` | `1 0 0 0` | `∅` | `1613 / — / — / —` | `MISSING` |
| `horror-gothic-suspense-b05/templates/manuscript-diagnosis.md [P4]` | `1 0 0 0` | `∅` | `1386 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/SKILL.md [P4]` | `1 0 0 0` | `规怎例检败` | `9111 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `160 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/examples/worked-example.md [无编号]` | `1 0 0 0` | `规` | `5745 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/01-mechanics-and-curses.md [无编号]` | `1 0 0 0` | `规怎适` | `11708 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/02-dread-and-atmosphere.md [无编号]` | `1 0 0 0` | `怎适` | `9917 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/03-evidence-and-revelation.md [P4]` | `1 0 0 0` | `例` | `8247 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/04-structure-and-narrators.md [无编号]` | `1 0 0 0` | `例` | `6493 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/05-negative-space-and-tone.md [P4]` | `1 0 0 0` | `例` | `7051 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/06-source-index.md [P4]` | `1 0 0 0` | `规例` | `7011 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/p4-field-guide.md [A-04-B02,M01… 共9]` | `1 0 0 0` | `规怎例反适` | `6622 / — / — / —` | `MISSING` |
| `horror-supernatural-craft/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `4672 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/SKILL.md [P4]` | `1 0 0 0` | `规怎例反检败` | `23425 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `190 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/counterexamples.md [无编号]` | `1 0 0 0` | `规怎例检适` | `8741 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/examples.md [无编号]` | `1 0 0 0` | `怎适败` | `10874 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/failure-modes.md [无编号]` | `1 0 0 0` | `规败` | `8087 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/freeze-manifest.json [无编号]` | `1 0 0 0` | `∅` | `2232 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/collections-and-boundaries.md [无编号]` | `1 0 0 0` | `规怎例检败` | `10669 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/credibility-and-pov.md [无编号]` | `1 0 0 0` | `规怎检` | `8291 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/escalation-and-closure.md [C1,C2,C5]` | `1 0 0 0` | `规检适` | `5597 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/fear-source-and-type.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `8000 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `955 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/rework-decision.md [无编号]` | `1 0 0 0` | `例反败` | `3750 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/references/rules-contracts-and-space.md [无编号]` | `1 0 0 0` | `规怎例检适` | `10064 / — / — / —` | `MISSING` |
| `horror-thriller-craft-b04/sources-index.md [无编号]` | `1 0 0 0` | `∅` | `5890 / — / — / —` | `MISSING` |

---

## 题材 04 武侠仙侠玄幻（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 04 武侠仙侠玄幻

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`speculative-wuxia-fantasy-craft`、`wuxia-fantasy-power-arc`、`wuxia-xianxia-plot-forge`、`fantasy-adventure-structure-lab`、`supernatural-power-craft`

**覆盖率**：已对齐 0 / v0 文件 61 = **0.0%**（v1/v2/v3 各版本有对应：6 / 0 / 0）

**flag 计数**：MISSING=61

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `speculative-wuxia-fantasy-craft/SKILL.md [P4]` | `1 0 0 0` | `规例反检适败` | `15478 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `196 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/counterexamples.md [C-01,C-02… 共16]` | `1 0 0 0` | `规怎例反适败` | `9482 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/examples.md [无编号]` | `1 0 0 0` | `规例检` | `9397 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/failure-modes.md [FM-01,FM-02… 共12]` | `1 0 0 0` | `规例适败` | `8934 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/01-portals-and-otherworld-laws.md [F01,F01-R1… 共15]` | `1 1 0 0` | `规怎例适` | `9559 / 10777 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md [F03,F03-R1… 共16]` | `1 1 0 0` | `规怎例适败` | `10962 / 11481 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/03-price-identity-and-names.md [F07,F07-R1… 共17]` | `1 1 0 0` | `规怎例适` | `10149 / 11481 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/04-institutions-rumor-and-antagonists.md [F12,F12-R1… 共15]` | `1 1 0 0` | `规怎败` | `9302 / 11481 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/05-prophecy-contracts-and-endings.md [F16,F16-R1… 共13]` | `1 1 0 0` | `规怎例适` | `8203 / 11481 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/06-pov-horror-and-boundaries.md [B1,B2… 共15]` | `1 1 0 0` | `规怎例适` | `8504 / 10777 / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `393 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/references/rework-decision.md [无编号]` | `1 0 0 0` | `规例败` | `3149 / — / — / —` | `MISSING` |
| `speculative-wuxia-fantasy-craft/sources-index.md [无编号]` | `1 0 0 0` | `规例` | `9867 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/SKILL.md [无编号]` | `1 0 0 0` | `∅` | `4452 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `286 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/examples/conflict-missing.md [无编号]` | `1 0 0 0` | `∅` | `637 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/examples/normal-design.md [无编号]` | `1 0 0 0` | `∅` | `497 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `780 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/01-power-source-and-price.md [无编号]` | `1 0 0 0` | `规例反适` | `4693 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/02-escalation-ladder.md [无编号]` | `1 0 0 0` | `规例反败` | `3481 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/03-legitimacy-and-institution.md [无编号]` | `1 0 0 0` | `规例反适` | `3359 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/04-information-and-reveal.md [无编号]` | `1 0 0 0` | `规例反` | `1333 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/05-counterexamples-and-boundaries.md [无编号]` | `1 0 0 0` | `规例反适` | `4188 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/references/source-index.md [无编号]` | `1 0 0 0` | `例` | `7646 / — / — / —` | `MISSING` |
| `wuxia-fantasy-power-arc/templates/power-arc-state.md [无编号]` | `1 0 0 0` | `∅` | `1172 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/SKILL.md [P4]` | `1 0 0 0` | `规例反败` | `13384 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `190 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/counterexamples.md [无编号]` | `1 0 0 0` | `规例反适` | `3777 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/examples.md [无编号]` | `1 0 0 0` | `∅` | `4102 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/failure-modes.md [无编号]` | `1 0 0 0` | `规怎例反败` | `4680 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/deception-and-identity.md [C1,C2… 共17]` | `1 0 0 0` | `规怎检败` | `6778 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/emotion-and-craft.md [N1,N2… 共24]` | `1 0 0 0` | `怎反检` | `6524 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/fate-and-taboo.md [H1,H2… 共9]` | `1 0 0 0` | `规怎例检适` | `6367 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/heroes-and-bosses.md [B1,B2… 共15]` | `1 0 0 0` | `规怎适` | `6025 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `468 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/rework-decision.md [无编号]` | `1 0 0 0` | `∅` | `3539 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/tokens-and-items.md [A1,A2… 共8]` | `1 0 0 0` | `规怎检` | `4645 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/references/world-and-society.md [G1,G2… 共14]` | `1 0 0 0` | `规怎例检适` | `6378 / — / — / —` | `MISSING` |
| `wuxia-xianxia-plot-forge/sources-index.md [无编号]` | `1 0 0 0` | `∅` | `4502 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/SKILL.md [P4]` | `1 0 0 0` | `规怎例反适败` | `12680 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `166 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/01-power-system-and-price.md [R001,R002… 共12]` | `1 0 0 0` | `规怎例反适败` | `17965 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/02-institutions-power-and-crowd.md [R020,R021… 共14]` | `1 0 0 0` | `规怎反适败` | `15423 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/03-identity-disguise-and-proof.md [R040,R041… 共16]` | `1 0 0 0` | `规怎反检适` | `17768 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/04-oaths-contracts-and-mirror-punishment.md [R060,R061… 共15]` | `1 0 0 0` | `规怎反适败` | `16403 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/05-quest-chain-aid-and-pursuit.md [R080,R081… 共18]` | `1 0 0 0` | `规怎反适` | `16322 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/06-superstition-disenchantment-and-horror.md [R100,R101… 共19]` | `1 0 0 0` | `规怎例反适` | `17373 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/07-rumor-ending-and-craft.md [R130,R131… 共21]` | `1 0 0 0` | `规怎例适` | `16795 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/08-conflicts-and-redlines.md [U-01,U-02… 共26]` | `1 0 0 0` | `规反检适` | `16465 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/p4-field-guide.md [A-05-B02,R001… 共9]` | `1 0 0 0` | `规怎例反检适` | `6010 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `9628 / — / — / —` | `MISSING` |
| `fantasy-adventure-structure-lab/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `4787 / — / — / —` | `MISSING` |
| `supernatural-power-craft/SKILL.md [P4]` | `1 0 0 0` | `规例检适败` | `14731 / — / — / —` | `MISSING` |
| `supernatural-power-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `829 / — / — / —` | `MISSING` |
| `supernatural-power-craft/references/design-and-diagnosis.md [无编号]` | `1 0 0 0` | `规例检` | `5702 / — / — / —` | `MISSING` |
| `supernatural-power-craft/references/rules.md [RC-01,RC-02… 共10]` | `1 0 0 0` | `规例反检适` | `24042 / — / — / —` | `MISSING` |
| `supernatural-power-craft/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `例适` | `5986 / — / — / —` | `MISSING` |
| `supernatural-power-craft/references/source-index.md [无编号]` | `1 0 0 0` | `规例适` | `8680 / — / — / —` | `MISSING` |
| `supernatural-power-craft/templates/diagnosis-report.md [无编号]` | `1 0 0 0` | `规检` | `2229 / — / — / —` | `MISSING` |
| `supernatural-power-craft/templates/power-system-canvas.md [无编号]` | `1 0 0 0` | `例适` | `2583 / — / — / —` | `MISSING` |

---

## 题材 05 科幻（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 05 科幻

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`sci-fi-future-plot-forge`、`sci-fi-novum-world-forge`、`science-fiction-conceptual-reveal`、`science-fiction-craft-b04`、`scifi-future-craft-b03`

**覆盖率**：已对齐 3 / v0 文件 62 = **4.8%**（v1/v2/v3 各版本有对应：2 / 3 / 3）

**flag 计数**：BLOCK_LOST=1；MISSING=59；RENUMBERED?=1；—=1

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `sci-fi-future-plot-forge/SKILL.md [P4,SCI-FI]` | `1 0 0 0` | `怎反败` | `7960 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `168 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/anti-examples.md [A1,A2,A3,A4,A5]` | `1 0 0 0` | `例检` | `3092 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/examples.md [E1,E10… 共10]` | `1 1 1 1` | `规适` | `5764 / 13712 / 20190 / 20214` | `—` |
| `sci-fi-future-plot-forge/failure-modes.md [无编号]` | `1 0 0 0` | `规例反检适败` | `4108 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/created-beings.md [CB-01,CB-02,CB-03,CB-04,CB-05]` | `1 0 0 0` | `规适` | `8206 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/expedition-combat.md [EC-01,EC-02,EC-03,EC-04,EC-05]` | `1 0 0 0` | `规适` | `7874 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/history-time.md [HT-01,HT-02,HT-03,HT-04,HT-05]` | `1 0 0 0` | `规适` | `7718 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/identity-infiltration.md [II-01,II-02,II-03,II-04,II-05]` | `1 0 0 0` | `规例适` | `7040 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/mind-war.md [MW-01,MW-02,MW-03,MW-04,MW-05,MW-06]` | `1 0 0 0` | `规适` | `7930 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/p4-field-guide.md [A-06-B01,SF-01… 共9]` | `1 0 1 1` | `规怎例反检适` | `5849 / — / 13995 / 14049` | `RENUMBERED?` |
| `sci-fi-future-plot-forge/references/society-love-craft.md [SL-01,SL-02,SL-03,SL-04,SL-05,SL-06]` | `1 0 0 0` | `规例适` | `9464 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `4376 / — / — / —` | `MISSING` |
| `sci-fi-future-plot-forge/sources.md [无编号]` | `1 0 0 0` | `检` | `6078 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/SKILL.md [SCI-FI]` | `1 0 0 0` | `规怎例适败` | `6929 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `272 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/alien-contact.md [C4-1,C4-2,C4-3,C4-4,C4-5,C4-6]` | `1 0 0 0` | `规例检适` | `4932 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/created-beings.md [C3-1,C3-2,C3-3,C3-4,C3-5,C3-6]` | `1 0 0 0` | `规例反检适` | `4974 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/failure-exit.md [无编号]` | `1 0 0 0` | `规例适` | `3808 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/hard-sf-traceability.md [C5-1,C5-2,C5-3,C5-4,C5-5]` | `1 0 0 0` | `规例反检适败` | `4308 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/heterotopia-inversion.md [C2-1,C2-2,C2-3,C2-4]` | `1 0 0 0` | `规例反检适` | `3869 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/institution-detail.md [C7-1,C7-2,C7-3,C7-4,C7-5,C7-6]` | `1 0 0 0` | `规例反检适` | `4730 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/novum-consequence-chain.md [C1-1,C1-2,C1-3,C1-4]` | `1 0 0 0` | `规例反检适` | `4020 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/reversal-and-framing.md [C6-1,C6-2,C6-3,C6-4,C6-5,C6-6]` | `1 0 0 0` | `规例反检适` | `4444 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/rule-adjudication.md [无编号]` | `1 0 0 0` | `规` | `7076 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/sources.md [无编号]` | `1 0 0 0` | `∅` | `10908 / — / — / —` | `MISSING` |
| `sci-fi-novum-world-forge/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `规检` | `4580 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/SKILL.md [P4]` | `1 0 0 0` | `规怎反检适败` | `9592 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `159 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/examples/worked-example.md [无编号]` | `1 0 0 0` | `反败` | `5084 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/01-anchor-object.md [R1]` | `1 0 0 0` | `规例反检适败` | `4189 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/02-reveal-timing.md [R2]` | `1 0 0 0` | `规例反检适败` | `4728 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/03-repetition-and-restaging.md [R3]` | `1 0 0 0` | `规例反检适败` | `4156 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/04-cognitive-framing.md [R4]` | `1 0 0 0` | `规例反检适败` | `5554 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/05-negative-space-and-close.md [R6]` | `1 0 0 0` | `规例反检适败` | `4366 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/06-failure-modes.md [R7]` | `1 0 0 0` | `规例反检适败` | `4095 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/p4-field-guide.md [A-06-B05,R1… 共8]` | `1 0 0 0` | `规怎例反检适败` | `5928 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/source-index.md [无编号]` | `1 0 0 0` | `规检` | `5578 / — / — / —` | `MISSING` |
| `science-fiction-conceptual-reveal/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `3806 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/SKILL.md [P4]` | `1 0 0 0` | `规怎例检败` | `10750 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `196 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/counterexamples.md [无编号]` | `1 0 0 0` | `规` | `7370 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/examples.md [无编号]` | `1 1 1 1` | `规例检败` | `7794 / 13712 / 20190 / 20214` | `BLOCK_LOST` |
| `science-fiction-craft-b04/failure-modes.md [M1,M2… 共7]` | `1 0 0 0` | `规例` | `7816 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/contact-and-otherness.md [R02,R03,R04,R07,R27]` | `1 0 0 0` | `怎` | `9007 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `468 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/information-and-pov.md [R15,R16,R24,R25,R28]` | `1 0 0 0` | `怎例反` | `8915 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/novum-and-rules.md [R01,R14,R17,R19,R20]` | `1 0 0 0` | `规怎例适` | `9150 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/rework-decision.md [无编号]` | `1 0 0 0` | `规例检适败` | `3349 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/structure-and-endings.md [R08,R09… 共8]` | `1 0 0 0` | `规怎` | `12918 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/references/world-and-institutions.md [R05,R06… 共7]` | `1 0 0 0` | `怎败` | `12983 / — / — / —` | `MISSING` |
| `science-fiction-craft-b04/sources-index.md [无编号]` | `1 0 0 0` | `规` | `9768 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/SKILL.md [R1,R2… 共7]` | `1 0 0 0` | `规怎例适` | `13877 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `541 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/examples/worked-example.md [无编号]` | `1 0 0 0` | `规` | `4203 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/01-exposition-and-evidence.md [R1]` | `1 0 0 0` | `败` | `3072 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/02-alienness-and-scale.md [R2]` | `1 0 0 0` | `例` | `3473 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/03-single-variable-world.md [R3]` | `1 0 0 0` | `规` | `3074 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/04-rules-costs-and-paperwork.md [R5]` | `1 0 0 0` | `∅` | `3395 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/05-time-and-mechanism-ledger.md [R4]` | `1 0 0 0` | `∅` | `3230 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/06-endings-conflicts-counterexamples.md [R7]` | `1 0 0 0` | `规` | `3393 / — / — / —` | `MISSING` |
| `scifi-future-craft-b03/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `4911 / — / — / —` | `MISSING` |

---

## 题材 06 历史架空（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 06 历史架空

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`historical-alt-history-craft`、`historical-contract-and-legitimacy-craft`、`historical-fiction-craft-b03`、`historical-fiction-plot-forge`、`historical-fiction-power-machine`、`historical-immersion-and-stakes`

**覆盖率**：已对齐 3 / v0 文件 74 = **4.1%**（v1/v2/v3 各版本有对应：1 / 3 / 3）

**flag 计数**：BLOCK_LOST=3；MISSING=71

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `historical-alt-history-craft/SKILL.md [P4]` | `1 0 0 0` | `规怎例适败` | `28635 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `190 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/counterexamples.md [R1–R5]` | `1 0 0 0` | `规怎败` | `8956 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/examples.md [无编号]` | `1 0 1 1` | `规怎例检适败` | `10165 / — / 13654 / 13654` | `BLOCK_LOST` |
| `historical-alt-history-craft/failure-modes.md [M1,M2… 共8]` | `1 0 0 0` | `例败` | `8886 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/01-source-contract-and-anchors.md [F1,F2,F20,F9]` | `1 0 0 0` | `怎例反检适` | `14609 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/02-gap-agents-and-institutions.md [F10,F15… 共8]` | `1 0 0 0` | `怎检适败` | `31712 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/03-prophecy-relics-and-ritual.md [F13,F18,F23,F6,F7]` | `1 0 0 0` | `怎检` | `17878 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/04-scene-voice-and-space.md [F11,F12,F14,F21]` | `1 0 0 0` | `规怎检` | `15177 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/05-bias-violence-and-limits.md [F17,F19]` | `1 0 0 0` | `规怎反败` | `11747 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `795 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/references/rework-decision.md [无编号]` | `1 0 0 0` | `反` | `3737 / — / — / —` | `MISSING` |
| `historical-alt-history-craft/sources-index.md [无编号]` | `1 0 0 0` | `∅` | `8995 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/SKILL.md [无编号]` | `1 0 0 0` | `怎败` | `16340 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `212 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/references/01-source-contract-and-paratext.md [A1,A2… 共14]` | `1 0 0 0` | `适败` | `10280 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/references/02-legitimacy-and-documents.md [D1,D2… 共13]` | `1 0 0 0` | `规检败` | `8376 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/references/03-real-figures-and-symmetry.md [C1,C2… 共11]` | `1 0 0 0` | `适败` | `9563 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/references/04-space-supernatural-and-period.md [E1,E2… 共17]` | `1 0 0 0` | `检败` | `9997 / — / — / —` | `MISSING` |
| `historical-contract-and-legitimacy-craft/references/05-source-index-and-adjudication.md [无编号]` | `1 0 0 0` | `规` | `12580 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/SKILL.md [P4]` | `1 0 0 0` | `规怎败` | `4913 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `166 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/examples.md [无编号]` | `1 0 1 1` | `反` | `2513 / — / 13654 / 13654` | `BLOCK_LOST` |
| `historical-fiction-craft-b03/references/p4-field-guide.md [A-07-B03,RH-01… 共9]` | `1 0 0 0` | `规怎例反适` | `6685 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/rules.md [RH-01,RH-02… 共18]` | `1 0 0 0` | `规怎例适败` | `13678 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/scope-and-conflicts.md [C10,C6,C7,C8,C9]` | `1 1 0 0` | `适` | `4438 / 31679 / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `2732 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/techniques.md [无编号]` | `1 0 0 0` | `例` | `2544 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `2797 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/templates/historical-diagnosis.md [无编号]` | `1 0 0 0` | `∅` | `927 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/templates/history-fiction-ratio.md [无编号]` | `1 0 0 0` | `∅` | `1095 / — / — / —` | `MISSING` |
| `historical-fiction-craft-b03/templates/real-figure-audit.md [无编号]` | `1 0 0 0` | `∅` | `990 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/SKILL.md [P4]` | `1 0 0 0` | `反败` | `7492 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `190 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/anti-examples.md [无编号]` | `1 0 0 0` | `规反` | `3905 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/document-plot.md [无编号]` | `1 0 0 0` | `∅` | `5374 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/examples.md [DOCUMENT-PLOT,KINSHIP-LOVE,MADNESS-MIND,OATH-TOKEN,PROPHECY-SONG,TERRAIN-SIGNAL]` | `1 0 1 1` | `反` | `4878 / — / 13654 / 13654` | `BLOCK_LOST` |
| `historical-fiction-plot-forge/failure-modes.md [无编号]` | `1 0 0 0` | `规检` | `3070 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/kinship-love.md [无编号]` | `1 0 0 0` | `∅` | `6689 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/madness-mind.md [无编号]` | `1 0 0 0` | `∅` | `5912 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/oath-token.md [无编号]` | `1 0 0 0` | `怎` | `5317 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/prophecy-song.md [无编号]` | `1 0 0 0` | `∅` | `5012 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `393 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/references/source-contract-and-decisions.md [无编号]` | `1 0 0 0` | `败` | `3599 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/sources.md [无编号]` | `1 0 0 0` | `∅` | `2920 / — / — / —` | `MISSING` |
| `historical-fiction-plot-forge/terrain-signal.md [无编号]` | `1 0 0 0` | `规` | `5641 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/SKILL.md [P4]` | `1 0 0 0` | `规怎检败` | `7354 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `238 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/conflicts-and-exceptions.md [无编号]` | `1 0 0 0` | `规例反` | `2813 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/disguise-cost.md [无编号]` | `1 0 0 0` | `规检` | `2668 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/era-sensitivity.md [无编号]` | `1 0 0 0` | `规` | `2194 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/failure-modes.md [无编号]` | `1 0 0 0` | `规` | `2791 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/finance-and-instrument.md [无编号]` | `1 0 0 0` | `怎例检` | `2884 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/history-interface.md [无编号]` | `1 0 0 0` | `规检` | `2952 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/hunt-and-pursuit.md [无编号]` | `1 0 0 0` | `检败` | `3082 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/justice-without-forensics.md [无编号]` | `1 0 0 0` | `规检` | `2700 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/oath-marriage-inheritance.md [无编号]` | `1 0 0 0` | `检` | `3116 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/performance-and-scapegoat.md [无编号]` | `1 0 0 0` | `怎检` | `3045 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/reputation-target.md [无编号]` | `1 0 0 0` | `检` | `2811 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/rumor-and-narrative.md [无编号]` | `1 0 0 0` | `检` | `2855 / — / — / —` | `MISSING` |
| `historical-fiction-power-machine/references/source-decisions.md [无编号]` | `1 0 0 0` | `规检` | `5705 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/SKILL.md [无编号]` | `1 0 0 0` | `例败` | `4947 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `297 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/examples/conflict-missing.md [无编号]` | `1 0 0 0` | `∅` | `682 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/examples/normal-design.md [无编号]` | `1 0 0 0` | `检` | `553 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/examples/worked-example.md [无编号]` | `1 0 0 0` | `∅` | `1099 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/01-time-institution-and-power.md [无编号]` | `1 0 0 0` | `规例反适败` | `3907 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/02-space-objects-and-livelihood.md [无编号]` | `1 0 0 0` | `规例反适败` | `3691 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/03-blood-identity-and-unreliable-eyes.md [无编号]` | `1 0 0 0` | `规例反适败` | `3734 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/04-voice-frame-and-settlement.md [无编号]` | `1 0 0 0` | `规例反适败` | `2851 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/05-antipatterns-and-boundaries.md [无编号]` | `1 0 0 0` | `例反适` | `3682 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/06-source-index.md [无编号]` | `1 0 0 0` | `∅` | `384 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/references/source-index.md [无编号]` | `1 0 0 0` | `例` | `5617 / — / — / —` | `MISSING` |
| `historical-immersion-and-stakes/templates/historical-causality.md [无编号]` | `1 0 0 0` | `∅` | `1211 / — / — / —` | `MISSING` |

---

## 题材 07 求生灾变（阈值 20%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 07 求生灾变

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；本题材按第 5.1 节收紧到 20%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`castaway-salvage-stronghold`、`survival-crisis-escalation`、`wilderness-disaster-survival-craft-b01`

**覆盖率**：已对齐 1 / v0 文件 28 = **3.6%**（v1/v2/v3 各版本有对应：0 / 1 / 1）

**flag 计数**：BLOCK_LOST=1；MISSING=27

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `castaway-salvage-stronghold/SKILL.md [无编号]` | `1 0 0 0` | `规怎例败` | `11358 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `222 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/examples/worked-example.md [无编号]` | `1 0 0 0` | `规怎检` | `3162 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/01-inventory-and-measurement.md [B02-R1,B02-R2,B02-R3]` | `1 0 0 0` | `规例反适` | `5679 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/02-shelter-engineering.md [B02-R4,B02-R5]` | `1 0 0 0` | `规例反适` | `3513 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/03-salvage-refit-chain.md [B02-R6,B02-R7]` | `1 0 0 0` | `规` | `3510 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/04-contact-and-signal.md [B02-R8,B02-R9]` | `1 0 0 0` | `规例适败` | `4869 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/05-group-governance.md [B02-R10,B02-R11]` | `1 0 0 0` | `规例适` | `4504 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/06-cost-and-aftermath.md [B02-R12,B02-R13]` | `1 0 0 0` | `规反` | `4618 / — / — / —` | `MISSING` |
| `castaway-salvage-stronghold/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `4960 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/SKILL.md [无编号]` | `1 0 0 0` | `规怎例反检适败` | `19660 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `787 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/examples/worked-example.md [AGENT3]` | `1 0 0 0` | `例检适` | `6431 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/01-resource-ledger.md [AGENT3,R1,R2]` | `1 0 0 0` | `规怎例反适` | `9583 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/02-escalation-ladder.md [AGENT3,R3,R4]` | `1 0 0 0` | `规怎例反适` | `9009 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/03-group-governance.md [AGENT3,R10,R8,R9]` | `1 0 0 0` | `规怎例反检适败` | `14474 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/04-shelter-salvage.md [AGENT3,R5,R6,R7]` | `1 0 0 0` | `规怎例反适` | `14869 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/05-morale-signal-irony.md [AGENT3,R11,R12,R13,R14,R15]` | `1 0 0 0` | `规怎例反检适败` | `22590 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/06-ecology-time-and-power.md [无编号]` | `1 0 0 0` | `规例反适` | `7841 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/07-source-roles-and-contrasts.md [PG10076,PG11703… 共13]` | `1 0 0 0` | `怎例反败` | `20838 / — / — / —` | `MISSING` |
| `survival-crisis-escalation/references/source-index.md [A-08-B03,P3]` | `1 0 0 0` | `例` | `10829 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/SKILL.md [无编号]` | `1 0 0 0` | `规怎反败` | `10721 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/agents/openai.yaml [无编号]` | `1 0 0 0` | `检` | `1497 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/references/conflicts-and-exceptions.md [C-1,C-2,C-3,C-4]` | `1 0 0 0` | `∅` | `5761 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/references/failure-modes.md [无编号]` | `1 0 0 0` | `规例适败` | `3206 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/references/rules.md [R-A,R-B… 共11]` | `1 0 1 1` | `规怎反检适败` | `13387 / — / 12692 / 12748` | `BLOCK_LOST` |
| `wilderness-disaster-survival-craft-b01/references/scene-patterns.md [S-1,S-2,S-3,S-4,S-5]` | `1 0 0 0` | `∅` | `4796 / — / — / —` | `MISSING` |
| `wilderness-disaster-survival-craft-b01/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `7770 / — / — / —` | `MISSING` |

---

## 题材 08 探险寻宝（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 08 探险寻宝

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`adventure-treasure-craft`、`adventure-treasure-craft-b02`、`adventure-treasure-craft-b03`

**覆盖率**：已对齐 3 / v0 文件 31 = **9.7%**（v1/v2/v3 各版本有对应：1 / 3 / 3）

**flag 计数**：BLOCK_LOST=3；MISSING=28；SHRUNK=2

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `adventure-treasure-craft/SKILL.md [P4]` | `1 0 0 0` | `怎例反检` | `9279 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `167 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/examples/worked-example.md [无编号]` | `1 0 0 0` | `规` | `3955 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/01-treasure-and-clues.md [M01,M02,M03,M20]` | `1 0 0 0` | `规例反适` | `6030 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/02-pirates-and-villains.md [M05,M06,M07,M08,M09]` | `1 0 0 0` | `规例反适` | `7536 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/03-expedition-and-survival.md [M04,M10… 共9]` | `1 0 0 0` | `规例反检适` | `17119 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/04-law-and-detection.md [M14,M15,M16,M19,M25]` | `1 0 0 0` | `规怎例反适败` | `9336 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/05-riddles-and-nonhuman.md [M17,M18,M22,M23,M24,M27]` | `1 0 0 0` | `规例反检适` | `11755 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/06-endings-and-sources.md [M21,M28,M32]` | `1 0 0 0` | `规例反检适` | `12355 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/p4-field-guide.md [A-09-B01,M01… 共9]` | `1 0 0 0` | `规怎例反检适` | `5806 / — / — / —` | `MISSING` |
| `adventure-treasure-craft/references/version-and-provenance.md [P3]` | `1 0 0 0` | `∅` | `5081 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/SKILL.md [无编号]` | `1 0 0 0` | `∅` | `4214 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `283 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/examples/conflict-missing.md [无编号]` | `1 0 0 0` | `∅` | `658 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/examples/normal-design.md [无编号]` | `1 0 0 0` | `∅` | `567 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/references/examples.md [无编号]` | `1 1 1 1` | `反` | `1303 / 6160 / 6080 / 6080` | `BLOCK_LOST` |
| `adventure-treasure-craft-b02/references/rules.md [无编号]` | `1 0 1 1` | `例反检适` | `13015 / — / 9887 / 9890` | `SHRUNK;BLOCK_LOST` |
| `adventure-treasure-craft-b02/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `适败` | `1302 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `11274 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/references/techniques.md [T01,T02… 共8]` | `1 0 0 0` | `∅` | `4045 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/templates/adventure-diagnosis.md [无编号]` | `1 0 0 0` | `∅` | `895 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b02/templates/expedition-designer.md [无编号]` | `1 0 0 0` | `∅` | `1249 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/SKILL.md [无编号]` | `1 0 0 0` | `规怎反适败` | `7455 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/agents/openai.yaml [无编号]` | `1 0 0 0` | `规` | `1931 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/examples/worked-example.md [无编号]` | `1 0 0 0` | `规` | `3984 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/references/conflicts-and-exceptions.md [C1,C2,C3,C4]` | `1 0 0 0` | `例适` | `4119 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/references/rules.md [RE-01,RE-02… 共18]` | `1 0 1 1` | `规检` | `11455 / — / 9887 / 9890` | `SHRUNK;BLOCK_LOST` |
| `adventure-treasure-craft-b03/references/source-index.md [无编号]` | `1 0 0 0` | `∅` | `5851 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/references/subtype-routing.md [无编号]` | `1 0 0 0` | `∅` | `3006 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `检` | `2889 / — / — / —` | `MISSING` |
| `adventure-treasure-craft-b03/templates/adventure-diagnosis.md [无编号]` | `1 0 0 0` | `规检` | `1858 / — / — / —` | `MISSING` |

---

## 题材 09 喜剧（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 09 喜剧

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`comedy-beat-craft`、`comedy-scene-mechanics`、`comic-engine-craft`、`comic-fiction-diagnosis`

**覆盖率**：已对齐 0 / v0 文件 29 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=29

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `comedy-beat-craft/SKILL.md [A1,A2,A3,G1,G2]` | `1 0 0 0` | `规怎例适败` | `11989 / — / — / —` | `MISSING` |
| `comedy-beat-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `432 / — / — / —` | `MISSING` |
| `comedy-beat-craft/references/01-attribution-and-beats.md [无编号]` | `1 0 0 0` | `检` | `5010 / — / — / —` | `MISSING` |
| `comedy-beat-craft/references/02-mechanism-library.md [B1,B10,B11,B12,B5,B8]` | `1 0 0 0` | `检` | `5907 / — / — / —` | `MISSING` |
| `comedy-beat-craft/references/03-branches-and-prohibitions.md [无编号]` | `1 0 0 0` | `∅` | `5408 / — / — / —` | `MISSING` |
| `comedy-beat-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `∅` | `10680 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/SKILL.md [无编号]` | `1 0 0 0` | `规例反检败` | `11521 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/agents/openai.yaml [无编号]` | `1 0 0 0` | `检` | `1002 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/references/01-narrator-devices.md [无编号]` | `1 0 0 0` | `规例反适` | `5848 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/references/02-incongruity-devices.md [无编号]` | `1 0 0 0` | `检` | `6170 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/references/03-plot-devices.md [无编号]` | `1 0 0 0` | `反适` | `8098 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/references/04-satire-costs.md [无编号]` | `1 0 0 0` | `∅` | `5127 / — / — / —` | `MISSING` |
| `comedy-scene-mechanics/references/05-source-index.md [无编号]` | `1 0 0 0` | `规` | `8510 / — / — / —` | `MISSING` |
| `comic-engine-craft/SKILL.md [无编号]` | `1 0 0 0` | `规例败` | `14355 / — / — / —` | `MISSING` |
| `comic-engine-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `665 / — / — / —` | `MISSING` |
| `comic-engine-craft/examples/worked-example.md [无编号]` | `1 0 0 0` | `例` | `2222 / — / — / —` | `MISSING` |
| `comic-engine-craft/references/01-partner-engines.md [C1,C2,C3,C4,C5]` | `1 0 0 0` | `规适` | `9514 / — / — / —` | `MISSING` |
| `comic-engine-craft/references/02-satire-engines.md [C13,C6,C7,C8,C9]` | `1 0 0 0` | `例适` | `11218 / — / — / —` | `MISSING` |
| `comic-engine-craft/references/03-openings-and-formats.md [无编号]` | `1 0 0 0` | `规例反适败` | `11283 / — / — / —` | `MISSING` |
| `comic-engine-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `例` | `6520 / — / — / —` | `MISSING` |
| `comic-engine-craft/references/05-confidence-and-feedback.md [无编号]` | `1 0 0 0` | `例适败` | `5439 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检败` | `14055 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `619 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/examples/worked-example.md [G1,G2,G3]` | `1 0 0 0` | `例检` | `6749 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/references/01-attribution-and-evidence.md [B1-01,B1-02,B1-04,B1-11]` | `1 0 0 0` | `例反检适` | `5065 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/references/02-satire-and-boundaries.md [B1-03,B1-06,B1-07,B1-08,B1-12]` | `1 0 0 0` | `规败` | `5444 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/references/03-repetition-openings-payoff.md [B1-05,B1-09,B1-10]` | `1 0 0 0` | `规反检适` | `6423 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/references/04-source-index.md [无编号]` | `1 0 0 0` | `例` | `6134 / — / — / —` | `MISSING` |
| `comic-fiction-diagnosis/references/05-conflicts-and-anti-patterns.md [K-1,K-2,K-3,K-4]` | `1 0 0 0` | `规` | `7207 / — / — / —` | `MISSING` |

---

## 题材 10 职业竞技（阈值 20%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 10 职业竞技

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **20%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；本题材按第 5.1 节收紧到 20%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`competition-underdog-arc`、`profession-competition-craft`、`vocation-proof-and-price`

**覆盖率**：已对齐 0 / v0 文件 38 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=38

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `competition-underdog-arc/SKILL.md [无编号]` | `1 0 0 0` | `规怎例反检败` | `15524 / — / — / —` | `MISSING` |
| `competition-underdog-arc/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `1241 / — / — / —` | `MISSING` |
| `competition-underdog-arc/examples/worked-example.md [无编号]` | `1 0 0 0` | `例检适` | `5699 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/01-arena-and-stakes.md [无编号]` | `1 0 0 0` | `怎适败` | `3602 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/02-underdog-training-and-cost.md [R2,R3,R4]` | `1 0 0 0` | `例反适败` | `7412 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/03-setback-rival-and-public-test.md [R5,R6,R7]` | `1 0 0 0` | `规例反检适` | `5417 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/04-endings-ethics-and-counterexamples.md [R11,R8,R9]` | `1 0 0 0` | `规怎例反败` | `4907 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/05-diagnosis-and-revision.md [R10,R12,R15]` | `1 0 0 0` | `怎反检` | `6216 / — / — / —` | `MISSING` |
| `competition-underdog-arc/references/source-index.md [无编号]` | `1 0 0 0` | `检` | `9813 / — / — / —` | `MISSING` |
| `profession-competition-craft/SKILL.md [P4]` | `1 0 0 0` | `规怎例反适败` | `29782 / — / — / —` | `MISSING` |
| `profession-competition-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `190 / — / — / —` | `MISSING` |
| `profession-competition-craft/counterexamples.md [无编号]` | `1 0 0 0` | `规反` | `7895 / — / — / —` | `MISSING` |
| `profession-competition-craft/examples.md [无编号]` | `1 0 0 0` | `例败` | `10699 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/01-scope-and-entry.md [E1,E2… 共7]` | `1 0 0 0` | `规怎例适` | `11837 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/02-training-and-competence.md [无编号]` | `1 0 0 0` | `怎例反检适` | `9898 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/03-work-process-and-ecosystem.md [无编号]` | `1 0 0 0` | `怎例适败` | `10586 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/04-pay-contract-and-career.md [无编号]` | `1 0 0 0` | `怎例适` | `8916 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/05-competition-and-ranking.md [无编号]` | `1 0 0 0` | `规例适败` | `9599 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/06-ethics-cost-and-endings.md [无编号]` | `1 0 0 0` | `规例适败` | `10640 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/07-templates.md [无编号]` | `1 0 0 0` | `例检` | `8250 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/08-diagnosis-and-revision.md [F1,F10… 共12]` | `1 0 0 0` | `规怎例反败` | `11091 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/09-per-source-playbook.md [无编号]` | `1 0 0 0` | `规怎例检适败` | `37363 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/historical-provenance.md [无编号]` | `1 0 0 0` | `∅` | `586 / — / — / —` | `MISSING` |
| `profession-competition-craft/references/rework-decision.md [无编号]` | `1 0 0 0` | `例败` | `3689 / — / — / —` | `MISSING` |
| `profession-competition-craft/sources-index.md [无编号]` | `1 0 0 0` | `例` | `7185 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/SKILL.md [无编号]` | `1 0 0 0` | `怎例适败` | `13216 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `1274 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/counterexamples.md [无编号]` | `1 0 0 0` | `规怎例反适败` | `3930 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/examples.md [无编号]` | `1 0 0 0` | `败` | `5511 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/01-source-roles.md [无编号]` | `1 0 0 0` | `反` | `5689 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/02-rulings.md [无编号]` | `1 0 0 0` | `规` | `4646 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/03-proof-machine.md [无编号]` | `1 0 0 0` | `∅` | `4212 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/04-loyalty-and-price.md [无编号]` | `1 0 0 0` | `∅` | `4021 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/05-disability-and-exit.md [无编号]` | `1 0 0 0` | `怎例反败` | `3533 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/06-diagnosis-and-revision.md [无编号]` | `1 0 0 0` | `检` | `4641 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/07-per-source-playbook.md [无编号]` | `1 0 0 0` | `∅` | `4438 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/references/08-provenance-and-compat.md [无编号]` | `1 0 0 0` | `∅` | `3216 / — / — / —` | `MISSING` |
| `vocation-proof-and-price/sources-index.md [无编号]` | `1 0 0 0` | `规例` | `4092 / — / — / —` | `MISSING` |

---

## 题材 11 身份复仇权谋（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 11 身份复仇权谋

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`identity-revenge-intrigue-b06`、`identity-revenge-powercraft-fiction`、`intrigue-revenge-craft-b04`、`revenge-identity-craft`、`revenge-intrigue-architecture`、`revenge-intrigue-craft`

**覆盖率**：已对齐 0 / v0 文件 60 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=60

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `identity-revenge-intrigue-b06/SKILL.md [无编号]` | `1 0 0 0` | `例适败` | `6206 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `294 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/examples/conflict-missing.md [无编号]` | `1 0 0 0` | `∅` | `983 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/examples/normal-design.md [无编号]` | `1 0 0 0` | `∅` | `1235 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/alliances-power.md [无编号]` | `1 0 0 0` | `规例反` | `2978 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/diagnosis-and-revision.md [无编号]` | `1 0 0 0` | `反检` | `2127 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/identity-evidence.md [无编号]` | `1 0 0 0` | `例反适` | `2262 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/motives-and-costs.md [无编号]` | `1 0 0 0` | `反适` | `1591 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/revelation-and-repair.md [无编号]` | `1 0 0 0` | `反` | `1647 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/references/source-index.md [无编号]` | `1 0 0 0` | `例` | `6340 / — / — / —` | `MISSING` |
| `identity-revenge-intrigue-b06/templates/identity-stakes-map.md [无编号]` | `1 0 0 0` | `∅` | `1494 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检败` | `9827 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/agents/openai.yaml [无编号]` | `1 0 0 0` | `规怎` | `1102 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/references/conflict-ledger.md [X-1,X-2,X-3,X-4]` | `1 0 0 0` | `适` | `3277 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/references/id-disguise-engine.md [ID-1,ID-2,ID-3,ID-4]` | `1 0 0 0` | `∅` | `3816 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/references/power-machine.md [PM-1,PM-2,PM-3,PM-4,PM-5]` | `1 0 0 0` | `例检适` | `4374 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/references/revenge-cost-ledger.md [RC-1,RC-2,RC-3]` | `1 0 0 0` | `例` | `4329 / — / — / —` | `MISSING` |
| `identity-revenge-powercraft-fiction/references/source-index.md [无编号]` | `1 0 0 0` | `检` | `5792 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/SKILL.md [无编号]` | `1 0 0 0` | `规例检适败` | `7126 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/agents/openai.yaml [无编号]` | `1 0 0 0` | `规怎例反适` | `1538 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/examples/worked-cases.md [无编号]` | `1 0 0 0` | `例检` | `3567 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/references/legacy-metadata.md [无编号]` | `1 0 0 0` | `规例适败` | `3770 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/references/rules.md [RM-01,RM-02… 共11]` | `1 0 0 0` | `规反适` | `17092 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `规例反适` | `5009 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/references/source-index.md [B-07-B04]` | `1 0 0 0` | `规` | `5959 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/references/techniques.md [无编号]` | `1 0 0 0` | `败` | `5243 / — / — / —` | `MISSING` |
| `intrigue-revenge-craft-b04/templates/intrigue-diagnosis.md [无编号]` | `1 0 0 0` | `适` | `3278 / — / — / —` | `MISSING` |
| `revenge-identity-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎检适败` | `10071 / — / — / —` | `MISSING` |
| `revenge-identity-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `879 / — / — / —` | `MISSING` |
| `revenge-identity-craft/examples/worked-cases.md [无编号]` | `1 0 0 0` | `反检适` | `2795 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/01-identity-engines.md [无编号]` | `1 0 0 0` | `例反适` | `9048 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/02-revenge-closure.md [无编号]` | `1 0 0 0` | `例反适败` | `6350 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/03-lineage-power-and-limits.md [无编号]` | `1 0 0 0` | `例反` | `7599 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `规` | `5806 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/05-decision-guide.md [V1,V10… 共14]` | `1 0 0 0` | `规例检适败` | `7970 / — / — / —` | `MISSING` |
| `revenge-identity-craft/references/legacy-metadata.md [无编号]` | `1 0 0 0` | `∅` | `3594 / — / — / —` | `MISSING` |
| `revenge-identity-craft/templates/identity-causal-chain.md [无编号]` | `1 0 0 0` | `∅` | `2007 / — / — / —` | `MISSING` |
| `revenge-identity-craft/templates/revenge-closure.md [无编号]` | `1 0 0 0` | `∅` | `2101 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/SKILL.md [无编号]` | `1 0 0 0` | `规例检适败` | `15140 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `478 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/examples/worked-example.md [WAVE4]` | `1 0 0 0` | `反检` | `5989 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/01-identity-claim-and-proof.md [R1,R2]` | `1 0 0 0` | `规怎例反适` | `8362 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/02-secrets-and-masks.md [R3,R4]` | `1 0 0 0` | `规怎例反适` | `6958 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/03-institutions-and-patronage.md [R13,R14,R5,R6,R7]` | `1 0 0 0` | `规怎例反检适` | `11700 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/04-revenge-accounting.md [R12,R8,R9]` | `1 0 0 0` | `规怎例反适败` | `5453 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/05-reveal-and-boundaries.md [R10,R11]` | `1 0 0 0` | `规怎例反检适败` | `6258 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/06-post-victory-control.md [无编号]` | `1 0 0 0` | `例` | `3351 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/legacy-metadata.md [无编号]` | `1 0 0 0` | `∅` | `523 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/source-index.md [WAVE4]` | `1 0 0 0` | `规例` | `10986 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/references/wave4-conditional-decision.md [WAVE4]` | `1 0 0 0` | `规` | `2575 / — / — / —` | `MISSING` |
| `revenge-intrigue-architecture/templates/intrigue-seven-tables.md [T1,T10… 共10]` | `1 0 0 0` | `∅` | `2545 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎例反检败` | `18351 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `1187 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/assets/icon-large.svg [无编号]` | `1 0 0 0` | `∅` | `430 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/assets/icon-small.svg [无编号]` | `1 0 0 0` | `∅` | `421 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/references/counterexamples-and-limits.md [无编号]` | `1 0 0 0` | `规例反适败` | `6028 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/references/identity-disguise-and-proof.md [A1,A10… 共10]` | `1 0 0 0` | `怎例反适败` | `8056 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/references/intrigue-ledger.md [B1,B10… 共10]` | `1 0 0 0` | `例适` | `7053 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/references/revenge-arc.md [C1,C2,C3,C4,C5,C6]` | `1 0 0 0` | `规适败` | `4024 / — / — / —` | `MISSING` |
| `revenge-intrigue-craft/references/sources-index.md [无编号]` | `1 0 0 0` | `规` | `8369 / — / — / —` | `MISSING` |

---

## 题材 12 儿童青少年（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 12 儿童青少年

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`child-story-craft`、`children-ya-craft-b05`、`childrens-youth-fiction-craft-b01`

**覆盖率**：已对齐 2 / v0 文件 29 = **6.9%**（v1/v2/v3 各版本有对应：1 / 2 / 2）

**flag 计数**：BLOCK_LOST=2；MISSING=27；SHRUNK=2

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `child-story-craft/SKILL.md [P4]` | `1 0 0 0` | `规怎例检败` | `8344 / — / — / —` | `MISSING` |
| `child-story-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `164 / — / — / —` | `MISSING` |
| `child-story-craft/references/01-oral-telling.md [无编号]` | `1 0 0 0` | `规例检` | `7911 / — / — / —` | `MISSING` |
| `child-story-craft/references/02-child-narrator.md [无编号]` | `1 0 0 0` | `规` | `4007 / — / — / —` | `MISSING` |
| `child-story-craft/references/03-formats.md [无编号]` | `1 0 0 0` | `例` | `1652 / — / — / —` | `MISSING` |
| `child-story-craft/references/04-source-index.md [无编号]` | `1 0 0 0` | `反` | `6369 / — / — / —` | `MISSING` |
| `child-story-craft/references/p4-field-guide.md [B-05-B03,S1… 共9]` | `1 0 0 0` | `规怎例反适` | `9048 / — / — / —` | `MISSING` |
| `child-story-craft/references/version-and-provenance.md [无编号]` | `1 0 0 0` | `∅` | `4846 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/SKILL.md [无编号]` | `1 0 0 0` | `怎例适败` | `7398 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `501 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/examples/conflict-missing.md [无编号]` | `1 0 0 0` | `∅` | `696 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/examples/hard-boundary-ethics.md [无编号]` | `1 0 0 0` | `∅` | `1395 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/examples/normal-design.md [无编号]` | `1 0 0 0` | `∅` | `745 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/references/examples.md [无编号]` | `1 1 1 1` | `规反` | `3774 / 2085 / 2166 / 2166` | `SHRUNK;BLOCK_LOST` |
| `children-ya-craft-b05/references/rules.md [B-05-B02]` | `1 0 1 1` | `规例反检适` | `12223 / — / 9395 / 9428` | `SHRUNK;BLOCK_LOST` |
| `children-ya-craft-b05/references/scope-and-conflicts.md [无编号]` | `1 0 0 0` | `例适` | `4123 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/references/source-index.md [B-05-B02]` | `1 0 0 0` | `∅` | `11013 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/references/techniques.md [C01,C02… 共7]` | `1 0 0 0` | `规怎例反适` | `5738 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/templates/child-diagnosis.md [无编号]` | `1 0 0 0` | `∅` | `1389 / — / — / —` | `MISSING` |
| `children-ya-craft-b05/templates/child-story-designer.md [无编号]` | `1 0 0 0` | `∅` | `1282 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检适` | `7236 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/agents/openai.yaml [无编号]` | `1 0 0 0` | `检` | `1301 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/examples/normal-design.md [无编号]` | `1 0 0 0` | `规检` | `2787 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/examples/revision-conflict.md [无编号]` | `1 0 0 0` | `规怎` | `2295 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/references/age-band-rules.md [无编号]` | `1 0 0 0` | `规` | `2911 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/references/conflicts-and-exclusions.md [C1,C2,C3,C4]` | `1 0 0 0` | `规适` | `3625 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/references/source-index.md [无编号]` | `1 0 0 0` | `规` | `4759 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/references/techniques.md [T01,T02… 共12]` | `1 0 0 0` | `规例败` | `5151 / — / — / —` | `MISSING` |
| `childrens-youth-fiction-craft-b01/templates/diagnosis-card.md [无编号]` | `1 0 0 0` | `规检` | `1828 / — / — / —` | `MISSING` |

---

## 题材 13 异世界穿越（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 13 异世界穿越

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`isekai-crossworld-craft`、`isekai-crossworld-craft-b01`、`isekai-crossworld-craft-b02`

**覆盖率**：已对齐 0 / v0 文件 18 = **0.0%**（v1/v2/v3 各版本有对应：0 / 0 / 0）

**flag 计数**：MISSING=18

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `isekai-crossworld-craft/SKILL.md [无编号]` | `1 0 0 0` | `规怎检败` | `8099 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft/agents/openai.yaml [无编号]` | `1 0 0 0` | `规` | `1352 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft/references/conflicts-and-exceptions.md [C1,C2,C3]` | `1 0 0 0` | `规例反` | `3887 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft/references/mechanism-taxonomy.md [无编号]` | `1 0 0 0` | `规例适` | `5585 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft/references/rule-verdicts.md [R1,R10… 共14]` | `1 0 0 0` | `规` | `8166 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft/references/source-index.md [无编号]` | `1 0 0 0` | `例反适` | `6297 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/SKILL.md [无编号]` | `1 0 0 0` | `规怎例败` | `9237 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/agents/openai.yaml [无编号]` | `1 0 0 0` | `规反` | `1062 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/references/conflicts-and-exceptions.md [无编号]` | `1 0 0 0` | `规怎例反` | `5039 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/references/mechanism-taxonomy.md [E1,E2,E3,E4,E5]` | `1 0 0 0` | `规怎反败` | `5332 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/references/rule-verdicts.md [R1,R10… 共12]` | `1 0 0 0` | `规例反检适` | `8888 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b01/references/source-index.md [无编号]` | `1 0 0 0` | `例适` | `5236 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/SKILL.md [无编号]` | `1 0 0 0` | `规怎例检败` | `12997 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/agents/openai.yaml [无编号]` | `1 0 0 0` | `规反` | `1221 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md [无编号]` | `1 0 0 0` | `规怎反检败` | `7133 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/references/mechanism-taxonomy.md [无编号]` | `1 0 0 0` | `∅` | `5699 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/references/rule-verdicts.md [R1,R10… 共16]` | `1 0 0 0` | `规反检适败` | `15661 / — / — / —` | `MISSING` |
| `isekai-crossworld-craft-b02/references/source-index.md [无编号]` | `1 0 0 0` | `例适` | `8643 / — / — / —` | `MISSING` |

---

## 题材 14 年代现实（阈值 30%）

# K1 机械盘点 raw 表 · genre-fiction-craft / 题材 14 年代现实

- 生成日期：2026-11-04（只追加不覆盖；重生成另起带日期文件）
- 数据来源：`git show <提交>:<路径>`，提交 v0=d23c461、v1=d2003e4、v2=3c1cb5f、v3=2a10c07；不检出、不改仓库、不复制原件、不放作品全文。
- 盘点单位：**v0 文件**（覆盖率按「已对齐的 v0 文件数 / 总数」计）。unit_id 附该文件内出现的内部规则编号。
- 阈值：任一更早版本(v0/v1/v2) → v3 缩减超过 **30%** 或超过 **1.5 KB** 打 SHRUNK（兼覆盖 2.3 节的 v2→v3 删除）；默认 30%。
- 字段（附录 A.1）：`unit_id` / `versions`(v0 v1 v2 v3，出现与否) / `blocks` / `bytes` / `flag`。
- `blocks` 简写：规=规则、怎=怎么做、例=例外、反=反例、检=检查、适=适用、败=失败、∅=未检出；由标签行关键词机械识别，非精读结论。
- `bytes` 为「最佳匹配候选文件」的字节数；版本重组后是信号，不是逐规则应恢复的量。
- `flag`：`MISSING`(v3 无对应)、`SHRUNK`(超阈值)、`BLOCK_LOST`(v0 有而 v3 匹配文件无的小块，仅 basename 高置信对齐时判)、`RENUMBERED?`(编号消失但按标题/前缀对齐)、`—`(对齐且无信号)。
- 对齐方法（2.3 节「新旧前缀 + 标题」，不比编号）：`basename` > `title`/`title~`(标题) > `prefix`(改号前缀) > `id`。
- 编号改号对照：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 谱系 v0 来源：`realism-craft-b09`

**覆盖率**：已对齐 3 / v0 文件 14 = **21.4%**（v1/v2/v3 各版本有对应：3 / 3 / 3）

**flag 计数**：MISSING=11；RENUMBERED?=3

| unit_id | versions | blocks | bytes (v0/v1/v2/v3) | flag |
|---|---|---|---|---|
| `realism-craft-b09/SKILL.md [无编号]` | `1 0 0 0` | `规例适` | `7206 / — / — / —` | `MISSING` |
| `realism-craft-b09/agents/openai.yaml [无编号]` | `1 0 0 0` | `∅` | `192 / — / — / —` | `MISSING` |
| `realism-craft-b09/examples/worked-example.md [B09]` | `1 0 0 0` | `∅` | `2189 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/01-class-and-material-constraints.md [B09,RC1,RC2,RC3]` | `1 0 0 0` | `例反检适` | `3069 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/02-family-community-and-growth.md [B09,RC4,RC5,RC6]` | `1 1 1 1` | `反适` | `2711 / 16430 / 17033 / 16763` | `RENUMBERED?` |
| `realism-craft-b09/references/03-agency-voice-and-endings.md [B09,RC10,RC7,RC8,RC9]` | `1 1 1 1` | `反适` | `3548 / 16430 / 17033 / 16763` | `RENUMBERED?` |
| `realism-craft-b09/references/04-history-genre-and-evidence.md [B09]` | `1 0 0 0` | `例` | `3138 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/05-workflow-and-failures.md [B09,W1,W2,W3,W4]` | `1 1 1 1` | `适` | `3379 / 16430 / 17033 / 16763` | `RENUMBERED?` |
| `realism-craft-b09/references/rules.md [B09]` | `1 0 0 0` | `∅` | `1599 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/scope-and-conflicts.md [B09]` | `1 0 0 0` | `适` | `1380 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/source-index.md [B-09]` | `1 0 0 0` | `∅` | `3597 / — / — / —` | `MISSING` |
| `realism-craft-b09/references/techniques.md [B09]` | `1 0 0 0` | `∅` | `1199 / — / — / —` | `MISSING` |
| `realism-craft-b09/templates/realism-designer.md [无编号]` | `1 0 0 0` | `适` | `1626 / — / — / —` | `MISSING` |
| `realism-craft-b09/templates/realism-diagnosis.md [无编号]` | `1 0 0 0` | `∅` | `1529 / — / — / —` | `MISSING` |


---

## genre 机械对齐阻塞（如实记录）


- **genre 覆盖率偏低是机械对齐的真实结果，不是跳过**：v0 题材文件名为「编号 + 描述」（如 `01-information-and-clues.md`），v3 重组为英文名（如 `fairness-and-format.md`），basename 几乎不重叠；v0 规则编号（`R1`、`CM-xx` 等）与标题在 v3 改为题材前缀编号（如 `MY-xx`）且标题重写，按「新旧前缀 + 标题」也难以对齐。依据第 2.8 节「v1→v2 题材目录改英文名，文件也重组了，没有办法按文件名对齐」与第 2.3 节，机械盘点只能出这些信号；逐条用规则编号和标题对齐是 W2 定向精读的任务。

- 已对齐的多为跨版本保留同名的 `examples.md` / 机制卡类文件；`MISSING` 行逐条列出，不伪造行、不跳过。

- `fantasy-adventure-structure-lab`（第 5 节注「部分进 08」）、`supernatural-power-craft`（「部分进 03」）为**跨题材多归属**：机械盘点按主归属 04 登记，不强行拆成两份对齐；08/03 的归属待 W2 定向精读核定。

- v1→v2 题材目录由中文名改英文名，按 `NN-` 数字前缀定位对应题材目录；genre 级公共入口文件不纳入题材池，不把 59 份 v0 SKILL.md 强行对齐到 1 份 v3 SKILL.md 来抬高覆盖率。

- **编号内嵌标题的解析限制**：v3 机制卡编号写在标题括号内（如 `# 关系机制卡（RO-K001–RO-K120）`），不是标准 `## 编号 标题` 形式，机械解析提不出这类 ID；2.3 节的 `RO-K121–166`（v2→v3 删除）、`05-science-fiction/mechanisms.md` 32.4→20.4 KB 等，须 W2 定向精读逐卡/逐文件核定，本表不据此伪造对齐行。
