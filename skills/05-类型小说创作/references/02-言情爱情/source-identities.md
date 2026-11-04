# 逐书身份、责任者与当前PG定位

逐书标题/责任者来自已完整读取的源Skill元数据，保留作者、译者、绘者、合集贡献者、母作与续作区别。NOT_DECLARED不猜补。FULL、SHA_MATCH、TRUSTED_FULL和历史台账是上游声明，不是本次原PG全书复验。PG SHA与源Skill SHA分别保存；短前缀不扩写。生产者实际回读11个PG，Main集成追加4个PG书头及其中2份归档元数据，合计15个PG有指定范围回读；范围见historical-boundaries.md与verification/。

全部身份字段的原文件、原行、SHA及历史变体在source-identities.json；旧字节另由file-map.json追溯，当前使用不依赖原执行包。原表中的未署名、旧作者归属与PASS保留为历史字段，现行身份以本文件主表及current_correction为准。

## B-03-B01

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG11640 | Love and Mr. Lewisham | Wells | 8376 | SHA256前16位 ce1ddcaebae6d1c6 | K018, K019 |
| PG13180 | The Tracer of Lost Persons | Chambers（源Skill署名；本次窗口不包含书头） | 7576 | SHA256 6073dd82c19244b329324367cf26075ccc981fc228a2313d9e606475ed2f6bd9 | K020 |
| PG15252 | Victorian Short Stories: Stories of Successful Marriages | 五篇合集：Elizabeth Gaskell / Thomas Hardy / George Moore / Walter Besant / Henry James | 4045 | SHA256 64d4911d537a05fec4d75565395d6d469b11d883e4452362231bb593e2500526 | K016, K020 |
| PG15473 | Love Stories | Rinehart | 9318 | SHA256前16位 d57013c49d4a92ea | K012, K020 |
| PG15766 | The Claverings | Trollope | 22228 | SHA256前16位 0b6d75946d978392 | K001, K008, K017 |
| PG1839 | Other Things Being Equal | Wolf | 8478 | SHA256前16位 462571947a21e43d | K018, K019 |
| PG1917 | The Queen of Hearts | Collins 合集 | 14905 | SHA256前16位 c06cdd297e87b9dd | K007, K016 |
| PG20533 | Jill the Reckless | Wodehouse | 14973 | SHA256前16位 20e67cbcb6c8957b | K006, K012, K021, K022 |
| PG21847 | Dr. Wortle's School | Trollope | 8385 | SHA256前16位 9d978bb4a653bbc7 | K008, K015, K160 |
| PG3719 | The Mistletoe Bough | Trollope | 1004 | SHA256前16位 3cfaf3045a2ca868 | K001, K006, K158 |
| PG3724 | The House of Heine Brothers | Trollope | 1076 | SHA256前16位 75328934279e6e89 | K001, K004, K008, K159 |
| PG4275 | Ruth | Gaskell | 17036 | SHA256前16位 c7a856420ae97fd7 | K009, K014, K159 |
| PG4398 | The Tides of Barnegat | F. H. Smith | 10608 | SHA256前16位 06876badecd4a7fe | K009, K014, K018, K022 |
| PG471 | The Bride of Lammermoor | Scott | 13556 | SHA256前16位 891fe7f89df8e6d3 | K002, K003, K006, K013, K016, K022 |
| PG49282 | The Chronicles of the Imp | Farnol | 5796 | SHA256前16位 88f25d660ced79c9 | K005, K006, K021, K022 |
| PG4961 | Our Mr. Wrenn | S. Lewis | 9629 | SHA256前16位 98b2563ff62958ad | K019 |
| PG68273 | Love's Bitterest Cup | Southworth | 12401 | SHA256前16位 068df2b8df1afb34 | K010, K015, K021, K022 |
| PG821 | Dombey and Son | Dickens | 39707 | SHA256前16位 30fbb4b4d653d6f8 | K001, K002, K004, K011, K017, K022 |
| PG969 | The Tenant of Wildfell Hall | A. Brontë | 18477 | SHA256前16位 c240eef53537a997 | K008, K010, K011, K017, K159 |

### 当前锚点及来源元数据证据

**PG11640**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K018：PG1839 L8249–8251；PG4398 L5289–5290；PG11640 L7928–7929/L8218–8259。
- K019：PG1839 L5996–5998/L109–159；PG4961 L3371/L9335–9337；PG11640 L3840–3842。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L24；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG13180**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：数字替换与单词分割是两步，Tracer帮助分词；理解告白不等于回应。 实读范围：L2998–3045。

- K020：PG13180 实核L2998–3045，数字L3012–3013/替换L3018–3020/串L3027/分词L3036–3038；PG15252 L901–903；PG15473 L1371。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L25；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG15252**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：五篇分别为The Manchester Marriage、A Mere Interlude、A Faithful Heart、The Solid Gold Reef Company Limited、The Tree of Knowledge；L29 Christmas1858仅第一篇刊载信息，不是合集出版年。 实读范围：L1–80，目录逐篇署名L12–20。

- K016：PG1917 L11952–11999；PG15252 L2440–2442；PG471 L12443–12446。
- K020：PG13180 实核L2998–3045，数字L3012–3013/替换L3018–3020/串L3027/分词L3036–3038；PG15252 L901–903；PG15473 L1371。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L26；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG15473**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K012：PG15473 L6934–7197；PG20533 L10546–10639。
- K020：PG13180 实核L2998–3045，数字L3012–3013/替换L3018–3020/串L3027/分词L3036–3038；PG15252 L901–903；PG15473 L1371。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L27；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG15766**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K001：PG3724 L816–817；PG15766 L327–330；PG821 L18245–18249；PG3719 L599–601。
- K008：PG3724 L982/L883–901；PG969 L15034–15036；PG21847 L6231–6779；PG15766 L826–827。
- K017：PG969 L17843–17860；PG821 L37389–37393/L37862–37883；PG15766 L9564–9573/L5430–5431。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L28；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG1839**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K018：PG1839 L8249–8251；PG4398 L5289–5290；PG11640 L7928–7929/L8218–8259。
- K019：PG1839 L5996–5998/L109–159；PG4961 L3371/L9335–9337；PG11640 L3840–3842。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L17；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG1917**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K007：PG1917 L9759–9760；匿名指控L10561–10564，新闻窗口L9501–10000。
- K016：PG1917 L11952–11999；PG15252 L2440–2442；PG471 L12443–12446。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L18；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG20533**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K006：PG49282 L5128–5133；PG3719 L386–388；PG20533 L14234–14258；PG471 L11270–11274。
- K012：PG15473 L6934–7197；PG20533 L10546–10639。
- K021：PG20533 L13839–13854/L12762–12763；PG49282 L1779–1780；PG68273（走私/地牢，来源未单列精确行）。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L29；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG21847**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K008：PG3724 L982/L883–901；PG969 L15034–15036；PG21847 L6231–6779；PG15766 L826–827。
- K015：PG21847 L6780–7245/L7246–7753；PG68273 L6168–6172/L4727–4730。
- K160：PG21847 L1709–1714。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L30；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG3719**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K001：PG3724 L816–817；PG15766 L327–330；PG821 L18245–18249；PG3719 L599–601。
- K006：PG49282 L5128–5133；PG3719 L386–388；PG20533 L14234–14258；PG471 L11270–11274。
- K158：PG3719 L817–819/L951–952。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L19；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG3724**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K001：PG3724 L816–817；PG15766 L327–330；PG821 L18245–18249；PG3719 L599–601。
- K004：PG3724 L590–621/L1013–1031；PG821 L6535/L908–947/L32444–32456。
- K008：PG3724 L982/L883–901；PG969 L15034–15036；PG21847 L6231–6779；PG15766 L826–827。
- K159：PG969 L14011–14019；PG4275 L4236–4239；PG3724 L448。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L20；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG4275**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K009：PG4275 L2940–2946/L3456–3462/L12766–12779；PG4398 L3501–4000/L4153–4154/L9546–9550。
- K014：PG4398 L9016–9025/L10574–10576/L9546–9550；PG4275 L11098–11109。
- K159：PG969 L14011–14019；PG4275 L4236–4239；PG3724 L448。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L21；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG4398**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K009：PG4275 L2940–2946/L3456–3462/L12766–12779；PG4398 L3501–4000/L4153–4154/L9546–9550。
- K014：PG4398 L9016–9025/L10574–10576/L9546–9550；PG4275 L11098–11109。
- K018：PG1839 L8249–8251；PG4398 L5289–5290；PG11640 L7928–7929/L8218–8259。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L22；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG471**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K002：PG821 L4582–4649；PG471 L12443–12446。
- K003：PG471 L11911–12000。
- K006：PG49282 L5128–5133；PG3719 L386–388；PG20533 L14234–14258；PG471 L11270–11274。
- K013：PG471 L7196–7199/L13317–13383。
- K016：PG1917 L11952–11999；PG15252 L2440–2442；PG471 L12443–12446。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L14；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG49282**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K005：PG49282 L249–272。
- K006：PG49282 L5128–5133；PG3719 L386–388；PG20533 L14234–14258；PG471 L11270–11274。
- K021：PG20533 L13839–13854/L12762–12763；PG49282 L1779–1780；PG68273（走私/地牢，来源未单列精确行）。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L31；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG4961**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K019：PG1839 L5996–5998/L109–159；PG4961 L3371/L9335–9337；PG11640 L3840–3842。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L23；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG68273**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K010：PG68273 L9706–9721；PG969 L11508–11524。
- K015：PG21847 L6780–7245/L7246–7753；PG68273 L6168–6172/L4727–4730。
- K021：PG20533 L13839–13854/L12762–12763；PG49282 L1779–1780；PG68273（走私/地牢，来源未单列精确行）。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L32；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG821**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K001：PG3724 L816–817；PG15766 L327–330；PG821 L18245–18249；PG3719 L599–601。
- K002：PG821 L4582–4649；PG471 L12443–12446。
- K004：PG3724 L590–621/L1013–1031；PG821 L6535/L908–947/L32444–32456。
- K011：PG969 L6534–6573/L7914–7918/L4518–4532；PG821 L30190–30193/L34406–34415。
- K017：PG969 L17843–17860；PG821 L37389–37393/L37862–37883；PG15766 L9564–9573/L5430–5431。
- K022：PG20533/PG49282喜剧；PG471悲剧；PG821/PG4398反讽；PG68273身份惊悚；各具体行锚见本批K卡。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L15；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

**PG969**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K008：PG3724 L982/L883–901；PG969 L15034–15036；PG21847 L6231–6779；PG15766 L826–827。
- K010：PG68273 L9706–9721；PG969 L11508–11524。
- K011：PG969 L6534–6573/L7914–7918/L4518–4532；PG821 L30190–30193/L34406–34415。
- K017：PG969 L17843–17860；PG821 L37389–37393/L37862–37883；PG15766 L9564–9573/L5430–5431。
- K159：PG969 L14011–14019；PG4275 L4236–4239；PG3724 L448。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-01/rounds/round-p4-final-2026-10-30/output/romance-social-cost-craft/references/01-source-roles.md` L16；源Skill SHA256 `dc3577f77cc77eae5e5a8bb9e1819d0f9062f31ea4856a466ca60ff16d9b97c7`。

## B-03-B02

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG1023 | Bleak-House | Dickens | 39837 | SHA256 f5a63bc64af664bb555a3cf8c2804e1d2b612cc07d898d567a1d5aa8e83edd85 | K166 |
| PG12234 | Mr-Scarborough-s-Family | Trollope（来源族表署名） | 22509 | SHA256 1484dace6fd564e32ebb122ff6df5277697ee7f76900d67d2253659d7568d935 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG1263 | The-Glimpses-of-the-Moon | Wharton | 9181 | SHA256 91e7d8106fe4f19ca8493d33e16fabe16b850f05715e31f9fd0edb5710ddb959 | K036 |
| PG1342 | Pride-and-Prejudice | Austen（来源族表署名） | 14529 | SHA256 595bb39fe77d98088ca138ae83602734e18733d3f32b16f45b717721beb1c9fb | K023, K025, K032, K033, K035 |
| PG158 | Emma | Austen（来源族表署名） | 16489 | SHA256 4ae98d6e56b57e5a3e7a3b9dbc344590aa6b7db7c05e08874885eb5131ad853d | K024 |
| PG1671 | When-a-Man-Marries | Rinehart | 6266 | SHA256 989f4d47d72d257290952b19e0bc5516c8b135e436d88d16939be2260eff27f1 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG27712 | Sir-Harry-Hotspur-of-Humblethwaite | Trollope（来源族表署名） | 7689 | SHA256 262f28c1e73ac0ee70d49a8e1c1aafd0dbd69725416e3ffc7114fe1fddeeb447 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG3321 | Children-of-the-Whirlwind | Leroy Scott（最新来源族表；旧Packard归属撤回） | 11484 | SHA256 6a1fbc8570ff0d7a2316a2ea76d19358bd4c92f724089d9d0a2e6c9c7cd8c866 | K026, K027, K028, K029, K030, K031, K034, K035, K037, K039, K041, K043, K044, K161 |
| PG3404 | April-Hopes | Howells | 13487 | SHA256 aba68d846684517edb7daf29086791a74b8013b50fd94ced61d7cbe307694138 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG35538 | The-Squatter-and-the-Don-A-Novel-Descriptive-of-Contemporary | Ruiz de Burton | 16337 | SHA256 c6ab6e32ccfe4df96ae38ba980c71da28aaecbc7b681e8da9119387494d9c0e2 | K036 |
| PG3699 | Miss-Sarah-Jack-of-Spanish-Town-Jamaica | Trollope（来源族表署名） | 1037 | SHA256 626b409615ffd02ae519bb59f7ed805ec440011b67bcd3ffaf188d90675d40df | K166 |
| PG3700 | The-Courtship-of-Susan-Bell | Trollope（来源族表署名） | 1317 | SHA256 d7f6b01a45c3931156997068bcd1cf526581678170cec66e5b2f389af2035e2e | K166 |
| PG4917 | The-Kellys-and-the-O-Kellys | Trollope（来源族表署名） | 19348 | SHA256 fbcb79069a4b147914fcfab9baf80c1f50c913c5779f2fe348ca33ce158dd885 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG524 | Ann-Veronica-A-Modern-Love-Story | Wells | 12109 | SHA256 600e54136ba4e8e986c8775bb2b0c56212f3c308f426a9306e2e24733c78f11e | K033, K040 |
| PG54010 | The-Younger-Sister-A-Novel-Vol-I | Hubback 续书三卷（来源族表署名） | 5471 | SHA256 b17bec60a40e3cc4dee0260043467e4847fefdc4ef83f5faa51beff0acc26a50 | K042 |
| PG54011 | The-Younger-Sister-A-Novel-Vol-II | Hubback 续书三卷（来源族表署名） | 7742 | SHA256 a5f7fa4166ae64b8717b16a7f69146a754b6e2bb3aaed5574421dbd9b5b4528f | K032, K042 |
| PG54012 | The-Younger-Sister-A-Novel-Vol-III | Hubback 续书三卷（来源族表署名） | 9047 | SHA256 2ba8653e446b44f5cf44ba7fd5e69ab25fa21295bde51512fe15068a08de0dbb | K042 |
| PG619 | The-Warden | Trollope（来源族表署名） | 7580 | SHA256 205b18b0bdcd686ab0c3929a47b93cc53a0e2a881d0b2c45caf7216f9f54f45c | K025, K036, K038, K040 |
| PG68222 | His-fortunate-Grace | Gertrude Atherton（书头L9；原“单本”是分组标签，不是作者） | 3903 | SHA256 6f46934dfeaeff0402ceffbb171f17b09a5299d0d143e98d7785e16d8132745c | 身份/结构范围；RO01/RO34/RO35，不增造技法 |

### 当前锚点及来源元数据证据

**PG1023**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K166：PG3699/PG3700/PG1023，最新行数见B02 source-index；旧形态表。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L18；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG12234**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L27；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG1263**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K036：PG619 L525–526/L2565–2570；PG35538 L771–773/L1797–1836/L6214–6226；PG1263 L101–176。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L19；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG1342**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K023：PG1342 L7505–7544/L7529–7533/L7696–7951/L7469–7485/L8114。
- K025：PG1342 L7737–7741/L7748–7749；PG619 L813–908。
- K032：PG1342 L13720–13738/L13730–13733；PG54011 L244–280。
- K033：PG1342 L13699–13702/L13673–13678；PG524 L2358–2409。
- K035：PG1342 L13753–13755/L13783–13793/L13804–13807；PG3321 L8595–8612/L8832–8835/L10580–10585/L11428–11449。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L20；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG158**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K024：PG158 L80–294/L673–946，尤其L928–946。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L15；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG1671**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L21；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG27712**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L28；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG3321**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K026：PG3321 L2431–2445/L2458/L7611–7630/L6768–6770/L7333–7343。
- K027：PG3321 L2472–2474/L6855–6864/L8013–8019。
- K028：PG3321 L3367–3398/L5605–5607/L7817–7823/L10782–10823/L10845–10850/L9869–9872/L9919–9931/L10994–11005。
- K029：PG3321 L2246–2259/L2298–2303/L2476–2478。
- K030：PG3321 L6023–6033/L8788–8790/L8886–8911/L4022–4025/L4036–4040。
- K031：PG3321 L5480–5486/L6659–6661/L5951–5983/L8407–8409/L8549–8550。
- K034：PG3321 L6998–7000/L7027–7028/L9377–9382/L7002–7004/L7212–7218/L7286–7289/L8941–8949/L9408–9413。
- K035：PG1342 L13753–13755/L13783–13793/L13804–13807；PG3321 L8595–8612/L8832–8835/L10580–10585/L11428–11449。
- K037：PG3321 L5164–5208（索引另写5174起）/L7266–7267/L8257–8266/L11144–11148/L11118–11130/L11137–11138。
- K039：PG3321 L8962–8969/L8407–8409/L8549–8550。
- K041：PG3321 L7964–7983/L7596–7599/L11036–11042/L11044–11055。
- K043：PG3321 L7642–7647/L11180–11188/L11428–11429/L6014–6021/L6323–6325/L5549–5552/L10994–11005。
- K044：B02 references/04-source-index与05-cross-source-decisions；PG3321 11484行/12区块为上游最终报告。
- K161：PG3321 L1247–1257/L10292–10371。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L22；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG3404**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L23；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG35538**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K036：PG619 L525–526/L2565–2570；PG35538 L771–773/L1797–1836/L6214–6226；PG1263 L101–176。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L29；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG3699**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K166：PG3699/PG3700/PG1023，最新行数见B02 source-index；旧形态表。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L24；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG3700**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K166：PG3699/PG3700/PG1023，最新行数见B02 source-index；旧形态表。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L25；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG4917**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L26；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG524**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K033：PG1342 L13699–13702/L13673–13678；PG524 L2358–2409。
- K040：PG619 L472–495/L497–530；PG524 L1199–1225。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L16；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG54010**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K042：PG54010 L28–35/L57–161；PG54011 L1–400/L50–266；PG54012 L1–59/L33–43。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L30；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG54011**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K032：PG1342 L13720–13738/L13730–13733；PG54011 L244–280。
- K042：PG54010 L28–35/L57–161；PG54011 L1–400/L50–266；PG54012 L1–59/L33–43。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L31；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG54012**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K042：PG54010 L28–35/L57–161；PG54011 L1–400/L50–266；PG54012 L1–59/L33–43。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L32；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG619**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K025：PG1342 L7737–7741/L7748–7749；PG619 L813–908。
- K036：PG619 L525–526/L2565–2570；PG35538 L771–773/L1797–1836/L6214–6226；PG1263 L101–176。
- K038：PG619 L7285–7330。
- K040：PG619 L472–495/L497–530；PG524 L1199–1225。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L17；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

**PG68222**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。
Main追加原文/元数据裁定：实读阅读版L1–65，标题L1/L6、作者L9、当前版年L17、版权L22；1897不自动推为首版年。旧历史字段的“单本”仅为作者族分组。 证据：verification/02-romance-responsibility-columns.txt 与 verification/02-romance-Trollope-metadata.txt。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-02/rounds/round-p4-final-2026-10-30/output/courtship-conflict-craft/references/04-source-index.md` L33；源Skill SHA256 `151b7592ac37c01b79341bd59d0a69f62fe9318f91f7d0043718ed4a18b38c68`。

## B-03-B03

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG145 | Middlemarch | Eliot, George, 1819-1880 | 33277 | SHA256 db33091e5dfb388041d13c5037409b0b08833628d3b06c24ab7fd9f522249923 | K049, K052, K057, K059 |
| PG15381 | Victorian Short Stories: Stories of Courtship | Gilbert, W. S. (William Schwenck), 1836-1911 [Contributor]; Crackanthorpe, Hubert, 1870-1896 [Contributor]; Egerton, George, 1859-1945 [Contributor]; Trollope, Anthony, 1815-1882 [Contributor]; Zangwill, Israel, 1864-1926 [Contributor] | 4021 | SHA256 01a3ca462eb36d86d7e70d5a71170b5f39c7fc184ac0c57d23dcb42135581c89 | K045, K047, K048, K049, K051, K052, K053, K054, K056, K057, K059, K061, K062 |
| PG1569 | The Lily of the Valley | Balzac, Honoré de, 1799-1850; Wormeley, Katharine Prescott, 1830-1908 [Translator] | 9734 | SHA256 8004565f928eaf8244edc45254e47749abfcb222b275bce7bf71ca669fd4ecd0 | K165 |
| PG1624 | The Two Destinies | Collins, Wilkie, 1824-1889 | 9481 | SHA256 058c20ed9e2e004da3f722c904cfc1720796101840b449305ff4ad8c2b83c21b | K050, K051, K054, K058, K059 |
| PG16389 | The Enchanted April | Von Arnim, Elizabeth, 1866-1941 | 8731 | SHA256 7711a12937b414622dd5ae40af673a42d3abe94afb8fce0c9120b399747ce473 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG20945 | Patty Blossom | Wells, Carolyn, 1862-1942 | 7295 | SHA256 173eff18ed1af43fdb01c5eec2fe97d11eb188058edda5549a2127d716bf190b | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG25579 | Ralph the Heir | Trollope, Anthony, 1815-1882 | 22136 | SHA256 6efced93b350d6e5447c886146b29c790e7230e981dc887a6789f177ea95557f | K045, K050, K059 |
| PG25726 | The pretty sister of José 1889 | Burnett, Frances Hodgson, 1849-1924; Reinhart, Charles Stanley, 1844-1896 [Illustrator] | 2159 | SHA256 a8591719300e7d8186f7569d7d34e1d438fd0144fc4b42d3b11816b593a46ed1 | K045, K046, K047, K048, K051, K054, K055, K057, K060 |
| PG27 | Far from the Madding Crowd | Hardy, Thomas, 1840-1928 | 16629 | SHA256 2ca22d1c86484cea6bcb444e24027e7be69b8b649ce6e3a3a6d0b81ac1471f66 | K048 |
| PG39172 | A Safety Match | Hay, Ian, 1876-1952 | 8729 | SHA256 d4d13c527a3ad19c906a870ae35a70e65b10aa8bdfd808ee6328f6089fad0f2d | K165 |
| PG42085 | A Bachelor Husband | Ayres, Ruby M. (Ruby Mildred), 1883-1955; Stahr, Paul, 1883-1953 [Illustrator] | 14343 | SHA256 633b716806b3ac766adc2927921e05414114e575353af1858b4a368251a94da5 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG47874 | My Wife and I; Or, Harry Henderson's History | Stowe, Harriet Beecher, 1811-1896 | 17195 | SHA256 ba940ea5c452d8c6771eaf8c132cf3727ec75a4610a597b322a8787481a0ef54 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG68069 | The principal girl | Snaith, J. C. (John Collis), 1876-1936 | 8267 | SHA256 769ece07018766e42aca73323dbcb725abd865dbae3df3a51545304d0997127f | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG7005 | The Antiquary — Complete | Scott, Walter, 1771-1832 | 18665 | SHA256 72d7d229977c4166e376b7865a05fc5bdc2a2a9405d4f569743eb5562051e64b | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG768 | Wuthering Heights | Brontë, Emily, 1818-1848 | 12342 | SHA256 deb0c9b35b247c97d5a1ed71043294b95cd90bcd3a668442a3e126d79ee8cb89 | K054, K056, K058 |
| PG7892 | Heart and Science: A Story of the Present Time | Collins, Wilkie, 1824-1889 | 15367 | SHA256 7a4403222d3d59b81b3a62a96c9a32518ed813356a13e3e41b431b22db4e5201 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |
| PG8897 | Nina Balatka | Trollope, Anthony, 1815-1882 | 8162 | SHA256 431c3973dcf358c4a72d46c31381ec9fb07d403d5e303c15f801e77a4d36ffe4 | K061, K164 |
| PG945 | Dust | Haldeman-Julius, E. (Emanuel), 1888-1951; Haldeman-Julius, Marcet, 1887-1941 | 4868 | SHA256 493a81f7a2a887d7dc29e2ff3cf2fbc168827f0c9e15f4c69d88f7474fbc3d75 | 身份/结构范围；RO01/RO34/RO35，不增造技法 |

### 当前锚点及来源元数据证据

**PG145**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K049：PG15381 L1542–1543/L2679/L2933–2934/L1048；PG145 L25068–25069。
- K052：PG15381 L60–61/L196/L200–201；PG145 L16739–16740。
- K057：PG15381 L1360/L2679；PG145 L33246–33247/L33251；PG25726 L2145–2152。
- K059：PG15381 L3538–3539；PG145 L24974–24976；PG25579 L22042–22043；PG1624 L70。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L7；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG15381**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K045：PG25726 L149/L751/L136；PG15381 L1300–1301；PG25579 L5633–5642。
- K047：PG15381 L730–731/L746/L1251–1252；PG25726 L900–935/L1017–1060。
- K048：PG25726 L264/L664/L537–538；PG15381 L3280；PG27 L35。
- K049：PG15381 L1542–1543/L2679/L2933–2934/L1048；PG145 L25068–25069。
- K051：PG25726 L1359–1360/L1457/L1494；PG15381 L3148–3149；PG1624 L7118。
- K052：PG15381 L60–61/L196/L200–201；PG145 L16739–16740。
- K053：PG15381 L3313/L3479/L3968/L4020。
- K054：PG15381 L768–770；PG25726 L2106/L1935/L2113；PG1624 L7185–7186；PG768 L6270。
- K056：PG768 L6215/L6217；PG15381 L103（旧104）/L200–201/L3175。
- K057：PG15381 L1360/L2679；PG145 L33246–33247/L33251；PG25726 L2145–2152。
- K059：PG15381 L3538–3539；PG145 L24974–24976；PG25579 L22042–22043；PG1624 L70。
- K061：B03 version-and-provenance；PG15381旧ANGELA L41–43/L84–92；PG8897旧L5400为采样状态。
- K062：PG15381贡献者Gilbert、Crackanthorpe、Egerton、Trollope、Zangwill；B03 source-index/version-and-provenance。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L8；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG1569**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K165：PG1569书信体；PG39172章题，原历史结构表未列行锚。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L9；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG1624**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K050：PG1624 L85/L99/L7188–7189；PG25579 L22030–22031。
- K051：PG25726 L1359–1360/L1457/L1494；PG15381 L3148–3149；PG1624 L7118。
- K054：PG15381 L768–770；PG25726 L2106/L1935/L2113；PG1624 L7185–7186；PG768 L6270。
- K058：PG1624 L9445–9446/L9451–9452；PG768 L12298–12299/L12341–12342。
- K059：PG15381 L3538–3539；PG145 L24974–24976；PG25579 L22042–22043；PG1624 L70。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L10；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG16389**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L11；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG20945**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L12；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG25579**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K045：PG25726 L149/L751/L136；PG15381 L1300–1301；PG25579 L5633–5642。
- K050：PG1624 L85/L99/L7188–7189；PG25579 L22030–22031。
- K059：PG15381 L3538–3539；PG145 L24974–24976；PG25579 L22042–22043；PG1624 L70。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L13；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG25726**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K045：PG25726 L149/L751/L136；PG15381 L1300–1301；PG25579 L5633–5642。
- K046：PG25726 L900–901/L799/L1519。
- K047：PG15381 L730–731/L746/L1251–1252；PG25726 L900–935/L1017–1060。
- K048：PG25726 L264/L664/L537–538；PG15381 L3280；PG27 L35。
- K051：PG25726 L1359–1360/L1457/L1494；PG15381 L3148–3149；PG1624 L7118。
- K054：PG15381 L768–770；PG25726 L2106/L1935/L2113；PG1624 L7185–7186；PG768 L6270。
- K055：PG25726 L353/L1212/L1609/L2061。
- K057：PG15381 L1360/L2679；PG145 L33246–33247/L33251；PG25726 L2145–2152。
- K060：PG25726 L2042–2054。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L14；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG27**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K048：PG25726 L264/L664/L537–538；PG15381 L3280；PG27 L35。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L15；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG39172**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K165：PG1569书信体；PG39172章题，原历史结构表未列行锚。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L16；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG42085**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L17；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG47874**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L18；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG68069**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L19；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG7005**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L20；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG768**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K054：PG15381 L768–770；PG25726 L2106/L1935/L2113；PG1624 L7185–7186；PG768 L6270。
- K056：PG768 L6215/L6217；PG15381 L103（旧104）/L200–201/L3175。
- K058：PG1624 L9445–9446/L9451–9452；PG768 L12298–12299/L12341–12342。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L21；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG7892**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L22；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG8897**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K061：B03 version-and-provenance；PG15381旧ANGELA L41–43/L84–92；PG8897旧L5400为采样状态。
- K164：PG8897 L5400，旧R1-f STRUCTURAL。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L23；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

**PG945**：仅身份/历史覆盖或结构定位；源Skill没有足够细节时，不虚构机制。RO01/RO34/RO35。

- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-03/rounds/round-p4-wave4-agent2-2026-10-30/output/romance-emotional-arc/references/source-index.md` L24；源Skill SHA256 `2600fd2b5d9bcfbb2f1cb7f4aeac2ee62d7b72b6a5b23e0e149a8d4fd03e4d9c`。

## B-03-B04

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG12557 | The Penalty | Gouverneur Morris | 9929 | SHA256 e00cfb1c8131f92974a4f8c5e691f835751f5bc202a4f94a3316f7e6edd8b055 | K069, K072, K076, K077, K080, K084 |
| PG1260 | Jane Eyre | Charlotte Brontë（L342） | 21001 | SHA256 68cae87bf3bf3907fde0e61ac61a0f6eceb40a7fe9d00a3714c56852aaa0d503 | K068, K069, K078, K084 |
| PG161 | Sense and Sensibility | Jane Austen | 12673 | SHA256 28957bc02be55eb1a58e662706593fcb0638b9941212790332056c7fd47c2da1 | K063, K072, K079, K082, K162 |
| PG19191 | The Fruit of the Tree | Edith Wharton | 16931 | SHA256 95d3462a2e6a259be1225e04ff8dd0b7114c91eef34adafd6952326ed952cfd4 | K076, K077, K080, K162 |
| PG23000 | Orley Farm | Anthony Trollope | 34165 | SHA256 6c01ed618cfb85e9781bc8ac5ac5f87f5daac10fe89358f991724b97c1ba3d18 | K064, K068, K076, K086 |
| PG24103 | Cousin Henry | Anthony Trollope | 7522 | SHA256 a3b47510b235d7b35656d14bc51c889c872687c6e2d8fead767d67cea099c3a2 | K087 |
| PG27990 | Theo | Frances Hodgson Burnett | 4009 | SHA256 0d2cec2131f9c5a29a047cd7d261a14cecc62026e9ccf79d7a2442ff37ac6612 | K068, K085 |
| PG283 | The Reef | Edith Wharton | 10769 | SHA256 16b5fec3e82c4e28bedd8c266c2359193150ae4d2b16f810962414e2c9282b70 | K066, K069, K074 |
| PG3615 | John Bull on the Guadalquivir | Anthony Trollope（归档书籍信息.json L4）；David Price（阅读版L1–2，转录者） | 980 | SHA256 a679b53056101b56fca4f27344262cfa04465bf54eb2827e051782eab706df26 | K067, K072, K162 |
| PG3632 | Poor Miss Finch | Wilkie Collins | 17928 | SHA256 86b04166198a18ce484ae727fae4d9a8529722f77b2e75291c96e59f6163437e | K070, K071, K082, K084 |
| PG3710 | An Unprotected Female at the Pyramids | Anthony Trollope（归档书籍信息.json L4）；David Price（阅读版L4–5，转录者） | 1266 | SHA256 831e713fe959a8fe731b3012318bb198edf4accdf6d9a9c34a10f03682df3785 | K086 |
| PG41031 | When a Man's Single: A Tale of Literary Life | J. M. Barrie | 8371 | SHA256 358ecf24b9fbd75211c59eb56d42337c16785f1e7bc43ae7997e303c65a5fffa | K072, K162 |
| PG43168 | Hathercourt | Mrs Molesworth | 14372 | SHA256 a0a9e7b92c102964df972970cae6fcb7d90adb5623a9ffa8835924b44c9d93a4 | K065, K085 |
| PG4629 | Home Scenes and Home Influence | T. S. Arthur | 6018 | SHA256 17a57c5ae749fe5b11cb46b7e30207f9f26c5a96912f14c9b4c99aaa6664a7be | K088 |
| PG5066 | The Whole Family | 十二章共同作者：William Dean Howells / Mary E. Wilkins Freeman / Mary Heaton Vorse / Mary Stewart Cutting / Elizabeth Jordan / John Kendrick Bangs / Henry James / Elizabeth Stuart Phelps / Edith Wyatt / Mary Raymond Shipman Andrews / Alice Brown / Henry Van Dyke | 7414 | SHA256 e5d75b41b42815f9aa9bb6ffe4389bf6c94cb7a3930352d08f9df1144b7174d1 | K083 |
| PG541 | The Age of Innocence | Edith Wharton（L11565） | 11568 | SHA256 f63756accf65880830dfbed5d7b903a98da42958ebbcf15a5e363e1d01dcad08 | K066, K073, K080, K082, K084 |
| PG6688 | The Mill on the Floss | George Eliot | 21240 | SHA256 cc7b6788a0a07b19a86f034a47eb2d721fb904876659e0399071ba788cd3c785 | K066, K075, K081 |
| PG70237 | The Unlit Lamp: A Study of Inter-Actions | Elisabeth Sanxay Holding | 10608 | SHA256 e05e908ea45efa05e38742185b33dc83a7b4c2743e0ee0545eb4deca9be33627 | K087 |
| PG7141 | Suburban Sketches | William Dean Howells | 5961 | SHA256 96759dccb8fde67cbaa9ca8ff8081c16e658adfa79fbb3945a26cfcd38415cd1 | K089 |

### 当前锚点及来源元数据证据

**PG12557**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K069：PG1260 L10946–11007；PG12557 L8767–8783；PG283 L9072–9077。
- K072：PG3615 L906–910/L966–969；PG41031 L6387–6388/L6413–6416；PG161 L2372–2374；PG12557 L933–934/L955–972。
- K076：PG12557 L9902–9904/L9288–9331；PG19191 L16251–16252；PG23000 L33101–33102。
- K077：PG12557 L9928–9929；PG19191 L11322–11343。
- K080：PG12557 L9700–9741/L9788–9815；PG19191 L11322–11330；PG541 L10989–10993/L11054–11055。
- K084：PG541 L10289–10308/L11526–11544；PG1260 L20826–20827；PG3632 L7513–7526；PG12557多线全知（来源无单一行锚）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L23；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG1260**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K068：PG27990 L3695–3721；PG23000 L33234–33238；PG1260 L20650–20654。
- K069：PG1260 L10946–11007；PG12557 L8767–8783；PG283 L9072–9077。
- K078：PG1260 L17607–17666/L17812–17957/L12451–12456。
- K084：PG541 L10289–10308/L11526–11544；PG1260 L20826–20827；PG3632 L7513–7526；PG12557多线全知（来源无单一行锚）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L18；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG161**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K063：PG161 L4290–4400，尤其L4373。
- K072：PG3615 L906–910/L966–969；PG41031 L6387–6388/L6413–6416；PG161 L2372–2374；PG12557 L933–934/L955–972。
- K079：PG161 L12476–12496/L12629–12652/L12531–12536/L12175–12196。
- K082：PG541 L8170–8174/L8620–8629/L10666–10672；PG3632 L12803–12818/L12810–12812；PG161 L6439–6440/L5719–5720。
- K162：PG161 L3007–3048/L8815–8824；PG19191 L9449–9451；PG41031 L7973–7975；PG3615 L251–299（扯扣子），L755–760（丑闻/误认语境）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L19；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG19191**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K076：PG12557 L9902–9904/L9288–9331；PG19191 L16251–16252；PG23000 L33101–33102。
- K077：PG12557 L9928–9929；PG19191 L11322–11343。
- K080：PG12557 L9700–9741/L9788–9815；PG19191 L11322–11330；PG541 L10989–10993/L11054–11055。
- K162：PG161 L3007–3048/L8815–8824；PG19191 L9449–9451；PG41031 L7973–7975；PG3615 L251–299（扯扣子），L755–760（丑闻/误认语境）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L17；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG23000**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：书头声明连载1861年3月至1862年10月，书版1862；可按原族口径并入Trollope。 实读范围：L1–45，标题/署名/日期L19–26。

- K064：PG23000 L33234–33241/L33234–33238。
- K068：PG27990 L3695–3721；PG23000 L33234–33238；PG1260 L20650–20654。
- K076：PG12557 L9902–9904/L9288–9331；PG19191 L16251–16252；PG23000 L33101–33102。
- K086：PG3710 L104–120/L1204–1215/L1254–1266；PG23000 L33062–33063/L33304–33310/L33490–33491。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L28；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG24103**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K087：PG24103 L279–343/L7510–7522；PG70237 L10251–10255/L10302/L10334–10336。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L29；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG27990**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K068：PG27990 L3695–3721；PG23000 L33234–33238；PG1260 L20650–20654。
- K085：PG43168 L3283–3303/L10281–10350/L13766–13838；PG27990 L3739–3759。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L22；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG283**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K066：PG283 L10315–10347；PG541 L10685–10689；PG6688 L20504–20548。
- K069：PG1260 L10946–11007；PG12557 L8767–8783；PG283 L9072–9077。
- K074：PG283 L10556–10573/L10733–10734/L9779–9781。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L16；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG3615**：当前知识详见所列K/HB；元数据不是另一套执行指令。
Main追加原文/元数据裁定：实读阅读版L1–35与归档书籍信息.json全文37行。作者来自JSON L4；1864 Chapman and Hall与David Price是底本/转录信息，不能填作作者。阅读版书头本身没有作者，不冒称该窗口署名。 证据：verification/02-romance-responsibility-columns.txt 与 verification/02-romance-Trollope-metadata.txt。

- K067：PG3615 L251–299（扯扣子）/L755–760/L806–817/L944–964。
- K072：PG3615 L906–910/L966–969；PG41031 L6387–6388/L6413–6416；PG161 L2372–2374；PG12557 L933–934/L955–972。
- K162：PG161 L3007–3048/L8815–8824；PG19191 L9449–9451；PG41031 L7973–7975；PG3615 L251–299（扯扣子），L755–760（丑闻/误认语境）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L26；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG3632**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K070：PG3632 L6495–6549/L6748–6767/L6803–6805。
- K071：PG3632 L9225–9228/L9290–9291/L17750–17814。
- K082：PG541 L8170–8174/L8620–8629/L10666–10672；PG3632 L12803–12818/L12810–12812；PG161 L6439–6440/L5719–5720。
- K084：PG541 L10289–10308/L11526–11544；PG1260 L20826–20827；PG3632 L7513–7526；PG12557多线全知（来源无单一行锚）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L20；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG3710**：当前知识详见所列K/HB；元数据不是另一套执行指令。
Main追加原文/元数据裁定：实读阅读版L1–35与归档书籍信息.json全文37行。作者来自JSON L4；1864 Chapman and Hall与David Price是底本/转录信息。“同上集”展开为本条明确责任关系。原阅读版写Tales of All Countries，保留其字面而不静默改成from。 证据：verification/02-romance-responsibility-columns.txt 与 verification/02-romance-Trollope-metadata.txt。

- K086：PG3710 L104–120/L1204–1215/L1254–1266；PG23000 L33062–33063/L33304–33310/L33490–33491。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L27；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG41031**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：当前版本书头1913，不能自动称首版年。 实读范围：L1–45，署名L3/L10，版本年L14。

- K072：PG3615 L906–910/L966–969；PG41031 L6387–6388/L6413–6416；PG161 L2372–2374；PG12557 L933–934/L955–972。
- K162：PG161 L3007–3048/L8815–8824；PG19191 L9449–9451；PG41031 L7973–7975；PG3615 L251–299（扯扣子），L755–760（丑闻/误认语境）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L24；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG43168**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：当前版本明确1878，署名不是未声明。 实读范围：L1–60，标题/署名/版年L1–6。

- K065：PG43168 L4631–4744/L4863–4905。
- K085：PG43168 L3283–3303/L10281–10350/L13766–13838；PG27990 L3739–3759。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L21；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG4629**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K088：PG4629 L5009–5059/L5071–5074/L5665。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L32；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG5066**：当前知识详见所列K/HB；元数据不是另一套执行指令。
Main追加原文/元数据裁定：实读L1–80，L14–17列十二作者，L22–33逐章对应；Howells不是全书唯一责任者。共同作者关系与声音分配分别记录，不把十二个声音算成十二次独立读者验证。 证据：verification/02-romance-responsibility-columns.txt 与 verification/02-romance-Trollope-metadata.txt。

- K083：PG5066 全文7414行/十二作者；L7250–7252/L7374–7383/L2164–2170/L2489–2501/L5705–5715。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L25；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG541**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K066：PG283 L10315–10347；PG541 L10685–10689；PG6688 L20504–20548。
- K073：PG541 L11391–11394/L11359–11362/L11366/L11496/L11500/L11541/L11547–11552/L11054–11068。
- K080：PG12557 L9700–9741/L9788–9815；PG19191 L11322–11330；PG541 L10989–10993/L11054–11055。
- K082：PG541 L8170–8174/L8620–8629/L10666–10672；PG3632 L12803–12818/L12810–12812；PG161 L6439–6440/L5719–5720。
- K084：PG541 L10289–10308/L11526–11544；PG1260 L20826–20827；PG3632 L7513–7526；PG12557多线全知（来源无单一行锚）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L15；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG6688**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K066：PG283 L10315–10347；PG541 L10685–10689；PG6688 L20504–20548。
- K075：PG6688 L20904/L20925–20927/L20933–20934/L20950–20953/L21121–21124/L21201–21240。
- K081：PG6688 L20579–20601/L20635–20637/L20803–20830。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L30；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG70237**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：版权1922；不是Radclyffe Hall的同名作品。 实读范围：L1–55，标题/署名/版权L1–23。

- K087：PG24103 L279–343/L7510–7522；PG70237 L10251–10255/L10302/L10334–10336。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L31；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

**PG7141**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K089：PG7141 L24–43/L5510–5961；B04 source-index/adjudication。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-04/rounds/round-p4-final-2026-10-30/output/romance-obstacle-and-cost/references/04-source-index.md` L33；源Skill SHA256 `95cae3d2cbe7aac7e15f7d65302eb270dd960972590de313f71b7817b8c440a5`。

## B-03-B05

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG11869 | Venetia | Earl of Beaconsfield (Disraeli) | NOT_DECLARED | NOT_DECLARED | K104 |
| PG1214 | The Street of Seven Stars | Mary Roberts Rinehart | NOT_DECLARED | NOT_DECLARED | K093, K163 |
| PG12280 | The Grandissimes | George Washington Cable | NOT_DECLARED | NOT_DECLARED | K093, K094, K095, K096, K099, K100, K101 |
| PG16249 | Bought and Paid For | Arthur Hornblow（据 George Broadhurst 剧本小说化） | NOT_DECLARED | NOT_DECLARED | K103 |
| PG2095 | Clotelle: A Tale of the Southern States | William Wells Brown | NOT_DECLARED | NOT_DECLARED | K092 |
| PG25727 | Vagabondia | Frances Hodgson Burnett | NOT_DECLARED | NOT_DECLARED | K103 |
| PG361 | Miss Billy Married | Eleanor H. Porter | NOT_DECLARED | NOT_DECLARED | K105 |
| PG380 | Weir of Hermiston, An Unfinished Romance | Robert Louis Stevenson | NOT_DECLARED | NOT_DECLARED | K106 |
| PG4599 | The Small House at Allington | Anthony Trollope | NOT_DECLARED | NOT_DECLARED | K091 |
| PG482 | The Woodlanders | Thomas Hardy | NOT_DECLARED | NOT_DECLARED | K098 |
| PG4969 | The Belton Estate | Anthony Trollope | NOT_DECLARED | NOT_DECLARED | K090 |
| PG507 | Adam Bede | George Eliot | NOT_DECLARED | NOT_DECLARED | K093, K163 |
| PG53864 | The Story of a Baby | Ethel Turner | NOT_DECLARED | NOT_DECLARED | K105 |
| PG54066 | The Younger Sister (Vols 1-3) | Mrs. Hubback | NOT_DECLARED | NOT_DECLARED | K101 |
| PG550 | Silas Marner | George Eliot | NOT_DECLARED | NOT_DECLARED | K102 |
| PG59181 | Tetherstones | Ethel M. Dell | NOT_DECLARED | NOT_DECLARED | K095, K097, K107, K108, K109, K110 |
| PG7359 | Indian Summer | William Dean Howells | NOT_DECLARED | NOT_DECLARED | K102 |
| PG76681 | Liliecrona's Home | Selma Lagerlöf | NOT_DECLARED | NOT_DECLARED | K106 |

### 当前锚点及来源元数据证据

**PG11869**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K104：PG11869 L451–456/L1040–1061/L4805。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L21；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG1214**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K093：PG1214 L958–967；PG507 L4403–4443；PG12280 L8870–8956。
- K163：PG1214 L450–520/L633–634/L958–967/L969–995；PG507 L2140–2241/L2519–2526/L4403–4443/L4666–4684。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L20；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG12280**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K093：PG1214 L958–967；PG507 L4403–4443；PG12280 L8870–8956。
- K094：PG12280 L9413–9423/L11332–11350/L10957–10965。
- K095：PG12280 L8693–8694；PG59181 L7013–7021。
- K096：PG12280 L14285–14286/L14304–14305/L14321/L14329–14335。
- K099：PG12280 L11778–11779/L11817–11820/L11062–11068。
- K100：PG12280 L11128–11159，尤其L11152–11159；L10320–10351。
- K101：PG12280 L8857–8858/L13601–13621；PG54066 L689–691/L570–593/L888–961/L2392–2406。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L9；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG16249**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K103：PG16249 L938–1000，尤其L987–988；L1357–1395/L1435–1441/L1542–1571；PG25727 L439–472/L495–505/L1251–1266。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L18；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG2095**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K092：PG2095 L56–70/L284–292/L301–306/L538–549。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L31；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG25727**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K103：PG16249 L938–1000，尤其L987–988；L1357–1395/L1435–1441/L1542–1571；PG25727 L439–472/L495–505/L1251–1266。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L19；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG361**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K105：PG361 L1–46/L542–581/L596–637/L1366–1447；PG53864 L82–160/L233–277/L419–430/L569–605。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L22；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG380**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K106：PG380 L1–29/L319–399/L410–416/L418–491/L608–618；PG76681 L1537–1567/L2051–2101/L2248–2278/L2505–2531。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L29；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG4599**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K091：PG4599 L3194–3330，尤其L3272–3273；L3936–3938；前文L1413–1433/L1545–1584/L2189–2213。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L13；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG482**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K098：PG482 L731–753/L1388–1443/L2827–2979/L3153–3165。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L11；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG4969**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K090：PG4969 L134–144/L237–254/L674–718/L752–789。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L12；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG507**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K093：PG1214 L958–967；PG507 L4403–4443；PG12280 L8870–8956。
- K163：PG1214 L450–520/L633–634/L958–967/L969–995；PG507 L2140–2241/L2519–2526/L4403–4443/L4666–4684。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L14；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG53864**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K105：PG361 L1–46/L542–581/L596–637/L1366–1447；PG53864 L82–160/L233–277/L419–430/L569–605。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L23；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG54066**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K101：PG12280 L8857–8858/L13601–13621；PG54066 L689–691/L570–593/L888–961/L2392–2406。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L17；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG550**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K102：PG550 L149–150/L294–331/L339–385；PG7359 L605–642/L2479–2545/L2698–2732。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L15；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG59181**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K095：PG12280 L8693–8694；PG59181 L7013–7021。
- K097：PG59181 L6603–6630/L6684–6695/L6700–6706/L6681–6682/L6833–6836。
- K107：PG59181 L9630–9704/L9945–10023/L10038–10200。
- K108：PG59181 L10341–10590。
- K109：PG59181 L10839–10857/L8402–8404/L8041–8045/L10893–10894。
- K110：PG59181 L9183/L9189；source-index相关窗口。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L10；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG7359**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K102：PG550 L149–150/L294–331/L339–385；PG7359 L605–642/L2479–2545/L2698–2732。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L16；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

**PG76681**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K106：PG380 L1–29/L319–399/L410–416/L418–491/L608–618；PG76681 L1537–1567/L2051–2101/L2248–2278/L2505–2531。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-05/rounds/round-p4-final-2026-10-30/output/romance-obstacle-delay-craft/references/source-index.md` L30；源Skill SHA256 `a64c215c7ecb1a02949592dd0ce2b5ff5c653b954025ff8bd9fd433c348b42ef`。

## B-03-B06

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG1028 | The Professor | Charlotte Brontë | 9413 | NOT_DECLARED | K126, K127, K133, K136, HB28 |
| PG121 | Northanger Abbey | Jane Austen | 7995 | NOT_DECLARED | K113, K114, K131 |
| PG1245 | Night and Day | Virginia Woolf | 18056 | NOT_DECLARED | K128, K136 |
| PG141 | Mansfield Park | Jane Austen | 15679 | SHA256 74590df7cef7953789113ee5dfe2886b290a724ea509f9a1286140c52baa2999 | K121, K123, K133, K134, HB20 |
| PG1437 | Juana | Honoré de Balzac | 2321 | NOT_DECLARED | K114, K115, K121, K128, K132, HB01, HB02, HB27, HB34 |
| PG1556 | The Marriage Contract | Honoré de Balzac | 5298 | NOT_DECLARED | K130, K132, K133, HB03, HB04, HB07, HB16, HB31 |
| PG1586 | Man and Wife | Wilkie Collins | 27019 | NOT_DECLARED | K115, K119, K128, K129, K135, HB17, HB18, HB24, HB36 |
| PG1608 | Camille (La Dame aux Camilias) | Alexandre Dumas fils | 8237 | NOT_DECLARED | K113, K118, K124, K125, K129, K131, K133, HB05, HB06, HB24, HB25, HB26, HB30, HB35 |
| PG16804 | An Eye for an Eye | Anthony Trollope | 7261 | NOT_DECLARED | K121, K122, K128, K131, HB08, HB09, HB10 |
| PG1684 | The Egoist | George Meredith | 23319 | NOT_DECLARED | K115, K121, K122, K126, K127, K131, K133, K134, HB15, HB27 |
| PG22000 | Kept in the Dark | Anthony Trollope | 7636 | NOT_DECLARED | K116, K126, K134, HB13 |
| PG24000 | Miss Mackenzie | Anthony Trollope | 15576 | NOT_DECLARED | K130, K131, K136, HB14 |
| PG3166 | Doctor Thorne | Anthony Trollope | 24486 | SHA256 d2a888071d9e16a86508bfe991e9bbac9e6e04c0c1257fa3476d84d0b27219be | K117, K118, K119, K121, K122, K125, K126, K127, K128, K129, K130, K131, HB19, HB20, HB22, HB24, HB27, HB28, HB29, HB30, HB37 |
| PG42812 | Katharine Frensham | Beatrice Harraden | 11408 | NOT_DECLARED | K113, K118, K128, K134, HB25 |
| PG4721 | Darkness and Daylight | Mary J. Holmes | 14078 | NOT_DECLARED | K116, K120, K124, K125, K135, HB11, HB12, HB18, HB29 |
| PG544 | Anne's House of Dreams | L. M. Montgomery | 8922 | NOT_DECLARED | K114, K118, K120, K125, K132, K135, HB21, HB22, HB26 |
| PG67123 | Show Boat | Edna Ferber | 11597 | NOT_DECLARED | K115, K118, K131, HB12, HB23 |
| PG77271 | Margaret Dashwood, or Interference | Mrs. Francis Brown（书头L9）；E. C. Hubback别名为上游继承，当前书头未证 | 4803 | SHA256 8491c6c2e00afbc9a623e4a476795fd2dddf007cb805a744157675a8dc8dc441 | K112, K119, K125, K131, HB23, HB32, HB33 |

### 当前锚点及来源元数据证据

**PG1028**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K126：PG22000 L3318–3367；PG1684 L15188–15189/L19666/L20990；PG1028 L3775–3784；PG3166 L21809–21824。
- K127：PG3166 L15329–15332/L15368；PG1684 L17719–17721/L17808；PG1028 L7759–7840。
- K133：PG1556 L556–563；PG1608 L7451/L8015–8016；PG1684 L41–46/L4512–4555；PG141 L15567（旧15259）；PG1028 L150–462。
- K136：PG1028 L7873–7930；PG24000 L4417–4448；PG1245 L6646–6680。
- HB28：PG1028 L3775–3784；PG3166 L21809–21824。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L17；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG121**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K113：PG121 L1460–1470/L3326–3350；PG1608 L1759–1809；PG42812 L1027–1093。
- K114：PG1437 L248–262/L580–584；PG121 L489（旧477–478）；PG544 L394–459。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L15；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1245**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K136：PG1028 L7873–7930；PG24000 L4417–4448；PG1245 L6646–6680。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L23；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG141**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：Sir Thomas/Fanny/Henry Crawford；非贵族姑妈/宫廷。 实读范围：书头L1–16与L10545–10620。

- K121：PG141 L65–72；PG1437 L1156–1161；PG3166 L1840–1851；PG1684 L3967；PG16804 L550–553；PG3166 L3794（旧3773）表亲权利。
- K123：PG141 实核L10545–10620，尤其L10559–10568/L10581–10591/L10599–10613；校验文件见historical-boundaries。
- K133：PG1556 L556–563；PG1608 L7451/L8015–8016；PG1684 L41–46/L4512–4555；PG141 L15567（旧15259）；PG1028 L150–462。
- K134：PG141 L10589；PG1684 L18554–18555（旧18555单行）；PG22000书信/PG42812自述（本条原Skill未单给统一行锚）。
- HB20：PG3166 B4/B9；PG141 B1/B3（区块定位）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L22；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1437**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K114：PG1437 L248–262/L580–584；PG121 L489（旧477–478）；PG544 L394–459。
- K115：PG1437 L665–684；PG1586 L4561–4583；PG67123 L7333–7334（旧2370–2373）；PG1684 L3825–3828。
- K121：PG141 L65–72；PG1437 L1156–1161；PG3166 L1840–1851；PG1684 L3967；PG16804 L550–553；PG3166 L3794（旧3773）表亲权利。
- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K132：PG544 L6499–6676；PG1437 L1746–1758；PG1556 L4126–4137。
- HB01：PG1437 L392–412/L553–556。
- HB02：PG1437 L1199–1203。
- HB27：PG1437 L1210–1214；PG1684 L41–46/L4512–4551（r5另列至4555）；PG3166 L23038–23061。
- HB34：PG1437全书评价；没有独立现代读者数据。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L9；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1556**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K130：PG1556 L2925–2971（旧窄锚2957）；PG24000 L9660–9671；PG3166 L24232–24256。
- K132：PG544 L6499–6676；PG1437 L1746–1758；PG1556 L4126–4137。
- K133：PG1556 L556–563；PG1608 L7451/L8015–8016；PG1684 L41–46/L4512–4555；PG141 L15567（旧15259）；PG1028 L150–462。
- HB03：PG1556 L3420–3426/L3615–3620。
- HB04：PG1556 L3560–3578。
- HB07：PG1556 L5136–5158。
- HB16：PG1556 L4850–4851。
- HB31：PG1556 L4824–4851。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L11；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1586**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K115：PG1437 L665–684；PG1586 L4561–4583；PG67123 L7333–7334（旧2370–2373）；PG1684 L3825–3828。
- K119：PG3166 L21809–21824/L15674–15723/L5501–5502；PG77271 L1419–1424/L1935–1937；PG1586 L20191–20256。
- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K129：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- K135：PG544 L4501–4632；PG4721 L11533–11535/L11395–11403；PG1586 L24876。
- HB17：PG1586 L24479–24900/L26744–26813；解放句精确L24876。
- HB18：PG1586 B21；PG4721 B10/B15（原卡仅区块号）。
- HB24：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- HB36：PG1586 B7/B9（区块定位）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L24；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1608**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K113：PG121 L1460–1470/L3326–3350；PG1608 L1759–1809；PG42812 L1027–1093。
- K118：PG1608 L2996–3007；PG544 L736–751；PG67123 L7392–7410；PG3166 L21723–21724；PG42812 L10721–10728。
- K124：PG4721 L3147–3148；PG1608 L2739–2745（病与十万开支）。
- K125：PG77271 L1771–1788；PG3166 L14730；PG4721 L7000–7016；PG544 L5804–5859；PG1608 L3827–3929。
- K129：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- K133：PG1556 L556–563；PG1608 L7451/L8015–8016；PG1684 L41–46/L4512–4555；PG141 L15567（旧15259）；PG1028 L150–462。
- HB05：PG1608 L593–644。
- HB06：PG1608 L7385–7396。
- HB24：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- HB25：PG1608 L4265–4548；PG42812 L10740–10891。
- HB26：PG1608 L7453–8164；PG544 L4501–4632。
- HB30：PG3166 B9；PG1608 B6（B06 counterexamples CE30，仅区块）。
- HB35：PG1608 L8236–8237。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L12；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG16804**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K121：PG141 L65–72；PG1437 L1156–1161；PG3166 L1840–1851；PG1684 L3967；PG16804 L550–553；PG3166 L3794（旧3773）表亲权利。
- K122：PG3166 L19960–20023/L15589–15639/L13624（旧13629–13637）；PG16804 L2302–2303；PG1684 L18393（原Skill未明说话者，不补猜）。
- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- HB08：PG16804 L663–668/L2658–2660（旧2659单行）。
- HB09：PG16804 L7045–7052/L7255–7261。
- HB10：PG16804全书；原条无单一行锚。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L13；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG1684**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K115：PG1437 L665–684；PG1586 L4561–4583；PG67123 L7333–7334（旧2370–2373）；PG1684 L3825–3828。
- K121：PG141 L65–72；PG1437 L1156–1161；PG3166 L1840–1851；PG1684 L3967；PG16804 L550–553；PG3166 L3794（旧3773）表亲权利。
- K122：PG3166 L19960–20023/L15589–15639/L13624（旧13629–13637）；PG16804 L2302–2303；PG1684 L18393（原Skill未明说话者，不补猜）。
- K126：PG22000 L3318–3367；PG1684 L15188–15189/L19666/L20990；PG1028 L3775–3784；PG3166 L21809–21824。
- K127：PG3166 L15329–15332/L15368；PG1684 L17719–17721/L17808；PG1028 L7759–7840。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- K133：PG1556 L556–563；PG1608 L7451/L8015–8016；PG1684 L41–46/L4512–4555；PG141 L15567（旧15259）；PG1028 L150–462。
- K134：PG141 L10589；PG1684 L18554–18555（旧18555单行）；PG22000书信/PG42812自述（本条原Skill未单给统一行锚）。
- HB15：PG1684 L17855–17915。
- HB27：PG1437 L1210–1214；PG1684 L41–46/L4512–4551（r5另列至4555）；PG3166 L23038–23061。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L25；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG22000**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K116：PG22000 L1543–1585/L3034–3056；PG4721 L5349–5353“永不隐瞒”为人物主张。
- K126：PG22000 L3318–3367；PG1684 L15188–15189/L19666/L20990；PG1028 L3775–3784；PG3166 L21809–21824。
- K134：PG141 L10589；PG1684 L18554–18555（旧18555单行）；PG22000书信/PG42812自述（本条原Skill未单给统一行锚）。
- HB13：PG22000 L3873–3909/L5567–5583。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L14；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG24000**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K130：PG1556 L2925–2971（旧窄锚2957）；PG24000 L9660–9671；PG3166 L24232–24256。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- K136：PG1028 L7873–7930；PG24000 L4417–4448；PG1245 L6646–6680。
- HB14：PG24000 L347–350/L5183–5202。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L21；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG3166**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：母亲Mary Scatcherd与女儿Mary Thorne分开；Frank爱女儿。书头称初版1858。 实读范围：L1–28/L820–990/L15580–15645/L23788–23812。

- K117：PG3166 实核L820–990（母亲L823–834，婴儿L937–985）/L15580–15645（Frank获知L15589–15639）/L23788–23812（女儿知继承及身世L23796–23809）。
- K118：PG1608 L2996–3007；PG544 L736–751；PG67123 L7392–7410；PG3166 L21723–21724；PG42812 L10721–10728。
- K119：PG3166 L21809–21824/L15674–15723/L5501–5502；PG77271 L1419–1424/L1935–1937；PG1586 L20191–20256。
- K121：PG141 L65–72；PG1437 L1156–1161；PG3166 L1840–1851；PG1684 L3967；PG16804 L550–553；PG3166 L3794（旧3773）表亲权利。
- K122：PG3166 L19960–20023/L15589–15639/L13624（旧13629–13637）；PG16804 L2302–2303；PG1684 L18393（原Skill未明说话者，不补猜）。
- K125：PG77271 L1771–1788；PG3166 L14730；PG4721 L7000–7016；PG544 L5804–5859；PG1608 L3827–3929。
- K126：PG22000 L3318–3367；PG1684 L15188–15189/L19666/L20990；PG1028 L3775–3784；PG3166 L21809–21824。
- K127：PG3166 L15329–15332/L15368；PG1684 L17719–17721/L17808；PG1028 L7759–7840。
- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K129：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- K130：PG1556 L2925–2971（旧窄锚2957）；PG24000 L9660–9671；PG3166 L24232–24256。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- HB19：PG3166 B17/B22（原卡仅区块号）。
- HB20：PG3166 B4/B9；PG141 B1/B3（区块定位）。
- HB22：PG3166 L23038–23061；PG544 B16。
- HB24：PG1608 L7641–7653；PG1586 L21999–22141；PG3166 L21356–21357/L21574。
- HB27：PG1437 L1210–1214；PG1684 L41–46/L4512–4551（r5另列至4555）；PG3166 L23038–23061。
- HB28：PG1028 L3775–3784；PG3166 L21809–21824。
- HB29：PG4721 B13/B15；PG3166 B22（区块定位）。
- HB30：PG3166 B9；PG1608 B6（B06 counterexamples CE30，仅区块）。
- HB37：PG3166 B23；具体获知L23796–23803。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L26；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG42812**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K113：PG121 L1460–1470/L3326–3350；PG1608 L1759–1809；PG42812 L1027–1093。
- K118：PG1608 L2996–3007；PG544 L736–751；PG67123 L7392–7410；PG3166 L21723–21724；PG42812 L10721–10728。
- K128：PG42812 L10740–10891；PG1586 L3788–3960/L5401–5429；PG16804 L2273–2274；PG1437 L793–819；PG1245 L11226–11368；PG3166 L12853–12869。
- K134：PG141 L10589；PG1684 L18554–18555（旧18555单行）；PG22000书信/PG42812自述（本条原Skill未单给统一行锚）。
- HB25：PG1608 L4265–4548；PG42812 L10740–10891。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L18；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG4721**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K116：PG22000 L1543–1585/L3034–3056；PG4721 L5349–5353“永不隐瞒”为人物主张。
- K120：PG544 L4501–4632；PG4721 L11533–11535。
- K124：PG4721 L3147–3148；PG1608 L2739–2745（病与十万开支）。
- K125：PG77271 L1771–1788；PG3166 L14730；PG4721 L7000–7016；PG544 L5804–5859；PG1608 L3827–3929。
- K135：PG544 L4501–4632；PG4721 L11533–11535/L11395–11403；PG1586 L24876。
- HB11：PG4721 L5180–5196/L5691–5697。
- HB12：PG4721 L3434–3454；PG67123 L3920–4002/L10006–10137。
- HB18：PG1586 B21；PG4721 B10/B15（原卡仅区块号）。
- HB29：PG4721 B13/B15；PG3166 B22（区块定位）。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L20；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG544**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K114：PG1437 L248–262/L580–584；PG121 L489（旧477–478）；PG544 L394–459。
- K118：PG1608 L2996–3007；PG544 L736–751；PG67123 L7392–7410；PG3166 L21723–21724；PG42812 L10721–10728。
- K120：PG544 L4501–4632；PG4721 L11533–11535。
- K125：PG77271 L1771–1788；PG3166 L14730；PG4721 L7000–7016；PG544 L5804–5859；PG1608 L3827–3929。
- K132：PG544 L6499–6676；PG1437 L1746–1758；PG1556 L4126–4137。
- K135：PG544 L4501–4632；PG4721 L11533–11535/L11395–11403；PG1586 L24876。
- HB21：PG544 L116–118/L4483–4493。
- HB22：PG3166 L23038–23061；PG544 B16。
- HB26：PG1608 L7453–8164；PG544 L4501–4632。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L16；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG67123**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K115：PG1437 L665–684；PG1586 L4561–4583；PG67123 L7333–7334（旧2370–2373）；PG1684 L3825–3828。
- K118：PG1608 L2996–3007；PG544 L736–751；PG67123 L7392–7410；PG3166 L21723–21724；PG42812 L10721–10728。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- HB12：PG4721 L3434–3454；PG67123 L3920–4002/L10006–10137。
- HB23：PG77271 L4621–4746；PG67123 L10147–10153。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L19；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

**PG77271**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：书头称First published in 1929；不是Austen执笔。别名不冒称本窗已证。 实读范围：L1–100，标题署名L1–9，初版声明L21。

- K112：PG77271 L774–802/L805–810/L1599–1603/L1970–2039。
- K119：PG3166 L21809–21824/L15674–15723/L5501–5502；PG77271 L1419–1424/L1935–1937；PG1586 L20191–20256。
- K125：PG77271 L1771–1788；PG3166 L14730；PG4721 L7000–7016；PG544 L5804–5859；PG1608 L3827–3929。
- K131：PG77271 L4621–4643/L4741–4746；PG67123 L10147–10153；PG1608 L8015–8164；PG16804 L7255–7261；PG1684 L23303–23307；PG3166 L23848–23849；PG121 L7915–7982；PG24000 L15574–15576。
- HB23：PG77271 L4621–4746；PG67123 L10147–10153。
- HB32：PG77271 L4010–4022。
- HB33：PG77271 L1771–1786。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-06/rounds/round-p4-agent2-final-2026-10-30/output/romance-craft-b06/sources-index.md` L10；源Skill SHA256 `6ff4a96dc91f04319e883a78ba6f955905a1608d0fa50a4ad893599546410cfb`。

## B-03-B07

| PG | 作品 | 责任者/责任关系 | 原报告总行数 | PG字节摘要 | 当前机制/历史条件 |
|---|---|---|---|---|---|
| PG11901 | Tommy and Grizel | Barrie, 1900 | NOT_DECLARED | SHA256前16位 e67ee89630fcfd1f | K152, K153, K157 |
| PG15402 | What Answer? | Dickinson | NOT_DECLARED | SHA256前16位 d20d5ca8cd1ff8ba | K143 |
| PG1621 | Miss or Mrs.? | Collins | NOT_DECLARED | SHA256前16位 5c60fb532a37abfe | K139, K147 |
| PG177 | The American | James, 1877 | NOT_DECLARED | SHA256前16位 278588f09727090b | K140, K149 |
| PG22002 | A Simple Story | Inchbald, 1791 | NOT_DECLARED | SHA256前16位 f057926e27cfea47 | K140, K148, K157 |
| PG25001 | An Old Man's Love | Trollope | NOT_DECLARED | SHA256前16位 6b51dc97f1c71772 | K142, K152 |
| PG26001 | The Bertrams | Trollope | NOT_DECLARED | SHA256前16位 465c6a911d7ad044 | K154 |
| PG2870 | Washington Square | James, 1880 | NOT_DECLARED | SHA256前16位 0b30c622280c790d | K141, K143, K144, K146, K147, K149 |
| PG39865 | Margaret Vincent | Clifford | NOT_DECLARED | SHA256前16位 89528adfa7065ffd | K147, K150, K153 |
| PG44374 | The Robber Baron of Bedford Castle | A. J. Foster and E. E. Cuthell（保留书头缩写，不猜全名） | 5833 | SHA256 e7114179c6867193d9a08fa26195574e124d306cd425e4b3b755b314f006a25e | K140 |
| PG4600 | A Hazard of New Fortunes | Howells | NOT_DECLARED | SHA256前16位 dd59641372931ee9 | K138 |
| PG57099 | Miss Crespigny | Burnett | NOT_DECLARED | SHA256前16位 4dba04d716c570f9 | K142, K143, K145, K151, K152, K153 |
| PG700 | The Old Curiosity Shop | Dickens | NOT_DECLARED | SHA256前16位 3c5e12af44a8a59c | K137, K150 |
| PG78710 | In Doors and Out | Oliver Optic | NOT_DECLARED | SHA256前16位 0a3a026fa2782c92 | K138, K143 |
| PG79505 | The Ladies of Lyndon | Kennedy, 1923 | NOT_DECLARED | SHA256前16位 6f40dddc826568aa | K142, K152, K157 |
| PG805 | This Side of Paradise | Fitzgerald, 1920 | NOT_DECLARED | SHA256前16位 a4e1b8c450e0d034 | K154, K157 |
| PG8203 | A Modern Instance | William Dean Howells | 16401 | SHA256 815c6624ac8ba3d913cbc8262f3659e3ee0554065bc59bedb4eca8b0619e8b0e | K155, K156 |
| PG9182 | Villette | Brontë, 1853 | NOT_DECLARED | SHA256前16位 31816e4d475820d9 | K142, K143, K147, K150, K151 |

### 当前锚点及来源元数据证据

**PG11901**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K152：PG25001 L7726–7727；PG57099 L3992–4001；PG79505 L11701–11706/L11793–11798；PG11901 L7103–7106/L7140–7147。
- K153：PG11901 L1033–1148/L1090–1094/L1506–1507/L13868–13872；PG39865 L332–340；PG57099 L3443–3444/L3491–3493。
- K157：B07 source-roles-b03b07 L29–31；PG22002 1791；PG79505 1923；PG805 1920；PG11901 1900。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L8；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG15402**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K143：PG15402 L140–145为上游核引，机制窗口另列L140–174；PG78710 L217–227；PG2870/PG9182/PG57099困境开场。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L9；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG1621**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K139：PG1621 L3361–3363/L3526–3550。
- K147：PG2870 L6702–6705；PG1621 L3361–3363；PG39865 L332–340；PG9182 L392–395。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L10；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG177**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K140：PG177门第（来源未列精确行）；PG22002 L168–170；PG44374 L2897–2898/L5479–5488。
- K149：PG2870 L7413–7418/L6854–6856；PG177 L14566–14570/L14710–14713。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L11；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG22002**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K140：PG177门第（来源未列精确行）；PG22002 L168–170；PG44374 L2897–2898/L5479–5488。
- K148：PG22002 L12541–12542。
- K157：B07 source-roles-b03b07 L29–31；PG22002 1791；PG79505 1923；PG805 1920；PG11901 1900。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L12；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG25001**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K142：PG25001 L273–278/L7726–7727；PG9182 L392–395/L21024–21025；PG57099 L3992–4001；PG79505 L11701–11706。
- K152：PG25001 L7726–7727；PG57099 L3992–4001；PG79505 L11701–11706/L11793–11798；PG11901 L7103–7106/L7140–7147。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L13；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG26001**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K154：PG26001 L25166–25167/L25099–25100；PG805 L46–47/L425–426。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L14；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG2870**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K141：PG2870 L6912–6923/L6789–6792/L6702–6705/L6278–6279。
- K143：PG15402 L140–145为上游核引，机制窗口另列L140–174；PG78710 L217–227；PG2870/PG9182/PG57099困境开场。
- K144：PG2870 L7321/L7334/L7413–7418。
- K146：PG2870 L7454–7458/L7258–7269。
- K147：PG2870 L6702–6705；PG1621 L3361–3363；PG39865 L332–340；PG9182 L392–395。
- K149：PG2870 L7413–7418/L6854–6856；PG177 L14566–14570/L14710–14713。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L15；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG39865**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K147：PG2870 L6702–6705；PG1621 L3361–3363；PG39865 L332–340；PG9182 L392–395。
- K150：PG9182 L21186；PG39865 L8911–8914；对照PG700 L23424–23430。
- K153：PG11901 L1033–1148/L1090–1094/L1506–1507/L13868–13872；PG39865 L332–340；PG57099 L3443–3444/L3491–3493。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L16；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG44374**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：当前底本1903；不自动称首版；两位共同责任者均保留。 实读范围：L1–80，署名L21，底本年L28。

- K140：PG177门第（来源未列精确行）；PG22002 L168–170；PG44374 L2897–2898/L5479–5488。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L17；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG4600**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K138：PG4600 L148–149；PG78710 L217–227/L75–80。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L18；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG57099**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K142：PG25001 L273–278/L7726–7727；PG9182 L392–395/L21024–21025；PG57099 L3992–4001；PG79505 L11701–11706。
- K143：PG15402 L140–145为上游核引，机制窗口另列L140–174；PG78710 L217–227；PG2870/PG9182/PG57099困境开场。
- K145：PG57099 L3408–3409/L3443–3444/L3491–3493。
- K151：PG9182 L10640/L10642–10647；PG57099 L4056–4057/L4263–4265。
- K152：PG25001 L7726–7727；PG57099 L3992–4001；PG79505 L11701–11706/L11793–11798；PG11901 L7103–7106/L7140–7147。
- K153：PG11901 L1033–1148/L1090–1094/L1506–1507/L13868–13872；PG39865 L332–340；PG57099 L3443–3444/L3491–3493。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L19；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG700**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K137：PG700 L433–434/L23526–23527/L23424–23430；完整终段窗口上游列L23424–23588。
- K150：PG9182 L21186；PG39865 L8911–8914；对照PG700 L23424–23430。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L20；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG78710**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K138：PG4600 L148–149；PG78710 L217–227/L75–80。
- K143：PG15402 L140–145为上游核引，机制窗口另列L140–174；PG78710 L217–227；PG2870/PG9182/PG57099困境开场。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L21；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG79505**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K142：PG25001 L273–278/L7726–7727；PG9182 L392–395/L21024–21025；PG57099 L3992–4001；PG79505 L11701–11706。
- K152：PG25001 L7726–7727；PG57099 L3992–4001；PG79505 L11701–11706/L11793–11798；PG11901 L7103–7106/L7140–7147。
- K157：B07 source-roles-b03b07 L29–31；PG22002 1791；PG79505 1923；PG805 1920；PG11901 1900。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L22；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG805**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K154：PG26001 L25166–25167/L25099–25100；PG805 L46–47/L425–426。
- K157：B07 source-roles-b03b07 L29–31；PG22002 1791；PG79505 1923；PG805 1920；PG11901 1900。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L23；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG8203**：当前知识详见所列K/HB；元数据不是另一套执行指令。
原文裁定：Bartley已死；Halleck拟向Marcia求婚，Atherton/Clara争论，未裁定/未成婚。 实读范围：书头L1–25与L16255–16401。

- K155：PG8203 实核L16283–16300/L16309–16344/L16346–16401，尤其L16390–16395/L16400–16401。
- K156：PG8203 实核L16302–16307。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L24；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

**PG9182**：当前知识详见所列K/HB；元数据不是另一套执行指令。

- K142：PG25001 L273–278/L7726–7727；PG9182 L392–395/L21024–21025；PG57099 L3992–4001；PG79505 L11701–11706。
- K143：PG15402 L140–145为上游核引，机制窗口另列L140–174；PG78710 L217–227；PG2870/PG9182/PG57099困境开场。
- K147：PG2870 L6702–6705；PG1621 L3361–3363；PG39865 L332–340；PG9182 L392–395。
- K150：PG9182 L21186；PG39865 L8911–8914；对照PG700 L23424–23430。
- K151：PG9182 L10640/L10642–10647；PG57099 L4056–4057/L4263–4265。
- 身份来源：`distill/分类蒸馏/16-类型小说专项/02-言情爱情/批次-07/rounds/round-p4-final-2026-10-30/output/romance-craft-b03-b07/references/source-roles-b03b07.md` L25；源Skill SHA256 `9c1d3d7fe2befeb112ed2c992f042bc2e12a181d820e2aeadd8cd76b12290e73`。

## 历史许可与引用条件

Gutenberg版本的public-domain/USA等原声明仅限其版本与司法范围，不授予其他译本、影印或现代版许可。此处没有重新作法律核验；源Skill内部许可/版本号不冒充第三方授权。原行锚对应固定整本阅读版，不是印刷页码；换版本需重核。

## PG5066 逐章共同作者

| 原PG行 | 章节 | 责任者 |
|---|---|---|
| 22 | The Father | William Dean Howells |
| 23 | The Old-Maid Aunt | Mary E. Wilkins Freeman |
| 24 | The Grandmother | Mary Heaton Vorse |
| 25 | The Daughter-in-Law | Mary Stewart Cutting |
| 26 | The School-Girl | Elizabeth Jordan |
| 27 | The Son-in-Law | John Kendrick Bangs |
| 28 | The Married Son | Henry James |
| 29 | The Married Daughter | Elizabeth Stuart Phelps |
| 30 | The Mother | Edith Wyatt |
| 31 | The School-Boy | Mary Raymond Shipman Andrews |
| 32 | Peggy | Alice Brown |
| 33 | The Friend of the Family | Henry Van Dyke |
