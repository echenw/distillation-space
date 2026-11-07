# 去来源自检 · genre-fiction-craft（G06-a5 · 历史架空 两谱系合片 power-machine ＋ craft-b03）

- 片号：**G06-a5**｜W3 主体轮第 15 批｜日期：2026-11-05｜性质：**静态只读自检**（未写 `output/`，未运行测试／lint／构建／应用，未做任何 git 写操作，未检出、未切换分支）
- 扫描对象：`notes/loss-inventory/genre-fiction-craft-G06-a5.md` 内 **18 条补丁新文**（P01–P18；`/usr/bin/grep -c '^- 新文：'` 实测 18，与 `^补丁 \*\*P` 计数 18、`^- 定位锚：` 计数 18、`^- 动作：行内追加` 计数 18 一致）
- 扫描方式：`/usr/bin/grep -h '^- 新文：' <记录> | /usr/bin/grep -cE '<模式>'`（计划第 495 行口径：本机 `grep` 为 ugrep，中文长模式报 exceeds complexity limits，统一用绝对路径 `/usr/bin/grep`；未使用本机默认 `grep`）
- 本片范围：v0 两谱系 27 文件 **90686 B**（power-machine 15 文件 47208 ＋ craft-b03 12 文件 43478）；r2 行段 **2713–2796（84）＋ 2867–2935（69）＝153 行 ＋ 14 补判＝167 单元**；决定 **50 条**（LI-GE-1321–1370）
- 落点目录：`output/genre-fiction-craft/references/06-historical-alternate/`（十件，盘上当前 100261 B）

## 一、开工基线自判（简报第 7 节三条）

| 检查 | 实测方法与结果 | 结论 |
|---|---|---|
| 逐件字节 | `wc -c` 十件＝`examples 13654｜guide 5915｜historical-fiction-patterns 25836｜history-contract 9452｜institutions-and-documents 7811｜livelihood-and-action 8528｜narration-and-period 7715｜relationships-and-belief 5540｜settlement-and-revision 4574｜templates 11236`，合计 **100261 B**；`git ls-tree -r -l 2a10c07` 同目录 v3 合计 **83675 B** | **盘上已不等于 v3 原态**，净增 16586 B |
| 内容等值（不只比字节） | 逐件 `git hash-object <盘上文件>` 与 v3 blob id 比对：`examples`／`guide`／`historical-fiction-patterns` 三件 **SAME-as-v3**；`history-contract`（a9e0ddfd…）、`institutions-and-documents`（51a611e2…）、`livelihood-and-action`（ec4be500…）、`narration-and-period`（5374ead1…）、`relationships-and-belief`（4cb3dc37…）、`settlement-and-revision`（977db441…）、`templates`（6db27041…）**七件 DIFFERS** | **开工基线＝v3 ＋ 本批 a1／a2／a3 的已落笔补丁**（题材 06 目录在本批内已被主代理写入），非 v3 原态 |
| mtime | `/usr/bin/stat` 实测：七件 DIFFERS 文件全部 **2026-11-05 14:01:32**，三件 SAME 文件 **03:59:01**；本轮开始时点晚于 14:01 | **登记事实**：题材 06 目录 7 件的新 mtime 与本批前几席的落笔时点一致（`notes/loss-inventory/genre-fiction-craft-G06-a1/a2/a3.md` mtime 13:49–13:50）；本席未做并发写入探测，不猜其它成因，按盘上态继续取锚 |
| 锚来源 | 18 个定位锚**只从当前盘上文件**逐字摘录（`Read` ＋ `/usr/bin/grep`），未从任何提交内容或他席记录抄取；其中 5 个锚（HI-01／HI-03／HI-05／HI-25／HI-70）本身就是本批他席刚落笔的段末句，已在记录「可能同点清单」标明先后 | 合规 |
| 跨目录引用 | 本片落点全部在题材 06 目录内；对 04／05／11 目录**零引用、零取锚**（判定基准侧只读 v1／v2 的 06 目录与 v0 谱系原文，不进 `output/` 之外的题材目录） | 合规 |
| 他席共用文件 | 简报明示 06 目录 10 件为多席共用：本片动 5 件（institutions 6 条、livelihood 6 条、history-contract 3 条、settlement 1 条、narration 1 条、templates 0 条），全部只给**行末块级锚**，不整节重写、不改小节标题、不动 HI 编号、不新增编号；与 a1／a2／a3 的 5 处同点按席位序写明 | 合规 |
| 动作标签合规 | 18 条全部 `动作：行内追加`，且落点全部是**散文／条目行**（各 HI 卡的「**怎么做**：」行末），**不含任何 Markdown 表格行**；本片未对机制卡表或模板表使用行内追加（模板 38 行判在位，见 LI-GE-1370），故无「竖线外甩内容」风险 | 合规 |
| 新文单行 | `awk '/^- 新文：/{print NF}'` 与 `grep -c $'\n'` 侧测：18 条新文各占一行，无换行、无小节标题；未使用 `新增小节` 与 `精确替换（子串）` | 合规 |

## 二、附录 B 全 11 类计数（对 18 条新文，逐类打印命中数）

| # | 目标 | 模式 | 命中 |
|---|---|---|---|
| 1 | 书名号里的作品名 | `《[^》]+》` | **0** |
| 2a | 来源编号 | `PG[ -]?[0-9]+` | **0** |
| 2b | 来源编号残片 | `(^`\|`[^A-Za-z0-9])-[0-9]{3,5}([^0-9]`\|`$)` | **0** |
| 3a | 来源数量 | `[0-9]+ ?本(材料\|书\|手册)` | **0** |
| 3b | 材料标称 | `材料标称` | **0** |
| 3c | 来源年代＋场域 | `(1[5-9]\|20)[0-9]{2} ?年(代)?.{0,8}(市场\|手册\|杂志\|出版\|建议)` | **0** |
| 4 | 指向学习材料的说法 | `书内\|书里\|同书\|该书\|此书\|原书\|来源是\|出自\|引自\|据称\|这批材料\|学习材料\|原文库\|批次` | **0** |
| 5a | 作家／名著类词 | `作家\|小说家\|评论家\|大师\|名著\|经典作品` | **0** |
| 5b | 拉丁字母人名 | `[A-Z][a-z]+ [A-Z][a-z]+` | **0** |
| 6 | 英文原句 | `"[A-Z][a-z]+( [a-z]+){4,}` | **0** |
| 7 | 包外路径 | `notes/\|results/\|/home/\|materials/\|rounds/` | **0** |
| 8 | 改动痕迹 | `旧版\|本版\|更正\|早先的版本\|融合版\|上一版` | **0** |
| 9 | 审计词 | `NOT_PROVEN\|VERIFIED\|NOT_RUN\|STATIC_CHECKED\|DESIGN_EXAMPLE\|OBSERVED\|F/H/P\|GQ[1-5]\|R1[78]` | **0** |
| 10a | 删除后空括号 | `（\s*）\|\(\s*\)` | **0** |
| 10b | 「见」悬空 | `见[，。；]` | **0** |
| 10c | 「据」悬空 | `据[，。；]` | **0** |
| 10d | 「与…同」残迹 | `与\s*同` | **0** |
| 11 | 分档词与禁用说法 | `夯\|拉完了\|硬规则\|用户明确要求` | **0** |

- **11 类拆成 13 组模式，全部 0 命中**，无 B.2「命中后写允许理由」的条目。
- 上批三个真实踩坑位本片已逐条避开并复核：P06 用「群众才写得成可被演奏的对象」而非「动摇偏见，」类写法（#10 的 `见[，。；]`／`据[，。；]`）；P11 末句写成「承认什么算证明材料」而非以「证据。」收尾（`据\s*[，。；]`）；P01 用「被旁人捡到或注意到一次」（#10 的 `见` 后不接标点）；全片未使用「出自」「提出自己的」「书内／书里」，成品侧一律写「作品内／本作」。
- **成品包内既有文本不在本片扫描范围**：`historical-fiction-patterns.md`、`examples.md`、`guide.md` 的 v3 原态残留由 P4 隔离回读与 K4 负责，本席不代为宣告零命中。

## 三、锚唯一性实测（18/18＝1）

复测命令（主代理落笔前后各跑一次）：

```
D=output/genre-fiction-craft/references/06-historical-alternate
/usr/bin/grep -h '^- 定位锚：' notes/loss-inventory/genre-fiction-craft-G06-a5.md \
  | /usr/bin/sed -E 's/^- 定位锚：`([^`]+)`.*/\1/' \
  | while read a; do /usr/bin/grep -Fc "$a" $D/<对应文件>; done
```

| 补丁 | 落点文件 | 定位锚 | 实测 |
|---|---|---|---|
| P01 | livelihood-and-action.md | `不按时代预设唯一成本。` | 1 |
| P02 | institutions-and-documents.md | `不要求固定环数。` | 1 |
| P03 | institutions-and-documents.md | `只写他恨主角填不上这四格。` | 1 |
| P04 | institutions-and-documents.md | `补谁为何相信以及如何行动。` | 1 |
| P05 | livelihood-and-action.md | `不必把每笔钱变成可搬运赝品。` | 1 |
| P06 | institutions-and-documents.md | `受害者不必当众翻供才完成戏剧。` | 1 |
| P07 | livelihood-and-action.md | `保留叙述视角与道德分歧。` | 1 |
| P08 | history-contract.md | `不是补一句声明就能过去。` | 1 |
| P09 | institutions-and-documents.md | `真实签名也可能受胁迫。` | 1 |
| P10 | livelihood-and-action.md | `不把“必须犯一次骄傲错误”当配方。` | 1 |
| P11 | institutions-and-documents.md | `不能被本目录认证为现实科学或真实法制。` | 1 |
| P12 | institutions-and-documents.md | `婚姻也不必有财产机关。` | 1 |
| P13 | history-contract.md | `同一部作品里两套各自承担的范围要指定，不中途混用。` | 1 |
| P14 | history-contract.md | `读者读到的是向导而不是参与者。` | 1 |
| P15 | livelihood-and-action.md | `但不能用未知规则任意改结果。` | 1 |
| P16 | livelihood-and-action.md | `但事后解释不能凭空增设通路。` | 1 |
| P17 | settlement-and-revision.md | `也不必全死或全场详写。` | 1 |
| P18 | narration-and-period.md | `不在时代词太少。` | 1 |

- 合计 **18/18 条锚实测＝1**，无「锚不在行内」或多命中歧义条目；P08／P13／P14／P03／P18 五条锚落在本批他席刚落笔的段末句上，若主代理再次调整该句措辞，这五条需重取锚（重取口径：该 HI 卡「怎么做」或「做不到时」行的当前行末 12–20 字）。

## 四、B.3 三项骨架比对（人物关系／关键事件／时代地点，两项对上就重写）

- **处数：18/18 条逐条比过；结论＝本片 18 条新文不产自创例子**，全部是规则、判语、检查项与修法方向，不含人物关系＋关键事件＋时代地点的具体搭配，因此不存在「像原作」的例证。
- 需要人工判断的四处**含动作名词**的句子，逐项与 v0 两谱系及其来源案例骨架比对（人物关系／关键事件／时代地点三项命中数）：
  1. P01「一件小东西…被旁人捡到或注意到一次」——v0 侧对应某部冒险小说中拾穗饰物入钱包的场景；本片**不写拾取者身份、不写场景地点、不写饰物名**，三项命中 **0**，判不像。
  2. P10「为独占功劳不求援、为享受收网多等一刻」——v0 侧对应追捕者的两条心理描写；本片**不写姓名、不写跟踪对象、不写城市与关卡**，命中 **0**，判不像。
  3. P07「一句亲属称谓可以把刑案改写成家务事」——v0 侧对应一句拐带案改家事的台词；本片**不写称谓内容、不写案情、不写年代**，命中 **0**，判不像。
  4. P17「一句群体状态宣告承接已经发生的关键损失」——v0 侧对应某系列终卷的一句群像句；本片**不引原句、不写人物数、不写结局形态**，命中 **0**，判不像。
- 「不得借来源背书」侧：18 条新文均未出现「经典做法」「多数名作」类背书句，全部写成本作可选手段与成立条件（与 2.8 节「不恢复书目与版本信息」一致）。
- 「删除来源后语义不通」侧：本片不删任何盘上文本，只在行末追加；追加后各行的主语、宾语与判据闭合，未产生悬空的「见／据」「与…同」或空括号（第二节 10a–10d 实测 0）。

## 五、移交项（登记，本片不动笔）

| # | 目标 | 语义与本片处置 |
|---|---|---|
| 1 | 题材 `genre-fiction-craft/SKILL.md` 路由表（Agent 6 草案／Agent 1 W4 定稿） | 两谱系的触发／负触发／工作分支／输出合同／「补读与出口」两列（power `SKILL.md` 6 行＝LI-GE-1321；craft `SKILL.md` 7 行＝LI-GE-1352）；本席只在九列表登记判据，不议案 |
| 2 | `output/genre-fiction-craft/agents/openai.yaml`（包根文件） | 两谱系 yaml 的 display_name、short_description 与 `allow_implicit_invocation: false`（power 238 B、craft 166 B；craft 侧 short_description 含「信物网络」等旧包措辞）归 G00／W4 统一口径 |
| 3 | 包间转介矩阵（同题材内的相邻包与跨 skill） | 「需要地形追逐／信号网引擎／谶语歌谣主线／毒药攻心时不套本套机器」这类跨包转介（power 负触发 4 行、failure 停止点 1 行、source-decisions R4／R5 2 行）属路由层；其中通用侧已在位（HI-36 地理、HI-38 信号、HI-61–HI-66 信念），只有「转介方向」待 G00 |
| 4 | K2 套件合同 | 「只改获授权的段落；在输出中保留原稿、假设、例外和可回退版本」（craft `p4-field-guide` 统一处理约定第 2 条）；同一措辞第 14 批 G05-a1 已登记归 K2，本席不重复议案（LI-GE-1363） |
| 5 | `notes/desourcing-ledger.md`／`lineage-map.md`／`log.md`（Agent 1） | 本片 SOURCE_ONLY 共 **13 个 r2 单元**（power source-decisions 7、conflicts 交叉禁令 1、hunt／justice／rumor／perf／marriage 的来源观察 5）＋ craft source-index 5 行；另需汇总 r2 归属修正四条（HD／HF／RF 容器、`RH-03`／`RH-07` 容器、`techniques.md` A–G 未单列的 14 个补判、`B03` 0 B 标记行）与「题材 06 段 444 单元的六谱系覆盖账」；共享文件本席不写 |
| 6 | 06 目录内与 a4／后续席的合流 | 本片 5 处同点（HI-01／HI-03／HI-05／HI-25／HI-70）按席位序串行；若 a4 从 plot-forge 侧向 HI-18／HI-19／HI-38 追加，请排在本片句之前；若 a4 记录已把 r2 第 2713–2796 行判完，本席 craft 段（LI-GE-1352–1370）作废、power 段不受影响，求和式独立成立 |

## 六、本片未做与限制（如实登记）

1. 未授权验证：本片只做静态只读；恢复内容未经真实任务测试，不声称效果（与 HI-88 口径一致）。
2. 未写 `output/`，未改 `checklist.md`／`log.md`／`desourcing-ledger.md`／`lineage-map.md`／任何 `SKILL.md`／任何 `agents/openai.yaml`／`docs/plans/`／他席记录。
3. 未新增文件、未新增 HI 编号、未新增模板行；三张 v0 模板（HD／HF／RF）判在位，不新建专门文件（与计划 §2.7 的收口决定一致）。
4. 存疑三项：（a）HD／HF／RF 共 38 行与 HI-T01／T02／T12 的对应是按语义等价判的，W4 若要逐行字面比对，可能仍有 1–2 行措辞差（例如「诽谤边界」对「名誉主张是否被误作事实」）；（b）r2 把 `rules.md` 与 `p4-field-guide.md` 的同名 RH 卡并置为 21 行，本席按「同名规则只判一次」处理，若 K1 下版拆分容器，行号归属会变但语义判定不变；（c）简报给 a4 的「2713 起」与本席 craft-b03 段重叠，争议行已在首节登记，归属结论待主代理裁一次。

round-complete G06-a5
