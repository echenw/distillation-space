---
name: romance-obstacle-and-cost
description: "Design or diagnose the obstacle-and-cost spine of a romance: who owns the obstacle, who can dissolve it, which ending type the obstacle implies (union / costly union / renunciation / no-closure), and how the cost is booked. Grounded in 19 fully-read 1840s–1920s English-language novels. For novel-length romance plotting and revision, not sweet-scene writing, modern/Asian web-novel conventions, or market prediction."
---

# Romance Obstacle and Cost（言情：障碍归属与代价结算）

## 0. 这是什么

人工填表 + 条件判断的设计/诊断 workflow，不是自动化系统，不含 scripts。
- 输入：作者的言情设定（人物、时代/世界规则、想要的结局形态）或已有稿（可带章节定位）。
- 输出：**障碍归属表**（§7）+ **代价账本**（§7）+ 按路由读取的规则与最小改写建议。
- 不做：不写正文、不预测读者反应或销量、不替代作者对题材的选择。

## 1. 证据底座（诚实口径）

- 样本：19 本 1840s–1920s 英美作品，**全部逐本 100% 分块阅读**（合计 213,375 行），台账 20/20 通过回源门禁 `kd32_ledger_gate.py`（分块覆盖 + 每块 ≥2 要点 + 带行号引文必须在原文 ±3 行内命中）。
- 族去重：19 本 → **15 个独立来源族**（Wharton 3 本 1 族：PG541/PG19191/PG283；1864《Tales of All Countries》2 本 1 族：PG3615/PG3710；Howells 2 本 1 族：PG7141/PG5066）。PG23000 台账未出现作者名，是否并入 Trollope 族 = NOT_PROVEN。
- **角色核账**：支持 13 本、补充 3 本（PG23000、PG24103、PG6688）、反例 3 本（PG70237、PG4629，另 PG6688 兼反例）、不适用 1 本（PG7141）。逐本角色与行号见 [04 来源索引](references/04-source-index.md)。
- **不是当代言情**：全批无 1940 年后语料，无东亚/网文语料，无读者数据。所有现代迁移标 H/NOT_PROVEN；所有"读者会……"标 NOT_PROVEN。
- 标记：**F** = 原文展示；**H** = 归纳的条件规则；**P** = 可执行动作；**NOT_PROVEN** = 证据不足。

## 2. 触发 / 负触发

### 触发
- 设计长篇言情的**阻力结构**："他们为什么不能马上在一起，撑得住几十章吗"。
- 中段塌陷：反复误会、角色原地打转、障碍说不清在谁身上。
- 结局选择：该结合、该付出代价地结合、还是该不结合。
- 已有稿诊断："结局不结实""赢了但没付代价""退让写成了误会没解开"。
- 婚后线/续卷张力：婚礼之后靠什么继续。

### 负触发
- 只要一场甜宠/告白场景的写法（无阻力结构需求）→ 不调用。
- 现代都市/东亚网文/轻小说语境（本批无语料，只有 H 级迁移意见）。
- 诗歌、歌词、剧本分镜、非虚构情感建议。
- 要求"保证读者感动/保证爆款" → 超证据边界，明确拒绝。
- 单本书的文本校对、语言润色。

## 3. 明确输入（缺什么就问什么，不猜）

| 输入 | 必需 | 缺失时的出口 |
|---|---|---|
| 篇幅与形态（长篇 / 中篇 / 连载） | 是 | 本 Skill 按长篇设计，短篇只给简化路径 |
| 时代与世界规则（阶层、财产、婚姻制度、名誉规则） | 是 | 无世界规则 → 先做世界规则表，否则障碍无法归属 |
| 双方人物与各自名下的资源/负债 | 是 | 缺则无法填障碍归属表 |
| 想要的结局形态（或"未定"） | 是 | 未定时先做 §5 G1 的四选一 |
| 已有稿（可选，带章节/段落定位） | 否 | 无稿只给检查清单，不虚构诊断 |

## 4. 任务路由

| 任务 | 先读 | 再读 | 首要输出 |
|---|---|---|---|
| 设计/修阻力结构 | [01 障碍归属](references/01-obstacle-ownership.md) | — | 障碍归属表 |
| 中段塌陷、误会滥用 | [01 §3](references/01-obstacle-ownership.md) | [02 §2](references/02-ending-and-cost.md) | 延迟装置替换方案 |
| 结局形态与代价 | [02 结局与代价](references/02-ending-and-cost.md) | — | 代价账本 + 结局方案 |
| 舆论/群像/多视角 | [03 舆论与视角](references/03-social-pressure-and-pov.md) | — | 闲话→行动对照表 |
| 核对来源、族去重、冲突 | [04 来源索引](references/04-source-index.md) | [05 裁决与冲突](references/05-adjudication-and-conflicts.md) | — |

## 5. 最短执行路径（2 个门）

**G1 结局形态四选一**（先定结局，再倒推阻力 — 本批不提供"哪种更好"的证据，由作者决定）：

1. **结合**（union）— PG1260、PG161、PG43168、PG27990、PG3632、PG41031。
2. **代价型结合**（costly union）— 结婚但账不清 — PG12557、PG19191。
3. **退让型**（renunciation）— 外部障碍清零后当事人仍选择不结合 — PG541、PG283、PG6688。
4. **无结局**（no-closure）— 不给复合也不给和解场景 — PG70237。

选不定就先看 §7 的代价账本：若你能写出"谁替谁付了什么"，选 2 或 3；写不出就别选 3。

**G2 障碍归属**（在谁名下、谁有权解除）：
- 在**第三方名下**（家族/遗嘱/旧承诺持有人/社会体面）→ 01 §1 硬障碍清单 + 01 §2 解除权。
- 在**当事人自己名下**（秘密、过去的经历、自我判定的"不配"）→ 01 §4。
- 只靠**误会** → 01 §3：降级为一次性转折器，必须补硬障碍。

## 6. 规则索引（10 条；canonical 在各 reference）

| ID | 一句话断言 | 标记 | 置信 | 位置 |
|---|---|---|---|---|
| O1 | 障碍必须挂在"能解除它的人"名下，挂错了中段必塌 | F→H→P | 中 | [01 §1](references/01-obstacle-ownership.md) |
| O2 | 硬障碍五型：旧承诺 / 财产资格 / 遗嘱条款 / 过去的秘密 / 体面与舆论 | F→H | 中 | [01 §1](references/01-obstacle-ownership.md) |
| O3 | 持续延迟用硬障碍；误会只做一次性方向转折，且必须改变下一步行动 | F→H→P | 中 | [01 §3](references/01-obstacle-ownership.md) |
| O4 | 承诺的解除必须由持有人本人执行；第三方代解除即成操控 | F→H→P | 中 | [01 §2](references/01-obstacle-ownership.md) |
| O5 | 误认型障碍的价值在于"重写角色对旧事的解释"，不在错位笑料 | F→H→P | 中低 | [01 §4](references/01-obstacle-ownership.md) |
| E1 | 退让型结局 = 障碍先清零 → 当事人主动不动 → 一个可观察的小动作把它固定 | F→H→P | 中 | [02 §1](references/02-ending-and-cost.md) |
| E2 | 代价账本三行：谁失去什么 / 谁替谁付 / 可否结清；结合不等于结算完成 | F→H→P | 中 | [02 §2](references/02-ending-and-cost.md) |
| E3 | 财产方向由归属决定：资格条款断裂即退婚，拉平装置则促成 | F→H | 中（有反例） | [02 §3](references/02-ending-and-cost.md) |
| S1 | 舆论按"一句闲话 → 一次行动改变"的粒度工作，不是氛围 | F→H→P | 中 | [03 §1](references/03-social-pressure-and-pov.md) |
| S2 | 多视角同一事件：每个视角必须有不同利害关系（单族证据，PG5066） | F→H | 低 | [03 §2](references/03-social-pressure-and-pov.md) |

## 7. 两张最小模板

**障碍归属表**

```
障碍 | 写在谁名下 | 谁有权解除 | 解除的条件/代价 | 该人愿不愿意解除 | 若被解除，谁受损 | 来源依据
```

**代价账本**

```
谁失去了什么 | 谁替谁付了 | 这笔账能否结清（可/不可/未定） | 由谁说出来（当事人/第三方/时间）
```

空列写"未知"，不要留白也不要编。

## 8. 禁止项

- 不得把 PG23000 / PG24103 / PG6688 / PG70237 / PG4629 / PG7141 当言情样本：前两本的法律/继承案、PG6688 的成长主线、PG70237 的不婚者主线、PG4629 的家庭训诫、PG7141 的速写集都不是恋爱引擎。
- 不得把 PG4629 的训诫（"妻子绝不可与丈夫对立"）当当代规则；引用必须带时代注记（详见 [05 §3](references/05-adjudication-and-conflicts.md)）。
- 不得声称"读者会更喜欢 X 结局"：无读者数据，一律 NOT_PROVEN。
- 不得把误会用成中段持续供能；不得让误会不改变任何行动。
- 不得把单族证据（PG5066 的十二视角）说成言情通则。
- 不得声称自动化：本 Skill 是填表 + 判断 workflow。

## 9. 失败出口

| 情况 | 能做的 | 不能做 |
|---|---|---|
| 世界规则没定（无阶层/财产/婚姻制度） | 先给世界规则表的最低项（财产谁继承、谁能解除婚约、什么算丑闻） | 不设计障碍 |
| 作者只要甜宠 | 说明适用边界并交还 | 不硬套阻力结构 |
| 障碍判定不出归属 | 给 O2 五型清单逐项试填 | 不替作者选 |
| 结局选不定 | 先填代价账本，用"写不写得出代付"来筛 | 不按"读者更喜欢"推断 |
| 现代/东亚语境 | 标 H 迁移意见并注明无本批语料 | 不假称有证据 |
| 要市场/效果保证 | 明确拒绝并说明 NOT_PROVEN | 不给数字、不承诺 |

## 10. 文件地图与自检

- [01 障碍归属](references/01-obstacle-ownership.md)：O1–O5、硬障碍五型、解除权、误会的降级用法。
- [02 结局与代价](references/02-ending-and-cost.md)：E1–E3、四型结局写法、代价账本、财产方向冲突。
- [03 舆论与视角](references/03-social-pressure-and-pov.md)：S1–S2、闲话→行动对照、十二视角。
- [04 来源索引](references/04-source-index.md)：19 本逐本角色、族去重、行号定位、SHA 与覆盖。
- [05 裁决与冲突](references/05-adjudication-and-conflicts.md)：对批次-02/03/06 历史规则的 KEEP/REVISE/REJECT/NOT_PROVEN 裁决与三条保留冲突。

自检：19 本全文覆盖、20/20 台账过门禁、15 独立来源族；无 scripts；P5 宿主真实任务测试未运行（GQ5 = NOT_PROVEN）。
