# 本轮来源定位与证据等级（自历史索引迁移，含 round-p4-final-2026-10-30 核验结果）

原著及其历史阅读证据不随 Skill 包复制。本表由已有元数据、原始与阅读版 SHA-256、逐段台账及原文引文回源核验形成；不表示本轮重读全书。历史索引（`round-p4-wave4-agent3-2026-10-30`）若有不同结论，以本轮核验为准——两者在本表的 SHA、行数、台账结论上没有差异，本轮只新增了三段定点补读证据与一份引用复核表。

| PG | 来源书名 | 全文行数 | 阅读版 SHA-256 | 可回源区间 | 验证级别 |
| --- | --- | ---: | --- | ---: | --- |
| PG19028 | Irish Plays and Playwrights | 9452 | 81db8e9e6a1e4dc7960e04b3d82706fe3517513ab48e571e1ab874a99639d1f6 | 9452/9452 | FULL |
| PG32433 | How to See a Play | 3739 | 3bf93587c60ad514047c2cdcec14cbf128072cbf3a0c36eaed0d5ad3f82f5942 | 3739/3739 | FULL |
| PG36790 | A Book About the Theater | 7332 | 596a36db50e90e51ef192ab8caab9b68fb58191f6a4868b437353ad34af7184b | 7332/7332 | FULL |
| PG43490 | The Social Significance of the Modern Drama | 8211 | 7608ff6ab592289e6682fe719d0b084d3582c2aa3c0e398defb9569793688180 | 8211/8211 | FULL |
| PG63188 | The Critic and the Drama | 2426 | 617362eca480d35ea2836207c9b30a82f45b694984c6ab785cd8c70335345642 | 2426/2426 | FULL |
| PG68853 | Pastiche and prejudice | 6578 | 780e0401e6eaecc5c3376127e149b68891e8be485ed96f2acfec699bd2f1e54e | 6578/6578 | FULL |
| PG72661 | Playwrights on playmaking | 6673 | 1be2139f771ea8ef607acff816f8c89149e0df9bf8acbf2b25407309680e18aa | 6673/6673 | FULL |
| PG74314 | The Sanskrit drama | 15490 | bf2b45fb3111cbe67ccbefa8fe5f367616aa15637a0c4d7011db38ecff7f193d | 15490/15490 | FULL |
| PG76555 | The Attic theatre | 18943 | e99a57dcd4cddd4dffffce4845d827bee6a9a8679c0939d5b73c39a9f41e227d | 18943/18943 | FULL |

## 台账回查与来源边界

全部台账均在 `distill/分类蒸馏/05-章节与场景设计/rounds/` 下，本轮用 `python3 distill/_tools/kd32_ledger_gate.py --book <台账> --src <原文> --pg <PG> --start <起> --end <止>` 逐个重跑，判定一律 PASS；每本元数据与两类 SHA 均 MATCH。

- PG19028: `round-perbook/notes/reading/ledger-PG19028-full.md`（L1-9452，16 块，34 引文）
- PG32433: `round-kd32-r02/notes/reading/ledger-PG32433-s1-3739.md`（L1-3739，32 块，33 引文）
- PG36790: `round-perbook/notes/reading/ledger-PG36790-full.md`（L1-7332，14 块，24 引文）
- PG43490: `round-perbook/notes/reading/ledger-PG43490-full.md`（L1-8211，25 块，41 引文）
- PG63188: `round-kd32-r01/notes/reading/ledger-PG63188-s1-2426.md`（L1-2426，24 块，23 引文）
- PG68853: `round-shard-dfm/notes/reading/ledger-PG68853-s1-6000.md`（L1-6000，10 块，62 引文）+ `ledger-PG68853-s6001-6578.md`（L6001-6578，2 块，3 引文）
- PG72661: `round-shard-dfm/notes/reading/ledger-PG72661-s1-6000.md`（L1-6000，10 块，43 引文）+ `ledger-PG72661-s6001-6673.md`（L6001-6673，3 块，10 引文）
- PG74314: `round-perbook/notes/reading/ledger-PG74314-full.md`（L1-15490，39 块，39 引文）。同目录另有 `ledger-PG74314-full.rejected.md`（旧版，门禁判 FABRICATED 后作废，不计）
- PG76555: `round-perbook/notes/reading/ledger-PG76555-full.md`（L1-18943，32 块，31 引文）

## 本轮新增证据（round-p4-final-2026-10-30）

- `notes/evidence-citation-audit.md`：把历史 Skill 的 28 条 F 引用按行号逐条回源复核，给出 SUPPORTED / THIN / OVERREACH / MISREAD 判定。
- `notes/evidence-supp-PG43490-L1440-2157.md`（实读 L1440-1470、L2136-2157，门禁 PASS）：压力源不是单个人物。
- `notes/evidence-supp-PG76555-L7425-7504.md`（实读 L7425-7504，门禁 PASS）：形式由制作约束生成。
- `notes/evidence-supp-PG32433-L152-165.md`（实读 L152-165，门禁 PASS）：幕／场划分的功利成因。

## 引用与管理边界（沿用历史条款，未删）

- 历史批次的作品／戏剧／评论所见为 F，提议的写作操作为 H/P；一部作品的形式不自动构成所有作品的定律。
- 本批结论按原著及历史已有阅读得出，不是本轮重新完整通读九书；实际读者效果（GQ5／P5）无回执。
- 来源许可事项：九本全部取自 Project Gutenberg 镜像，每本的 `书籍信息.json` 记录 `source_rights_warning`（PG 有美国公版规则与例外，须按文本与司法辖区核验；非全文仅元数据）与 `source_license_check: MIRROR_HEADER_SCREENED_US_PD_RULES_NOT_LEGAL_OPINION`。该筛查不构成法律意见。

## 历史版本的差异说明（便于审计）

| 项 | 历史 round-p4-wave4-agent3 | 本轮 round-p4-final |
|---|---|---|
| 来源数与 SHA | 9，一致 | 9，一致，本轮重算核对 |
| 台账覆盖 | 声称 9/9 FULL | 本轮重跑门禁，9/9 PASS（结论一致，但本轮有实际运行证据） |
| 引用错数 | 未做逐条回源复核 | 复核 28 条，发现 1 条 MISREAD、2 条 OVERREACH、3 条 THIN |
| S6 反例 | 用 PG74314 L5536-5600 作"修辞无需改"的反例 | 判定为 MISREAD，本轮重立为三判据版 |
| S8 | 标 ADOPT（有来源依据） | 降级 NOT_PROVEN（无来源支撑，仅为输出格式） |
| S0 | 无 | 新增：效果优先于合规则（PG63188 L381-387） |
| K1–K6 | 无 | 新增：来源分歧与不适用清单 |
