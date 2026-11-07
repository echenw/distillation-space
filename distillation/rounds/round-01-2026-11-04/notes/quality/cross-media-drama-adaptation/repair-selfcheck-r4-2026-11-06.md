# 附录 B 自检回执（R4 · cross-media-drama-adaptation · 修复批 2026-11-06）

- 范围：`output/cross-media-drama-adaptation/` 全 13 文件；改前／改后同脚本对比。
- 工具：`/usr/bin/grep -rnE`（本机 grep 为 ugrep，中文长模式会报 exceeds complexity limits，按 `suite-contract §4.2` 统一用 BSD grep）。
- locale：**声明判读档 `LC_ALL=en_US.UTF-8`**，并按 `§4.2bis` 作 `LC_ALL=C` 两档回显；逐类计数未经 `sort|uniq` 并组，直接 `grep -rnE | wc -l`。
- 覆盖：B.1 全 11 类正则、§4.2bis 补档 6 条、B.3 四项人工判断；新增内容禁词专项。命中逐条人工判断，不把命中直接判违规。
- 本席写入范围：本自检文件 + `notes/repair-ledger-cross-media-drama-adaptation.md` + 本包 output 内 4 文件；未写 brief.json／review.json／k5-bindings／checklist／log／desourcing-ledger／总账／其它包／skills／计划文档；未做 git 写操作；未跑测试／构建／真实任务。

## 一、B.1 全 11 类 + §4.2bis 补档：改前／改后逐类计数对比

| 类 | 模式（摘要） | 改前命中 | 改后命中 | 对比 |
|---|---|---|---|---|
| #1 | `《[^》]+》` | 0 | 0 | 无变化 |
| #2a | `PG[ -]?[0-9]+` | 0 | 0 | 无变化 |
| #2b | `(^\|[^A-Za-z0-9])-[0-9]{3,5}([^0-9]\|$)` | 0 | 0 | 无变化 |
| #2 补 | `GB/?T? ?[0-9]{4,6} ?- ?[0-9]{4}` | 0 | 0 | 无变化 |
| #3a | `[0-9]+ ?本(材料\|书\|手册)` | 0 | 0 | 无变化 |
| #3b | `材料标称` | 0 | 0 | 无变化 |
| #3c | `(1[5-9]\|20)[0-9]{2} ?年(代)?.{0,8}(市场\|手册\|杂志\|出版\|建议)` | 0 | 0 | 无变化 |
| #3 补 CN1 | `一[本部册两三四五] ?(材料\|书\|手册)` | 0 | 0 | 无变化 |
| #4 | `书内\|书里\|同书\|该书\|此书\|原书\|来源是\|出自\|引自\|据称\|这批材料\|学习材料\|原文库\|批次` | 0 | 0 | 无变化 |
| #5a | `作家\|小说家\|评论家\|大师\|名著\|经典作品` | 0 | 0 | 无变化 |
| #5b | `[A-Z][a-z]+ [A-Z][a-z]+` | 0 | 0 | 无变化 |
| #5b 补 | 排除表 `Skill Owner\|Plot Canvas\|Diagnosis Report\|Scene Table` | 0 | 0 | 无变化 |
| #6 | `["“][A-Z][a-z]+( [a-z]+){4,}`（弯引号起点，§4.2bis） | 0 | 0 | 无变化 |
| #7 | `notes/\|results/\|/home/\|materials/\|rounds/` | 0 | 0 | 无变化 |
| #8 | `旧版\|本版\|更正\|早先的版本\|融合版\|上一版` + 补 `旧例\|原例` | 0 | 0 | 无变化 |
| #9 | `NOT_PROVEN\|VERIFIED\|NOT_RUN\|STATIC_CHECKED\|DESIGN_EXAMPLE\|OBSERVED\|F/H/P\|GQ[1-5]\|R1[78]` | 0 | 0 | 无变化 |
| #10 | `（[[:space:]]*）\|\([[:space:]]*\)\|见[[:space:]]*[，。；]\|据[[:space:]]*[，。；]\|与[[:space:]]*同` | 15 | 15 | 同址，见下 |
| #11 | `夯\|拉完了\|硬规则\|用户明确要求` | 0 | 0 | 无变化 |

### #10 改前 15 行 → 改后 15 行逐条回显与判断

改前命中（`LC_ALL=en_US.UTF-8`）：`references/interactive-adaptation.md:74`、`references/conflicts.md:12/21/29`、`references/plot-and-ending.md:1/24/38/41`、`references/stage-realization.md:45`、`references/transferability.md:59`、`examples/adaptation-cases.md:13`、`SKILL.md:106/128/134/144`。

改后逐条同址：**仅 `references/interactive-adaptation.md` 因 §4 删去第二份四词定义表（−5 行）由 `:74` 变为 `:69`**，其余 14 行行号与文本逐字不变。

逐条人工判断（15/15）：全部为「可见／看得见／同情／与…同／同书式领域词」的词尾子串假阳性——例如 `conflicts.md:12`「向观众可见」、`plot-and-ending.md:38`「兴趣中心与同情」、`transferability.md:59`「回到当前作品的目标、条件和证据」、`SKILL.md:144`「权利与许可」——均非「删除来源后留下的空括号／悬空的见、据」。按 `§4.2bis`「#10 三档字面改标点后悬空＋同行共现语义判据」，真残迹 **0**；改前改后同为 0。

### locale 两档回显（§4.2bis locale 必写）

| locale | #10 计数 | #4 计数 |
|---|---|---|
| `LC_ALL=en_US.UTF-8`（判读档） | 15 | 0 |
| `LC_ALL=C`（字节解释档） | 26 | 0 |

`C` 档把中文括号按字节解释，计数虚高（与 §4.2bis 实测一致）；判读以 `en_US.UTF-8` 档为准，两档均已回显，未走 `sort|uniq` 并组。

## 二、新增内容禁词专项（改后）

禁词模式（合并派单列举项）：`NOT_PROVEN|VERIFIED|NOT_RUN|STATIC_CHECKED|DESIGN_EXAMPLE|OBSERVED|PASS|FAIL|BLOCKED|NOT_APPLICABLE|F/H/P|GQ[1-5]|R1[78]|夯|拉完了|硬规则|用户明确要求|融合版|旧版|本版|更正|上一版|旧例|原例|早先的版本|《[^》]+》|[0-9]+ ?本(材料|书|手册)|(1[5-9]|20)[0-9]{2} ?年|作家|小说家|评论家|大师|名著|经典作品`。

- 全包（13 文件）：**0 命中**。
- 新增／改写 5 行逐行扫描（把该行文本再送同一模式）：**5/5 均「无」**——
  - `SKILL.md:168`「状态词定义见 SKILL.md §10」
  - `SKILL.md:204`「§10 是包内交付状态词的唯一定义处……本轮未执行的检查归「未能核实」……」
  - `references/interactive-adaptation.md:52`「检查结果的状态词定义见 SKILL.md §10。」
  - `templates/interactive-branch-sheet.md:39`「状态词定义见 SKILL.md §10；该列可填「未知」作占位……」
  - `templates/adaptation-workbook.md:60`「状态词定义见 SKILL.md §10；「未知」是这一列的合法占位值……」
- 来源信息（书名号／作者／作品人物情节／原句／来源编号／年代／篇数）：由 #1／#2／#3／#4／#5／#6 逐类覆盖，改后均 0；新增 5 行无书名、无作者、无作品人物情节、无原句、无来源编号、无年代、无篇数。
- 「改动痕迹」：新增文案未写「旧版／本版／更正／融合版／上一版／旧例／原例」等，改的是条文本身而非记录改动过程。

## 三、B.3 人工判断（13/13 全文逐文件回读，改前／改后）

| 项 | 结论 |
|---|---|
| 例子与 v0 来源案例情节骨架相近（人物关系／关键事件／时代地点 ≥2 项对上） | 0 处。Case A–E 均为自建示例（车票／钥匙／信、办公室文件、雨夜车站→海边、照抄边界、内心独白冲突），无具体作品骨架 |
| 具体作品标志性情节元素（无书名也算） | 0 处 |
| 借来源背书（「经典做法是…」「很多名作都…」） | 0 处 |
| 删除来源后语义不通（主语悬空／只剩半句／表格空列） | 0 处 |

改后专项复核：
- `references/interactive-adaptation.md §4`：删去第二份四词定义表后，:52 指针句 →空行→「没有执行与被输入挡住是两种不同情形……凡不是已完成的项，在分支表「证据或限制」列写明原因和影响」→「路线图用于表达叙事因果……」，上下文连贯，「前者／后者」句内自足，未产生悬空主语、半句或空列。
- `templates/interactive-branch-sheet.md`「路线验证」表：表头行 + GFM 分隔行 + 6 数据行在位，未因改 :39 破坏表格。
- `templates/adaptation-workbook.md §7`：表头行 + 分隔行 + 占位数据行 + 5 条说明在位，:57 五值占位未动。
- `SKILL.md §10`：四词定义表（表头／分隔／四行）逐字未动，新增说明句为独立段落、非表格内。

## 四、结论（§4.2bis 诚实线）

- 改前／改后对比：**#1–#9、#11、补档 6 条同为 0 命中；#10 同为 15 行且逐条同址（仅 1 行因删表 −5 行位移），真残迹同为 0；禁词专项 0 命中；B.3 四项 0 处 ⇒ 零新增违规。**
- 按 `suite-contract §4.2bis`：19 条子模式中 13 条（1a、2b、3a、4a、5a、5b、6a、8a、10a–10e）本轮仍属检测有效性未证；本回执只报「同脚本、同址、零新增」，**不写「全类零违规」一类超出检测能力的断言**，也不把「能构造正控制」写成「目标类已被真实覆盖」。
- GQ5 维持 NOT_PROVEN：未跑测试／构建／真实任务（未授权）；本批只做静态文本落笔，不证明宿主加载或效果。

## 五、改动后文件数与字节（留痕）

- 改前 13 件 / 76222 B（`notes/k5-bindings-2026-11-05.tsv` 第 3 行 tree_sha `77269b54…`）。
- 改后 13 件 / 75549 B（净 −673 B）：`SKILL.md:168` −38、`:204` +155、`interactive-adaptation.md:52-57` −818、`interactive-branch-sheet.md:39` −19、`adaptation-workbook.md:60` +47。反算 75549−(−673)＝76222，与 tsv 基线逐字节相符。
- 行数（wc -l）：`SKILL.md` 241→241、`interactive-adaptation.md` 91→86（−5）、`interactive-branch-sheet.md` 56→56、`adaptation-workbook.md` 63→63；全包 902→897。其余 9 文件未动。
