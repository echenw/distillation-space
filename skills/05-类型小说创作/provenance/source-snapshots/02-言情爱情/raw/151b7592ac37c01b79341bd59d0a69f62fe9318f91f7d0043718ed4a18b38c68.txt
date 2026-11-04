# 来源索引 · 19 本固定 PG 原件与读取证据

来源角色为小说个案 `FICTION_CASE`，不是写作技巧公理或现代关系心理学。`RANGE_COVERED` 意为已有台账范围并集从 L1 到 EOF；不能等同本轮真人重新逐字阅读，且可能包含老轮次的未独立认证内容。

本轮（round-p4-final-2026-10-30）更新：

- 阅读版 SHA-256 全部重新计算（`hashlib.sha256` 遍历 `distill/有原始正文/16-类型小说专项/02-言情爱情/<PG>-<书名>/整本阅读版.txt`），并在此表给出完整 64 位值；与上一版索引的短前缀一致。
- **PG3321 是本轮唯一亲自实读并按块回源的来源**：L1–11484，12 份补充台账，逐份 `kd32_ledger_gate.py` 自检 PASS。历史 `PG3321.ledger.md`（round-02，L1-4209）被同一门禁判为 FABRICATED，保留但不计入证据。
- 其余 18 本为继承台账：本轮只核对存在性、区间并集与 SHA 身份，**未逐条复核其引文行号**，引用时按"继承定位、未复核"处理。

## 逐本清单（19/19）

| PG ID | 阅读版目录名 | 行数 | 阅读版 SHA-256 |
|---|---|---:|---|
| PG158 | Emma | 16489 | `4ae98d6e56b57e5a3e7a3b9dbc344590aa6b7db7c05e08874885eb5131ad853d` |
| PG524 | Ann-Veronica-A-Modern-Love-Story | 12109 | `600e54136ba4e8e986c8775bb2b0c56212f3c308f426a9306e2e24733c78f11e` |
| PG619 | The-Warden | 7580 | `205b18b0bdcd686ab0c3929a47b93cc53a0e2a881d0b2c45caf7216f9f54f45c` |
| PG1023 | Bleak-House | 39837 | `f5a63bc64af664bb555a3cf8c2804e1d2b612cc07d898d567a1d5aa8e83edd85` |
| PG1263 | The-Glimpses-of-the-Moon | 9181 | `91e7d8106fe4f19ca8493d33e16fabe16b850f05715e31f9fd0edb5710ddb959` |
| PG1342 | Pride-and-Prejudice | 14529 | `595bb39fe77d98088ca138ae83602734e18733d3f32b16f45b717721beb1c9fb` |
| PG1671 | When-a-Man-Marries | 6266 | `989f4d47d72d257290952b19e0bc5516c8b135e436d88d16939be2260eff27f1` |
| PG3321 | Children-of-the-Whirlwind | 11484 | `6a1fbc8570ff0d7a2316a2ea76d19358bd4c92f724089d9d0a2e6c9c7cd8c866` |
| PG3404 | April-Hopes | 13487 | `aba68d846684517edb7daf29086791a74b8013b50fd94ced61d7cbe307694138` |
| PG3699 | Miss-Sarah-Jack-of-Spanish-Town-Jamaica | 1037 | `626b409615ffd02ae519bb59f7ed805ec440011b67bcd3ffaf188d90675d40df` |
| PG3700 | The-Courtship-of-Susan-Bell | 1317 | `d7f6b01a45c3931156997068bcd1cf526581678170cec66e5b2f389af2035e2e` |
| PG4917 | The-Kellys-and-the-O-Kellys | 19348 | `fbcb79069a4b147914fcfab9baf80c1f50c913c5779f2fe348ca33ce158dd885` |
| PG12234 | Mr-Scarborough-s-Family | 22509 | `1484dace6fd564e32ebb122ff6df5277697ee7f76900d67d2253659d7568d935` |
| PG27712 | Sir-Harry-Hotspur-of-Humblethwaite | 7689 | `262f28c1e73ac0ee70d49a8e1c1aafd0dbd69725416e3ffc7114fe1fddeeb447` |
| PG35538 | The-Squatter-and-the-Don-A-Novel-Descriptive-of-Contemporary | 16337 | `c6ab6e32ccfe4df96ae38ba980c71da28aaecbc7b681e8da9119387494d9c0e2` |
| PG54010 | The-Younger-Sister-A-Novel-Vol-I | 5471 | `b17bec60a40e3cc4dee0260043467e4847fefdc4ef83f5faa51beff0acc26a50` |
| PG54011 | The-Younger-Sister-A-Novel-Vol-II | 7742 | `a5f7fa4166ae64b8717b16a7f69146a754b6e2bb3aaed5574421dbd9b5b4528f` |
| PG54012 | The-Younger-Sister-A-Novel-Vol-III | 9047 | `2ba8653e446b44f5cf44ba7fd5e69ab25fa21295bde51512fe15068a08de0dbb` |
| PG68222 | His-fortunate-Grace | 3903 | `6f46934dfeaeff0402ceffbb171f17b09a5299d0d143e98d7785e16d8132745c` |

合计 19 份、225,362 行（本轮 `splitlines()` 统计口径）。

## 证据族去重（19 本 ≠ 19 个独立证据）

| 证据族 | 成员 | 是否本轮实读 |
|---|---|---|
| Austen | PG1342、PG158 | 否（继承） |
| Trollope | PG619、PG12234、PG4917、PG27712、PG3699、PG3700 | 否（继承） |
| Hubback 续书三卷 | PG54010、PG54011、PG54012 | 否（继承） |
| Leroy Scott | PG3321 | **是（本轮 L1–11484）** |
| Dickens | PG1023 | 否（继承，本轮未取得行级证据 → 未证明） |
| Wharton | PG1263 | 否（继承） |
| Ruiz de Burton | PG35538 | 否（继承） |
| Howells | PG3404 | 否（继承） |
| Wells | PG524 | 否（继承） |
| Rinehart | PG1671 | 否（继承，本轮未取得行级证据 → 未证明） |
| Atherton | PG68222 | 否（继承，仅形态参照） |

## 重点规则引用定位

- R1–R6：PG1342 L7505–7951、L13673–13807（继承定位）；同族反例 PG158 L673–946。**本轮新增**：PG3321 L1247-1257（改邪归正的生意账）、L2246-2259（权力方交易）、L2431-2458（标签制造）、L3367-3398（假信误导）、L6023-6033（以礼相待）、L6998-7004（坦白被截断）、L7817-7823（当面摊牌）、L10292-10371（制造者自述）。
- R7–R9：PG619 L472–530、L525–526、L2565–2570、L7285–7330；跨族差异 PG1263 L101–176、PG35538 L771–773/L1797–1836（继承定位）。**本轮新增**：PG3321 L5174-5208（婚姻计价）、L7596-7599（私下递话）、L7964-7983（可核威慑夺械）、L8257-8266（筹码控制）、L11036-11055（权威公开倒向）、L11118-11138（按社会后果重算起诉）。
- R10：PG54010 L28–35/L57–161；同族后卷 PG54011 L50–266、PG54012 L33–43（继承定位）。PG3321 不提供续作证据。
- 自主权边界：PG524 L2358–2409（继承定位）；不是 2026 年法律或心理临床权威。
- 不告知与归属判断（本轮新增）：PG3321 L5951-5983、L8407-8409、L8549-8550、L8962-8969。

## 阅读与授权边界

- 原始来源为该工作区固定 Gutenberg 文件及对应 metadata。逐文件完整 64 位 SHA 与 19 本 L1→EOF 区间在本轮 `notes/source-coverage.md` 与本文件保存，不将其作为消费者必须访问的外部依赖。
- 某些旧卡片仍标 `SCAN/FAM/UNREAD`，反映旧轮次的当时取样；不得把这些历史口径当作本次最终阅读范围，也不能拿新范围替代可信语义复核。
- 同作者多本、续书同一作品族只算一个独立证据族。
- 原书元数据中的 USA public-domain 或其他许可陈述只限对应版本与管辖区，不授予其他译本/影印本再发行权；本 Skill 仅包含短定位及原创方法。
- 本包不夹带原著完整文本；阅读版行号不是印刷版页码，外部原件须重新核实。
