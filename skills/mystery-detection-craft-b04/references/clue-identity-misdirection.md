# 线索、身份与误导（R1′ / R2′ / R3′ / R9′）

## R1′ 线索发现即描写（判据＝"对读者可见"）

**规则**：结尾要用的每个物证/细节，必须在发现它的那一刻写给读者；揭示段只允许**重新解释**，不允许**首次出现**。判据是**读者能不能在此之前看到**，不是"所有角色是否都知道"。

**逐字级证据**
- `PG54445` L1029 / L1047：首例未尸检（"We thought that was a 'fade-out.'"）、次例由 Bear 亲做尸检结论 "There were no findings." —— 尸检的"有/无"在第一时间就交代给读者，阴性结论本身成为线索。
- `PG54445` L6010-6012：替代动线（各层 porch 由窄混凝土楼梯相连、宽到可过担架）**存在但被当场封死**——"the door to that porch is always locked at night. The key is on the inside." → 给替代路径再排除，比"根本不提"更公平。
- `PG1661` L3746-3747：跛足依据"右脚印记总比左脚浅"（重心少压在右脚）。
- `PG70634` L1058-1090：口径 ".45 army bullet—Colt automatic"、射距 "Between five and six feet"。

**台账级证据**：`PG863` L3178-3210（信封涂鸦 "possessed"＋新种秋海棠 → 推新遗嘱存在）；`PG68679` L3221-3232（黄纸小条水印 "Copy" = 记者用纸）。

**合法变体（R1′ 相对 R1 的修订）**
- `PG78220` L6897-6928：第一人称叙述者在自己书房发现地毯血渍与一枚亮蓝色小物件，**对妻子隐瞒**（答"没什么"，等她离开才摊开手）。细节对读者可见、对书中人不可见。<br>分段锚点（本轮 `awk NR>=6893 && NR<=6932` 实读）：血渍 L6897-6898／蓝色小物件 L6904-6906／妻子进屋与"Nothing." L6908-6919／等她离开后摊开手 L6928（青金石耳环 L6930-6931）。
- `PG78220` L1601-1608：叙述者连续三次试图说明"关于那口钟"的事，都被警方以 "absolute silence"/"Time's short" 打断 → 读者与叙述者共同持有警方所缺的信息。

**不适用**：类型本身不承诺可解；或凶手视角的隐瞒——但隐瞒必须是"叙述者没说"，不能是"伪造事实"，且结尾要给读者可回查的空白。

**检查问句**
1. 遮住最后 20%，我能否指出"哪一句描写"支持结论？
2. 这句话在发现场景，还是在揭示场景才第一次出现？
3. 若删掉揭示段的口述，读者还剩下什么可看？
4. 若用第一人称隐瞒：读者看到了吗？结尾给了可回查的空白吗？

---

## R2′ 识别链分级（≥2 条，且 ≥1 条不可临时改变）

**规则**：凡是"身份误认"型诡计，至少给两条互相独立的识别链；**并且必须标注每条"凶手能否临时改变"，保证至少一条属于不可改变类**。只靠一条（如衣服）会让读者觉得"作者说像就像"。

**为什么必须分级**
- `PG54445` L3191-3192：两名医生以"His queer walk, MacArthur. One shoulder higher than the other.... And we both saw it."指认 Cub。
- 而全书真凶的伪装正是"剃中间头缝凸显秃斑＋发蜡后梳改变额线＋模仿 Cub 的'左肩高'棱角姿态"（`_resume-PG54445.md` 结案要点），终局以"那双眼睛的颜色和 Cub Sterling 的一样"（L9117-9121，[台账]）收束。
- 同时 `PG54445` L3194 MacArthur 立刻反驳："neither of you saw his face" → 作者把"步态可被模仿"这件事提前埋进了同一段。

**两类识别链**
| 类别 | 例子 | 来源 |
|---|---|---|
| **可临时改变**（必须有第二条补位） | 衣物/发式/化妆 | `PG863` L4285-4314 伪装＝"可复制特征"（衣服＋胡须＋眼镜）[台账] |
| — | 胎记 | `PG56237` L7820 "You painted the birthmark on your face?"（本轮 `awk NR==7820` 实读确认；PG75642 全书 `grep -ci birthmark` = 0）[台账] |
| — | 名字 | `PG75642` L6009-6016 "The man she had known was Hugh Dwyer. Curran was a new name to her." [台账] |
| **不可临时改变**（至少一条） | 创口/器械形态 | `PG68679` L6063-6067 刺创周长通常小于凶器，"可能是细长剪刀所致"[台账] |
| — | 负重与步态习惯 | `PG1661` L3746-3747 [逐字] |
| — | 笔迹 | `PG56237` L4824-4826 "I know by comparison of handwritings." [逐字] |
| — | 无意识动作 | `PG75244` L8278-8283 凶手用残指熟练卷烟，三双眼睛同时盯着那只手 [逐字] |

**物证归属可转移（陷阱）**：`PG55348` L2016-2032 / L4236-4275 绿松石戒指曾失窃、由他人拾得佩戴 → 物证指向人，不等于指向持有人。

**检查问句**
1. 两条链里有没有一条是凶手在案发当天临时改不了的？
2. 这条链是否在案发前被独立描写过（不是只在揭晓段出现）？
3. 物证的"指向"是持有人还是使用人？

---

## R3′ 错误权威框架（正当性来自方法论的不确定区间）

**规则**：先让一个**有资格**的人给出错误但方法论自洽的结论。错误的来源必须是**该方法论本身的不确定区间**，不能是专家愚蠢，更不能是"印象"。纠正必须靠同一方法论内的新事实，不能靠作者宣布。

**正例（专家自陈不确定）**
- `PG54445` L2126-2127："Toxicology, like other branches of the Profession, is partly guess work." [逐字]
- `PG68679` L6063-6067：法医指出刺创 circumference 通常小于凶器（皮肤被撑开），故"可能是细长剪刀所致"——凶器**未被唯一锁定**，为"另一把刀/另一把剪"留口。[台账]
- `PG70634` L10448-10487：Hagedorn 用珠宝放大镜逐段对光看了近五分钟，只说"可能是这把，不敢确定"，要拿 helixometer 再看。[逐字]
- `PG54445` L1970-1974：第二助理化学师明确"have not proceeded with any obscure tests"，拒绝越权深入 → 既制造滞后，又避免长篇讲义。

**失效条件（明确写成反模式）**
- `PG54445` L5168-5169：精神科医生只给出 "His hands, the hysterical set of his left shoulder, the peculiar light which comes into his eyes...."；被追问 "Have you any evidence, yes or no?" 后答 "No."（L5177）。**印象型侧写不得充当错误框架**。
- 同书 L1083 另一处更轻的错误假说是 "Fear psychosis"，当场被动作驳回（L1085-1086）。

**纠正的正例**：`PG55348` L983-1001 埃及学朋友当场纠正侦探假设——"非埃及乃秘鲁印加墓俑（日纹胸饰）"。[台账]

**"多派假说并列"的扩展用法**：`PG55960` L1684-1685 / L1901-1941 / L2082-2103 三派凶手论（Dean guilty / Dean innocent / Gilmar 杀 Kirkstone）长期并列不收敛；`PG73126` L1887-2086 三视角推理擂台，每次结论都明写为**可撤回的假说**；`PG56237` L6801-7300 "to theorise is the only way... One may have a dozen theories, and then can abandon each one in turn"。

**检查问句**
1. 若我是该专家，会不会也这么判？（不会 → 那是作者偷懒）
2. 纠正它用的是"新事实"还是"作者特权"？
3. 读者在第几处能第一次怀疑这个权威？为什么？
4. 我给的是"方法论的不确定"还是"性格/印象"？

---

## R9′ 多证人契约与盲区

**规则**：用多视角/证词体时，先立"每个人只说自己亲历"的契约，再给每个证人一个**可被读者记住的盲区**（看不到、听不到、理解错）。证词之间的缝隙就是线索；不要让某个证人全知。

**操作化版本（`PG54445`，全部逐字级）**
1. **隔离问询**：L2223-2224 "call them quietly ... and separately"。
2. **离场加誓**：L2459-2460 "two years ago you took an oath concerning silence"。
3. **书面化**：L5185-5263 Cub 的正式证词——含时间、在场者、本人行踪，以及"因 Mattus 的先见，从外科借来术后病人推入 Rose 原床位，并对病人称 Rose 已转私人房间"的现场替代与口径统一。
4. **盲区随证词一起交付**：L2502-2505 工友 William 坚称 "it's as hard to get past me as a watchdog"，同时交代自己"当时在厨房"——**每份不在场证明都自带盲区**。
5. **区分"感觉"与"看见"**：L2351-2353 "suddenly I felt someone passing in the corridor... There was no one in sight."
6. **先确认记忆机制，再取用记忆内容**：`PG70634` L9765 → L9767 "Why, his brother was murdered that night!" → L9769-9771 Vance 复述并要求确认。

**加强版（仅限封闭机构/专业群体，不得泛化）**
- `PG54445` L6302-6306："One thing you got to remember is you are up against professional liars. All nurses and doctors are professional liars. Didn't one tell me my mother was 'doing nicely' when she had been dead an hour? So watch everybody in the same way you watch a spy."
- 适用：医院、学校、企业、教会等封闭机构题材。**不适用**：把"所有证人皆说谎"当成普遍设定——那会摧毁公平性本身。

**书面报告作为取证载体**：`PG78157` L6461-6587（Climpson 的书面报告）[逐字]；`PG54445` L1981-1982（把口头结论强制转为"typed report ... by nine this morning"）。

**检查问句**
1. 每个证人不知道什么？这个盲区是否在证词**之前**建立？
2. 删掉一个证人的证词，读者会失去哪条线索？
3. 有没有证人"恰好"知道太多？
4. 我有没有把"感觉到了"写成"看见了"？
