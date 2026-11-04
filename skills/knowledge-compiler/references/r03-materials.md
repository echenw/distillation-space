# R03 — 导入材料与交付准备

材料需要转换格式、检查隐私、预览候选改动或做增量更新时，查对应的小节。这里的工具只读取指定的输入，输出报告或草稿；实际的 AI 运行、写文件和批准仍由获准的执行环境负责。项目总需求、每轮交付和累计成果的位置按 R01 §1–2 与 R06 §4.13 管理，这些工具不会自动维护 `requirements.md`、冻结轮次 `output/` 或合并 `results/`。

## 1. 导入材料：格式转换、许可与隐私

```bash
python3 <SkillRoot>/scripts/kd_material_ops.py normalize --input /authorized/chatgpt-export.json
python3 <SkillRoot>/scripts/kd_material_ops.py normalize --input /authorized/notes.docx --include-text --redact
python3 <SkillRoot>/scripts/kd_material_ops.py coverage --root /authorized/batch --manifest /authorized/coverage.json
```

### 1.1 支持的格式与上限

- `normalize` 支持 UTF-8 的 TXT、MD、LOG，HTML，标准 Word DOCX 的主文档，普通 JSON 文档（包括顶层数组）、结构化会话 JSON（ChatGPT 的 mapping，或带 messages 的 Claude 等常见导出）和 PDF。
- PDF 只在本机已有可信的 `pdftotext` 时只读提取；工具不可用或解析失败就返回错误，**不编造内容，不安装软件**。PDF 里的复杂图表和扫描图片、DOCX 的批注和表格布局都不在文本提取范围内，要由宿主认可的专用提取器另外提供。
- PDF 的同一次原件读取和提取响应同时生成非空文本单元与 `extraction_observations.pdf`。`observed_page_slots` 只数提取流中观察到的页槽（`count_basis:extraction_stream`），不认证 PDF 元数据总页数；末尾 form-feed 只去掉一个终止分隔符造成的空后缀。首、中、末的其他无文本页保留原始 1-based 页码、`pdf:page:N` 锚点和 `reason:UNKNOWN`，不能据此断言是扫描页、空白页或损坏页。
- 文本与无文本页混合时，无论是否加 `--include-text` 都返回 `NEEDS_REVIEW`、退出码 2；无缺口时沿用原有风险状态。全无文本仍为 `FAIL/EMPTY_EXTRACTION`，提取器失败仍为 `FAIL/PDF_EXTRACTION_FAILED`。缺口不生成空单元、假行号或缺失文件计数，已有非空正文、页锚点及提取文本摘要的算法保持不变。
- 输入原件上限 8 MiB，提取后总文本上限 12 MiB。对提取结果中超过 8 MiB 的单个文本单元，`normalize` 按 UTF-8 边界（优先换行）无损拆成 `:part:N-of-M` 来源片段，片段分别带 SHA-256，适配 R09 每文件 8 MiB 的检查上限；全局 `extracted_text_sha256` 仍对应拆分前的提取全文。超过总上限的原件需要经授权预先按事件、页或行切分并记录缺口，不能截断后标成已完整处理。
- 脚本不访问用户 HOME、网络、剪贴板或其他没指定的目录，也不写材料仓库。

### 1.2 会话导出

- ChatGPT 的 `mapping` 带 `current_node` 时，只提取从根到当前节点的真实 `parent` 路径；废弃的兄弟回答不算在内，并计入 `excluded_branch_messages`。所有父节点（包括没选中的分支）都先验证没有悬空的 parent 和环。
- 缺 `current_node` 时，只有一条连续的 parent 链才按真实的拓扑顺序解析。有分叉时保留 `branch_status:unresolved`；分叉或断链都强制 `NEEDS_REVIEW`，不用时间戳拼出一段线性对话。
- Claude 的 `chat_messages` 和普通的 `messages` 按自身的事件顺序。消息保留角色（user/assistant/tool）、工具调用与结果、消息 ID 和对话 ID。
- 来源里的 `type:tool_result` 只有和结构角色 `role:tool` 一致时才算工具返回事件。这个分类**不证明宿主确实执行过**，可信的工具回执仍要独立核验。模型声称执行成功、工具调用建议、实际的工具返回和用户纠正各自独立，不能合并成“已证实的行为”。
- `assistant` 自报的 `tool_result` 和不是字符串的角色会被拒绝。`author.role`、`role`、`sender` 同时声明不同身份时返回 `CHAT_ROLE_CONFLICT`；`user` 或 `system` 使用 `tool_use` 或定向的工具 recipient 时返回 `CHAT_EVENT_ROLE_CONFLICT`。`human`/`user` 和 `function`/`tool` 只在核对时当作同义角色，输出保留来源的拼写。
- 明确属于会话结构的 JSON（含 mapping、messages、chat_messages 或 conversations）必须有有效事件。ChatGPT 选中的链里只允许没有消息的父根占位；其他选中节点缺消息或消息不是对象时稳定拒绝，不悄悄跳过，也不降级成 `json:root` 文档通过。不含会话结构键的普通 JSON，包括没有会话对象的顶层数组，走通用文档处理；数组中一旦有会话对象，所有项仍须满足会话合同，不能把坏项混入普通文档。
- 结构不兼容时不猜测工具成功：`recipient` 只能是字符串或 null，`conversations` 必须是对象数组，其他类型返回受控的 FAIL JSON 和非零退出码。
- 根解析器照旧拒绝重复字段。`NaN`、`Infinity`、`-Infinity`、转换后不再有限的指数数值，以及嵌套过深的输入（即使文件不到 8 MiB），都返回 `INVALID_JSON`。带引号的这些词只是普通字符串，合法的有限数字照常读取。

### 1.3 锚点

- 消息和对话的 ID 只在缺失、为 null 或空串时，才退回到图节点键或数组序号；非空的原始 ID 原样保留。
- 锚点的写法是 `chat:v1:` 加一个紧凑的 JSON 二元组 `[[身份类型,会话值],[身份类型,消息值]]`，可以还原出原始标识。身份类型有 `id`（真实 ID 或 UUID）、`index`（位置兜底）和 `node`（mapping 节点键兜底）。不同类型下字面相同的值不会冲突，原始 ID 里的冒号也不会造成拼接碰撞；完整身份真正相同时返回 `CHAT_ANCHOR_DUPLICATE`。
- 编码后的原始锚点最长 4096 字符，更长的在这一步就返回 `SOURCE_ANCHOR_INVALID`，不留到 R09 才失败。分片追加的 `:part:N-of-M` 不占原锚点额度；序号和总数受提取字节资源上限约束，R09 按同一规则检查原锚点与后缀。

### 1.4 隐私、许可与输出

- 默认只返回来源和转换内容的摘要、单元锚点、行数和风险计数，**不回显内容**。显式加 `--include-text` 才输出文字；检测到邮箱、手机号或密钥时必须同时加 `--redact`，并保留原始字节和脱敏输出两个 SHA。
- 凭据扫描、脱敏、分片保护和解码后来源元数据检查共用完整跨度规则：除原有 API key、token、password 等形式，还识别大小写不敏感、支持 tab 的 `Authorization: Bearer`（token 字符包括 `._~+/=`）、`postgres` / `mongodb` / `mongodb+srv` / `mysql` URL 中直至 `@` 的 userinfo，以及完整 `RSA PRIVATE KEY`、`PRIVATE KEY`、`OPENSSH PRIVATE KEY` 块。脱敏移除整个私钥块及其正文，数据库 host/path 不作为必需敏感字段。完整形状的虚构示例仍需 triage；`Bearer <TOKEN>` 和 PUBLIC KEY 块不因这些新规则报警。
- 分片不得切入完整凭据跨度；完整跨度本身超过 8 MiB 时返回 `SENSITIVE_UNIT_UNSPLITTABLE`。原有邮箱、电话、许可预警及资源上限继续适用。这些有限结构规则不证明凭据有效，也不覆盖所有畸形、截断或跨原始单元的秘密。
- 锚点和角色也来自不可信的原件。会话 ID、消息 ID 和 mapping 节点的兜底键，先按原始解码后的字符串扫描敏感模式，再编码成锚点；编码后的锚点和角色在输出前再扫一次，避免 JSON 的 `\n`、`\t` 转义把密钥格式藏起来。
- 来源 ID 或角色里扫到邮箱、电话或密钥形式的内容时，不管有没有 `--include-text` 或 `--redact`，都返回 `SENSITIVE_SOURCE_METADATA`（错误信息不含原值）。不能随手换一个锚点假装来源关联仍然成立；宿主要另行受控处理原件，确认合法的映射后再提交。
- 报告包含 `normalizer_version`、`extractor`、`extractor_version`（外部工具版本查不到时为 null）和 `extracted_text_sha256`。每个 `units[i]` 带一份可以直接交给 R09 的 `lineage` 和 `output_sha256`。同一来源的转换结果不算独立证据。
- 当前的归一化算法标识是 `kd-material-ops/9`。分片同时按原文字节和最终脱敏字节检查资源上限，脱敏扩容会继续分片；每片保留原文字节摘要、输出摘要和同一原件关联，行数对应最终输出。旧的 `/2` 到 `/8` 生成的来源关联不能当作当前算法的结果，要对获准的原件重新归一化、重新固定输出摘要并审查差异。
- 风险识别只是保守的预警，**不能声称已经绝对匿名**。许可判定始终是 `license_verified:false`，版权不明的由人判断；疑似受保护的文档和敏感素材，未经许可不能进入正式产物。

### 1.5 交给 R09 的来源关联

- R09 的 `dossier.json` **版本 2** 要求每个 `sources[]` 写明 `lineage`。没有转换过的一手文本用 `{"kind":"direct"}`。转换过的材料按**一个文件对应一个归一化单元**，把 `units[i].lineage` 逐字写进对应的来源，存盘的字节必须和 `units[i].text` 一致。没有 lineage 的版本 1 不能通过结构检查。
- 宿主须在同轮持久保留完整 normalization 报告及非空单元文件，以报告的 `source_sha256` 绑定原件；报告和后续范围裁决放在 R09 受检纯文本目录之外。PDF 的 `extraction_observations.pdf.no_text_pages` 必须随报告进入本轮 scope review，不能只保存文本单元后丢掉缺口。经证据支持的范围裁决，或另行授权的视觉/OCR 复核，可解决任务范围问题，但须保留原观察及裁决依据；本工具不自动运行 OCR。
- R09 据此核对原件摘要、提取器及版本、页或消息锚点，以及原单元和脱敏输出的摘要关联。提取器版本为 null 时 R09 拒绝完整批次通过：要补上可信的版本证据，或者保留这个缺口。
- 同一个原件 SHA 加同一个 `source_anchor` 的单元，即使复制成多个路径、多个来源编号或不同的脱敏输出，也只算一个来源，R09 会拒绝重复声明；同一来源的不同单元可以分别登记。
- 手工摘要、拼接多个单元或增删换行，都不能当作一个归一化单元，也不能谎称 direct；保留逐项的原件来源，交宿主审查。
- 原件可以留在原来的受控路径，R09 不重读它，也不认证它的真伪。转换输出不能冒充另一份独立的事实证据。

### 1.6 阅读范围记录 `coverage`

本地清单路径按字面文件名解析，可包含 `%`，不会做 URL 解码。绝对路径、父级穿越、NUL 和符号链接仍被拒绝；Markdown 链接属于另外的 URI 边界。

- 清单要列出当前批次的全部来源。读得到的来源给出 `path`、`sha256` 和若干不重叠的 `spans[start,end,label,reason,sha256]`；`label` 是 `relevant`、`irrelevant`、`unread` 或 `unavailable`。
- 来源**确实缺失**时写 `{"path":"missing.txt","availability":"unavailable","reason":"具体缺口","spans":[]}`。可以保留旧的 `sha256` 或写 null，但不能编造当前的行号和行摘要；存在的文件不能标成缺失。缺失的来源在 `line_classes.unavailable` 里只算一个占位，行数报告为 `unavailable_line_counts:"UNKNOWN"`，不算已读。
- 工具检查现有来源的真实字节、完整清单、窗口 SHA 和重叠。`availability` 必须是字符串 `available` 或 `unavailable`，否则返回 `COVERAGE_AVAILABILITY_INVALID`；`spans` 必须是数组，每个 `label` 必须是上面四个字符串之一，否则返回 `COVERAGE_SPAN_INVALID`。坏输入只会得到受控的错误，不会抛出未处理的异常。
- 只要有 `unread` 或 `unavailable`，结果就是 `NOT_PROVEN`。“已核实不相关”不等于没看过；全部分类通过也不证明模型的注意力或语义准确。它和 R09 的溯源检查分工不同，不是第二个知识维护来源。

## 2. 确认执行范围、输入版本和输出要求

R01 的 `plan.depth` 取 `quick`、`standard` 或 `strict`，工具按深度限制能做的事。**深度不等于覆盖范围**：全量、定向或轻量覆盖及初始/增量/专项方式以本轮 `checklist.md` 的确认内容为准；`task-brief` 的 `plan.depth` 不会替它们做范围验收。

- **quick**：在本轮已确认的覆盖范围内整理材料、核对原文和风险、提出产物建议。确认后的任务不能选 `action:create` 或 `update`，只能是 `materials_only`，或者 Skill、Rule 的 `action:propose`；不能申请编辑 Skill、Rule 或生产文件的权限；不能声称已经生成可用的 Skill 或做过真实宿主评测。
- **standard**：形成受控的候选、来源关联、候选的静态检查和逐项的用户审阅。没做真实宿主评测就保持 `NOT_PROVEN`。
- **strict**：在 standard 之上，要求独立冻结的验证集、真实宿主的消费回执、实际任务产物和安全回归。没有权限、模型或预算时停在“待验证”，不把命令行 fixture 当成宿主运行。

固定版本和目标时：

- 草稿状态可以暂缺材料的 `snapshot_sha256`；确认后要生成或更新产物的，必须固定每个来源的快照。确认后的 `update` 还要有 `target.before_sha256`，以目标文件树或配置文件当前的实际摘要为准。
- 用户意图变了，就不能再用**任何历史已确认版本**里的旧用户消息定位。Skill 和 Rule 不能指向同一个物理目标。
- 多个子代理各自限定在自己的工作单元和材料 ID 内；宿主能力不明时退回单个 Agent。模型、版本、Token 预算和报价都是**需要核实的输入**，不是随手填的成功声明。
- Skill 目标至少写明什么时候触发和不触发、输入和输出、用到的工具和外部资源、必要的依赖、失败和回退，以及正例、反例和边界用例。Rule 目标要标明是项目文件、某个宿主的全局规则，还是知识库的 Scope；前两种按实际的文件权限授权，知识库的 `global` 不是用户的全局配置文件。

## 3. 起草候选 Skill/Rule，检查改动差异

```bash
python3 <SkillRoot>/scripts/kd_candidate_review.py scaffold --brief /safe/task-brief.v1.json --id S1
python3 <SkillRoot>/scripts/kd_candidate_review.py review --before /safe/old-skill --after /safe/new-skill --kind skill --before-sha256 <old-tree-sha256>
python3 <SkillRoot>/scripts/kd_candidate_review.py maintenance --skill /safe/staged-skill
```

- `scaffold` 在标准输出里给出候选 `SKILL.md` 或 Rule 的结构草稿，标明 `PROPOSAL_ONLY`，不写用户文件，也不把来历不明的内容当作命令复制。**它只给结构，内容仍要由 AI 读完材料后提炼**：宿主 AI 按 R06 §3–4 阅读有出处的材料，编写不带来源信息的候选指令，在本轮 notes/ 的 dossier 中关联来源证据与成品唯一锚点，靠不住的源码主张和冲突交人工复核。有明确的编辑授权时，可以把候选放进获准的目录，或按 R06 §5 改到目标源文件；安装到个人目录仍要单独授权。没有编辑授权时只交付可审阅的提案。
- `review` 不写文件。它对修改前后的整个文件树算稳定的摘要，列出改动和删除的文件、可执行脚本的变化、需要外部证据复核的新增规范性语句行号、夹带的已知来源记录或出处标记，并做 Skill 的静态检查。成品内的注释或标记不能免除外部证据复核。规范性语句的识别是**启发式**的，扫描没有异常不等于每条语义都有证据；仍要用 R09 的 `material` 逐条对照 dossier，核对反例和适用条件，并给出可审阅的新增、修改和删除。普通修改按已有授权执行；目标、归属或权限的重大变化要重新确认，正式知识入库仍走 G1。目标摘要变了就直接拒绝原来的差异，不向旧文件无条件覆盖。
- `maintenance` 检查静态引用、夹带的已知来源记录与出处标记、重复的长条目和 TODO 之类的待核标记。它不自动删除旧规则、安装包或历史版本；这些只是审查提示，不能因为次数少或没被引用就停用。

## 4. 核对实际运行记录与费用

```bash
python3 <SkillRoot>/scripts/kd_execution_review.py --brief /safe/task-brief.v1.json --events /safe/actual-host-events.json
```

- R01 的 `plan.max_cost_usd` 可选；并行时要写明 `host_max_agents` 和 `budget_max_agents`。**每个发出过 `model_request` 的 Agent（包括 `lead`）都要在冻结的 `plan.agents.model_routing` 里声明 `model` 和 `max_context_tokens`**，否则脚本拒绝验收。没有模型请求时可以省略路由。脚本不启动 Worker，也不调用付费模型。
- 宿主运行时把 `events` 写进**同一任务的受控运行证据附件**，用 `plan_sha256` 固定任务。事件类型有 `agent_start`、`agent_end`、`model_request`、`tool_result`。每条记录有唯一 ID、worker 和 work_unit_id；模型请求记录 request_id、model、input/cached_input/output Token、duration_ms 和 usd_per_million（input、cached_input、output 三个价格）；工具返回记录 exit_code 和 output_sha256。
- 脚本核对任务、Agent 和工作单元的对应关系，每个工作单元的完成状态，请求去重，缓存不超过输入，模型和上下文路由，费用上限和结果摘要字段。`max_context_tokens` 指整个上下文窗口，检查 **`input_tokens + output_tokens <= max_context_tokens`**；`cached_input_tokens` 是 input 的一部分，不再加一次。
- 这些字段目前来自 `fixture` 或 `host_reported` 数据，结构完全一致也只能标为 `SIMULATION_ONLY` 或 `HOST_REPORTED_UNAUTHENTICATED`。**真实的额度扣减、缓存命中率和宿主完成证据，要靠用户授权的连接器或不可伪造的宿主日志**，自己写的 JSON 不是计费回执。
- 并行任务的实际会话、工具隔离、Worker 生命周期、超时和回退由宿主执行器管理，本 Skill 只核对计划和事后记录。宿主不支持并行时按 R01 退回单个 Agent 并留下记录，不要声称启动了并不存在的子代理。

## 5. 比较效果、处理变化并交付

R09 `compare` 的冻结 oracle 里，`cases[]` 可以用 `expected_files` 断言产物的路径和 SHA-256，这时允许 `expected_stdout:null`（至少要有一个 expected_files）。**只有带非空 expected_files 的案例，各组的 `run` 才必须提供 `artifact_dir`**；只看 stdout 的案例不需要空的产物目录。路径相对 `--outputs`，并受边界检查。它适用于代码变更、文档产出和组合文件，但**仍然是严格的文件字节对照**：允许多个正确答案的任务，由宿主指定**独立冻结的领域判定器**先生成可核对的回执。脚本不执行来历不明的判定器，也不能用候选模型的自评代替。

```bash
python3 <SkillRoot>/scripts/kd_incremental.py --previous /safe/old-brief.json --current /safe/new-brief.json --dossier /safe/old-dossier.json
python3 <SkillRoot>/scripts/kd_material_quality.py compare --operation create --oracle /safe/frozen-oracle.json --manifest /safe/run-results.json --outputs /safe/output-root --candidate /safe/new-skill
python3 <SkillRoot>/scripts/kd_material_quality.py compare --operation update --oracle /safe/frozen-oracle.json --manifest /safe/run-results.json --outputs /safe/output-root --baseline /safe/old-skill --candidate /safe/new-skill
```

- `kd_incremental.py` **仅比较显式传入的两份任务 JSON 快照**，不自动读取项目 `requirements.md`、批次索引、各轮 `output/` 或 `results/manifest.yaml`。若要用它比较相邻轮次，**两份快照必须都列出比较范围内的完整有效材料集合**，对继承的材料保留同一 ID 和来源 SHA，新材料追加 ID；仅列本轮新增材料的清单不能拿来直接比较，否则历史材料会被误报为 `removed_materials`。需要只分析增量批次时，按本轮 `inputs/manifest.yaml` 和既有成果手工限定范围，不把它的差异报告冒充成果合并、权限或总需求继承的证明。它比较两版任务快照里冻结的材料 ID、SHA、目标与整体计划。带 `--dossier` 时，R09 版本 2 的每个 `sources[]` 都要用 `material_id` 指向旧快照里对应的 `materials[].id`，并把原件摘要和旧快照绑定。两种 ID 的命名空间各自独立；缺映射、快照不一致或旧主张指向不存在的来源都会被**拒绝**，不会把失效的报告伪装成空清单。
- 它报告 `added/changed/removed/unchanged`、**新旧两版依赖的并集**、`retired_work_units`、`detached_prior_dependencies`、受影响的工作单元和旧主张。**工作单元的生命周期独立于材料摘要**：旧的工作单元 ID 在新版里消失时列入 `retired_work_units`；同一工作单元不再依赖某个旧材料 ID（或整个单元退役）时列入 `detached_prior_dependencies`，即使所有材料的 SHA 都没变。只增加依赖不算解绑。
- 移除来源时，不能因为旧的工作单元从新计划里消失，就漏掉它的退役和旧证据的失效。`reconfirmation_needed` 仅按两版计划 SHA 是否变化计算，不认证实际授权；已有授权仍覆盖普通调整时按 R01 §4 追加 draft 和真实授权记录，新增范围或关键决定缺授权才补问。输入快照仍须更新，旧证据失效不能忽略。没有变化不等于知识正确，也不能只按时间戳跳过失败或待处理的来源。这个工具不重启宿主，也不写源文件。
- 新建的目标没有旧 Skill，按 R09 的 `create` 记两组；更新按 `update` 记三组，并固定真实的旧目录。要证明效果或做 strict 验收时，两种模式都要证明好于实际不加载 Skill 的对照，而且逐个案例没有退步。只做整理、提案或静态修订的任务不强制运行对照，效果未验证就照实标明。不能用空目录伪造基线；结构通过不代表有真实收益或生产批准。

正式交付时向用户报告：总需求依据、当轮覆盖和深度、`rounds/<轮次>/output/` 的实际交付位置及 `results/` 是否更新，来源、许可和安全情况，候选的取舍，修改前（新建时为“不存在”）和修改后的状态，冲突和遗漏，真实的 Agent 和费用证据，评测情况和没有验收的层面，以及暂存、安装或发布的状态。学习和提炼是否真的改善了任务结果仍要独立验证；已有的 S12 和 G1 权限没有后门。

## 6. 本 Skill 不做的事

- 不安装库或第三方命令，不提供无凭据的模型 API 服务。
- 不自动扫描用户 HOME、账号或私有聊天，不持续采集对话，不爬取网页。
- 不把 PDF 里提取不出的图片和表格说成已读。
- 不自动启动未知的子代理。
- 不另建一套知识数据库，也不开第二条事务写入路径。

适配多个宿主时，由真实的宿主保存各自的配置和能力声明。静态的打包测试不能当作对应的 Skill 已经被自动触发。
