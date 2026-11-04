# 当前任务与来源索引

当前执行入口是fused-rules.md、knowledge-details.md、historical-boundaries.md、workflow.md、templates.md和examples.md。source-identities.md/json独立承接129个任务来源条目的书名、责任者、原PG行锚及元数据证据。

| 任务 | 当前知识/例材 | 原Skill基线 |
|---|---|---|
| B-03-B01 | K001–K022、K158–K160；E01 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft` |
| B-03-B02 | K023–K044、K161/K166；E02–E03 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft` |
| B-03-B03 | K045–K062、K164–K165；E04–E05 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc` |
| B-03-B04 | K063–K089、K162；POV/资源/结局分支 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost` |
| B-03-B05 | K090–K111、K163；E11 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft` |
| B-03-B06 | K112–K136、HB01–HB37；E06–E10 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06` |
| B-03-B07 | K137–K157；E12–E14 | `distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07` |

## 追溯的边界

rule-evidence.json逐规则给源Skill文件、SHA和原行；microcard-evidence.json逐K卡保留来源；historical-counterexample-evidence.json逐HB保留旧反例；decision-log.json按对象/条件/动作/限制/结果记录裁决。file-map.json逐旧文件映射到当前知识/模板/例材/身份与原字节存档。reading-ledger.json仅认证源Skill实读范围。

[包内隔离来源说明](../../provenance/source-snapshots/02-言情爱情/README.md)指向details中的旧包展开和raw中的原始字节；它们用于历史追溯，不能当“当前完整细节”或现行步骤。[逐文件映射](file-map.json)给出各原稿的实际存放路径，复制本Skill时须一并保留本包provenance目录。古书全读与效果认证的缺口见historical-boundaries.md，不继承原PASS。
