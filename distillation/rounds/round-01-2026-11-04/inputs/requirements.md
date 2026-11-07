# 小说 Skill 完善计划 · 项目总需求

- 依据：`docs/plans/novel-skill-improvement-plan.md`（基线 `main@c734510`）
- 日期：2026-11-04
- 性质：跨轮继承的**项目总需求**。只记跨轮目的、产物、范围、验收与长期约束；当轮执行方式记在 `rounds/round-01-2026-11-04/checklist.md`。
- 状态：第 9 节 D1–D5 已由用户裁决并授权执行（见下）。

## 一、七问（knowledge-compiler 第 1 步）

### ① 学习目标
找回 v0–v2 迭代中丢掉的写作知识，并使 `skills/` 下 8 个小说 skill 满足 knowledge-compiler 对成品 Skill 的要求（R18 §1–4、§2a–2d，R09 §3、§6 的 GQ1–GQ4，R17 §4a，SKILL.md §3）。`skills/knowledge-compiler` 本身不改。

重点是反例、失败出口、适用条件、模板字段和机制卡。

### ② 产物与位置
8 个完整 Skill（名称不变）：

1. character-and-narrative-control
2. cross-media-drama-adaptation
3. fiction-planning-and-diagnosis
4. genre-fiction-craft
5. line-editing-and-proofreading
6. preset-card-generation
7. scene-conflict-and-rhythm
8. story-architecture-and-longform-planning

工作稿在 `distillation/rounds/round-01-2026-11-04/output/<skill>/`；冻结后按 **D1=A** 应用到 `skills/`。**不建 `distillation/results/` 副本**，当前成果只认仓库里的 `skills/`。来源信息只放在 `notes/`。

### ③ 材料、限制、隐私
- 材料（只读，用 `git show <提交>:<路径>`，不检出、不改仓库）：
  - v0 `d23c461`（74 个独立 skill，路径 `skills/<name>/...`）
  - v1 `d2003e4`（合并成 7 个 skill）
  - v2 `3c1cb5f`（7 个 skill）
  - 基线 v3 `2a10c07`（7 个 skill）
  - preset-card `d57fd12`（加入 preset-card-generation）
  - knowledge-compiler `c734510`（加入编译器，作为成品规范依据）
- 线索：`~/knowledge-distillation-workspace/results/notes/three-version-audit-20261102.md`（11-02 三版审计），只当线索，不当证据。
- 限制：v0 本身含重复内容与来源文件；缩减幅度只是盘点信号，**不是应恢复的量**，须按 P1「以下情况不算丢失」的三类逐条排除。
- 隐私：材料里没有密钥和个人隐私；书名、作者、引文、来源编号、年代、篇数只能进 `notes/`，成品一律不提。

### ④ 覆盖与方式（**D4=A**）
专项修订。机械盘点全量覆盖，精读只做定向的；genre 的深度按 **D4=A**：

> **14 类全部机械盘点 + 定向精读，热门三类与 v0 全文对照。**

- 14 类题材：`genre-fiction-craft/references/01–14` 全部纳入 K1 机械盘点与 P1 定向精读。
- 热门三类与 v0 全文对照：按 P3 第 8 条与 §6.1，指 **04 武侠仙侠玄幻、02 言情（含 RO-K121–166）、05 科幻（机制卡）** 三类，做与 v0 的全文对照。
- 阈值：默认缩减超过 30% 或超过 1.5 KB；**genre 01 推理、07 求生灾变、10 职业竞技收紧到 20%**（第 5.1 节、附录 A.1）。
- 编号改号不算丢失，按 2.3 节用「新旧前缀 + 标题」对齐，不比编号：`AC-01–18→A1–C3`、`SV-T→SD-T`、`PD/PT→PS/PV`、`IDP→IR`、`COM→CO`、`RM/RD→RL`。
- 分片：v0 精读量每片约 100 KB 以内；超过 300 KB 的谱系组按 v0 skill 再切片（附录 F）。

### ⑤ 完成标准
本计划第 7 节九条；**不更新 `distillation/results/`**。

补充（D3-C / GQ5）：本轮为静态交付，GQ5 无真实任务测试时记 `NOT_PROVEN`，静态通过不写成效果已证明；不把未验证项写成通过。

### ⑥ 允许的操作（**D3=C**）
- 读仓库和 git 历史；写 `distillation/`；在 `scratchpad/` 跑只读统计脚本；按 D1 在冻结后写 `skills/`。
- **D3=C = 在 D3-B 基础上**：允许运行 knowledge-compiler 的**只读** `kd_*` 检查器（`kd_material_quality`、`kd_delivery_preflight`、`kd_artifact_quality`、`kd_round_output`、`kd_workspace_audit`），且**每个 skill 派一个只读审查子代理**，只看成品包、不看 notes，做隔离回读和 GQ1–GQ4（由 Agent 1 在 W4 另派，Agent 1 只汇总与出门禁，不自审自过）。
- **不运行真实任务测试（GQ5 未授权）**；不运行任何写操作的脚本。
- **commit / push 仍需另行授权**，本轮一律不执行；同时禁止 `git reset` / `checkout` / `clean` / `add` / `commit` / `push`，不删除任何既有文件，不修改有未提交修订的计划文档。
- `skills/knowledge-compiler/` 任何字节都不改。

### ⑦ 学习深度
标准。审计已列的条目、热门三类题材、v2→v3 被连带删除的规则体（如 SU-02），按严格处理；材料没有依据的地方写「没有依据，按作者判断」，不编造阈值、数字或成体系的反例。

## 二、用户裁决（第 9 节，已裁决并授权执行）

| # | 决策 | 裁决 | 落地口径 |
|---|---|---|---|
| D1 | 工作区与落地 | **A** | `distillation/` 工作区，冻结后应用到 `skills/`，不建 `results/` 副本 |
| D2 | preset-card-generation 边界 | **A** | 保留「推进 / 文风 / 表达」三轴全流程，但只负责预设卡和三轴诊断；一般规划、结构、精修转兄弟 skill，兄弟 skill 遇卡片请求转回它，**双向转介** |
| D3 | 验证授权 | **C** | 只读 `kd_*` 检查器 + 每 skill 一个只读审查子代理（隔离回读、GQ1–GQ4）；**不含**真实任务测试（GQ5 未授权）；commit/push 需另行授权 |
| D4 | genre 覆盖深度 | **A** | 14 类全部机械盘点 + 定向精修，热门三类与 v0 全文对照（见 ④） |
| D5 | 附录 H 写作建议 | **A** | 纳入本轮。与材料同义的合并进现有规则并补条件；材料没有的作为新规则写入；与材料冲突的列给用户裁决。按 H.18 的「skill + 建议编号 1–72」映射分配，不按 H.x 章节切 |

D2 的 Owner 与转介矩阵、D3 的审查子代理安排、D5 的 H.18 映射与共用项裁决，均在 `notes/suite-contract.md`（K2 定稿）与 §6.1 派发表中约束；**D5 已采纳，附录 H 是本轮正式任务**。

## 三、长期约束（跨轮继承，写入本 requirements）

1. **成品不提来源**：不出现书名、作者、作品人物 / 情节 / 设定、原句、来源编号、年代、篇数，也不出现别人的项目、仓库链接和包外路径。
2. **例子一律自创、通用**；自创例子须与 v0 来源案例比情节骨架（人物关系 + 关键事件 + 设定），相近就重写。
3. **不改 `skills/knowledge-compiler/`**，字节与 `c734510` 相同。
4. **不把有意的口径调整当成丢失**（也不把后版已改正的事实错误、只属于某一部作品的情节和史实当成丢失恢复回来）。
