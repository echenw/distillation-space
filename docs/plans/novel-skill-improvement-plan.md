# 小说 Skill 完善计划（依据 knowledge-compiler，v0–v2 找回 + v3 合规）

- 日期：2026-11-04
- 基线：`main@c734510`
- 状态：待用户确认第 9 节的决策后执行

## 1. 目标

- 以 `skills/knowledge-compiler` 为标准，完善 `skills/` 下 8 个 skill。knowledge-compiler 本身不改。
  - 7 个从 v0–v2 迭代来的 skill：character-and-narrative-control、cross-media-drama-adaptation、fiction-planning-and-diagnosis、genre-fiction-craft、line-editing-and-proofreading、scene-conflict-and-rhythm、story-architecture-and-longform-planning。
  - preset-card-generation：没有历史版本，只做合规和接口两部分。
- 从 v0/v1/v2 找回迭代中丢掉的知识，重点是反例、失败出口、适用条件、模板字段和机制卡。
- 成品满足 knowledge-compiler 对成品 Skill 的要求：R18 §1–4、§2a–2d，R09 §3、§6 的 GQ1–GQ4，R17 §4a，以及 SKILL.md §3。
- 成品不提来源：不出现书名、作者、作品里的人物和情节，也不出现来源编号、年代、篇数和原句。例子一律自创、通用。

## 2. 现状（已核实）

### 2.1 版本

| 版本 | 提交 | 内容 | 体量 |
|---|---|---|---|
| v0 | `d23c461` | 74 个独立 skill，765 个文件 | 约 5.2 MB |
| v1 | `d2003e4` | 合并成 7 个 skill，175 个文件 | 约 1.46 MB |
| v2 | `3c1cb5f` | 7 个 skill，201 个文件 | 约 1.97 MB |
| v3 | `2a10c07` | 7 个 skill，206 个文件 | 约 1.85 MB |
| — | `d57fd12` | 加入 preset-card-generation | — |
| — | `c734510` | 加入 knowledge-compiler | — |

v1→v2 时，english-prose-line-editing 改名为 line-editing-and-proofreading，题材目录从中文名改成英文名。

### 2.2 丢失信号

只统计 7 个 skill。这只是信号，不是证明：v0 本身有重复内容和来源文件。

| 关键词 | v0 | v1 | v2 | v3 |
|---|---|---|---|---|
| 反例 | 1323 | 288 | 187 | 143 |
| 失败 | 851 | 309 | 243 | 226 |
| 不适用 | 570 | 53 | 105 | 103 |
| 依据 | 431 | 250 | 469 | 137 |

### 2.3 已确认的丢失

- **v2→v3 删掉了言情机制卡**：RO-K121–RO-K166 共 46 张，v3 只到 RO-K120。`02-romance/mechanisms.md` 从 40.7 KB 降到 23.6 KB。
  - 抽样结果：多数卡混着具体作品的人名、金额和章题。每张卡里通常有一条能通用的机制，例如“爱与感激不同，对方的付出不构成回应的义务”“注意力在别处会造成非恶意的误解，共享场景可以补上信息”。
  - 也有卡纯属来源观察，例如档案取样、章题形式、同一作者作品的篇幅差异，这类不恢复。
  - 处理方法：逐卡抽出通用机制，和 RO-K001–120 及 RO 规则去重后再决定；恢复的部分改写成自创情境，沿用 RO-K121 起的编号。
- **科幻机制卡缩减**：`05-science-fiction/mechanisms.md` 从 32.4 KB 降到 20.4 KB。
- **SU-02 规则本体被连带删除**：`scene-conflict-and-rhythm/references/intensity-and-rhythm.md` 缩了 57%。SU-02 丢了四样东西：
  - 1–5 的相对强度刻度；
  - “降级只降强度、篇幅、修辞，不降因果必要性、信息量、人物动机”；
  - 反例“削弱前文 ≠ 中段注水”；
  - 检查项“单峰目标只有一个 5 分”。

  这是去来源时把规则本体一起删了。
- **同一模式在其他文件也有**：setup-and-payoff 缩 54%，action-and-fight 缩 28%，line-editing 四个 `en-*.md` 各缩 48–67%，story 的 serial-volume-and-closure 缩 39%。
- **v0 专门文件在 v3 没有对应**：v0 有 9 份 `failure-modes.md`、9 份 `counterexamples.md`、2 份 `anti-examples.md`、35 个模板（如 series-volume-dependency、revenge-closure、adventure-diagnosis、revision-check）。v3 没有对应的专门文件，覆盖情况待盘点。
- **编号消失不等于丢失**：AC-01–18 改成了 A1–C3，SV-T 改成了 SD-T，PD/PT 改成了 PS/PV。所以盘点要比内容，不能只比编号。
  - genre 在 v1→v2 统一了题材前缀：IDP 改成 IR（已核实 IR-01 的标题就是原来 IDP-01 的“身份主张、认定与资格”），COM 改成 CO，RM/RD 改成 RL。
  - P1 用“新旧前缀对照 + 标题”来对齐这些编号。

### 2.4 11-02 审计线索

线索来自 `~/knowledge-distillation-workspace/results/notes/three-version-audit-20261102.md`，只当线索，不当证据。下表是按 v3 逐项核对的结果：

| 项 | v3 状态 |
|---|---|
| F-2 planning.md 标号误伤 | 已修 |
| S-3 载体五项检查 | 已补回：`serial-chapters-and-installments.md` 第 58–64 行的 SV-16 载体审计表有五项（载体身份、正文边界、非正文栏目、发行提示、回溯入口）；P1 只核对模板里有没有对应的填写行 |
| F-1 定位卡没有定义 | 仍缺 |
| S-1 结构审查十一项及三条细则 | 仍缺 |
| S-2 单条反馈的“可核错误”例外 | 部分补回：`serial-production.md:60` 已放宽为“是否需要第二个同向信号取决于风险和合同”，但没写明“设定矛盾、时间线错误这类可核错误，不必等第二个信号” |
| S-4 层级依赖表等专表 | 仍缺 |
| S-5 细节四条 | 只取通用部分 |
| C-1 视角方案卡缺提示行 | 部分缺：`templates/narrative-workbook.md` §1 现有 8 行，已有“能不能知道”；缺“重心类型”“放弃的候选及损失”“能进谁的意识”“主视点理由” |
| C-2 三项回归问题 | 仍缺 |
| C-3 逐项失败检查 | 仍缺 |
| C-4 F6 误用条目 | 仍缺 |
| R-1 SU-19 审计表缺“象征”行 | 仍缺：`rhythm-diagnosis.md` §3 已改成按单元填写的 7 列表，没有“意象或物件在收束处出现一次”这一检查；补法改为加一列或在表下加一条检查 |
| L-1 负触发完整示例 | 仍缺 |
| L-2 EN-27 示范例 | 仍缺（改用自创例子） |
| X-1–X-7 改编细则 | X-1–X-6 在 v3 均未见：grep“交给导演 / 布景细节”“线条 / 交点”“灵感 / 均衡”“字幕 + 戏剧价值”“缓流”“第二次通读”都没有对应句；X-7 是个案，只取通用判语 |

### 2.5 来源残留

| 位置 | 残留 |
|---|---|
| fiction-planning `references/rules-drafting.md`、`rules-premise-and-structure.md`、`rules-revision-and-method.md` 第 8 行 | 都写着“28 本材料标称 1808–1929 年……” |
| fiction-planning `rules-drafting.md` 第 43、79、107、114、144 行 | 来源编号残片 `-14243`、`-8269`、`-2110`、`-4841`、`-3790` |
| fiction-planning `scope-and-conflicts.md` 第 74–76 行 | 残片 `-2236`、`-2111`，以及“1890 年代英国市场”“1911 年前的手册” |
| fiction-planning `rules-revision-and-method.md:148`、`self-check-modern-and-zh.md:32` | 来源年代（“1920 年代美国杂志市场”“1884 年的出版建议”） |
| genre `12-children-youth/more-examples.md:22` | 一部真实儿童书的情节元素 |
| character `references/boundaries-and-ethics.md:73` | “书里明写……” |
| genre `11-identity-revenge-intrigue/stance-and-boundaries.md` IR-05D | 疑似：“节本、翻译、未完稿……须绑定实际版本”“引文位置不可核时，就缩小主张”。像是在讲学习材料的版本和引文，正则查不出来。P4 判断：如果指学习材料，就改写成针对用户自己资料的说法，或者删掉 |

### 2.6 合同与接口缺口

- **审计词**：cross-media 的 `interactive-adaptation.md:55` 和 `templates/interactive-branch-sheet.md:41`、fiction-planning 的 `references/diagnosis.md:411`，运行文本里有 `NOT_PROVEN` 等审计词。
- **preset-card-generation**：
  - 没有 `agents/openai.yaml`，没有负触发和转介，SKILL.md 没有失败出口；
  - “规划、写章节、改稿去 AI 味、审阅章节”这几条路由，和 fiction-planning、story-architecture、line-editing 重叠；
  - 另外 7 个 skill 都没提到它。
- **cross-media**：description 一个兄弟 skill 都没提，SKILL.md 没有失败出口。
- **路由表**：8 个 SKILL.md 的路由表都没有 R18 §3 建议的“需要时补读 / 缺料或冲突时的出口”两列。

### 2.7 v0 专门文件（P1 逐个核对 v3 是否覆盖）

反例、失败模式、反面示例文件（11 个 skill）：

| v0 skill | 文件 | v3 落点 |
|---|---|---|
| historical-alt-history-craft | counterexamples、failure-modes | genre 06 |
| historical-fiction-plot-forge | anti-examples、failure-modes | genre 06 |
| horror-thriller-craft-b04 | counterexamples、failure-modes | genre 03 |
| mystery-detective-plot-forge | counterexamples、failure-modes | genre 01 |
| profession-competition-craft | counterexamples | genre 10 |
| romance-craft-b06 | counterexamples、failure-modes | genre 02 |
| sci-fi-future-plot-forge | anti-examples、failure-modes | genre 05 |
| science-fiction-craft-b04 | counterexamples、failure-modes | genre 05 |
| speculative-wuxia-fantasy-craft | counterexamples、failure-modes | genre 04 |
| vocation-proof-and-price | counterexamples | genre 10 |
| wuxia-xianxia-plot-forge | counterexamples、failure-modes | genre 04 |

模板（35 个，按 v0 skill 列出）：

| v0 skill | 模板 | v3 落点 |
|---|---|---|
| action-fight-scene-craft | action-checklist | scene（已改号保留） |
| adventure-treasure-craft-b02 / -b03 | adventure-diagnosis、expedition-designer | genre 08 |
| character-psychology-trauma-craft | character-state-card、revision-check | character |
| children-ya-craft-b05 | child-diagnosis、child-story-designer | genre 12 |
| childrens-youth-fiction-craft-b01 | diagnosis-card | genre 12 |
| fiction-craft | diagnosis-report、novel-plan、revision-sheet、scene-plan | fiction-planning（同名保留） |
| historical-fiction-craft-b03 | historical-diagnosis、history-fiction-ratio、real-figure-audit | genre 06 |
| historical-immersion-and-stakes | historical-causality | genre 06 |
| horror-gothic-suspense-b05 | dread-scene-planner、haunting-designer、manuscript-diagnosis | genre 03 |
| identity-revenge-intrigue-b06 | identity-stakes-map | genre 11 |
| intrigue-revenge-craft-b04 | intrigue-diagnosis | genre 11 |
| plot-architecture | diagnosis-report、plot-canvas、scene-table | story（plot-canvas、plot-scene-table 保留） |
| psycho-trauma-craft-b10 | psycho-trauma-designer、psycho-trauma-diagnosis | character |
| realism-craft-b09 | realism-designer、realism-diagnosis | genre 14 |
| revenge-identity-craft | identity-causal-chain、revenge-closure | genre 11 |
| revenge-intrigue-architecture | intrigue-seven-tables | genre 11 |
| serialized-volume-planning | series-volume-dependency | story（对应审计 S-4，v3 缺） |
| supernatural-power-craft | diagnosis-report、power-system-canvas | genre 04 |
| wuxia-fantasy-power-arc | power-arc-state | genre 04 |

“v3 落点”一列只是按目录名初分。字段是否还在、是否逐项可填，由 P1 逐个比对，结果记进 loss-inventory。

### 2.8 genre 各题材的版本体量（11-02 审计没覆盖 genre）

| 题材 | v1 | v2 | v3 | v2→v3 主要变化 |
|---|---|---|---|---|
| 01 推理 | 56k | 56k | 58k | — |
| 02 言情 | 98k | 120k | 109k | mechanisms.md −17 KB（RO-K121–166） |
| 03 恐怖 | 77k | 77k | 73k | templates-and-cases −5.7 KB，mechanism-and-causality −2.3 KB |
| 04 武侠仙侠玄幻 | 77k | 107k | 110k | — |
| 05 科幻 | 72k | 94k | 83k | mechanisms.md −12 KB |
| 06 历史架空 | 103k | 104k | 81k | 删 source-cases.md（32.6 KB）；relationships-and-belief −4.5、institutions-and-documents −3.6、livelihood-and-action −3.4、history-contract −2.4、narration-and-period −2.0 KB |
| 07 求生灾变 | 27k | 28k | 28k | — |
| 08 探险寻宝 | 36k | 38k | 37k | — |
| 09 喜剧 | 39k | 39k | 37k | 删 sources-and-editions.md（11.4 KB） |
| 10 职业竞技 | 47k | 47k | 35k | case-notes −6.8 KB，worksheets-and-cases −5.5 KB |
| 11 身份复仇权谋 | 65k | 65k | 57k | 删 sources-and-editions.md（23.7 KB） |
| 12 儿童青少年 | 28k | 29k | 29k | — |
| 13 异世界穿越 | 24k | 24k | 25k | — |
| 14 年代现实 | 30k | 31k | 29k | sources-and-boundaries −1.7 KB |

- **删掉的来源文件不直接恢复**：v3 删掉 source-cases、sources-and-editions 这类文件是对的。但 P1 要读一遍，挑出其中的手法和案例分析（不是书目和版本信息）：后文其他文件没覆盖的，改写成通用机制或自创例子；只是书目的，记“不恢复”。
- **v1→v2 的题材差异另行盘点**：v1→v2 时题材目录改了英文名，文件也重组了，没有办法按文件名对齐，P1 用规则编号和标题来对齐。已知其中一部分编号消失是改号，例如 SV-T 改成了 SD-T。

## 3. 范围

### 在范围内
- 8 个 skill 的内容找回、去来源、合同补全和接口统一。
- knowledge-compiler 要求的工作区记录。

### 不在范围内
- 修改 knowledge-compiler。
- 新增材料里没有的知识（自创例子和经 D5 采纳的附录 H 建议除外）。
- 改 skill 名称或目录名。
- 新增自动化脚本。
- 未经授权的测试、真实任务运行、commit 和 push。

## 4. 工作区

按 knowledge-compiler §1 的结构，放在仓库根目录 `distillation/`：

```
distillation/
├── requirements.md                     总需求（本计划确认后写入）
├── materials/2026-11-04-history/
│   └── manifest.yaml                   v0–v3 提交 SHA、路径、规模；不复制原件
└── rounds/round-01-2026-11-04/
    ├── checklist.md
    ├── log.md
    ├── inputs/{manifest.yaml, requirements.md}
    ├── notes/
    │   ├── lineage-map.md              v0 74 个 → v3 7 个 + 14 类题材
    │   ├── loss-inventory/<skill>.md   丢失候选与逐条决定
    │   ├── source-synthesis/<skill>.md R17 §4a 决策链及成品落点
    │   ├── desourcing-ledger.md        逐文件去来源回读记录
    │   ├── delivery-preflight-spec/    有枚举模板的 skill 各一份
    │   └── quality/<skill>/{brief.json, review.json}
    └── output/<8 个 skill>/
```

- 来源信息只放在 `notes/`。
- 不另建 `distillation/results/`，当前成果只认仓库里的 `skills/`。

## 5. 谱系初分（P1 核定）

| v3 | v0 来源 skill |
|---|---|
| character-and-narrative-control | narrative-pov-information-control、nonlinear-time-craft、character-psychology-trauma-craft、psycho-trauma-craft-b10 |
| cross-media-drama-adaptation | cross-media-drama-transfer |
| fiction-planning-and-diagnosis | fiction-craft、fiction-craft-and-language、reader-experience-and-critique、research-fact-verification |
| line-editing-and-proofreading | style-refinement-and-proofreading |
| scene-conflict-and-rhythm | foreshadowing-and-rhythm、scene-chapter-design-lab、action-fight-scene-craft |
| story-architecture-and-longform-planning | plot-architecture、serialized-volume-planning |
| genre 01 推理 | crime-mystery-craft-b03、mystery-clue-fairplay、mystery-detection-craft-b04、mystery-detective-plot-forge、mystery-evidence-chain-designer |
| genre 02 言情 | courtship-conflict-craft、romance-craft-b03-b07、romance-craft-b06、romance-emotional-arc、romance-obstacle-and-cost、romance-obstacle-delay-craft、romance-social-cost-craft |
| genre 03 恐怖 | gothic-weird-horror-craft、horror-dread-and-revelation、horror-gothic-suspense-b05、horror-supernatural-craft、horror-thriller-craft-b04 |
| genre 04 武侠仙侠玄幻 | speculative-wuxia-fantasy-craft、wuxia-fantasy-power-arc、wuxia-xianxia-plot-forge、fantasy-adventure-structure-lab（部分进 08，待核）、supernatural-power-craft（部分进 03，待核） |
| genre 05 科幻 | sci-fi-future-plot-forge、sci-fi-novum-world-forge、science-fiction-conceptual-reveal、science-fiction-craft-b04、scifi-future-craft-b03 |
| genre 06 历史架空 | historical-alt-history-craft、historical-contract-and-legitimacy-craft、historical-fiction-craft-b03、historical-fiction-plot-forge、historical-fiction-power-machine、historical-immersion-and-stakes |
| genre 07 求生灾变 | castaway-salvage-stronghold、survival-crisis-escalation、wilderness-disaster-survival-craft-b01 |
| genre 08 探险寻宝 | adventure-treasure-craft、adventure-treasure-craft-b02、adventure-treasure-craft-b03 |
| genre 09 喜剧 | comedy-beat-craft、comedy-scene-mechanics、comic-engine-craft、comic-fiction-diagnosis |
| genre 10 职业竞技 | competition-underdog-arc、profession-competition-craft、vocation-proof-and-price |
| genre 11 身份复仇权谋 | identity-revenge-intrigue-b06、identity-revenge-powercraft-fiction、intrigue-revenge-craft-b04、revenge-identity-craft、revenge-intrigue-architecture、revenge-intrigue-craft |
| genre 12 儿童青少年 | child-story-craft、children-ya-craft-b05、childrens-youth-fiction-craft-b01 |
| genre 13 异世界穿越 | isekai-crossworld-craft、isekai-crossworld-craft-b01、isekai-crossworld-craft-b02 |
| genre 14 年代现实 | realism-craft-b09 |

74 个 v0 skill 都已分配，没有重复分配。

### 5.1 体量（决定精读的先后和分片大小）

| v3 目标 | v0 来源数 | v0 体量 | v3 体量 | v3 / v0 |
|---|---|---|---|---|
| character | 4 | 242 KB | 164 KB | 68% |
| cross-media | 1 | 53 KB | 61 KB | 115% |
| fiction-planning | 4 | 422 KB | 328 KB | 78% |
| line-editing | 1 | 91 KB | 64 KB | 70% |
| scene | 3 | 168 KB | 122 KB | 73% |
| story | 2 | 391 KB | 256 KB | 65% |
| genre 01 推理 | 5 | 338 KB | 58 KB | 17% |
| genre 02 言情 | 7 | 334 KB | 109 KB | 33% |
| genre 03 恐怖 | 5 | 368 KB | 73 KB | 20% |
| genre 04 武侠仙侠玄幻 | 5 | 439 KB | 110 KB | 25% |
| genre 05 科幻 | 5 | 343 KB | 83 KB | 24% |
| genre 06 历史架空 | 6 | 402 KB | 81 KB | 20% |
| genre 07 求生灾变 | 3 | 225 KB | 28 KB | 12% |
| genre 08 探险寻宝 | 3 | 165 KB | 37 KB | 22% |
| genre 09 喜剧 | 4 | 193 KB | 37 KB | 19% |
| genre 10 职业竞技 | 3 | 293 KB | 35 KB | 12% |
| genre 11 身份复仇权谋 | 6 | 297 KB | 57 KB | 19% |
| genre 12 儿童青少年 | 3 | 121 KB | 29 KB | 24% |
| genre 13 异世界穿越 | 3 | 116 KB | 25 KB | 22% |
| genre 14 年代现实 | 1 | 35 KB | 29 KB | 83% |

- **事实**：14 类题材从 v0 到 v3 保留了 12%–33%（年代现实除外），非题材 skill 保留了 65%–115%。v0 的数字包含来源索引、重复的同题材 skill 和英文原句，所以比例低不等于丢失多。
- **推断**：求生灾变（12%）、职业竞技（12%）、推理（17%）压缩最狠，单位体量的丢失风险最高。P1 机械盘点时，这三类的阈值收紧到“缩减超过 20% 的规则小块全部列入”。
- **分片**：每片的 v0 精读量控制在约 100 KB 以内。超过 300 KB 的谱系组（fiction-planning、story，以及 genre 01–06、10）按 v0 skill 再切片，每片做完就更新 log.md 和 loss-inventory，保证随时停下都能接着做。

## 6. 阶段

### P0 建需求（knowledge-compiler 第 1–2 步）
- 写 `requirements.md` 和本轮 `checklist.md`，内容是本计划的目标、范围、验收和授权。
- 冻结 `inputs/requirements.md` 和 `inputs/manifest.yaml`，在 checklist 里记下 SHA-256。
- **出口**：checklist 状态为“进行中”，输入能核对。

### P1 谱系与丢失清单（覆盖 7 个 skill）
1. **机械盘点**：在 scratchpad 用只读脚本完成，不需要精读。比对 v0/v1/v2/v3 的文件、标题、规则编号、规则小块（规则 / 怎么做 / 例外 / 反例 / 检查 / 适用 / 失败）和模板行。缩减超过 30% 或超过 1.5 KB 的文件全部列入。
2. **定向精读**：只读机械盘点标出来的段落，并和 v3 的对应位置比较。
3. **逐条决定**：每条候选给一个决定，写明丢失类型、v3 落点（文件 + 规则编号）和理由。
   - 恢复（通用改写）
   - 合并到现有规则
   - 不恢复（写理由）
   - 待核
4. **以下情况不算丢失，不恢复**：
   - 后版有意的口径调整（审计 §三：story 8 处口径反转、scene SU-07 放宽、character 去数值化、fiction 硬口径）；
   - 后版已改正的事实错误（审计 §四）；
   - 只属于某一部作品的情节和史实。
- **出口**：7 份 loss-inventory 覆盖第 5 节全部 v0 skill，第 2 节列出的项都有决定。

### P2 套件合同
- **Owner 与转介矩阵**：8 个 skill 谁负责什么、相近请求转给谁。preset-card 的边界按 D2 定。
- **description 与转介**：description 写全相关兄弟 skill 名，“适用与转介”节要包含 preset-card-generation。
- **交付状态词**：统一用“已完成 / 依据 / 未能核实 / 待作者决定”，替换运行文本里的 NOT_PROVEN、VERIFIED 等审计词。
- **去来源检查清单**（R18 §2b）：
  - 书名号作品名、作者和人名；
  - 来源编号，包括 `-NNNN` 这类残片；
  - 来源的年代和篇数；
  - “原文 / 书内 / 同书 / 书里 / 来源是 / 材料标称”这类说法；
  - 包外路径；
  - “旧版 / 本版 / 更正”这类改动痕迹；
  - 删除来源后留下的空括号和悬空的“见 / 据”。
- **模板规范**（R18 §2a）：每个编号占一行，列为“值 / 状态 / 稿件证据位置”，允许填“未知”。
- **措辞**：不出现分档词，不写“硬规则”“用户明确要求”“融合版”。

### P3 逐个 skill 返工

每个 skill 都要完成五件事：
1. 按 loss-inventory 找回丢失项，用通用写法和自创例子；
2. 去来源；
3. SKILL.md 写清触发、负触发和转介，路由表加“补读 / 出口”两列，补上失败出口；
4. 复杂操作补到 R18 §2d 的深度：判断标准、步骤、诊断到修订的闭环、一个自创难例（含 A/B 分支和失败出口）、负面回归；
5. 写 R17 §4a 决策链并标出成品落点。

先用最小的一个校准方法，顺序如下：

1. **line-editing-and-proofreading**
   - 补回四个 `en-*.md` 的规则和区分条件；固定冗语对照表换成自创例子。
   - L-1：补完整的“先判负触发”示例。
   - L-2：EN-27 补自创示范，并注明“具体化不能补写事实”。
2. **cross-media-drama-adaptation**
   - 补 description、兄弟转介和失败出口（缺原作文本、媒介不明、规则冲突），替换审计词。
   - X-1–X-6 按通用规则评估；X-7 只留通用判语，不留个案。
   - 检查 v3 新增的互动改编部分（AD-35–40）。
3. **scene-conflict-and-rhythm**
   - 补回 SU-02 等规则缩掉的区分条件、反例和检查项（intensity、setup-and-payoff、action-and-fight、suspense-and-reveal、rhythm-diagnosis、scope-and-conflicts）。
   - R-1：补“象征”一行。
4. **character-and-narrative-control**
   - C-1：工作表加提示行（重心类型、放弃的候选及损失、不能知道、能进谁的意识、主视点理由）。
   - C-2：三项回归问题及附带核查并入诊断 §9。
   - C-3：逐项失败检查，重点是结局范围和关系变化两项。
   - C-4：补 F6 一行。
   - 改写“书里明写”；对照 v0 创伤类内容补边界。
5. **story-architecture-and-longform-planning**
   - S-1：结构审查十一项和三条细则，改写成通用清单，不带人名。
   - S-2：补“可核错误”例外。
   - S-3：补齐余项和模板表。
   - S-4：补层级依赖表等专表，可参考 v0 的 series-volume-dependency 模板。
   - S-5：只取通用部分（口气长度的限定、暴力桥接的几种方式）。
   - 检查 serial-* 系列文件的缩减。
6. **fiction-planning-and-diagnosis**
   - 清掉 2.5 节列的全部残留，改写成不借来源的适用限制。
   - F-1：补定位卡五项字段（契约两行、道德立场、事实契约、主要人物三场景预测、待作者决定事项）。
   - 检查 v2→v3 缩减的 rules-* 和 examples 文件。
7. **preset-card-generation**
   - 补 `agents/openai.yaml`，设 `allow_implicit_invocation: false`。
   - 按 D2 补负触发和转介。
   - 补失败出口，以及卡片版本和锁定内容冲突时的出口（R18 §2d 最后一段）。
   - 保留“冒号后不反转”和“示例原创”两条规则。
8. **genre-fiction-craft**：按题材分 14 片。
   - 先做武侠仙侠玄幻、言情（RO-K121–166）、科幻（机制卡）。
   - 然后依次做历史、身份复仇、恐怖、推理、职业，最后是其余题材。
   - 对照 v0 的 failure-modes、counterexamples、anti-examples 和专用模板补齐。
   - 替换儿童书情节元素。
   - 最后整理 SKILL.md 路由和混合题材一节。

### P4 全套隔离回读
- 只拿成品包逐文件回读，确认没有来源、作品、作者、包外路径和改动痕迹，记在 `desourcing-ledger.md`。
- 把自创例子和 v0 的来源案例比情节骨架（人物关系 + 关键事件 + 设定），像的就重写。
- 核对跨 skill 接口（GQ3）和相对链接。

### P5 质量门禁与交付（第 5 步）
- 每个 skill 写 `brief.json`（正常、缺料、冲突、边界四类用例）和 `review.json`。
- GQ1–GQ4 给出状态和证据。没有真实任务测试时，GQ5 记 NOT_PROVEN。
- 冻结 `output/`，记录整树 SHA。
- 按 D1 应用到 `skills/`。
- checklist 改为“状态：已完成 / 验收范围：静态交付”，log 写明验收依据。

## 7. 验收

1. **丢失清单完整**：覆盖全部 74 个 v0 skill，以及 v1→v2、v2→v3 的删除和缩减；第 2 节列出的项（含 RO-K121–166 和审计线索）逐条有决定。
2. **找回的内容用得到**：每条“恢复 / 合并”在成品里有落点，而且这个文件能从 SKILL.md 的路由表到达。
3. **成品自足**：8 个 skill 逐文件回读有记录；正则扫描零命中，或每个命中都写明不是来源（例如用户稿件里的“原文”）；2.5 节列的残留全部消失。
4. **行为合同齐全**：每个 SKILL.md 有触发、负触发和兄弟转介，有含“补读 / 出口”两列的路由表，主要操作有失败出口；R18 §4 六问逐个 skill 记在 notes。
5. **模板可逐项填写**：有枚举编号的模板每个编号一行，并有对应的 preflight spec。
6. **复杂操作有深度**：规划、写作、改稿、审稿、卡片生成 / 诊断 / 修订，各自具备判断标准、步骤、诊断到修订的闭环和自创难例。
7. **不回退**：v3 的规则编号、路由和 skill 名都保留；删除或改号都有记录；相对链接全部能解析。
8. **质量记录齐全**：brief、review 和 GQ 状态齐全；`output/` 冻结 SHA 与 checklist 一致。
9. **knowledge-compiler 不变**：字节与 `c734510` 相同。

## 8. 不许做

- 不改 `skills/knowledge-compiler/`。
- 不恢复出处、书名、作者、作品的人物 / 情节 / 设定、原句、来源数量和年代。
- 不把有意的口径调整和已改正的错误当成“丢失”恢复回来。
- 不为凑深度编造阈值、数字或成体系的反例；材料没有依据的地方写明“没有依据，按作者判断”。
- 不在没有决定记录的情况下删除 v3 内容。
- 未经授权，不运行 kd_* 脚本和真实任务，不 commit，不 push。

## 9. 待确认的决策

| # | 决策 | 选项 | 建议 |
|---|---|---|---|
| D1 | 工作区与落地 | A：`distillation/` 工作区，冻结后应用到 `skills/`，不建 results/ 副本<br>B：只产出 `output/`，暂不动 `skills/`<br>C：不建工作区，直接改 `skills/` | A |
| D2 | preset-card-generation 边界 | A：保留它的“推进 / 文风 / 表达”三轴全流程，但只负责预设卡和三轴诊断；一般性的规划、结构和精修转给兄弟 skill，兄弟 skill 遇到卡片请求转给它<br>B：收窄为只做卡片 | A |
| D3 | 验证授权 | A：只做静态检查（默认）<br>B：加跑 knowledge-compiler 的只读检查脚本（kd_material_quality、kd_delivery_preflight、kd_artifact_quality、kd_round_output、kd_workspace_audit）<br>C：在 B 的基础上，每个 skill 派一个只读审查子代理，只看成品包，做隔离回读和 GQ1–GQ4<br>D：再加真实任务测试（GQ5） | C |
| D5 | 附录 H 的写作建议是否纳入本轮 | A：纳入。与材料规则同义的合并进现有规则并补条件，材料没有的作为新规则写入；与材料冲突的列给你裁决<br>B：只纳入与材料一致的部分<br>C：不纳入，留到下一轮 | A |
| D4 | genre 覆盖深度 | A：14 类全部机械盘点 + 定向精读，热门三类与 v0 全文对照<br>B：只看 v1→v3 的差异<br>C：14 类全部与 v0 全文对照 | A |

`distillation/` 工作区要不要提交进仓库，到提交时另行决定。仓库是公开的，notes 里会有来源记录。

## 10. 验证策略

| 层级 | 内容 | 授权 |
|---|---|---|
| 静态 | git diff、grep、统计脚本（放在 scratchpad，只读）；人工回读，记录在 notes | 默认已有 |
| 只读检查脚本 | 只读 kd_* 检查器，保留原始输出和退出码 | D3-B |
| 独立审查 | 审查者独立于作者，只读成品包，不看 notes | D3-C |
| 真实任务 | 同一份最终版，跑四类用例 | D3-D |

不同层级之间不能互相代替：静态通过，不等于效果已经证明。

## 11. 风险

| 风险 | 应对 |
|---|---|
| v0 体量大（5.2 MB），上下文装不下 | 先机械盘点，再定向精读；按 skill 和题材分片；log.md 随时记下断点 |
| 恢复了错误或来源专属内容 | 恢复前先对照后版的改正和有意调整 |
| 恢复太多导致 skill 臃肿 | 只恢复能增加区分条件、反例、失败出口或模板字段的内容，优先合并而不是追加 |
| 自创例子其实是改头换面的原作 | P4 做情节骨架比对 |
| 去来源时再次误删知识 | 规则先改写再删出处，删除后通读改过的句子 |
| preset-card 与兄弟 skill 误触发 | 按 D2 建双向转介 |
| 作者自审不独立 | D3-C |

## 附录 A：P1 盘点与记录格式

### A.1 机械盘点的输出

只读脚本放在 scratchpad，用 `git show <提交>:<路径>` 读取各版本，不检出、不改仓库。每个谱系组输出一份表：

| 字段 | 含义 |
|---|---|
| unit_id | 盘点单位：规则编号；没有编号的用“文件路径 + 标题” |
| versions | 在 v0 / v1 / v2 / v3 中出现与否（例：`1 1 1 0`） |
| blocks | 各版本这个单位里含有的小块：规则 / 怎么做 / 例外 / 反例 / 检查 / 适用 / 失败 |
| bytes | 各版本这个单位的字节数 |
| flag | 标记原因：`MISSING`（v3 没有）、`SHRUNK`（缩减超过阈值）、`BLOCK_LOST`（某类小块在 v3 消失）、`RENUMBERED?`（编号消失但 v3 有相似标题） |

阈值：默认缩减超过 30% 或超过 1.5 KB；求生灾变、职业竞技、推理三类收紧到 20%。

### A.2 loss-inventory 的每条记录

每条记录是一行表格，列如下：

| 列 | 写法 |
|---|---|
| 编号 | `LI-<skill 缩写>-NNN`，例如 `LI-SC-001` |
| 来源位置 | 版本 + 路径 + 规则编号或标题（只在 notes 中出现） |
| 丢失类型 | 整条规则 / 规则小块（写明哪类）/ 模板字段 / 例子 / 整个文件 |
| v3 现状 | 没有 / 部分（写明在哪）/ 改号后保留（写新编号） |
| 决定 | 恢复 / 合并 / 不恢复 / 待核 |
| 理由 | 不恢复时写清楚：重复、只属于某部作品、后版有意调整、后版已改正、与现规则冲突 |
| 成品落点 | 文件 + 规则编号（恢复和合并必填） |
| 状态 | 未处理 / 已写入 output / 已回读 |

### A.3 断点续做

- 每处理完一片，就在 `log.md` 追加一行：时间、片名、处理到的编号、下一步。
- 任何时候中断，下一次从 log.md 最后一行接着做，不重新盘点已经完成的片。
- 机械盘点结果放在 `notes/loss-inventory/raw/`，只追加不覆盖。重新生成时另起文件名，带日期。

## 附录 B：去来源扫描清单（P3 每个 skill 收尾、P4 全套各跑一次）

本机的 `grep` 实际是 ugrep，遇到中文长模式会报“exceeds complexity limits”。所以统一用 `/usr/bin/grep -rnE`，范围排除 `knowledge-compiler/`。

### B.1 正则（命中就逐条判断）

| # | 目标 | 模式 |
|---|---|---|
| 1 | 书名号里的作品名 | `《[^》]+》`（例外：zh-mechanics 讲标点用法时列举的“《》”符号本身） |
| 2 | 来源编号和残片 | `PG[ -]?[0-9]+`、`(^\|[^A-Za-z0-9])-[0-9]{3,5}([^0-9]\|$)` |
| 3 | 来源的数量和年代 | `[0-9]+ ?本(材料\|书\|手册)`、`材料标称`、`(1[5-9]\|20)[0-9]{2} ?年(代)?.{0,8}(市场\|手册\|杂志\|出版\|建议)` |
| 4 | 指向学习材料的说法 | `书内\|书里\|同书\|该书\|此书\|原书\|来源是\|出自\|引自\|据称\|这批材料\|学习材料\|原文库\|批次` |
| 5 | 作者、作家和名人 | `作家\|小说家\|评论家\|大师\|名著\|经典作品`，以及拉丁字母人名（`[A-Z][a-z]+ [A-Z][a-z]+`） |
| 6 | 英文原句 | `"[A-Z][a-z]+( [a-z]+){4,}` |
| 7 | 包外路径 | `notes/\|results/\|/home/\|materials/\|rounds/` |
| 8 | 改动痕迹 | `旧版\|本版\|更正\|早先的版本\|融合版\|上一版` |
| 9 | 审计词 | `NOT_PROVEN\|VERIFIED\|NOT_RUN\|STATIC_CHECKED\|DESIGN_EXAMPLE\|OBSERVED\|F/H/P\|GQ[1-5]\|R1[78]` |
| 10 | 删除后的残迹 | `（\s*）\|\(\s*\)\|见\s*[，。；]\|据\s*[，。；]\|与\s*同` |
| 11 | 分档词和禁用说法 | `夯\|拉完了\|硬规则\|用户明确要求` |

### B.2 允许保留的情形（命中后在 desourcing-ledger 里写明理由）

- **用户自己的稿件**：“原文”“原稿”指用户正在改的稿子；改编 skill 里的“原作”指用户要改编的作品；同人或穿书语境里的“原著”指用户选定的底本。
- **用户稿件的版本号**：`v1→v2`、`draft-v3`、`serial-v2-outline` 这类。
- **本包内部编号**：规则编号（SU-02、RO-K001 等）和修改级别（L0–L4）。
- **自创例子里的年份**：例如“1910 年的小镇”这类虚构设定。但要过 B.3 的骨架比对。
- **事实核验场景**：讲事实核验方法时出现的“来源”“出处”“引语”，指的是用户要核验的资料。

### B.3 正则查不出的情形（逐文件回读时判断）

- **例子与 v0 来源案例的情节骨架相近**：人物关系、关键事件、时代地点三项有两项以上对得上，就重写。
- **具体作品的标志性情节元素**：没有书名也算违规，例如 2.5 节列的儿童书元素。
- **借来源背书的说法**：例如“经典做法是……”“很多名作都……”，改成直接写适用条件和限制。
- **删除来源后语义不通**：主语悬空、只剩半句、表格空列。

## 附录 C：Owner 与转介矩阵草案（P2 定稿，preset-card 一行取决于 D2）

### C.1 各 skill 负责什么

依据是各 skill 现有的 description。

| skill | 负责 | 不负责（转给） |
|---|---|---|
| fiction-planning-and-diagnosis | 总流程：定篇幅、媒介、类型和交付；新作规划的入口；成稿诊断、修订删减、成稿自检；现实断言的事实核验；读者反馈 | 结构骨架和分卷（story）、视角和信息（character）、单场设计（scene）、句子精修（line-editing）、题材规则（genre）、预设卡（preset-card） |
| story-architecture-and-longform-planning | 单本结构（主行动、终点、高潮、因果、多线、结尾）；长篇分卷、卷末收与接、跨卷伏笔账、连载排产 | 场内节奏（scene）、视角（character）、总流程和赛道（fiction-planning） |
| character-and-narrative-control | 视角合同、叙述距离、信息控制、证词与自辩、心理落到动作上、场景与概述、非线性时间 | 场景冲突和强度（scene）、卷级结构（story） |
| scene-conflict-and-rhythm | 场景单位、知情与空间、伏笔兑现、悬念、强度与节奏、章末钩子、动作打斗 | 卷级节奏（story）、视角（character）、句子精修（line-editing） |
| line-editing-and-proofreading | 中英文句子级精修、校对、体例、句子层的 AI 腔 | 结构和场景问题（转对应 skill）、预设卡里的表达约束（preset-card） |
| genre-fiction-craft | 14 类题材特有的规则、机制、反例和题材混合 | 不分题材的通用手法（转对应的通用 skill） |
| cross-media-drama-adaptation | 改编为舞台、影视、音频和互动形式 | 小说本身的创作（转对应 skill） |
| preset-card-generation（D2-A） | 预设卡（推进模式卡、文风卡、表达约束卡）的生成、诊断、审校、修订；用“推进 / 文风 / 表达”三轴给章节做诊断 | 不写成卡、也不用三轴的一般规划、结构、精修和题材问题（转对应 skill） |

### C.2 重叠请求怎么分

| 用户请求 | 归属 | 判断依据 |
|---|---|---|
| “帮我规划一本书” | fiction-planning 做入口，结构部分交给 story | 要定赛道和交付的，从 fiction-planning 进 |
| “规划一卷 / 排章纲” | story；要写成推进卡给模型用时，交给 preset-card | 产物是规划文档，还是给模型的卡 |
| “去 AI 味” | 改具体稿子交给 line-editing；写成反 AI 味的约束卡交给 preset-card | 产物是改好的文本，还是卡片 |
| “写这一章” | fiction-planning 的起草流程，场景细节交给 scene；用户已有文风卡或推进卡时交给 preset-card | 有没有卡作为输入 |
| “审这一章” | fiction-planning 的诊断；用户指定按三轴审时交给 preset-card | 审查框架 |
| “这一章节奏拖” | 单元内的问题交给 scene，跨章跨卷的问题交给 story | 问题的尺度 |
| “武侠打斗写不好” | 题材约束看 genre 04，动作写法看 scene | 先用题材约束，再用通用手法 |

### C.3 落地要求

- 每个 SKILL.md 的“适用与转介”节都写出 C.2 中与自己相关的行。
- description 写全会转去的兄弟 skill 名。
- GQ3 核对双向引用：A 说转给 B 的地方，B 都要说接收什么。

## 附录 D：requirements.md 草稿（对应 knowledge-compiler 第 1 步的七问）

| 问 | 本项目的回答 |
|---|---|
| ① 学习目标 | 找回 v0–v2 迭代中丢掉的写作知识，并使 8 个小说 skill 满足 knowledge-compiler 的成品要求 |
| ② 产物与位置 | 8 个完整 Skill（名称不变）。工作稿在 `distillation/rounds/round-01-2026-11-04/output/`，冻结后按 D1 应用到 `skills/`。不建 `distillation/results/` |
| ③ 材料、限制、隐私 | 材料是 git 提交 v0 `d23c461`、v1 `d2003e4`、v2 `3c1cb5f`（只读）；基线是 v3 `2a10c07` 和 preset-card `d57fd12`。线索是 11-02 三版审计记录（只当线索）。材料里没有密钥和个人隐私；书名、作者和引文只能进 notes |
| ④ 覆盖与方式 | 专项修订。机械盘点全量覆盖，精读只做定向的；genre 的深度按 D4 |
| ⑤ 完成标准 | 本计划第 7 节；不更新 `distillation/results/` |
| ⑥ 允许的操作 | 读仓库和 git 历史；写 `distillation/`；在 scratchpad 跑只读统计脚本；按 D1 写 `skills/`；kd_* 脚本和子代理按 D3；commit 和 push 需要另行授权 |
| ⑦ 学习深度 | 标准。审计已列的条目、热门三类题材、v2→v3 被连带删除的规则体，按严格处理 |

长期约束（写进 requirements.md，跨轮继承）：
- 成品不提来源。
- 例子一律自创、通用。
- 不改 knowledge-compiler。
- 不把有意的口径调整当成丢失。

## 附录 E：GQ 用例草案（P5 写入各 skill 的 brief.json；全部自创）

每个 skill 四类用例：正常、缺料、冲突、边界。“期望”一栏写的是合格成品应有的行为，不是固定答案。

### line-editing-and-proofreading
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 一段约 800 字的中文小说正文，要求精修句子和标点，保留口吻 | 先定第 0 轮的三件事，再按层次改，交付改后文本和逐条说明 |
| 缺料 | 只有一句“帮我润色”，不说用途、体例和读者 | 先问；用户不答时按最小改动处理，并列出所做的假设 |
| 冲突 | 要求“每句都更有力”，同时要求保留方言口语和意识流段落 | 先判负触发：口语和意识流段不改，冲突列给作者选 |
| 边界 | 英文对白稿，只要拼写和标点校对 | 只做机械层，不碰风格 |

### cross-media-drama-adaptation
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 3 万字中篇改编成 90 分钟舞台剧 | 给改编合同、分场表和信息载体方案 |
| 缺料 | 只有梗概，没有原作文本 | 只出方案草稿，依赖原文的部分标明“未见原文” |
| 冲突 | 要保留全部内心独白，又不许用旁白 | 列出冲突和替代载体，由作者选 |
| 边界 | 改成多结局的互动音频 | 走互动改编分支，交付分支表 |

### scene-conflict-and-rhythm
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 设计一场两人谈判戏 | 写明进场和离场各变了什么、约束从哪来、知情差 |
| 缺料 | 只说“这一章节奏慢”，不给正文 | 先要正文；先给检查清单，不臆断原因 |
| 冲突 | 作者把高潮定在第 10 章，但第 6 章已有更强的对决 | 按 SU-02 给“降级前文”和“重定峰值”两条路，由作者裁决 |
| 边界 | 几十人的群战 | 走群战与转述规则，不逐人写打斗 |

### character-and-narrative-control
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 双视点悬疑 | 交付视角合同和统一信息表 |
| 缺料 | 人物还没有任何台词样本 | 走“声口待定”的出口，不编造口吻 |
| 冲突 | 坚持第一人称，又要读者知道主角不知道的阴谋 | 列出补光、换视点、事后叙述等选项和各自代价 |
| 边界 | 叙述者不是人（例如一栋房子） | 说明视角合同哪些项不适用、哪些要改写 |

### story-architecture-and-longform-planning
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 12 万字单本 | 交付主行动、终点、中点、高潮时点 |
| 缺料 | 连载已发 80 章，只给后续想法，没给已发大纲 | 先要已发内容的状态账，再规划 |
| 冲突 | 已发布章节锁定，新卷设定与已发内容矛盾 | 只改未发部分，列出最小冲突集合，由作者裁决 |
| 边界 | 每篇独立、共享人物的系列短篇 | 说明篇幅容器和分卷规则哪些适用 |

### fiction-planning-and-diagnosis
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 从一个点子做新作计划 | 定赛道，交付骨架和场景表 |
| 缺料 | 要诊断，只给了梗概 | 只做梗概层的诊断，列出还需要哪些正文 |
| 冲突 | 读者反馈要求加感情线，作者的契约是纯推理 | 给反馈分级，说明对契约的影响，由作者决定 |
| 边界 | 半纪实作品里的统计数字 | 走事实核验流程，核实不了的标“未能核实” |

### genre-fiction-craft
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 仙侠长篇设计功法代价体系 | 题材规则加机制，交付代价账 |
| 缺料 | 只说“写个言情”，没有人物和阻碍 | 先问；先给几种阻碍类型供选 |
| 冲突 | 推理要求线索先给，作者却想最后一章才让凶手出场 | 列出冲突，给“早出场但不显眼”这类折中方案 |
| 边界 | 科幻、言情、悬疑混合 | 按混合题材规则确定主次 |

### preset-card-generation
| 类 | 输入 | 期望 |
|---|---|---|
| 正常 | 为一部都市异能连载生成推进模式卡 | 交付推进卡，并通过交付前检查 |
| 缺料 | 要文风卡，但没给样文，也没描述 | 先要样文；先给几种候选文风让作者选 |
| 冲突 | 已锁定的文风卡要求短句，新的表达约束卡写“不要碎句” | 走版本和锁定内容的冲突出口，不擅自覆盖已锁定的卡 |
| 边界 | 要给图片生成模型写提示词卡（不是小说） | 判为负触发，说明不适用 |

## 附录 F：执行分片表（断点续做的单位）

- 每片的 v0 精读量约 100 KB 以内；单个 v0 skill 超过 100 KB 的，按文件再切成 a1、a2……
- 每片完成的标准：
  - loss-inventory 这一片的记录都有决定；
  - 决定为恢复或合并的，已写入 `output/`；
  - 跑过附录 B 的扫描；
  - log.md 追加了一行。

| 片 | 内容 | v0 来源（体量） |
|---|---|---|
| K0 | P0 建工作区和需求 | — |
| K1 | P1 机械盘点，7 个 skill 一次跑完，只出 raw 表 | 全部（不精读） |
| K2 | P2 套件合同：附录 C 定稿、状态词、模板规范 | — |
| S01 | line-editing | style-refinement-and-proofreading（91 KB） |
| S02 | cross-media | cross-media-drama-transfer（53 KB） |
| S03a | scene：伏笔、悬念、强度、章末 | foreshadowing-and-rhythm（59 KB） |
| S03b | scene：场景单位、动作打斗 | scene-chapter-design-lab（53 KB）、action-fight-scene-craft（54 KB） |
| S04a | character：视角、信息、时间 | narrative-pov-information-control（72 KB）、nonlinear-time-craft（37 KB） |
| S04b | character：心理、创伤 | character-psychology-trauma-craft（40 KB）、psycho-trauma-craft-b10（91 KB） |
| S05a1–a2 | story：单本结构 | plot-architecture（217 KB，按文件切两片） |
| S05b1–b2 | story：分卷连载 | serialized-volume-planning（173 KB，按文件切两片） |
| S06a1–a3 | fiction-planning：总流程、规则、模板 | fiction-craft（277 KB，按文件切三片） |
| S06b | fiction-planning：成稿自检 | fiction-craft-and-language（70 KB） |
| S06c | fiction-planning：反馈与核验 | reader-experience-and-critique（20 KB）、research-fact-verification（54 KB） |
| S07 | preset-card：合规与接口 | 无 v0 |
| G04 | genre 武侠仙侠玄幻，约 5 片 | 5 个 v0 skill，439 KB |
| G02 | genre 言情，约 4 片；含 RO-K121–166 | 7 个，334 KB |
| G05 | genre 科幻，约 4 片 | 5 个，343 KB |
| G06 | genre 历史架空，约 4 片；含 source-cases 的案例分析 | 6 个，402 KB |
| G11 | genre 身份复仇权谋，约 3 片 | 6 个，297 KB |
| G03 | genre 恐怖，约 4 片 | 5 个，368 KB |
| G01 | genre 推理，约 4 片 | 5 个，338 KB |
| G10 | genre 职业竞技，约 3 片 | 3 个，293 KB |
| G07 | genre 求生灾变，约 3 片 | 3 个，225 KB |
| G08 | genre 探险寻宝，约 2 片 | 3 个，165 KB |
| G09 | genre 喜剧，约 2 片 | 4 个，193 KB |
| G12 | genre 儿童青少年，约 2 片 | 3 个，121 KB |
| G13 | genre 异世界穿越，约 2 片 | 3 个，116 KB |
| G14 | genre 年代现实，1 片 | 1 个，35 KB |
| G00 | genre 的 SKILL.md 路由和混合题材一节 | — |
| K4 | P4 全套隔离回读 | — |
| K5 | P5 质量门禁、冻结、落地 | — |

顺序就是表中顺序，genre 内按 D4 的优先级排列。每片相对独立，中断后从 log.md 记的片名接着做。

## 附录 G：notes 里另外三种记录的格式

### G.1 source-synthesis/<skill>.md（R17 §4a 决策链）

每条复杂需求一节，五项都要写；简单而没有分支的需求写一句“不适用”，并说明原因：

1. **情境**：输入是什么，哪些信息确实拿得到；分清已知、推断和用户要求。
2. **区分信号**：凭什么判断走 A 而不走 B，反信号是什么，判错的代价是什么。
3. **两条分支的做法**：A、B 各自读什么、产出什么、什么时候停下请作者裁决。
4. **反例与修复**：什么情况会推翻判断，修完后复查什么。
5. **成品落点**：最终文件 + 规则编号。出处只写在这一节的“来源”小项里，不进成品。

### G.2 operations-contract/<skill>.md（R18 §2c）

- 不能照抄 SKILL.md 全文。
- 至少写一个真实会失败的用户输入，以及对应的保护分支。
- 写明后续怎么验证；可以引用附录 E 的用例编号。

### G.3 R18 §4 六问（每个 skill 一张表）

| 问 | 本 skill 的答案 | 成品位置 |
|---|---|---|
| 1 触发：相近但不该用的请求，转给谁 | | |
| 2 缺料：没给正文时，会不会编造引文或已完成的动作 | | |
| 3 冲突：版本、锁定内容、互斥要求，由谁裁决 | | |
| 4 权限：分析会不会被当成允许改稿、写文件 | | |
| 5 格式：模板字段和交付格式是否一致 | | |
| 6 消费者：声称的跨 skill 接口有没有真实的提供方 | | |

状态只写 FAIL（实测失败）、STATIC_CHECKED（只做了静态检查）或 NOT_PROVEN（没有独立回执）。这些词只用在 notes 里，不进成品。

## 附录 H：写作建议（Claude 提出，待 D5 采纳）

这些建议来自我对小说写作的理解，不是从 v0–v2 材料提炼的，身份是“设计推断”，没有读者数据支持。

采纳后写进 skill 时，和其他规则一样要写适用条件和反例，不加固定的章数、字数和比例。多数建议在现有 skill 里已有相近规则，采纳时以补条件、补反例、补检查为主。

### H.1 所有 skill 共用的底层检查

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 1 | **每场戏都要有变化**：进场和离场时，处境、关系、信息、目标、代价至少变一项。没有变化的场景，合并、删掉，或改成概述 | scene、fiction-planning | 缓冲场可以只改变情绪或读者的理解，但要说清它缓冲的是什么 |
| 2 | **欲望 → 阻碍 → 选择 → 代价**：关键推进要来自人物自己的选择，代价要让读者看得见 | story、character | 被命运或灾难推着走的故事也能成立，此时“不做选择”本身就是代价 |
| 3 | **先问读者此刻知道什么**：开写一章前，列出读者已知、人物已知、谁比谁知道得多。读者知道危险而人物不知道，产生悬念；读者也不知道，才是惊奇。同一个揭示不要两头都想要 | character（信息表）、scene | 群像或多视点要按视点分别记 |
| 4 | **承诺和兑现记账**：开篇的问题、章末钩子、伏笔、能力设定，都是对读者的承诺。在规划文档里记账，结局前逐条兑现、转化或明确放弃 | story、scene | 故意不兑现可以，但要让读者感到是有意为之 |
| 5 | **具体胜过形容**：情绪和氛围靠视点人物此刻会注意到的具体事物传达，不靠堆形容词 | line-editing、preset-card（表达） | 快速过渡段可以概括 |

### H.2 长篇与连载

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 6 | **状态账本**：每章结束时更新人物的位置、伤势、持有物、知情状态、关系变化和未兑现的承诺。长篇的连贯性错误多半出在没有账本 | story（跨卷记账）、preset-card（给模型的上下文） | 短篇可以只记知情状态和承诺 |
| 7 | **升级要有天花板和代价**：实力或局势每升一级，同时提高代价或加一条新限制，不能只是数值变大 | genre 04、story（套路与升级） | 阶段性的碾压爽点可以暂时没有代价，但要计划好回收点 |
| 8 | **钩子轮换**：章末钩子在危险、疑问、揭示、情感、反转之间轮换，避免连续几章用同一种钩子，让读者麻木 | scene、story | 不规定轮换周期，按读者反馈和章长判断 |
| 9 | **中段靠复杂化，不靠重复**：中段的冲突要改变问题的性质（新信息、盟友反目、目标错位），不要让同一种阻碍再来一遍 | story、fiction-planning（中段塌的诊断） | 系列单元剧可以重复结构，但每个单元的赌注要不同 |

### H.3 给模型写作用

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 10 | **先列节拍再写正文**：每章先列节拍（谁想要什么、发生了什么改变），作者确认后再展开，节拍数量按章长定 | fiction-planning（起草）、preset-card | 作者想即兴流写时不强制 |
| 11 | **AI 腔清单当检查项，不当禁词表**：总结式段尾（“这一刻他终于明白……”）、对称的三连句、先直说情绪再演一遍、过多的“仿佛 / 似乎 / 一丝”、每段一样长、结尾必升华。改根因：给这一段一件只属于这一场的具体任务，而不是换同义词 | line-editing、preset-card（表达约束卡） | 防止改过头，变成一串碎句、人人说谜语、毫无情绪 |
| 12 | **新章开头不复述前情**：需要前情时，由人物当前的行动带出来 | story（续卷前情）、preset-card | 隔了很久才更新的连载，可以有一句话的提醒 |
| 13 | **声口区分**：给主要人物各定用词范围、句长习惯、回避的话题和口头习惯；遮住说话人标签，仍能分辨是谁在说 | character、preset-card（文风） | 还没有台词样本时走“声口待定” |
| 14 | **潜台词**：重要对话里，人物说出口的和真正想要的不一致；不让人物把自己的心理动机直接讲出来 | character、scene | 直白本身就是性格特点的人物除外 |

### H.4 修订

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 15 | **由大到小分轮改**：结构 → 场景 → 段落 → 句子 → 校对，每轮只盯一个层级；上层没定下来之前不精修句子 | fiction-planning（修订）、line-editing（层次） | 交稿前的小修可以直接进句子层 |
| 16 | **反向大纲**：对已写的稿子逐场写一句“这场改变了什么”，找出没有变化、重复和顺序错位的场景 | fiction-planning（诊断）、story | 不到一章的短稿不需要 |
| 17 | **读者反馈只取观察，不取药方**：记录读者在哪里停下、哪里困惑、哪里想跳过，改法由作者决定 | fiction-planning（读者反馈） | 设定矛盾、时间线错误这类可核错误，可以直接改（呼应 S-2） |

### H.5 开篇与结尾

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 18 | **开篇给一个在行动中的人物和一个扰动**：背景和设定先压到最少，等读者开始追问时再给 | fiction-planning（开篇契约）、story | 氛围型作品可以慢开，但开篇要让读者知道读下去能得到什么 |
| 19 | **常见的开法要有理由**：醒来、天气、照镜子描写外貌、梦境开场都不是禁区，只是太常见，用的时候要说得出这一章为什么非这样开不可 | fiction-planning、preset-card（推进） | 梦境如果本身就是故事规则的一部分，可以用 |
| 20 | **高潮由主角的选择决定**：巧合可以制造麻烦，不能解决麻烦；结尾要回答开篇提出的那个问题 | story（结尾、因果与巧合） | 喜剧和荒诞作品可以让巧合解决问题，但要有贯穿全篇的规则撑着 |
| 21 | **高潮之后留一个短的余波场**：让读者看到改变之后的人物或世界 | story、scene（结尾） | 悬疑可以停在揭示之后，余波压到一两段 |

### H.6 人物

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 22 | **人物弧以一个错误信念为轴**：开篇人物相信一件不对的事，故事逼他去检验；结局是他改变了、坚持并付出代价，或者因此堕落 | character、story | 人物自身不变的故事也能成立，此时改变的是他周围的世界 |
| 23 | **配角有自己的目标**：每个重要配角写一句“他在这场戏里想要什么”，避免只为主角服务的工具人 | character、fiction-planning（人物工具化的诊断） | 只出场一次的功能性人物可以不写 |
| 24 | **对手的逻辑要自洽**：对手的行动在他自己掌握的信息和价值观里是合理的；主角输的地方要输得真实 | character、genre 11 | 灾难、怪物这类自然力量式的对手不需要动机，但需要规则 |

### H.7 设定与世界观

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 25 | **设定在冲突中揭示**：只写这一场人物会想到、会用到的设定；百科式的说明留在作者自己的设定文档里 | genre（各题材的世界观）、fiction-planning（设定压过人物） | 读者本来就期待看设定的题材，可以有说明段，但要和人物的风险挂上钩 |
| 26 | **先展示限制，再用来解决问题**：关键的能力、技术、法术，在用来破局之前，先让读者见过它的限制；限制比能力更能制造故事 | genre 04 / 05、scene（伏笔与兑现） | 揭示能力本身就是谜底的故事，至少要提前给公平的线索 |
| 27 | **加设定前先查冲突**：新增设定前，先和已有设定、已发布的章节核对一遍 | story（跨卷记账）、genre | 还没有发布的草稿可以改旧设定，但要记下改了什么 |

### H.8 风格、视角与模型工作流

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 28 | **视角距离要稳**：同一场戏里，不要无理由地在贴近人物内心和全知评论之间来回跳 | character（叙述距离） | 场末有意拉远做收束可以 |
| 29 | **句子节奏服务张力**：紧张时短句和动作动词多一些，舒缓时句子可以长一些；全篇不要只有一种节奏 | line-editing、scene | 紧张段也不要全是碎句 |
| 30 | **感官要选，不要列**：视觉之外也用声音、气味、触感，但每处只用最能代表这一刻的一两种 | line-editing、preset-card（文风） | 感官本身是情节线索时可以写细 |
| 31 | **给模型的上下文分层**：按卡片（推进 / 文风 / 表达）→ 状态账本 → 本章节拍 → 上一章最后一段原文的顺序给，不要整本大纲一股脑塞进去 | preset-card、story | 宿主上下文够大时可以多给，但要分层标明 |
| 32 | **关键场景出两版**：让模型按不同的选择或不同的揭示时机各写一版，由作者挑，比反复改一版更快找到方向 | fiction-planning（起草）、scene | 日常过渡章不需要 |

### H.9 对白

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 33 | **每句对白都有意图**：要东西、拒绝、试探、掩饰或攻击；没有意图的寒暄删掉，或压成概述 | scene、character | 用来建立日常质感的寒暄可以留一两句 |
| 34 | **不让人物互相讲彼此早就知道的事**：需要向读者交代信息时，改成冲突中的追问、误解，或者让不知情的第三方来问 | scene、line-editing | 宣誓、审判这类仪式性场合，重述本身有功能 |
| 35 | **对白标签从简**：多用“说”，或用动作带出说话人；少用“咆哮道”“冷笑道”这类自带情绪的动词 | line-editing、preset-card（表达） | 童书和喜剧可以写得更夸张 |
| 36 | **打断、答非所问、沉默也是对白**：冲突对话里，不必每句都完整回答上一句 | scene、character | 信息交接类的对话要答清楚，免得读者跟丢 |

### H.10 中文连载实务

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 37 | **前几章就让读者知道这本书的核心乐趣是什么**，并尽快给第一次兑现 | story（开篇契约）、genre | 慢热作品要靠简介和开篇的语气先建立预期 |
| 38 | **每章至少推进一条线**（主线、感情线、成长线、悬念线中的一条），章末留下读者想点开下一章的理由 | story、scene（章末） | 不规定字数，按平台和读者习惯定 |
| 39 | **读者评论分三类处理**：可核错误直接改；读者看不懂的，查是不是表达出了问题；口味分歧只记录，不跟着改 | story（读者反馈）、fiction-planning | 和第 17 条、S-2 一致 |
| 40 | **长时间停更后回归**：用一章之内的行动把关键状态带回来，不写长篇回顾 | story（续卷前情） | 卷首可以有一段简短的前情 |
| 41 | **外挂、系统这类设定要有规则、限制和成长代价**，并且让它制造问题，而不只是解决问题 | genre 04 / 13、story（套路与升级） | 轻松向作品可以弱化代价，但规则要稳定 |

### H.11 题材通用

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 42 | **先兑现题材的承诺，再创新**：读者选题材是为了特定体验（推理的公平解谜、言情的关系推进、恐怖的不安感），先保证这份体验，再在上面做变化 | genre（各题材指南） | 有意颠覆题材的作品，要在开篇就让读者感到这是有意为之 |
| 43 | **套路是工具**：用一个套路时先问“这次和读者见过的有什么不同”，人物、代价、视角、结局至少变一项 | genre、preset-card（推进） | 致敬或戏仿作品可以刻意保留原样 |
| 44 | **混合题材分主次**：由一个题材决定结构和结局，其他题材提供质感和支线 | genre（混合题材） | 双主线的作品要分别给两条线结局 |

### H.12 作者的工作方式

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 45 | **初稿先写完再改**：初稿阶段不回头精修前文，发现的问题记进修改清单 | fiction-planning（起草） | 视点或主线选错这类结构性错误，要尽早停下来重定 |
| 46 | **每次写完记一行**：下一场要写什么、卡在哪里；下次从这里接着写 | fiction-planning、story | 和本计划的 log.md 断点做法相同 |
| 47 | **隔一段时间再改**：初稿写完后放一放，再用读者的眼光去读 | fiction-planning（修订） | 连载有截稿压力时，至少隔一夜再读 |
| 48 | **修改清单按影响排序**：先改影响理解和追读的问题，再改句子层面的问题 | fiction-planning（诊断报告）、line-editing | 校对类错误可以随手改 |

### H.13 情感与主题

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 49 | **情绪的力度来自前因**：写情绪高点之前，先检查读者是否已经在乎这个人、知道他会失去什么 | scene、character | 开篇的强情绪事件可以先给，关系后补 |
| 50 | **克制常比直说更有力**：人物越想压住情绪，读者感受越强；让动作和细节替人物哭 | character、line-editing | 喜剧和儿童文学可以直白 |
| 51 | **主题不说出来**：主题通过人物在两难中的选择体现，不由人物或叙述者宣讲 | fiction-planning（说教检查） | 寓言和童话可以有明确的寓意，但要短 |
| 52 | **母题重复时让含义变化**：同一个物件第二次出现时，处境已经不同（和 SU-13 合并） | scene（母题） | — |

### H.14 时间与结构技巧

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 53 | **闪回要有触发和后果**：由当前场景里的东西引出，回到现在时处境要因此改变；不在高潮前插长闪回打断张力 | character（非线性时间） | 结构性的双时间线不受此限 |
| 54 | **场景和概述分工**：重要的变化用场景演出来，过渡和重复的过程用概述带过 | character（场景与概述）、scene | 风格上以概述为主的作品，关键处仍要落到场景 |
| 55 | **多视点群像**：每个视点人物有自己的问题和弧线；换视点时，新视点要带来旧视点给不了的信息或代价 | character（切换账本） | — |
| 56 | **时间压力**：给故事一个期限（倒计时、季节、仪式日），让选择变得紧迫 | story、scene | 日常向作品可以没有外部期限，但要有内在的时机 |

### H.15 敏感题材与边界

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 57 | **创伤和暴力写后果，不写奇观**：重点放在对人物的影响和之后的生活，不渲染细节 | character（创伤边界）、genre 03 | 恐怖的惊吓需要具体，但仍要服务于人物 |
| 58 | **涉及未成年人的内容按读者年龄定边界**：儿童向作品以安全感和自主性为底线 | genre 12 | — |
| 59 | **写现实中的群体和职业，先核实**：核实不了的写成虚构机构，不对真实群体下结论 | fiction-planning（事实核验）、genre 10 / 14 | — |
| 60 | **模仿文风只学手法，不抄原句**：要写“像某种风格”时，拆成可描述的特征（句长、用词、视角距离、节奏），不复制具体作品的句子和标志性表达 | preset-card（文风卡） | 和成品不提来源的要求一致 |

### H.16 简介、标题、短篇与改编

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 61 | **简介先写人物和困境，再写钩子**，不写成设定百科 | story、genre | — |
| 62 | **章节标题保持一种风格**，不剧透关键揭示 | story | — |
| 63 | **短篇只讲一件事**：一个人物、一次变化，开头尽量靠近结尾 | fiction-planning、story（篇幅容器） | 连环短篇可以共享人物，但每篇自成一个变化 |
| 64 | **改编先定必须保留的读者体验，再决定删改**：媒介换了，保留的是体验，不是情节清单 | cross-media（能不能转） | 合同明确要求忠实于情节时，以合同为准 |

### H.17 场面与细节

| # | 建议 | 落到哪里 | 边界 / 反例 |
|---|---|---|---|
| 65 | **揭示之前给读者猜的机会**：重要揭示之前，相关线索至少以不显眼的方式出现过；回头看时，读者应当觉得“原来如此”，而不是“凭什么” | scene（悬念与揭晓）、genre 01 | 恐怖片式的突然惊吓可以不铺垫，但事后要讲得通 |
| 66 | **喜剧靠执念和错位**：让人物认真地追求一件事，而读者看得见他看不见的错位；笑点放在句末或段末 | genre 09、line-editing | 讽刺要选准对象，避免嘲笑弱者 |
| 67 | **动作场面先保证读者跟得上**：交代空间（谁在哪里）、目标（各自要什么）、代价（每一下的后果）。读者能跟住局势，比动作华丽更重要（和动作检查表 A1–A7 合并） | scene（动作与打斗） | — |
| 68 | **人名和称谓保持一致**：同一个人物的称呼随关系或场合变化时要有理由；主要人物名字的首字和字数错开，免得读者认混 | line-editing（体例）、character | 身份谜题这类有意制造的混淆除外 |
| 69 | **数字、时间线、距离做成一张表**：年龄、日期、行程时间、金额前后一致，改一处要连带检查其他地方 | line-editing（全书体例）、story（状态账本） | — |
| 70 | **群戏调度**：一场戏人多时，只让两三个人有完整的动作和台词，其余人用群体反应带过；镜头每次只跟一个焦点 | scene、character | 群像作品的高潮可以轮流给特写，但要按顺序来 |
| 71 | **先交代空间，再开始行动**：进入新场景时，用一两个能定位的细节说明在哪里、有谁、出口在哪，再开始冲突 | scene（知情与空间） | 混乱场面可以故意延后交代，但关键行动前要补上 |
| 72 | **章末最后一句落在具体的东西上**：一个动作、一句台词或一个物件，比总结式的感慨更有余味（和第 11 条呼应） | scene（章末）、line-editing、preset-card（表达） | — |

### H.18 落地方式

按 skill 汇总，各自接收的建议编号：

| skill | 建议编号 |
|---|---|
| fiction-planning-and-diagnosis | 1、9、10、15、16、17、18、19、23、25、32、39、45、46、47、48、51、59、63 |
| story-architecture-and-longform-planning | 2、4、6、7、8、9、12、16、18、20、21、22、27、31、37、38、39、40、41、46、56、61、62、63、69 |
| character-and-narrative-control | 2、3、13、14、22、23、24、28、33、36、49、50、53、54、55、57、68、70 |
| scene-conflict-and-rhythm | 1、3、4、8、14、21、26、29、32、33、34、36、38、49、52、54、56、65、67、70、71、72 |
| line-editing-and-proofreading | 5、11、15、29、30、34、35、48、50、66、68、69、72 |
| genre-fiction-craft | 7、24、25、26、27、37、41、42、43、44、57、58、59、61、65、66 |
| preset-card-generation | 5、6、10、11、12、13、19、30、31、35、43、60、72 |
| cross-media-drama-adaptation | 64 |

一条建议落到两个 skill 时，按附录 C 的 Owner 写在主 skill 里，另一个 skill 只写转介，不写两份。

- **先查重**：D5 采纳后，每条建议先在 P1 的 loss-inventory 里查重。材料里有同义规则的，合并进现有规则并补条件；材料里没有的，作为新规则写入对应 skill。
- **成品写法**：“设计推断”的身份只记在 notes 里，成品里正常写成规则，带适用条件和反例。
- **冲突处理**：和材料提炼出的规则冲突时，不自动覆盖，列给你裁决。
- **验收**：对应附录 E 的用例时，这些建议只算静态完成，效果仍是 NOT_PROVEN。
