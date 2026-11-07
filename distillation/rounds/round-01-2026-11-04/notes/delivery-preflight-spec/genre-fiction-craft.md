# delivery-preflight-spec · genre-fiction-craft

承载位置：本文件是本轮 22.4 第 4 项的逐 skill spec 条目（R18 §6 的可选只读结构预检在本轮**不执行脚本**，static 权限，见 `checklist.md` §二十六 与本文末）。成品包＝`output/genre-fiction-craft/`。

## 一、枚举模板与编号全集（机械实测，双档回显）

| 模板件 | ID 独占表行数 | 宽式唯一 ID（全文） | 其中标题级 ID |
|---|---|---|---|
| output/genre-fiction-craft/references/01-mystery/worksheets-and-cases.md | 0 | 12 | 6 |
| output/genre-fiction-craft/references/02-romance/templates.md | 60 | 98 | 0 |
| output/genre-fiction-craft/references/03-horror/templates-and-cases.md | 0 | 26 | 26 |
| output/genre-fiction-craft/references/04-wuxia-xianxia-fantasy/templates-and-cases.md | 0 | 108 | 33 |
| output/genre-fiction-craft/references/05-science-fiction/templates.md | 0 | 30 | 0 |
| output/genre-fiction-craft/references/06-historical-alternate/templates.md | 0 | 53 | 12 |
| output/genre-fiction-craft/references/07-survival-disaster/templates.md | 32 | 32 | 0 |
| output/genre-fiction-craft/references/08-adventure-treasure/templates.md | 37 | 55 | 0 |
| output/genre-fiction-craft/references/09-comedy/templates-and-examples.md | 0 | 1 | 1 |
| output/genre-fiction-craft/references/10-profession-competition/worksheets-and-cases.md | 0 | 14 | 4 |
| output/genre-fiction-craft/references/11-identity-revenge-intrigue/templates-and-examples.md | 0 | 5 | 5 |
| output/genre-fiction-craft/references/12-children-youth/templates.md | 26 | 26 | 0 |
| output/genre-fiction-craft/references/13-isekai-time-travel/templates-and-cases.md | 15 | 15 | 1 |
| output/genre-fiction-craft/references/14-period-realism/templates-and-examples.md | 19 | 19 | 0 |

求和：模板件 **14** 件｜ID 独占表行 **189** 行（分布在 6 件）｜宽式唯一 ID **494**｜标题级 ID **88**。

与 `delivery-preflight-spec.json`（§6 的 JSON 载体）的一致性：JSON 内本 skill 条目 **0** 件、field_ids 合计 **0** 个；实测宽式全集 **494** 个 ⇒ **差额 494**。

## 二、§2a 可填性判定

- 判定：有 189 条 ID 独占表行（6 件），列名与 §2a 三列形的对照见下
- 逐行三列要求（值／状态／稿件证据位置）：逐件表头实测见 `field-id-matrix.md` 的 genre 复测节与本文件第一节；**存在 ID 独占行，但表头列名不统一**（六件里 07／12／13 已含「已知事实/位置/版本」「回看/未知」「正文位置与版本」等等价列，02／08／14 用「填写内容／何时使用／规则／例子」「对象／条件与动作提示」「需要的具体输入」等异名）。
- 空值处置：按各 skill 模板自带声明——不知道的格子写「未知」，不为填满而编；「未知」不得写成「已完成」（character `narrative-workbook.md:3`、`SKILL.md:266-273`；scene `templates/scene-workbook.md` §7 同口径）。
- 取词口径：ID 独占表行判据＝表格首列**整格等于**一个 ID（宽式 `[A-Z]{1,4}-[A-Z]{0,2}\d{1,3}[A-Z]?`）；正文级与标题级 ID 单列回显，不混入可填行计数。窄式 `[A-Z]{2}-\d\d` 对 `HO-T##`／`IS-X##`／`RO-T##` 一类带字母中缀的编号恒零命中，故本文件一律用宽式（见 `field-id-matrix.md` 更正注）。

## 三、待裁与不执行声明

- 本文件**不修正品**，只登记列形与全集差额；是否统一列名属交付格式裁决，见 `notes/w4-review-queue.md` 的 W4-45／W4-47／W4-52 与本 skill 相关行。
- `kd_delivery_preflight.py` 未运行（static 权限；SKILL.md §R09 收口条文明确「不另设机器门禁」，执行需另行授权）。因此本 skill 的 §6 预检状态＝**NOT_PROVEN（未执行）**，不等于通过。
- 状态词：全集与行数为**已完成**（有实测回显）；§2a 是否满足为**依据**上文两表；脚本预检为**未能核实**；列形取舍为**待作者决定**。
