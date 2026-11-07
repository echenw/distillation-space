# 修复批分片 ledger（R2 · scene-conflict-and-rhythm · 2026-11-06）

- 席次／Owner：R2，唯一 `output/scene-conflict-and-rhythm/`
- 触发：作者答复「全部按推荐」（`notes/user-decisions-2026-11-05.md` 13 条决定件），修复批发车
- 依据：`notes/repair-ledger-2026-11-06.md`（总账与裁决表，本席只读）、`notes/repair-workplan-2026-11-06.md` 第二／三节、`notes/user-decisions-2026-11-05.md` #2 原文、`notes/suite-contract.md` §2.1／§4.2、`notes/w4-closure-2026-11-05.md`、`notes/p4-closure-2026-11-05.md`、`notes/quality/scene-conflict-and-rhythm/review.json` 与 `brief.json`，以及本包 output 17 文件全文
- 写入范围：本包 output 内 4 个文件、本分片 ledger、`notes/quality/scene-conflict-and-rhythm/r2-appendixB-selfcheck-2026-11-06.md`；禁写面（brief.json／review.json／k5-bindings-*.tsv／checklist.md／log.md／desourcing-ledger.md／总账／其它 7 包／skills／计划文档）未碰，未做 git 写操作，未跑测试／构建／真实任务
- 编号约定：#2A＝作者裁决第 2 条 A 分支；GQ2-①～④＝工作单第三节「scene GQ2」四项的序号，非新编裁决号

## 一、逐处改动（位置／改前／改后／依据／裁决编号）

| # | 位置 | 改前 | 改后 | 依据 | 裁决编号 |
|---|---|---|---|---|---|
| 1 | `references/rhythm-diagnosis.md:70-81`（§6「状态词」小节） | `### 状态词`＋「对作者交付只用四个词，逐项给依据：」＋四行表（`\| 状态词 \| 什么时候用 \|` 表头、分隔行、已完成／依据／未能核实／待作者决定 四行）＋禁令句；与 `SKILL.md:253-258` 逐字重复的完整第二份表 | 删去重复的引导句与四行表体，改为一行指针「状态词定义见 SKILL.md §9。」；原禁令句「不把「未能核实」「待作者决定」写成「已完成」；不把未验证的效果判断写成通过。」原样保留 | `review.json` S-01／GQ2 ①／rv_recheck、`brief.json` SC-G01、`w4-closure` W4-44；`SKILL.md §9` 保留唯一权威表（四词核对为「已完成／依据／未能核实／待作者决定」，符合，未改） | #2A |
| 2 | `references/intensity-and-rhythm.md:11` | 「单峰的设计里，高潮是**全篇**强度的标尺。」 | 「单峰的设计里，高潮是**本单元**强度的标尺。」 | 工作单第三节 scene GQ2 第 1 项；「本单元」取自同句前半「先决定本单元最高强度」的既有表述，不新造；与归一后的「单元」定义一致 | GQ2-① |
| 3 | `references/intensity-and-rhythm.md:28` | 「- **规则**：先确定读者当前阅读的单位（场、章、**卷**或整篇），再决定强度分布；不同单位不必重复同一结构。」 | 「- **规则**：**短篇的单元是全篇，长篇是章或场景**；先确定读者当前阅读的单位，再决定强度分布；不同单位不必重复同一结构。」 | ① 单元定义归一：定义句逐字取 `SKILL.md:177` 现有表述（不新造）；② 同文件 :3「卷级安排见 story-architecture-and-longform-planning」／:36「连载钩子和卷级悬念转交长篇规划 Skill」与 :28 把「卷」列为阅读单位的自相矛盾，删「卷」值域后消解；`review.json` S-02／F-10、`brief.json` SC-G03 | GQ2-①＋② |
| 4 | `references/setup-and-payoff.md:47-60`（SU-07 卡体） | 仅 3 行粗体字段（`**规则**`／`**怎么做**` 4 步／`**边界**`），六字段「用于／不用／反例／检查／自拟例／出口」全缺，且与同文件 SU-01／SU-06／SU-08 的八字段列表式卡体不同构 | 按该包既有卡体字段格式补齐为 8 字段：`- **规则／用于／怎么做／不用／反例（自创）／检查／自拟例（自创）／出口**`；「不用」内容逐字取自原「边界」行；新增 5 字段文案取包内既有表述（SKILL.md §4 症状行、SU-07 规则、SU-12／SU-06／SU-01 出口句式），例子标注（自创）；字段名沿用既有八字段名，不新造 | `review.json` F-01／GQ2 ④、`brief.json` SC-G06、`SKILL.md:224` 入口层字段承诺 | GQ2-③ |
| 5 | `SKILL.md:275`（§10 失败出口表，表末新增一行） | 表末无「无授权」行；`SKILL.md` 全文「授权」二字 0 命中 | `\| 没有修改文件的授权 \| 只给文本，不写文件 \|`（措辞逐字取自 `references/scene-and-action-diagnosis.md:147` 既有原句） | `brief.json` SQ-R39／SC-G11、`review.json` SQ-R39／rv_recheck；与计划第 8 节「未经授权，不运行…」静态权限（D3-A 只做静态检查）一致 | GQ2-④ |

## 二、无动作项（记「无动作」，未改任何文件）

| 裁决号 | 结论 | 说明 |
|---|---|---|
| #3A | 无动作 | 占位行即合法可填面，spec 已预写；本包 `templates/` 占位行不动 |
| #5A | 无动作 | 两列只需 §6 参考文件表；属 genre §4 十四题材表，非本包范围 |
| #9 | 无动作 | 登记类保留：该书／某书 8 行保留、RO-K117–119 不补回、导演 vs 作者不改；工作单无 #9 落地项 |
| #12 | 无动作 | 保留原句（CY-07 防口已覆盖） |
| #13 | 无动作 | 豁免并按 W4-123 先例登记 |
| #2A（四词字面） | 无动作 | `SKILL.md §9` 四行状态词已是「已完成／依据／未能核实／待作者决定」，符合固定口径，未改 |

## 三、附录 B 自检结论（详见 `r2-appendixB-selfcheck-2026-11-06.md`）

- `LC_ALL=en_US.UTF-8 /usr/bin/grep -rnE` 跑 B.1 全 11 类：#1–#9、#11 零命中；#10 命中 21 行，逐条读毕全为「依据／证据／数据／收据／可见／不见」词尾子串假阳性，真命中 0。
- §4.2bis 补档 6 条：`旧例｜原例`／标准号／弯引号／5b 排除表均 0；CN1／CN2 命中同一行 `SKILL.md:289`「帮我规划一本书」，属 B.2 用户作品语义，真命中 0。
- 新增内容禁词专项（4 个改动文件的改写行）：审计词、分档词、「硬规则」、「用户明确要求」、「融合版」、改动痕迹、来源信息（书名／作者／作品人物情节／原句／来源编号／年代／篇数）**0 命中**。
- B.3 四项逐文件人工回读（17/17 全文）：无情节骨架相近、无标志性情节元素、无借来源背书、无删除来源后语义不通；两处表格分隔行在位。
- 诚实线：按 `suite-contract §4.2bis`／`p4-closure §七`，13 条子模式检测有效性未证，本结论不写成「全类零违规」。GQ5 维持 NOT_PROVEN（未跑测试／构建／真实任务，未授权）。

## 四、改动后文件数与字节

| | 文件数 | 字节 |
|---|---|---|
| 改前 | 17 | 168166（与 review.json tree_inventory 一致） |
| 改后 | 17 | 169017（+851） |

行数：`SKILL.md` 298→299（+1）、`references/rhythm-diagnosis.md` 100→93（−7）、`references/intensity-and-rhythm.md` 103→103（0）、`references/setup-and-payoff.md` 76→79（+3）；其余 13 文件未动。

## 五、断点与未闭合项（交主代理）

1. **brief 层 F-05 `scene:289` 裸对端行号 +1**：本席在 `SKILL.md §10`（:275）增 1 行，使 :289 起整体 +1；按派单属 brief 层，主代理下一批统一处理，本席未碰 `brief.json`。相应 `review.json`、`k5-bindings-*.tsv`、整树 SHA、spec/INDEX/JSON 重算与 8 包附录 B 重扫同批。
2. `references/chapter-ends-and-endings.md:9` 仍写「场景或章节单元（场、章、幕）」，是 `review.json` S-02 提到的第三处值域；工作单第三节只点名 `SKILL:177` 与 `intensity :11/:28`，本席不扩范围、未动，如需三处全归一请主代理另裁。
3. `review.json` GQ2 另列 ③ SC-07 长谈三问缺「题材／信息交代」一支、⑤「已发表／已锁定」事实核对前置，以及 GQ3 七接口、S-03／S-04／S-05、`brief.json` SC-G02（§7 与 §10 行数不等）、F-01 提到的 `SKILL.md:224` 字段承诺措辞——均不在本批「GQ2 四项」授权内，未动，不替作者裁新口径。
4. GQ5 维持 NOT_PROVEN；本批只做静态文本落笔，不证明宿主加载或效果。
