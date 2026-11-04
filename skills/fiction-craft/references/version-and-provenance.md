# 版本、来源和使用边界

- **版本关系**：当前为 2026-10-30 P4 实质返工候选；基线 Skill 的 version 为 `1.0.0`，并非已发布的新语义版本。
- **基线元数据（原样迁移）**：language=zh-CN；evidence=28 works; declared span 1808–1929, bulk 1888–1928 English-language craft books, drama and short-story manuals, plus classical poetics and Chinese classical criticism；status=static-delivery; real tasks NOT_RUN; effects NOT_PROVEN.
- **来源总数**：28（按 A-02 任务清单 PG ID）。本轮逐本重新验 SHA，28/28 匹配。
- **P2 证据口径**：28/28 来源有可核读段区间及细节记录；索引末段不以缺少具体情节引文为由误判缺读。仍不等于本轮重读全书。
- **来源类型**：M（方法）/ C（评论）/ FC（小说案例）/ R（索引）区分；小说事实 F 不直接等于创作通则，跨作品规则是 H/建议 P。
- **许可证与使用约束**：旧 frontmatter 没有声明可继承的 license；此处不虚构授权。仅提供最低限度短引、PG/行号及来源索引，不重新分发原著全文。
- **测试状态**：历史 real tasks NOT_RUN、effects NOT_PROVEN；本轮仅修正规则、原文回读与静态验证，P5/GQ5 NOT_PROVEN；P6/P7 NOT_DONE。
- **规则权威**：`references/rules.md` 为 RC-01...21 唯一权威；`p4-field-guide.md` 为索引，不可推翻 RC。

## 来源作用总览（不以出现次数代替支持）

| PG | 阅读台账 | 关键规则引用 | 来源角色 |
|---|---|---|---|
| PG10865 | TRUSTED_FULL | RC-06, RC-08, RC-12, RC-13 | 支持/限定/反例在各 RC 逐条核对 |
| PG12743 | TRUSTED_FULL | RC-13 | 支持/限定/反例在各 RC 逐条核对 |
| PG13589 | TRUSTED_FULL | RC-09, RC-12, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG15383 | TRUSTED_FULL | - | 本轮未在核心 RC 锚点使用；只作语料背景，不充当多源共识 |
| PG17470 | TRUSTED_FULL | RC-15, RC-17 | 支持/限定/反例在各 RC 逐条核对 |
| PG1974 | TRUSTED_FULL | RC-03, RC-05, RC-10, RC-13 | 支持/限定/反例在各 RC 逐条核对 |
| PG20526 | TRUSTED_FULL | RC-08, RC-09, RC-10, RC-12, RC-13, RC-15, RC-16, RC-17, RC-18, RC-19, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
| PG21964 | TRUSTED_FULL | RC-03, RC-09 | 支持/限定/反例在各 RC 逐条核对 |
| PG23822 | TRUSTED_FULL | RC-13, RC-15, RC-16, RC-17, RC-18, RC-19 | 支持/限定/反例在各 RC 逐条核对 |
| PG25471 | TRUSTED_FULL | RC-01, RC-06, RC-08, RC-10, RC-17, RC-18 | 支持/限定/反例在各 RC 逐条核对 |
| PG27224 | TRUSTED_FULL | RC-02, RC-14, RC-15, RC-16 | 支持/限定/反例在各 RC 逐条核对 |
| PG30776 | TRUSTED_FULL | RC-01, RC-02, RC-03, RC-04, RC-06, RC-08, RC-11, RC-14 | 支持/限定/反例在各 RC 逐条核对 |
| PG32092 | TRUSTED_FULL | RC-03, RC-05, RC-06, RC-07, RC-11, RC-14, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
| PG3250 | TRUSTED_FULL | - | 本轮未在核心 RC 锚点使用；只作语料背景，不充当多源共识 |
| PG36580 | TRUSTED_FULL | RC-01, RC-05 | 支持/限定/反例在各 RC 逐条核对 |
| PG38887 | TRUSTED_FULL | RC-04, RC-11, RC-15 | 支持/限定/反例在各 RC 逐条核对 |
| PG492 | TRUSTED_FULL | RC-02, RC-03, RC-04, RC-15, RC-17, RC-18, RC-19 | 支持/限定/反例在各 RC 逐条核对 |
| PG58471 | TRUSTED_FULL | RC-03, RC-05, RC-12, RC-14, RC-19, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG61340 | TRUSTED_FULL | - | 本轮未在核心 RC 锚点使用；只作语料背景，不充当多源共识 |
| PG61625 | TRUSTED_FULL | RC-02, RC-04, RC-05, RC-07, RC-08, RC-11, RC-14, RC-17, RC-18, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
| PG64210 | TRUSTED_FULL | RC-01, RC-03, RC-04, RC-10, RC-12, RC-13, RC-15, RC-16, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG66600 | TRUSTED_FULL | RC-12, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG68291 | TRUSTED_FULL | RC-02, RC-03, RC-10, RC-13, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG70492 | TRUSTED_FULL | RC-05, RC-08, RC-10, RC-11, RC-16, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
| PG72446 | TRUSTED_FULL | RC-01, RC-02, RC-04, RC-05, RC-07, RC-08, RC-09, RC-10, RC-11, RC-14, RC-16, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
| PG72910 | TRUSTED_FULL | RC-04, RC-14, RC-18, RC-19 | 支持/限定/反例在各 RC 逐条核对 |
| PG76688 | TRUSTED_FULL | RC-09, RC-12, RC-13, RC-16, RC-20 | 支持/限定/反例在各 RC 逐条核对 |
| PG78424 | TRUSTED_FULL | RC-09, RC-11, RC-19, RC-21 | 支持/限定/反例在各 RC 逐条核对 |
