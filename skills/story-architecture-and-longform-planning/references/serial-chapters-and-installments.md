# 章末与每一期（SV-09、SV-10）

返回 [SKILL.md](../SKILL.md)。空白表在 [serial-tables.md](../templates/serial-tables.md)，书目在 [serial-source-index.md](serial-source-index.md)。

本文件管分次阅读的两个位置：章末断在哪、断得多密，以及每一期本身站不站得住。钩子的具体写法（真问题还是切断句子）、兑现日志、悬念强度转 `scene-conflict-and-rhythm` 的 SU-15、SU-16；卷末的收法见 SV-04、SV-05。

## SV-09 章末落幕，下章落地

**规则**：分次读的章，末尾把动作推到一个点上收住；下一章第一句先交代时间、地点或谁在动。

**用在**：按章、按期分次发表，读者隔一天或一周才读下一章，章与章之间能切开。

**怎么做**：
1. 每章最后一到三句标收法：

| 收法 | 是什么 | 本语料的例子 | 下章怎么接 | 不算 |
|---|---|---|---|---|
| 来了一个人或一个声音 | 一个人、一条船、一声喊进入当前场景 | PG42545 L822 “Small boat two points off the starboard bow!” | 写这个人或物到了哪里、什么样 | “门外有脚步声”却不说是谁、什么时候；和本章的线无关、凭空闯入的人或枪声 |
| 一个要回答的问题 | 人物或事件提出、能执行的疑问；或者动作停在半空 | PG63483 L243–244 “Then he uttered a sudden exclamation of surprise and sprang toward the door” | 接住动作的结果，或解释刚才发生了什么 | 抽象自问“他能活下来吗” |
| 一个新事实 | 判定或揭开的信息：一封信、一份电报、一张图、一个判决 | PG42545 L1278 “Walked right into our trap!” | 写人物对这个事实的第一个反应或动作 | 叙述者的总结代替事实 |

2. “他不知道明天会发生什么”这类空悬念不算收法，改成能指认的人、物、事实。
3. 查下一章第一句：有没有时间、地点或动作？没有就补一句；不要在首句复述上一章。
4. 数同一种收法连着出现了几章。连着三章同一种，换一种或改成场景收束（起点，只是提醒）。
5. 最后一章不再挂章末钩，让位给卷末入口（SV-05）；如果本卷全闭合，最后一章可以完全收住。
6. 钩子要兑现：哪章抛出、哪章回答，记进 `scene-conflict-and-rhythm` 的兑现日志（SU-16）。

**产物**：章末检查表（serial-tables.md §6）。

**不用**：一次读完的书（章末可以是场景收束）；章与章写的是同一个场景、切开会破坏节奏；最后一章；作者有意用平收。

**卡住时**：作者不想要章末钩子，就记成“场景收束型”，只查下一章首句落不落地，不硬加。钩子太强、读者只想跳到结局的，降成“新事实”或场景收束，不靠更长的悬念解决。

**依据**：
- 原文，作者自述：PG47455 L3895–3896：“Each chapter closes with a ‘curtain.’ In other words, the chapter works the action up to an interesting point”，L3897 然后 “drops a quick curtain”。紧接着 L3898 说出版方 “will not endure inconsistency for a moment”。
- 原文，三种收法和落地的配对（都是真章末）：

| 书 | 章末 | 下一章首句 | 收法 |
|---|---|---|---|
| PG42545 | L370 “we’ll soon know if he passed Statia” | L381 “As the destroyer drew into the little port of Orange Town” | 问题 → 地点 |
| PG42545 | L822 “Small boat two points off the starboard bow!” | L832 “Very small and pitiful appeared the tiny speck” | 到场 → 接住来者 |
| PG42545 | L1278 “Walked right into our trap!” | L1288 “every one was highly elated at the successful outcome of the ruse” | 事实 → 反应 |
| PG42545 | L1812 “Submarine on the starboard bow!” | L1822 “every one leaped up and dashed on deck” | 到场 → 动作 |
| PG49197 | L1338 “Lower away!”（主角刚被推下海） | L1349 “Sixty's unprovoked and murderous attack on Matt” | 动作悬空 → 回到水里的主角 |
| PG63483 | L243 “sprang toward the door of the freighthouse” | L257 “All were surprised by Merriwell’s sudden move.” | 动作悬空 → 解释 |
| PG63483 | L908 “Then they drew aside by themselves and talked in low tones.” | L921 回到主角一方 | 密谈 → 换线 |
| PG1752 | 第 22 章末 | L7220 “At half-past ten that same evening” | 绝对时间落地 |

- 原文，平收：精装系列允许平收。PG42569 第一章以登上第一个西印度岛屿收（L428–430），第二章从 L440 “For the first few days of their stay in Nassau” 接。Conrad 的分部长篇 PG1083 共 24 章，多数章末是离场、关门这类场景收束，例如 L4277：“And the door shut after her.”
- 原文，钩子越强越好并不成立：没有读者数据能说明强度和留存的关系。
- 推断：三种收法加下一章落地，是分次阅读条件下的结构位置；“三章换一种”是提醒，没有来源证明第三章必然失效。
- 更正：旧版把 PG61174 L945（证人进门）和 PG49197 L1276（推下海）当章末钩，两处都在章中间；本版改用实际章末。旧版说 PG47455 记述“钩子过强导致连载终止”，原文（L427–432）是作者童年办胶版小报时读者围堵他提前讲结局的趣事，本版不再当反例。

**可信度**：高。作者自述一族加四个作品族；连续三章的阈值是建议。

## SV-10 每一期都不能拖

**规则**：分期发表，每一段都要单独站得住，至少推进一件事；写的人觉得长了，读者一定也觉得。

**用在**：周更、日更、分册；每一期都可能是读者决定追不追的那一期。

**怎么做**：
1. 每期写一句“本期推进了什么”：一个事实、一个关系的变化、一个决定、一次失败。写不出就合并或重写。
2. 作者自己的体感是第一道闸：写着觉得长，就在这里删。
3. 对话要推着故事走；只为抖机灵的回嘴删掉。
4. 事件要多，不能是旧的；情节可以简单，但要醒目。
5. 注水的判据和删段的方法转 `fiction-planning-and-diagnosis`（CL-09）；章内松紧和节奏转 `scene-conflict-and-rhythm`。

**不用**：一次读完、以氛围和密度为目标的文学长篇（推进的定义要先改写）。

**卡住时**：一期必须交代大量设定，就把设定拆到人物会碰到它的地方，每期只放这一期用得上的那一层。

**篇幅有下限、材料不够时**：合同规定了页数或平台要求字数，故事却撑不满，不要往里灌离题的东西。办法是讲究比例，让故事自然落到要求的长度：一个故事可以分成好几个部分；情节只需要少数几个人物时，可以让它在更多人物身上展开；可以加副线，但每条都要帮着说明主线。对话最容易离题，不朝主线走的那段就删。仍然撑不满，就改容量（SV-13），不硬凑。

**依据**：
- 原文：PG5978 L3609–3611：“The production of novels in serial form forces upon the author the conviction that he should not allow himself to be tedious in any single part.”；L3615–3616：“he cannot afford to have many pages skipped”。
- 原文：PG5978 L5930–5932：“When once the sense that the thing is becoming long has grown upon him, he may be sure that it will grow upon his readers.”
- 原文：Cook 写给丛书作者的要求，PG47455 L3902–3907：对话要“moves the story along”；“A multitude of incidents--none of them hackneyed--is a prime requisite.”；L3906–3907 “The plot must be simple, but it must be striking.”
- 原文：Trollope 回答“合同规定了页数怎么办”，PG5978 L5850–5851：“by studying proportion in his work, he may teach himself so to tell his story that it shall naturally fall into the required length.”；L5854–5856：“There may be subsidiary plots, which shall all tend to the elucidation of the main story”；对话 L5867–5869：只有“as long as it tends in some way to the telling of the main story”才讨人喜欢。
- 推断：分期发表让“单期可读”成为硬约束；Trollope 自己也承认分期写作的人（PG5978 L3612–3613）“will often be tedious”，这条是要求，不是保证。

**可信度**：中。两个作者族的自述。
