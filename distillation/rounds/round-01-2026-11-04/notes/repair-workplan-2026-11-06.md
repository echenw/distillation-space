# 修复批工作单（参数化 · 2026-11-06 主代理预写）

- 触发：作者答复 13 条决定件（`notes/user-decisions-2026-11-05.md`，`nA` 或「全部按推荐」）。答复到达前**不执行**本单任何落笔。
- 原则：**一次过**（全部 output/ 与 brief 改动单批完成，避免 8 份正式 review 绑定反复过期）；修复席不携「作者裁决」名义自创新口径，逐处改动落 repair ledger；GQ5 维持 NOT_PROVEN。

## 一、改前快照
8 包整树 SHA 与 brief sha 取 tsv 现行值（genre `ef3668e4…`/101/1,058,213），留照 scratchpad；确认无并发写入者。

## 二、决定件落地（按答复分支执行，未选分支跳过）
- #1A：character `boundaries-and-ethics.md` §1 外加「即时危险→一句现实求助指引」小节（不指名机构/不判断现实/不替代专业）；#1B：character＋fiction-planning＋scene 各一行。
- #2A：scene 删 SKILL/references 重复表（留 SKILL 唯一表）；story 定义从 serial-platform-migration.md:52 上浮 SKILL 层；cross-media 以 SKILL:201 为准并给「本轮未执行」归档位；#2B：只修 scene 重复与 cross-media 分歧。
- #3A：无动作（spec 已按占位行合法预写）；#3B：scene action-checklist、cross-media branch-sheet（AD 族 40 行）、story serial-tables 逐项成行。
- #4B：story SKILL §10 四行「同上」（:384/:386/:387/:388）逐行补独立句（取各文件实有出口，不新造）。
- #5A：无动作；#5B：genre §4 十四行补「需要时补读／缺料或冲突时的出口」两列（会位移 brief 锚，触发 F-01 全量重算）。
- #6A：preset-card 两处定义「含标点的非空白字符数，小节标题行不计」＋示例卡复测（607 应在带内）；#6B 纯汉字（482 落带外须动内容）；#6C 删数字带。
- #7A：SKILL.md:150 改「三状态＋依据作附件」＋已知降级记录槽；expression「正文」双义改名；§3 明写「本包不提供空白模板」。
- #8A：「本包用「」标记术语与条目名，稿件引号仍按 SR-13」一句＋GB/T 15834/15835 编号保留＋worked-example 稿件片段引号统一。
- #10A：fp `SKILL.md:32/:147` 改「按 genre 的题材契约核对，缺项回本包登记」；#10B：genre 让出 `:17`（十四题材目录联动改）。
- #11A：genre §6（:99-102）措辞改与实际一致（分流表在 guide 首节、标题不统一；触发条件由 rules 承担）——行内改文不动锚；#11B：4 篇标题统一＋14 篇补触发栏（228 锚重算，冻结顺延）。
- #12：保留原句（CY-07 防口已覆盖）或抽象为「危险器具」；#13：豁免并按 W4-123 先例登记。

## 三、GQ 修复（分支无关部分）
- **fp SEM-01–05/07**：SKILL.md:65 vs :86 赛道指令二选一归口（其余按 #2 落定口径）；删减方案数/提问数/类型契约归属/规则卡字段声明/路由具名逐组收口；scope-and-conflicts §2 K 表不扩（交付口径归口后引它）。
- **preset-card SEM-01–03**：:200 承诺句对齐 §1/§9.2；SKILL.md:68 禁令强制程度与 card-method:56/expression:102 加回链；writing.md:12 默认文风与 style.md:71 定位/冒名回链。
- **line-editing S-01/S-02**：台账「一编号一行」与例三 SR-10 两行归口（或例三改单行）；四套列名统一（与 #8 联动）。
- **character SEM 三组**：pov-cases.md:110/111/:136 示范行改标（按 #1/#2 联动）；narrative-workbook:142 与 :134/:140 消歧；四词↔五档映射行（SKILL §9.1）。
- **scene GQ2**：「单元」定义归一（SKILL:177 vs intensity :11/:28）；intensity 文件内 :3/:36 与 :28 自相矛盾修复；SU-07 卡体六字段补齐；workflow/出口表补「无授权不写文件」行。
- **GQ3×3**（按 #10 落定）：fp 六向接收行＋模板「转出去向」列＋§8 自查第七问；preset-card this→genre 行级闭合（或按 #10B 撤）；character IF-01（切片表互认/字段映射）＋IF-03（preset-card 7↔3 互逆对齐）＋IF-05（公平解谜 Owner 唯一化）。
- **Q6（#11A 路径）**：§6 措辞改写。
- **brief 层**：F-01 六处结论按现树更正＋brief 重冻结（新 brief_sha）；F-05 八处真缺陷补缀（4 裸对端行号 +1：scene:289/character:307/fp:147/line:188；4 gaps 裸文件名）；W4-116 前缀补缀；F-06 genre description 补 preset-card 行。
- **W4-14/15**：FC-21 confidence 字段中文化（LI-FP-134 RV-05 先例）＋术语 10 处处置（坐标在 CL-verify 6.1）。
- **spec/INDEX/JSON**：W4-47 边界句入 character spec；prose/标题级 ID 判定按 8 份 review 的 ID census 定档；INDEX/JSON 依修复后树重算（W4-09 冻结在整树 SHA 后）。

## 四、复测与冻结
1. 全 8 包附录 B 11 类重扫（零新增违规为门槛）。
2. 8 包重绑复测：树迁移后整树 SHA 重测、peer 值刷新（**genre peer 三处旧值 07d638e5：scene/story/crossmedia 三份正式件**→一律 ef3668e4 后新值）、锚抽验。
3. 冻结：tsv 单笔更新 → brief/field_ids 冻结（W4-09 销）→ checklist 状态改「出口」→ log.md 收官行 → desourcing-ledger 修复批节。
