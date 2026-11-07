# 修复批重绑台账（K5，2026-11-06）

- Owner：主代理。权威绑定表＝`notes/k5-bindings-2026-11-06.tsv`（修复后树）；`notes/k5-bindings-2026-11-05.tsv` 按 A.3 原样保留，是修复前树的历史证据，不覆盖。
- 算法：照 `skills/knowledge-compiler/scripts/kd_round_output.py:123-127` —— 相对包根路径按 `path.encode('utf-8')` 升序 → 逐行 `"<relpath>\t<sha256(文件原始字节)>\n"` → 对该拼接串再取 SHA-256。整树同理，根为 `output/`。
- 复测：主代理与独立只读复核席 B 各自独立复算 8 包树哈希，**8/8 逐包全等**。

## 一、修复后整树冻结值

| 项 | 值 |
|---|---|
| `output/` 文件数 | **217** |
| `output/` 总字节 | **2,361,511** |
| `output/` 两级整树 SHA-256 | **`d86672d4497c03b64b3861ef3750a600f82075c56d370219f26fe4d45de8df2c`** |
| `inputs/requirements.md` SHA-256 | `63f1f746556016dceb63de27684362f0116be944f207be3528da8dffcc689df5` |
| 修复前整树参照（§四十七） | `796c8fc18921170adf735c92f0a0850b009b64ce8f73197a9d5cbe4addf13b03`（217 件／2,344,850 B） |

净变化：**+16,661 B / 217 件**（件数不变，全部为行内改文）。

## 二、8 包新树绑定（详见 tsv）

| 包 | tree_sha256（前 12） | 件数 | 字节 | brief_sha256（前 12） |
|---|---|---|---|---|
| character-and-narrative-control | `3355d7cad855` | 17 | 194854 | `012e356f3982` |
| cross-media-drama-adaptation | `d752c6c946c0` | 13 | 75549 | `259673418912` |
| fiction-planning-and-diagnosis | `fc894f67d481` | 27 | 349507 | `69ddd2b7f907` |
| genre-fiction-craft | `067fa13ea075` | 101 | 1058396 | **`7d5e5c847c957`**（本批改 brief） |
| line-editing-and-proofreading | `4248dc050cae` | 10 | 114289 | `9d29bd3cfe72` |
| preset-card-generation | `ce734911aa2c` | 11 | 115304 | `cfe0c1fdf92f` |
| scene-conflict-and-rhythm | `2cdf8c5cea06` | 17 | 169017 | `239610b5eaec` |
| story-architecture-and-longform-planning | `b84b6e70591e` | 21 | 284595 | `8537a5662c2d` |

仅 `genre-fiction-craft/brief.json` 被收口席 A 改动（F-01 六处／F-05 八处／F-06／W4-116），其 brief SHA 由 `7872b791…` 变为 `7d5e5c84…`；其余 7 份 brief 本批未改，`shasum -a 256` 实测与基线逐包相等。

## 三、主代理裁定：8 份正式 review.json 不改（重要）

**事实**：8 份 `notes/quality/*/review.json` 的 `status` 均为 `review-independent-r1`，`reviewer` 明记「只读子代理，非作者」（计划第 10 节 D3-C）。它们绑定的是**修复前树**，其 `brief_sha256`／`skill_tree_sha256`／`bound_to_tree_sha`／`sections.interfaces[].peer_tree_sha256` 等字段全部是修复前实测值；`gq` 与 `findings` 的结论也基于修复前行号与文本。

**裁定**：独立只读复核席 B 建议把这些字段刷新为现树值（并指出 genre peer 旧值有 4 种、散落 ≥7 份，工作单 §四「三份」口径不足）。**本席不采纳该改写**，理由：

1. 这些文件是**非作者独立复核的证据**。由主代理（成品作者侧）批量改写其绑定 SHA，会使一份针对旧树的复核结论看起来像针对新树，构成「把未观察到的结果写成通过」，违反计划第 8 节与用户规则「不自审自过、不伪装成功」。
2. 修复批只做静态文本落笔，**未对修复后树重做独立隔离回读**；GQ1–GQ4 的 pass／fail 档位不随修复批自动继承。席 B 亦明确「任何 GQ 主据消解不等于该 GQ 通过，档位变更须独立复测＋主代理裁定」。
3. 改写会同时使行号锚、findings 引文与 evidence 文本失效，需整份重做才自洽，不是字符串替换能完成的。

**替代处置（已落地）**：
- 8 份 `review.json` 原件**逐字节不动**，作为「修复前树的独立复核」历史证据保留。
- 新树的权威绑定＝本文件与 `k5-bindings-2026-11-06.tsv`；修复前绑定＝`k5-bindings-2026-11-05.tsv`。
- 在 `checklist.md` 与 `log.md` 如实标注：**修复后树的独立隔离回读（W4-r2）未执行**，需另行授权由非作者只读子代理重做；在此之前不得写「K4 8/8 对修复后树有效」。
- 工作单 §四「genre peer 三处旧值刷新」因此**未按字面执行**，这是有依据的范围收窄，交用户复核。

## 四、字段级失效清单（供 W4-r2 重做，不在本批改）

| 位置 | 失效内容 |
|---|---|
| 8 份 `review.json` 顶层 | `brief_sha256`、`skill_tree_sha256`、`tree_files/bytes`、`freeze_note`、`binding_method.*`、`bound_to_tree_sha.*` |
| 同上 | `bound_to_tree_sha.peers_measured.<pkg>.peer_tree_sha256`（7 个 peer 全旧） |
| 同上 | `sections.interfaces[].peer_tree_sha256`、`gq[].peer_tree_sha256[]`、`gq[].peers[]`、`peer_tree_sha256_measured[]`、`limits[].peer_tree_drift` |
| 同上 | `findings`／`evidence_ref` 里引用的修复前行号（R1–R8 造成位移：character `:277` 起 +2、fp `:45` 后 +6、scene `:275` 后 +1、line-editing `:109` 后 −1） |
| `delivery-preflight-spec/` | 各 spec 的树哈希占位已由收口席 A 改为「待主代理 K5 冻结」；本文件 §一 的实测值即冻结值，见下一节 |
| `k5-bindings-2026-11-05.tsv` | 保持原样（历史证据） |

## 五、preflight spec 的冻结值回填口径

收口席 A 把 spec 的哈希字段统一写成「待主代理 K5 冻结」占位并声明「不自造 SHA」。本席现以 §一 实测值冻结，但**采用「追加冻结回填节」而非逐字改写占位**：`INDEX.md` 追加一节列出 8 包完整 tree/brief SHA 与整树值，声明各 spec 表格内占位以该节为准；占位文字本身保留为修复批时点的历史记录。理由：占位同时出现在表格单元格与「本批不提前冻结」「本席不自造 SHA」等状态说明句中，逐字替换会使说明上下文与事实不符，制造新的不一致。

**`field_ids` 冻结（W4-09）维持未冻结**：席 A 与两席 spec 均注明「须由非作者按 `inputs/requirements.md` 判定哪些编号族真要求逐项可填」，属判定动作而非机械回填，本席不代裁、不提前冻结。

## 六、状态口径（不夸大）

- 已冻结：`output/` 整树两级 SHA、8 包 tree/brief SHA（新 tsv）、preflight spec 的树哈希占位回填。
- 未冻结：`field_ids`（W4-09，待非作者判定）。
- 未验证：修复后树的独立隔离回读、GQ1–GQ4 档位复议、**GQ5 恒 NOT_PROVEN**（真实任务测试未授权）。
- 未闭合：总账 §五 的 IF-01／IF-03／IF-05、Q6 档位重定、scene 第三处值域、cross-media GQ2 ①④⑥、character GQ2 S1–S3 等——见 `repair-ledger-2026-11-06.md` 与各分片 ledger，本批不代裁、不扩大范围。
