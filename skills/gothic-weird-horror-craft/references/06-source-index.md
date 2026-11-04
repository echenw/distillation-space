# 来源索引与版本/许可/证据边界

## §1 任务与版本元数据（必须随包保留）

| 项 | 值 |
|---|---|
| task_id | A-04-B01 |
| parent_task_id | A-04 |
| category | 16-类型小说专项/03-恐怖惊悚怪谈/**批次-01** |
| owner（任务表） | Main A（owner_queue_position 4 / subtask_order 1） |
| source_count | 25 |
| o200k_tokens（任务表估算） | 2,156,471 |
| source_path（批次视图，只读符号链接） | `distill/分类蒸馏/_来源批次/16-类型小说专项/03-恐怖惊悚怪谈/批次-01` |
| original_source_path | `distill/有原始正文/16-类型小说专项/03-恐怖惊悚怪谈` |
| workspace_path | `distill/分类蒸馏/16-类型小说专项/03-恐怖惊悚怪谈/批次-01` |
| method | `distill/knowledge-compiler/SKILL.md`（五步 + P0–P7） |
| 本轮次 | `rounds/round-p4-final-2026-10-30` |
| Skill id | `gothic-weird-horror-craft` |
| 覆盖率 | 25/25 FULL（`kd32_coverage_check.py` → `{"coverage_full": 25}`） |
| 逐本回源闸 | 32 份有效台账，`tally {"PASS": 32}`，0 失败、0 作废 |

**替代关系（replacement / scope）**：
- 本包**不替代**同题材批次-02 的 `horror-supernatural-craft`（来源清单不同、批次不同、任务 ID 不同）。
- 批次不是新的语义类型：`batch_is_workload_partition_not_new_semantic_genre = true`（任务表字段）。
  即"批次-01"只是 03-恐怖惊悚怪谈 这个题材下的**工作量分片**，不是另一个子类型。
- 本包**未接管**任何历史 Skill —— 批次-01 工作区此前不存在 output/、results/ 或 SKILL.md（P0 已用 `find . -type f` 全量枚举确认）。因此不存在"旧版本被本版替代"的关系；若日后发现历史产物，应作为**新增替代**记录在此，而不是静默覆盖。

## §2 来源角色核账（25 本，逐本可追溯）

角色取值：支持 / 补充 / 反例 / 冲突 / 不适用 / 未证明。

| PG | 作品（作者） | 角色 | 一句话理由（证据） |
|---|---|---|---|
| PG10150 | Dracula's Guest…（Stoker） | 支持 | 预警结构 + 可再生罪证 + 双重身（L69 / L2152-2155 / L5480-5481） |
| PG10744 | Men, Women, and Ghosts（Phelps） | 补充 | 灵异与日常/工业苦难并置；警告勿与灵建立亲密关系（L4051-4071 / L2251-2273） |
| PG10966 | The Ghost Pirates（Hodgson） | 支持 | 渐进侵占 + 等级制压制证词 + 感知差（L1533-1546 / L2568-2597 / L6192-6254） |
| PG1147 | A Journey from This World to the Next（Fielding） | 不适用（取作反例） | 冥界讽刺游记，无恐怖机制；仅取"伪造神迹"作可信度工程反例（L2395-2420） |
| PG14044 | The Angels of Mons…（Machen） | 支持 | 谣言生成 + 证词链批判 + 留白落点 + **感官阶梯**（L155-156 / L284-285 / **L714-756 日记（钟声→白影→白袍→乳香）、L733 字迹变歪、L758-770 作者压缩为病理报告** / L812-814） |
| PG14195 | The Haunted and the Haunters（Bulwer-Lytton） | 支持 | horror vs fear 分野 + 先兆/恶臭蒸气/黑暗成形的三段推进 + 理性-超自然混合模型 + 物证闭环（L250-277 / L380-384 / L575-577 / L591-606 / L877-909 / L1088-1094） |
| PG14471 | The Empty House…（Blackwood） | 支持 | 气氛先行 + 动物感知器（L59-101 / L1202-1227） |
| PG16726 | Four Weird Tales（Blackwood） | 支持 | 尺度恐怖 + 异象被扣留精确性质（L1200-1226 / L2930-2948 / L5271-5272） |
| PG18730 | Lore of Proserpine（Hewlett） | 补充 + 反例 | 可见性关系理论；反"异类须分善恶"（L1093-1110 / L2726-2731 / L3280-3298） |
| PG22662 | The Mummy's Foot（Gautier/Hearn） | 支持 | 怪诞调性 + 物件驱动 + 物证替换结尾（L118-119 / L299-301 / L529-531） |
| PG23217 | The Roll-Call of the Reef（Quiller-Couch） | 支持 | 可信度契约 + 仪式点名 + 声音信号 + 双重身体（L405-408 / L496-515 / L545-551） |
| PG2548 | The Poor Clare（Gaskell） | 支持 + 反例 | 代际诅咒 + 二重身；反"恐怖=惊吓"（L1084-1085 / L1585-1593 / L2050-2053） |
| PG25525 | Works of E. A. Poe（Raven Ed.） | 支持 | 分类学观察 + 伪造引信 + 怪诞讽刺（L40831-40855 / L41860-41882 / L42844-42858） |
| PG30368 | A Christmas Carol（Dickens） | 补充（冲突侧） | 幽灵作为功能装置/道德改造（L776-777 / L2638-2666） |
| PG3075 | The Return（de la Mare） | 支持 | 身份替换 + 被他人命名 + 证据灭失 + 悬置（L7747-7748 / L6590-6595 / L8695-8736） |
| PG389 | The Great God Pan（Machen） | 支持（核心） | 不可命名 + 转手叙述 + 铭文证据 + 临床式变形（L1153-1155 / L2060-2063 / L2195-2197） |
| PG4387 | Present at a Hanging…（Bierce） | 支持（核心） | 冷报道体 + 法证式否证 + 制度无能 + 留一问（L1786-1788 / L1600-1601 / L1638） |
| PG49222 | John Silence（Blackwood） | 支持 | 程序化病例结构 + 动物探针（L2001-2013 / L10403-10413）；疗法属人物设定，不作 P |
| PG53688 | Melmoth the Wanderer IV（Maturin） | 支持 | 嵌套故事 + 诱惑者功能 + "人最大的敌人是自己"（L801-831 / L2441-2486） |
| PG696 | The Castle of Otranto（Walpole） | 支持（原型） | 哥特原型 + "作者不必信、人物须信"（L137-145 / L294-307 / L570-600） |
| PG79426 | The Libertine Vol. II（Dacre） | 部分不适用 | 哥特世情，无超自然；仅"作者插话判词"可迁移（L2248-2254） |
| PG79428 | The Libertine Vol. IV（Dacre） | 部分不适用 | 同上；另取疯人院听觉空间（L2414-2432）与父罪及子的道德收束（L2947-2961） |
| PG8223 | Edgar Huntly（Brown） | 支持 + 冲突侧 | 不可靠第一人称（梦游）；前言明确弃用哥特城堡（L45-49 / L2830-2844） |
| PG84 | Frankenstein（Shelley） | 支持 | 造物者弃责 + 嵌套书信 + 怪物自述反转（L1506-1523 / L4575-4578） |
| PG9502 | The Room in the Dragon Volant（Le Fanu） | 支持（核心）+ 反例 | 超自然→犯罪反转 + 程序细节；反"必须保留超自然解释"（L4800-4843 / L4953-4959 / L5095-5177 / L5270-5280） |

**未证明（NOT_PROVEN）**：坡的"效果统一论/创作论"在 PG25525 台账覆盖区间内无对应证据；
任何形式的"写作训练量建议"在 25 本中均无证据。二者一律不写成规则。

## §3 行号口径（关键，避免引用错位）

- 本包所有 `L起-止` 均指该本 **`整本阅读版.txt`（阅读版）** 的行号。
- 阅读版与 `原始完整电子书.txt`（原始版）行数不同，例如 PG696：原始 4505 / 阅读 4120；
  PG10150：原始 5592 / 阅读 5588；PG25525：原始 49218 / 阅读 49213。
- 引用验证请用：
  `python3 distill/_tools/kd32_ledger_gate.py --book <台账> --src <整本阅读版.txt> --pg <PG> --start <起> --end <止>`

## §4 来源 SHA（P1 已核验，与 `书籍信息.json.raw_sha256` 逐本比对 25/25 OK）

```
PG10150 838424b6ea0afca4a89defd9ceda938cb4020fc31e5f1b5e4ea1a0e1a0fb1f11
PG10744 22f78c2d15c5ce4476e0ccc9d8efa3afb8897e782c5656936cf3180f2ef511a8
PG10966 229243244b4db6ba8a183682f60dad7f790c61532d9f83c4562f8aa9ea4a2644
PG1147  906f26d89ae1079bd054a9bc4410332a3b55fbb897b7d626eef9e94790e07413
PG14044 65e75ee4ddda4a754798c4f01f3e42ccb1c3c806ffd6688315d391b2e41d63a2
PG14195 c05db123f2bacdda44b50dba8c9322708e55bd3ea283c077e01d3393f48429a8
PG14471 3e088960cbd9b68bb7a425f519b5630562ec2b489874c8c03461f0a50c9fcd14
PG16726 48f5473e7e204cb7e4d65f12e996a1cfd05eb9afe228fa2b89409a3d8de2f415
PG18730 1380756a99b13b49ec5cd0641d3315dd21e282238444ed445a7891e7cd084fcc
PG22662 40cdb17a7b1e12476068735c7027cce3cbb125418bd49dc28bfa3112fbd8bfc4
PG23217 37c6393a0c68cbc6bed0bd099b3c4c934ae647271d2ffaa18b0c50b32959a60e
PG2548  998713cb7c03c3129a09231617c3ba8bd01bf3a4fda2fac879b6c9caad42f54e
PG25525 4419bc7d454ef18d382fa0e29247e9a1c21baa9b0fd79362a4960944a2d04878
PG30368 07b97a681c890e118231afa89a3be759e65579ac7a1ac895943b62a96dfa349a
PG3075  5f866be14ca4252c3faaf930fc09e760d83910bc529221d8ff46865d80779b24
PG389   d34f676e7b5e5a412f587e4bf9370438d7c2ea7cead34ab80a8d31bbc51e448f
PG4387  75ac7581df0470a8bbad66794ba8fdb59b94159a66b1a410be20ebd74e475ccc
PG49222 65b730adeb7964a73fd6c6c12d9b6aa8ad6aec7bcb54c1c6e03c46a3c4e3048c
PG53688 f655094d3fe00052a0ceb1cd4a9c6fb658b231a02fb2735dc0cde216613e36f7
PG696   bbe35d93142d38cc7a503209e29489175f2a0ec568f1e5d49231feb73bb2cb1b
PG79426 5d9e73794e672854acc6d763bda5852d789e83a25b4200741a6114597037d2ca
PG79428 2f1b94852d5bfe0e9ef748da7bcc29736ceb350fdbba32eaa29d93ba0cf3412c
PG8223  78919dd2964f1cbbaa4c8f6ef1307fe018c91eab40cad51f6d209e79db481225
PG84    7810cd483cffcf2cc8a1d8f0d5807931e69d4f48cd14149b8c76f88af82fead3
PG9502  e0b888c9a1eda5255bdb0c0950ff89c700d74a38556d01e50a27ff8599e4b1c0
```

## §5 权利与许可（如实声明，不做法律意见）

- 全部来源为 Project Gutenberg 镜像文本（各本 `书籍信息.json` 的
  `source_kind = Gutenberg_independent_mirror_text`）。
- 各本 `rights` 字段原文：
  **"Project Gutenberg official edition; rights need per-work and jurisdiction verification before reuse"**。
- `acquisition_status = SOURCE_BYTES_AND_MARKERS_VERIFIED_RIGHTS_NOT_LEGAL_CERTIFICATION`
  —— 即"字节与标记已核验"，**不是**权利的法律认证。
- 本包只做**创作工艺规则**的归纳，不复制作品正文；引用均为短句且标注行号，用于回源核验。
  如需商业再版、翻译或大段引用，必须按各作品各自的司法辖区另行核验。

## §6 证据边界（必须随结论一起说）

1. 台账证明的是"**声明区间覆盖 + 引文可回源**"。`kd32_coverage_check.py` 自述：
   "机器核验=台账声明区间的并集覆盖；不证明模型真实输入"。本包沿用该口径，不宣称更强。
2. 语料年代与语种：18–20 世纪初英语传统（含一部英译的法文短篇 PG22662）。
   对现代背景、非英语传统、影视/游戏媒介、规则怪谈等形态，适用性 `NOT_PROVEN`。
3. 作品内的**角色做法**（如 John Silence 的疗法）不是作者的写作教学，不可当方法论输出。
4. 单部作品的情节不可升格为通则；本包的通则均由 ≥2 部独立来源同向支撑，
   单来源支撑的条目已显式标注来源并降级为"可选形态"。
