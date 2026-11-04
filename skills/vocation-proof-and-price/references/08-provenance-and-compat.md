# 08 来源沿革、跨批次兼容与未证明项

## 本 Skill 的沿革

- **本批次（B-06-B03）此前没有 Skill**。本轮在 `rounds/round-p4-final-2026-10-30` 从零建立，因此 `kind = new`。
- 复用的历史成果（只读，未修改）：
  - `round-kd32-r01/notes/reading/`（PG2366 / PG2460 / PG25086）
  - `round-kd32-r02/notes/reading/`（PG19343）
  - `round-perbook/notes/reading/`（15 本）
  - `round-shard-dfm/notes/reading/`（PG401 / PG2725 / PG3364 / PG5764）
  - 23 份台账本轮全部重跑 `kd32_ledger_gate.py`，全部 PASS。
- 未采用的历史产物：无（本批次无历史 Skill、无历史 ZIP、无历史收口回执）。

## 与同父类别另两份 Skill 的关系

| Skill | 任务 | 负责 | 与本 Skill 的关系 |
|---|---|---|---|
| `profession-competition-craft` | B-06-B01（批次-01） | 职业引擎强度 A/B/C 定轴 + 12 条失败模式 F1–F12 | **正交**。本 Skill 的 P/L/E 与 A/B/C 可同时判定（如"A 档 + P 轴"）。本 Skill 对其裁决见 `02-rulings.md` |
| `competition-underdog-arc` | B-06-B02（批次-02） | 逆袭弧 R1–R11（劣势账本、规则性失败、有代价结局） | **部分重叠**。逆袭弧可视为 P 轴的一个子类；本 Skill 不重复其六场景骨架，只在 R2/R4/R7/R8 处给出裁决 |

**本 Skill 不复核上两者所用来源**（不在本批 23 本内）。若用户已在用上两者，不要互相推翻；按 `02-rulings.md` 的裁决处理分歧：REVISE 与 REJECT 的 8 条以本批证据为准，KEEP 的 9 条沿用。

## 元数据（必须随 Skill 一起迁移，不得丢弃）

```
skill_id: vocation-proof-and-price
task_id: B-06-B03
category: 16-类型小说专项/09-职业与竞技/批次-03
parent_category: 16-类型小说专项/09-职业与竞技
source_count: 23
sources_full: 23
sources_not_full: 0
independent_source_families: 20   # Henry James 3 本并 1 族；Howells 2 本并 1 族
corpus_years: 1833-1958
material_role: FICTION_CASE（23/23，见各书 书籍信息.json）
runtime_tests: NOT_PROVEN
license: 内部蒸馏产物，仅在本仓库使用
supersedes: []
superseded_by: []
```

## 未证明 / 已知缺口（如实登记，不得随版本流失）

1. **runtime / 读者效果 NOT_PROVEN** —— 无真实作者任务、无宿主运行、无独立评审、无读者数据。所有"这样写更好"都是 H。
2. **跨批次来源未复核** —— 批次-01 / 批次-02 的 PG 来源不在本批，其 F 未被本轮回源。
3. **PG19343 / PG25086 证据密度低** —— 台账门禁通过但要点较简；其 F 一律 `SINGLE_SOURCE`，不承担规则推翻。
4. **PG25086 的幻想装置不参与归纳** —— 金星代表设定属科幻装置。
5. **NOT_PROVEN 规则 2 条**：R17（守门人是失败者）、R18（战地记者技能清单）——均为角色论断/讽刺修辞，只作写法样本。
6. **当代职业语料为零** —— 全样本 1833–1958，命中当代平台劳动即走出口 X4。
7. **P5–P7 未完成**：本轮按 2026-10-30 用户决定"到 P4 则视为 Skill 收口"，GQ1–GQ5、正式冻结、`results/` 采纳仍记 NOT_PROVEN / 未做，不从 P4 推断已上线或宿主已验证。
