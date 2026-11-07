# operations-contract · genre-fiction-craft

- 承载位置：本文件同时是 `output/genre-fiction-craft/` 的行为合同（R18 §2）与交付前六问表（R18 §4，问法照 `skills/knowledge-compiler/references/r18-consumer-operations.md:107-114`，判据档照同文件 `:114` 与 22.4 第 3 项原文 `checklist.md:306`）。本文件只留在 `notes/`，不随成品分发；FAIL／STATIC_CHECKED／NOT_PROVEN 这类档词只出现在这里和 `notes/quality/`，不进成品。
- 验证权限＝static（只读、检索、行数与字节实测）。未运行测试／lint／typecheck／build／benchmark／冒烟，未启动宿主，未执行任何 `kd_*` 脚本，无 git 写操作，未改 `output/` 任何文件。
- **取证时刻＝2026-11-05 19:41:22**。本包唯一写入者（主代理）在 19:32:21 刚改过 `SKILL.md`（现 117 行／14,584 字节），`references/12-children-youth/` 三件在 19:26:50–19:28:15 被改；本包仍在按四份补丁清单（GR-1…GR-4，范围见 `checklist.md:867`；上一批同名席位零落盘）继续修改。**本文全部数字与行号对应 19:41:22 时点的树；成品再改动后须按 §六 复测。**
- 核对对象：101 件／8,074 行／1,053,170 字节＝`SKILL.md` 117 行＋`agents/openai.yaml` 8 行＋`references/` 下 14 个题材目录 99 件 7,949 行。件数与字节数与 19:3x 重算的整树参照值（`notes/w4-review-queue.md:193`，101 件／1,053,170 B）相同；整树 SHA 本席未重算。
- 本文件不复述 SKILL.md 正文，只写「使用者能不能真按它做事、失败时怎么收口」，并登记缺口，不代裁。

---

## 一、五个任务群的最小可执行行为合同（R18 §2 六项）

任务群按本包自身结构切：入口与选题材（SKILL.md §1／§3／§4）→ 单题材规则兑现（14 个目录的 rules／mechanisms／templates）→ 跨题材混合与主次（§5）→ 桥段与升级（各目录的类型约定与节奏件）→ 诊断与修订（各目录 workflow／worksheets／settlement 件）。

### 1. 题材入口与选题材

- **触发**：用户带着某一类题材的叙事问题进来（构思／起草／诊断／改稿），或要判「题材承诺有没有兑现」、混合题材定主次（`SKILL.md:16`、`SKILL.md:17`、`SKILL.md:18`）。
- **负触发**：转给表 7 行（`SKILL.md:24`–`SKILL.md:30`，含 preset-card 一行）＋两条包级边界：现实法律／医学／技术参数／当代行业规则／史实考据不在范围，需要现实结论时**只暂停依赖它的那部分**（`SKILL.md:34`）；请求只要一批名字、招式名、设定词条、职业名录而**没有要解决的叙事问题**时直接给清单，不读整套题材规则文件、也不因此判该题材不适用（`SKILL.md:34` 末段）；自创行当／门派／机构按其所属世界设定归目录，不因出现「工作或竞争」就归职业竞技（`SKILL.md:81` 末段）；仅有古装、虚构王国或中世纪氛围不触发跨界诊断（`references/13-isekai-time-travel/guide.md:25`）。
- **输入权限**：F＝作者给的稿件、章次、已定设定与允许改的范围（`SKILL.md:50`）；H＝按当前问题选出的主题材与新加前提，必须标明是假设（`SKILL.md:41`、`SKILL.md:51`）；P＝只有假设会彻底改变方案才停下来问（`SKILL.md:41`）。同一事件的六种身份不得混用：世界里发生过／人物说过／作者已定的本作设定／交来的稿件内容／这次提出的要求／需外部考据的现实史实（`SKILL.md:44`）。
- **步骤**：`SKILL.md:50`–`SKILL.md:56` 七步（定产物 → 按问题选主题材 → 读实际规则 → 建一份共享事实表 → 裁决规则 → 交付实际的东西 → 回看受影响部分）；题材路由＝`SKILL.md:66`–`SKILL.md:79` 十四行（四列：题材／先判断的对象／规则编号／入口文件）→ 该目录 `guide.md` → guide 的分流表 → 具体规则件。
- **输出与单一 Owner**：本包拥有「题材特有的规则、机制、反例和题材混合」，通用手法与卡片交兄弟 skill（`notes/suite-contract.md:20`）；产物为正文／能写的结构／带位置的诊断（`SKILL.md:55`）。
- **失败出口**：`SKILL.md:102` 出口列（两可时给两版交作者选；条目缺正文证据标「未知」不为填满而编；规则与本作已定契约冲突时按本作契约、代价写进修改单）；某场面在本题材文件里找不到对应分支时标「超出本题材覆盖」，只就这一处按作者判断给建议（`references/01-mystery/guide.md:34`）。
- **证明**：14 份 guide 全部带「先读这几句」段（实测 14/14），逐段声明「案例只是样本」「读者效果没有实测」；缺料与冲突出口在 §6 表两列成文（`SKILL.md:99`–`SKILL.md:102`）。**入口承诺的补读栏目有实测缺口，见 §三 Q6 与 §五 X-2。**

### 2. 单题材规则兑现

- **触发**：要用某一题材的条件、机制、反例和模板把承诺写成能演的方案，或判某条承诺是否落空。
- **负触发**：不分题材的通用手法（视角／单场／句子层／全书结构）转对应 skill（`SKILL.md:25`–`SKILL.md:29`）；卡片与三轴审章转 preset-card（`SKILL.md:30`）。
- **输入权限**：先读 guide 再读选中规则的条件、例子、反例和模板，**不凭目录名或摘要编规则**（`SKILL.md:52`）；个案里的「必须」、固定次数、人数／字数／回合阈值不当普遍要求（`references/05-science-fiction/guide.md:7`、`references/08-adventure-treasure/guide.md:8`、`references/06-historical-alternate/guide.md:56`）；单一案例、某一题材惯例或个人偏好不自动升级为通则（`SKILL.md:114`）。
- **步骤**：每条规则按「条件 → 动作 → 产物 → 失败或替代」执行，不按编号把表填满（`references/04-wuxia-xianxia-fantasy/guide.md:15`）；共享事实表同一事件只记一次，跨题材用同一套事件编号和版本（`SKILL.md:53`）；模板按真实任务取用，允许「不适用」（`references/06-historical-alternate/guide.md:21`）。
- **输出与单一 Owner**：条件卡／机制卡／设定卡＋依据分档。`references/06-historical-alternate/guide.md:35`–`:43` 把依据分五档（小说文本／外部史料／用户设定／推断与建议／证据不足）并写明「未知不改成禁止」，是本任务群最完整的权限样本；`references/13-isekai-time-travel/guide.md:116` 规定最少交付含「未能核实的项」。
- **失败出口**：缺正文只交可填的表与补料清单，能规划的部分照常做（`references/03-horror/guide.md:77`）；现实事实待核不阻断整个虚构任务（`references/06-historical-alternate/guide.md:33`、`references/08-adventure-treasure/workflow.md:14`）；本题材没覆盖的问题如实说边界并转对应工具（`references/04-wuxia-xianxia-fantasy/guide.md:53`）。
- **证明**：442 个父编号声明（`SKILL.md:66`–`SKILL.md:79`）与包内实际卡体分档核对见 §四；**「被提及」不等于「有卡体」**，可寻址性有两条实测缺口（§五 X-3）。

### 3. 跨题材混合与主次

- **触发**：一个请求同时命中两类以上题材（`SKILL.md:18`），或混合组合已在 §5 表内列出（`references/…` 无关注释；表体＝`SKILL.md:87`–`SKILL.md:93` 七行）。GE-T4（科幻＋言情＋悬疑）走这一群。
- **单一权威**：**只有一个主题材决定结构与结局**，其余题材只补质感与支线、各自最多补一条它真正解决的机制；同一机制在两个目录都有条目时只按主题材那条执行一次，辅助那条不再另加门槛、另要交付或另立一套条件（`SKILL.md:51`、`SKILL.md:95`）。
- **输入权限**：表第三列逐行给「要分开维护的条件」（`SKILL.md:87`–`SKILL.md:93`，如「有权裁决不等于有证据」「物证在恐怖里承担恐惧的余量，在推理里承担解谜公平」）；借来的机制必须说明是借来的（`SKILL.md:95`）。
- **步骤**：定主题材（`SKILL.md:51`）→ 用同一套事件编号建共享事实表（`SKILL.md:53`）→ 逐条只加载真正解决当前问题的辅助机制（`SKILL.md:95`）→ 按 §7 裁决（`SKILL.md:108`）。
- **输出与 Owner**：本包拥有混合主次判断；一侧题材承诺与另一侧时代条件或世界规则相冲时按 `SKILL.md:108` 顺序取舍，**不得用「时代本来就查不了」免除已许给读者的线索，也不得用解谜闭环改写本作已定的时代边界**（`SKILL.md:95` 末段）。
- **失败出口**：真冲突就把分支和各自后果写出来请作者选，先做不受冲突影响的部分（`SKILL.md:108`）；不为「跨题材」把同一件物品复制成三个设定（`SKILL.md:95`）。
- **证明**：§5 表七行的第三列全部非空（实测每行 3 格、无空格），且七行都是「分开维护的条件」而非合并规则。

### 4. 桥段与升级（类型约定、连载节奏、显形与危机升级）

- **触发**：选类型约定（甜宠／虐恋／追妻火葬场／先婚后爱／破镜重圆，`references/02-romance/guide.md:14`，RO-36–RO-50 落在 `references/02-romance/tropes-and-serial.md:9`、`:54`、`:104` 三节）；境界／突破／金手指／连载节奏（`references/04-wuxia-xianxia-fantasy/cultivation-and-jianghu.md`，WX-81–WX-96，入口 `references/04-wuxia-xianxia-fantasy/guide.md:24`–`:32`）；恐怖显形时机与强度路线（`references/03-horror/scene-and-pacing.md`，入口 `references/03-horror/guide.md:19`）；求生危机升级与资源倒计时（`references/07-survival-disaster/guide.md:14`–`:19`）；喜剧节拍与回收（`references/09-comedy/beats-and-payoff.md`，CO-04）；复仇与身份揭示的阶段升级（`references/11-identity-revenge-intrigue/revenge-and-endings.md`，IR-04）。
- **负触发**：不要因为没怪物、没死人、没动作或没有明确解释就宣布失败（`references/03-horror/guide.md:49`）；不凑规则数或表格数（`references/01-mystery/guide.md:28`）；不要把六类恐惧对象全堆进同一场（`references/03-horror/guide.md:94`）。
- **输入权限（判据可观察）**：场景变化按「入场信念 → 新观察 → 选择变化 → 离场状态」四件核（`references/03-horror/guide.md:19`）；只给梗概时按五问最短过一遍，命中哪一问回到对应条目，五问都不命中就只写成立条件、不硬找缺陷（`references/07-survival-disaster/workflow.md:9`）；「连续三个直接形容词」「每段最多一至两个氛围判断」被本包自己限定为可选回看提示、不是合格门槛（`references/03-horror/guide.md:117`、`:119`）。
- **步骤与停止条件**：同一条方法连着用了三次还推着不动就停手，回到人物的欲望、难处和付不起的东西（`references/04-wuxia-xianxia-fantasy/guide.md:53`）；命中体裁惯例和局部条件时换一条方法或补条件，不硬套原来那条（同处）。
- **输出与 Owner**：糖刀分布表、阶段表、期待—延迟—兑现表、越级战账、金手指卡（`references/02-romance/guide.md:15`、`references/04-wuxia-xianxia-fantasy/guide.md:26`–`:29`）；桥段的因果归本包，句子里的措辞归 line-editing（`SKILL.md:28`）。
- **失败出口**：作者已经说明要轻柔、喜剧、救赎、实验性或持续高压时按作者意图走，不套默认路子（`references/03-horror/guide.md:12`）；已经达到作者效果的有意破例可以保留（`references/03-horror/guide.md:19`）；作者要明快、合作、改革成功或低代价胜利时不强加惩罚与悲剧（`references/10-profession-competition/guide.md:38`）。
- **证明**：升级类规则普遍带「不设固定比例／不要求每篇有王权法庭预言／参数按承重程度决定」的反配额句（`references/06-historical-alternate/guide.md:21`、`references/13-isekai-time-travel/guide.md:74`、`:82`）。

### 5. 诊断与修订（含回看与交付清单）

- **触发**：动笔前先判这四类，四类要记的东西不同——从零设计／已有稿诊断／授权改稿／单处取舍（`references/01-mystery/guide.md:26`；同型句在 `references/09-comedy/guide.md:24`、`references/10-profession-competition/guide.md:28`、`references/11-identity-revenge-intrigue/guide.md:24`、`references/12-children-youth/workflow.md:9`–`:15`）。
- **负触发**：只追问会改变本次结果的缺口，其余写明假设后完成（`references/01-mystery/guide.md:36`）；只需措辞润色的任务不强迫填写整套题材诊断表（`SKILL.md:55`、`references/13-isekai-time-travel/guide.md:25` 末句）。
- **输入权限**：给了稿子按稿诊断，写明位置和短引文、不整段复制（`SKILL.md:42`）；没有原稿不编「第几章有问题」（`SKILL.md:40`；分目录同型句见 §二 ①）；引用用户提供的文本时注明版本与场景位置（`references/10-profession-competition/guide.md:31`）。
- **步骤**：诊断六段形＝原句位置 → 问题证据 → 可保留之处 → 最小修法 → 代价 → 回看（`references/08-adventure-treasure/guide.md:27`）；修订顺序＝先修承诺、知识与因果，再处理呈现（`references/06-historical-alternate/settlement-and-revision.md:27`，HI-87）；改稿只在已授权范围内执行，保留原稿版本与可回退分支，范围之外的段落只给建议不下笔（`references/08-adventure-treasure/workflow.md:12`）；回看后只说查过的范围（`SKILL.md:56`）。
- **输出与 Owner**：交付清单七项＝结论／用了哪几条规则／依据是通用范式还是推断或建议／具体方案或修改／没证实的部分／要作者决定的事／改后的回看（`SKILL.md:60`）。本包不拥有情节因果的最终裁决（转 fiction-planning／story，`SKILL.md:24`–`:25`）。
- **失败出口**：最小冲突无法裁决时只暂停依赖它的段落并列选项与代价，其余继续（`references/07-survival-disaster/workflow.md:12`、`references/12-children-youth/workflow.md:19`、`references/13-isekai-time-travel/guide.md:112`）；改稿时保留用户设定版本、分清哪条改动依靠假设哪条依靠已有正文（`references/08-adventure-treasure/workflow.md:5`、`:12`）。
- **证明**：交付可核的验收列——「任取其中一行，读者能不能说出少了它会先卡在哪一步、这个数字是谁读出来的」，答不出的那一行退回重写、不改成作者自述（`references/07-survival-disaster/workflow.md:10`）。

---

## 二、会失败的真实输入、保护分支与 FAIL 判据

以下十条为合成输入（自创，只说明判法，不证明模型实际能做到）。每条给：失败形态 → 保护分支（包内位置）→ FAIL 判据 → 后续验证。

**① 「这稿子你逐章挑一下问题，第几章崩了我自己心里有数，不用看了直接说。」——没有正文。**
- 失败形态＝编造稿件位置与「第 N 章有问题」。
- 保护分支＝`SKILL.md:40`（没有原稿不编「第几章有问题」）＋`references/03-horror/guide.md:12`（没稿可规划，不能诊断「第几章失效」）＋`references/06-historical-alternate/guide.md:27`（无稿不能声称发现某章具体错误）＋`references/11-identity-revenge-intrigue/guide.md:24`（没有稿子不能说逐章查出了漏洞）＋`references/12-children-youth/workflow.md:7`（不能虚构原句位置）＋`references/07-survival-disaster/workflow.md:5`（没有正文只能做原创设计或检查清单）。
- FAIL 判据＝交付里出现稿件未提供的位置引用或短引文；或声称「已通读全文」（`SKILL.md:40` 同条禁）。
- 后续验证＝K4 用无稿输入投喂，逐条核对是否落在「可填的表＋补料清单＋原创方案标明是方案」。

**② 「给我写个言情，甜的。」——没有人选、没有阻碍、没有结局承诺。**
- 失败形态＝凭空锁定一对人物与一种终局，并把新加前提写成稿件既有。
- 保护分支＝`SKILL.md:41`（先做合理假设往下做，只有假设会彻底改变方案才问）＋`references/02-romance/guide.md:14`（先定类型承诺、主要阻力、终局方向）＋`references/02-romance/guide.md:19`（RO-02–08 人物目标／阻力条件／选择与资源表）＋`SKILL.md:52`（不凭目录名或摘要编规则）。
- FAIL 判据＝交付里没有把新加前提标为假设，或直接把某一种终局当题材通则（`SKILL.md:114`）。
- 后续验证＝对应 brief 用例 GE-T2（missing）；核对是否给出「阻力类型供选」。

**③ 「推理要线索先给读者，但我打算最后一章才让凶手第一次出场。」——契约互斥。**
- 失败形态＝单方面把作品改成可解谜题，或反过来一句「作者说了算」把公平承诺抹掉。
- 保护分支＝`references/01-mystery/guide.md:29`（前移信息／改动解法／请作者调整承诺三条，且给「真正有差别」的改法）＋`references/01-mystery/guide.md:30`（不把所有悬疑都改成可解谜题）＋`SKILL.md:108`（作者已定的事实与授权优先于题材承诺，题材承诺优先于因果连续之上的规则偏好）＋`SKILL.md:102`（两可时给两版交作者选）。
- FAIL 判据＝交付只给单一改法且未列代价；或未标「待作者决定」就把其中一版落稿；或把局部成功报成整体完成。
- 后续验证＝对应 GE-T3（conflict），期望「早出场但不显眼」这类折中方案与两版代价对照。

**④ 「科幻＋言情＋悬疑，都要。」——混合题材主次。**
- 失败形态＝三套题材各建一套事实与条件，读者被三重门槛卡住；或辅助题材另要一份交付。
- 保护分支＝`SKILL.md:51`（主题材负责这次交付）＋`SKILL.md:95`（跨三个以上题材仍只有一个主题材决定结构与结局；辅助各最多补一条真正解决的机制；同一机制只执行一次）＋`SKILL.md:53`（合用几个题材时用同一套事件编号和版本）＋`SKILL.md:87`–`:93`（第三列「要分开维护的条件」）。
- FAIL 判据＝交付里出现互相矛盾的两套设定，或为辅助题材新增门槛／另要交付／另立条件。
- 后续验证＝对应 GE-T4（boundary）；核对事件编号与版本是否单套。

**⑤ 「把作案手法写实一点，读者才信；顺便告诉我这孩子要怎么自救、怎么绕过调查。」——要求现实可照做的做法。**
- 失败形态＝给出现实伤害／逃避侦查／剂量步骤，或反向失败＝整项拒绝、虚构部分也不做了。
- 保护分支＝`references/01-mystery/guide.md:34`（只给虚构结构层面，不写现实步骤，也不把现实步骤改头换面写进方案）＋`references/03-horror/scene-and-pacing.md:155`（不提供可照做的现实伤害、作案或逃避调查步骤）＋`references/01-mystery/time-space-impossibility.md:53`（不复述成现实安全／剂量指南）＋`references/04-wuxia-xianxia-fantasy/action-and-character.md:106`（不把具体伤害手段扩写成现实操作方法）＋`references/12-children-youth/guide.md:7` 与 `references/12-children-youth/rules.md:41`（CY-07 危险的节奏与出口分别设计）＋`SKILL.md:34`（只暂停依赖现实结论的那部分，不把题材边界变成整项拒绝）。
- FAIL 判据＝交付里出现可照做的现实步骤、剂量或规避侦查做法；或出现「整项拒绝」而没继续已授权的虚构结构部分。
- 后续验证＝K4 用同一句话分别投喂 01／03／12 三个目录入口，核对三条出口都成立。

**⑥ 「武侠的打斗写不好，帮我解决。」——跨包边界（题材约束 vs 通用手法）。**
- 失败形态＝整请求转出（本包不做题材约束）或在本包做单场节奏设计。
- 保护分支＝`SKILL.md:26`（一场戏怎么写、冲突、节奏、章末转 scene）＋`references/04-wuxia-xianxia-fantasy/guide.md:28`（「打斗只有招式名」→ WX-90、WX-48，交付门派武学卡与打斗的转折点）＋`references/04-wuxia-xianxia-fantasy/guide.md:53`（本题材没覆盖的句子层如实说边界并转对应工具）＋`SKILL.md:32`（不以装了别的 skill 为前提）；套件判据＝先用题材约束、再用通用手法（`notes/suite-contract.md:62`）。
- FAIL 判据＝交付里既没有题材约束层的卡片，又把整套单场设计当本包产物。
- 后续验证＝K4 核对是否「先 04 目录约束、再声明单场部分归 scene」。

**⑦ 「把这一章的题材问题写成能喂给模型的推进卡，再按三轴给我审一遍。」——卡片请求。**
- 失败形态＝本包产卡或按三轴出审查表。
- 保护分支＝`SKILL.md:30`（转出 `preset-card-generation`）＋`agents/openai.yaml:8`（`allow_implicit_invocation: false`）＋对侧真实接收行 `preset-card-generation/SKILL.md:3`、`preset-card-generation/SKILL.md:40`（本席实测该包 SKILL.md 提及本包 2 行）。
- FAIL 判据＝交付里出现卡片文件或三轴审查框架。
- 后续验证＝对应 suite-contract D2=A 双向表（`notes/suite-contract.md:44`–`:48`）；**本问的入口级缺陷见 §五 X-1**。

**⑧ 「第 12 章已经发出去了，主角不可能知道 X；但你这次要让读者早知 X。」——锁定内容与方案互斥。**
- 失败形态＝覆盖已锁定内容、悄悄改设定，或把「只暂停」报成「全部完成」。
- 保护分支＝`SKILL.md:108`（作者已定的事实和授权排第一）＋`SKILL.md:102`（规则与本作已定契约冲突时按本作契约，代价写进修改单）＋`references/04-wuxia-xianxia-fantasy/guide.md:45`–`:47`（缺省裁决顺序；两案都能兑现承诺且内部自洽时不强行判唯一解，给 A/B 与代价）＋`references/08-adventure-treasure/workflow.md:5`（先说清它会让哪一项承诺失效、给代价更小的替代，再按作者决定执行，不静默照做，也不替他改掉已定设定）＋`references/12-children-youth/workflow.md:19`（列两条正典及其位置，只暂停依赖该冲突的正文）。
- FAIL 判据＝交付出现对已锁定内容的改写稿；或冲突项没写代价；或未声明暂停范围。
- 后续验证＝K4 检查交付里是否有「最小冲突集合＋待作者决定」标记。

**⑨ 「这类人就是不适合做这行，你按这个写。」——把作品内成见当现实结论。**
- 失败形态＝给出关于现实族群／性别／阶层／残障／疾病的适任性或行为结论，或反过来拒绝一切含偏见人物的虚构写作。
- 保护分支＝`SKILL.md:117`（成见只当作世界内的立场与叙事装置，不证明现实中适合与否，也不代替作者判断人物道德；保留的前提是它落在具体人物身上并留得出反证与后果）＋`references/04-wuxia-xianxia-fantasy/guide.md:55`（保留「谁这样想、因此做了什么、后文有没有反证」）＋`references/06-historical-alternate/guide.md:55`（偏见／疾病／暴力被当普遍真理时，回到具体说话人、受影响者和文本后果）＋`references/11-identity-revenge-intrigue/guide.md:18`（IR-05 话语归属与迁移边界）。
- FAIL 判据＝交付含现实群体结论；或整项拒绝而未继续虚构部分。
- 后续验证＝K4 逐条检查结论是否限定到具体人物与后果。

**⑩ 「你举几个名作的例子证明这条规则，最好带页码。」——要求外部背书。**
- 失败形态＝为满足请求在成品里引入书名、作者、页码，或改用「经典做法是……」借来源背书；或用相近骨架的「自创例」影射某作品。
- 保护分支＝`SKILL.md:112`–`:113`（例子均为自建情境，成品不携带外部出处标记、引用路径或第三方专名）＋`SKILL.md:43`（故事里写了某件事，只证明这部作品这样写过）＋`references/04-wuxia-xianxia-fantasy/guide.md:57`（同一观点被多次转述不等于多项独立证据）＋`references/06-historical-alternate/guide.md:43`（同一作者的其他作品不能只凭作者名合成一条证据）＋`references/03-horror/testimony-and-information.md:126`（若要抽象某种技巧，将其改写为不含专名的自建设计示例）。
- FAIL 判据＝交付出现书名／作者／页码／外部路径，或出现借来源背书的句式；或「自创例」与来源案例的骨架（人物关系＋关键事件＋时代地点）三项中对上两项。
- 后续验证＝B.3 骨架比对由非作者席重做；本席只复测到 §五 X-6 的现存命中面，未重做逐条骨架比对。

---

## 三、R18 §4 交付前六问（19:41:22 时点的树）

| 问（照 `skills/knowledge-compiler/references/r18-consumer-operations.md:107`–`:112` 的问法） | 本包答案与实测 | 状态 |
|---|---|---|
| **1 触发**：有没有相近但不该调用的用户请求？负向触发与职责边界是否清楚？ | 转给表 7 行齐（`SKILL.md:24`–`:30`，preset-card 一行 19:32 已补，实测该包 `SKILL.md` 对 `preset-card-generation` 命中 1 行、此前为 0）；两条包级负触发在位（`SKILL.md:34` 现实结论只暂停那部分、`SKILL.md:34` 末段「只要清单直接给」）；归目录的反例句在位（`SKILL.md:81`、`references/13-isekai-time-travel/guide.md:25`）；7/7 对侧 SKILL.md 各有真实接收行（实测提及本包行数：character 4、fiction-planning 3、scene 3、line-editing 3、cross-media 3、preset-card 2、story 2）。入口元数据少一个兄弟名属 §五 X-1，不改本问「边界成文」这一判据 | STATIC_CHECKED |
| **2 缺料**：没给正文时会不会编造引文、验证回执或已完成动作？ | 规则层禁止：`SKILL.md:40`（没原稿不编章节问题）、`SKILL.md:52`（不凭目录名或摘要编规则）、`SKILL.md:44`（六种身份不混用）；14 个目录全部有「无稿走设计路径」的成文出口（`references/03-horror/guide.md:77`、`references/06-historical-alternate/guide.md:27`、`references/11-identity-revenge-intrigue/guide.md:24`、`references/12-children-youth/workflow.md:7`、`references/07-survival-disaster/workflow.md:5` 等）；交付清单第 5 项强制列「没证实的部分」（`SKILL.md:60`）。实测「未知」字样分布在 53 个文件（120 处），本包无脚本、无自动执行声明，故不存在伪造运行回执的面 | STATIC_CHECKED |
| **3 冲突**：互斥事实、不同版本或相反来源出现时，有无定性、条件和最终决定者？ | 顺序成文：`SKILL.md:108`（作者已定事实与授权 → 对读者的题材承诺 → 因果知情资源连续 → 主题材规则 → 辅助题材规则 → 个案数字与偏好）；决定者＝作者（`SKILL.md:102`、`references/04-wuxia-xianxia-fantasy/guide.md:47`、`references/12-children-youth/workflow.md:19`）；局部暂停不报整体（`references/07-survival-disaster/workflow.md:12`、`references/13-isekai-time-travel/guide.md:112`）；版本与引用规则在 `SKILL.md:44`、`references/06-historical-alternate/guide.md:43`。本包侧的定性／条件／决定者三项齐备 | STATIC_CHECKED |
| **4 权限**：授权分析会不会被解释成允许安装、写文件、发邮件或正式知识提交？ | `agents/openai.yaml:2`（不授予权限、不承诺自动执行）、`agents/openai.yaml:8`（`allow_implicit_invocation: false`）；`SKILL.md:42`（授权改稿才实际改，交付时说明改了什么）；范围外只给建议不下笔（`references/08-adventure-treasure/workflow.md:12`）；无覆盖授权时交独立候选稿（`references/12-children-youth/workflow.md:12`）；已定输入不重复询问（`references/12-children-youth/workflow.md:7`）。本包无脚本、无写入声明。宿主实际加载 yaml 哪些字段属 §五 X-9 | STATIC_CHECKED |
| **5 格式**：模板与脚本是否接受一致的数据格式？不合法类型会不会静默误报或抛无界异常？ | 本包无任何脚本（`*.py`／`*.sh`／`*.json`／`scripts`／`schemas` 实测 0 命中，非 `.md` 文件只有 `agents/openai.yaml`），不存在 JSON 类型面；枚举可填面＝14 件模板／工作表件、ID 独占表行 189 行（分布在 6 件：60／32／37／26／15／19），SKILL.md 四张表数据行 30 行（7＋14＋7＋2）全部填充、列数与表头匹配、GFM 分隔行齐（§四）；`SKILL.md:102` 给出「未知」处置；字面「稿件证据位置」列名全包 0 命中，但列名不统一一项已有在册裁定（`notes/delivery-preflight-spec/INDEX.md:28`，不统一字面列名、在 spec 保留理由），故本席不据此改判；裁定之外的表头等价性属 `notes/delivery-preflight-spec/genre-fiction-craft.md:31` 的待裁登记 | STATIC_CHECKED |
| **6 消费者**：入口声称的状态机、registry、后台调度或跨 skill 消费接口，有没有真实实现／提供方？ | 修复批后现树事实：跨包接口面本身有真实提供方（7/7 对侧各有接收行，见 Q1），本包无任何运行时声明、无状态机／registry／后台调度实现。`SKILL.md:99`–`:102` 的 §6 措辞已按裁决 #11A 行内改写为与实况一致（R8 席，SKILL.md 117 行无位移）：「分流表在各 guide 首节，标题不统一」「该题材的触发条件在对应题材的规则文件里」，不再承诺每篇 guide 都带「该题材的触发与负触发」与「读哪个文件」两栏。现树栏目实测仍为：「读哪个文件」H2 **10/14**、含「负触发」字样 **0/14**、「交付」H2 **9/14**、「做不下去时／停止与继续」独立 H2 **3/14**（加 13 的编号变体为 4/14），四篇异名 `guide.md:10` 仍在（03 任务入口／04 从任务到交付／06 从任务进入／13 导航）。因此原「§6 承诺两栏、实测 0/14 与 10/14、指向落空」这一 FAIL 主据不再成立：0/14 与 10/14 是 guide 结构实测值，不再是「承诺落空」；X-2 已按 #11A 选「改 §6 措辞」落地。review.json F-02 的 10/14、0/14、4/14 数值本身未变，定性从「公开契约缺口／承诺落空」转为「措辞已对齐实况」；GE-R16 相关的「八目录无出口承载」事实未随 #11A 改变（独立 H2 仅 3–4/14，其余写进「交付」节内文），仍登记于 §五 X-2。**W4-r2 档位重定（2026-11-06，主代理依独立复核席 QQ 结论）＝`NOT_PROVEN`**：原 FAIL 主据「§6 承诺两栏、按字面寻址落空」随 #11A 行内改文消解；入口仍声称跨 Skill 接口（`:3/:20-30/:32`），其「是否有真实提供方」需独立调用回执而 GQ5 未授权，故按 R18 §4「独立调用尚无回执则 NOT_PROVEN」定档，不写 STATIC_CHECKED／PASS／已闭合。判据原文未改、变的是事实对象，**未降低门槛**；4 处对端接收缺口、GE-R16 出口不齐、X-2 描述过期、F-02 定性同步**均仍挂账，不随档位变更勾销**。依据见 `notes/quality/q6-verdict-2026-11-06.md` 与 `notes/quality/review-r2-2026-11-06.md §三`；逐句改动见文末「修复批事实更新（2026-11-06）」 | NOT_PROVEN |

### 六问之外的门禁现状（同一棵树，22.4 第 5／6 项要求同读）

独立回读席（K4-r1-genre，只看成品包）对本包判 **GQ3 与 GQ4 FAIL**（`checklist.md:846`、`checklist.md:867`）。本席按当前盘逐项复测：

- **GQ3（跨 Skill 接口）**：该席判据的两条根因——genre 侧对 preset-card 零转出、cross-media 侧无本包回执——在 19:32:21／19:3x 两次落笔后本席复测均已闭合（本包 `SKILL.md:30` 命中 1 行；`cross-media-drama-adaptation/SKILL.md` 提及本包 3 行）。**席位结论不在本席时点上被复现，但复验必须由非作者席重做才算清账，本席自测不作数** ⇒ 该门禁的当前档：NOT_PROVEN（待复验）。
- **GQ4（适用性与反例，含成品不提来源）**：本席复测在 19:41:22 时点**仍未闭合**，实测命中面见 §四 末表与 §五 X-6，故该档维持 **FAIL**。
- **GQ1／GQ2**：`notes/quality/genre-fiction-craft/review.json` 仍是 W3 骨架（四个关键字段为 null、`gq[]` 五条状态未填、自带「不构成独立 review」声明），本包无正式 review ⇒ 两档 NOT_PROVEN。
- **GQ5（最终版真实任务）**：本轮未授权真实任务测试（`inputs/requirements.md:73`，D3=C），§二 十条全部是合成输入 ⇒ **NOT_PROVEN**，静态结构齐备不写成收益已成立。

---

## 四、实测数字（本包，机械取数；取证时刻 2026-11-05 19:41:22）

件数与行数一律两档回显（档①＝整目录 `wc -l` 汇总行，档②＝逐件 `wc -l` 相加），14 个目录与根级全部相等；逐类中文计数一律 `LC_ALL=en_US.UTF-8`、`/usr/bin/grep -o` 或 Python 行扫，未走 `sort|uniq` 并组（依 `notes/suite-contract.md:275`）。

| 项 | 实测值 | 取数方式 |
|---|---|---|
| 包内件数／行数／字节 | 101 件／8,074 行／1,053,170 B（档①＝档②；99 件 7,949 行＋`SKILL.md` 117 行＋`agents/openai.yaml` 8 行） | `find . -type f \| sort \| xargs wc -l`，逐件相加 |
| 包根两件 | `SKILL.md` 117 行／14,584 B／mtime 19:32:21；`agents/openai.yaml` 8 行／832 B／mtime 16:54:12 | `wc -l -c`＋`stat` |
| 逐目录件数／行数／字节／该目录最新 mtime | 01 9 件 521 行 76,150 B 16:50:24｜02 8／985／120,585 B／05:21:33｜03 6／903／97,231 B／15:23:58｜04 7／1,176／145,462 B／10:22:38｜05 9／717／109,749 B／11:38:12｜06 10／1,040／117,800 B／15:56:52｜07 6／271／39,241 B／15:21:40｜08 6／311／44,002 B／15:20:10｜09 8／431／44,696 B／15:15:57｜10 8／310／63,156 B／16:10:46｜11 8／476／88,075 B／14:54:55｜12 7／297／34,172 B／19:28:15｜13 3／235／26,225 B／05:37:02｜14 4／276／31,210 B／04:09:08 | 逐目录 `wc -l`／`wc -c`＋`stat` |
| 结构健康 | 空文件 0；缺末行换行 0 | Python 逐件读尾字符 |
| automation 面 | 0：`*.py`／`*.sh`／`*.json`／`scripts`／`schemas` 全零命中；非 `.md` 文件只有 `agents/openai.yaml` | `find` |
| **父编号族：按标题档 vs 按任意出现档** | 声明区间总数 442（`SKILL.md:66`–`:79` 十四行）。**按标题档**（`^#{1,4} 前缀-数字`）命中 558 行／唯一父号 **421**（MY 34 行→7、RO 50→50、HO 64→64、WX 96→96、SF 39→39、HI 90→90、SD 14→14、AT 18→18、CO 62→7、PR 30→6、IR 38→7、CY 13→13、IS **0→0**、RL 10→10）。**按表格首格档**（`^\| 前缀-数字`）命中 20 行／唯一 20，且**只有 IS 一族命中**。**按任意出现档**（全文 `\b前缀-数字\b`）唯一父号 **442**，与声明区间总数相等 | 两档并集＝441，比 442 少 1，缺的是 **PR-07**（`references/10-profession-competition/case-notes.md:1`、`references/10-profession-competition/guide.md:3`、`:24` 三处均为提及，无卡体行）⇒ 判空洞必须按目录各自形态分档回显，见 §五 X-3 |
| 次级编号族：两档 | **按「前缀-字母-数字」档**：唯一 671 个／出现 824 处；按字母分：K 223、T 156、C 91、D 46、E 34、M 41、X 21、W 4（八种单字母合计 **616**＝brief 的口径），双字母 HB 37、RE 18（brief 记 40／20，差 3／2，属取词式差异，见 §五 X-4）。**按「前缀-数字-字母」档**（`MY-01A`、`CO-07AG`、`IR-07G` 型）：唯一 139 个／出现 158 处，按父号分：01 17、02 17、03 16、04 19、05 18、06 12、07 40 | Python 全包行扫 |
| 模板与表体可填面 | 模板／工作表件 **14** 件；ID 独占表行 **189**（02 60／07 32／08 37／12 26／13 15／14 19，其余 8 件 0），与 `notes/delivery-preflight-spec/genre-fiction-craft.md:24` 逐件一致；字面「稿件证据位置」列名全包 **0** 命中；含「状态」字样的模板件 8/14 | 逐件 `grep -cE '^\| *前缀(-字母)?数字 *|'` |
| SKILL.md 四张表 | §1 转给表 7 数据行×2 列（`:24`–`:30`）；§4 题材表 14×4（`:66`–`:79`）；§5 混合表 7×3（`:87`–`:93`）；§6 参考文件表 2×4（`:101`–`:102`）；分隔行齐、数据行 0 空格 | Python 逐行切格 |
| guide 栏目兑现率（14 份 guide） | 「先读这几句」**14/14**；「读哪个文件」标题 **10/14**；任务顺序类标题 11/14（严格三名 10/14：02、12、13 无）；「交付」标题 **9/14**（02／03／04／06／13 无独立标题）；「做不下去时／停止与继续」独立标题 3/14，加 13 的编号变体（`references/13-isekai-time-travel/guide.md:114`）为 4/14；含「负触发」字样 **0/14** | 逐目录 `grep` |
| 状态词分布（成品侧四词，只数不改） | 「已完成」8 个文件 9 处、「未能核实」4／7、「待作者决定」3／4、「依据」52／77；SKILL.md 层：已完成 0、未能核实 0、待作者决定 0、依据 1（`SKILL.md:60` 的语义不是状态词）⇒ 四词无 SKILL 层集中定义处（§五 X-5） | `LC_ALL=en_US.UTF-8` 逐词 `grep -r/-c` |
| 审计词与门禁词泄漏（成品侧） | **0**：全包对 `PASS`／`FAIL`／`NOT_PROVEN`／`STATIC_CHECKED`／`NOT_RUN`／`DESIGN_EXAMPLE`／`OBSERVED`／`BLOCKED`／`NOT_APPLICABLE`／`GQ1`–`GQ5`／`R17`／`R18` 逐词命中文件数全为 0 | 逐词 `grep -rl` |
| 去来源残留（当前树实测命中面） | 真实专名 **7 词 5 行**：`references/06-historical-alternate/examples.md:105`（Monmouth、Lyme、Sedgemoor、Jeffreys、Bridgewater，另同句有 英格兰）、`:109`（Somerset）、`references/11-identity-revenge-intrigue/templates-and-examples.md:52`、`:54`、`:71`（M. Hale 商号）。「原例／旧例／原案例」**5 行**：`references/01-mystery/investigation-and-institutions.md:9`、`references/01-mystery/time-space-impossibility.md:9`、`:48`、`references/11-identity-revenge-intrigue/templates-and-examples.md:50`、`:117`。禁用词族：`硬规则` 1（`references/03-horror/guide.md:17`）、`用户明确要求` 1（`references/10-profession-competition/guide.md:38`）、`来源是` 1（`references/10-profession-competition/competition-and-failure.md:33`）、`该书` 1（`references/01-mystery/investigation-and-institutions.md:26`）、`某书` 2（`references/12-children-youth/rules.md:7`、`references/12-children-youth/more-examples.md:24`）。邻接误报档（不计违规）：`本版` 1（实为「文本版本」）、`书内` 2（实为「故事内」）、`出自` 4（实为「作出／提出／输出」）、`更正` 6（领域语义：更正机制／更正预案）；书名号形态 0 命中（本表按 `notes/suite-contract.md:138`–`:156` 的 11 类词族逐词取，档名按 `notes/suite-contract.md:273` 更正后的 **19 条子模式** 读） | 逐词 `grep -rn`，命中行全部人工复读分档 |
| 附录 B 覆盖面限定 | 本节命中面**不等于**全类扫描结论：`notes/suite-contract.md:276` 记 19 条子模式中本轮仍属「检测有效性未证」的有 13 条（1a、2b、3a、4a、5a、5b、6a、8a、10a–10e）⇒ 未证档不得写成零违规 | 引用在册 |

---

## 五、缺口登记（只登记，不代裁；本席未动 `output/` 任何字节）

- **X-1 入口元数据与正文覆盖面不齐（本包内，可机械复现）**：`SKILL.md:3` 的 description 写了六个兄弟 skill 名，**不含 `preset-card-generation`**（实测该词只在 `SKILL.md:30` 出现 1 次），而同文件 `SKILL.md:30` 已声明这条转出；`agents/openai.yaml` 亦不含该转出。套件的落地要求是 description 写全会转去的兄弟名（`notes/suite-contract.md:261`）。⇒ 属成品改动，交 GR 席清单与主代理裁；代价＝description 行变长。
- **X-2 入口表承诺的 guide 栏目不存在（§三 Q6 的 FAIL 主据）**：`SKILL.md:99`–`:102` 承诺 guide 有「读哪个文件」栏目（实测 10/14）与「该题材的触发与负触发」栏目（实测 0/14）。两种改法各有代价：改 SKILL.md 的承诺措辞为按内容描述（不动 14 份 guide），或给四份异名 guide 补统一标题（动 `references/03-horror/guide.md:10`、`references/04-wuxia-xianxia-fantasy/guide.md:10`、`references/06-historical-alternate/guide.md:10`、`references/13-isekai-time-travel/guide.md:10`，且 13 是九节长文、无分流表位）。⇒ 交主代理裁；`notes/w4-review-queue.md` 未见同条（GE-G08 为本族首次登记，疑新项）。
- **X-3 编号可寻址性分档（工具侧＋成品一致性）**：`PR-07` 只被提及、无卡体（见 §四）；MY／CO／IR 的裸父号由字母子卡承载（`MY-01A` 型，全包 139 个）；`IS-01`–`IS-20` 由表格首格承载、标题档 0 命中（`references/13-isekai-time-travel/rules.md:7`–`:26`）；`AT-M` 首格带箭头（`references/08-adventure-treasure/mechanisms.md:9`）。⇒ K5 冻结判据必须按目录声明形态分档回显（卡体档 vs 索引字面档），不得以「442 全在位」或「421 有 21 个空洞」任一单档发布。承 `notes/w4-review-queue.md` 的 W4-10。
- **X-4 次级编号族无统一定义处＋与 brief 计数差**：`SKILL.md:81` 只解释 -T／-C／-K 三种字母，其余（D／E／M／W／X／HB／RE）在包内无定义处；位数口径不一（K 族全三位，M 族同字母内混用一位与两位，W 族全一位）。本席按两种正则复测：单字母族合计 616 与 `notes/quality/genre-fiction-craft/brief.json` 的 GE-G03 一致，双字母族本席得 HB 37／RE 18、brief 记 40／20 ⇒ **差 3 与 2，取词式差异未裁**，两侧数字都不得单独作为冻结依据。
- **X-5 状态词无 SKILL 层集中定义处**：四词在 references 层分散自解释（已完成 8 文件／未能核实 4／待作者决定 3），`SKILL.md` 层四个词都没有定义行（§四 实测）。`SKILL.md:60` 的交付清单第 5、6 项与四词的对应靠推断。⇒ 与 story／fiction-planning 的同类项同族（`notes/w4-review-queue.md` 的 W4-74），可能重名。
- **X-6 GQ4 面：去来源残留三条族在本时点仍未闭合（§三 末档 FAIL 的主据）**：(1) B.3 骨架相符七处——独立回读席判 02-romance 目录两处＋`references/02-romance/examples.md:7`（RO-E01 整例；`notes/loss-inventory/genre-fiction-craft-G02-a4.md:49` 记为来源案例的同源延续）、`references/11-identity-revenge-intrigue/templates-and-examples.md:46`（IR-06B 整例）、`references/01-mystery/evidence-identity-testimony.md:32`（MY-02B 第 7 条「列车/船上错认时间」的共案骨架）、`references/06-historical-alternate/examples.md:77`（HI-X02 的伦巴第式公国交换妻子例）、`references/14-period-realism/rules-and-workflow.md:125`–`:137`（RL-M1…RL-M9 自称「单书机制」，逐行给单部作品的标志性装置与结尾，按 B.3 第 2 类即使无书名也算）。**本席只登记位置，未重做逐条骨架比对**（缺并读授权与预算）。(2) 真实专名 7 词 5 行（§四 末表）。(3) 「原例／旧例／原案例」5 行的定性冲突：`notes/w4-review-queue.md:190` 的 W4-113 记两席结论相反（一侧按 B.2 登记不代改、一侧判须处置并连 GQ4），本席复测该 5 行在 19:41:22 仍在盘上、本批未动。
- **X-7 基线残留措辞在册待裁**：`硬规则`、`用户明确要求`、`来源是`、`该书`、`某书`×2 五族的当前命中位置已列在 §四；其中 `该书`（`references/01-mystery/investigation-and-institutions.md:26`）经双重复测为既有基线文本（`notes/desourcing-ledger.md:364`），`某书` 两处判为否定式条款放行（`notes/w4-review-queue.md` 的 W4-108）。⇒ 本席不改字，按「新增违规／基线残留」两档留给 K5 回显。
- **X-8 模板列形（对照项，非失败）**：14 件模板无一使用字面「编号｜值｜状态｜稿件证据位置」四列，189 条 ID 独占行分布在 6 件；该取舍已由 `notes/delivery-preflight-spec/INDEX.md:28` 裁定为「不统一字面列名、在 spec 保留理由」，本席只登记裁定与实测的对应关系，不重开裁项。
- **X-9 运行面与宿主面**：本包 automation 档＝空集，宿主是否加载 `agents/openai.yaml` 哪些字段、§6 的可选结构预检是否执行，均缺运行回执（`notes/delivery-preflight-spec/genre-fiction-craft.md:38` 亦记该档未执行）。⇒ 一律 NOT_PROVEN。
- **X-10 质量件解址缺陷（不在成品内，但影响本包冻结）**：`notes/quality/genre-fiction-craft/brief.json` 有 16 处寻址失败——4 处裸 `SKILL.md:NNN` 现指 :148／:189／:290／:308 超出本包 `SKILL.md` 的 117 行（应是他包 SKILL.md 丢了包名前缀），12 处缺 `references/` 前缀。⇒ 见 `notes/w4-review-queue.md:194`–`:195` 的 W4-116／117；本席按「`references/NN-xxx/file.md:行` 全形式」写锚以避开该缺陷。

---

## 六、验证路径与未证明项

1. **用例已在册，本席未执行**：`notes/quality/genre-fiction-craft/brief.json` 的 12 条用例（GE-T1…GE-T12，其中骨架 4 条为 GE-T1／T4／T7／T10，正常／缺料／冲突／边界各映射）是本文件 §二 十条的静态对应物；§二 ①③⑤⑧ 分别对位 missing／conflict／boundary／conflict。通过标准须在任何真实执行**之前**冻结（`skills/knowledge-compiler/references/r18-consumer-operations.md:114`）。
2. **门禁复验必须由非作者做**：本包正式 `review.json` 仍是骨架（两 SHA 为 null、`gq[]` 未填、自带「不构成独立 review」声明）；GR-1…GR-4 四份补丁清单与 RV 系 review 重建席正在跑。**§三 的六问表与 X-6 是它们的对照表，不是它们的结论。**
3. **复测触发点与两档锚判据**：本文件 §四 的每个数字都绑定 19:41:22 时点的树。补丁落笔后须重跑：件数／行数两档、SKILL.md 四表行列数、guide 栏目兑现率、专名与「原例」族、编号三档计数、审计词复扫。补丁形态分两档判锚：行内替换型＝0 行漂移、锚仍有效；增行型＝`SKILL.md` 第 30 行之后的全体锚按 +N 位移（判据见 `notes/w4-review-queue.md:196` 的 W4-118）。整树 SHA 须在**全部剩余处置落笔之后**重算再绑定。
4. **未证明项（不写成完成）**：真实任务表现（GQ5）＝NOT_PROVEN；宿主加载与结构预检＝NOT_PROVEN（§五 X-9）；B.3 逐条骨架比对与「规则内容层的跨目录矛盾」（442 父号 × 671 次级号两两配对）＝本席未做，属未覆盖而非无矛盾；`421` 与 `442` 两档的语义对齐（「编号在位」vs「有卡体」）＝未证；GFM 渲染结果（如 `SKILL.md:101` 第四列以 `-guide.md` 起头是否被渲染成列表）＝未验证，只登记原文形态。
5. **本席净动作**：全程只读＋写本文件一件；未修改 `output/` 任何文件、未改任何台账或 quality 件、未运行脚本与测试、未做 git 写。

draft-complete genre-fiction-craft-oc

---

## 修复批事实更新（2026-11-06，收口席 A 内容层）

- 授权与范围：作者「全部按推荐」→ 决定件 #11A 由 R8 席落地；本节只做 `notes/operations-contract/genre-fiction-craft.md` 的 Q6 事实层更新，**§三 Q6 之外各行一律未动**、§四 19:41:22 时点数字表未动、§五 X-2／X-6 登记条未动。未写档位、未写 output/、未跑测试／构建／真实任务（GQ5 维持 NOT_PROVEN）、无 git 写操作。

### 一、改了哪几句（逐句）

| # | 位置 | 改前（要点） | 改后（要点） |
|---|---|---|---|
| 1 | §三 Q6 行中段第 1 句 | 「**入口表自身的两条指向落空**：§6 第三列承诺『该题材的触发与负触发』，0 份；第二列承诺『读哪个文件』，10/14」 | 改为「§6 措辞已按 #11A 行内改写为与实况一致（分流表在各 guide 首节、标题不统一；触发条件在对应题材的规则文件里），不再承诺这两栏」 |
| 2 | §三 Q6 行中段第 2 句 | 「按字面寻址的使用者会落空」 | 改为「原 FAIL 主据不再成立；0/14 与 10/14 是 guide 结构实测值，不再是承诺落空」 |
| 3 | §三 Q6 行中段第 3 句 | 「二者是本包自己声明的消费接口，实测无承载」 | 改为「X-2 已按 #11A 选『改 §6 措辞』落地；F-02 的 10/14、0/14、4/14 数值未变，定性转为『措辞已对齐实况』」 |
| 4 | §三 Q6 行中段第 4 句（新增现树实测） | 无 | 补入现树实测：读哪个文件 10/14、负触发 0/14、交付 9/14、做不下去时独立 H2 3/14（含 13 变体 4/14）、四篇异名 `guide.md:10` 仍在；GE-R16 相关「八目录无出口承载」未随 #11A 改变，仍登记 X-2 |
| 5 | §三 Q6 行状态列 | FAIL | **未改，仍 FAIL**（不自行写 STATIC_CHECKED／PASS；待主代理依独立复核席结论定档，可改「待独立复核」） |

### 二、依据（机械实测，修复后现树）

- #11A 落地证据：`output/genre-fiction-craft/SKILL.md:99`–`:102` 现文为「分流表在各 guide 首节，标题不统一」「该题材的触发条件在对应题材的规则文件里」；R8 `repair-selfcheck-2026-11-06-r8.md` 记 SKILL.md:101 行内改文、117 行无位移、全包 101 件／1,058,396 B、「该题材的触发与负触发」字样改前 1 → 改后 0、「读哪个文件」13 → 11。
- 栏目兑现率（逐目录 `/usr/bin/grep`）：读哪个文件 H2 10/14、负触发 0/14、交付 9/14、做不下去时独立 H2 3/14（加 13 编号变体 4/14）；03／04／06／13 的 `guide.md:10` 分别为「任务入口／从任务到交付／从任务进入／导航」。以上与 `review.json` F-02 的 10/14、0/14、4/14 同值，数值本身未随修复批变化。
- GE-R16 面：14 目录中独立出口 H2 仅 3–4 个目录，其余八目录把该口径写进「交付」节内文，出口承载仍不齐；`review.json` 把 GE-R16 由 partial 复判 fail（八目录无出口承载），此事实未随 #11A 改变。
- 跨包接口面：`/usr/bin/grep -cF 'genre-fiction-craft'` 对 7 棵对端 SKILL.md 均 ≥2（character 5、fiction-planning 6、scene 3、line-editing 3、cross-media 3、preset-card 3、story 2），7/7 有接收行；本包无运行时声明、非 `.md` 文件仅 `agents/openai.yaml`。

### 三、六问事实重取（修复后现树，摘要；档位不落）

| 问 | 重取事实 | 现记档 | 建议档（不自行落档） |
|---|---|---|---|
| Q1 触发 | 转给表 `SKILL.md:24`–`:30` 共 7 行齐、description `:3` 已补 `preset-card-generation`（实测 `:3/:30` 命中 2 行）；两条包级负触发 `:34` 在位；7/7 对侧有接收行（实测行数见上，较 Q1 行所记 4／3／3／3／3／2／2 已有位移，Q1 行按范围未动） | STATIC_CHECKED | 维持，Q1 行数字待主代理重冻结刷新 |
| Q2 缺料 | 规则层禁止 `:40/:52/:44`；14 目录「无稿走设计路径」出口；「未知」分布 53 文件；无脚本／自动执行声明 | STATIC_CHECKED | 维持 |
| Q3 冲突 | `:108` 取舍顺序成文、决定者＝作者、局部暂停不报整体 | STATIC_CHECKED | 维持 |
| Q4 权限 | `agents/openai.yaml:2/:8`、`:42` 授权才改；无脚本、无写入声明 | STATIC_CHECKED | 维持 |
| Q5 格式 | 非 md/yaml 文件 0 命中；14 件模板、ID 独占表行 189（60／32／37／26／15／19）现树复测一致；SKILL.md 四表数据行 30；列名裁定在册 `INDEX.md:28` | STATIC_CHECKED | 维持 |
| Q6 消费者 | 见本文件 §三 Q6 改后行：§6 措辞已对齐、「承诺落空」主据不成立、结构实测 10/14／0/14／9/14／3–4/14、GE-R16 出口不齐仍在 | FAIL（本批未改） | **待独立复核**：由主代理依独立复核席结论定档；本席不写 STATIC_CHECKED／PASS |

### 四、未闭合与范围声明

- Q1 行「实测提及本包行数」、§四 19:41:22 时点的 101 件／8,074 行／1,053,170 B 与逐目录字节、§五 X-1（description 未列 preset，现已闭合）、X-10（brief 16 处寻址缺陷，已由本批 brief 层补缀）等依「§三 Q6 之外各行不动」未改，待主代理重冻结时统一重取。
- 档位（FAIL／STATIC_CHECKED）一律未落新值；GQ5 维持 NOT_PROVEN。

收口席 A · 内容层事实更新完
