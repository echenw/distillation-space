# 旧元数据与保留事项（完整迁移，不得丢弃）

## 身份（保留，不可改）
- **name**：`intrigue-revenge-craft-b04`（沿用基线，未重命名）
- **task_id**：B-07-B04
- **category**：16-类型小说专项/11-身份复仇与权谋/批次-04
- **parent_task_id**：B-07（批次 04 是**工作量切分**，不是新的语义体裁）
- **source_count**：16
- **o200k_tokens**：2,515,613
- **original_source_path**：`distill/有原始正文/16-类型小说专项/11-身份复仇与权谋`
- **source_path**：`distill/分类蒸馏/_来源批次/16-类型小说专项/11-身份复仇与权谋/批次-04`
- **workspace_path**：`distill/分类蒸馏/16-类型小说专项/11-身份复仇与权谋/批次-04`

## 基线产物（保留，不可覆盖）
基线包：`results/skills/intrigue-revenge-craft-b04/`（由 `results/manifest.yaml` 登记，`manifest_version: 1`、`revision: 1`、`owner_runtime: Main-04`、`accepted_rounds: rounds/round-01-2026-10-25/`）。

| 基线文件 | SHA-256（round-01 登记） |
|---|---|
| skills/intrigue-revenge-craft-b04/SKILL.md | 702b53b1b2d0971319a423ae178224fc2dd93031e91be0de930a4bd7e36e92a8 |
| skills/intrigue-revenge-craft-b04/references/rules.md | 983404f36c6b158c8eb40b9d6dc49c7c54c2aea8e329bd72ad13e210c3ac64d1 |
| skills/intrigue-revenge-craft-b04/references/scope-and-conflicts.md | 62edce4285d9561b9ffbb387ecdeef6282923e633a2ccc9d638c38cc2714ba79 |
| skills/intrigue-revenge-craft-b04/references/source-index.md | dbc51587fd9b9465cecaca0bb0a995d067f6b9170741bde4d49b77d95613a798 |
| skills/intrigue-revenge-craft-b04/references/techniques.md | 761fd8976b0203405f0c4195c1ee6464e091e9b90ea84db8733d1a1c400d86c3 |
| skills/intrigue-revenge-craft-b04/templates/intrigue-diagnosis.md | 3ebdc007770eafcc76d44198a51d56507c1dc256d0c3f19dc958f5848daf0838 |

基线 GQ 状态（manifest 原文）：`GQ1 PASS / GQ2 PASS(自查) / GQ3 N/A / GQ4 PASS / GQ5 NOT_PROVEN`。

## 保留的能力项（本轮未删除）
- **RM-01～RM-10**：编号、名称与适用范围全部保留；本轮只做 REVISE（RM-03 / RM-04 / RM-09 / RM-10）与 KEEP（其余）。
- **ID-01～ID-10**：诊断表十个维度全部保留。
- **C16 冲突边界**（蓄奴制辩护 vs 反奴隶制作品）：保留并强化。
- **负触发与失败出口**：保留并细化。
- **NOT_PROVEN 声明**：保留（GQ5 仍未跑）。

## 本轮的扩展（新增，不是替换）
- **RM-11 记录与证词的可改写性**：新增规则，依据 PG64359 L347-351 + PG7311 L5679-5693 / L5684-5686。
- **ID-11**：诊断表新增"记录/证词审计"行。
- **引用纪律 R-ADJ-01**：新增写入 `rules.md` 开头。
- **技法 J / K**：`techniques.md` 新增"记录与证词四问"与"污点储存"。
- **保留的冲突清单**：`scope-and-conflicts.md` 新增 6 条明确不统一的条目。

## 覆盖与许可
- 覆盖声明：16/16 来源阅读版 SHA 本轮逐字节复核一致；16/16 有 FULL 台账证据（`not_full_ids` 为空）。
- 许可：来源为 Project Gutenberg 等美国公版书；**美国公版状态不代表全球统一权利**，本包不附原著全文。
- 替代关系：本包**替代** wave4 轮 `rounds/round-p4-wave4-agent1-2026-10-30/output/intrigue-revenge-craft-b04/` 的同名 Skill（本轮在其基础上实质改写）；**不替代**基线 `results/skills/`（基线冻结只读）。
- 后续若再改：必须保留本文件的"身份"与"基线产物"两节，并在"本轮的扩展"下追加新条目，不得删除旧条目。

## 红线
不得覆盖 `results/skills/`、不得修改冻结轮次（round-01 / round-02 / round-perbook / round-p4-wave4-agent1）与原始正文。基线文件逐文件 SHA 另存于工作轮次 `notes/baseline-files.json`。
