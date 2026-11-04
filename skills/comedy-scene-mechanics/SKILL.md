---
name: comedy-scene-mechanics
description: "Diagnose or design the scene-level mechanics of comic and humorous fiction: narrator stance (fall-guy vs accomplice), false precision, catalogue escalation, simile-with-a-second-inference, register clash, running-gag signatures, crossed-purposes dialogue, lies that boomerang, recognition reversal, absurd-premise paperwork, meta-narration, and the costs of satire. Built on 24 full-text works (Wodehouse/Twain/Chesterton/Dickens/Thackeray/Wilde/Jonson/Jerome/Collins). For novels and linked sketches, not one-line jokes, sitcom scripts, or pure parody."
---

# Comedy Scene Mechanics（喜剧场景机制工艺）

## 0. 这是什么

人工填表 + 条件判断的设计/诊断 workflow，**不是自动化系统，也没有 scripts**。
- 输入：作者的喜剧设定（体裁、叙述者站位、笑点目标）与/或已有稿（一章或若干场景）。
- 输出：**叙述者站位判定 + 笑点机制配置表 + 场景诊断表**（模板 §7），以及按路由要读的规则。
- 不做：不写正文、不预测"读者会不会笑"、不比较哪种机制更好笑（无读者数据，见 §6）。

## 1. 证据底座

- 样本：24 本，全部为全文本阅读版，逐本台账均通过 `kd32_ledger_gate` 回源门禁（分块覆盖 + 每块要点 + 逐字引文可回源）。合计约 19.6 万行。
- **族去重**：作者族约 9 —— Wodehouse 系 7 本算 1 条独立证据线（PG2042/PG2233/PG6753/PG6768/PG6836/PG6955/PG8713）、Twain 系 7 本算 5 条（PG119/PG3189/PG5784/PG8525 + Huck Finn 三个分章重刊合为 1：PG7100/PG7102/PG7107）、Chesterton 2 本（PG1696/PG5265）算 2 条、Dickens（PG883）、Thackeray（PG4558）、Wilde（PG844）、Jonson 含编者绪论（PG5166）、Jerome（PG308）、Grossmith（PG1026）、Her Ladyship's Elephant（PG28149）、Collins 1729 讽刺论著（PG30343）各 1 条。**同族多本只算一条独立证据。**
- 置信口径：高 = ≥3 族且无反例；中 = 2 族；低 = 1 族或已知反例。规则表 §5 逐条标注。
- 身份标记：**F** = 原文展示（可回源到 PG + 行号）；**H** = 由 F 推出的条件规则；**P** = 可执行动作。

## 2. 触发 / 负触发

### 触发
- 设计幽默长篇或连作短篇的场景级笑点机制（不是宏观"引擎配置"）。
- 已有稿"写得规矩但不可笑"或"笑点很密但读着累"——需要定位是机制缺失还是机制滥用。
- 讽刺作品：靶子、频率与反噬风险的判断。
- 需要判断"叙述者该站在哪里"（自己当笑柄 / 与读者合谋）。

### 负触发
- 单句笑话、段子集、梗图文案（无场景结构）。
- 情景剧/影视脚本（对笑点密度与节奏的要求属于另一媒介）。
- 纯恶搞或戏仿（本体是靶文本，机制不同）。
- 宏观"喜剧引擎选型"（谁制造笑点、全书机制轮换）——那是同类别 `comic-engine-craft` 的范围，本 Skill 不重复、也不替代它。
- 要求"保证读者笑"或"给出笑点密度阈值"：超出证据边界（§6）。

## 3. 输入（缺任一项先问，不猜）

1. **体裁**：长篇小说 / 连作短篇 / 戏剧 / 论辩性讽刺散文。戏剧只走 §5 中标注"戏剧可用"的规则。
2. **叙述者站位**：笑柄（叙述者自己被拆台）还是合谋（叙述者与读者一起看人物出错）。这一项决定能启用哪些机制（§4 G1）。
3. **笑点目标**：角色驱动 / 情境驱动 / 讽刺驱动。
4. **材料**：设定说明，或待诊断的一章/若干场景原文。
5. **讽刺靶子**（若有）：靶子是谁、能否还手——对应 S1 的三栏检查。

## 4. 最短执行路径（3 个门，顺序不可跳）

**G1 站位门**：叙述者会不会被自己的叙述拆台？
- 会（笑柄位）→ 走 M1/M2/M3/M5，禁止启用 M7（读者不再信任叙述者给出的错位语境）。
- 不会（合谋位）→ 走 M7/M8/M9/M11。
- 戏剧/无叙述者 → 跳过 G1，只走 M5/M6/M9/M12③。

**G2 机制门**：这一场缺的是"供给"还是"调度"？
- 缺供给（整场没有笑点）→ [02 错位与清单](references/02-incongruity-devices.md)。
- 缺调度（笑点都在但互相抵消/重复疲劳）→ [03 情节与节拍](references/03-plot-devices.md)。
- 叙述者本身有问题（该笑的地方不笑、不该解释的地方解释）→ [01 叙述者装置](references/01-narrator-devices.md)。

**G3 边界门**：这场有讽刺吗？靶子是谁？
- 有 → 先读 [04 讽刺的成本](references/04-satire-costs.md) 并填三栏检查，再回到机制。
- 无（纯闹剧/纯人物喜剧）→ 跳过。

## 5. 规则索引（M1–M12 + S1，canonical 在各文件）

| ID | 一句话断言 | 置信 | 站位要求 | 位置 |
|---|---|---|---|---|
| M1 | 冷面自欺叙述者：给叙述者一个错误的自我定位，只让他陈述事实与自我评价 | 高 | 笑柄位 | [01 §1](references/01-narrator-devices.md) |
| M2 | 伪精确与冗余计算：在庄重处插入可验证却无意义的数字与算式 | 高 | 通用 | [02 §1](references/02-incongruity-devices.md) |
| M3 | 清单递进：≥4 项，前 3 项递增，末项突然降格 | 高 | 通用 | [02 §2](references/02-incongruity-devices.md) |
| M4 | 比喻延长句：第一句定形象，第二句从比喻内部推出更荒诞的后果 | 高 | 通用 | [02 §3](references/02-incongruity-devices.md) |
| M5 | 语域错位与字面化：专业术语用在最不匹配的日常对象上，且不解释 | 中 | 通用（戏剧可用） | [02 §4](references/02-incongruity-devices.md) |
| M6 | 重复签名与节拍：每章一个签名句出现 2–3 次，第 3 次必须变形 | 高 | 通用（戏剧可用） | [03 §1](references/03-plot-devices.md) |
| M7 | 错位对话：双方各持互斥话题，每句在两边语境中都成立，不加解释者 | 中 | 合谋位 | [03 §2](references/03-plot-devices.md) |
| M8 | 即兴谎言的自生长与反噬：每加一层码就欠后文一件道具 | 中 | 合谋位 | [03 §3](references/03-plot-devices.md) |
| M9 | 认知翻转：先认真建框架再翻，翻转力度 = 前一个框架的强度 | 中 | 通用（戏剧可用） | [03 §4](references/03-plot-devices.md) |
| M10 | 荒诞前提 + 一本正经的机构/流程：用真实文书形式包装不可能的前提 | 中 | 通用 | [03 §5](references/03-plot-devices.md) |
| M11 | 元叙述与机制自陈：先立规则再当面违反，或先嘲笑一种写法再反衬自己 | 中 | 合谋位 | [01 §2](references/01-narrator-devices.md) |
| M12 | 开场三型：伪精确清单 / 元叙述声明 / 通感句（通感句只有 2 族证据，不是通则） | 中 | 通用 | [01 §3](references/01-narrator-devices.md) |
| S1 | 讽刺的成本：靶子能否还手 + 密度是否让作者自己成为笑柄；越界时改用自嘲 | 中 | 有讽刺时必过 | [04 §1](references/04-satire-costs.md) |

## 6. 禁止项

- 不得宣称"保证笑果"、不得给笑点密度阈值：本批无任何读者实测数据，效果比较全部 NOT_PROVEN。
- 族去重：同作者多本只算一条独立证据；Huck Finn 三个分章重刊（PG7100/7102/7107）合为 1 条。
- 不得把单部作品的**情节设计**上升为机制通则（例：PG6836"母亲偷走裤子"、PG3189"推销员打断论文"、PG844"虚构弟弟 Ernest"、PG5265"决斗＝论辩"都是该书/该剧的情节，不是通则）。
- 不得把本批 24 本当作"喜剧幽默类型"的完整画像：批次只是工作量切分。
- 时代性内容（PG883 的阶层描写、PG5784 的性别段落、PG30343 的宗教论战）只能带时代注记引用，不作当代模板。
- 无自动化系统声称；无 scripts；不预测命中率。

## 7. 三张最小模板（输出合同的一部分）

- **站位判定表**：`作品/章节 | 叙述者站位（笑柄/合谋/无） | 启用机制（M1–M12） | 与站位冲突的机制 | 说明`
- **笑点机制配置表**：`场景 | 机制 ID | 原文/计划证据（行号） | 上场同机制? | 疲劳风险 | 待作者决定`
- **场景诊断表**：`诊断项（供给/调度/站位/边界） | 观察到的事实 | 命中规则 | 建议动作 | 证据出处`

空列一律写"未知"，不留空。讽刺类任务额外附 S1 三栏：`靶子是谁 | 他能否还手 | 刺的频率`。

## 8. 失败出口

| 情况 | 能做的 | 不能做 |
|---|---|---|
| 站位未定 | 给 G1 两选项的后果对照（笑柄位禁用 M7；合谋位叙述者不能自己出丑） | 不替作者定站位 |
| 找不到任何机制证据 | 回到 [05 来源索引](references/05-source-index.md) 按族查同族样本，标注"该族仅 1 条证据" | 不用其他族的证据冒充（例：不为 Wodehouse 系设计套用 Chesterton 的论证型喜剧） |
| 机制疲劳 | 用配置表查"上场同机制"，给轮换方案 | 不断言"几章必换"（无阈值证据） |
| 讽刺靶子敏感 | 提示时代注记义务，并给出"改用自嘲"的替代路径 | 不代作者决定靶子；不用 PG30343 的 1729 年立场替当代作品背书 |
| 体裁是戏剧 | 只走 M5/M6/M9/M12③ | 不套用 M1/M11（无叙述者） |

## 9. 文件地图与自检

- [01 叙述者装置](references/01-narrator-devices.md)：M1、M11、M12。
- [02 错位与清单](references/02-incongruity-devices.md)：M2、M3、M4、M5。
- [03 情节与节拍](references/03-plot-devices.md)：M6、M7、M8、M9、M10。
- [04 讽刺的成本](references/04-satire-costs.md)：S1 + 三条保留冲突。
- [05 来源索引与裁决](references/05-source-index.md)：24 本逐本定位、族去重、覆盖档位、对历史规则集 C1–C10 的裁决记录。

自检：本批 24 本台账 100% 通过门禁，但**门禁只验证引文可回源与分块覆盖，不证明阅读深度**；M5/M8/M9/M10/M11/M12/S1 为"中"置信（2 族），M2/M3/M4/M6 为"高"（≥3 族）。GQ5（真实任务验证）未运行。

## 10. 元数据（版本、来源、覆盖、许可、替代关系）

- 版本：v1（round-p4-final-2026-10-30，任务 B-04-B03）。
- 来源数：24（PG1026、PG119、PG1696、PG2042、PG2233、PG28149、PG30343、PG308、PG3189、PG4558、PG5166、PG5265、PG5784、PG6753、PG6768、PG6836、PG6955、PG7100、PG7102、PG7107、PG844、PG8525、PG8713、PG883）。
- 覆盖：24/24 全本台账通过 `kd32_ledger_gate`；未 FULL 来源 0。逐本行数与 SHA-256 见 `notes/source-coverage.md`（本轮目录）。
- 许可与出处：全部原文为 Project Gutenberg 公共域文本的工作区副本（`distill/有原始正文/…`，只读链接）；PG30343 为 1729 年 Collins 论著的 William Andrews Clark Memorial Library 重印本（含 Bloom 夫妇绪论），其宗教论战立场属 1729 年语境；PG5166 的"气质喜剧"论述出自编者绪论而非琼生自述，按 H 级引用。
- 替代关系：**不替代**同类别 `comic-engine-craft`（批次-04，宏观引擎选型）；两者互补——引擎层决定"笑点由谁供给"，本 Skill 决定"每一个场景里笑点怎么落地"。对 `comic-engine-craft` 的历史规则裁决：C2/C3/C5/C7 KEEP（C3/C6 由"低置信"升级为"中"）、C1/C10 REVISE、C9 KEEP 并加条件（宣言的反例走画面外、行动的后果走画面内）、**C8 在本批无任何正例，本 Skill 不采纳**，以 M11（机制自陈）取代；C4 NOT_PROVEN，不进入本 Skill。裁决依据见 [05 §3](references/05-source-index.md)。
