# 套件合同定稿（K2 · W1 · Agent 1）

- 依据：计划附录 C（Owner 与转介矩阵）、附录 B（去来源扫描）、附录 E（GQ 用例）、附录 G.3、R18 §2a / §2b、R09 §6.1；用户裁决 D2=A、D3=C。
- 性质：**定稿**。K2 只出规范与清单，**不代写 8 个 SKILL.md、不写 `quality/<skill>/brief.json` 正式文件、不改 `skills/`**。落地动作归 W3 执行组（见第七节）。
- 本文件属 `notes/`，内含内部编号与审计词说明；这些词**不进成品**。

---

## 一、Owner 与转介矩阵（附录 C 定稿）

### C.1 各 skill 负责什么 / 不负责（转给谁）

| skill | 负责 | 不负责（转给） |
|---|---|---|
| fiction-planning-and-diagnosis | 总流程：定篇幅、媒介、类型和交付；新作规划的入口；成稿诊断、修订删减、成稿自检；现实断言的事实核验；读者反馈 | 结构骨架和分卷（story）、视角和信息（character）、单场设计（scene）、句子精修（line-editing）、题材规则（genre）、预设卡（preset-card） |
| story-architecture-and-longform-planning | 单本结构（主行动、终点、高潮、因果、多线、结尾）；长篇分卷、卷末收与接、跨卷伏笔账、连载排产 | 场内节奏（scene）、视角（character）、总流程和赛道（fiction-planning）、推进卡（preset-card） |
| character-and-narrative-control | 视角合同、叙述距离、信息控制、证词与自辩、心理落到动作上、场景与概述、非线性时间 | 场景冲突和强度（scene）、卷级结构（story）、预设卡（preset-card） |
| scene-conflict-and-rhythm | 场景单位、知情与空间、伏笔兑现、悬念、强度与节奏、章末钩子、动作打斗 | 卷级节奏（story）、视角（character）、句子精修（line-editing）、预设卡（preset-card） |
| line-editing-and-proofreading | 中英文句子级精修、校对、体例、句子层的 AI 腔 | 结构和场景问题（转对应 skill）、预设卡里的表达约束（preset-card） |
| genre-fiction-craft | 14 类题材特有的规则、机制、反例和题材混合 | 不分题材的通用手法（转对应的通用 skill）、预设卡（preset-card） |
| cross-media-drama-adaptation | 改编为舞台、影视、音频和互动形式 | 小说本身的创作（转对应 skill）、预设卡（preset-card） |
| **preset-card-generation（D2=A）** | 预设卡（推进模式卡、文风卡、表达约束卡）的**生成、诊断、审校、修订**；用「推进 / 文风 / 表达」三轴给章节做诊断 | **不写成卡、也不用三轴的**一般规划（fiction-planning）、结构（story）、精修（line-editing）、题材（genre）、视角人物（character）、场景节奏（scene）、改编（cross-media）问题——转对应兄弟 skill |

### D2=A 的边界（双向转介，逐条写死）

**保留**：preset-card 的「推进 / 文风 / 表达」三轴全流程（生成 → 诊断 → 审校 → 修订）完整保留，**但只负责预设卡和三轴诊断**。

**preset-card → 兄弟 skill**（请求不写成卡、也不用三轴时转出）：

| 请求形态 | 转给 |
|---|---|
| 一般性的新作规划、定赛道、成稿诊断 | fiction-planning-and-diagnosis |
| 单本结构、分卷、排章纲（产物是规划文档，不是给模型的卡） | story-architecture-and-longform-planning |
| 改具体稿子去 AI 味（产物是改好的文本） | line-editing-and-proofreading |
| 题材规则、机制、混合题材 | genre-fiction-craft |
| 视角合同、人物声口、信息控制 | character-and-narrative-control |
| 单场设计、强度节奏、章末钩子 | scene-conflict-and-rhythm |
| 改编为舞台 / 影视 / 音频 / 互动 | cross-media-drama-adaptation |

**兄弟 skill → preset-card**（遇到卡片请求一律转回）：

| 触发 | 判断依据（C.2） |
|---|---|
| 生成 / 修订 / 诊断推进模式卡、文风卡、表达约束卡 | 产物是「给模型的卡」 |
| 把规划、结构写成推进卡给模型用 | 产物是卡，不是规划文档 |
| 按推进 / 文风 / 表达三轴审章节 | 审查框架是三轴 |
| 写「反 AI 味的约束卡」 | 产物是约束卡，不是改好的文本 |
| 用户已有文风卡或推进卡作为输入、要据此写这一章 | 有卡作为输入 |

**双向对照**：A 说转给 B 的地方，B 都要说接收什么（GQ3 双向引用核对，见第七节）。上两表互为逆关系，W3 落地时逐行双向核。

### C.2 重叠请求怎么分（相关行须写进各自 SKILL.md 的「适用与转介」）

| 用户请求 | 归属 | 判断依据 |
|---|---|---|
| 「帮我规划一本书」 | fiction-planning 做入口，结构部分交给 story | 要定赛道和交付的，从 fiction-planning 进 |
| 「规划一卷 / 排章纲」 | story；要写成推进卡给模型用时，交给 preset-card | 产物是规划文档，还是给模型的卡 |
| 「去 AI 味」 | 改具体稿子交给 line-editing；写成反 AI 味的约束卡交给 preset-card | 产物是改好的文本，还是卡片 |
| 「写这一章」 | fiction-planning 的起草流程，场景细节交给 scene；用户已有文风卡或推进卡时交给 preset-card | 有没有卡作为输入 |
| 「审这一章」 | fiction-planning 的诊断；用户指定按三轴审时交给 preset-card | 审查框架 |
| 「这一章节奏拖」 | 单元内的问题交给 scene，跨章跨卷的问题交给 story | 问题的尺度 |
| 「武侠打斗写不好」 | 题材约束看 genre 04，动作写法看 scene | 先用题材约束，再用通用手法 |

---

## 二、交付状态词（统一口径 + 审计词替换位置）

### 2.1 统一四词

成品对作者交付只用这四个词：

| 状态词 | 含义 |
|---|---|
| **已完成** | 检查已执行，且有可核的证据支持 |
| **依据** | 交付时附的证据 / 稿件内可核位置（不是固定答案，也不是来源背书） |
| **未能核实** | 检查已执行，但结论依赖未核实的判断、设计假设或缺失的输入，不能记作已完成 |
| **待作者决定** | 存在冲突 / 取舍 / 锁定内容矛盾，由作者裁决，不擅自覆盖 |

不允许在成品里出现审计词、门禁词、状态码。`PASS/FAIL/NOT_PROVEN/STATIC_CHECKED/NOT_RUN/DESIGN_EXAMPLE/OBSERVED/F/H/P/GQ1–5/R17/R18` 及 `BLOCKED/NOT_APPLICABLE` 等**只留在 `notes/`**（附录 G.3、R09 §6.1），不进成品。

### 2.2 审计词替换对照

| 现有审计词 | 成品写法 |
|---|---|
| `VERIFIED` | 已完成（并写「依据」） |
| `NOT_PROVEN` | 未能核实 |
| `NOT_RUN` | 未能核实（注明未执行及所缺输入） |
| `STATIC_CHECKED` | 已完成（另标「验收范围：静态交付」） |
| `BLOCKED` / `NOT_APPLICABLE` | 待作者决定 / 未能核实（按是否缺输入分） |
| `DESIGN_EXAMPLE` / `OBSERVED` | 依据（注明自创例或稿件证据位置） |
| `PASS` / `FAIL` | 已完成 / 未能核实 |
| `F` / `H` / `P` / `GQ1–5` / `R17` / `R18` | 不进成品，只留 notes |

### 2.3 现有运行文本中的替换位置（2.6 节三处，已用 `/usr/bin/grep -rnE` 核实）

全仓库 `skills/`（排除 `knowledge-compiler/`）中 `NOT_PROVEN` / `VERIFIED` 只命中以下 3 个文件：

| # | 位置（当前工作树实际行号） | 内容 | 替换为 |
|---|---|---|---|
| 1 | `skills/cross-media-drama-adaptation/references/interactive-adaptation.md:54–59` | `VERIFIED` / `NOT_PROVEN` / `NOT_RUN` 的定义段，及「凡不是 VERIFIED 的项……」 | 四词；「凡不是已完成的项，在分支表『证据或限制』列写明原因和影响」 |
| 2 | `skills/cross-media-drama-adaptation/templates/interactive-branch-sheet.md:39,41` | 第 39 行说明句、第 41 行表头「结果（VERIFIED／NOT_PROVEN／NOT_RUN／BLOCKED）」 | 表头改为「结果（已完成／依据／未能核实／待作者决定）」；说明句同步 |
| 3 | `skills/fiction-planning-and-diagnosis/references/diagnosis.md:411` | 状态码清单 `VERIFIED / NOT_PROVEN / NOT_RUN / BLOCKED / NOT_APPLICABLE` 与 `PASS / FAIL`，并提到「与 SKILL.md §9 的中文五态一一对应」 | 改成四词；删去内部状态码清单；「中文回执模板」统一为四词，不并列两份回执 |

替换与回读是 **W3 执行组动作**（P3 第 2、6 条），K2 只定稿。替换后按附录 B #9 正则复扫零命中。

---

## 三、模板规范（R18 §2a）

有枚举编号的模板，**每个编号独占一行**，三列齐全，允许填「未知」：

| 编号 | 值 | 状态 | 稿件证据位置 |
|---|---|---|---|
| `<内部规则编号，如 SU-02 / RO-K001 / EN-27>` | `<逐项填写值>` | 已完成 / 依据 / 未能核实 / 待作者决定 / **未知** | `<用户当前稿件内可核位置，如「第 3 章第 2 场」；无则填「未知」>` |

落地要求：

- 枚举要求在 reference 写满，最终填写模板不得合为一行；编号与 reference 一一对应。
- 「值 / 状态 / 稿件证据位置」三列每行都在；「未知」是合法值，但**不得把未知写成已完成**。
- 「稿件证据位置」只指向**用户当前稿件**，不指向来源编号、包外路径、批次或 notes。
- 每个有枚举模板的 skill 在 `notes/delivery-preflight-spec/<skill>.md` 配一份 spec（列出编号全集与逐行填写要求），P5 用 `brief.json` 核对字段可填、缺省与当前任务证据定位。
- 表格必须有 GFM 分隔行（R09 §6.4 第 2 条）；有数据行却缺分隔行视为交付格式失败。

---

## 四、去来源检查清单

### 4.1 P2 的 7 类（第 6 节 P2，逐条判断）

1. 书名号作品名、作者和人名；
2. 来源编号，包括 `-NNNN` 这类残片；
3. 来源的年代和篇数；
4. 「原文 / 书内 / 同书 / 书里 / 来源是 / 材料标称」这类说法；
5. 包外路径；
6. 「旧版 / 本版 / 更正」这类改动痕迹；
7. 删除来源后留下的空括号和悬空的「见 / 据」。

### 4.2 附录 B 的 11 类正则（B.1）

本机 `grep` 是 ugrep，中文长模式会报「exceeds complexity limits」；统一用 `/usr/bin/grep -rnE '<模式>' skills --exclude-dir=knowledge-compiler`，命中逐条判断，不把命中直接判违规。

| # | 目标 | 模式 |
|---|---|---|
| 1 | 书名号里的作品名 | `《[^》]+》`（例外：讲标点用法时列举的「《》」符号本身） |
| 2 | 来源编号和残片 | `PG[ -]?[0-9]+` 、`(^\|[^A-Za-z0-9])-[0-9]{3,5}([^0-9]\|$)` |
| 3 | 来源的数量和年代 | `[0-9]+ ?本(材料\|书\|手册)` 、`材料标称` 、`(1[5-9]\|20)[0-9]{2} ?年(代)?.{0,8}(市场\|手册\|杂志\|出版\|建议)` |
| 4 | 指向学习材料的说法 | `书内\|书里\|同书\|该书\|此书\|原书\|来源是\|出自\|引自\|据称\|这批材料\|学习材料\|原文库\|批次` |
| 5 | 作者、作家和名人 | `作家\|小说家\|评论家\|大师\|名著\|经典作品` ，以及 `[A-Z][a-z]+ [A-Z][a-z]+` |
| 6 | 英文原句 | `"[A-Z][a-z]+( [a-z]+){4,}` |
| 7 | 包外路径 | `notes/\|results/\|/home/\|materials/\|rounds/` |
| 8 | 改动痕迹 | `旧版\|本版\|更正\|早先的版本\|融合版\|上一版` |
| 9 | 审计词 | `NOT_PROVEN\|VERIFIED\|NOT_RUN\|STATIC_CHECKED\|DESIGN_EXAMPLE\|OBSERVED\|F/H/P\|GQ[1-5]\|R1[78]` |
| 10 | 删除后的残迹 | `（\s*）\|\(\s*\)\|见\s*[，。；]\|据\s*[，。；]\|与\s*同` |
| 11 | 分档词和禁用说法 | `夯\|拉完了\|硬规则\|用户明确要求` |

（表中 `\|` 为正则内的「或」，写成 `/usr/bin/grep -rnE` 模式时按 ERE 原样使用。）

### 4.3 B.2 允许保留的情形（命中后在 `desourcing-ledger.md` 写明理由）

- **用户自己的稿件**：「原文」「原稿」指用户正在改的稿子；改编 skill 里的「原作」指用户要改编的作品；同人或穿书语境的「原著」指用户选定的底本。
- **用户稿件的版本号**：`v1→v2`、`draft-v3`、`serial-v2-outline` 这类。
- **本包内部编号**：规则编号（SU-02、RO-K001 等）和修改级别（L0–L4）。
- **自创例子里的年份**：例如虚构设定的「1910 年的小镇」；但要过 B.3 的骨架比对。
- **事实核验场景**：讲事实核验方法时出现的「来源」「出处」「引语」，指用户要核验的资料。

### 4.4 B.3 正则查不出的情形（逐文件回读人工判断）

- **例子与 v0 来源案例的情节骨架相近**：人物关系、关键事件、时代地点三项有两项以上对得上，就重写。
- **具体作品的标志性情节元素**：没有书名也算违规（如 2.5 节的儿童书元素）。
- **借来源背书的说法**：例如「经典做法是……」「很多名作都……」，改成直接写适用条件和限制。
- **删除来源后语义不通**：主语悬空、只剩半句、表格空列。

P3 每个 skill 收尾各跑一次、P4 全套再跑一次；结果记 `notes/desourcing-ledger.md`。有一处不合格就不能冻结或交付。

---

## 五、措辞禁用

成品（SKILL.md、references、templates、examples、agents、附录与元数据）一律不出现：

- **分档词**：如「夯」「拉完了」及同类分档 / 评级词（附录 B #11）；
- **「硬规则」**；
- **「用户明确要求」**；
- **「融合版」**（含「旧版 / 本版 / 更正 / 上一版」等改动痕迹，附录 B #8）。

配套口径：

- 不出现「经典做法是……」「很多名作都……」这类借来源背书的说法，改成适用条件与限制（B.3）。
- 材料没有依据的地方写「**没有依据，按作者判断**」，不编造阈值、数字或成体系的反例（第 8 节）。
- 缩减幅度是盘点信号，**不是应补回的量**；不写「本版补回 X%」这类改动痕迹。

---

## 六、附录 E 的 8 skill × 4 类用例（装配成可写入 `brief.json` 的清单，全部自创）

- 全部用例自创，不含书名、作者、作品人物 / 情节 / 设定、原句、来源编号、年代、篇数。
- 四类映射：正常 → `positive`、缺料 → `missing`、冲突 → `conflict`、边界 → `boundary`。
- `expected` 写的是**合格成品应有的行为**，不是固定答案（附录 E 原文口径）。
- 装配方式：下列每个 `cases` 数组可直接写入 `notes/quality/<skill>/brief.json` 的 `cases` 字段（R09 §6.1）。brief 的 `version`、`requirements`、`capabilities`、`interfaces`、`applicability` 由 K5 / W4 依最终 Skill 承诺补，**K2 不代写**。GQ5 真实任务未授权，这些用例只算静态完成，效果记 NOT_PROVEN。

```json
{
  "line-editing-and-proofreading": {"cases": [
    {"id":"LE-T1","kind":"positive","scenario":"一段约 800 字的中文小说正文，要求精修句子和标点，保留口吻","expected":"先定第 0 轮的三件事，再按层次改，交付改后文本和逐条说明"},
    {"id":"LE-T2","kind":"missing","scenario":"只有一句「帮我润色」，不说用途、体例和读者","expected":"先问；用户不答时按最小改动处理，并列出所做的假设"},
    {"id":"LE-T3","kind":"conflict","scenario":"要求「每句都更有力」，同时要求保留方言口语和意识流段落","expected":"先判负触发：口语和意识流段不改，冲突列给作者选"},
    {"id":"LE-T4","kind":"boundary","scenario":"英文对白稿，只要拼写和标点校对","expected":"只做机械层，不碰风格"}
  ]},
  "cross-media-drama-adaptation": {"cases": [
    {"id":"CM-T1","kind":"positive","scenario":"3 万字中篇改编成 90 分钟舞台剧","expected":"给改编合同、分场表和信息载体方案"},
    {"id":"CM-T2","kind":"missing","scenario":"只有梗概，没有原作文本","expected":"只出方案草稿，依赖原文的部分标明「未能核实」"},
    {"id":"CM-T3","kind":"conflict","scenario":"要保留全部内心独白，又不许用旁白","expected":"列出冲突和替代载体，由作者选"},
    {"id":"CM-T4","kind":"boundary","scenario":"改成多结局的互动音频","expected":"走互动改编分支，交付分支表"}
  ]},
  "scene-conflict-and-rhythm": {"cases": [
    {"id":"SC-T1","kind":"positive","scenario":"设计一场两人谈判戏","expected":"写明进场和离场各变了什么、约束从哪来、知情差"},
    {"id":"SC-T2","kind":"missing","scenario":"只说「这一章节奏慢」，不给正文","expected":"先要正文；先给检查清单，不臆断原因"},
    {"id":"SC-T3","kind":"conflict","scenario":"作者把高潮定在第 10 章，但第 6 章已有更强的对决","expected":"给「降级前文」和「重定峰值」两条路，由作者裁决"},
    {"id":"SC-T4","kind":"boundary","scenario":"几十人的群战","expected":"走群战与转述规则，不逐人写打斗"}
  ]},
  "character-and-narrative-control": {"cases": [
    {"id":"CH-T1","kind":"positive","scenario":"双视点悬疑","expected":"交付视角合同和统一信息表"},
    {"id":"CH-T2","kind":"missing","scenario":"人物还没有任何台词样本","expected":"走「声口待定」的出口，不编造口吻"},
    {"id":"CH-T3","kind":"conflict","scenario":"坚持第一人称，又要读者知道主角不知道的阴谋","expected":"列出补光、换视点、事后叙述等选项和各自代价"},
    {"id":"CH-T4","kind":"boundary","scenario":"叙述者不是人（例如一栋房子）","expected":"说明视角合同哪些项不适用、哪些要改写"}
  ]},
  "story-architecture-and-longform-planning": {"cases": [
    {"id":"ST-T1","kind":"positive","scenario":"12 万字单本","expected":"交付主行动、终点、中点、高潮时点"},
    {"id":"ST-T2","kind":"missing","scenario":"连载已发 80 章，只给后续想法，没给已发大纲","expected":"先要已发内容的状态账，再规划"},
    {"id":"ST-T3","kind":"conflict","scenario":"已发布章节锁定，新卷设定与已发内容矛盾","expected":"只改未发部分，列出最小冲突集合，由作者裁决"},
    {"id":"ST-T4","kind":"boundary","scenario":"每篇独立、共享人物的系列短篇","expected":"说明篇幅容器和分卷规则哪些适用"}
  ]},
  "fiction-planning-and-diagnosis": {"cases": [
    {"id":"FP-T1","kind":"positive","scenario":"从一个点子做新作计划","expected":"定赛道，交付骨架和场景表"},
    {"id":"FP-T2","kind":"missing","scenario":"要诊断，只给了梗概","expected":"只做梗概层的诊断，列出还需要哪些正文"},
    {"id":"FP-T3","kind":"conflict","scenario":"读者反馈要求加感情线，作者的契约是纯推理","expected":"给反馈分级，说明对契约的影响，由作者决定"},
    {"id":"FP-T4","kind":"boundary","scenario":"半纪实作品里的统计数字","expected":"走事实核验流程，核实不了的标「未能核实」"}
  ]},
  "genre-fiction-craft": {"cases": [
    {"id":"GE-T1","kind":"positive","scenario":"仙侠长篇设计功法代价体系","expected":"题材规则加机制，交付代价账"},
    {"id":"GE-T2","kind":"missing","scenario":"只说「写个言情」，没有人物和阻碍","expected":"先问；先给几种阻碍类型供选"},
    {"id":"GE-T3","kind":"conflict","scenario":"推理要求线索先给，作者却想最后一章才让凶手出场","expected":"列出冲突，给「早出场但不显眼」这类折中方案"},
    {"id":"GE-T4","kind":"boundary","scenario":"科幻、言情、悬疑混合","expected":"按混合题材规则确定主次"}
  ]},
  "preset-card-generation": {"cases": [
    {"id":"PC-T1","kind":"positive","scenario":"为一部都市异能连载生成推进模式卡","expected":"交付推进卡，并通过交付前检查"},
    {"id":"PC-T2","kind":"missing","scenario":"要文风卡，但没给样文，也没描述","expected":"先要样文；先给几种候选文风让作者选"},
    {"id":"PC-T3","kind":"conflict","scenario":"已锁定的文风卡要求短句，新的表达约束卡写「不要碎句」","expected":"走版本和锁定内容的冲突出口，不擅自覆盖已锁定的卡"},
    {"id":"PC-T4","kind":"boundary","scenario":"要给图片生成模型写提示词卡（不是小说）","expected":"判为负触发，说明不适用"}
  ]}
}
```

---

## 七、C.3 落地要求（**W3 执行组动作；K2 只出定稿，不代写 8 个 SKILL.md**）

以下逐条是 W3 在 P3 各分片中**实际写入 `output/<skill>/SKILL.md`** 的动作，K2 不执行：

1. **「适用与转介」节**：每个 SKILL.md 写出 C.2 中与自己相关的行；并包含 `preset-card-generation`（P2 要求）。preset-card 一行按 D2=A 写全双向转介（第一节两表）。
2. **description**：写全**会转去的兄弟 skill 名**。现状缺口（2.6 节）：cross-media 的 description 一个兄弟 skill 都没提；另 7 个 skill 都没提到 preset-card-generation——W3 逐一补。
3. **路由表**：8 个 SKILL.md 的路由表都缺 R18 §3 建议的「需要时补读 / 缺料或冲突时的出口」两列——W3 补两列，并给主要操作补失败出口（cross-media、preset-card 现状没有失败出口；preset-card 另补卡片版本与锁定内容冲突时的出口，R18 §2d 最后一段）。
4. **GQ3 双向引用核对**：A 说转给 B 的地方，B 都要说「接收什么」。按第一节 D2=A 两表 + C.1「不负责（转给）」列逐行双向核；核对结果记 `notes/quality/<skill>/review.json` 的 `interfaces[]`（R09 §6.3），绑定双方当前树 SHA。无跨 skill 依赖的明示空接口并独立检查有无遗漏。
5. **负触发与失败出口**：preset-card 设 `agents/openai.yaml` 的 `allow_implicit_invocation: false`，补负触发（P3 第 7 条）；保留「冒号后不反转」「示例原创」两条规则。
6. **状态词与审计词替换**：按第二节 2.3 的三处位置改写运行文本，替换后跑附录 B #9 正则复扫。
7. **模板与去来源**：按第三节逐编号一行、按第四节全 11 类正则 + B.3 人工判断逐文件回读（P3 收尾各一次、P4 全套一次）；命中按 B.2 在 `desourcing-ledger.md` 写理由。

**门禁口径（D3-C）**：以上写入由 W3 执行；W4 由 Agent 1 另派**只读审查子代理**（每个 skill 一个，只看成品包、不看 notes）做隔离回读与 GQ1–GQ4，Agent 1 只汇总与出门禁，**不自审自过**。静态通过不写成效果已证明；GQ5 无真实任务时记 NOT_PROVEN。


### 4.2bis 附录 B 判据修订（2026-11-05 16:50 追加，依 `notes/p4-closure-2026-11-05.md` 整树收口；不改写 §4.2 原表）

- **条数更正**：B.1 实为 **19 条子模式**，不是 18（原表把 #10 的两档空括号形态并成一档计）。凡引用「18 条」的台账与 spec 行一律按 19 读。
- **补档（六条）**：#8 加 `旧例|原例`；#2 加标准号形态 `GB/?T? ?[0-9]{4,6} ?- ?[0-9]{4}`（现 2b 对 `15834-2011` 实测不命中）；#3 加中文数词 `CN1 一[本部册两三四五] ?(材料|书|手册)` 与 `CN2`（阿拉伯档整树 0 命中，补档新增 22 行且重叠 0，须同时配 B.2 例外，否则一次引入 22 条误报）；#6 起点字符集改 `["“]`（弯引号漏检，实测抓到 `fiction-planning/references/scope-and-conflicts.md:19` 的英文原句）；#5b 加排除表 `Skill Owner|Plot Canvas|Diagnosis Report|Scene Table`；#10 三档字面改为「标点后悬空＋同行共现」语义判据（裸 A 判据会误伤 196 行，A∧B 后 23 行逐条判为领域语义或守卫句）。
- **locale 必写**：BSD grep 在未设 `LC_ALL` 时按字节解释中文括号类（实测 `见[，。；]` 得 121、`据[，。；]` 得 366，真值 59／224）；`LC_ALL=en_US.UTF-8` 下 `grep -oE 'A|B' | sort | uniq -c` 会把不同中文匹配串并组（实测「书里」被算进「出自」）。⇒ 任何逐类计数须声明 locale 并两档回显，走过 `sort|uniq` 的旧回执须重取。
- **覆盖诚实线**：19 条中本轮仍属**检测有效性未证**的 13 条：1a、2b、3a、4a、5a、5b、6a、8a、10a–10e（能构造正控制不等于目标类被真实覆盖；已证 6 条：2a、3b、3c、7a、9a、11a，其中仅 11a 有真实正例）。未证档**不得**写成「零违规」。
