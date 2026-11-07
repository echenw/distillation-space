# W3 派发依据 · 分片台账与证据修正（W1 / W2 汇总）

- 轮次：W1.5 / W2 汇总轮｜代理：Agent 1（规范与门禁仲裁员）｜日期：2026-11-04
- 性质：**只记录 W1 五个 Worker 的只读边界结论与 W2 只读证据修正，不新增任何材料知识、不做逐条决定**。
- 依据：计划附录 F（执行分片表）、§5.1、§6.1、§2.3–§2.6；W1 五个 Worker 回传的边界清单；W2 只读核对结论；`notes/loss-inventory/raw/*-2026-11-04-r2.md`（K1 返工表）。
- 分片上限：附录 F 每片 v0 精读量约 100 KB 以内；单个 v0 skill 超过 100 KB 的按文件再切成 a1、a2……。

---

## 一、W1 切片数字（可复核）

### 1.1 Agent 2 / 3 / 4 的非题材分片

| 片 | v0 来源 | 实测体量 | 切片 |
|---|---|---|---|
| S03b | scene-chapter-design-lab + action-fight-scene-craft | 108 KB | a1 53 KB / a2 54 KB（按两个 v0 skill 切） |
| S04a | narrative-pov-information-control + nonlinear-time-craft | 110.3 KB | 超 100 KB，需按文件再切（切法见 §2 ⑥） |
| S04b | character-psychology-trauma-craft + psycho-trauma-craft-b10 | 131.9 KB | 超 100 KB，需按文件再切 |
| S05a | plot-architecture | 222776 B | a1 111572 B + a2 111204 B |
| S05b | serialized-volume-planning | 177904 B | b1 90769 B + b2 87135 B |
| S06a | fiction-craft | 283915 B | a1 `rules.md` 101960 B（独占）/ a2 94823 B / a3 87132 B |
| S06c | reader-experience-and-critique + research-fact-verification | 74.6 KB | 一片 |

### 1.2 Agent 5（热门与幻想题材）

- 分片：G02 4 片 / G04 5 片 / G05 4 片 / G06 4 片 / G13 2 片 = **19 片，22 精读单元**。
- 与 §6.1 一致：G05 科幻归 Agent 5，与 G02 同属机制卡题材但**不是同一种丢失**（见 §2 ②③）。

### 1.3 Agent 6（其余题材 + G00 草案）

- **9 类切片**（§6.1 已修订：Agent 6 是 9 类题材 + G00 草案，不是 10 类）。
- 超每片 100 KB、需再切或上浮片数的项：
  - G10 ③ 119.4 KB
  - G11 两片约 105 KB
  - G01 ③ / G03 ② 约 104 KB

### 1.4 阈值（§5.1、附录 A.1、§6.1 口径约束）

- **三类收紧到 20%：G01 推理 / G07 求生灾变 / G10 职业竞技**（其余默认 30% 或缩减 >1.5 KB）。
- 缩减幅度是盘点信号，**不是应补回的量**；按 P1「以下情况不算丢失」三类逐条排除。

---

## 二、W2 证据修正（**只读核对结论**，W1 结论以此为准）

> 本节全部是 W2 的只读核对结果，只登记，不新增推断。W3 须按修正后的口径落笔。

### ① C-2 / S-1 出处修正

- **C-2「连续性回归三问」**：W1「疑已在 `character/references/diagnosis.md:160–162`」**作废**。v0 的 S04a 两个 skill（narrative-pov-information-control、nonlinear-time-craft）grep「回归三问」**零命中**；真实出处在 **S04b 的 `scene-revision.md:11`**（五项回归核查）。v3 `character/references/diagnosis.md:160–162` 是另一套「连续性回归三问」，只覆盖前两项，其余仍缺。**C-2 不属 S04a**，W3 不得按 S04a 分片处理它。
- **S-1「D6 全稿结构复核」11 项**：疑已在 `story/references/plot-diagnosis.md:317–327`，**缺三条细则**。W3 须比内容核定，不盲信计划 2.4 节的「仍缺」。

### ② RO-K 去重与逐卡分类（G02）

- v3 `02-romance/mechanisms.md` 的 **RO-K116–120 是 v2 RO-K162–166 的通用化改写**；46 张删除卡中这 5 张已有落点；**v2 原 116–120 未进 v3**。
- 逐卡分类：**Agent 5 的只读分类为 34 含通用机制 / 9 纯来源观察 / 3 待核；计划 2.3 节未给配额数字，不预设比例；W3 按 2.3 原文逐卡决定**。
  - **更正说明（W3 第 1 批，Agent 1）**：本节上一版写成「与计划 2.3 节『39 纯观察 / 7 含机制』口径不同、差异源于是否把卡末『不要普遍化』限制句计入机制、W3 先统一口径」，属**子代理误引**，现予更正。已只读核对计划 2.3 节原文：该节只有「多数卡…每张卡里通常有一条能通用的机制」「也有卡纯属来源观察…这类不恢复」「逐卡抽出通用机制，和 RO-K001–120 及 RO 规则去重后再决定；恢复的部分改写成自创情境，沿用 RO-K121 起的编号」，**没有任何配额数字**。34/9/3 只是 Agent 5 的只读分类线索，不是配额，也不构成与 2.3 节的「口径冲突」；W3 按 2.3 原文逐卡决定，不预设比例、不需要统一配额。**2.3 节原文不改动。**
- **W3 不得把 46 张整批当待恢复、不得重复补回已有落点的 5 张**；纯来源观察不恢复；恢复部分沿用 RO-K121 起编号并与 RO-K001–120 去重。

### ③ G05 逐卡压缩（不套 G02 做法）

- SF-K001–102 在 **v2 / v3 均连续 102 张，未删卡**；102 卡行 **29025 B → 18409 B**（均 285 → 180，约 −37%），属**逐卡压缩**。
- W3 按**字段找回**（逐卡补回被压掉的区分条件/反例/检查），**不套用 G02「补回删卡编号」的做法**。

### ④ G01 缩减发生在 v0→v1

- v0 346895 B → v3 `01-mystery` 59546 B（约 17%）；但 **v2→v3 九文件仅 −7% ~ +6%，无单件缩减 >20%**。
- 缩减发生在 **v0→v1**，W3 须**逐块对 v0 核**，不能只看 v2/v3 差；否则会把 v0→v1 重组误判成 v3 删除。

### ⑤ cross-media 的 X-1–X-6 与失败出口细化

- X-1–X-6 在 v0 有确切位置：**SK:67、02:16、06:11-12、06:40-41、03:15、04:16、05:43**；**v3 六组仍零命中**。
- W1「无失败出口」细化为：**SK:39、SK:56 已部分承接**；**§7 五类出口表、主流程出口、A/B 案备忘格式仍缺**。W3 按此清单补，不重复补已承接项。

### ⑥ S04a 再切（补足 §1.1 的「需再切」）

- **a1 = narrative-pov-information-control 全 8 文件 74532 B**
- **a2 = nonlinear-time-craft 全 9 文件 38384 B**

---

## 三、2.5 / 2.6 节残留与接口缺口（精确文件:行号）

### 3.1 来源残留（2.5 节，P3 收尾 + P4 全套各跑一次附录 B）

| 位置 | 残留 |
|---|---|
| fiction-planning `references/rules-drafting.md`、`rules-premise-and-structure.md`、`rules-revision-and-method.md` **第 8 行** | 「28 本材料标称 1808–1929 年……」 |
| fiction-planning `rules-drafting.md` **第 43、79、107、114、144 行** | 来源编号残片 `-14243`、`-8269`、`-2110`、`-4841`、`-3790` |
| fiction-planning `scope-and-conflicts.md` **第 74–76 行** | 残片 `-2236`、`-2111`，以及「1890 年代英国市场」「1911 年前的手册」 |
| fiction-planning `rules-revision-and-method.md:148`、`self-check-modern-and-zh.md:32` | 来源年代「1920 年代美国杂志市场」「1884 年的出版建议」 |
| genre `12-children-youth/more-examples.md:22` | 一部真实儿童书的情节元素 |
| character `references/boundaries-and-ethics.md:73` | 「书里明写……」 |
| genre `11-identity-revenge-intrigue/stance-and-boundaries.md` **IR-05D** | 疑似来源语境：「节本、翻译、未完稿……须绑定实际版本」「引文位置不可核时，就缩小主张」；正则查不出，P4 人工判断：若指学习材料则改写成针对用户自己资料的说法或删掉 |

### 3.2 合同与接口缺口（2.6 节）

| 位置 | 缺口 |
|---|---|
| cross-media `references/interactive-adaptation.md:55`；`templates/interactive-branch-sheet.md:41`；fiction-planning `references/diagnosis.md:411` | 运行文本残留 `NOT_PROVEN` 等审计词（替换口径见 `notes/suite-contract.md` 第二节） |
| preset-card-generation | 没有 `agents/openai.yaml`，没有负触发和转介，SKILL.md 没有失败出口；「规划、写章节、改稿去 AI 味、审阅章节」与 fiction-planning / story-architecture / line-editing 重叠；另外 7 个 skill 都没提到它 |
| cross-media | description 一个兄弟 skill 都没提，SKILL.md 没有失败出口（细化见 §2 ⑤） |
| 8 个 SKILL.md | 路由表都缺 R18 §3 建议的「需要时补读 / 缺料或冲突时的出口」两列 |

---

## 四、W3 派发仍缺（如实登记，非阻塞清单结论）

1. **S01 校准样例已回传**：`notes/source-synthesis/line-editing-and-proofreading.md` 第二节「校准样例与写法口径」为 W3 全体复用格式；本轮已由 Agent 1 静态核查（见 §五）。
2. **K1 返工表已定稿**：`notes/loss-inventory/raw/*-2026-11-04-r2.md` 与 `_summary-2026-11-04-r2.md` 为 W3 精读输入；**90.4% 单元标 `UNALIGNED?`，是待定向精读信号，不是丢失清单**。
3. **已补（W3 第 1 批，见 §六）**：S04b 按文件再切 a1/a2 的具体方案、Agent 6 四类超 100 KB 的按文件再切 / 片数上浮建议、G02 逐卡口径。
4. **仍待补**：W2 其余 Worker 的只读边界结论回传；Agent 6 四类超 100 KB 项的具体文件名与累计字节（由 Agent 6 回传，本台账不编造）；片数上浮需主代理确认；G00 草案与 `genre/SKILL.md` 定稿（W4）。
5. **误引撤销**：原第 3 条里「§2 ② 的逐卡口径统一（34/9/3 与 39/7 谁为准，需作者/主代理裁决）」**作废**——39/7 为子代理误引，2.3 节未给配额数字，不存在待裁决的配额口径；更正见 §2 ②。
6. **G05 处理口径**：按逐卡压缩按字段找回，**不套 G02 补编号做法**（§2 ③、§6.1）。

---

## 五、S01 静态核查结论索引（Agent 1 门禁职责，只读）

- 复核输出：`notes/quality/line-editing-and-proofreading/agent1-s01-desourcing-rescan-2026-11-04.txt`（附录 B 全 11 类原始 stdout）。
- 结论：EN-34–40 共 7 条在 v0 `d23c461:skills/style-refinement-and-proofreading/` 均有对应内容（C05/C08/C16/C18/C19/C21/C22），**非自创新规则**；附录 B 复扫与 Agent 2 一致（#6 命中 1、#10 命中 14，其余 13 组零命中，合计 15 条，逐条判允许、零违规）；状态词四词、禁用词、description 七兄弟名、路由表「补读/出口」两列、L-1/L-2 落点均齐。**静态核查通过，不含 GQ5 真实任务验证，未验证项不写成通过**。详见同目录 `agent1-s01-static-review-2026-11-04.md`。

---

## 六、W3 派发缺口补齐（W3 第 1 批，Agent 1 只记录不新增材料知识）

### 6.1 S04b 按文件再切 a1/a2（**推荐方案：按 v0 skill 边界切，与 §2 ⑥ S04a 同构**）

上限口径：100 KiB = 102400 B（若按 100000 B 计亦满足）。实测 v0 `d23c461` 两 skill 共 21 文件 **135037 B ≈ 131.9 KiB**，与 W1 回传一致。**两片均 ≤100 KiB、不拆任何单文件**。

**a1 = character-psychology-trauma-craft 全 10 文件 = 41223 B（40.3 KiB）**

| 文件 | 字节 | 累计 |
|---|---|---|
| `SKILL.md` | 8828 | 8828 |
| `agents/openai.yaml` | 636 | 9464 |
| `references/counterexamples.md` | 1776 | 11240 |
| `references/examples.md` | 3426 | 14666 |
| `references/psychological-mechanics.md` | 12168 | 26834 |
| `references/scene-revision.md` | 3152 | 29986 |
| `references/source-index.md` | 4960 | 34946 |
| `references/trauma-boundaries.md` | 2886 | 37832 |
| `templates/character-state-card.md` | 2298 | 40130 |
| `templates/revision-check.md` | 1093 | **41223** |

**a2 = psycho-trauma-craft-b10 全 11 文件 = 93814 B（91.6 KiB）**

| 文件 | 字节 | 累计 |
|---|---|---|
| `SKILL.md` | 9486 | 9486 |
| `agents/openai.yaml` | 525 | 10011 |
| `examples/scene-examples.md` | 6004 | 16015 |
| ★ `references/72-source-differences.md` | 20768 | 36783 |
| ★ `references/rules.md` | 24410 | 61193 |
| `references/scope-and-conflicts.md` | 3694 | 64887 |
| ★ `references/source-index.md` | 16925 | 81812 |
| `references/techniques.md` | 3940 | 85752 |
| `references/version-and-license.md` | 3036 | 88788 |
| `templates/psycho-trauma-designer.md` | 2839 | 91627 |
| `templates/psycho-trauma-diagnosis.md` | 2187 | **93814** |

- ★ = **不可拆大块**：`72-source-differences.md` 20768 B、`rules.md` 24410 B、`source-index.md` 16925 B，合计 **62103 B**。三者**整体归属 a2、不拆分、不跨片**；a2 余量 102400 − 93814 = **8586 B**，仍在上限内，故无需为容纳大块再切第三片（附录 F 只列 a1/a2）。
- 注：a2 的 `72-source-differences.md`、`source-index.md`、`version-and-license.md` 属来源类文件，K1 r2 表按 `SOURCE_ONLY` 标记处理（2.8 节「删掉的来源文件不直接恢复」）；**「不可拆」不等于「应恢复」**。
- 不推荐按字节均衡再切（把三个大块拆到两片）：会破坏 v0 skill 谱系边界，且 a2 本身 93814 B 已在上限内，没有再切必要。

### 6.2 Agent 6 四类超 100 KB 的明确建议

判据：**超幅 >10% 按文件再切**（附录 F 硬口径）；**超幅 ≤5% 片数上浮**（§6.1「每片 v0 精读量**约** 100 KB 以内」的「约」字容差，须写明理由并由主代理确认）。

| 片 | 回传体量 | 超幅 | 建议 | 依据 |
|---|---|---|---|---|
| G10 ③ | 119.4 KB | +19.4% | **按文件再切**：③ 拆为 ③a/③b（不拆单文件），G10 片数 3→4 | 附录 F「单个 v0 skill 超过 100 KB 的，按文件再切成 a1、a2……」；19.4% 已超出「约」的容差，不能按上限内例外放行 |
| G01 ③ | 103.9 KB | +3.9% | **片数上浮**：G01 4→5，按文件把超限片拆到新片（不拆单文件） | §6.1 用「约」；≤5% 记为上限内例外，须在分片记录写明超出理由 |
| G03 ② | 104.3 KB | +4.3% | **片数上浮**：G03 4→5，同上 | 同上 |
| G11 两片 | ≈105 KB | +5% | **片数上浮**：G11 3→4（或两片各自按文件再切） | 同上 |

- 兜底：若主代理要求严格 ≤100 KiB（不采「约」），**四类一律改为按文件再切 a1/a2**，不拆单文件。
- 具体文件名与累计字节由 Agent 6 回传，**本台账不编造**；片数上浮改变派发片数，须主代理确认后才生效。

### 6.3 G02 逐卡口径（以 2.3 节原文为准）

- **按 2.3 原文逐卡决定**：逐卡抽出通用机制，与 RO-K001–120 及 RO 规则去重后再决定；恢复部分改写成自创情境、沿用 RO-K121 起编号；纯来源观察（档案取样、章题形式、同一作者作品篇幅差异一类）**不恢复**。
- **不得重复补回**：v3 `02-romance/mechanisms.md` 的 RO-K116–120 已是 v2 RO-K162–166 的通用化改写，46 张删除卡中这 5 张已有落点；**v2 原 116–120 未进 v3**；W3 不得把 46 张整批当待恢复。
- **34/9/3 只是 Agent 5 的只读分类线索，不是配额**；计划 2.3 节未给配额数字，**不预设比例**（误引更正见 §2 ② 与 r2 汇总追加更正）。
- 与 G05 区分：G05 是逐卡压缩、按字段找回，**不套 G02「补回删卡编号」做法**（§2 ③）。
