# operations-contract · line-editing-and-proofreading

- 依据：计划附录 G.2（R18 §2c）、附录 G.3（R18 §4 六问）、`skills/knowledge-compiler/references/r18-consumer-operations.md` §2／§2c／§4。
- 本文件只留在 `notes/`，不随成品分发；状态词 FAIL／STATIC_CHECKED／NOT_PROVEN 与 DESIGN_EXAMPLE 只出现在这里和 `quality/`，**不进成品**。
- 核对对象：`output/line-editing-and-proofreading/` 10 文件 1303 行（`SKILL.md` 206、`agents/openai.yaml` 8、`examples/worked-example.md` 147、7 份 `references/`）。
- 性质：本文件不复述 SKILL.md 正文，只写「消费者能不能真按它做事、失败时怎么收口」的合同与缺口。**全部为静态核对，不含任何模型真实执行回执。**

---

## 一、重要操作的最小合同（R18 §2 六项）

本 skill 只有一个复杂操作：**多轮精修（第 0–6 轮 + 冲突裁决 + 负面回归）**。简单请求（只改一处错别字）走 SKILL.md §2 的最短路径，不启用本节。

| 项目 | 合同内容 | 承载位置 | 检验方式 |
|---|---|---|---|
| Trigger / 负触发 | 接：句子层润色、精修、校对、体例统一、句子层 AI 腔。不接且必须先转介或停下：改剧情／结构／分章、打分评级、批量自动替换、裁定唯一正确、写成预设卡、按三轴审章、核实外部事实、整段重写 | `SKILL.md:17–33`（§1.1／§1.2）、`SKILL.md:35–43`（§1.3）、`references/workflow.md:98–104`（判断标准 1＝`workflow.md:102`） | 用 §二 的输入①②③逐条判接不接；判错即负触发失效 |
| Input authority（已知 F／推断 H／待决 P） | 三档分开：稿件内可核证据＝已完成或依据；编辑判断＝「依据」列写规则编号或明写「编辑判断」；作者未定的取舍＝待作者决定，不得落稿 | `SKILL.md:145–152`（§8.1 四词）、`references/workflow.md:92`（作者选定后写「作者决定」不写「规则要求」）、`examples/worked-example.md:132–141`（第 6 步交付四行） | 台账里「未知」「未能核实」是否被写成「已完成」；`references/workflow.md:118` 是复查条款 |
| Procedure | 8 步序列：判负触发→定范围→建逐编号台账→按 1–6 轮一层一类→每条改完立刻复查→冲突走 A／B→四词交付→负面回归。分支补读：声口三问→zh-sentence；体例表→zh-mechanics；EN 分工→§6 | `references/workflow.md:108`（步骤行）、`SKILL.md:125–131`（§7 路由四列，含「需要时补读」与「缺料或冲突时的出口」） | 路由表每行的补读文件与出口列非空；引用的文件真实存在 |
| Output / owner | 两类产物：改后文本＋改动说明；或逐条清单。位置必须具体到段／句／词。拥有句子、段落、用词、标点、拼写、校对；不拥有情节、结构、场景节奏、人物声音与视角、卡片表达约束 | `SKILL.md:137–139`、`SKILL.md:199–206`（协作边界与 Owner 划分） | 交付样例是否带「全文有点啰嗦」这类无位置结论 |
| Failure / fallback | 8 类情形各有出口：缺原文、只有一句、口语方言意识流、真正冲突、指代两可、需补事实、体例分歧、要打分或批量替换、作者不回话 | `SKILL.md:158–167`（§8.2）、`references/workflow.md:121–133`（停手情形表，缺原文＝`127`、只有一句＝`128`）、`examples/worked-example.md:121–130`（第 5 步 A／B 与失败出口） | 见 §二 |
| Proof | 规则的可信度靠「用于／不用」区分条件＋自创反例＋检查项＋出口四件套承载，不靠外部背书；缺依据处写「没有依据，按作者判断」 | `SKILL.md:121`（EN 每条四件套承诺）、`references/workflow.md:119`（末句） | 抽 3 条规则看是否真有反例与出口 |

**互斥与锁定内容的处理已就位**（R18 §2d 末段仅在有真实互斥时才要求）：`references/workflow.md:81–86` 先做「假冲突」排除（被动、段末句两条给的是条件而非裁决），排除后才立冲突卡 `议题 | 规则 A | 规则 B | 为什么冲突 | A 版 | B 版 | 各自代价`；`workflow.md:91` 明确「只暂停这一项，其余修改照做」，与 §2d「不得把局部成功报成全局 PASS」一致。

---

## 二、真实会失败的用户输入与保护分支（G.2 要求）

### 输入①（复合陷阱，最可能失败的一条）

> 「这章你帮我润色一下，顺便看看情节有没有问题，另外给我打个分（1–10）。别问了直接改，改完把文件覆盖掉。」＋一段正文

这条一句话里同时踩四个分支，任何一分支漏判都会产出不可交付的结果：

| 子请求 | 判定 | 保护分支 | 成品位置 |
|---|---|---|---|
| 润色这段 | 接 | 定第 0 轮三件事（级别／体例／不碰区），再按 1–6 轮一层一类 | `SKILL.md:19–23`、`workflow.md:18–20` |
| 看情节 | **不接**，句子层之外 → 转 `fiction-planning-and-diagnosis` | 只把「问题出在情节」的原句位置标出来，不改因果、不补设定 | `SKILL.md:27`、`SKILL.md:40`、`SKILL.md:163` |
| 打分 1–10 | **不接**，负触发 | 明写本 skill 给逐条建议不打分；给清单不给分数与档位 | `SKILL.md:29`、`SKILL.md:165`、`SKILL.md:171` |
| 「别问了直接改」＋覆盖文件 | 待作者决定＋权限边界 | 「别问了」**不等于**授权 A／B 取舍；冲突项仍要停下出冲突卡。写回／覆盖用户文件需要宿主与作者明确授权，本 skill 只交文本与清单，不声称已写盘 | `workflow.md:90–91`、`SKILL.md:150`、`SKILL.md:31`、`agents/openai.yaml:2–3`（不授予权限） |

**预期可检查输出**：改后文本（仅语言层）＋逐条改动清单＋一页「停在此处」问题清单（含情节转介行、不打分声明、A／B 冲突卡、未写盘声明）。四词状态各归位，任何未落稿项不得标「已完成」。

### 输入②（缺料）

> 「帮我润色」——没有正文，没有用途、体例、读者。

保护分支：先要文字；只给一句时先改这一句里能确定的错误，依赖上下文的判断一律写明「缺上下文」，**不凭空举「稿子里的错」**（`SKILL.md:139`、`SKILL.md:160`、`workflow.md:127–128`）。作者不回话或只回「你看着办」→ 按最小改动处理并逐条列出假设（`SKILL.md:167`）。

### 输入③（越界改写）

> 「把这段重写得好一点」，未给方向与幅度。

保护分支：整段重写超出本 skill，需作者单独授权；授权后也**只做点名范围内**的有限改写，逐条记台账、不添事实、不把口语改书面语、不给意识流补主语（`SKILL.md:31`、`workflow.md:18`、`workflow.md:114–116`、`workflow.md:33`）。

三条均为 **DESIGN_EXAMPLE**（自创合成输入），只说明判法，不证明模型实际能做到。

---

## 三、R18 §4 六问表（本 skill 一张）

| 问 | 本 skill 的答案 | 成品位置 | 状态 |
|---|---|---|---|
| 1 触发：相近但不该用的请求，转给谁 | 七条负触发各有转介去向；重叠请求按「产物是文本还是卡／问题尺度是单元内还是跨卷／先用题材约束还是通用手法」三条分法 | `SKILL.md:25–33`（七条）、`SKILL.md:35–43`、`SKILL.md:181–188`、`examples/worked-example.md:83–95`（例三第 1 步逐条判，表在 85–93） | STATIC_CHECKED |
| 2 缺料：没给正文时会不会编造引文或已完成的动作 | 不会（规则上禁止）：缺原文只能要文字；只有一句时其余写「缺上下文」；台账「稿件证据位置」只指向用户当前稿件，无则填「未知」，且禁止把未知写成已完成 | `SKILL.md:139`、`SKILL.md:160`、`workflow.md:21–29`、`workflow.md:127–128` | STATIC_CHECKED |
| 3 冲突：版本、锁定内容、互斥要求由谁裁决 | 作者裁决。先排除「有条件而非冲突」的假冲突（`workflow.md:83–86`），真冲突立冲突卡（`workflow.md:90`）给 A／B 与代价，作者选定前一版都不落稿、只暂停该项其余照改（`workflow.md:91`）；作者已选过的不重复问（`workflow.md:92`）。作者有意保留的破格与不碰区（引文、专名、口头禅）优先于规则 | `workflow.md:81–92`、`SKILL.md:150`、`SKILL.md:162`、`workflow.md:20`（圈不碰区）、`examples/worked-example.md:121–130` | STATIC_CHECKED |
| 4 权限：分析会不会被当成允许改稿、写文件 | 已分开：审阅类请求只交清单不改稿；改动级别需作者定，整段重写超出本 skill；`agents/openai.yaml` 显式不授权且 `allow_implicit_invocation: false`；交付只给文本，不声称已写盘 | `SKILL.md:137–138`、`SKILL.md:31`、`agents/openai.yaml:2–3`、`agents/openai.yaml:8` | STATIC_CHECKED |
| 5 格式：模板字段与交付格式是否一致 | 有枚举可填模板且可逐项编辑：逐编号台账「编号｜值｜状态｜稿件证据位置」四列、编号独占一行、允许「未知」、表格必须有分隔行，符合 R18 §2a（非「列出即算完成」）。**但逐条清单在三处用了三套列名**，见 §五 缺口 G-1 | `workflow.md:21–29`、`examples/worked-example.md:103–116`、`SKILL.md:138`、`workflow.md:77` | STATIC_CHECKED |
| 6 消费者：声称的跨 skill 接口有没有真实提供方 | 有，双向都能实测到。本包引用七个兄弟名（preset-card 11 次、fiction-planning 8、scene 6、story 5、character 4、genre 3、cross-media 3）；反向 7/7 个包各有真实接收／转出行，非只提名字：`preset-card-generation/SKILL.md:39`「改具体稿子去 AI 味（产物是改好的文本，不是约束卡）→ line-editing」、`SKILL.md:82`、`character-and-narrative-control/SKILL.md:305`、`fiction-planning-and-diagnosis/SKILL.md:43`、`scene-conflict-and-rhythm/SKILL.md:284`、`story-architecture-and-longform-planning/SKILL.md:30`、`genre-fiction-craft/SKILL.md:28`。本包 §10.3 承诺「A 说转给 B，B 都要说接收什么」，与上述实测一致 | `SKILL.md:190–197`、`SKILL.md:199–206` | STATIC_CHECKED |

无 FAIL 项。**NOT_PROVEN 面**：六问全部只做了成品内静态核对，没有任何独立隔离回读或真实模型执行回执，因此每行只能到 STATIC_CHECKED，不能升为「已验证可用」。

---

## 四、本轮实测数字（可复核，非心算）

| 项 | 实测值 | 取数方式 |
|---|---|---|
| 包内文件数／行数 | 10 文件／1303 行 | `wc -l` 各文件相加 |
| 规则编号唯一集 | **56**（EN-01…EN-40 ＋ SR-01…SR-16，两端无缺号） | `grep -rEoh "(SR|EN)-[0-9]+" \| sort -u \| wc -l` |
| 审计词与状态码泄漏 | **0** | 全包 `grep -rEon "PASS\|FAIL\|NOT_PROVEN\|STATIC_CHECKED\|NOT_RUN\|DESIGN_EXAMPLE\|OBSERVED\|GQ[1-5]\|R1[78]\|BLOCKED\|NOT_APPLICABLE"`（R18 §2b、合同第二节） |
| 路由表两列（补读／出口） | 5 行×2 列全非空 | `SKILL.md:125–131` |
| 交付状态词 | 四词齐（已完成／依据／未能核实／待作者决定），「未知」为台账列合法值 | `SKILL.md:145–152` |
| 兄弟 skill 名出现在 description 要求 | 本包 §1.3 列出全部 7 个转介去向 | `SKILL.md:35–43` |

---

## 五、缺口与待裁项（本文件的主要产出）

- **G-1 逐条清单列名三套并存（一致性缺口）**：同一消费者视角的「逐条清单」在三处列名不同——`SKILL.md:138` 为 `位置｜原文｜改后｜依据｜风险或需作者确认`，`references/workflow.md:77` 为 `位置｜原文｜改后｜理由`（4 列），`examples/worked-example.md:119` 为 `位置｜原文｜改后｜依据｜复查`。三者语义上有交叠（依据≈理由；风险／需作者确认≠复查），但成品没有一行话说明哪个用于哪个产物，路由表也没区分。
  - 建议修法（**未动笔**，属成品改动且无席位议案）：统一为 SKILL.md 的五列，`workflow.md:77` 的「理由」改「依据」并补第五列；`worked-example.md:119` 的「复查」并回「风险或需作者确认」或在 §8.2 明确两种清单各自用途。
  - 归口：G00／W4 待裁清单（承 checklist §二十二 22.4 第 7 项）。
- **G-2 「每个编号独占一行」措辞歧义**：`workflow.md:21` 与 `examples/worked-example.md:105` 写「每个编号独占一行」，`workflow.md:27` 补的是「编号与规则一一对应，不合为一行」（禁止多个编号挤一行），但例三第 3 步 SR-10 出现**两行**（同一编号两条待办）。两种读法互相矛盾，实现者会犹豫。
  - 建议修法：措辞改「每条待办独占一行；同一编号可有多个待办，不得把多个编号并到一行」。归口同上。
- **G-3 无枚举模板目录**：本包没有 `templates/`，逐编号台账内嵌在 `workflow.md` 第 0 轮。按 R18 §6，无枚举模板的成果不要求空 spec，因此**不为本 skill 建 `delivery-preflight-spec/` 条目**；若作者要独立体例表模板，另立项再建。

---

## 六、后续怎么验证（G.2 第三句）

1. **用例已由 K2 装配**：`notes/quality/line-editing-and-proofreading/brief.json` 的四个用例即本节输入的静态对应物——`LE-T1` positive（800 字中文精修，期望走第 0 轮三件事＋按层改）、`LE-T2` missing（只有一句「帮我润色」，期望先问、不答则最小改动并列假设）、`LE-T3` conflict（「每句都更有力」对「保留方言口语和意识流」，期望先判负触发＋A／B 两版＋失败出口）、`LE-T4` boundary（英文对白只要拼写标点校对，期望只做机械层不碰风格）。
2. **判据先冻结再执行**：按 R18 §4 末段，四个用例的通过标准须在真实执行前冻结（当前 `brief.json` 仍是骨架，`requirements/capabilities/interfaces/applicability` 为空、GQ1–GQ4 全 `not_proven`、两个 SHA 为 null）。
3. **必须由非作者做**：K4 按 D3-C 由另派只读子代理**只看成品包、不看 notes** 做隔离回读，看得懂的地方记 EXTERNAL_NOTES_REFERENCE，出现来源／作品／项目名／包外路径的记违规；B.3 人工判断同样由非作者重做。本文件的 §三 六问是他们的对照表，不是他们的结论。
4. **GQ5 保持 NOT_PROVEN**：真实任务测试未获授权；本节 §二 的三条输入是设计例，不能当作收益证明。
5. **冻结前**：G-1／G-2 任一被判改则需重跑附录 B 全 11 类与本节 §四 全部数字，再冻结 `brief_sha256`／`skill_tree_sha256` 与整树 SHA。
