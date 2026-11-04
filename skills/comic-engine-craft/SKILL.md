---
name: comic-engine-craft
description: "Design or diagnose the comic engine of humorous fiction: who produces the joke, which mechanism sustains it, where it pays off, and when to stop. Covers attribution, absurd-premise bookkeeping, name inflation, deadpan catalogues, said/meant gaps, off-scene payoffs, refusal/omission, and satire targets. For novel-length or linked-sketch comedy; not one-line jokes, sitcom scripts, or pure parody."
---

# Comic Engine Craft（喜剧引擎工艺）

## 0. 这是什么 / 不是什么

人工判断 + 条件路由的设计与诊断 workflow，不是自动化系统，不含 scripts，不预测笑点命中率。

- **输入（必须有，缺则先问）**：① 体裁与长度（长篇 / 连作短篇集 / 单篇）；② 叙述视角（第一人称参与者、见证者、匿名寓言腔、全知）；③ 讽刺或笑的靶子（人物信念、关系权力、语义误会、机构规则、时代风气）；④ 已有稿或场景（没有就只给设计，不评价稿件）。
- **输出**：引擎配置表 + 包袱调度表（§7）+ 所走规则与依据（PG + 行号）。
- **不做**：不写正文；不保证读者会笑；不对现实法律/医疗/商业制度下断言（一律标 `UNRESOLVED`）。

## 1. 来源与可信边界（2026-10-31 最终 P2 回源）

- 权威任务 `B-04-B04`，共 24 本来源、193,004 行。`批次来源清单.json` 24/24 个阅读版 SHA-256 与实文一致；注意 PG3711 的原始完整电子书与阅读版 SHA 不同，**两个格式间不能因为书目相同就假称哈希相同**。
- 本轮逐本回源 P2 校验结果：**24/24 FULL、193,004/193,004 行连续可查、零缺口**，详见 [来源索引](references/04-source-index.md) 及轮内 `notes/p2-source-gate-audit-20261031.json`。
- **新读与继承严格区分**：PG3829 L103-522 是本轮真实新读；其他若来自 2026-10-25/26 的长篇细节台账，只进行了分块、原文 SHA、准确引文的定位复核，旧版 11/24 的统计是过期快照；13 本旧缺口已由 2026-10-31 台账补齐 run（workflow dwfrun-720d232d，hy3×50，一本书一个代理）全本逐段实读（13 份台账 `notes/reading/ledger-PG*-L*.md` 门禁逐本 PASS，合计 85,742 行），wave 补证的重排台账并行保留作第二证据。
- **台账知识融合（2026-10-31 第二批）**：13 本新台账（151 块/291 引文，门禁逐本 PASS）中的喜剧机制、错位结构与反例已融入 references 01/02/03/05（「融合补充」行），并新增三个机制条目——02 §6 制度字面主义、02 §7 虚惊与讣告、03 §7 文件层反讽；C 系列规则编号与裁决**不变**，只增不删。改动清单与抽查记录见第 11 节与 [04 来源索引](references/04-source-index.md)。
- **本轮实质规则修订**：PG3829 中养鸡计划的自信与真实资源矛盾补充 C3/C7；PG3184 的“善意故事后续灾难”并非现实道德指令，可与 PG74733 的 C15“帮助被利用”及温情结局并存；PG1999 角色兜售写作秘诀是反讽而非写作科学。新增 [05 条件诊断](references/05-confidence-and-feedback.md)。
- F = 由 PG 行号与文本语义真正支持的小说事实；H = 适用范围受限的机制判断；P = 作者可选动作。**门禁 PASS 只证明有来源覆盖与逐字引文，不保证历史全部解释真确，更不能预测读者笑果**。P5/GQ5 未跑。

## 2. 触发 / 负触发

**触发**：设计长篇喜剧的引擎（笑点由谁产生、靠什么持续供给）；已有稿「好笑但累」（同一机制连用疲劳）；讽刺作品的宣言与兑现调度；幽默短篇集/连作的结构与开篇；判断某场景该不该继续开玩笑。

**负触发**：单句笑话/段子集（无引擎需求）；情景剧脚本（媒介节奏不同）；纯恶搞/戏仿（本体是靶文本）；要求「保证读者笑」；现实制度咨询；纯哀伤场景（见 §8 失败出口）。

## 3. 任务路由

| 你的任务 | 先读 | 再读 | 首要输出 |
|---|---|---|---|
| 笑点归属不清 / 角色分工 | [01](references/01-partner-engines.md) C1–C5 | [03](references/03-openings-and-formats.md) C15 | 引擎配置表 |
| 讽刺方向 / 术语错位 / 宣言双版本 | [02](references/02-satire-engines.md) C6–C9、C13 | — | 引擎配置表 + 包袱调度表 |
| 开篇、形态、连作例外 | [03](references/03-openings-and-formats.md) C10–C12、C14、C16 | — | 开篇检查 |
| 机制疲劳 / 该不该继续笑 | [03](references/03-openings-and-formats.md) C12、C14 与停手边界 | [02](references/02-satire-engines.md) C7 边界 | 轮换或删除建议 |
| 来源与证据核对 | [04](references/04-source-index.md) | — | — |
| 自信过剩却缺资源／善意的反转 | [05](references/05-confidence-and-feedback.md) | [01](references/01-partner-engines.md) C3 + [03](references/03-openings-and-formats.md) C15 | 引擎配置表 + 责任与现实代价核对 |

## 4. 最短执行路径（两个门）

**G1 归属**：笑点主要由谁制造？人物搭档 → 01；叙述者或世界规则 → 02；机构/行业 → 02 的 C6/C8；没有固定归属 → 01 的 C1 否定条件，逐场标注。

**G2 距离**：这个包袱在哪里兑现？同场反转 / 换场回响 / 画外让读者独知 / 不兑现。它决定 C9 与 C11 的选择，也决定能否用「拒写」。

走完两个门再查具体规则（C1–C16），不要先选规则再找场景。

## 5. 规则索引（16 条）

| ID | 一句话断言 | 状态 | 位置 |
|---|---|---|---|
| C1 | 笑点归属不固定，不必配「理智叙述者 + 狂人搭档」 | KEEP | [01](references/01-partner-engines.md) §1 |
| C2 | 预介与行动形成期待差；信件不是开场必需品（书信体是例外） | REVISE | [01](references/01-partner-engines.md) §2 |
| C3 | 错位前提由角色认真执行，资源与旁人意愿可以让前提逐项破产（PG3829 条件例） | KEEP + 新反例 | [01](references/01-partner-engines.md) §3、[05](references/05-confidence-and-feedback.md) |
| C4 | 称谓重用需被新行动或新来源反证（机构重复或对手命名皆可） | REVISE | [01](references/01-partner-engines.md) §4 |
| C5 | 应答位可以是对白、沉默或可见行动 | KEEP | [01](references/01-partner-engines.md) §5 |
| C6 | 术语与实际情境的意义错位（含由听者补全生效的反向情形） | KEEP | [02](references/02-satire-engines.md) §1 |
| C7 | 宏大宣言与日常细节的落差，且有明确停手边界 | KEEP | [02](references/02-satire-engines.md) §2 |
| C8 | 公开宣言 / 私下行动双版本 | KEEP | [02](references/02-satire-engines.md) §3 |
| C9 | 后场兑现与知情差服从 POV | KEEP | [02](references/02-satire-engines.md) §4 |
| C10 | 开篇建立预期并随后错位（连作可继承前作预期） | REVISE | [03](references/03-openings-and-formats.md) §1 |
| C11 | 拒写/省略本身可以当包袱 | 新增 | [03](references/03-openings-and-formats.md) §2 |
| C12 | 清单升级 + 一次结算 | 新增 | [03](references/03-openings-and-formats.md) §3 |
| C13 | said/meant 的修辞间隙，由无关角色一句大白话打断 | 新增 | [02](references/02-satire-engines.md) §5 |
| C14 | 单点装置反复结算 | 新增 | [03](references/03-openings-and-formats.md) §4 |
| C15 | 帮助可能反成他人利用的工具（PG74733 / PG3184 的不同靶子），并非“善意必失败” | 保留并补反例 | [03](references/03-openings-and-formats.md) §5、[05](references/05-confidence-and-feedback.md) |
| C16 | 道德选择写成算账，不画成长曲线 | 新增 | [03](references/03-openings-and-formats.md) §6 |

## 6. 禁止项

- 本批 24 本均有 P2 全文结构覆盖门禁，但继承旧轮的批注未全部逐条语义重审；不得凭“门禁 PASS”或书名推断某种喜剧技法。
- 族去重：Twain 族内 PG7106 是 PG32325 的重刊章节，不另计证据。
- 时代敏感表述（种族、民族、性别）只能带年代注记引用，不作当代模板。
- 不得声称保证笑果；无读者数据；现代市场/付费动机等推论全部 NOT_PROVEN。
- 不得给出定量节拍（如「每 N 章换机制」「伤亡多少之后必须转严肃」）——无证据。
- 不把单部小说的情节设计升级为所有作品必须遵守的规则。

## 7. 两张最小模板

- **引擎配置表**：`章节/场景 | 笑点归属（人物/叙述者/机构/世界） | 启用机制（C1–C16） | 上场同机制? | 疲劳风险 | 兑现位置 | 待作者决定`
- **包袱调度表**：`设置（物件/称号/说法） | 兑现位置（同场/换场/画外/不兑现） | 间隔 | 结算方式（冷句/错项/拒写） | 已兑现?`

空列写「未知」，不要填空。

## 8. 失败出口

| 情况 | 能做的 | 不能做 |
|---|---|---|
| 无体裁/视角/靶子 | 给 G1 一问 + 两类备选机制（人物信念矛盾 C8 / 规则错位 C3、C6） | 不编长篇、不保笑果 |
| 机制疲劳 | 用调度表查「上场同机制」，给轮换、合并或删除方案 | 不断言几章必换 |
| 讽刺目标敏感或涉及弱势群体 | 把靶子转向虚构程序的自相矛盾，保留真实损失为严肃剧情 | 不代作者决定靶子，不嘲笑身份 |
| 纯哀伤/葬礼场景 | 不触发笑点模板，允许静默与内心细节，只检查 POV | 不强行制造笑点 |
| 要求现实制度结论 | 标 `UNRESOLVED` 并说明小说不能推断现实 | 不给具体法律/医疗/财务建议 |

## 9. 元数据与替代关系（从历史成果迁移）

- 历史 `results/manifest.yaml`：manifest_version 1、revision 1、task_id `B-04-B04`、owner_runtime `Main-02（solo）`、accepted_rounds `round-01-2026-10-25`、acceptance `static_only_gq5_not_proven`；历史产物 SHA：SKILL.md `a35ba1b2d7c4b4324a446cbcd10ab737d0dcdc6dcd0e06570b70531187ad46b9`、01 `8566af93dbb66225d4e7ae747f8b141dd65d6a02cbec6df990d11277afb62d49`、02 `b14092633c9e25d618bca955442d30eb284bf2b8258b84bfc5e87cf99ee81109`、03 `c8b1d7c7498ed3a567791b83133b99f5f221e34b98753801320163c4694d47c1`、04 `79e197397df274939784dd4c088a850479063e9b74dfc6717fe36dd606999498`。
- 本包**替代** `round-p4-wave4-agent3-final-2026-10-30/output/comic-engine-craft`（该版把 6 本不可回源的书标成 TRUSTED_FULL，已在本版更正）；不改动 `results/` 下已冻结的旧产物。
- **2026-10-31 更新**：前轮 13 本来源覆盖缺口已由 2026-10-31 台账补齐 run（workflow dwfrun-720d232d，hy3×50，一本书一个代理）全本实读关闭（13 份新台账门禁 PASS；85,742 行），wave 补证的重排台账并行保留，当前 24/24 P2 PASS。仍未验收的是 P5/GQ5 真实宿主执行与读者效果、历史语义全面独立复核及 P6/P7。

## 10. 笑点调度与误会诊断（执行要点）

1. **归类**：先判断笑点来自人物信念冲突、关系权力、语义误会、机构荒诞还是讽刺距离；若只是身份羞辱，先确认作者是否把它设定为批判而非邀请共嘲。
2. **设置**：读者先知道什么、A 以为是什么、B 实际想要什么。
3. **误会**：若依赖 A 暂时不知情，必须留出可回看的误读依据；若只是拖一句解释，缩短或另设障碍。
4. **递进**：重复包袱应在对象、代价、语气或角色主动权至少一项上改变；没有变化就减少重复（不能定死节拍）。
5. **兑现**：同场反转、跨场回响、画外独知或不兑现留白都可选；提前写收束线索，确保视角合法。
6. **停手**：出现真实伤亡、弱势群体损失或纯哀伤时，参考 PG5782 L1113-1116 与 PG32325 L4658-4659 的做法——明确刹车或明确拒写，不继续降格。

针对误会、节奏、反转、承接的实际场景表与边界输出见 [worked-example](examples/worked-example.md)。C1–C16 的动作与反例以 references 当前版为准；历史索引中的定量命令不再采用。

## 11. 1.0.1（2026-10-31）台账知识融合（第二批）

本 Skill 此前无独立 version 字段（历史 manifest 记 revision 1，视为 1.0.0 基线）；本节对应补丁版本 1.0.1，与 `agents/openai.yaml` 的 `version` 同步。**只增不删**：C1–C16 的编号、断言与既有证据全部保留，新知识一律挂在「融合补充」行或 NEW 机制条目下。

- **证据底座**：13 本历史缺口书新台账合计 151 块/291 条逐字引文，`kd32_ledger_gate.py` 逐本 PASS；[04 来源索引](references/04-source-index.md) 13 行证据性质列已改写为「全本实读、门禁 PASS（块/引文数）」。新增引文按 `sed -n 'Np' <整本阅读版.txt>` 抽核 9 条全部逐字属实。
- **01（C1–C5）**：单人肖像式双源（PG3179 L838＋PG580）与镜像双线（PG45782）；延迟视觉揭晓（PG7464 L6860）；荒诞前提＋严肃演算双源（PG3179 L1081＋PG3829）；自封称谓双源（PG3179＋PG7050）、以物证名（PG587）、口头禅复用（PG7464）；被环境催化的错误应答（PG7464 L8261-8850）。
- **02（C6–C9、C13）**：伪理性化（PG4020 L3301）、职业框架误植（PG7464）；两条降格路线双源（PG4020＋PG7464）与反向目标（PG4020 L1317）；机构级双版本（PG4020 L6829-7392）与官方身份挪用（PG45782）；群体误读物证双源（PG587＋PG3711）与长程知情差（PG3179）。**新增 §6 制度字面主义（三源：PG4249/PG4020/PG45782）与 §7 虚惊与讣告（双源：PG587/PG4020）**。
- **03（C11/C12/C14/C15）**：拒写升格为体裁承诺双源（PG3179 天气附录＋PG12793 L2559）；清单式机构讽刺双源（PG4020 L2398＋PG19851）；单词/单物升级双源（PG45782 jug＋PG19851 salvage）与结算即重启（PG3829 L6538）；C15 补两源（PG3179 L3429 施舍羞辱、PG12793 感恩熊）。**新增 §7 文件层反讽（三源：PG19851/PG12793/PG3179）**。
- **04/05**：source-index 13 行证据性质改写并记录融合入口；05 新增 PG7464《The Adventures of Sally》条件诊断（与 PG3829 双源互证，不同叙事链逐书计证）＋PG3829 phantom eggs 补充（L1327）。
- **边界不变**：时代敏感表述、不保证笑果、不推断现实制度效力、同作者不同叙事链逐书计证等禁止项全部维持。
