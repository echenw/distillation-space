# BUILD-REPORT-part2.md — 05-genre-fiction-craft（构建 B：落盘核验与差异面闭合）

构建 key：`05-genre-fiction-craft-B`。日期：2026-11-01。
写入范围（按作业边界）：`results/candidates/05-genre-fiction-craft/`（独占）+ `fusion/audit/full-lineage/05-genre-fiction-craft/disposition-addendum.json` + 本报告。未改动 distill/、fusion/skills/、history/、results/skills/ 及其他 Skill 的候选目录；无 git 写操作。

## 0. 本部分职责与接续关系

构建 A 已产出候选目录骨架（发行版 96 文件整树复制）+ BUILD-REPORT.md（含 44 条 UNRESOLVED 处置总表、addendum 51 条登记）+ `disposition-addendum.json`，**但其 §3 登记的 8 处 RESTORE 与 §5 登记的 1 处自缺陷修复（V08）均未写入候选文件**（本会话逐文件 diff 实测：11 个拟改文件与发行版逐字节相同）。本部分（B）做三件事：

1. **逐条独立复核 44 条 UNRESOLVED**：每条打开 distill 来源原文（只读）与母版/发行版正文比对，不凭编号或标题判定承接（§1 逐条证据表）。
2. **把账本已登记、但未落盘的全部编辑实际写入候选树**（§2 落盘清单），并核实差异面恰为登记面。
3. **全树自缺陷扫描**（重点 references/08–14 与全树）：悬空链接、悬空规则编号引用、占位符、绝对路径、断裂标点/粗体（§4）；外加对 addendum 的一处文件指认勘误（§3）。

## 1. 44 条 UNRESOLVED 逐条复核（本会话实读来源原文 + 母版/发行版正文）

处置不变量与构建 A 相同：**RESTORE 8 / CONFIRMED_COVERED 35 / INTENTIONAL 1**。下表每条给出本会话实读的来源位置与承接/写入位置。星号 * = 承接位置在发行目录 08/13（候选未改，正文已承载）。

| id | 来源（distill，本会话实读） | 处置 | 承接正文（母版/发行版实读）或写入位置（候选） |
|---|---|---|---|
| G5-K002 | 05-科幻/批次-01 sci-fi-future-plot-forge/references/mind-war.md §2 永久物质化（Lothar 幻影战马；Karth 创造权；密度→时长→自主性三段） | CONFIRMED_COVERED | knowledge-details.md K001：「幻象持久、自我再造与自治分别是该世界的条件，不推出想象密度决定寿命的公式」——三段公式被母版正文显式裁决不承 |
| G5-K005 | 同上 mind-war.md §5 欺骗工程（示弱三连/定时立威/双酬合规） | CONFIRMED_COVERED | K004：「反复弱点、尺寸/时机威慑和同时满足两套规则可以组织智胜；出现一次已足够建立时无须凑三次」 |
| G5-K013 | 同上 identity-infiltration.md §3 潜伏工程（同化反函数/泄密时钟/死信箱/提前自首/假死/媒体钓饵/假在场/蓝图对位） | CONFIRMED_COVERED | K012+K013+SF09（死信箱→单向联络、提前自首→自首小罪、媒体钓饵→诱饵报道、假在场、复制图纸缺陷、同化/暴露累积条件化） |
| G5-K018 | 同上 history-time.md §3 末日前置叙事（结局先行/末日清单/洁净死讯/课程预演） | CONFIRMED_COVERED | K017：「先给终点再追『如何到此』、早见铭文后解码、旧世界怨情清单、灾前排演与真正灾难的情绪差」 |
| G5-K022 | 同上 expedition-combat.md §3 资源双刃律+求生包 | CONFIRMED_COVERED | K022（水火洞穴既供生存也可能吸引危险；水粉/营养片/计时器/自毁胶囊=旧故事装备）+K023（预期的暗与静支持推断=黑暗证明/无声定理） |
| G5-K024 | 同上 society-love-craft.md §1 制度双引擎（环境塑德/荣誉替代/恐惧治理/布道代言+追问悬置） | **RESTORE** | 环境塑德律 grep 母版/发行版零命中→已写入候选 K025（见 §2-1）；其余三律 K025 既有 |
| G5-K042 | 05-科幻/批次-02 sci-fi-novum-world-forge/references/alien-contact.md C4-2 沟通阶梯 | **RESTORE** | 阶梯本体 K041 已承；「最关键的信息放在最难沟通的一层」grep 零命中→已写入候选 K041（§2-2） |
| G5-K050 | 同上 institution-detail.md C7-3/7-5/7-6（蝴蝶效应/孤独惩罚/揭发通道） | CONFIRMED_COVERED | K052（局部选择汇成陷阱…不强制无所不知反派=不做大老板）+K053（孤独比死更坏是人物偏好）+K054（角色转而公开暴露制度） |
| G5-K054 | 05-科幻/批次-03 scifi-future-craft-b03/SKILL.md R2 运作三联（谁做/多久一次/做不成会怎样；三格填满才进正文） | **RESTORE** | 例已承 K057（斧必有锤是角色推断）；「三问」grep 零命中→已写入候选 fused-rules.md SF10（§2-3）；硬门槛「填满才许进正文」按母版配额清理降为条件化 |
| G5-K065 | 05-科幻/批次-04 science-fiction-craft-b04/references/novum-and-rules.md R14/R17（反转只改意义/道具一物三用） | CONFIRMED_COVERED | SF18（提前提供足以支持关键转折的事实…不设出现两次配额）+K068（铝弹排水量等回溯前提）+SF19（道具能从货物变藏身处再变证据，但不必一物三用）+K069（赤铁矿货物→假血→录音载体） |
| G5-K078 | 05-科幻/批次-05 science-fiction-conceptual-reveal/references/04-cognitive-framing.md R4/R5 | CONFIRMED_COVERED | SF20+K097（变化概念失传等例）+SF21（无100词阈值；何时暴露局限取决于信息合同）+K098（框架参与揭示） |
| G5-K080 | 05-科幻/批次-05 同上 06-failure-modes.md R7 五类失败 | CONFIRMED_COVERED | K101 五例全承（自袭后再解释/四轮逃亡/煤层冰层讲座/以为带鲸/导语先说陪伴者）且保留「是否失败是编辑假设」边界；K095 承导语预告 |
| G3-K006 | 02-言情/批次-01 romance-social-cost-craft/references/02-social-cost-rules.md Rp6 长期等待计价 | CONFIRMED_COVERED | RO17（时间可改变工作、家人、财富…记录期限）+K008（同锚：神前已婚/旁人称疯狂/职业漂泊）+examples「不要求每半年机械重算」=硬性计价显式条件化 |
| G3-K019 | 02-言情/批次-02 courtship-conflict-craft/references/01-courtship-engines.md R5 退出权双向条件 | CONFIRMED_COVERED | RO15（当下愿意、能否拒绝、能否离开…实际替代选择；形式同意不能自动解除强迫）+K034（同锚 PG3321 八行号全保留）+K027；「接收端四项缺一标 UNKNOWN」的检测语义由 RO15+RO12 合并承载 |
| G3-K028 | 02-言情/批次-03 romance-emotional-arc/references/01-refusal-and-vow.md R1 拒绝宣言 | CONFIRMED_COVERED | K045（不结婚宣言例）+K060（公牛事故「区分事件解围和意愿成立」=宣言被事故推翻的反例承接）+RO19（800字门槛显式撤销） |
| G3-K031 | 同上 03-reversal-and-vacancy.md R5 空缺逆转 | CONFIRMED_COVERED | RO18 离场和空位+K051（井边等待/整年空位，同锚）+K060；「≥1/5 篇幅」硬比例显式撤销（RO18「不必在固定章节比例退出」） |
| G3-K053 | 02-言情/批次-05 romance-obstacle-delay-craft/references/rules-obstacle-delay.md R3 清白危机第三方解套 | CONFIRMED_COVERED | K094（Palmyre 还帽道歉与希望女士拜访；可以有交换也可以出于关心）+K095（所有谣言都显得可信而真话不可思议=「truth only is incredible」同锚）+RO12 |
| G3-K065 | 02-言情/批次-07 romance-craft-b03-b07/references/obstacle-and-refusal-playbook.md 拒绝三层 | CONFIRMED_COVERED | RO16「礼节、理由和动机自陈是可选表达层」=D23/D24/D25 修正逐字承接；K144/K145/K146 三层例+两动作（先说出对方正在求婚；离场后评价） |
| G4-K006 | 04-武侠/批次-01 speculative-wuxia-fantasy-craft/references/02-artifacts-taboos-and-trials.md F04 禁忌三段 | CONFIRMED_COVERED | F13（写禁令填…违反后的实际变化）+T05 模板（实际收益/代价/痕迹）+C15 七衣痕迹例+模板映射行「撤前二利/第三罚」显式撤销硬三段 |
| G4-K007 | 同上 F05 试炼交底 | CONFIRMED_COVERED | F12（公开/隐藏目标、裁判权限、失败后果、可退出/申诉、任务是否会追加；承诺公平终点再临时加题才须解释失信=终局条款）+C05（追加本身成为制度冲突）+F38（工匠账单=物证/工匠/公开验证）+T07 |
| G4-K010 | 同上 03-price-identity-and-names.md F08 身份三重验证 | CONFIRMED_COVERED | F33（PG1599 鞋及另一只鞋=材质+公开匹配；「无须三证」显式撤销）+T08（物件/配对/身体/知识列）+F37（信物经侍者传递=第三方之手） |
| G4-K012 | 同上 F14 名号由事件产生 | CONFIRMED_COVERED | 收束与表达 F72（后来谁如何命名/使用/误解；被接受命名、自选名字、侮称重新认领都可成立；不要求名称必须他人授予或只在结尾公布）+F36 |
| G4-K014 | 同上 04-institutions-rumor-and-antagonists.md F13 群体转变行为链 | **RESTORE** | 四环（劳动/交谈/互助）已承 F29（同锚）；「替代行为等价出口」grep 零命中→已写入候选 F29（§2-4） |
| G4-K015 | 同上 F15 传闻造物 | **RESTORE** | 密谈造权已承 F30（耳语变名声/伪怪物传言）；传闻怪物五拍弧线与舆论包装 grep 零命中→已写入候选 F30（§2-5） |
| G4-K018 | 同上 05-prophecy-contracts-and-endings.md F19 组织等价物 | **RESTORE** | 帽色/数字/口令已承 C28（同锚）；「家用物入会兼顾神圣与喜剧」grep 茶壶/法冠零命中→已写入候选 模板与案例.md C28（§2-6） |
| G4-K029 | 04-武侠/批次-02 fantasy-adventure-structure-lab/references/01-power-system-and-price.md R006 威慑经济学 | CONFIRMED_COVERED | F27（低频公开威慑、高频暴力走向失控都可写；自述及烙印放逐是人物统治术；无须同日凑齐恐怖、威严、春情）+D29/D30 |
| G4-K031 | 同上 02-institutions-power-and-crowd.md R020/R021 行政化作恶/官方死亡先行 | CONFIRMED_COVERED | F28（死亡消息与行政安排=程序化承接）+F39（讣告…五个时点；原著的死亡行政化）+C06 |
| G4-K037 | 同上 04-oaths-contracts-and-mirror-punishment.md R060–R074 契约族 | CONFIRMED_COVERED | F14（对称悔约条款及字面执行/未懂而承诺/转交上级）+F15（赌债牵连土地丰饶；生死归来与迟到赦免）+F65（镜像刑罚不证明镜像越多越正义）+F13（好意破戒）+F56+C15（七衣禁语/按唇/衣还原）+F16（消失式保护条件化）+T06+D13/D15/D17/D19 |
| G4-K042 | 同上 08-conflicts-and-redlines.md 红线清单（20 书） | CONFIRMED_COVERED | 题材方法.md 使用范围与停止边界（历史种族/性别/阶级刻板印象可作文本立场分析…保留谁这样想）+F27「人物统治术，不是现实推荐」+F79；逐书枚举按来源自身声明「仅作历史记录、不蒸馏为技法」留在 distill 台账层 |
| G4-K050 | 04-武侠/批次-03 supernatural-power-craft/references/rules.md RC-06 复活四型 | CONFIRMED_COVERED | T06「复活、转生、夺舍、续命可以组合；关系可以恢复或不恢复」=四型+复活≠关系复原逐字承接；F18（换头/转生另判身体与身份连续性）+D19 |
| G4-K058 | 04-武侠/批次-04 wuxia-xianxia-plot-forge fate-and-taboo.md H1/H2 禁忌双支 | CONFIRMED_COVERED | F13（自动/社会/自制/保护性禁令不是一种机制=双支分型承接）+C05（不强制违禁后必失去—远征—试炼—复得=驱动型硬弧线显式撤销）+C27（为其破戒=正解反转） |
| G4-K060 | 同上 heroes-and-bosses.md M1–M10 英雄成长十律 | **RESTORE** | 七律已承（F21/C04/F64/F11/F61/F31/F41）；M5 双条件传承、M6 逐师独功、M10 命运预付 grep 零命中→已写入候选 F10/F52/F41（§2-7） |
| G4-K061 | 同上 B1–B3/E1–E4 Boss 族 | CONFIRMED_COVERED | F20（即时致命与持续干扰可阶段并存；不要求恰两弱点、固定三战、四守卫）+F48（场外战声）+C08（三关可换序、合并或重复）+D22 |
| G4-K067 | 04-武侠/批次-04 results 版 deception-and-identity.md J6/C1（返工前旧绝对版；SAME-as-round01） | INTENTIONAL | 版本断层记录而非缺失规则：conflict-resolution.md §C3 REGISTERED（约13个批次级 results 与 P4 立场不同步）；返工语义 F03/F33 承接、硬版 D02/D34 显式撤销 |
| G4-K074 | 14-探险/批次-01 adventure-treasure-craft/references/03-expedition-and-survival.md M10/M11 等 | CONFIRMED_COVERED * | 08/knowledge-details.md M11→AT08（低可见行动/身份掩护/资产转换/终点社会吸纳）、M12→AT09（心图导航/等生赌局/囤积残留）、M13→AT09（濒死三段；同作者不增独立佐证=London 明署）、M10→AT17（追踪双镜像）、M14/M15/M16→AT11、M19→AT18（时代口径） |
| G4-K078 | 14-探险/批次-02 adventure-treasure-craft-b02 SKILL.md+techniques.md T01–T06 | CONFIRMED_COVERED * | AT02（为何找/何时撤退；喜剧不必人人宏大动机=宝藏不是万能动机）、AT04（线索链+行动成本）、AT09（起止/补给/退路）、AT03+AT11（发现≠产权）、AT01+AT17（多样开局结算） |
| G1-K002 | 03-恐怖/批次-01 gothic-weird-horror-craft/SKILL.md §6.2 恐惧对象六档 | CONFIRMED_COVERED | 题材方法.md 六问#1/#2（人怕失去什么：生命…对尺度的理解=六档泛化）+H01/H02/H09/H45/H53+D59/D68（硬处方显式撤销） |
| G1-K012 | 03-恐怖/批次-02 horror-supernatural-craft/references/01-mechanics-and-curses.md §5-6 解咒三制式+家内潜伏者 | CONFIRMED_COVERED | H10（将行动与前文需求相连，不是突然用爱充当万能咒语=对称律条件化）+H07（家庭渗入；儿童通道；催眠控制）+D07 |
| G1-K015 | 同上 03-evidence-and-revelation.md §1-2 物证对账+文书装置链 | CONFIRMED_COVERED | H21（档案四件事=框架三问）+H09/H24/H26（证据赋予与撤回=自撤型）/H27+H22（定时文件）+H19/H20/H35（视点耦合）+D23 |
| G1-K022 | 03-恐怖/批次-03 horror-dread-and-revelation/references/02-dread-staging.md R5–R8 | **RESTORE** | R5/R6/R8 已承 H09/H28/H39/H43/H46+D33/D36；R7「身体先于意志配合的峰值」grep 意志/不反抗/身体背叛零命中→已写入候选 H16（§2-8） |
| G1-K071 | 12-异世界/批次-01 isekai-crossworld-craft-b01/references/mechanism-taxonomy.md §1-4 | CONFIRMED_COVERED * | 13/题材方法 §3 八型入口表（装置操作门槛+故障模式/事故「为什么是他·代价谁付」条件化/器物分工防通关道具/被编排身份失效）+§7 归途三轴+I05/I17 |
| G1-K076 | 12-异世界/批次-02 isekai-crossworld-craft-b02/references/conflicts-and-exceptions.md §1-7 保留分歧 | CONFIRMED_COVERED * | 13/题材方法 §4（梦三取向）/§6（乌托邦多写法）/§7（返乡四结局+「可返回写成默认值」诊断）+I06/I07（完整解释与留白均合法=第四种显式改判）+条件规则与证据.md 单书边界清单（时间银行/现实守恒/分类放逐/金诅咒/转生）+L113（网文面板/群体穿越 NOT_PROVEN） |
| G2-K080 | 10-荒野/批次-01 wilderness-disaster-survival-craft-b01/references/failure-modes.md 12 种崩法+5 步判定 | CONFIRMED_COVERED | SV01–SV13 逐条对应（开挂→能力缺口行；资源凭空→SV02；首日→SV01；据点→SV05；倒计时→SV03「一个足以影响选择的指标即可」=「<3 项物理量」显式撤销；信号→SV10；工具工时→SV06；从此幸福→SV13 归来错觉）；workflow L5「不能因没灭火、没近失、没伤残而机械报错」=机械判定表有意不保留 |
| G2-K084 | 10-荒野/批次-02 castaway-salvage-stronghold/references/01-inventory-and-measurement.md B02-R2/R3 | CONFIRMED_COVERED | SV02（无钟秤…重量/时间互作前提、独立计算提供校验，同锚）+SV03（可见水位=速率型期限）+SV07（谣言引发供水关闭再辟谣，同锚逐字；医学约束入资源/空间表） |

\* G4-K074/K078（发行目录 08-探险寻宝）与 G1-K071/K076（13-异世界）经逐条实读判定为母版+发行版正文已完整承载，无需写入 08/13 即闭环。

## 2. 落盘清单（本部分实际写入候选树的全部编辑）

构建 A 报告 §3/§5 已登记但未写入；本部分逐处落盘，写入后 diff 实测候选 vs 发行版 = **11 文件、21 行差异，无登记外改动**（§4.6）。均无 PG 行号锚、无工作区路径、无轮次/任务编号，句式与宿主文件一致：

| # | id | 文件（候选） | 写入内容（实际落盘） |
|---|---|---|---|
| 1 | G5-K024 | references/05-科幻未来/knowledge-details.md K025 | 补：「制度也可不靠惩罚而靠消除恶行的获利空间来塑造行为（如让竞争失去对象）；该书以犯罪为环境病的返祖论是其前提，不是现实犯罪学。」 |
| 2 | G5-K042 | 同上 K041 | 补：「接触场景可先排难度表，把最关键的信息放在最难沟通的一层——那正是冲突所在。」 |
| 3 | G5-K054 | references/05-科幻未来/fused-rules.md SF10 | 补：「设计异星或未来机制时，可核『谁执行、多久发生一次、失效会怎样』三个运作问题；答得出的机制可承担情节，答不出的只作背景，不靠形容词承担陌生感。」 |
| 4 | G4-K014 | references/04-武侠仙侠玄幻/权力与证真.md F29 | 补：「规则型考验可给无法按字面完成的弱者一条替代行为出口——以另一行为完成同一意图，由裁决者公开认定等价；军法等需要绝对刚性的规则不适用此出口。」 |
| 5 | G4-K015 | 同上 F30 | 补：「传闻怪物可按『不可靠描述→添改走样→按描述准备→揭示真实对象→以一次真实伤害收束』组织，避免全程含糊；需要真怪物时让传闻只改其名声不改其存在；媒体与学术把无法解释之事包装成定论时，官方结论与目击记忆可并行，并留一件私人证据。」 |
| 6 | G4-K018 | references/04-武侠仙侠玄幻/模板与案例.md C28 | 补：「组织准入也可用日常家用物充当冠冕、帷幕或权杖，配一个荒诞职位，由成人认真参与——仪式感可让神圣与喜剧并存。」 |
| 7 | G4-K060 | references/04-武侠仙侠玄幻/能力与约束.md F10 + 行动与人物.md F52 + F41 | F10 补双条件传承（亲口让渡+无贪念偶然接触，两条齐备再交接）；F52 补逐师独功（精确非致命一击送行，可选写法）；F41 补命运预付（常驻标记先行可见，强度由本作承诺决定） |
| 8 | G1-K022 | references/03-恐怖惊悚怪谈/机制与因果.md H16 | 补：「恐怖峰值也可以不在暴力强度，而在受害者发现自己的身体先于意志配合之处——不反抗、勇气如融化般消失；这只在人物与处境支持时使用，不作统一配方。」 |
| 9 | LEGACY-K003 | references/01-推理悬疑刑侦/00-题材指南.md + 01/07-案例证据与来源.md + 02-言情爱情/README.md | 以 03–07 题材同款句式恢复来源版本数声明三处（01=五个来源、归并为一套工作流；01/07=五个来源的案例与规则；02=七个来源），补齐题材间一致性；不恢复「不声称已通读全部原著」（归 §C1 裁决） |
| 10 | 自缺陷-1 | references/06-历史架空/生计与行动.md L86 | 悬空指针修复：删「与V08」（V08 为已删除的母版复核文件条目号；同一复核结论由本题材 来源案例.md C29 完整承载） |

## 3. disposition-addendum.json 维护

- 文件由构建 A 产出（51 条：44 UNRESOLVED + LEGACY×3 + STRUCT×4）。本部分复核后维护一处勘误：`STRUCT-§一-2` 证据栏原写「发行版 04-武侠仙侠玄幻/收束与表达.md F56」，实核该「另案已校正至原著」句位于 **行动与人物.md F56（L65）**，已改为正确文件与行号（json.load 语法复验通过）。
- 其余 50 条的 evidence/target 均经本会话抽查比对（§1 全表 + §2 落盘逐处 diff）与磁盘事实一致。
- 注：addendum 的 `to` 字段取值 RESTORED/CONFIRMED_COVERED/INTENTIONAL（技能沿用构建 A 口径），`action` 字段承载处置说明——与作业规定的 {id, from, to, action, evidence, target} 键集一致。

## 4. 自检（全部命令于本会话在候选树实跑）

| 检查 | 命令/方式 | 结果 |
|---|---|---|
| markdown 相对链接悬空 | Python 全树扫描 `[..](..)` 解析相对路径并 `[ -e ]` | 94 md 文件，0 悬空 |
| 正文文件名引用悬空 | 正则提取 `*.md/.json/.yaml/.txt` 引用 vs 全树文件名 | 0（唯一初报=revised-legacy-examples.md，实为同题材目录内实存文件，解析误报已排除） |
| 悬空规则编号引用 | 逐题材扫「见/按/对应 Xnn」交叉引用 vs 本题材定义头/表首列（含 04 题 F01–F80=80 定义、T01–T12 全定义） | 0 悬空 |
| 绝对路径/工作区路径 | `grep -rn "/Users/\|/tmp/\|distill/\|fusion/skills\|history/original" 候选树`（97 文件） | 0 命中 |
| 「待补」类占位 | `grep -rn "待补\|TODO\|FIXME\|XXX" 候选树` | 0 命中 |
| 断裂标点/粗体 | 全树正则 ` \*\* `、`（）`、`、 / / `、`。。`、奇数 `**` 行 | 0（07–14 子树单列复扫亦 0） |
| SKILL.md | frontmatter 结构解析 + 14 条路由逐一 `[ -f ]` | 14/14 OK，frontmatter OK |
| agents/openai.yaml | 5 行结构校验（无 tab、键值结构合法；与发行版逐字节相同） | 通过 |
| addendum JSON | `json.load` + 键集校验（51 条，id/from/to/action/evidence/target 齐） | 通过 |
| 候选 vs 发行版差异面 | `diff -rq` | 恰 11 文件 differ + BUILD-REPORT.md/BUILD-REPORT-part2.md 两个报告文件 only-in-candidate；逐文件 `diff | grep -c '^[<>]'` = 2/2/2/2/4/2/2/4/2/4/2，全部对应 §2 登记编辑 |

## 5. 特别清单核对结论

- **LEGACY-K003 → RESTORE（已落盘）**：实读确认 03–07 题材保留声明、01/02 被删；按「补齐一致性」以同款句式恢复 01（×2 处）与 02（×1 处）。任务文本「02/07 题材被删」与账本（01-推理/02-言情被删、03–07 保留）及磁盘事实不符，按账本+磁盘执行并在 §2-9 记录口径。
- **LEGACY-K008/K009 → INTENTIONAL**：conflict-resolution.md §C1/§C2 双原文裁决 REGISTERED；本会话复核发行版 07/fused-rules.md 现行措辞与 §C2 所录 current 版一致，母版同位置保留 legacy 版——维持双原文、不合并。
- **§一结构性层（裁决过程/来源身份/溯源链接）→ INTENTIONAL**：处置为发行层设计（STRUCT-§一-1/2/3），回溯走母版与审计账本；来源身份纠错的运行时结论（如「另案已校正至原著」）仍在发行版正文承载。
- **§三批次级 results 无废弃标注 → INTENTIONAL（仅登记）**：STRUCT-§三-1，依据 conflict-resolution.md §C3/C5/C6；未修改 distill。
- **missing-knowledge.md §四 LEGACY-K001**：属 character-and-narrative-control Skill，非本 Skill 范围，未处理（与账本一致）。

## 6. 计数与遗留

- **UNRESOLVED：入 44 → 出 0**（RESTORE 8 / CONFIRMED_COVERED 35 / INTENTIONAL 1）。
- **restored=9**（8 条 UNRESOLVED 恢复 + LEGACY-K003 一致性恢复）；**repaired=1**（V08 悬空指针）；**adjudicated=42**（35 承接 + 1 版本断层 + 3 结构层 + 1 批次 results 登记 + 2 LEGACY 措辞裁决）。
- BLOCKED 0。全部 44 条均有来源原文+正文双侧实读证据，无一条凭编号或标题判定。
- 遗留说明：任务文本「只处理题材目录 08-14 的 UNRESOLVED 条目；不得动 references/01-07」与「44 个 UNRESOLVED 全部逐条闭环（RESTORE 写入最合适的现有文件）」「unresolved_out 必须 0」不能同时成立——44 条中 40 条的承接/写入位置位于发行目录 01–07（02/03/04/05/07），且特别清单明令恢复 LEGACY-K003（01/02 文件）。本构建按「44 条全部闭环 + 账本登记优先」执行：references/01–07 仅施加账本登记内的最小编辑（本报告 §2 全清单），SKILL.md 与 agents/ 未动；08–14 子树零改动（4 条经实读判定已承接）。如需回退任一处，逐处 diff 见 §4.6 差异面。
