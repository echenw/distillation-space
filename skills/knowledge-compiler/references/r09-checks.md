# R09 — 检查材料与候选 Skill

这些只读检查核对三样东西：材料的来源记录、完整的 Skill 目录、实际任务的对照记录。检查通过只说明结构符合要求；理解是否正确、Skill 是否有帮助，仍要靠独立任务和可靠的运行证据。

## 1. 三个检查命令

```bash
python3 <SkillRoot>/scripts/kd_material_quality.py material --materials /safe/batch --dossier /safe/dossier.json --skill /safe/new-skill
python3 <SkillRoot>/scripts/kd_material_quality.py skill --skill /safe/new-skill --host generic
python3 <SkillRoot>/scripts/kd_material_quality.py compare --operation create --oracle /frozen/oracle.json --manifest /frozen/results.json --outputs /frozen/observations --candidate /safe/new-skill
```

- **material** 核对版本 2 的来源关联、内容摘要、声明的阅读范围和中间 dossier 中每条主张（Claim）的证据和成品锚点关联。成功返回 `STRUCTURE_VALID_SEMANTICS_UNPROVEN`，不证明实际读过、原件身份或归纳正确。版本 1 缺来源关联，返回 `DOSSIER_V1_LINEAGE_NOT_PROVEN`。
- **skill** 检查完整目录、入口元数据（frontmatter）、内部引用、Python 语法和目录摘要；`--host chatgpt` 另外核对 `agents/openai.yaml` 的 interface 字符串。成功返回 `STATIC_STRUCTURE_VALID`，不证明触发和运行效果。
- **compare** 检查调用方提交的任务对照结果。新建（`create`）比较 none 和 candidate 两组；更新改用 `--operation update` 并加 `--baseline /safe/old-skill`，比较 none、baseline 和 candidate 三组。即使结构通过，fixture 仍标为 `SIMULATION_ONLY`，host_reported 仍标为 `HOST_REPORTED_UNAUTHENTICATED`，不能代替可信宿主的验收、G1 或 S16。

输入必须是严格的 JSON：拒绝重复键、无效 UTF-8、非有限数和过深的嵌套；`version` 必须是对应的整数，布尔值和浮点数不算。失败时不回显不可信的原文。归一化、隐私和来源关联的约定只在 R03 §1 维护。

## 2. 材料与主张清单 `dossier.json`

内容摘要、行号和引文都用实际文件计算，不要猜。dossier 是中间证据，只保存在本轮 `notes/` 等成品目录之外；最终 Skill 不放引用、来源索引或出处标记（R18 §2b）。

```json
{
  "version": 2,
  "sources": [
    {"id": "SRC1", "path": "source.txt", "sha256": "<sha256>", "lines": 8, "lineage": {"kind": "direct"}, "material_id": "M1"},
    {"id": "SRC2", "path": "logs/task.txt", "sha256": "<sha256>", "lines": 14, "lineage": {"kind": "direct"}, "material_id": "M2"}
  ],
  "windows": [
    {"source_id": "SRC1", "start": 1, "end": 8, "sha256": "<第 1–8 行连同换行符拼接后的 sha256>"},
    {"source_id": "SRC2", "start": 1, "end": 14, "sha256": "<同样的算法>"}
  ],
  "claims": [{
    "id": "RULE1",
    "assertion": "Check the actual tool result before retrying",
    "skill_path": "references/checks.md",
    "skill_anchor": "Check the actual tool result before retrying",
    "applicability": "Only after a transient failure",
    "limitations": "Never retry irreversible operations",
    "evidence": [{"source_id": "SRC2", "start": 9, "end": 9, "quote": "<原文>", "quote_sha256": "<原文 UTF-8 的 sha256>"}]
  }],
  "conflicts": [{"source_ids": ["SRC1", "SRC2"], "status": "VERSIONED", "reason": "Different releases"}]
}
```

- `sources` 覆盖 `--materials` 指定的受检文本文件，`lineage` 必填。不要传入含 `manifest.yaml` 和总需求的整个工作区，只提交有出处的原文或规范化文本；整理后的 `batch.md` 不算独立原件。`direct` 只表示没转换过的一手文本；`normalized` 的一个文件对应 R03 的一个归一化单元，按原字节保存正文并原样保留 lineage，不能用摘要或拼接冒充。原件身份仍由可信宿主核验。
- 单个来源不超过 8 MiB，总量不超过 32 MiB；超出的分批并记录缺口，不悄悄截断。`windows` 按行的并集算覆盖范围。缺来源、摘要漂移、窗口不符或有没覆盖的行，都会阻断完整批次。
- 归一化版本、提取器版本、原件和输出的 SHA、锚点的约定见 R03 §1。旧版本、未知的提取器版本和坏锚点会被拒绝；同一原件 SHA 加同一 `source_anchor` 不能声明多次，同一来源的不同单元不自动算独立事实。
- 行覆盖、`windows` 与 `lineage` 的 PASS 只检查已提交的文本单元，不能消除 normalization 报告中的 PDF 无文本页缺口，也不能证明全文读完。宿主须按 R03 §1.1、§1.5 保留报告、原件 SHA 和原始页观察，将未解决的缺口带入 scope review；不能制造空单元、假行号或缺失文件来补分母。
- 用 `kd_incremental.py` 做增量对照时，每个来源要有 `material_id`，并把 direct 的 SHA 或 normalized 的原件 SHA 绑定到旧的任务快照（见 R03 §5）；单独运行本检查时这个字段可选。
- 每条 claim 在 dossier 保留 `assertion`、`applicability`、`limitations`、准确的 `evidence`（源行、原文和引文摘要）以及 `skill_path`、`skill_anchor`。`skill_path` 指向成品内真实文件，`skill_anchor` 必须在该文件中唯一出现并包含完整的 `assertion`，不能只指向代码示例。成品不再嵌入映射标记；缺失、重复、错位或越界的关联都拒绝，同一目标不能用不同 claim ID 重复登记。映射对得上不保证语义正确，未登记规范和危险泛化仍要独立审查。
- `conflicts` 至少引用两个不同的已声明来源，`status` 只接受 UNRESOLVED、RESOLVED、VERSIONED。UNRESOLVED 会阻断完整批次；其他状态只保留裁决或版本差异，不授予正式批准。同一任务的摘录、模型重写和不同的来源编号都不增加独立支持。

## 3. 检查完整 Skill 的结构

候选放在独立的暂存目录，原 Skill 保留作基线。每轮最终产物仍应按 R06 §5.1 完整保存到该轮 `output/`；结构检查并不会冻结它，也不会把候选自动合入 `results/`。目标源文件的维护按 R06 §5 的授权执行；结构检查不授予个人安装目录、正式记录或展示文件的写权限。`skill` 只读校验，不运行候选脚本。Skill 的摘要绑定全部受控路径和字节，任何文件一变，旧的效果结果就不能复用。

代码块、缩进代码、行内代码和转义链接不算安装依赖或实际主张；正文里的直接链接和引用式链接（含图片）必须有效。脚本只支持确定的语法子集，复杂的 Markdown 和 YAML 仍要人工核查。frontmatter 的 `name`、`description`、其他允许的平面字段，以及 ChatGPT interface 字段使用非空、可打印的单行字符串：引号要闭合，冒号后要有空白，以数字、日期、保留词或符号开头的值要加引号。frontmatter 的 `metadata` 另外支持单层字符串映射，键必须唯一，值同样须是非空、可打印的单行字符串；数组、更深层的对象及其他复杂 YAML 仍不在支持范围内。结构检查与正式发布共用 `kd_skill_metadata.py` 的 frontmatter 契约，必需 `name` 和非空 `description`，允许额外的唯一平面字符串字段、空行和注释；不设入口行数上限或描述最小字符数。字段被接受不代表宿主会消费该字段。文件数、单文件和总字节的资源保护仍然有效。

静态检查通过不能说成 Codex 或 Claude 会自动触发，也不能说成提炼有效。**逐项对照总需求能力清单**：外貌/性格/成长等条款若被合并、更名或移除，要写明确对应和授权；不能靠“14 项仍有 14 个编号”假装未改变需求。**若正文承诺 Schema 校验、确定性 Lint、指纹引擎或自动状态管理，必须核查交付内是否实际有对应脚本/Schema、公开调用方式与运行证据**；仅引用上游实现或在 Markdown 写流程不得宣称“已实现自动检查”，只能说明“人工/Agent 按规则执行”。**最终 Skill 入口和 references 只保留运行所需规则，不把 R09/R10 返工勾销、内部 Agent 分工、未决施工备忘作为正式使用指令**；这些材料留在同轮 `notes/` 与审查报告。实际执行的证明要在获准、隔离的 Agent 环境里独立完成，并保留版本、任务、实际结果和可信日志。

## 4. 独立对照的要求

先冻结评判标准（oracle），生成候选的一方不能读取保留的答案。新建时以“实际不加载 Skill”为对照，不造同名旧 Skill 或空目录。更新时固定旧 Skill 和候选的完整目录，旧基线必须含 SKILL.md。命令行默认 `update`，省略旧路径会被拒绝；`operation` 必须和结果记录一致。

```json
{"version":1,"cases":[
  {"id":"C1","kind":"positive","should_trigger":true,"expected_stdout":"OK\n","expected_exit":0},
  {"id":"C2","kind":"negative","should_trigger":false,"expected_stdout":"NOOP\n","expected_exit":0},
  {"id":"C3","kind":"boundary","should_trigger":true,"expected_stdout":"SAFE\n","expected_exit":0},
  {"id":"C4","kind":"safety","should_trigger":true,"expected_stdout":"REJECT\n","expected_exit":0}
]}
```

- results 和 oracle 的 `version` 都是整数 1，只有 dossier 是 2。results 必填 `oracle_sha256`、`candidate_tree_sha256`、`mode`、`environment` 和 `runs`。`create` 填 `operation:create` 和 `baseline_tree_sha256:null`，每个案例两组；`update` 填 `operation:update` 和真实的 `baseline_tree_sha256`，每个案例三组。没带 `operation` 的旧记录只按 update 解释。
- 每条 run 有 `case_id`、`arm`、stdout 的相对路径和摘要、整数 `exit_code`、`skill_invoked`、`duration_ms` 和相同的 `environment`。none 组必须没有调用 Skill，其他组按 `should_trigger` 核对。每个案例每组恰好一条记录，缺失、重复或多出的组都被拒绝。
- 产物可以用 `expected_files:[{path,sha256}]` 核对，这时 `expected_stdout` 可以是 null，每条 run 要提供 `artifact_dir`，细节见 R03 §5。有多种合理答案时，由独立冻结的判定器先生成可核对的回执，不能由候选自己打分。
- PASS 的条件：候选通过的案例数**严格超过每个对照组**（新建超过 none，更新超过 none 和 baseline），对照组已通过的案例没有一个退步，negative 和 safety 全部通过。和不加载 Skill 持平只说明没有证明新增价值；比不加载 Skill 差时，不能靠“比旧版好”过关。
- 报告分别给出 `regressions_vs_none`、`regressions_vs_baseline` 和计数，它们不是统计显著性，也不是正式评测。有随机性的真实收益另按 R11 和 R03 固定评分方法、最小改进量、重复次数和容差；这个只读对照器不授予 verified。

## 5. 实际执行与效果证明

证明 Skill 的效果需要实际运行的授权。只做整理或静态修订的任务按 R06 §4–6 交付，并注明效果未验证。完整的验证顺序：锁定材料 → 整理和提炼 → 写 dossier 和主张 → `material` → `skill` → 独立的真实任务观测 → 两组或三组 `compare` → 复核冲突、语义和遗漏 → 按授权修改源文件，或申请正式的 G1 和 S12。

仓库里的离线测试只证明结构链和拒绝能力，不包含真实的模型生成，不能当作 Codex 或 Claude 的实际行为。学习和提炼的效果证明仍需要相同的输入、实际宿主的产物、独立冻结的判据和可信的审查。所有辅助 JSON 都留在任务记录里，不是生产授权的凭据。

## 6. 成品 Skill 质量门禁 GQ1–GQ5（交付前，不替代独立审查）

§1–5 的静态检查和离线对照不能推出「生成的 Skill 自洽、能力已实现或已经可以上线」。**本节针对新建/修订 Skill 的最终交付**，不要求只产生短笔记或 Rule 的任务假造 Skill。审查对象是最终待冻结的 `output/<真实-skill-id>/`（或获准的等价候选目录），**不是材料摘录、上游源码或早期 v1 草稿**。若本轮约定仅为静态交付，可在该约定达到后完成并冻结静态草稿；GQ5 和其他欠缺证据的项继续 `NOT_PROVEN`，不得据此宣称全面合格或上线。

| 门禁 | 应审查的实际行为与阻断条件 |
|---|---|
| **GQ1 功能真实性** | 从用户总需求与最终入口声明逐项列能力 ID，对应实际工作流或随包实现与验证结果。复杂任务不能因在表格里列出ID、输入/输出就判深度合格：逐项核对可区分分支、反证/排除条件、修后复验与所指向的真实reference（R18 §2d）；只读结构通过不等于专业质量通过。区分 `workflow`（Agent/人工执行）、`automation`（包内真实脚本/Schema）与 `external`（外部依赖）。声称确定性 Lint、Schema 校验或自动状态引擎却只有 Markdown / 上游源码：**FAIL**；缺证据不能写 PASS。合并、增删需求维度须有可核对映射与用户决定。 |
| **GQ2 语义自洽** | 独立逐节检查 SKILL.md、所有 Reference 和模板的跨文件规则，逐组登记原文 A/B、实际冲突或解释、反例及复验；例如新建人物允许声口待定 vs 正文审查要求三条真实台词。枚举要求在reference写满但最终填写模板合为一行，不算逐项可用，按R18 §2a核对字段可填、缺省与版本/当前任务证据定位（相关时）。仅有修复单「已勾销」而最终行为未复验：**NOT_PROVEN**。静态关键词或哈希无法判定语义真伪。 |
| **GQ3 跨 Skill 接口** | 同时使用多个 Skill 时，核实 Owner、provider/consumer、数据字段/类型/版本/路径、缺字段分支、仲裁和双方实际引用；绑定两份 Skill 的当前树 SHA。没有提供方接口却让消费方依赖其 Registry 或状态引擎，不能 PASS；无跨 Skill 依赖则明示空接口并独立检查有无遗漏。 |
| **GQ4 适用性与反例** | 每个重要规则或阈值记录材料来源、目标适用范围、限制、反例和采纳/改写理由。按R17 §4a将跨来源笔记中的关键区分性条件与反例反向定位到最终消费者规则，笔记里的出处记录只有作者/书名/摘要但操作细则缺失时不得按“已融合”判完整。来源驱动的关键规则，来源身份、位置与适用决策记在本轮 notes/ 供审查回查；最终包内的规则要自带适用条件，不提来源，不出现别人的项目和作品，读者不必回查出处就能用（R18 §2b；有一处不合格即 GQ4 不通过）。记忆半衰期、节奏百分比、固定字数等不得不分宿主/题材机械升级为全局硬门。原项目存在该规则不等于本 Skill 必须照搬。 |
| **GQ5 最终版真实任务** | 用同一份最终版 Skill 至少覆盖**正常、缺失信息、规则冲突、边界输入**四类任务，记输入、宿主、实际输出与独立判定。需要证明价值时仍按 §4–5 比较 none / candidate（更新另加 baseline）；失败后在同 Round 返工，**重跑最终树 SHA 对应的失败案例**。不能用 v1 通过记录、模型自评或「勾销」代替最终版验收。 |

**消费者操作补查：** 可按 [R18 §4](r18-consumer-operations.md) 在本轮 notes/ 中记录误触发、缺料、冲突、权限、输入格式和真实依赖的检查结果，并逐项回读 R18 §2a 的模板与 §2b 的成品自足要求；有明确枚举清单时可用 `scripts/kd_delivery_preflight.py` 静态辅助，但不能验证原著解释正确。此补查属于现有GQ1–GQ4，不新增 GQ6。未经真实宿主运行，GQ5 仍为 `NOT_PROVEN`；素材中的 README 指令、YAML 路由不等于自动执行。

### 6.1 冻结 brief、独立 review 与证据

1. 在当前轮 `notes/quality/brief.json` 固定 version 1 的 `requirements`、`capabilities`、`interfaces`、`applicability`、`cases` 数组，每项用唯一 ID。brief 必须根据**已确认的真实总需求和最终 Skill 承诺**完整盘点，先于质量审查固定，不能删掉难实现的需求来制造全绿。`cases` 至少含 `positive/missing/conflict/boundary` 四种，不只是四个顺利案例。外部依赖和无法自动化的步骤不可伪装成已经实现的脚本。
2. 在独立 `notes/quality/review.json` 保存 version 1、实际 `brief_sha256`、`skill_tree_sha256`、`producer`、`reviewer` 和同 ID 五组结论，以及至少一组 `semantics` 不同位置的真实交叉对照。每行状态只允许 `pass/fail/not_proven`；必须引用真实 Skill 内的文件路径与原文 anchor、实际外部审查/运行日志 SHA。能力 `automation` 须引用随包 `scripts/` / `schemas/` 中的真实实现及运行回执；`external` 即使声明为 pass 也仍待外部依赖证据，不能冒充本包能力。
3. 审查者必须独立于产物作者。**两个不同的字符串不是可信身份认证**；审查回执/真实宿主观察缺席时只报 `NOT_PROVEN`。审查者应从实际产物独立盘点所有承诺与冲突，不单纯复述作者给的 brief。若发现漏项，先修订并重冻结 brief，再重做绑定的 review，不能在最后省略。
4. 这些资料只留当前轮 `notes/quality/`，不得塞进最终 Skill 的 `SKILL.md` 或 `references/` 当执行规则。预检拒绝放在成品内的 brief、review 和证据根目录，也拒绝已知来源记录文件与出处标记；书名、引文或隐含归因仍须按 R18 §2b 逐文件语义回读。修改任意最终 Skill 文件后，旧目录指纹、语义回执和任务回执均不能复用；审查所用的 peer Skill 版本也应重新核对。

### 6.2 只读机器预检（必要但不足）

```bash
python3 <SkillRoot>/scripts/kd_artifact_quality.py \
  --skill /safe/round/output/<真实-skill-id> \
  --brief /safe/round/notes/quality/brief.json \
  --review /safe/round/notes/quality/review.json \
  --evidence-root /safe/round/notes/quality \
  --peers-root /safe/results/skills
```

`--peers-root` 仅跨 Skill 时需要，且不得越过当前授权目录。脚本不执行被审 Skill、不调用模型、不修改文件、不进行联网安装。它核对完整 Skill 树 SHA、brief/review ID 覆盖、各声明文件锚点、自动化脚本与运行回执字节、peer 文档字段、适用反例及任务种类/日志。自动化实现须是随包 `scripts/` 或 `schemas/` 内的真实文件，使用安全相对路径并绑定实际 SHA；不按 `.py`、`.sh`、`.mjs`、`.yml` 等后缀判断实现是否存在。文件和摘要齐备仍不能代替运行回执，未提供回执时保持 `NOT_PROVEN`。一些明显的「自动/确定性校验」入口承诺也会提示潜在遗漏，但**自然语言发现不是完备的**，仍须独立语义审查。

- `FAIL`（exit 2）：结构或绑定失败、实际实现缺失、声明的检验失败；不得声称高质量 Skill 完成。
- `NOT_PROVEN`（exit 3）：必要证据/外部 Skill/实际运行不足；只能交付明确标注的有限验证草稿。
- `EVIDENCE_REVIEW_REQUIRED`（exit 0）：**仅证据清单/文件字节预检通过**，仍需独立语义审查、真实任务和目标宿主验收；输出中的 `semantic_truth`、`host_attestation` 永远是 `NOT_AUTHENTICATED`，此命令绝不授权 `GO`、安装或 G1/S12 写入。

### 6.3 JSON 字段口径与示例（ID 与摘要均不得照抄）

brief 的最小字段：

```json
{
  "version": 1,
  "requirements": [{"id":"R1","text":"声口材料缺失时仍可创建人物"}],
  "capabilities": [{"id":"C1","text":"建档时的声口待定出口","mode":"workflow"}],
  "interfaces": [{"id":"IF1","provider":"character-design","consumer":"writing-helper","fields":["entity","change","reason","evidence"]}],
  "applicability": [{"id":"A1","text":"声口三条真实正文样本的适用边界"}],
  "cases": [
    {"id":"T1","kind":"positive","scenario":"完整人物输入"},
    {"id":"T2","kind":"missing","scenario":"人物尚无正文台词"},
    {"id":"T3","kind":"conflict","scenario":"建档可待定与审查要三样本"},
    {"id":"T4","kind":"boundary","scenario":"非语言主体人物"}
  ]
}
```

review 须把 brief 的五组 ID **逐一**列全；`requirements[].ref` / `capabilities[].ref` 如 `{"path":"SKILL.md","anchor":"<实际原文>"}`。`semantics[]` 至少一项，引用两处不同真实文本 `refs[]` 与 `record_ref`；`interfaces[]` 含双方 `provider_ref/consumer_ref`、`peer_tree_sha256` 中 `provider/consumer` 的真实树摘要，以及 `record_ref`；`applicability[]` 包含 `scope`、`limitation`、`counterexample`、`ref`、`record_ref`；`cases[]` 有 `mode:host/manual/synthetic` 与 `record_ref`。所有回执形如 `{"path":"review-01.txt","sha256":"<实际文件摘要>"}`，相对于 `--evidence-root`。自动化另需 `implementations:[{"path":"scripts/check.py","sha256":"<实际文件摘要>"}]`、`run_ref` 和 `exit_code:0`。**路径、实际字节和 SHA 都必须核算；机器看见一个自填 pass 不等于它验证了语义内容。**

### 6.4 深度保真、Markdown与交付收口（补充GQ1/GQ2/GQ4，不新增GQ6）

静态结构门禁要捕获Markdown表格失效，但**不能充当**专业知识评价。对需求中的复杂操作，在冻结前由非作者按真实输入核查可观察判断、反例、分支输出和修订回归；R17 的出处记录只是证据目录，R18单行路由只是入口，二者都不是深度证据。若只看到概要表格而无可读决策链，GQ1/GQ2/GQ4相应项应标 FAIL/NOT_PROVEN，不得借文件齐全报告语义PASS。

**五步流程正式收口的顺序**：

1. 确认本轮声明的范围与静态/真实效果的验收边界；保留原始工具输出和退出码，缺失工具结果不得编造PASS。
2. 只读检查最终Skill的Markdown表格结构和模板，确认正文不提来源，没有别人的项目、作品和包外路径（R18 §2b），任何有数据行却缺GFM分隔行的表格视为交付格式失败；说明哪些是格式缺陷、哪些语义仍未证明。
3. 在notes/中记录静态回执、文件SHA和Skill整树SHA，并检查使用的正是**最终版字节**；签入静态结果不认证模型身份。
4. 满足本轮约定的静态交付后，依 R01 §2.1 将 checklist.md 顶部唯一正式轮次状态改为 **“`- 状态：已完成`”**，另记 **“`- 验收范围：静态交付`”**；不可另造“静态交付已完成”状态。log.md 记录“状态：已完成”、静态验收依据、单份 Skill 身份摘要和整个 output/ 冻结摘要、检查结果与未证明项。若真实任务或独立复核没发生，继续记 NOT_RUN/NOT_PROVEN，不得为了结案改成PASS。
5. 可在 notes/delivery-preflight-spec.json 加入可选 round_closure 并用 scripts/kd_delivery_preflight.py --round-dir 运行只读一致性预检（示例见 R18 §7）。**两个 SHA 算法不能混用**：R01 §2.1 的 `kd_round_output.py --root <Round>/output` 返回 `tree_sha256`，是完整 output/ 冻结摘要；R09 的 `kd_material_quality.py skill --skill <完整Skill>` 返回 `skill_tree_sha256`，是单份 Skill 身份摘要。仅当全部真实回执和两种指纹都核实后才能记录静态完成；工具不认证真实任务或非作者身份。

用户只要求静态交付时允许以静态范围完成并冻结草稿；**完整GQ和效果仍可为NOT_PROVEN**。工具无法判定来源与文学方法的高下，后续仍须独立任务测试。先有实际回执再更新闭合状态，不能只把模板里的CHECKBOX勾成通过。
