# 结构与呈现的综合诊断

本文件融合 A-02 的对应规则与 C-07 的独有方法；引用保留原 PG 和固定阅读版行号。旧反例中的历史立场不替代本条条件。

## RC-04 终场、终局状态与发现型写法

结局先行是一种规划方式；发现型写法可先确定下一段的压力并在修订时回查。

### 何时检查
写到最后收不住；中段塌；结尾像补上去的；连载写到后面人物失控；编辑问“这故事到底要走到哪”。

### 可观察问题（不是自动失败条件）
- 能否说出最后一场戏的画面/最后一句的方向
  - 能否说出“什么不可逆地改变了”
  - 结尾是否回收了开头的意象/问题
  - 中段事件是否在“倒推链”上
  - 连载是否有“终局状态”而不是“永远下一章”。

### 条件、动作与分支
短篇终场已清晰时列画面、行动、代价及倒推因果；三环是起步练习。长篇可先定关系或社会状态，不必先写最后一句。侦探若承诺解谜，可先推机关与解答，再检查发现过程。人物生长、探索或开放结构允许结局暂定；写后核对承诺与准备。latent 可是选择、关系、问题或意象，不要求第一段出现终局符号。

### 失败出口
写不出结尾时推进一个可写单元，记录待决；不要把不确定结尾当作全局停稿理由。

### 融合后的独有补充
保留 《金银岛》与原著的发现型自述、原著的 Trollope 例外；这些是工作法案例，不是速度或成品质量证明。

### 字段
`ending_mode`（terminal scene / terminal state / discovery）、`terminal_scene` 或 `terminal_state`、`three_causal_links`、`latent_image`、`last_line_direction`（终场最后动作的方向，用动作代替直接结论）、`milestone_turns`（长程里程碑转折清单）、`ending_check`。

### 原例与反证
1. ** Trollope 边写边定**：“my incidents are fabricated to fit my story as it goes on”。这说明连载可以没有预知终场；具体适用条件见下文。
2. **《Fiction Writers on Fiction Writing》：人物生长、结尾不在心**：Montgomery 的长篇由人物生长；Stribling 说 “No, the ending is not clearly in mind.” 具体适用条件见下文。
  3. **《金银岛》卡壳后换地**：十五天十五章后卡住，换地后一章一天；这说明“倒推”也可能卡住，换环境/换介质能恢复。具体适用条件见下文。
  4. ** 侦探先抛谜面**：“propound your mystery at the beginning … work backwards to the first step”。侦探仍须知道终局，只是谜面在前；具体适用条件见下文。

### 证据定位
-《How to Write a Novel: A Practical Guide to the Art of Fiction》 “Take your stand at the end of the story, and work it out backwards.”（M）
-《On the art of writing fiction》 “see the end of your story before you begin to write it”（M）
-《Fiction Writers on Fiction Writing》 “The climax; I always start with it”（M）
-《Materials and Methods of Fiction》 “he must see the end of his story from the beginning”（M）
-《The writing of fiction》 “no conclusion can be right which is not latent in the first page”（M）
-反例：《Essays in the Art of Writing》；《How to Write a Novel: A Practical Guide to the Art of Fiction》；《Fiction Writers on Fiction Writing》。

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-06 主线、多线、照应与链条

线索可因果交汇、并重交织，也可通过人物、时地、主题或形式照应；先确认功能再删并。

### 何时检查
长篇越写越散；次线抢戏；群像热闹但主线不动；改编时不知道删哪条线；连载写到后面每条线都要独立收束，主线却停滞。

### 可观察问题（不是自动失败条件）
- 能否一句话说出主行动（谁要什么、谁阻止、代价）
  - 每条次线是否有独立主角/独立高潮
  - 抽掉一条次线，主线是否变化
  - 多条线是否在同一场面/同一决定处汇合
  - 是否存在只在主题上相似、情节上互不相干的线。

### 条件、动作与分支
给各线记录名称、欲求或问题、独有功能、承重事实和联系方式。情节型查因果与共同决定；并重型查互相照亮或资源交叉；跨时空可通过物件、文献、后果或主题建立联系；picaresque/tale 可按每站处境、经验或语调组织。抽去一线时比较事件、人物、主题、气氛与声音，不仅问主线结局是否改变。汇聚比例 3/4 是历史建议。

### 失败出口
联系暂不清时保留待判并给压缩/合并/独立篇章方案；无直接相遇不能自动判赘线。

### 融合后的独有补充
C07-F09：事件栏记录变化、信息或问题；人心栏记录人物后果及实际反馈或效果假设。先按项目目标判断弱项；只有氛围不自动补事件，只有事件也不要求每章补情绪段。两栏都弱须有文本依据才建议重写，不能凭猜测读者感受下结论。

### 字段
`main_action`、`strands[]`（name/function/intersection）、`major_convergence`、`cut_log`。

### 原例与反证
1. ** 链条式不算 plot**：picaresque 单线串联不构成“编织”；此时不强行加交汇，改按 C 分支验收“每站是否改变主角处境”。
  2. ** 等重多线**：允许若干等重故事，但须交织；不能拿“多线”当“无主线”的借口。具体适用条件见下文。
  3. ** 舞台拉幕点**：要求在多线汇聚处拉幕；但传奇/情节剧可加 Prologue（作者自陈例外）。具体适用条件见下文。

### 证据定位
-《The Technique of Fiction Writing》 “the main course of the story must be single”（M）
-《Materials and Methods of Fiction》 “The word plot signifies a weaving together”（M）
-《Materials and Methods of Fiction》 “avoid a sub-plot, unless…”（M）
-《Play-Making: A Manual of Craftsmanship》 “the curtain should be raised at the point where separate lines have converged”（M，舞台）
-《闲情偶寄》 “此一人一事，即作传奇之主脑也”（M，中文引文，戏曲）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-07 场景、概述、过渡与呈现方式

按所需体验选择展开、压缩和连接；场景不以目标—阻力—转折三项齐全为定义。

### 何时检查
全篇都是概述，读者不进戏；全是场景，篇幅爆炸；时间跳跃生硬；中段发闷；该演出来的对峙被一句“他们谈了谈”带过。

### 可观察问题（不是自动失败条件）
- 每段是否有连续的时间/地点/人物动作
  - 是否存在“该演出来的对峙”被概述
  - 是否有“只交代后来怎样”的长段
  - 时间跳跃处是否有锚点（季节、身体、物件）
  - 连续单元是否只加码、无缓解（K-13：短篇兴趣不减；长篇允许缓解，但须服务更大张力）
  - 对话是否只在高潮/转折处承担主要功能（书面叙事；舞台另算）。

### 条件、动作与分支
建立 unit_table，记录呈现模式、功能、信息和时间跨度。关键对抗若需要读者当场体验，可展开行动/对白/空间；若目标是距离、留白或快速经过，可以概述。过渡可用季节、身体、物件、关系或目标变化承接，也可简短报时。场景、概述、反思、抒情和蒙太奇可混合。对话可承载冲突、信息、人物声音、关系和节奏，不限高潮。

### 失败出口
混合单元标混合，不为分类强删；安静体验场不必制造对抗。无目标不等于无功能。

### 融合后的独有补充
融合 C07-F06：front view 问读者此刻看到、听到、期待什么，可检查空间和动作；这是“口袋舞台”类比，不是要求小说变剧本。内心与概述是合法方法，舞台也可通过叙述、合唱或对白压缩事件。

### 字段
`unit_table`（段号/type/function/字数）、`scene_to_summary_log`、`transition_log`。

### 原例与反证
1. ** 内部 23 人反对描写、6 人主张全描写**：配比无统一标准。具体适用条件见下文。
  2. **原著的 tale/sketch 可以以概述为主**：强行场景化会破坏文体。具体适用条件见下文。
  3. ** 过渡要“colourless and quiet”**：不是无信息；纯拖延的过渡应删。具体适用条件见下文。
  4. ** “If I use more than one sentence of description I wince.”**：这是快节奏作者的反信号，不是通则。具体适用条件见下文。

### 证据定位
-《The Technique of Fiction Writing》 描写随叙事逐项发生、不能一次做完（M）
-《The writing of fiction》 “not fearing to go slowly”；“colourless and quiet”（M）
-《The writing of fiction》 “It should be reserved for the culminating moments”（M，对白，书面）
-《Fiction Writers on Fiction Writing》 日常细节建立可信（M）
-《Fiction Writers on Fiction Writing》 “If I use more than one sentence of description I wince.”（M，反信号）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-08 单元停顿与后续期待

章末可暂解、未解、余波、回声或安静停顿；只有已经提出的具体承诺才登记兑现。

### 何时检查
章末平淡；读者不追下一章；幕末像断在原点；折末没有“且听下回”；连载每章都在重复“危机—解除—再危机”。

### 可观察问题（不是自动失败条件）
- 单元首末状态是否同一
  - 末句是否封死或留白墙
  - 是否给出“cue for curtain”却继续演
  - 下一单元是否兑现上一单元的承诺
  - 读者是否早已预判却一直被拖。

### 条件、动作与分支
逐单元检查状态、信息、关系、情绪或形式发生了什么，下一单元为什么需要存在。连载停顿可使用未解问题，但不得虚假惊吓后无代价撤销。记录已承诺的问题、预计兑现区间及修改；无需下一章立刻揭晓。识别读者已能预判但文本无新代价的拖延。舞台幕末暂解和戏曲小收煞、大收煞按演出条件使用。

### 失败出口
三查均无变化时再查休息、气氛和对照功能；无钩子不自动删章。

### 融合后的独有补充
C07 的落幕类比只支持检视停顿和期待，不是当代追读或每章 cliffhanger 的数据。《The art of fiction》；《Play-Making: A Manual of Craftsmanship》；《闲情偶寄》。

### 字段
`unit_end_table`（unit/state_changed/open_question/delay）、`payoff_log`（承诺→兑现）。

### 原例与反证
1. ** “opening out”**：反高潮/开放结尾可以成立；此时“未解”是设计，不是缺陷。具体适用条件见下文。
  2. **《Wild Duck》省掉“揭穿”必看场面**：改写反响仍成立；说明“幕末必须有大场面”不是硬规则。具体适用条件见下文。
  3. ** 悬念终须兑现**：为钩子而钩子、下一章不兑现，读者感到被骗。具体适用条件见下文。

### 证据定位
-《Play-Making: A Manual of Craftsmanship》 “An act… ought to consist either of a minor crisis, carried to its temporary solution”（M）
-《闲情偶寄》 “宜紧忌宽”（M，中文引文，戏曲）
-《闲情偶寄》 “七情俱备”（M，中文引文，戏曲）
-《Short Story Writing: A Practical Treatise》 “the quicker you terminate it the better”（M）
-《Fiction Writers on Fiction Writing》 “I map everything out in advance.”（M，长篇分节）
-《The writing of fiction》 过渡页（M）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-09 开篇定向与进入位置

开篇根据项目需要逐步建立人物、时空、语调和问题；晚入场与框架进入均有适用条件。

### 何时检查
开头软、读者进不去；编辑说“前三段没有故事”；说明性/历史叙事被要求“直接开打”；舞台开场交代生硬；框架故事不知从哪起。

### 可观察问题（不是自动失败条件）
- 首段末读者是否知道时间/地点/主角
  - 是否知道这是什么类型/什么情绪
  - 是否有一个可追的问题
  - 背景信息是否织进动作，而不是成块说明
  - 第一段删掉后，故事是否仍能懂。

### 条件、动作与分支
比较晚入场、典型场合、从前因开始、讲述框架四种方案。查读者在当前时点必须知道什么，区分有效留白与无法辨认行动。人物、何时何地、语调/类型、待解问题可逐步给出，不强制首段四职齐全。删首段只是比较信息与体验损益，不能因后文仍懂就证明首段无用。背景可由行动、声音、物件或叙述直接交代。

### 失败出口
信息尚未决定可先试写不同入口；没有四职不停止起草。篇幅数字与舞台重复三遍仅属历史选项。

### 融合后的独有补充
原著的 begin at the beginning 与 begin as late as possible 保留各自上下文；未证明讨论相同对象前不宣布不可化解矛盾。Rip 的框架和静态景物保留为晚入场的反例。

### 字段
`opening_contract`（who/where-when/tone-type/question）、`entry_point`、`exposition_log`（信息→承载动作）。

### 原例与反证
1. **《The art of narration》一处主张“尽可能晚”，另一处又主张“从故事开头写起”**：两种建议在作品层面未调和，不能当通则。执行条件见本条的不同分支。
  2. **《Rip》两层框架、两段静态写景仍成立**：框架/多层叙事可以违反“晚入场”。具体适用条件见下文。
  3. ** 舞台开场每个要点说三遍**：因观众迟到/不专注；小说无此强制力。具体适用条件见下文。
  4. ** 允许 withheld 开头**：但要求足够技巧与回报。具体适用条件见下文。

### 证据定位
-《The art of narration》 “Begin as late in the story as you possibly can.”（MIX）
-《The art of narration》 “begin at the beginning of the story”（MIX，反例）
-《Short Story Writing: A Practical Treatise》 “will seldom comprise more than two or three paragraphs”（M）
-《Fundamentals of fiction writing》 第一段给时间/地点/主角（M）
-《The writing of fiction》 “unless you have a salamander to show him”（M）
-《The Theory of the Theatre, and Other Principles of Dramatic Criticism》 舞台开场三遍法（M，舞台）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。

## RC-10 结尾与承诺

依作品实际承诺选择闭合、解谜、开放、仪式或混合结尾，检查末尾承担的独有工作。

### 何时检查
结尾收不住；高潮后还在解释；侦探结尾没解谜；文学结尾被要求“给个交代”；戏曲/舞台收场散；开放结尾被读者当成没写完。

### 可观察问题（不是自动失败条件）
- 高潮在哪一场；高潮后还有几段
  - 未解问题是“需要解释”还是“需要留白”
  - 开头埋的意象/问题是否回收
  - 类型读者期待的是“答案/团圆/余味/惊叹”
  - 删掉最后一段，结尾是否仍成立。

### 条件、动作与分支
列 ending_contract、climax_scene、未决线索、已完成决定和后高潮材料。明确解谜承诺需兑现其范围，悬疑不一律承诺公平谜题。开放可留下不确定、关系或余味，不必把每条线结清；不能用开放标签掩盖原先答应的答案。高潮后的解释、后果、关系转变、悼念和新状态均可有价值；删末段要比较损失，不以还能读通判断其多余。

### 失败出口
结尾未定可交付多个方案与代价；用户已授权改写就执行所选最合适的可撤销方案。

### 融合后的独有补充
保留 Lady or Tiger、White Old Maid 的不揭秘密、Forster 的 opening out 与李渔七情收煞等不同美学；不排高低，也不要求快乐结局。

### 字段
`ending_contract`、`climax_scene`、`post_climax_material`、`latent_image`、`ending_check`。

### 原例与反证
1. **《Aspects of the Novel》 “Not completion. Not rounding off but opening out.”**：开放结尾成立；但 Forster 也承认“几乎所有小说结尾都弱”。具体适用条件见下文。
  2. **《Lady, or the Tiger?》开放是为幽默效果**：作者自己把它标为例外。具体适用条件见下文。
  3. ** 侦探必须解释**：先抛谜面、倒推机关；不能用“开放”逃避解谜。具体适用条件见下文。
4. **《闲情偶寄》 古典戏曲要团圆**：“七情俱备”；现代小说不必。具体适用条件见下文。

### 证据定位
-《Short Story Writing: A Practical Treatise》 “the quicker you terminate it the better”（M）
-《Short Story Writing: A Practical Treatise》 “conclusion and the climax should be as nearly simultaneous as possible”（M）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “add another word after the climax”（M）
-《The Poetics of Aristotle》 “Every tragedy falls into two parts,--Complication and Unravelling”（C）
-《Aspects of the Novel》 “Not completion. Not rounding off but opening out.”（C）
-《The writing of fiction》 “no conclusion can be right which is not latent in the first page”（M）
-《闲情偶寄》 “七情俱备”（M，中文引文，戏曲）
-《Types of Prose Narratives: A Text-Book for the Story Writer》 “work backwards to the first step”（M，侦探）
  - 《The White Old Maid》以“秘密不揭”收束（C/FC，开放型例）

证据性质：历史方法、评论或例证；本条工作流为P，现代效果为H/NOT_PROVEN。
