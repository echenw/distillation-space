# 版本、来源账与许可（元数据，迁移时须完整保留）

## 身份

| 字段 | 值 |
|---|---|
| skill_id / name | `sci-fi-novum-world-forge` |
| 任务 ID | `A-06-B02` |
| 类别 | `16-类型小说专项/05-科幻未来/批次-02` |
| Owner | Main A（owner_queue_position 6，subtask_order 2，parent_task_id `A-06`） |
| kind | **new**（本任务工作区此前无 `output/`、无 `results/`、无 `skill.zip`，无可继承 Skill） |
| 本轮 | `rounds/round-p4-final-2026-10-30` |
| 生成日期 | 2026-10-30 |

## 来源账

| 项 | 值 |
|---|---|
| 来源总数 | **28** |
| 已 FULL（可回源台账覆盖） | **28 / 28**，缺口行数 0 |
| o200k tokens | 1,160,354 |
| SHA-256 核验 | 28/28 与 `批次来源清单.json` 的 `sha256_reading` 逐本一致 |
| 年代范围 | 1826–1963 |
| 来源性质 | 全部为虚构/论说体小说作品，**无写作教材、无作者自述** |
| 知识角色汇总 | 支持 22 / 补充 4 / 反例 7 / 冲突 3 组 / 不适用 1 / 未证明 0 |

## 证据链

1. 权威任务记录：`docs/plans/分类独立知识蒸馏计划/任务清单.json`（`task_id == "A-06-B02"`）
2. 来源视图清单：`distill/分类蒸馏/_来源批次/16-类型小说专项/05-科幻未来/批次-02/批次来源清单.json`
3. 缺口派发明细：`docs/plans/分类独立知识蒸馏计划/workflow20-20261030/start-state.json`（本任务 `not_full=2`、`remaining_lines=15577`、`not_full_ids=[PG1013,PG1906]`）
4. 覆盖核账：本轮 `notes/source-coverage.md`
5. 融合与裁决：本轮 `notes/source-synthesis.md`
6. 阅读台账：各历史轮次 `rounds/*/notes/reading/ledger-PG*.md`（33 份，门禁全 PASS）＋本轮 `notes/reading/` 2 份（PASS）
7. 门禁工具：`distill/_tools/kd32_ledger_gate.py`（引文回源 ±3 行核验）、`distill/_tools/kd32_p4_check.py`（P4 结构核验）

## 版本与替代关系

- 本 Skill **不替代**同题材兄弟批次的 Skill：批次-01 `sci-fi-future-plot-forge`、批次-04 `science-fiction-craft-b04`、批次-05 `science-fiction-conceptual-reveal`。三者来源与本任务 28 本**互不重叠**，规则不得互相套用。
- 本 Skill 与批次-01 的关系已在 `references/rule-adjudication.md` A 类逐条裁决：A6／A7／A8 之外均被 REVISE 或 REJECT，其中 A8（六域划分）明确 REJECT。
- 元规则：单部作品的情节设计不得升级为题材定律（见 `references/failure-exit.md` §4）。

## 许可与版权

- 28 份来源均为 Project Gutenberg 公共领域文本（书目元数据见各 PG 目录的 `书籍信息.json` 与 `原著来源.url`）。
- 台账中逐字引文均为短片段引用，用于回源核验，附精确行号。
- 本 Skill 本身可自由复制与修改；修改时**必须保留本文件全部字段**，并在新版本中记录前版 SHA。

## 打包与哈希

本文件自身参与 skill 树的哈希，故**不在此处自记 skill 树 SHA**（自记会改变自身哈希，形成自引用）。
权威哈希记录在**本文件之外**、不参与该哈希的两处：

- 本轮 `notes/skill-closure.json` 的 `skill_sha` / `skill_tree_sha256` / `skill_md_sha256` / `zip_sha256`；
- 本轮 `checklist.md` 的「回执与打包」小节。

打包事实（固定值，不随本文件变化）：

| 项 | 值 |
|---|---|
| zip 内条目 | 25（19 个非目录文件 + 目录项） |
| 逐文件回读 | 18/18 与磁盘逐字节一致（`notes/skill-closure.json` 为自引用文件，按约定跳过比对） |
| 打包命令 | `zip -qr skill.zip output notes checklist.md`（在本轮目录下执行） |

自引用说明：`skill.zip` 内含 `notes/skill-closure.json`，而该回执记录 zip 自身的 SHA，二者不可能逐字节自洽。磁盘版回执（权威版）记录交付 zip 的真实 SHA；zip 内副本记录上一轮打包值。详见 `checklist.md`。

## 完成度与未决项

- **P4 收口**：已完成（结构、引用、元数据、打包）；`kd32_p4_check.py` 返回 `ok=true / P4_SKILL_CLOSED / problems=[]`。
- **P5**：GQ1–GQ5 与真实宿主行为测试 **NOT_PROVEN**（本轮未执行，不阻断 P4 收口，按 2026-10-30 用户决定"到 P4 则视为 Skill 收口"）。
- **P6 冻结**：未执行。
- **P7 `results/` 采纳**：未执行，本轮不预写 `results/`。
- 已知目录异常（只读记录，未修改）：`05-科幻未来/批次 -02/`（目录名含空格）下另有 PG1013、PG1906 的 full 台账，门禁亦 PASS；该目录不在任务清单的 `workspace_path` 内，本轮不采信为本任务证据。
