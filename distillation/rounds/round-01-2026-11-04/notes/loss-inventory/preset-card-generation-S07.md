# 分片丢失清单与逐条决定 · preset-card-generation（S07）

- 片名：**S07**（preset-card：合规与接口修复，**无 v0 谱系**）｜代理：Agent 4 分片执行｜轮次：**W3 主体轮第 4 批**｜日期：2026-11-05
- 依据：计划附录 A.2（九列记录格式）、附录 A.3、§2.6、第 6 节 P3 第 7 条、附录 B / C / E / F（S07 行「无 v0」）；`notes/suite-contract.md`（K2 定稿）第一节 C.1 preset-card 行、D2=A 双向两表、C.2 重叠请求表、第二节四状态词、第四节附录 B、第五节措辞禁用、第七节 C.3 第 1/2/3/5 条；`notes/slice-prep-2026-11-04.md` §3.2 preset-card 行；`notes/source-synthesis/line-editing-and-proofreading.md` 第二节（W3 统一写法口径）；`notes/loss-inventory/cross-media-drama-adaptation-S02.md` 第四节（S02 移交项）。
- 无 v0 口径：`notes/loss-inventory/raw/_summary-2026-11-04-r2.md` 明载「preset-card-generation：无 v0（不进入 7 份 raw 表）」，`raw/` 目录下无本 skill 的 r2 表文件。本片不做找回，全部决定来自合同、计划条目与基线既有内容；「来源位置」列相应写依据（合同节 / 计划条目 / 基线行），不写 v0 路径。
- 状态口径：「已写入 output」表示决定已落账、修复已写入成品。独立隔离回读按 D3-C 留 W4 由 Agent 1 另派只读子代理，本片状态不写「已回读」，不自审自过。

---

## 一、逐条决定表（九列）

| 片名 | 编号 | 来源位置（依据） | 丢失类型 | v3 现状 | 决定 | 理由 | 成品落点 | 状态 |
|---|---|---|---|---|---|---|---|---|
| S07 | LI-PC-001 | 合同第七节 C.3 第 2 条、第一节 C.1 preset-card 行、D2=A；计划 §2.6、P3 第 7 条 | 接口字段（description 兄弟名 + 触发口径） | 没有：基线 description 一个兄弟 skill 都没提，也没有「产物是卡」的接单口径 | 恢复 | C.3 第 2 条要求 description 写全会转去的兄弟 skill 名；按 D2=A 写全七个兄弟名，并写清「只接产物是给模型的卡的请求和按三轴做的诊断」 | `SKILL.md` frontmatter description | 已写入 output |
| S07 | LI-PC-002 | 合同 D2=A 转出表（七行）、C.1 preset-card 行 | 接口（转出侧转介表） | 没有：基线无「适用与转介」节、无负触发、无转介 | 恢复 | D2=A「逐条写死」；转出七行按合同原文落笔，判断依据统一为「产物是卡还是文档／文本、审查框架是否三轴」 | `SKILL.md` §1（适用／不接／转给表） | 已写入 output |
| S07 | LI-PC-003 | 合同 D2=A 接收表（五行）、C.2；S02 记录第四节移交项「preset-card 的 SKILL.md 转介（兄弟侧接收行）归 S07 落地」 | 接口（接收侧表，接 S02 移交） | 没有：基线无接收侧 | 恢复 | 接收五行按合同原文；第 2 行写明含「把改编方案中的推进安排或表达约束写成卡」，接住 cross-media §12.2 的转介 | `SKILL.md` §9.2 | 已写入 output |
| S07 | LI-PC-004 | 合同 C.2 重叠请求表（与 preset-card 相关的四行）；slice-prep §3.2「与 fiction-planning / story-architecture / line-editing 重叠」 | 接口（重叠收敛判断依据行） | 没有：基线任务入口把规划、写章、改稿、审稿全收在自家 | 恢复 | C.2 要求相关行写进各自 SKILL.md；按「产物是规划文档还是卡、是改好的文本还是卡、有无卡作输入、审查框架」四条判断依据写清 | `SKILL.md` §9.1（四行表）、§2 表后收口句 | 已写入 output |
| S07 | LI-PC-005 | 合同 D2=A「只负责预设卡和三轴诊断」、C.1 行 | 接口（任务入口收敛） | 部分：基线 8 行任务入口中 4 行（开新书规划分卷排章纲、写章节、改稿润色、一般审稿）按 D2=A 不再是本 skill 的交付 | 合并 | 任务入口收敛为「生成／诊断卡、把规划结构文风表达写成卡、三轴审章、按已有卡写章」；planning.md 开头与交付节同步改写为「写成卡的小节素材」，规划文档交付写明转出；writing.md、revision.md、style.md 的方法本体保留（是「按已有卡写章」接收行与「改前改后」示范的支撑内容） | `SKILL.md` §2、§3；`references/planning.md` 开头、交付节 | 已写入 output |
| S07 | LI-PC-006 | R18 §3；计划 §2.6「路由表都缺两列」；合同 C.3 第 3 条 | 接口（路由表两列） | 没有：基线「参考资料」是一列清单，无补读与出口列 | 恢复 | 9 个 reference 各一行，加「需要时补读／缺料或冲突时的出口」两列；出口行与 §8 失败出口一致 | `SKILL.md` §6 参考文件表（9 行 × 4 列） | 已写入 output |
| S07 | LI-PC-007 | 合同 C.3 第 3 条；slice-prep §3.2「SKILL.md 没有失败出口」；cross-media §11 先例（S02 LI-CM-010） | 接口（失败出口节） | 没有 | 恢复 | 八类情形×出口：缺样文（PC-T2）、只有梗概、锁定冲突（PC-T3）、版本基准不明、卡内冲突未裁决、作者不答、产物不是卡、三项全缺改交问题清单；附「未经生成测试不作保证」收口 | `SKILL.md` §8 | 已写入 output |
| S07 | LI-PC-008 | R18 §2d 末段（计划 P3 第 7 条转述）；合同 C.3 第 3 条；附录 E `PC-T3` | 接口（卡片版本与锁定内容冲突出口） | 没有：基线只在通用原则里有「保留用户的设定」，没有冲突出口 | 恢复 | 已锁定的卡与新约束冲突时不擅自覆盖：列冲突条款与受影响范围、交作者裁决、裁决前两版都不落稿；另补版本基准不明的出口 | `SKILL.md` §8 第 3、4 行 | 已写入 output |
| S07 | LI-PC-009 | 计划 P3 第 7 条「补负触发」；合同 C.3 第 5 条；附录 E `PC-T4` | 接口（负触发行） | 没有 | 恢复 | 负触发含「给图片生成模型、视频模型写提示词卡（不是小说）判负触发」（PC-T4）与「产物不是卡也不用三轴」两条；不自创其余负触发 | `SKILL.md` §1「不接」清单 | 已写入 output |
| S07 | LI-PC-010 | 计划 P3 第 7 条「补 agents/openai.yaml，设 allow_implicit_invocation: false」；slice-prep §3.2；合同 C.3 第 5 条 | 接口文件（缺失） | 没有：基线无 agents/ 目录 | 恢复 | 按四个完工包的 yaml 格式新建：interface 三字段 + policy.allow_implicit_invocation: false；short_description 与 default_prompt 写清「只接产物是给模型用的卡或按三轴做的诊断」「锁定内容冲突不擅自覆盖」 | `agents/openai.yaml`（新建） | 已写入 output |
| S07 | LI-PC-011 | 合同第二节 2.1 四词、2.2 对照表；S02 LI-CM-004 先例 | 接口（交付状态词节） | 没有：基线「输出约定」只有「未经实际生成测试的效果不作保证」 | 恢复 | 四词表照合同第二节；并写明四词在本 skill 的落法（格式字数核对记已完成、生成效果未经测试记未能核实、取舍记待作者决定） | `SKILL.md` §7 | 已写入 output |
| S07 | LI-PC-012 | 合同第一节 D2=A「保留」段；基线 SKILL.md 各节 | 结构（SKILL.md 全文重排） | 部分：基线有规划／写章节／改稿与审稿／预设卡四节，按 D2=A 需重排为卡片与三轴两条主线 | 合并 | 保留基线的通用原则七条、交付前检查两组、输出约定四条；新增 §3 最短路径四入口（生成卡、三轴审章、按卡写章、设计推进七步）；「分析过程、缺陷标识、来源不写入成品」改为「分析过程与缺陷归类不写入成品」；补 metadata version/language（对齐完工包格式） | `SKILL.md` 全文 | 已写入 output |
| S07 | LI-PC-013 | 计划 P3 第 7 条「保留『冒号后不反转』」；基线 SKILL.md 预设卡步骤 5、card-method.md §7 | 规则本体（既有） | 已有：两处都在 | 不恢复（原样保留） | P3 第 7 条明令保留；本次只在 SKILL.md 重排中保位，规则文字不改 | `SKILL.md` §3 步骤 5；`references/card-method.md` §7 | 已写入 output |
| S07 | LI-PC-014 | 计划 P3 第 7 条「保留『示例原创』」；基线通用原则 6 | 规则本体（既有） | 已有 | 不恢复（原样保留） | 同上 | `SKILL.md` §4 第 6 条 | 已写入 output |
| S07 | LI-PC-015 | r2 汇总「preset-card-generation：无 v0（不进入 7 份 raw 表）」；raw/ 目录核对；计划附录 F S07 行「无 v0」 | 谱系核对 | 无 v0 谱系单元，raw 表不存在 | 不恢复（登记） | 如实登记：本片无找回项，无单元→决定覆盖对照表可做；基线内容全部按合同与红线处理，不引入 v0 材料 | 无（登记于本表与本记录开头） | 已写入 output |
| S07 | LI-PC-016 | 红线（来源编号残片、指向学习材料的说法、借来源背书）；合同 B.3 第 3 条；S01 校准样例 §0/§5 | 来源残留（整文件级） | 残留：`card-pitfalls.md` 全文 22 条缺陷挂在「对比评测高分卡评语」框架上，23 处〔推进/NNN 题材〕类来源卡编号、命中次数统计、「评语认可的写法」背书语、「原记录的来源路径与内容不符，未能回源」过程语 | 合并 | 保留缺陷本体（病灶示例、成因、自查、改法、边界）与缺陷标识，删引用框架：评分档词改中性称谓（高分卡→写得好的卡等）、命中次数删、评语引用改写为直接症状描述、评测过程语（全批／本轮／其余九份／未能回源）删、「评语的取舍」改「冲突批评的裁定顺序」并去评测框架 | `references/card-pitfalls.md` 全文 | 已写入 output |
| S07 | LI-PC-017 | 同 LI-PC-016 依据 | 来源残留（整文件级） | 残留：`card-method.md` 15 处〔来源卡〕引用、「来自对比评测中高分卡的共同做法」「文中「」内是评语原话」框架、「评语认可的写法」块、§8「评语中的写法」表头 | 合并 | 主干方法七节与条件化做法表全部保留；引用改写为「写法示意」直接陈述；「单一来源支持」改「依据尚单薄」；「本节来自作者的直接要求，没有评测数据支持」删（保留读者前提的诚实声明「尚未经过本 Skill 的生成测试验证」） | `references/card-method.md` 全文 | 已写入 output |
| S07 | LI-PC-018 | 同上；另基线 SKILL.md 通用原则 6「不使用真实作品的原文、人物和名句」；合同 B.3 第 2 条 | 来源残留（文件级 + 真实名句） | 残留：`card-diagnosis.md` 「评语原话」「高分卡／中段卡／低分卡」框架、「在历史记录中出现的次数」；第二部分 `scope.real-name-or-ip-borrow` 行引用真实作品名句「剑气纵横三万里，一剑光寒十九洲」 | 合并 | 五类根因、交付前检查、缺陷目录、审校步骤全部保留；评分档词改中性称谓；真实名句删去、症状改为「直接搬现成的名句当标准」（本 skill 自己的规则就禁止名句）；「同批其他卡片」改「同一组内其他卡片」 | `references/card-diagnosis.md` 全文 | 已写入 output |
| S07 | LI-PC-019 | 同 LI-PC-016 依据 | 来源残留（散布） | 残留：`planning.md` 3 处、`progression.md` 7 处、`style.md` 5 处、`expression.md` 1 处「评测／评语认可的写法／〔来源卡〕」 | 合并 | 引文内容是通用写法示意，去引用框架后并入正文（例如「四种可验收结果」「开局拆到章级」直接成句）；「评测所用格式」改「下面的默认格式」（三处）；「排名第一的文风卡也有约一半示例违规」改为不借排名的表述 | 四个文件对应行 | 已写入 output |
| S07 | LI-PC-020 | 合同 B.1 #4 扫描命中；S01 校准 §5「顺手消除类命中」 | 误报消除 | 残留：「整句搬到别的书里照样成立」3 处命中 #4 的「书里」子串（泛指用法，非指向学习材料） | 合并 | 改为「别的作品」，语义不变，#4 该子串归零；「说出／认出自己的情绪」4 处「出自」子串误报读原句判允许、不改坏语义 | `expression.md` 病灶表、`card-pitfalls.md` 第 10 条、`card-method.md` §2 条件表 | 已写入 output |
| S07 | LI-PC-021 | 合同 B.2 第 3 条「本包内部编号」允许保留 | 编号判断 | 缺陷标识（`specificity.*` 等点分标识）在 card-pitfalls 与 card-diagnosis 间互查、审校归组用 | 不恢复（保留） | 标识是包内缺陷目录编号，不指向包外来源；删除会断开两文件互查与「审校一组卡片」的归组功能；命中次数已删，标识脱离来源统计 | 两文件的缺陷标识 | 已写入 output |
| S07 | LI-PC-022 | 合同 D2=A 按「请求与产物」定 Owner，不要求删参考内容；expression.md「写成卡」结构第 4 项要求改前改后示范 | 内容取舍 | writing.md、revision.md 含改稿与写正文的完整方法 | 不恢复（保留） | 这些方法是「按已有卡写这一章」（接收行 5）、「表达约束卡给改前改后示范」的支撑内容；Owner 收敛落在 SKILL.md 的入口与转介上，不删参考本体；两文件本轮无来源残留、未改写 | `references/writing.md`、`references/revision.md` | 已写入 output |
| S07 | LI-PC-023 | 合同第四节 B.1 全 11 类、B.2、B.3；计划 P3 第 3 条 | 去来源自检 | 见 `notes/quality/preset-card-generation/s07-desourcing-selfcheck.md` | 合并 | 全 11 类 `/usr/bin/grep -rnE` 复扫 + B.3 逐文件回读；结果摘要在本记录第三节 | 自检文件 | 已写入 output |
| S07 | LI-PC-024 | slice 口径第 9 条；S02 记录移交口径；合同 C.3 第 2 条「另 7 个 skill 都没提到 preset-card」 | 跨片接口（兄弟 description 缺口） | 缺口在七个兄弟包的 description / 转介节 | 不恢复（移交） | 兄弟 skill 是否提 preset-card 属各兄弟分片范围，本片不改他人 output；已完工四包（cross-media、scene、line-editing、character）的 description 均已含本 skill 名（cross-media §12.2 有双向转介、scene §1 有负触发行），缺漏在未完工四包（fiction-planning、story-architecture、genre、以及 G00 汇总），列移交项回报主代理 | 无（本片不改他人文件） | 移交 |

**决定计数**：恢复 10 条（LI-PC-001 至 004、006 至 011）、合并 9 条（005、012、016 至 020、023）、不恢复 5 条（013、014、015、021、022）、移交 1 条（024），合计 **24 条决定**。无 v0 谱系单元，故无 r2 单元覆盖对照表（见 LI-PC-015）。

---

## 二、W3 派发口径逐项落账

| 派发口径（slice 口径 9 项） | 落账 |
|---|---|
| 1. 建包：复制基线为 output 包，确认基线无 agents/templates/examples | 已建：`output/preset-card-generation/`＝SKILL.md + 9 个 references；基线确无 agents/templates/examples（`skills/preset-card-generation/` 仅两文件、references 9 文件），agents/ 为本片新建 |
| 2. agents/openai.yaml 补建 | LI-PC-010 |
| 3. SKILL.md 失败出口 | LI-PC-007 |
| 4. 卡片版本与锁定内容冲突出口（R18 §2d、合同第七节第 3 条、PC-T3） | LI-PC-008 |
| 5. 路由表两列 | LI-PC-006 |
| 6. description 与「适用与转介」双向两表（接 S02 移交） | LI-PC-001、002、003、004 |
| 7. 负触发行（PC-T4）+ 保留两条既有规则 | LI-PC-009、013、014 |
| 8. 重叠收敛（fiction-planning / story-architecture / line-editing） | LI-PC-004、005 |
| 9. 兄弟 skill description 是否提及本片（不改他人文件） | LI-PC-024，移交 |

---

## 三、附录 B 摘要（详见 selfcheck）

- 终扫：#1、#2、#3、#5、#6、#7、#8、#9、#11 九类零命中；#4 命中 4 条（全部为「说出／认出自己的」中「出自」子串的固有误报，判允许）；#10 命中 12 行 15 子串（「判据，」「依据。」「看见。」「与同位替代」「与同一组内」等正常词误报，判允许）。**违规 0。**
- 初扫（改写前基线）真命中已全部改写消除：56 处〔来源卡〕引用、23 处评测/评语框架词、12 处评分档词、1 处真实作品名句、3 处「别的书里」。B.1 正则未覆盖的〔推进/NNN〕类编号残片与评测框架按 B.3 人工判断处理。

---

## 四、本片断点（供 Agent 1 下一轮统一追加 `log.md`）

- 片名：**S07**
- 处理到的编号：**LI-PC-001 至 LI-PC-024**（24 条决定：恢复 10、合并 9、不恢复 5、移交 1）
- 下一步：决策链在 `notes/source-synthesis/preset-card-generation.md`；附录 B 摘要交 Agent 1 汇总进 `desourcing-ledger.md`；`notes/quality/preset-card-generation/` 下 `brief.json`、`review.json` 为 W4 冻结物，本片未改动；独立隔离回读与 GQ1–GQ4 按 D3-C 留 W4。
- 移交项：见第五节。

## 五、跨片移交项

1. **未完工四包的 description / 转介缺口**（归各兄弟分片与 G00）：fiction-planning-and-diagnosis、story-architecture-and-longform-planning、genre-fiction-craft 的 output 包尚未产出，其 description 未提 `preset-card-generation`；G00（genre SKILL.md 定稿）涉及转介时按 D2=A 补「题材规则归 genre、写成卡归 preset-card」的判断依据行。
2. **已完工四包无需返工**：cross-media（§12.2 双向 + §11 出口行）、scene（§1 负触发行 + 转给表末行）、line-editing、character 的 description 均已写全本 skill 名；本片接收表已与其转出侧逐行对上（S02 移交已接住，见 LI-PC-003）。
