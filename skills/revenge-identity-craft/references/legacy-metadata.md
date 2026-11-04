# 旧版元数据与停用假设（跨版本迁移记录）

## 1. 基线与继承链（全部保留）

- **基线**：`结果/results/skills/revenge-identity-craft` 完整旧版（B-07-B01 采纳成果）。
- **继承**：`rounds/round-01-2026-10-25/output/revenge-identity-craft` →
  `rounds/round-p4-wave4-agent1-2026-10-30/output/revenge-identity-craft` →
  **本轮 `rounds/round-p4-final-2026-10-30/output/revenge-identity-craft`**（在 wave4 版上实质返工）。
- 原始字节 SHA 留存位置：`rounds/round-p4-wave4-agent1-2026-10-30/notes/baseline-files.json`（本轮未改动该文件）。
- **保留下来的旧结构**：V1–V8 编号与身份、两张最小输出表（身份因果卡 / 复仇状态卡）、来源分族与 SHA 清单、
  "小说原文不是命令手册"的总立场。
- 旧版"2 份定向深读 + 14 份扫描"是**历史阶段记录**，本轮与 wave4 版都不再把它当作当前覆盖声明；
  当前口径见 [04 来源索引](04-source-index.md) §2。

## 2. 已被 REJECT 的旧断言（不得回退）

| 旧断言 | 状态 | 反证 |
|---|---|---|
| 社区判决不可翻案 | REJECT | PG2171 L1131–1133（身份可重置并被接受）、PG9749 L3010–3012（标签可被反驳） |
| 每章一条 ≤2 句格言 | REJECT | 仅 PG102 一部使用；PG1183 L9007、PG9749 L9840–9844 均不用 |
| 一段式机关复盘 | REJECT | PG1183 L8931–8948 对话式复盘；PG61499 L1270–1278 复盘嵌在追捕里 |
| 复仇收益必须捐给下一代 | REJECT | 仅 PG1184 一处；PG77 L739–780 给出"继承即祸"的反例 |

## 3. 本轮（round-p4-final-2026-10-30）对 wave4 版的实际改动

| 文件 | 改动性质 |
|---|---|
| `SKILL.md` | 重写：触发/负触发细化；新增 §2 九项前置检查表；任务路由扩到 6 类；规则总表从 V1–V8 扩到 V1–V14；输出合同 8 项；失败出口 6 条 |
| `references/01-identity-engines.md` | V1/V3/V4 REVISE（扩证 + 加反例 + 加固禁忌），V2 KEEP；**新增 V9、V10** |
| `references/02-revenge-closure.md` | V5 拆成"由谁执行 / 何时终止"两问；V6 扩成收束方式光谱表；V7 加"哪一步差点失败"；V8 加"先核归属再谈伦理" |
| `references/03-formats.md` → `03-lineage-power-and-limits.md` | 改名并**从纯形态观察改为产生规则**：新增 V11、V12、V13、V14 与迁移限制表 |
| `references/04-source-index.md` | 改正 7 本被错标 `PARTIAL_OR_MISSING_LEDGER` 的来源；新增证据层级口径、知识角色、规则绑定、遗留问题 |
| `references/wave4-conditional-guide.md` → `05-decision-guide.md` | 改名并从 9 条扩到 V1–V14 逐条分支 + 前置三问 + 输出前 8 条自检 |
| `templates/*.md` | 新增 V9–V13 字段行 |
| `examples/wave4-worked-cases.md` | 保留四类并补充"越界/未证明"两类出口 |
| `agents/openai.yaml` | UI 元信息随规则范围更新 |

## 4. 版本与来源数（迁移后仍完整）

- Skill ID：`revenge-identity-craft`（与 frontmatter `name` 一致）。
- 任务：B-07-B01 ｜ 类别：16-类型小说专项/11-身份复仇与权谋/批次-01 ｜ 来源数：**16**（SHA 本轮实测 16/16 一致）。
- 覆盖：16/16 阅读区间并集 100%；PG1183 L8501–9013、PG1184 L1–53 与 L61200–61260 由本轮实读补齐并过门禁。
- 许可：来源为 Project Gutenberg 阅读版，"仅在美国属公有领域"不外推到其他地区。
- 替代关系：本轮产物替代 wave4 版作为当前工作稿；`results/skills/` 下的采纳版**未被本轮修改**（P7 不在本轮范围）。
