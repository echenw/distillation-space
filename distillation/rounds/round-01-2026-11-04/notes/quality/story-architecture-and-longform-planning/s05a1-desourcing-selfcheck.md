# S05a1 去来源自检记录（附录 B 全 11 类 + B.3 人工判断）

- 片名：S05a1（story：v0 `plot-architecture` a1 段）｜代理：Agent 3｜轮次：W3 主体轮第 7 批｜日期：2026-11-05
- 范围：`output/story-architecture-and-longform-planning/` 全部 21 个文件（SKILL.md、agents/openai.yaml、references 13 份、examples 2 份、templates 4 份）。本片改写其中 **4 个**：`SKILL.md`（合同类）、`references/plot-rules.md`、`references/plot-planning.md`、`references/plot-revision.md`；`agents/openai.yaml` 核对后原样保留。其余 16 个为基线文件，其中 `references/plot-diagnosis.md`、`examples/plot-examples.md`、`references/plot-scope-and-conflicts.md`、`templates/plot-*.md` 属并行片 **S05a2** 落点（本片未动；扫描时点该片已有在途改动），`references/serial-*.md`、`examples/serial-examples.md`、`templates/serial-tables.md` 属 **S05b1/b2** 落点（本片未动）。命中按归属登记。
- 命令：统一 `/usr/bin/grep -rnE '<模式>' <目录>`；本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`，故不用。
- 性质：Worker 自检，属 `notes/quality/`。**不是** D3-C 的独立隔离回读；后者按派发留 W4 由 Agent 1 另派只读子代理。本记录不写公共 `desourcing-ledger.md`。
- 扫描时点说明：本包由本片与 S05a2 同时建包（同一 v3 基线，双方文件不重叠）；扫描为建包后快照，a2 落点文件仍在该片中持续修改，其命中数以该分片自检为准，本记录的 a2/serial 命中登记供其参考。
- 结论：**11 类共 29 条命中；本片落点 4 文件命中 6 条全部判允许、零违规；a2/serial 落点命中全部登记为待对应分片处理**。逐类见下。

## 一、全 11 类复扫计数（快照）

| # | 目标 | 全包命中 | 本片 4 文件 | 基线/a2/serial 文件（待对应分片） |
|---|---|---|---|---|
| 1 | 书名号作品名 `《[^》]+》` | 0 | 0 | 0 |
| 2 | 来源编号与残片 `PG[ -]?[0-9]+`、`-[0-9]{3,5}` | 0 | 0 | 0 |
| 3 | 来源数量与年代 | 0 | 0 | 0 |
| 4 | 指向学习材料的说法 | **1** | 0 | 1（serial-zh-webnovel:9，S05b） |
| 5a | 作家/大师类词 | 0 | 0 | 0 |
| 5b | 拉丁字母人名 `[A-Z][a-z]+ [A-Z][a-z]+` | **8** | 1（SKILL ×1） | 7（plot-examples ×4、templates ×3，均 S05a2） |
| 6 | 英文原句（直引号 5 词以上） | 0 | 0 | 0 |
| 7 | 包外路径（notes/、results/、/home/、materials/、rounds/） | 0 | 0 | 0 |
| 8 | 改动痕迹（旧版/本版/更正/早先的版本/融合版/上一版） | 0 | 0 | 0 |
| 9 | 审计词（NOT_PROVEN/VERIFIED/NOT_RUN/STATIC_CHECKED/DESIGN_EXAMPLE/OBSERVED/F/H/P/GQ/R17/R18） | 0 | 0 | 0 |
| 10 | 删除后的残迹（空括号、悬空见/据、与同） | **20** | 5（SKILL ×2、plot-rules ×2、plot-revision ×1） | 15（plot-examples ×6、plot-scope ×3、plot-diagnosis ×2、serial-examples ×2、serial-production ×1、plot-diagnosis-report ×1） |
| 11 | 分档词和禁用说法（夯/拉完了/硬规则/用户明确要求） | 0 | 0 | 0 |

合计 29 条（1+8+20）。附加扫（#2 第二模式 `(^|[^A-Za-z0-9])-[0-9]{3,5}([^0-9]|$)`、PASS/FAIL/BLOCKED/NOT_APPLICABLE、`L[0-9]{3,5}` 行号型锚点）：全包零命中。本片改写前基线四文件的状态词形残留（「未证实」×3、「未验证」×2、「尚未验证/未验证」×4、「设计推断」×1、「未核」×4、`RC，即 PL 编号` 旧编号痕迹 ×1）已全部清除并经本复扫确认归零。

## 二、本片 4 文件命中逐条判断

### #5b（1 条）

| 位置 | 原句 | 判断 |
|---|---|---|
| `SKILL.md` §1「### 跨 Skill Owner」 | 「Skill Owner」两词命中连续首字母大写模式 | 允许。小节标题的英文短语（Skill＝技能、Owner＝责任方），非人名、非作品名、无来源指涉。正则目标（作者/名人指涉）未命中其实质。 |

### #10（5 条，`据[，。；]`/`见[，。；]` 误报）

| 位置 | 命中子串 | 所在词 |
|---|---|---|
| `SKILL.md` §3 诊断已有稿子 | 据， | 「文本位置作**证据，**先试着推翻它」 |
| `SKILL.md` §5 SV-04 卡 | 据。 | 「没有读者数**据。**」 |
| `references/plot-rules.md` PL-03 冲突状态 | 据。 | 「必须给出 A/B/C/D 与判**据。**」 |
| `references/plot-rules.md` PL-10 可信度 | 据， | 「没有读者留存数**据，**不作留存保证」 |
| `references/plot-revision.md` §5 | 据， | 「它是修订与回归的证**据，**不是第四个交付物」 |

全部是完整句、主语明确、语义通顺的正常词（证据/数据/判据），不是删除来源后悬空的「见／据」。允许。`（\s*）`、`\(\s*\)`、`与\s*同`、`见\s*[，。；]` 四个子模式在本片文件零命中。

## 三、B.2 允许情形（本片 4 文件层面）

- **本包内部编号**：PL-01–PL-16、SV-01–SV-16、PA/ST/DR 模板编号、SU-03/04/15/16（指向 `scene-conflict-and-rhythm` 的规则编号）、B1/B2/B3（PL-06 分支号）。符合 B.2 第 3 条。
- **用户稿件语境**：「没读到的部分标‘未读’」「不覆盖原稿」「用户稿件的语言峰值」「稿件证据位置只填用户当前稿件内的可核位置」——指用户正在写的稿子。符合 B.2 第 1 条。
- **历史参数的降级表述**：plot-planning §6「只有历史数字（7,500 词/32 页/3,000–6,000 词/10–20 章）→ 只放『历史参数』栏，不作当代规范」——数字本身在 v0 即被规则定义为「历史参数、禁止作当代规范」，保留是规则对象而非来源年代断言；与 PL-13 卡「不要把历史上的数字当规范」同口径。允许。
- **否定式规范说明**：「不编造平台标准」「不承诺追读、订阅、完读或销量」「不指向来源编号或包外路径」（a2 落点的模板句，此处仅 SKILL.md 引用其出口文字）——均为对成品的规范性禁令。允许。

## 四、B.3 人工判断（逐文件回读本片改写的 4 份文件）

1. **与 v0 来源案例的骨架比对**：本片没有新增自创例——所有改动是（a）并入 v0+v1 共有的规则条件（PL-01/02/04/05/08 的软化块，共 5 组），（b）合同类表格（负触发、输入权限、失败出口、路由出口列，内容为边界与出口描述，无情节），（c）措辞合规替换（状态词形、旧编号痕迹）。无新人物、新地点、新事件、新年代进入成品；逐句核对无与 v0 来源案例（真实作品情节）两项以上骨架对应的新情境。v0 P4 直接执行示例的两个微例未搬入成品（移交 S05a2，见 loss-inventory LI-ST-004）。
2. **具体作品的标志性情节元素**：本片改写未引入任何作品名、人名、地标、机构名；恢复句均用「作品契约要求…时」「主题性荒诞、神话奇迹」等通用类型词。#1 书名号、#5a 作家类词全包零命中佐证。
3. **借来源背书的说法**：回读四文件无「经典做法是……」「很多名作都……」式句子；恢复句只写适用条件与代价（如「单来源经验默认不作硬门」「读者接受度未证明」），无背书。
4. **删除来源后语义**：diff 逐处复查（plot-rules 19 处、plot-planning 7 处、plot-revision 7 处、SKILL.md 12 处），无主语悬空、无空括号、无表格空列；PL-04/05/08 恢复句与各自反例、流程文件出口三处联动一致（plot-planning §4/§7/§8、SKILL.md §5 卡同步改写）；「未核→未读」替换后 §2/§7/§9 三处语义完整（未读＝范围标记，不再是状态词）。
5. **全包辅助复扫**：`kd32`、`ledger`、Gutenberg、公版、英译、`source-index`、`provenance`、行号锚点 `L[0-9]{3,5}`——本片 4 文件零命中。

## 五、额外静态复查

| 检查项 | 结果 |
|---|---|
| 改动痕迹（补回/续排/编号续排/旧版/本版/更正/融合版/上一版） | 本片 4 文件零命中（#8 全包零命中）；无「本片补回 X」类自述进成品 |
| 审计词与状态码（#9 全模式 + PASS/FAIL/BLOCKED/NOT_APPLICABLE 附加扫） | 本片 4 文件零命中；「效果未证明」为 v3 基线既有诚实口径（plot-rules §0），保留不改 |
| 禁用说法（#11 全模式 +「硬规则」「用户明确要求」「融合版」） | 零命中 |
| 四词状态词 | 本片未新增交付状态句；「未知」为模板规范允许值；plot-revision §4 回归交付句用「未能核实」 |
| 相对链接（SKILL.md + 三个 reference 的 `](...)` 全量解析） | 无断链 |
| GFM 表格分隔行 | 本片新增/改写的表格（§1 归属表、§2 输入权限表、§8 失败出口表、§10 四列路由表、PL-04/05/08 分支行内改动）均有分隔行；逐表核对无「有数据行缺分隔行」 |
| 写入范围 | `git status` 仅既有 `M docs/plans/...` 与 `?? distillation/`；`skills/` 未动（`git diff HEAD -- skills/` 为空）；本包 diff 恰为本片 4 个文件（a2 落点的在途差异为其所有）；未写 log.md／checklist.md／raw 表／desourcing-ledger.md／suite-contract.md／slice-prep.md |
| 与并行片边界 | 本片只写 SKILL.md、references/plot-rules.md、references/plot-planning.md、references/plot-revision.md；a2 范围（plot-diagnosis、plot-examples、plot-scope-and-conflicts、templates/plot-*）与 S05b 范围（serial-*）零写入；共享 notes（source-synthesis）为新建＋追加式，先查后写 |

## 六、待对应分片处理的登记（本片未动的命中）

| 文件（归属分片） | 命中 | 供该分片参考的只读观察 |
|---|---|---|
| `references/serial-zh-webnovel.md`（S05b1/b2） | #4 ×1（:9「一部书**里**的一卷」） | 「书里」在此指用户自己的连载作品（一部书的一卷），非学习材料——按 B.2 第 1 条方向判允许；由 S05b 复核定案 |
| `examples/plot-examples.md`（S05a2） | #5b ×4（:15/:42「The Salt Road」、:74/:109「The Last Tram」）；#10 ×6（:3/:25/:30/:44/:127/:287，均为「读者数据/证据」类词）；#3 说明句「效果未验证」 | 英文名为自创示范作品名（虚构海岸共和国等设定），需过 B.3 骨架比对后由 a2 定案；#10 为误报方向；「效果未验证」建议对齐本片「未证明」口径 |
| `references/plot-scope-and-conflicts.md`（S05a2） | #10 ×3（:90/:119/:148，「数据/证据」类误报方向） | 读原句判误报 |
| `references/plot-diagnosis.md`（S05a2） | #10 ×2（:10/:308，「证据」类误报方向） | 读原句判误报 |
| `templates/plot-diagnosis-report.md`（S05a2） | #10 ×1（:81「待验证」在「没有证据的只放‘待验证’」） | 「待验证」为模板栏位提示词；a2 判断是否对齐四词（建议改「未知」或「未能核实」） |
| `templates/plot-canvas.md`、`plot-scene-table.md`（S05a2） | #5b ×2（标题「Plot Canvas」「Scene Table」） | 模板英文标题，非人名；判允许方向 |
| `examples/serial-examples.md`（S05b1/b2） | #10 ×2（:3/:64，「读者数据」类误报方向） | 读原句判误报 |
| `references/serial-production.md`（S05b1/b2） | #10 ×1（:69「读者数据」误报方向） | 读原句判误报 |

## 七、供 Agent 1 汇总进 `desourcing-ledger.md` 的摘要

> S05a1／story-architecture-and-longform-planning：附录 B 全 11 类正则 + B.3 人工判断已跑完，范围 `output/story-architecture-and-longform-planning/` 全部 21 文件（快照，含并行片在途文件）。全包 29 条命中：#1/#2/#3/#5a/#6/#7/#8/#9/#11 零命中；#4=1、#5b=8、#10=20。本片落点 4 文件（SKILL.md 合同类＋plot-rules/plot-planning/plot-revision）命中 6 条，逐条判允许、零违规（「跨 Skill Owner」1 条为标题短语；「据/见」5 条为证据/数据/判据类正常词误报）；改写前基线的状态词形残留（未证实 ×3、未验证 ×2、尚未验证 ×4、设计推断 ×1、未核 ×4、旧编号痕迹 ×1）已全部清除并复扫归零。恢复/合并落账：PL-01/02/04/05/08 五组软化块按 v0+v1 双佐证恢复（含「B 型不要求同框」「开篇不设第一段硬阈」「不要求唯一合理出口」三处方向性修正）、负触发清单恢复、合同类四表落地。基线/a2/serial 文件命中 23 条全部登记待对应分片（S05a2：plot-examples 英文示范作品名待骨架比对；S05b：serial-zh-webnovel「书里」为用户作品语境），本片未动其文件。B.3 逐文件回读本片 4 份：无新增自创例、无背书、无残迹；相对链接无断链、表格分隔行齐全。**本片落点零违规，可交 W4 独立隔离回读。**
