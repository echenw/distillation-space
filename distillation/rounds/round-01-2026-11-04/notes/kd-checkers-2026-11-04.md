# D3-C 只读检查器：调用方式核对与执行记录（W1）

- 核对依据：`skills/knowledge-compiler/SKILL.md`（§5 第 5 步、§2.2）、`references/r09-checks.md`（§1、§6.2、§6.4）、以及 5 个脚本的 `argparse` 定义（只读查看）。
- **未修改 `skills/knowledge-compiler/` 任何字节**；未检出、未写仓库、未跑真实任务。
- D3=C 授权范围：允许只读 `kd_*` 检查器 + 每 skill 一个只读审查子代理（W4 另派）；**不含真实任务测试（GQ5 未授权）**；commit/push 需另行授权。

## 一、5 个只读检查器的实际调用方式

| # | 脚本 | 调用方式（已核实） | 依据 |
|---|---|---|---|
| 1 | `kd_workspace_audit.py` | `python3 kd_workspace_audit.py --workspace <工作区根目录>` （可选 `--expect-rounds N`） | SKILL.md §5 第 124 行；脚本 `argparse` 第 383–385 行。脚本 docstring 明示「No external YAML dependencies and no writes」「never rewrites historical rounds」 |
| 2 | `kd_material_quality.py` | 子命令三选一：`material --materials <dir> --dossier <dossier.json> --skill <skill-dir>`；`skill --skill <skill-dir> [--host generic\|chatgpt]`；`compare --operation create\|update --oracle <json> --manifest <json> --outputs <dir> --candidate <dir> [--baseline <dir>]` | r09-checks.md §1；脚本第 708–721 行（`compare` 另有循环生成的必填参数，**待 W4 确认，不猜**） |
| 3 | `kd_delivery_preflight.py` | `python3 kd_delivery_preflight.py --skill <skill-dir> --spec <spec.json> [--round-dir <round-dir>]` | 脚本第 403–406 行；r09-checks.md §6.4 第 5 点 |
| 4 | `kd_artifact_quality.py` | `python3 kd_artifact_quality.py --skill <dir> --brief <brief.json> --review <review.json> --evidence-root <dir> [--peers-root <dir>]` | r09-checks.md §6.2；脚本第 322–327 行 |
| 5 | `kd_round_output.py` | `python3 kd_round_output.py --root <round/output> [--expected <tree_sha256>]` | r09-checks.md §6.4 第 5 点；脚本第 132–134 行 |

脚本 1 需在 `skills/knowledge-compiler/scripts/` 目录内运行（同目录 `import kd_round_output / kd_skill_metadata`）。

## 二、本轮实际执行

**只执行了 `kd_workspace_audit`（参数明确、脚本明示只读）。**

- 命令：`python3 kd_workspace_audit.py --workspace /Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation`
- 原始输出与退出码：`notes/kd-workspace-audit-2026-11-04.txt`
- 结果：**退出码 0**，输出 `status: PASS`、`findings: []`、`rounds_total: 1`、`rounds_active: 1`、`rounds_completed: 0`、`rounds[0].status = 进行中`。
- **如实口径**：这是 advisory 静态预检（输出自身写明「does not verify actual human approval or task quality」），只说明轮次命名、状态字段、多个进行中轮次、`results/` 布局等结构无异常。**不等于验收通过、不等于 GQ1–GQ5 通过、不等于效果已证明、不认证用户授权**。`output/` 仍是 8 个空目录，本轮未完成。

## 三、其余 4 个：**调用方式待 W4 确认**

`kd_material_quality` / `kd_delivery_preflight` / `kd_artifact_quality` / `kd_round_output` 的参数形式已核实，但**本轮不跑**，原因如实记录：

- 运行所需输入产物在 W1 尚不存在：`dossier.json`（含 sources/windows/claims）、`delivery-preflight-spec.json`（含枚举模板字段）、`notes/quality/<skill>/{brief.json,review.json}`（含真实回执）、以及冻结后的完整 `output/<skill>/` 树。
- W1 `output/` 是 8 个空目录；硬跑只会得到结构拒绝或 `NOT_PROVEN`，**不能写成通过**，也不拿它冒充验收。
- 按 §6.1 轮次表与 P5，这 4 个在 **W4 收口**由执行组在真实产物齐备后执行；`kd_material_quality.py compare` 的其余必填参数、`kd_artifact_quality.py --peers-root` 的实际取值，届时按脚本与 `references/` 核定，**不猜参数、不伪造通过**。
- P4 独立回读按 D3-C 由 Agent 1 在 W4 另派只读审查子代理（每个 skill 一个，只看成品包、不看 notes）；Agent 1 只汇总与出门禁，不自审自过。

## 四、红线遵守

- 未写 `skills/` 下任何正式文件；未动 `skills/knowledge-compiler/` 任何字节。
- 未运行真实任务测试（GQ5 未授权）；未 commit / push / reset / checkout / clean / add。
- 未把未验证项写成通过；`kd_workspace_audit` 的 PASS 仅按 advisory 静态预检如实报告。
