# Agent 1 静态核查结论 · S01（line-editing-and-proofreading）

- 轮次：W1.5 / W2 汇总轮｜角色：**Agent 1（规范与门禁仲裁员）**｜日期：2026-11-04
- 性质：**只读门禁核查**，不改 Agent 2 任何文件（`output/`、`notes/source-synthesis/`、`notes/loss-inventory/` 均只读）。
- 范围：`R/output/line-editing-and-proofreading/` 全部 10 文件；对照 `R/notes/source-synthesis/line-editing-and-proofreading.md`（校准样例）与 `R/notes/loss-inventory/line-editing-and-proofreading-S01.md`（分片记录）。
- 命令统一用 `/usr/bin/grep -rnE`（本机 `grep` 是 ugrep，中文长模式报 exceeds complexity limits）；原始输出见同目录 `agent1-s01-desourcing-rescan-2026-11-04.txt`。
- **本核查是静态核查，不含 GQ5 真实任务测试（未授权）；未验证项一律不写成通过。**

---

## 一、EN-34–40 的来源判定（重点）

判定口径：计划第 3 节「不新增材料里没有的知识」。逐条在 v0 `d23c461:skills/style-refinement-and-proofreading/` 找对应标题编号；**7 条全部找到，非自创新规则**。

| 成品编号 | 成品落点 | v0 对应编号 | v0 位置（标题行） | 判定 |
|---|---|---|---|---|
| EN-34 并列连词前的逗号 | `references/en-mechanics-and-punctuation.md:113` | C05「并列从句前的逗号」 | `references/en-mechanics-and-punctuation.md:70` | 有来源（改号 C→EN） |
| EN-35 括注的标点 | `references/en-mechanics-and-punctuation.md:124` | C08「括号的标点」 | `references/en-mechanics-and-punctuation.md:115` | 有来源（改号） |
| EN-36 限定词辖域与相关词靠近 | `references/en-sentence-revision.md:102` | C16「相关词靠近与 only/not/all 辖域」 | `references/en-sentence-revision.md:86` | 有来源（改号） |
| EN-37 摘要时态 | `references/en-sentence-revision.md:113` | C18「摘要时态」 | `references/en-sentence-revision.md:116` | 有来源（改号） |
| EN-38 松散句连排 | `references/en-sentence-revision.md:124` | C19「松散句连排」 | `references/en-sentence-revision.md:131` | 有来源（改号） |
| EN-39 主题句与段落功能 | `references/en-paragraph-and-emphasis.md:78` | C21「主题句是说明/论辩的默认，不是通例」 | `references/en-paragraph-and-emphasis.md:26` | 有来源（改号） |
| EN-40 段末的两种处理 | `references/en-paragraph-and-emphasis.md:89` | C22「段末：回扣还是新意（两说，冲突卡）」 | `references/en-paragraph-and-emphasis.md:41` | 有来源（改号） |

- 分片记录 `LI-LE-005` 至 `LI-LE-011` 的来源位置写为「v2 EN-xx；v0 Cxx」，与上述 v0 核对一致；v0 四份 `en-*.md` 共 C01–C29 连续，编号体系完整。
- 结论：**不构成「自创新规则」阻塞**。编号由 C 系列改为 EN 系列属计划 2.3 节「编号消失不等于丢失」的改号，成品不解释编号来历（附录 B #8 零命中，见下）。

## 二、附录 B 全 11 类独立复扫

| 类 | 命中 | 类 | 命中 |
|---|---|---|---|
| #1 书名号作品名 | 0 | #6 英文原句 | **1** |
| #2a PG 来源编号 | 0 | #7 包外路径 | 0 |
| #2b `-NNNN` 残片 | 0 | #8 改动痕迹 | 0 |
| #3a 数量年代 | 0 | #9 审计词 | 0 |
| #3b 材料标称 | 0 | #10 删除残迹 | **14** |
| #3c 年代+市场/手册 | 0 | #11 分档/禁用说法 | 0 |
| #4 指向学习材料 | 0 | | |
| #5a 作者/名人 | 0 | | |
| #5b 拉丁人名 | 0 | | |

- **合计 15 条命中（#6 1 条 + #10 14 条），其余 13 组零命中**，与 Agent 2 回传摘要（9 组零命中 / #6 1 / #10 14 / 零违规）**数字一致**（Agent 2 按「组」合并子项计数，本表按 15 个子模式列）。
- 逐条"允许"判断由 Agent 2 在 `s01-desourcing-selfcheck.md` 与分片记录 §附录 B 摘要给出：#6 为自创英文直接引语示范；#10 为 `（）` 标点列举、`常见，`、以及「依据，」「证据。」「根据」等正常词后跟标点的正则固有误报。Agent 1 复核了命中行数与原始行内容，**未重做 B.3 全文人工回读**（见 §四待验证项）。
- 额外复核：禁用词与改动痕迹（融合版 / 夯 / 拉完了 / 硬规则 / 用户明确要求 / 旧版 / 本版 / 更正 / 上一版）**零命中**；审计词与状态码（#9）**零命中**。
- 相对链接 8 处全部可解析；含数据行的表格均有 GFM 分隔行。

## 三、接口与合同项

| 核查项 | 结果 |
|---|---|
| 交付状态词四词（已完成 / 依据 / 未能核实 / 待作者决定） | 齐（`SKILL.md` §8.1，四词均在成品中出现） |
| 措辞禁用（分档词、硬规则、用户明确要求、融合版） | 零命中 |
| description 写全会转去的**七个**兄弟 skill 名 | 齐：story / scene / character / fiction-planning / genre / cross-media / preset-card 全部出现在 frontmatter description |
| 路由表「需要时补读 / 缺料或冲突时的出口」两列 | 齐（`SKILL.md:125` 表头两列均在，且 §7 四行都有出口内容） |
| L-1 负触发完整示例落点 | 齐：`examples/worked-example.md:75`「例三：先判负触发」，含 A/B 分支与失败出口；`SKILL.md` §1 / §7 / §8.2 指向它 |
| L-2 EN-27 自创示范落点 | 齐：`references/en-word-choice-and-concision.md:60`「示范（自创，L-2）」 |
| 与 preset-card 双向转介（D2-A） | 齐：`SKILL.md` §10.2 / §10.3 |

## 四、阻塞清单

**本轮静态核查：实质阻塞 0 项**（未发现需退回 Agent 2 的问题，不代改任何文件）。

以下为**未验证 / 留下游**项，登记在案，**不计入「通过」**：

1. **GQ5 真实任务测试未授权** → 效果仍为 NOT_PROVEN；静态核查不等于效果已证明。
2. **W4 独立隔离回读未执行**：按 D3-C 由 Agent 1 另派只读审查子代理（不看 notes）做 GQ1–GQ4；本轮 Agent 1 自审不作独立复核，不自审自过。
3. **B.3 人工判断未由 Agent 1 重做**：附录 B 查不出的四类（例子骨架比对、标志性情节元素、借来源背书、删除后语义不通）由 Agent 2 自检，W4 独立回读时须重新逐文件核对。
4. **15 条命中的「允许」判定**依赖 Agent 2 的逐条理由；W4 复核时须确认「没有依据，按作者判断」等固定说法未被误改。
5. 分片记录 27 条决定（LI-LE-001–027）的「恢复/不恢复」语义正确性属定向精读结论，本轮只核静态可达性，不核定内容。

## 五、结论

S01 成品包**静态项齐备**：EN-34–40 均有 v0 来源、附录 B 复扫与 Agent 2 一致且零违规、状态词/禁用词/七兄弟名/两列路由/L-1/L-2 落点齐全、链接与表格格式合规。可交 W4 做独立隔离回读；**GQ5 与独立复核未做，不写「已回读」、不写验收通过**。
