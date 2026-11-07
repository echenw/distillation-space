# 预设卡的诊断与修订

本文用于解释批评意见、定位已有卡片的问题、修订卡片和审校一组卡片。生成新卡的方法见 [card-method.md](card-method.md)；质量高的卡也会出现的缺陷及其改法见 [card-pitfalls.md](card-pitfalls.md)，本文不重复那些改法。

## 诊断步骤

1. **取证。** 指出原句、位置和本卡的目标。缺少原句或上下文时，说明哪一部分无法确认。
2. **分清三种情况。** 卡片条款本身有缺陷；条款没有问题，是正文没有照做；批评意见本身不可靠。第三种按 [card-pitfalls.md](card-pitfalls.md) 末尾“冲突批评的裁定顺序”处理。
3. **归到根因，再定位缺陷。** 先按下一节判断属于哪一类根因，再到缺陷目录中找到对应条目。同一原句可以命中多个缺陷，说明它们的关系，不重复报告。
4. **按根因修改。** 补机制、判据、界线、替代或缺失内容。只要求诊断时给出建议，不改写文件；要求修订时交付完整的卡。
5. **复读。** 检查修改处与其他条款、示例是否冲突，是否新增了机械配额、新的套路或无法核实的豁免。

诊断的每一项写成：原句 → 触发条件 → 为什么妨碍执行 → 改法。

处理顺序：先处理定位错误、条款冲突、示例违规、豁免架空和事实错误；再处理覆盖和可执行性；最后处理冗余和文本问题。顺序取决于对成稿的影响，不取决于缺陷被点名的次数。

## 五类根因

有缺陷的卡的问题可以归为五类上游根因。修订时对准根因，一次修改可以消除同类的多处问题。

| 根因 | 判断时提的问题 | 修法 | 修法的边界 |
| :--- | :--- | :--- | :--- |
| 数量要求没有刻度 | 这一条是数量问题吗？数的是什么，在多大范围内数？ | 补数字、单位、生效范围和终点 | 不为凑数给每条加数字；不规定“每张卡至少几个数字” |
| 条款之间没有检查过冲突 | 把所有祈使句两两配对，是否有“同一对象、相反动作”？ | 划出稿面可见的界线，或定先后，或合并为一条带条件的规则 | 不以删除用户的关键要求换取一致 |
| 判据不可核对 | 遮住形容词和口诀后还剩什么？成立与否由谁判断？ | 换成能数、能查、能判、能演的判据 | 语义要求不强行数字化 |
| 只禁止，不建立 | 被禁的位置改写什么？ | 禁令与同位替代成对出现 | 替代不能成为新的固定套路 |
| 缺少交付前检查 | 文本是否完整、干净、不重复？ | 逐项执行下一节的文本检查 | 不声称做过没有做的检查 |

前两类各自只需一道固定检查即可大面积消除，修订时优先处理。

## 交付前文本检查

- 引号成对，使用中文标点。格式有字数限制时逐项核对；字数按含标点的非空白字符数计，小节标题行不计。
- 没有病句、残句和指代不明。
- 没有占位符、模板字段、重复的标题和未作答的提示问句。
- 每个栏目的内容回答的是该栏目的问题。
- 没有无意残留的外文词。
- 没有自我评价和推销语句。
- 与同一组内其他卡片没有逐字相同的段落。发现相同时，不把它们当作两份独立意见。
- 字数在格式规定范围内。

## 缺陷目录

缺陷标识用于在审校一组卡片时归组。目录分两部分：第一部分的缺陷在 [card-pitfalls.md](card-pitfalls.md) 中有症状示例和改法，这里只给出对应条目；第二部分是只在本文说明的缺陷。

### 第一部分：见 card-pitfalls.md

| 缺陷标识 | 条目 |
| :--- | :--- |
| `specificity.no-countable-threshold` | 第 1 条 |
| `specificity.uncheckable-value-word`、`specificity.subjective-effect-as-criterion`、`specificity.metaphor-as-criterion`、`specificity.circular-definition` | 第 2 条 |
| `specificity.unmeasurable-unit`、`scope.unbounded-range` | 第 3 条 |
| `pacing.per-chapter-quota-backfire`、`exception.exemption-missing`、`specificity.threshold-misdesigned` | 第 4 条 |
| `self-contradiction.clause-collision` | 第 5 条 |
| `example.sample-violates-own-rule`、`example.physically-off` | 第 6 条 |
| `exception.exemption-guts-rule` | 第 7 条 |
| `over-constraint.absolute-ban-collateral` | 第 8 条 |
| `requirement.ban-without-replacement` | 第 9 条 |
| `exception.blacklist-bypassable` | 第 10 条 |
| `cliche.new-tic-prescription`、`cliche.stock-imagery-as-positive`、`over-constraint.identity-stereotype-binding` | 第 11 条 |
| `requirement.unexecutable-abstraction`、`structure.noun-chain-as-mechanism`、`terminology.undefined-jargon`、`terminology.cross-domain-borrow`、`terminology.misused-word` | 第 13 条 |
| `requirement.option-menu-no-decision` | 第 14 条 |
| `requirement.coverage-gap`、`requirement.cost-consequence-missing` | 第 15 条 |
| `genre-fit.interchangeable-generic`、`genre-fit.axis-drift-onto-other-genre`、`scope.applicability-misjudged`、`scope.off-axis-overreach` | 第 16 条 |
| `pacing.escalation-without-ladder` | 第 17 条 |
| `structure.runon-no-split`、`text-hygiene.broken-delivery` | 第 18 条 |
| `example.no-sample-at-all` | 第 19 条 |
| `redundancy.same-sense-restated`、`redundancy.detached-boilerplate-tail` | 第 20 条 |
| `over-constraint.typography-as-style` | 第 21 条 |
| `pov.conflicting-mode`、`pov.switch-guard-missing` | 第 22 条 |

以下症状归入上表已有的缺陷：禁用词表以“这类”“不限于”开口，归 `exception.blacklist-bypassable`；禁令只管段末，章末同样的写法没有管到，归 `requirement.coverage-gap`；多项并列不排主次，归 `requirement.option-menu-no-decision`；章末钩子固定为一两种，归 `pacing.per-chapter-quota-backfire`。

### 第二部分：本文说明的缺陷

症状列里的引句是缺陷的样子。这些缺陷集中出现在写不出可照做条款的卡和条款不稳定的卡上。

| 缺陷标识 | 症状与示例 | 修改方向 |
| :--- | :--- | :--- |
| `requirement.effect-as-goal-no-method` | 只写想要的效果，不写达成手段。例如“掌控规则”，是摸到底层逻辑、拿道具还是直接成神毫无区分，等于许愿 | 保留效果目标，紧跟达成手段和稿面上的证据 |
| `requirement.symptom-without-check` | 只有病名，没有查法；或把判断交还给写作者的自觉，如“心里要有账”“自己把握”。“避免”栏三条只有病名，一句可回查的问话都没有 | 改为查什么位置、看什么信号、命中后怎么改 |
| `requirement.soft-wording-not-binding` | 用“尽量”“适当”“可以考虑”“少”作约束 | 补条件、额度或判例。只删除这些词不算修改 |
| `requirement.dimension-gap` | 格式规定的栏目缺失或空置 | 补入实质内容 |
| `requirement.section-off-prompt` | 栏目内容答非所问，例如加码栏写的是质量口号；或把条款写成提问 | 按该栏目应当回答的问题重写 |
| `requirement.domain-fact-error` | 题材常识、史实或行业事实有误。例如开篇断言“读者不爱看主角幸存”，末世题材吃的就是怎么活下来 | 核实后修改；无法核实时收窄表述或写明不确定 |
| `exception.exemption-restates-requirement` | 例外栏只是把主要求重复了一遍 | 删除；确有例外时另写触发条件和边界 |
| `exception.wrong-target` | 豁免放行了不应放行的对象，例如以“这是角色台词”为由免除事实一致 | 写明豁免解除的是哪一项限制，其余限制保留 |
| `over-constraint.harmful-prescription` | 正面要求本身有害，照做即出问题。例如“大量使用感叹号和省略号制造紧张感”——把标点当节奏使，照做正文必满屏感叹号和省略号；“多用温和的语气助词（如啊、呀、呢）”——照做二十章，人人“好呀”“对呢”“来啦”，满屏嗲腔；“每句话都要让读者得到新东西”——照办就是电报体 | 推演这条要求连用二十章的结果；改为带条件的方法并加护栏。过渡句和节拍句允许存在 |
| `self-contradiction.prose-violates-own-rule` | 卡片的行文与它提倡的写法相反。例如讲“冷面”的卡写得最热最满，先把自己的规矩破了；“很少使用副词与形容词”，正文却连着“留白极大”“极度干练”“极度克制” | 删去卡片行文中的程度副词和评价。小说正文的句法限制不自动适用于说明文字，但示例必须遵守 |
| `self-contradiction.recipe-is-own-ban` | 给出的补救方案落入本卡的禁项 | 把补救方案与禁项、崩点逐条对照后修改 |
| `scope.real-name-or-ip-borrow` | 搬用现成名句或真实作品。例如范例直接搬现成的名句当标准；“避免”栏明写“只学语感，不搬内容”，示例却搬得最彻底 | 示例原创；把想学的特点写成自己的条款 |
| `reference.unexplained-benchmark` | 以读者认不出的对象作对标，并且不说明学它的哪一点 | 换成可执行的风格特征 |
| `terminology.code-mix-residue` | 中文条款中残留外文词作机制名 | 给出中文说法；必要的专名保留 |
| `voice.promotional-self-praise` | 卡片自我评价或推销。例如“是新手作者最安全的选择，也是老手返璞归真的体现”——这种头衔句一句都落不到笔上；“烧脑体验优秀”是给自己打分 | 删除 |
| `voice.narrator-announcement` | 卡片要求或示范了叙述者出面点题、宣布意义 | 删除没有新增内容的总结；叙述者的口气另按文风卡的“叙述”一节确定 |
| `outline-pollution.template-residue` | 模板字段、提示问句、占位符留在成品中。例如四个栏目开头抄的是通用模板问句、无一处作答，占去近三分之一篇幅 | 删除残留，填入实质内容 |
| `density.long-but-empty` | 篇幅长，可执行的内容少 | 删除复述，补入缺失的做法、条件或示范，再压缩 |
| `dialogue.uniform-voice` | 卡片要求人物口气各异，示例或条款却使所有人一个腔调。例如“粗人的句子短而硬，读书人的句子绕一点”，通篇零演示 | 在示例中演示两个人的差别；按说话动机区分，不按身份分配句式 |

## 写不出可照做条款的卡的共同特征

这类卡的主要问题是写不出可以照做的条款：抽象名词罗列、软性措辞、没有示范、条款互相冲突，另有模板残留、自我评价和有害的正面要求。审校一组卡片时先筛查这几项，可以最快分出不可用的卡；这类卡不提供任何可以借鉴的写法。

## 审校一组卡片

1. 逐卡执行诊断步骤，记录原句和缺陷标识。
2. 按缺陷标识归组，找出多张卡共有的问题。共有的问题通常指向同一类根因，优先统一处理。
3. 按对成稿的影响排序，给出逐卡问题和共性问题两部分。
4. 有对照文本时检查逐字相同的段落。相同模板不等于抄袭，但相同文本不能算作两份独立证据。
