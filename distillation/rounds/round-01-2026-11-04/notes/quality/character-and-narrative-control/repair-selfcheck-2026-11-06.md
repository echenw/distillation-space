# 修复批附录 B 自检 · character-and-narrative-control（R1 席，2026-11-06）

- 范围：`output/character-and-narrative-control/` 全 17 件（另对 `notes/delivery-preflight-spec/character-and-narrative-control.md` 跑禁词专项）。
- 工具：`/usr/bin/grep -rnE`（本机 grep 为 ugrep，中文长模式会报复杂度限制，一律改用 BSD grep）；`LC_ALL=en_US.UTF-8`（suite-contract §4.2bis 要求逐类计数声明 locale，未设时中文括号类按字节解释会误报）。
- 口径：附录 B 全 11 类正则（`notes/suite-contract.md` §4.2）改前、改后各跑一遍，比对命中集合；命中逐条判断，不把命中直接判违规。B.3 逐处回读人工判断。
- 门槛：零新增违规（总账 §三第 2 项）。

## 一、11 类正则改前／改后对比

| 类 | 目标 | 改前 | 改后 | 结论 |
|---|---|---|---|---|
| B.1 | 书名号作品名 | 0 | 0 | 无变化 |
| B.2 | 来源编号／残片 | 0 | 0 | 无变化 |
| B.3 | 数量／年代 | 0 | 0 | 无变化 |
| B.4 | 指向学习材料的说法 | 6 行 | 6 行 | 同址，均为既有合法命中 |
| B.5 | 作者、作家、名人／英文人名 | 0 | 0 | 无变化 |
| B.6 | 英文原句 | 0 | 0 | 无变化 |
| B.7 | 包外路径 | 0 | 0 | 无变化 |
| B.8 | 改动痕迹 | 0 | 0 | 无变化 |
| B.9 | 审计词 | 0 | 0 | 无变化 |
| B.10 | 删除后的残迹 | 23 行 | 23 行 | 同址，均为既有合法命中 |
| B.11 | 分档词／禁用说法 | 0 | 0 | 无变化 |

B.4 六行（改前＝改后）：`examples/pov-cases.md:13`、`references/information-control.md:21`、`references/narrator-and-viewpoint.md:79`、`references/testimony-and-self-justification.md:46`、`references/zh-and-serial.md:37`、`SKILL.md:145`。逐条为「出自／引自／该书」类领域语义或登记行，属 B.2 允许保留情形；#9 要求不删，本席未动。

B.10 二十三行（改前＝改后）：`examples/pov-cases.md:116/130/132`、`examples/psychology-cases.md:29/51/65`、`references/boundaries-and-ethics.md:14`、`references/diagnosis.md:182/214`、`references/information-control.md:64`、`references/objects-loss-and-change.md:56`、`references/psychology-in-action.md:81`、`references/social-pressure-and-silence.md:67/77`、`references/testimony-and-self-justification.md:74/76/86`、`references/time-mechanisms.md:71/133`、`SKILL.md:256/264`、`templates/narrative-workbook.md:113/128`。逐条判为领域语义或守卫句（与 suite-contract §4.2bis 所记「A∧B 后 23 行」一致）；本席新增内容未落入这些行。

⇒ 11 类命中集合改前＝改后，**零新增违规**。

## 二、B.3 人工判断（逐处回读新增内容）

| 新增处 | 判断 |
|---|---|
| `boundaries-and-ethics.md` §6 | 通用条文，措辞自创；无真实机构名、无作品情境、无人物关系／关键事件／时代地点骨架；无「经典做法是…」类背书；段落完整、主语不悬空 |
| `SKILL.md` §9.1 映射行（:275） | 状态词与判断档位的分层说明，非例子；完整句，无作品元素、无背书、无空列 |
| `SKILL.md:153` 归属括注 | 完整括号内说明，指定契约登记的唯一归口；未新增规则、未引入作品信息 |
| `narrative-workbook.md:142` | 引用 §9.1 的消歧句；完整句，未新增第二份定义表 |
| `pov-cases.md:110/:111/:136` | 仅状态列改标；表格四列齐全、无删除后空列或半句 |
| `delivery-preflight-spec/...md:27` | notes 层完整 bullet，无作品元素 |

⇒ B.3 四项（骨架相近／标志性情节元素／借来源背书／删除后语义不通）均不成立，通过。

## 三、禁词专项

模式：`NOT_PROVEN|VERIFIED|NOT_RUN|STATIC_CHECKED|DESIGN_EXAMPLE|OBSERVED|GQ[1-5]|R1[78]|F/H/P|PASS|FAIL|BLOCKED|NOT_APPLICABLE|夯|拉完了|硬规则|用户明确要求|融合版|旧版|本版|更正|上一版|补回|续排|《[^》]+》|PG[ -]?[0-9]+`。

- `output/character-and-narrative-control/`：0 命中。
- `notes/delivery-preflight-spec/character-and-narrative-control.md`：3 行命中，均为既有行 :3／:20／:25（含 `R18`／`NOT_PROVEN`，notes 层允许）；本席新增的 :27 未命中。
- 来源信息（书名／作者姓名／作品人物情节／原句／来源编号／年代／篇数）：11 类 B.1–B.4 已覆盖，新增内容 0 命中。

⇒ 新增内容不出现审计词、分档词、「硬规则」「用户明确要求」「融合版」、改动痕迹（补回／续排／本版／旧版）、来源信息。

## 四、体量

改前 17 件／193531 字节（`review.json` binding）→ 改后 **17 件／194854 字节**（净增 1323 字节）。`SKILL.md` §9.1 新增映射行及其后空行使 :277 起原行号 +2；其余既有行号不动。

## 五、结论

附录 B 全 11 类零新增违规，B.3 通过，禁词专项通过。本包改动仅涉及 4 个成品文件与 1 个 spec 文件，均在写入范围内；本包 review.json 的树 SHA／锚绑定随改动失效，重绑复测归主代理。
