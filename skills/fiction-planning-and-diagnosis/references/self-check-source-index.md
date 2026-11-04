# 来源索引

返回 [SKILL.md](../SKILL.md)。行号 `L` 指 Project Gutenberg 转录本“整本阅读版”的行号，不是原书页码。引文只取短句。

## 1. 两本书

| Source ID | 作者 | 作品 | 版本 | 正文范围 | 转录本 SHA-256 |
|---|---|---|---|---|---|
| PG51010 | F. Marion Crawford（1854–1909） | *The Novel; What It Is* | Macmillan，纽约与伦敦，1893 | L40–1099；L1103 以后是出版社书目广告 | `d4260a9a92d16146388955e56623f077bfb004fb77a10fb7eb09eb63be69ecc8` |
| PG76460 | Walter Besant（1836–1901） | *The Art of Fiction* | 1884 年 4 月 25 日皇家研究院讲稿；Chatto & Windus，伦敦，1902 年新版 | 讲稿 L35–945；注释 L946–1006；附录 L1011–1103 | `3327b4efb9b4a884785ebac38855b17404b19d52ae17a1531a96b3779ebe168d` |

两书同代、同语言、同一个书市，作者都是当时的畅销小说家，用的是同一套剧场比喻和同一批经典。它们一致的地方是同一传统内部的会合，不算两个独立来源的互证。1884 年初刊和 1902 年版之间的文字差异没有核对过。Henry James 1884 年回应 Besant 的同名文章不在本 skill 的来源里。

## 2. 测试与来源

| 测试 | Crawford（PG51010） | Besant（PG76460） | 说明 |
|---|---|---|---|
| CL-01 契约 | L79–81 “marketable commodity”；L85–86 “intellectual artistic luxury”；L102–103 “amuse and interest”；L112–113 “unwritten contract tacitly existing between writer and reader”；L218 “public amusers” | L44–48 “sister and the equal”；L84–124 小说地位低；L852–853 市场失败不等于艺术失败 | 两栏小说观是两书的立场；两行模板是本 skill 的设计 |
| CL-02 说教 | L108–113；L154 “a simple fraud”；L157–159；L180 “the moral lesson is a mistake”；L240–244 | L623–624 “conscious moral purpose”；L634–636 “practically a law of English Fiction”；L638–639 “the preaching novel is the least desirable of any” | 三层拆分和反读测试是本 skill 的设计 |
| CL-03 设定与景物 | L785–799 | L222–256；L235–236 “the human interest must absolutely absorb everything else” | 两书同向 |
| CL-04 经验账本 | L785–787 “experience of men and women”；L800–802 “I would almost say that”；L885–895 | L389–421；L408–409 “never to go beyond your own experience”；L948–975 历史小说的例外 | 账本是本 skill 的设计 |
| CL-05 三场景与删名 | L798–799 “moving before the eye of his mind” | L543–544 “If they do not grow and become every day clearer”；L546–548 “kill and bury”；L576–595 塑造人物的几种方法 | 三场景和删名是代理测试 |
| CL-06 事实契约 | L667–746；L729–731 “historical facts are limitations” | L948–975；L957–962《罗慕拉》“great as a study”；L966–967 “when he must describe, he must borrow” | 三种契约是本 skill 的设计 |
| CL-07 人物双审 | L810–813 “altogether impossible”；L885–887 “surroundings which never were and never can be possible” | L397–399 “must be real, and such as might be met with in actual life” | 两书冲突；“反应可理解”是本 skill 取的共同点 |
| CL-08 场面表 | L481–494；L491–492 “illusions of a good play”；L882–930 小说比舞台自由 | L521–533；L527–528 “a novel is like a play”；L532–533 “from the front” | 同一个剧场比喻，不算两份证据 |
| CL-09 无功能才删 | L534–535 没有形状的颜色；L638–643 | L505–519；L513–515 不推进故事的删去；L994–998 大量场景从未落到纸上 | “无功能才删”是本 skill 的放宽 |
| CL-10 写完 | | L675–676 “completely and carefully finished” | 单一来源 |
| CL-11 双栏 | L429–430 吸引读者；L826–828 “appeal to the heart”；L963–983 | L735 “the story is everything”；L736–743；L741–743 “as impossible as life without uncertainty”；L745 | 两种优先级 |
| CL-12 复述 | L504–505 “The means, all subservient to language, are many, but the object is always one”；L504–513；L516–517；L561 “not the place for a study of methods” | | 复述测试是本 skill 的设计 |
| CL-13 修订 | L436–437；L544–546 “clever handling of grammar and a careful selection of words” | L643–681；L652–653 “a single sentence carelessly worded”；L656–661 风格压过情境；L665–667 “cannot be made beautiful by attention and pains”；L667–673 一气写成的例子 | 轮次表是本 skill 的设计 |
| CL-14 可教性 | L43–60 自称意见；L496–501 诀窍无数 | L50–53 法则可精确传授；L376 “Rules will not make a man a novelist”；L747–748 “the Art itself can neither be taught nor communicated” | Besant 前后有张力 |
| 方言 | L522–558；L528–531；L538–539；L553–556 | | 只保留读者成本的问题 |

## 3. 不作为规则的历史主张

| 主张 | 出处 | 为什么不采纳 | 可以保留的部分 |
|---|---|---|---|
| 小说必须有自觉的道德目的 | PG76460 L623–636；对照 PG51010 L180 | Besant 的“法则”是对 1884 年英国书市的描述；Crawford 明说道德教训是错误；两人都反对说教 | 道德氛围、同情、后果 |
| 人物必须像真人，不得越出个人经验 | PG76460 L397–409 | 与奇幻、科幻、寓言冲突；Besant 自己给历史小说开了例外；Crawford 允许不可能的人物 | 反应可理解；字面可能性按体裁定 |
| 所有段落都必须推进情节 | PG76460 L513–519 | Besant 同时要求每场写完；“推进”的定义太窄 | 无功能才删 |
| 语言只是媒介，所以语言技巧不重要 | PG51010 L504–517 | 媒介论推不出“不需要语言层”；两书只是没有给出方法 | 语言是唯一媒介；风格靠修改 |
| 小说法则可以像和声、透视一样精确传授 | PG76460 L50–53 | Besant 自己在 L745–748 说艺术不可教，全文也没有交付一条精确的法则 | 手艺检查表可以教 |
| 好稿必被接受；被六家拒绝就放弃；绝不自费 | PG76460 L1040–1041、L1056–1058、L1068–1069 | 1884 年三卷本时代的出版条件，没有代理、自出版和数字平台；被拒的经典很多 | 投稿前先写梗概 |
| 非历史小说不写有年代感的细节；方言必然缩小读者；各民族小说家分高下 | PG51010 L638–640、L553–556、L967–971 | 年代质感是很多类型的乐趣；方言文学已是重要的美学；民族本质论无法检验 | 细节服务人物；方言有读者成本 |
| 小说应以爱情为主，干净甜美 | PG51010 L422、L427 | 这是 Crawford 描述的 1893 年“完美小说”的理想，他自己说“请不要真去构想它”（L437–440） | 立体的真实胜过平面的照片（L430–431） |

其他只作历史背景的说法：
- “年轻姑娘读者”决定英语小说的尺度（PG51010 L272–294）：1893 年的出版审查结构。同一段里 Crawford 也说这是“时代的坏兆头”，又说“我们毕竟都是男人和女人”，要一起读。
- 小说是十八世纪末突然出现的，源于大革命带来的情感习惯（PG51010 L458–468、L1031–1048）：文学史上的猜测，Crawford 自己称之为“guess”。
- 不要追求全新的情节，“你做不到”（PG76460 L1066–1067）：三卷本时代的原创观。

## 4. 引用时的注意事项

- 引 Crawford 关于经验的话时，带上他的保留：“I would almost say that”（L800–802），不要读成无条件的断言。
- 引“人物必须真实”时，两边一起引：Besant L397–409，Crawford L810–813 和 L885–895。只引 Crawford 允许不可能人物的一面（L885–895），会把他读成“随便写”。
- Besant 说的道德“法则”，指作品里弥漫的道德意味，不是“每本书都要写一个论题”；也要和他反说教的话（L638–639）一起引。
- 不要说“两书没有任何语言评价”：Crawford 有关于语法和选词的劝告（L544–546）和对语言变化的赞赏（L436–437），只是没有系统的方法。
- 不要把 Besant 说国王贵族“主要因为漂亮的服装才有画面感”（PG76460 L919–921）当成“别写国王”的经验规则：那是他对未来小说将取材于“广大奋斗着的无名大众”的预测（L914–922）。
- Besant 关于销量和图书馆借阅比例的数字是书中的说法，没有独立核实。
