# 人物、信息、可信度与主题

本文件融合 A-02 的对应规则与 C-07 的独有方法；引用保留原 PG 和固定阅读版行号。旧反例中的历史立场不替代本条条件。

## RC-05 人物与事件双向检查

人物、情境、终局、效果均可作为入口；检查当前项目所需的动机和事件关系。

### 何时检查
不知从人物还是情节起笔；人物像道具；情节压得人物喘不过气；编辑说“人物不可信”或“故事没发生”；人物小传很厚，但一进情节就变成传声筒。

### 可观察问题（不是自动失败条件）
- 素材最先抓住你的是什么（一个人、一个困境、一个必须发生的场面、一个情绪/画面）
  - 人物能否说出三处“只有他会这样”的决定
  - 情境是否已含对抗力量
  - 终局场面是否必须先发生
  - 人物是否只在传递信息/推动机关。

### 条件、动作与分支
人物入口：目标、恐惧、资源、约束怎样产生选择；情境入口：压力迫使谁在何种代价中行动；终局入口：哪些前史使最后选择成立；效果入口：哪些动作或感知形成体验。可比较三个关键决定、删人测试与遮名辨识，但数量不作门槛。区分只承担信息、喜剧或对照功能的配角与被情节强扭的角色。扁人物和不改变的主角也可有效。

### 失败出口
无法预测人物时可写秘密历史、临时情境或直接试写；不必删掉人物或先解决全部心理问题。

### 融合后的独有补充
融合 C07-F05：葬礼、借钱、被误解三个未写场景是练习；预测话、动作、犹豫，不能以模型自编答案证明人物已真实。首次出场可选辨识细节与动作；删名、gesture tags 和口头禅检查要保留节奏、身体及关系信息。Besant 的 grow 是作者脑内主观经验，不能把练习失败直接说成稿件事实。

### 字段
`entry_type`、`entry_evidence`、`character_card`、`situation_forces`、`plot_forces_character`、`character_causes_turn`。

### 原例与反证
1. ** 玩偶人物**：“inventing a situation and sticking doll-like characters in it” 是失败经验。执行条件见本条的新分支。
  2. ** Hardy 让人物 suspend their natures**：人物被情节/命运压干，失真。执行条件见本条的新分支。
  3. ** Assingham 夫妇为传递信息而造**：功能人物被读者看穿。执行条件见本条的新分支。
  4. ** 通俗短篇反例**：以代理情绪为目标的短篇，“extreme character drawing is generally a mistake”。执行条件见本条的新分支。

### 证据定位
-《Partial Portraits (includes The Art of Fiction)》 “character in itself is plot”（C，H 到步骤）
-《The writing of fiction》 “what his characters, being what they are, would make of the situation”（M）
-《Fiction Writers on Fiction Writing》 “Character makes plot.”（M）
-《The Poetics of Aristotle》 “Plot, then, is the first principle”（C）
-《The Technique of Fiction Writing》 “each incident functions in the development of a plot or dramatic problem”（M）
-《Dramatic Technique》 “character is situation.”（M，舞台）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-11 叙述权限、距离与切换

检查信息由何种叙述通道提供；视角数量和切换位置服务作品契约。

### 何时检查
限知视角突然写出人物不可能知道的事；全知与限知混用；多人视角切换生硬；第一人称写着写着变成作者；编辑说“视角乱了”；为了传信息临时换到配角脑子里。

### 可观察问题（不是自动失败条件）
- 叙述者此刻能知道什么、不能知道什么
  - 是否存在“越界知识”（别人的内心、远处发生的事、尚未发生的结局）
  - 语域/距离是否与视角人物匹配
  - 切换处是否有场景/章节/排版标记
  - 切换买回了什么（范围、反讽、对照、信息）。

### 条件、动作与分支
记录谁讲、谁看、当时或事后、可进入谁的意识、可知何种前史。贴身视角按人物感知和推断过滤；全知或框架叙述可提供角色未知信息。切换记 trigger/benefit/marker/cost：收益含信息、情绪、对照、主题和形式，标记也可以是清楚的上下文。短篇一视角、长篇2–3视角仅为历史起点；不以数量或“一句信息”直接否定切换。

### 失败出口
局部段落契约不明时列两种可解释读法与影响，避免假定全书违约；必要时补来源或重锚，不强行换人称。

### 融合后的独有补充
人物预测不是视角学；C07 的 front view 只作呈现检查，不能冒充聚焦理论。专业深化由04负责，本包保留诊断所需的信息合同。

### 字段
`pov_contract`、`distance_profile`、`switch_ledger`（trigger/benefit/marker/cost）、`pov_violations`。

### 原例与反证
1. **《Bleak House》《War and Peace》频繁切换仍成立**：说明“一致性”不是绝对；执行条件见本条的新分支。
  2. ** Assingham 夫妇为传递信息而造**：行为不可信；切换的代价高于收益。执行条件见本条的新分支。
  3. ** 1926 选本仍有第一人称叙述者公开现身**：不是所有时代都禁“叙述者现身”。执行条件见本条的新分支。
  4. ** 第一人称三种禁用**：是逐篇选择，不是一刀切；执行条件见本条的新分支。

### 证据定位
-《The writing of fiction》 “record anything not naturally within his register”（M）
-《The writing of fiction》 “it is best to shift as seldom as possible”（M）
-《The writing of fiction》 “no convention is in itself objectionable”（M）
-《The Technique of Fiction Writing》 短篇不应改视角（M）
-《Materials and Methods of Fiction》 “there is always one best point of view”（M）
-《How to Write a Novel: A Practical Guide to the Art of Fiction》 视角看不见的不写（M）
-《Aspects of the Novel》 “bounce the reader into accepting what he says”（C）
-《The art of narration》 叙述者公开现身（MIX，反例）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-12 信息差与紧张来源

按每一条信息比较读者、人物与叙述者已知，分别设计未知答案、知情危险、同步惊奇和混合状态。

### 何时检查
悬念不成立；读者早就猜到；揭秘时读者失望；舞台/小说同一场戏效果相反；改编时不知道哪些信息该提前给。

### 可观察问题（不是自动失败条件）
- 读者进入时知道什么
  - 人物知道什么
  - 作者/叙述者知道什么
  - 揭晓点在哪；揭晓后还剩什么
  - 读者是否已从类型惯例预知。

### 条件、动作与分支
用 knowledge_matrix 逐事件记录谁何时知道、通过何途径知道；定 reveal_points、揭晓后的处境变化和仍然未定的后果。读者少知可产生好奇，读者多知也能产生悬念；二者不是体裁互斥。标题与类型惯例是读者信息的一部分，但知道会有答案不等于已知真相。已预知身份仍可悬念于发现、行动和代价。

### 失败出口
未知格填未知；可先用读者/主角/对手几行，不因未填满停止写揭晓。保密须遵守叙述权限，不能仅靠有机会说话却无原因沉默。

### 融合后的独有补充
舞台“观众全程知道秘密”是历史主张，不能扩成一切戏剧或禁止悬疑使用戏剧反讽。原著的读者健忘说只作市场批判，不用作设计依据。

### 字段
`knowledge_matrix`、`suspense_mode`、`reveal_points`、`reader_question`。

### 原例与反证
1. ** 舞台要求观众全程知道秘密**：侦探若照搬会泄底。执行条件见本条的新分支。
  2. ** 悬念有时靠“almost fabulous stupidity”**：这是市场观察，不是正面方法。执行条件见本条的新分支。
  3. ** 小说唯一可预设义务是“有趣”**：不能拿“读者会不懂”当删减借口，也不能拿“读者会懂”当免解释理由。执行条件见本条的新分支。
  4. **侦探读者默认“会有答案”**：类型惯例本身是知识状态的一部分；执行条件见本条的新分支。

### 证据定位
-《The Theory of the Theatre, and Other Principles of Dramatic Criticism》 “the audience must know the secret all the time”（M，舞台）
-《Play-Making: A Manual of Craftsmanship》 “the source of the highest pleasure”（M，舞台）
-《Fundamentals of fiction writing》 “The imposing of an illusion is the object and test of fiction”（M）
-《Fundamentals of fiction writing》 “The effects are cumulative”（M）
-《Short Story-Writing: An Art or a Trade?》 “almost fabulous stupidity of the large mass of readers”（C）
-《Short Story Writing: A Practical Treatise》 3,000 词内不设前置缓解、≥10,000 词可减压（M）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-13 可信度、偶然与虚构契约

区分现实可核事实、作品世界规则、人物选择与偶然事件；不同契约容许不同的概率和因果。

### 何时检查
读者说“太巧了”；真实事件改编被嫌假；幻想/闹剧被要求“合理”；侦探靠巧合破案；人物在关键时刻突然得到恰好需要的东西。

### 可观察问题（不是自动失败条件）
- 作品承诺的是“可能发生”还是“不可能但自洽”/“夸张取笑”
  - 巧合出现在前提、转折还是解结
  - 巧合是否直接决定胜负/生死/婚配
  - 是否有前文铺垫/人物因果可替代
  - 类型内部规则是否前后一致。

### 条件、动作与分支
写 credibility_contract，列巧合的位置（前提/途中/解结）、作用和替代方案。重人物因果的写实或解谜作品可检查偶然是否替代了承诺中的解决，考虑前史、行动或可见偶然性；荒诞、喜剧、命运主题和幻想可有意由偶然组织。真实改编保留事实，不为让其像小说而伪造前因；可呈现人物惊讶、背景频率和已知条件。“补双倍铺垫”只是修辞性建议。

### 失败出口
契约不明先给分支，不自动按最严写实处理；不能解释的现实事实标未知而非改成假因果。

### 融合后的独有补充
融合 C07-F11：字面可能性和反应可理解性分开。 倾向生活可能；与存在语境张力。心理可理解是许多人物叙事的有用目标，不是所有非人、荒诞或不可知叙事的普遍硬约束。不要将不可能角色一律视为错误，也不以设定免除作品自定的规则。

### 字段
`credibility_contract`、`chance_audit`（位置/作用/替代方案）、`setup_log`。

### 原例与反证
1. **Oedipus 的巧合是悲剧前提，不是解结**：命运框架可豁免；执行条件见本条的新分支。
  2. ** 允许“delightful improbability”**；要求按 farce 评：闹剧/传奇可容偶然。执行条件见本条的新分支。
  3. ** 纯奇“probability is not called for”**：仍要求 magnificence/splendor/magic 的内部一致；执行条件见本条的新分支。
  4. ** “dime novel” 容忍度更高**：这是类型契约，不是写实规则；执行条件见本条的新分支。

### 证据定位
-《Short Story Writing: A Practical Treatise》 “verisimilitude, not verity, is wanted in fiction.”（M）
-《The Poetics of Aristotle》 诗人写“可能发生”（C）
-《The Author's Craft》 “true within his chosen convention, and not further.”（M）
-《Fundamentals of fiction writing》 “Could it happen under the conditions?”（M）
-《Play-Making: A Manual of Craftsmanship》 “A coincidence… which coincides with a crisis… wholly inacceptable in serious art.”（M，舞台）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “probability is not called for”（M，纯奇）
-《Studying the Short-Story》 “as farce, which blithely assumes the improbable as true”（C/FC）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-16 主题、议论、道德与讽刺

主题可由行动后果、叙述议论、寓言、反讽或形式承载；按实际契约判断失配。

### 何时检查
结尾突然说教；人物替作者讲道理；主题正确但故事无聊；寓言被要求“藏起来”；讽刺被误读成宣传。

### 可观察问题（不是自动失败条件）
- 主题能否写成一个问题而非口号
  - 人物是否在关键处做出体现主题的选择
  - 删掉点题句，行动是否仍成立
  - 类型是否本来承诺“教训”
  - 反讽标记是否足够。

### 条件、动作与分支
可写 theme_question 或明确主题立场，找 proof_scene 与 declarations，比较点题句删前删后的信息、声音和伦理效果。人物被迫说不合其处境的作者口号时，考虑行动、代价或叙述层的替代。寓言、教育、论辩小说可明示；一般小说也可有有力议论。讽刺先查语境标记，不把角色观点自动当作者结论。

### 失败出口
不能把议论改成动作时可以保留、缩写或调整叙述位置，不自动删除。作者无意表达道德时不强加意义。

### 融合后的独有补充
融合 C07-F02 的三层：直接布道/论文；选择、同情与后果；Besant 的“英国小说自觉道德目的”历史观察。《The Novel; what it is》；《The art of fiction》。反读测试仅检视开放性，允许相反合理解读不是合格小说的必要条件。Crawford 自认落入宣讲也保留作立场反例。

### 字段
`theme_question`、`proof_scene`、`declarations_log`、`genre_exception`。

### 原例与反证
1. ** 道德故事由“作者明显要教”定义**：“obvious concern about the lesson”；此时“藏主题”反而失败。执行条件见本条的新分支。
  2. ** 自己承认好故事含 “strong argument for good”**：只是反对把故事当伦理真理的载体；执行条件见本条的新分支。
  3. ** 主张小说塑造时代道德**：这是价值立场，不是事实；执行条件见本条的新分支。
  4. **讽刺表面直陈可能是有意反讽**：不能一律删；执行条件见本条的新分支。

### 证据定位
-《Short Story Writing: A Practical Treatise》 “strong argument for good”；“didacticism in literature is always inartistic”（M）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “have the moral seem to grow naturally out of the action”（M）
-《文心雕龍》 “為情而造文”（C，中文引文）
-《The writing of fiction》 “a mere irrelevant happening”（M）
-《The Writing of the Short Story》 “any didactic purpose is not obtrusive”（M）
-《Aspects of the Novel》 “The story is neither moral”（C，反例）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。
