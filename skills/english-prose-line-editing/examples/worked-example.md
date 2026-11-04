# Worked examples · 两个 DESIGN_EXAMPLE

返回 [SKILL.md](../SKILL.md) · 流程 [05](../references/05-workflow-and-failure-modes.md) · 规则 [01](../references/01-mechanics-and-punctuation.md) · [02](../references/02-sentence-revision.md) · [03](../references/03-paragraph-and-emphasis.md) · [04](../references/04-word-choice-and-concision.md) · 来源 06

**状态：`DESIGN_EXAMPLE`。** 下面两段输入是为演示而写的构造文本，不是客户稿。示例只展示“如何按本 Skill 做判断”，不证明规则在现代英语中有效；所有现代适用性仍是 `H/NOT_PROVEN`。

**共同前提**：人工工作流；只改副本；每条 finding 带 `Cxx` 与 《The Elements of Style (Strunk original)》 Lxxx`；作者裁决优先；不自动批量改稿。

---

## Example 1 · 说明文分轮修改

### 输入（构造文本）

> Library fines are an issue that is often discussed. The library has a policy, it charges ten cents a day for overdue books, DVDs and magazines. The policy was approved by the board, which was formed in 2019, and it applies to all borrowers. A survey of this region was made by the library staff. The results were considered to be significant by the staff. Fines are not unimportant. In conclusion, fines are a factor in whether people return books on time.

**R0 scope memo（示例）**

| 项 | 值 |
|---|---|
| 文体 | 说明/评论（library newsletter） |
| 读者 | 普通借阅者 |
| 房规 | 项目 style sheet：Oxford comma；其余未指定 |
| 改动级别 | 句级 + 段末句；允许删冗词，不补事实 |
| 不碰 | 引文、数字、专名、作者语气 |
| 事实边界 | 不新增“罚款提高了归还率”一类因果结论 |

### R1 段落层（分支：说明文，继续）

| ¶ | topic phrase | 段落功能 | 支持句 | 离题句 | 动作 |
|---|---|---|---|---|---|
| 1 | 图书馆罚款政策 | 说明 + 收束 | S1–S7 | 无 | 保留为一段；不拆 |

- 一段一题成立（C20）。
- 末句是结论/后果，属于 Rule 9 的“收束”功能（C21）；先不判“回扣 vs 新意”，留到 R6 前复核（C22先检查主题内后果与末位强调是否兼容）。
- **分支判断**：这是说明文，不是小说对白；继续 R2。若输入是小说场景，转 Example 2 的负触发路径。

### R2 句法层

| 句 | 测试 | 结果 | 规则 | 建议 | 风险 |
|---|---|---|---|---|---|
| S2 | 独立测试 | 逗号两侧各有主谓，无连词 → 逗号粘连 | C03 / | 逗号改分号（最小改动） | 句子的“政策—收费”关系不变 |
| S2 | 系列测试 | `books, DVDs and magazines` 是 3+ 项单连词 | C07 / | 按房规加 Oxford comma | 仅体例差异，不是语法错误 |
| S3 | 指称测试 | 删掉 `which was formed in 2019` 不改变 `the board` 的指称 | C02 / | 保留成对逗号，不改 | 若改成限制性会改变含义 |
| S4 | 施动者测试 | `A survey ... was made by the library staff` 的施动者是 staff，但主语是 survey | C13 / | 改 `The library staff surveyed this region.` | 主语转为staff；若应保留调查/地区为话题，可用This region was surveyed by the library staff |
| S5 | 嵌套测试 | `were considered to be significant` 其中to be significant是系表结构，并非第二个被动；可以讨论表达经济性 | C13 / （主语选择）及C25 | 改 `The staff considered the results significant.` | 施事明确，改主动不丢信息 |

- **未改项**：S3 的 `which` 从句是非限制性，成对逗号正确；不要因为“逗号多”就删。
- **未改项**：S1 的 `that is often discussed` 虽然弱，但删掉后只剩 `Library fines are often discussed.`，不改变命题；留到 R3 处理。

### R3 简洁层

| 原句 | 删除/合并 | 省 | 命题/范围/语气变化 | 采用 |
|---|---|---|---|---|
| `Library fines are an issue that is often discussed.` | 删 `an issue that is` | 4 词 | 无；仍是“常被讨论” | 采用 → `Library fines are often discussed.` |
| `The library has a policy; it charges ten cents a day...` | 删 `has a policy;` | 3 词 | 无；policy 的具体内容就是收费 | 采用 → `The library charges ten cents a day...` |
| `In conclusion, fines are a factor in whether...` | 删 `In conclusion` | 2 词 | 无；但 `factor` 仍空 | 采用删填充语；`factor` 留到 R4 |

- **拒绝删除**：`ten cents a day`、`all borrowers`、`2019` 都是范围/事实，不得为简洁删掉。
- 没有设词数上限；没有把句子全砍短（C25/C33）。

### R4 用词层

| 命中项 | 档位 | 句子真正意思 | recast | 原文是否支持 | 风险 |
|---|---|---|---|---|---|
| `a factor in whether` | 可用但陈腐（第三档） | 罚款会影响是否按时归还 | `Fines influence whether people return books on time.` | 是；“influence”不主张唯一原因 | 比“are a factor”略强，但仍是“影响”不是“导致” |
| `not unimportant` | 否定回避？ | 作者可能想说“罚款并非无关紧要” | **不改**；标 `query` | 无法确定作者是否故意用双重否定 | 改成 `important` 会升级强度（C14） |

- `factor` 不能只换成 `element`；这里整句 recast（C28）。
- `not unimportant` 进入失败出口：见下方“失败出口”。

### R5 标点/机械层

| 定位 | 项目 | 当前 | 房规依据 | 建议 | 仅体例差异？ |
|---|---|---|---|---|---|
| S2 列表 | 系列逗号 | `books, DVDs and magazines` | 项目 style sheet: Oxford | `books, DVDs, and magazines` | 是 |
| S3 | 非限制性从句逗号 | 成对 | C02 | 保留 | 否（语义） |
| 全文 | 所有格/引号/拼写 | 无异常 | — | 不改 | — |

### R6 输出（clean copy + 一个未决 query）

> Library fines are often discussed. The library charges ten cents a day for overdue books, DVDs, and magazines. The board, formed in 2019, approved the policy, which applies to all borrowers. The library staff surveyed this region. The staff considered the results significant. Fines are not unimportant. Fines influence whether people return books on time.
>
> `[query: “Fines are not unimportant” 是否保留双重否定？改成 “Fines matter” 会提高强度；需作者确认。]`

**Diff（摘要）**

| 原文 | 改后 | 规则 | 授权范围/状态 |
|---|---|---|---|
| `has a policy, it charges` | `charges`（R2 改分号；R3 删空结构） | C03 → C25 | 编辑 |
| `A survey ... was made by the library staff.` | `The library staff surveyed this region.` | C13 | 编辑 |
| `The results were considered to be significant by the staff.` | `The staff considered the results significant.` | C13 + C25 | 编辑 |
| `In conclusion, fines are a factor in whether...` | `Fines influence whether...` | C25 + C28 | 编辑 |
| `books, DVDs and magazines` | `books, DVDs, and magazines` | C07 | 房规 |
| `Fines are not unimportant.` | 保留 + query | C14 | **待作者** |

### 语义变化与授权（Example 1）

- **触发**：作者说“把 `not unimportant` 改成肯定句，显得有力”。
- **需要核对的语义代价**：C14 要求正面表述由原文蕴含且不改变强度；`important` / `matter` / `significant` 的强度不同，书内第三例还自认只是 guess。
- **输出**：`停手点：S6 | 触发：要求正向化 | 不能改：强度不明 | 需要作者：你要断言“重要”还是“并非无关紧要”？ | 可选：保留双重否定 / 用 “matter” / 用 “important”`。
- **结论**：未明确允许提高断言强度时保留query；若作者已明确要求断言important，按该授权修改并记录强度变化，不重复询问。

---

## Example 2 · 小说对白：负触发与作者裁决

### 输入（构造文本）

> Mara set the cup down. "You're late," she said. "It's the train," said Ilya.
>
> "It stopped for twenty minutes. In the tunnel."
>
> She looked at him, her hand still on the cup. "Twenty minutes," she repeated. "And you didn't think to call?"
>
> "The signal was dead. I tried."

### 负触发判断（先于任何修改）

| 检查 | 结果 | 动作 |
|---|---|---|
| 文体 | 小说对白 + 叙述 beat | **不套用** C20–C22 主题句、C25 简洁、C13 被动、C14 肯定式 |
| 对白标点 | 说话人标签、逗号、句号基本正确 | 只按 C24 查分段；C01/C03 的对白例外优先 |
| 作者风格 | 短句、碎片、`said Ilya` 语序 | 不把“短”当毛病；不把 `said Ilya` 改成 `Ilya said`（书内无此规则） |
| 可改范围 | 只有一处段落归属明确 | 只改 C24；其余进 query |

### R1 段落层（只做对白分段）

| 话轮 | 说话人 | 当前分段 | 建议 | 依据 |
|---|---|---|---|---|
| 1 | Mara | 与 Ilya 的第一句同段 | 在 `"You're late," she said.` 后分段 | C24 / ：换说话人即换段 |
| 2 | Ilya | 与 Mara 同段 | 独立成段 | 同上 |
| 2 续 | Ilya | `"It stopped... In the tunnel."` 独立段 | 保留；同一说话人继续，不因句号碎片再分段 | C24 + C04 的强调例外 |
| 3 | Mara | 独立段，叙述 beat 同段 | 保留 | C24：beat 跟随其说话人 |
| 4 | Ilya | 独立段 | 保留 | C24 |

**唯一接受的修改**：

```text
Mara set the cup down. "You're late," she said.

"It's the train," said Ilya.
```

- 上面仅展示受影响的原第一段：按说话人拆成两段。后续 Ilya 的 `"It stopped..."` 续段仍独立保留；没有改对白措辞、没有改 `said Ilya`、没有合并碎片或暗中决定续段是否合并。

### R2–R5（只做“不改”的记录）

| 检查 | 结果 | 规则 | 动作 |
|---|---|---|---|
| `"It stopped for twenty minutes. In the tunnel."` | 句号后片段，但在对白中像有意的 afterthought | C04 / ；when_not 允许强调片段 | **不改**；问作者这是否是刻意节奏 |
| `"And you didn't think to call?"` | 真实质问，不是 hedging | C14 / | 不改否定 |
| `"The signal was dead. I tried."` | 短句节奏，删/并会改变人物语气 | C25 / when_not | 不改 |
| `said Ilya` | 书内没有“说话人标签必须前置/后置”的规则 | — | 不改；不是 finding |
| 主题句/段末 | 小说对白不适用 | C21 / | 不检查 |
| 被动 | 无被动问题 | C13 | 不检查 |

### 输出（一个修改 + 两个作者问题）

**Clean copy（仅分段）**

> Mara set the cup down. "You're late," she said.
>
> "It's the train," said Ilya.
>
> "It stopped for twenty minutes. In the tunnel."
>
> She looked at him, her hand still on the cup. "Twenty minutes," she repeated. "And you didn't think to call?"
>
> "The signal was dead. I tried."

**给作者的问题**

1. `In the tunnel.` 是刻意停顿/afterthought，还是应回接成 `It stopped for twenty minutes in the tunnel.`？
   - 保留：节奏更冷、更短；代价是语法上是片段。
   - 回接：更完整；代价是失去停顿。
2. 第一段拆开后，`"It's the train," said Ilya.` 与 `"It stopped..."` 是否要合并成同一段？
   - 合并：同一说话人连续，读起来更顺；代价是段落变长。
   - 分开：节奏更碎；代价是可能被读成换人（本示例不建议，因为无新说话人）。

### 失败出口（Example 2）

- **触发 A**：作者说“把所有碎片都改成完整句”。
  - 动作：这项明确要求已授权相应的句法与节奏调整；没有已锁定声口的互斥约束时，直接改为 `It stopped for twenty minutes in the tunnel.`，说明原先停顿被消除。C04 与 C38-E2 保护有意片段免受默认误改，不禁止作者主动选择完整句。只有与另一项明确禁改要求相冲突时，才把该处留为 query，其余可确定编辑继续完成。
- **触发 B**：作者说“对话太啰嗦，帮我精简”。
  - 动作：按当前授权实际交保义精简稿，例如把 Ilya 的解释收为 `"The train stopped in the tunnel for twenty minutes," said Ilya.`；保留时间、地点、说话人和停运事实，并说明碎片节奏已收拢。`"I tried."` 另承载尝试及自辩，不能因字短就删；若删减会改变已锁定的信息或声口，局部保留或提出具体 query，不据此暂停全部精简。
- **触发 C**：作者说“给我一个更有力的结尾”。
  - 动作：先在现有事实和立场内调整强调。例如 `"I tried. The signal was dead."` 将结尾重心移到通信障碍，不新增人物行为或结果；说明这一重心变化，不保证所有读者都觉得更有力。若进一步方案需要新事实、情节或人物立场，明确标为创作候选，保留与原稿的区别；真正冲突才按 C37 局部待决，不一律拒写。
- **输出格式**：`已完成的授权内修改 | 理由及功能得失 | 局部待定项与具体原因（如有） | 所需下一步（如有）`。

---

## 两个例子共同说明

1. **不是每轮都要产出修改**：Example 1 的 R1 没有改段落，Example 2 的 R2–R5 几乎全是“不改”的记录。记录“为什么不改”与记录“改了什么”同样重要。
2. **规则有 when_not**：说明文的简洁规则不能搬到对白；对白的碎片保护不能搬到说明文。
3. **冲突要停**：Example 1 的 `not unimportant` 与 Example 2 的碎片都不是“技巧不够”，而是作者意图问题。
4. **输出必须可回退**：每条修改带规则、位置、原文、改后及授权范围；已有校对授权可执行普通等义编辑，不要求另找逐项批准人；未决项留在 query，不混进 clean copy。
5. **示例不是验证**：示例不构成真实任务验证；效果仍为 `NOT_PROVEN`。

## 反例复核说明

were considered to be significant只有外层considered为被动，significant是形容词表语；不能用它证明C12双重被动。要测C12，使用原书Gold was not allowed to be exported或He has been proved to have been seen entering the building，并按C12检查改后仍可保留被动。主题内的重要后果可以作为段末新信息；不能因为兼具两种功能就自动阻断编辑。
