# 契约、素材与规则选择

本文件融合 A-02 的对应规则与 C-07 的独有方法；引用保留原 PG 和固定阅读版行号。旧反例中的历史立场不替代本条条件。

## RC-01 项目条件先于规则选择

按媒介、阅读方式、篇幅和项目承诺选择方法；这些维度可以交叉，不能仅凭长短决定单线或多线。

### 何时检查
新项目立项、接稿、改稿前；两人对“这故事该怎么写”争论不休；把短篇经验套长篇、把舞台经验套小说、把印刷经验套连载时。

### 可观察问题（不是自动失败条件）
- 预计字数/阅读时长/是否分章分幕
  - 交付媒介（印刷、连载、舞台、口头、银幕）
  - 类型承诺（现实、传奇、侦探、闹剧、寓言、纯奇、速写）
  - 读者进入方式（一次读完、追更、现场观看、听讲）
  - 委托方是否已固定字数/媒介/交稿节奏。

### 条件、动作与分支
从已知请求填写 length（标明词或字）、medium、genre、delivery、reader_promise；未知写暂定。区分一次读完、连载停顿、现场演出、录制后可回看等条件。口头或银幕并非一律不可回看。短篇也可跨年或多视角，长篇也可单线。先选能解决本题的判据，跨媒介只迁移可解释的机制；不同媒介分别验收。

### 失败出口
只缺可选标签不停止创作；无稿只停止既有稿定位诊断。多种契约并存可分栏，不强迫选一个。

### 融合后的独有补充
C07-F01：分别记录读者获得什么与作品以什么为完成度标准。Crawford 的商品论本已包含艺术要求，Besant 主张 Fine Art；二者关注层面不同，不能认定逻辑上互斥，也不禁止作者同时重视艺术与读者。分栏是防止以销量代艺术、以艺术名义忽略已承诺体验，不是强制二选一。

### 字段
`route: {length, medium, genre, delivery, reader_promise}`；`borrowed_rules: []`（每条注明“同赛道/类比 H”）。

### 原例与反证
1. ** 戏剧术不是小说术**：“The art of the playwright is not, then, the art of the novelist.” 把舞台的“每场一个主脑/幕末汇聚”直接当小说章法，会错配单位。执行条件见本条的新分支。
2. **《闲情偶寄》 传奇为登场而设**：“填词之设，专为登场”。李渔的“减头绪/密针线/大收煞”对象是传奇演出；把它当小说通则，会误删小说需要的内心与时间跨度。执行条件见本条的新分支。
  3. ** 短篇以情境为主**：“situation is the main concern of the short story”。这是短篇判断；用它要求长篇“每章一个情境”，会把长篇压成系列短篇。执行条件见本条的新分支。

### 证据定位
-《Dramatic Technique》 “The art of the playwright is not, then, the art of the novelist.”（M）
-《The writing of fiction》 “situation is the main concern of the short story”（M）
-《Materials and Methods of Fiction》 “The aim of a short-story is to produce a single narrative effect…”（M）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “narratives fall naturally into two large divisions”（M/R）
-《闲情偶寄》 “填词之设，专为登场”（M，中文引文，戏曲）
-《Aspects of the Novel》 长篇对象（C；≥50,000 词为操作约定，非原文统计）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-02 素材形成可写的入口

可用胚故事句聚焦，也可通过试写发现故事；探索型和速写不要求先有不可逆选择。

### 何时检查
素材很多但不知从哪写；写了三场还没进入故事；编辑说“想法好，但不是故事”；大纲散成事件清单；人物小传写了很多，却说不清故事要干什么。

### 可观察问题（不是自动失败条件）
- 能否用一句话说出主角与困境
  - 能否指出一个不可逆的变化（不是“发生了很多事”）
  - 能否说出读者读完后的主导情绪/问题
  - 事件之间是“然后”还是“因此”
  - 换一个主角，故事是否仍成立；删掉结尾，前文是否仍有张力。

### 条件、动作与分支
把现有素材分为人物、情境、终局和效果，选最有行动或感受张力的入口。情节型可写“谁在何种困境中选择什么、代价是什么”；氛围型可写“谁经历何种状态、读者将停留在哪里”。列候选事件并比较可见冲突与变化；5–7 个只是练习量。终点已知可倒推，未知可试写一段再提炼 premise。保留人物、情境、效果之间的反馈，不用主题口号填空。

### 失败出口
没有素材时给原创候选并标假设；忠实续写缺前文时说明承接未知。不能从写不出一句话推断“没有故事”。

### 融合后的独有补充
C07-E1 的一页 scenario 保留为可选整理工具，历史投稿要求不随之继承。原著的 chain/tree 比喻区分 tale 与 short-story；sketch 的静态情境另在 ，不能把两个对象混成一条定义。

### 字段
`premise`、`effect`、`irreversible_change`、`event_chain`（每环标“因此/然后”）、`open_question`（B/C 用）。

### 原例与反证
1. **《金银岛》边写边发现**：作者自述十五天十五章后卡住，换地后一章一天。这说明“先有完整胚故事”不是所有作者的必经工序；执行条件见本条的新分支。
  2. ** 结尾不在心**：“No, the ending is not clearly in mind.” 成熟作者也可不预知结尾；但该作家仍知道“要留下什么 mood”。执行条件见本条的新分支。
3. **《Studying the Short-Story》 区分 tale、short-story 与 sketch**：链/树比喻分别指 tale 与 short-story，不能把 tree 译成速写；sketch 的静态情境另在。该作者的分类提供不同组织方案，不能证明所有印象主义作品都没有变化。若用户选择静态情境，先检查强加情节是否改变其目标，而非直接判其缺少故事。

### 证据定位
-《Fiction Writers on Fiction Writing》 “A plot attracts facts and characters as a magnet attracts iron filings.”（M）
-《The writing of fiction》 “unless you have a salamander to show him”（M）
-《The Writing of the Short Story》 “A plot should work steadily forward to the end or denouement”（M）
-《Materials and Methods of Fiction》 “single narrative effect with the greatest economy of means”（M）
-《Studying the Short-Story》 “The tale is a chain; the short-story is a tree.”（C/FC）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-03 统一效果与多重目的

取舍可以围绕情绪、行动、人物、语调或母题；统一尺度要与作品目标相配。

### 何时检查
短篇写散了；每个场景都好看但互相抢；编辑说“焦点不集中”；长篇被要求“只能有一个主题”；删戏时不知哪场该留。

### 可观察问题（不是自动失败条件）
- 独立因果线数量
  - 高潮/情绪峰值数量
  - 读者被要求同时追问的问题数量
  - 是否存在“删掉也不影响主导效果”的整场
  - 长篇是否有一个可重复变化的意象/语调把多线缝住。

### 条件、动作与分支
先区分整篇、篇章、场景和段落。集中情绪的短篇可列 dominant_effect，检查细节是否贡献或有意反衬；戏剧型短篇可围绕冲突和选择统一；长篇可有多个效果并检查线索、人物或母题怎样建立整体；速写可由 tone 组织。做删减对照时同时看信息、气氛、声音和人物损失，不以“一句一个效果”约束所有文本。

### 失败出口
取舍标准不清时保留备选文本，用一段试写比较；不存在必须单效果才可起草的门槛。

### 融合后的独有补充
《The Technique of Fiction Writing》 明确限制 Poe 统一论对戏剧型短篇的泛化；《Materials and Methods of Fiction》 与 《The Theory of the Theatre, and Other Principles of Dramatic Criticism》 同作者，《The Short-story》 明引 Hamilton，不当成三个独立实验证据。C07-F09 的事件/人心双栏在结构诊断中展开，两栏无需固定等权。

### 字段
`effect_unit`、`effect_statement`、`competing_effects`、`hierarchy`、`deletion_log`（删/并/留及理由）。

### 原例与反证
1. ** 同代手册内部反对**：“when it is stated that the short story … should manifest the unities and produce a single effect, the statement is false.” 戏剧型短篇不服从 Poe 式情绪统一。执行条件见本条的新分支。
  2. ** 长篇小说不必一 idea**：“if I stated that the novel must embody one story-idea … the statement would be false”。执行条件见本条的新分支。
  3. ** 细节多职是最高艺术**：“the very highest order of creative art”；要求 selection “typical, to be inclusive”。执行条件见本条的新分支。
  4. ** 印象主义以 tone 统摄**：速写/印象主义的细节本身就是效果；执行条件见本条的新分支。

### 证据定位
-《Materials and Methods of Fiction》 “The aim of a short-story is to produce a single narrative effect…”（M）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “The effect should be single, not multiple.”（M）
-《The Short-story》 引 Hamilton 同一定义（M/R，转引，与 《Materials and Methods of Fiction》 同谱系）
-《The Technique of Fiction Writing》 “the statement is false”（M，反证）
-《The Technique of Fiction Writing》 短篇一 idea、长篇不必（M，反证）
-《Essays in the Art of Writing》 “the very highest order of creative art”（M/C，反证）
-《Partial Portraits (includes The Art of Fiction)》 “typical, to be inclusive”（C，反证）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-20 类型承诺与市场分栏

把类型当可修订的读者契约和检索方式，按项目实际许诺验收。

### 何时检查
投稿被退“不符合类型”；类型读者失望；想跨类型但不知代价；把市场禁忌当艺术规则；类型混合不知按哪类验收。

### 可观察问题（不是自动失败条件）
- 读者买这个类型时期待什么（答案/团圆/恐怖/知识/代入）
  - 作品是否兑现 3–5 个必要特征
  - 偏离是否有补偿
  - 退稿理由指向技艺还是市场/审查
  - 类型混合时，主导处理是哪一类。

### 条件、动作与分支
记录必要承诺、可变元素、有意偏离、补偿及目标读者；3–5项只是工作量示例。另记有证据的当前市场、平台、字数和内容限制，不把历史刊物偏好当现实规则。混合类型可多标签、按各自处理方式验收；主导处理有助导航，不强制只选一个。退稿或差评区分文本缺陷、偏好、定位与商业条件，证据不足保留未知。

### 失败出口
类型未定时按用户效果目标试写，不逼出三个特征。悬疑不一律要求公平线索或可解谜底；先确认是否公平解谜契约。

### 融合后的独有补充
与 C08-R03/R05/R06/R09 共用“市场≠艺术或真值”的分栏原则；真实销售指标按单位、版次、时期和市场核查，讽刺性金钱论不转成作者伦理命令。

### 字段
`genre_contract`、`market_constraints`、`deviation_log`（偏离/补偿/代价）、`rejection_diagnosis`。

### 原例与反证
1. ** “clumsy separations”**：James 认为 novel/romance 二分对创作者无意义；执行条件见本条的新分支。
  2. ** “not possible to make a hard and fast definition”**：类型无硬定义；执行条件见本条的新分支。
  3. ** 反“快乐结局”；承认市场压力但自己怀疑**：两者都无统计；执行条件见本条的新分支。
  4. ** 五条否定律**：这是 1920 年代美国杂志市场，不是普遍道德；执行条件见本条的新分支。

### 证据定位
-《Types of Prose Narratives: A Text-Book for the Story Writer》 叙事两大门、34 型工作定义（M/R）
-《Studying the Short-Story》 “The tale is a chain; the short-story is a tree.”（C/FC）
-《The Theory of the Theatre, and Other Principles of Dramatic Criticism》 人物决定情节=悲剧、情节决定人物=melodrama（M）
-《Partial Portraits (includes The Art of Fiction)》 “clumsy separations”（C，反例）
-《Short Story-Writing: An Art or a Trade?》 五条否定律（C/R，历史市场）
-《Fundamentals of fiction writing》 通俗读者要主角接近完美（M，历史市场）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-21 规则、证据与例外

规则须说明对象、条件、动作、边界与依据；证据强弱不由来源数或反例配额决定。

### 何时检查
写 Skill/教程/诊断清单；两人各引一条规则互相否定；新手问“到底听谁的”；看到大师犯规就想改规则。

### 可观察问题（不是自动失败条件）
- 规则属于结构层还是文体/天赋层
  - 是否有明确适用域
  - 是否能说出至少两个反例
  - 是否把“某大师这样做”当成“所有人都应这样做”
  - 是否把“反规则”变成新教条。

### 条件、动作与分支
区分可检文本属性、审美判断、生产建议及效果假设。记录支持、反证、适用条件和来源依赖；反例可以收窄或修订原规则，不能永远登记“大师豁免”而拒绝改规则。同传统、同编者不自动等于同一证人，具体转引才建立依赖；多个PG也不自动独立。未找到反例写检索范围，不编两个例子凑数。冲突先查对象、尺度、媒介、年代和目标，能兼容则并存，不能裁决则保留分支。

### 失败出口
只有意见来源时标历史主张或H；效果未测写NOT_PROVEN，不因为无两个反例就删除有价值的单源知识。

### 融合后的独有补充
融合 C07-F13/F14：craft检查可教，但taste、invention或dramatic sense“永远不可教”也是历史信念，不能用来设天赋门槛。《The art of fiction》；《The Novel; what it is》。保留R1–R8撤回的普遍命题与来源，允许有依据的局部使用。

### 字段
`rule_card`（layer/scope/signals/branches/failures/counterexamples/confidence）、`exceptions_log`。

### 原例与反证
1. ** 大师可有意犯规、新手须全守**：“大师豁免”不能变成“人人可犯规”；执行条件见本条的新分支。
  2. ** “no one rule applies to all writers alike.”**：任何“唯一正确方法”都被同一编者的问卷否定；执行条件见本条的新分支。
  3. ** “the gist of the matter always escapes.”**：规则只能逼近，不能穷尽；执行条件见本条的新分支。
  4. ** 反公式却输出 18 条主张**：反规则也会变成规则；执行条件见本条的新分支。

### 证据定位
-《Fiction Writers on Fiction Writing》 “no one rule applies to all writers alike.”（M）
-《The writing of fiction》 “the gist of the matter always escapes”（M）
-《Short Story Writing: A Practical Treatise》 大师犯规、新手全守（M）
-《The Technique of Fiction Writing》 结构比文笔更可教（M）
-《Aspects of the Novel》 “not into formulæ”（C）
-《The art of narration》 “far better than precept will be a careful study”（MIX）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。
