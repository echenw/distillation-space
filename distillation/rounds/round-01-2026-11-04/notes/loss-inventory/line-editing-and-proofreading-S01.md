# 分片丢失清单与逐条决定 · line-editing-and-proofreading（S01）

- 片名：**S01**｜代理：**Agent 2**｜轮次：**W2 校准**｜日期：2026-11-04
- 依据：计划附录 A.2（逐条记录格式）、附录 A.3（断点续做）、第 6 节 P3 第 1 条、`notes/suite-contract.md`（K2 定稿）、`notes/loss-inventory/raw/line-editing-and-proofreading-2026-11-04.md`（K1 raw 表）。
- 列定义：按附录 A.2 的 8 个字段，另在首列加「片名」标记以合派发说明的 9 列。来源位置**只在 notes**。
- 状态口径：本片全部决定已处理完毕；「已写入 output」表示决定已落账、恢复／合并已写入成品。独立隔离回读按 D3-C 留 W4 由 Agent 1 另派只读子代理，本片状态不写「已回读」，不自审自过。
- 「不恢复」三类的排除口径：有意口径调整、已改正的事实错误、作品专属内容（计划 P1）。缩减幅度只作盘点信号，不作为应补回的量。

| 片名 | 编号 | 来源位置 | 丢失类型 | v3 现状 | 决定 | 理由 | 成品落点 | 状态 |
|---|---|---|---|---|---|---|---|---|
| S01 | LI-LE-001 | v2 `3c1cb5f:skills/line-editing-and-proofreading/references/en-mechanics-and-punctuation.md` EN-01–EN-10；v0 C01–C10 | 规则小块（用于／不用／做法／记录／反例） | 部分：只剩规则／怎么做／不用／自拟例 | 合并 | 通用区分条件与反例属规则本体，去来源时被连带删除，非有意口径调整 | `references/en-mechanics-and-punctuation.md` EN-01–EN-10 | 已写入 output |
| S01 | LI-LE-002 | v2 `.../references/en-sentence-revision.md` EN-11–EN-19；v0 C11–C19 | 规则小块 | 部分：9 条各剩 4 行 | 合并 | 同上 | `references/en-sentence-revision.md` EN-11–EN-16、EN-31–EN-33 | 已写入 output |
| S01 | LI-LE-003 | v2 `.../references/en-paragraph-and-emphasis.md` EN-20–EN-24；v0 C20–C24 | 规则小块 | 部分：7 条各剩 3 行 | 合并 | 同上 | `references/en-paragraph-and-emphasis.md` EN-17–EN-23 | 已写入 output |
| S01 | LI-LE-004 | v2 `.../references/en-word-choice-and-concision.md` EN-25–EN-29；v0 C25–C29；文件头「核心平衡」 | 规则小块、规则本体 | 部分：7 条各剩 3 行，核心平衡句已无 | 合并 | 同上；「具体化不得补写事实、简洁不得删范围限定词」是通用原则 | `references/en-word-choice-and-concision.md` EN-24–EN-30 与文件头 | 已写入 output |
| S01 | LI-LE-005 | v2 EN-05「并列从句前的逗号」；v0 C05 | 整条规则 | 没有：v3 EN-05 主题改为「并列结构」 | 恢复 | 主题独立（连词前逗号、but 不省、同主语紧凑句可省），合并会走样；用通用写法与自创例 | `references/en-mechanics-and-punctuation.md` EN-34 | 已写入 output |
| S01 | LI-LE-006 | v2 EN-08「括号的标点」；v0 C08 | 整条规则 | 没有 | 恢复 | 括注内外标点规则独立，合并会走样 | `references/en-mechanics-and-punctuation.md` EN-35 | 已写入 output |
| S01 | LI-LE-007 | v2 EN-16「相关词靠近与 only／not／all 辖域」；v0 C16 | 整条规则 | 没有 | 恢复 | 限定词辖域是独立区分条件，中文 SR-05 不能替代英文条目 | `references/en-sentence-revision.md` EN-36 | 已写入 output |
| S01 | LI-LE-008 | v2 EN-18「摘要时态」；v0 C18 | 整条规则 | 没有：v3 EN-31 只讲时态一致 | 恢复 | 基准时态、间接引语、删转述标签与「时态一致」侧重点不同 | `references/en-sentence-revision.md` EN-37 | 已写入 output |
| S01 | LI-LE-009 | v2 EN-19「松散句连排」；v0 C19 | 整条规则 | 没有 | 恢复 | 连续同型句的判断与「不设阈值」的区分条件独立 | `references/en-sentence-revision.md` EN-38 | 已写入 output |
| S01 | LI-LE-010 | v2 EN-21「主题句是说明／论辩的默认」；v0 C21 | 整条规则 | 部分：v3 EN-17 残留「不必每段都有显式主题句」 | 恢复 | 残留句不足以覆盖说明段默认、叙事段不硬加、公式化起句等区分条件 | `references/en-paragraph-and-emphasis.md` EN-39 | 已写入 output |
| S01 | LI-LE-011 | v0 C22「段末：回扣还是新意（两说）」；v2 EN-22 | 整条规则（含 A／B 分支） | 部分：v3 workflow 冲突裁决有一条 | 恢复 | 需要 A／B 两版、冲突点与失败出口，是 R18 §2d 的载体 | `references/en-paragraph-and-emphasis.md` EN-40；`examples/worked-example.md` 例三 | 已写入 output |
| S01 | LI-LE-012 | v0 C26／v2 EN-26 固定冗语对照表 | 例子／对照表 | 没有 | 恢复 | 恢复「可压缩 + 采用前复检从句类型／时态／强调」的规则；具体搭配按用户指定全部换成自创例子 | `references/en-word-choice-and-concision.md` EN-25 对照表；`references/workflow.md` 第 4 轮第 2 步 | 已写入 output |
| S01 | LI-LE-013 | 11-02 三版审计线索 L-1；附录 E `LE-T3` | 例子（负触发完整示例） | 没有：`examples/worked-example.md:17` 只有第 0 轮 | 恢复 | 基线版本一直缺，v0 无可搬原文；用户指定补完整「先判负触发」示例 | `examples/worked-example.md` 例三；`SKILL.md` §1／§7／§8.2 | 已写入 output |
| S01 | LI-LE-014 | 11-02 审计线索 L-2；v0 C27／C28 | 例子（EN-27 示范） | 没有：EN-27 只有规则／怎么做／限制 | 恢复 | 补自创示范（输入／不合格改法／合格改法／证据前提／检查／出口），注明「具体化不能补写事实」 | `references/en-word-choice-and-concision.md` EN-27 示范与 EN-26；`SKILL.md` §8.2 | 已写入 output |
| S01 | LI-LE-015 | `notes/suite-contract.md` 附录 C.3 第 2 条；计划 §2.6 | 接口字段（description） | 部分：只提 story、character | 合并 | description 写全会转去的 7 个兄弟 skill 名，含 `preset-card-generation` | `SKILL.md` frontmatter description | 已写入 output |
| S01 | LI-LE-016 | `notes/suite-contract.md` 附录 C.1／C.2／D2-A 两表 | 接口（触发／负触发／兄弟转介） | 部分：只有「转给别的 skill」列表 | 合并 | 写清触发清单、负触发清单、C.2 相关行、与 preset-card 的双向转介 | `SKILL.md` §1.1／§1.2／§1.3、§10 | 已写入 output |
| S01 | LI-LE-017 | 计划 §2.6；R18 §3 | 接口（路由表两列） | 没有 | 恢复 | 路由表加「需要时补读／缺料或冲突时的出口」两列，保证全部找回内容可从 SKILL.md 到达 | `SKILL.md` §7 参考文件表 | 已写入 output |
| S01 | LI-LE-018 | `notes/suite-contract.md` 第二节；计划 §2.6 | 接口（失败出口、状态词） | 部分：停手情形只在 workflow | 合并 | SKILL.md 补失败出口表与四词状态；不出现审计词、分档词、禁用说法 | `SKILL.md` §8.1／§8.2 | 已写入 output |
| S01 | LI-LE-019 | R18 §2d | 复杂操作深度 | 没有 | 恢复 | 判断标准、步骤、诊断→修订闭环、自创难例（A／B 分支与失败出口）、负面回归 | `references/workflow.md`「复杂操作」节；`examples/worked-example.md` 例三 | 已写入 output |
| S01 | LI-LE-020 | R18 §2a | 模板字段 | 部分：旧台账 8 列 | 合并 | 改为每个编号一行、三列「值／状态／稿件证据位置」，允许「未知」，保留 GFM 分隔行 | `references/workflow.md` 第 0 轮；`examples/worked-example.md` 例三第 3 步；`SKILL.md` §8.1 | 已写入 output |
| S01 | LI-LE-021 | 附录 B.3；v3 `references/zh-mechanics.md` 间隔号例 | 来源残留（真实人名） | 部分：用真实作家音译名作间隔号例 | 合并 | 换成自创音译人名并注明「自拟」；B.3 人工判断命中，正则查不出 | `references/zh-mechanics.md` SR-13 间隔号例 | 已写入 output |
| S01 | LI-LE-022 | 附录 B.3／措施禁用；计划 §8 | 来源与改动痕迹措辞 | 部分：泛称「作家」、元声明「不出自任何作品」、禁用词列举句、编号来历说明 | 合并 | 逐句通读改过的句子后做措辞微调，不删规则内容；成品不提补回／续排／本版／原文出处 | `references/zh-sentence-and-wording.md`、`references/zh-mechanics.md`、`references/workflow.md`、四个 `en-*.md`、`SKILL.md`、`examples/worked-example.md` | 已写入 output |
| S01 | LI-LE-023 | K1 raw 表 `MISSING`；v0 `d23c461:skills/style-refinement-and-proofreading/references/source-index.md` | 整个文件 | 没有（v3 无对应） | 不恢复 | 来源索引本身是出处清单，无可通用规则可提；红线禁止恢复来源编号／年代／篇数 | 无 | 已写入 output |
| S01 | LI-LE-024 | v0 C29／v2 EN-29 历史词表条目表（年代词形、人称分工等 12 行） | 条目表（年代／篇数／来源立场） | 部分：v3 EN-29 只留通用处理原则 | 不恢复 | 年代、篇数与来源专属立场；后版已通用化，属有意口径调整 | 无（保留 `references/en-word-choice-and-concision.md` EN-29 通用原则） | 已写入 output |
| S01 | LI-LE-025 | v0 四份 `en-*.md` 的 F／P／H 标记、可信度、书内明说／两说／未证实、来源编号与行号、书内英文原句 | 来源痕迹与原句 | 没有（v3 已删） | 不恢复 | 红线：不恢复书名／作者／原句／来源编号／年代／篇数；删除是去来源的正确结果 | 无 | 已写入 output |
| S01 | LI-LE-026 | v0 `SKILL.md` frontmatter 的 sources 字段、§6／§9 的书名与年代、§7 的来源索引路由行 | 来源残留 | 没有（v3 已删） | 不恢复 | 同上 | 无 | 已写入 output |
| S01 | LI-LE-027 | K1 raw 表 `examples/worked-example.md SHRUNK`；v0 示范用 C01／C11／C07 编号 | 编号与例子 | 改号后保留：v3 用 EN-01／EN-11／EN-07；例子骨架为自创 | 不恢复 | 编号改号不算丢失（计划 §2.3）；自创例子与来源案例无可比对差异，不重写 | 无 | 已写入 output |

---

## 附录 B 扫描结果与逐条判断（摘要；详细自检见 `notes/quality/line-editing-and-proofreading/s01-desourcing-selfcheck.md`）

- 范围：`output/line-editing-and-proofreading/` 全部 10 个文件；命令统一用 `/usr/bin/grep -rnE`（本机 `grep` 是 ugrep，中文长模式会报 `exceeds complexity limits`）。
- 全 11 类复扫结果：**#1、#2a、#2b、#3a、#3b、#3c、#4、#5a、#5b、#7、#8、#9、#11 共 9 组零命中**；**#6 命中 1 条**、**#10 命中 14 条**，合计 15 条命中。
- 逐条判断结论：**15 条全部判为允许，零违规**。
  - **#6 的 1 条**（`references/en-mechanics-and-punctuation.md` EN-08 自拟例 `She said, "The meeting starts at noon."`）：自创的英文直接引语示范，用于对比直接／间接引语，不是任何作品原句；按 B.2「自创例子」精神与 B.3 骨架比对（无人物关系、关键事件、时代地点可对应来源案例）判允许。
  - **#10 的 14 条**分三类，均为正则固有误报或 B.1 明确例外：
    1. 讲中文标点用法时列举的空括号符号 `（）`（`zh-mechanics.md` SR-13）——附录 B #1 对书名号符号本身的例外同理，属标点用法列举。
    2.「常见，」被 `见[，。；]` 命中 2 条（`zh-mechanics.md`、`SKILL.md` 对白格式表）——「常见」是正常词，不是删除来源后悬空的「见」。
    3.「依据，」「证据。」「根据」等正常词后跟标点被 `据[，。；]` 命中 11 条——其中 `references/workflow.md` 的「没有依据，按作者判断」是计划第 8 节要求的固定说法，不能为躲正则改写；其余均为完整句，主语明确，语义通顺，不是悬空的「据」。
  - B.2 允许情形已逐类写明理由：用户稿件「原文／原稿」（全篇多处，指用户正在改的稿子）、本包内部编号（SR／EN／L0–L4）、模板规范里「不指向来源编号」的元说明、状态词「依据」的释义句「不是来源背书」。
  - B.3 人工判断：逐文件回读未见与 v0 来源案例情节骨架相近的例子（人物关系／关键事件／时代地点三项无两项以上对应）；未见具体作品标志性情节元素；未见「经典做法是……」「很多名作都……」式背书；删除来源后无主语悬空、半句、表格空列；「列夫·托尔斯泰」等真实人名已换为自创人名（LI-LE-021）。
  - 顺手消除的命中（不属最终 15 条）：元说明里的「出自」「批次」、禁用词字面列举句、`When Lena` 连续首字母大写词，均已改写并复扫确认零命中。
- 额外复查：改动痕迹字样（补回／续排／已有编号／旧版／本版／更正／融合版）**零命中**；审计词与状态码（#9）**零命中**；禁用说法（#11）**零命中**；相对链接全部可解析；含数据的表格均有 GFM 分隔行。
- 结论：本片成品包可交 W4 做独立隔离回读；本记录不写公共 `desourcing-ledger.md`，摘要回传 Agent 1 汇总。

---

## 本片断点（供 Agent 1 追加 `log.md`）

- 片名：**S01**
- 处理到的编号：**LI-LE-001 至 LI-LE-027**（27 条决定齐全；恢复／合并 22 条、不恢复 5 条）
- 下一步：S01 校准样例与写法口径已回传，W3 其余 5 个代理按 `notes/source-synthesis/line-editing-and-proofreading.md` 第二节落笔；本片附录 B 摘要交 Agent 1 汇总进 `desourcing-ledger.md`；独立隔离回读与 GQ1–GQ4 按 D3-C 留 W4 由 Agent 1 另派只读子代理。
