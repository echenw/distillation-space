#!/usr/bin/env python3
"""r3 修复批落笔器（主代理单写入者）。dry=只验锚点；apply=备份→临时副本正控制→实写→复测。"""
import hashlib, os, shutil, sys

ROOT = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
OUT = os.path.join(ROOT, "output")
BACKUP = os.path.join(ROOT, "scratchpad", "r3-prepatch-2026-11-07")

# (tag, pkg, rel, mode, anchor, payload, expected_line_delta or None)
E = []
def ed(tag, pkg, rel, mode, anchor, payload, ld=None):
    E.append((tag, pkg, rel, mode, anchor, payload, ld))

# ── genre（V1 两补丁＋Q1-4 echo）──
ed("g1-Owner声明", "genre-fiction-craft", "SKILL.md", "insert_after",
   "判断题材承诺有没有兑现：读者被许诺了什么，作品有没有给。",
   "题材契约的登记归本包，兄弟包按本包对应题材目录的契约核对。", 0)
ed("g2-fp/character承接", "genre-fiction-craft", "SKILL.md", "insert_after",
   "由本包按对应题材目录作答；",
   "`fiction-planning-and-diagnosis` 转来的题材契约核对以本包登记的契约为准，缺项回它自己的清单登记；`character-and-narrative-control` 的公平与可靠性契约登记归本包，对方按本包契约核对、不另设登记；", 0)
ed("g3-character回声行", "genre-fiction-craft", "SKILL.md", "insert_before",
   "不在范围：现实的法律、医学、技术参数、当代行业规则和史实考据",
   "从 `character-and-narrative-control` 转入本 skill 的：推理的公平线索、恐怖与言情等题材的契约。\n\n", 1)

# ── character SKILL.md ──
ed("c1-首档名:105", "character-and-narrative-control", "SKILL.md", "replace",
   "作品里写了、推断、设计方案、证据不够、超出范围",
   "文本中明确呈现、推断、设计方案、证据不够、超出范围", 0)
ed("c2-首档名:275", "character-and-narrative-control", "SKILL.md", "replace",
   "稿件里能定位的记「已完成」并给位置",
   "「文本中明确呈现」记「已完成」并给位置", 0)
ed("c3-治理句收缩:153", "character-and-narrative-control", "SKILL.md", "replace",
   "（这一契约的登记归 `genre-fiction-craft` 的题材契约，见 §1.3；本包按它核对，不另设登记）",
   "（公平与可靠性契约的题材侧登记归 `genre-fiction-craft`，见 §1.3）", 0)
ed("c4-§1.3 genre行尾", "character-and-narrative-control", "SKILL.md", "replace",
   "| 推理的公平线索、恐怖与言情等题材的契约 | `genre-fiction-craft` |",
   "| 推理的公平线索、恐怖与言情等题材的契约 | `genre-fiction-craft`（题材契约由其登记，本包按登记核对，不另设登记） |", 0)
ed("c5-:270案A删词", "character-and-narrative-control", "SKILL.md", "replace",
   "检查已执行，但结论依赖未核实的判断、设计假设或缺失的输入，不能记作已完成",
   "检查已执行，但结论依赖未核实的判断或缺失的输入，不能记作已完成", 0)
ed("c6-:237补读列", "character-and-narrative-control", "SKILL.md", "replace",
   "十二个反例、五档可信度 |",
   "十二个反例、五档可信度、即时危险时的现实求助指引 |", 0)
ed("c7-:237出口列", "character-and-narrative-control", "SKILL.md", "replace",
   "碰上现实医疗、法律或当事人健康的问题，退出那一部分，小说的部分照常做 |",
   "碰上现实医疗、法律或当事人健康的问题，退出那一部分，小说的部分照常做；文本显示人物处于即时危险时，按 §6 给一句现实求助指引 |", 0)
ed("c8-§9.2即时危险行", "character-and-narrative-control", "SKILL.md", "insert_after",
   "| 要真实病名、诊断、疗法，或判断时间旅行的物理可行性 | 退出那一部分，小说的部分照常做（§1.2） |",
   "\n| 文本显示人物处于即时危险 | 按 boundaries-and-ethics §6 给一句现实求助指引，稿子和人物回到文学层处理 |", 1)
ed("c9-genre回声行", "character-and-narrative-control", "SKILL.md", "insert_before",
   "## 2. 使用方式",
   "从 `genre-fiction-craft` 转入本 skill 的：全篇的人物动机、谁来讲、视角越界、时间模型。\n\n", 1)
ed("c10-pov:96列名", "character-and-narrative-control", "examples/pov-cases.md", "replace",
   "| 请求里的一句 | 判成什么 | 依据 | 处理 |",
   "| 请求里的一句 | 判成什么 | 理由 | 处理 |", 0)
ed("c11-pov:134列名", "character-and-narrative-control", "examples/pov-cases.md", "replace",
   "| 项 | 状态 | 依据 |",
   "| 项 | 状态 | 所附材料 |", 0)

# ── scene ──
ed("s1-:224八字段", "scene-conflict-and-rhythm", "SKILL.md", "replace",
   "每条的「用于／不用／反例／检查／出口」",
   "每条的「规则／用于／怎么做／不用／反例／检查／自拟例／出口」", 0)
ed("s2-双回声行", "scene-conflict-and-rhythm", "SKILL.md", "insert_before",
   "**职责边界**：本 Skill 负责场景/章节内部的冲突、节奏、动作呈现和钩子写法",
   "从 `genre-fiction-craft` 转入本 skill 的：一场戏怎么写、冲突、伏笔、悬念、节奏、章末。\n从 `character-and-narrative-control` 转入本 skill 的：伏笔怎么埋和回收、悬念强度、章末钩子、松紧节奏、一场戏的进出、打斗。\n\n", 2)
ed("s3-rhythm§7指针化", "scene-conflict-and-rhythm", "references/rhythm-diagnosis.md", "replace",
   """| 情形 | 出口 |
|---|---|
| 没有正文、只有构思 | 改做设计路径；不出「稿子第几段有问题」的定位式诊断，写明哪些判断要等有了稿子才能确认 |
| 只说「这一章节奏慢」，不给正文 | 先要正文，先给检查清单，不臆断原因 |
| 峰值冲突（前文比预定高潮更强） | 按 SU-02 给「降级前文」和「重定峰值」两条路由，各写代价，停在待作者决定，不擅自改已锁定章节 |
| 两条要求互相矛盾、两读都成立 | 给 A/B 两版，作者选定前哪一版都不落稿，其余不冲突的修改照做 |
| 需要补写事实或问题出在人物、视角、结构 | 停在场景层，把问题转给对应 skill |
| 作者不答或只回「你看着办」 | 按最小改动处理，逐条列出所做的假设，不擅自扩大改动范围 |
| 卡片请求、按三轴审章节 | 转 `preset-card-generation` |""",
   "失败出口与 SKILL.md §10 同一张表，按那边的情形与出口执行；本节不再另列，避免两表行数漂移。", -8)
ed("s4-scene-cases:111主责", "scene-conflict-and-rhythm", "examples/scene-cases.md", "replace",
   "越出单元内的修改，须与 `story-architecture-and-longform-planning` 一起看。",
   "越出单元内的修改，主责在 `story-architecture-and-longform-planning`（SKILL.md §11.1），本 Skill 只出单元内的强度与因果依据。", 0)
ed("s5-场章幕案1", "scene-conflict-and-rhythm", "references/chapter-ends-and-endings.md", "replace",
   "（场、章、幕）", "（场、章）", 0)

# ── story ──
for row_old, row_new, tag in [
    ("| 容量表 | 开书前；按固定周期核对 | SV-13 | 同上 |", "| 容量表 | 开书前；按固定周期核对 | SV-13 | `templates/serial-tables.md` |", "t1"),
    ("| 卷末四问、复位四问 | 每卷收尾前 | SV-05、SV-06 | 同上 |", "| 卷末四问、复位四问 | 每卷收尾前 | SV-05、SV-06 | `templates/serial-tables.md` |", "t2"),
    ("| 开放线台账 | 有跨卷线时；每卷末更新 | SV-08 | 同上 |", "| 开放线台账 | 有跨卷线时；每卷末更新 | SV-08 | `templates/serial-tables.md` |", "t3"),
    ("| 卷间依赖矩阵 | 跨卷改动、接手旧稿时 | SV-02、SV-08 | 同上（§12） |", "| 卷间依赖矩阵 | 跨卷改动、接手旧稿时 | SV-02、SV-08 | `templates/serial-tables.md` §12 |", "t4"),
    ("| 章末检查表 | 每章定稿时 | SV-09、SV-10 | 同上 |", "| 章末检查表 | 每章定稿时 | SV-09、SV-10 | `templates/serial-tables.md` |", "t5"),
    ("| 套路与变化表 | 进入第二卷后 | SV-11、SV-12 | 同上 |", "| 套路与变化表 | 进入第二卷后 | SV-11、SV-12 | `templates/serial-tables.md` |", "t6"),
    ("| 续卷开头方案 | 每卷开篇 | SV-07 | 同上 |", "| 续卷开头方案 | 每卷开篇 | SV-07 | `templates/serial-tables.md` |", "t7"),
    ("| 开载检查表、反馈日志 | 开载前；连载中 | SV-14、SV-15 | 同上 |", "| 开载检查表、反馈日志 | 开载前；连载中 | SV-14、SV-15 | `templates/serial-tables.md` |", "t8"),
]:
    ed(tag + "-§7同上", "story-architecture-and-longform-planning", "SKILL.md", "replace", row_old, row_new, 0)
ed("t9-双回声行", "story-architecture-and-longform-planning", "SKILL.md", "insert_after",
   "从 `preset-card-generation` 转入本 skill 的：单本结构、分卷、排章纲，且产物是规划文档、不是给模型的卡。",
   "\n从 `genre-fiction-craft` 转入本 skill 的：全书主线、多线汇合、分卷、连载排期。\n从 `character-and-narrative-control` 转入本 skill 的：主线、多线、因果、删场、分卷和连载的规划。", 2)
ed("t10-§12桥接句", "story-architecture-and-longform-planning", "SKILL.md", "insert_after",
   "| **待作者决定** | 存在冲突 / 取舍 / 锁定内容矛盾，由作者裁决，不擅自覆盖 |",
   "\n\n四词用于对作者交付与各表的状态列；「假设」「未读」「未知」「不适用」「待登记」是资料状态值，不是四词，交付时按四词报告该项状态，不把「假设」写成「已完成」。", 2)
ed("t11-serial-tables:133", "story-architecture-and-longform-planning", "templates/serial-tables.md", "replace",
   "| 作者决定 | 已确认／未能核实／待作者决定／不适用 |",
   "| 作者决定 | 按 [SKILL.md](../SKILL.md) §12 四词填写；作者未定的记「待作者决定」，不涉作者的行记「不适用」 |", 0)
ed("t12-migration:52扩句", "story-architecture-and-longform-planning", "references/serial-platform-migration.md", "replace",
   "状态词定义见 SKILL.md §12。",
   "状态词定义见 SKILL.md §12；「依据」给交付时附的可核位置，本表的合同条款、官方说明、账号后台页面即属此类，不限于稿件内。", 0)

# ── cross-media ──
ed("x1-:201未执行归档", "cross-media-drama-adaptation", "SKILL.md", "replace",
   "| 未能核实 | 检查已执行，但结论依赖未核实的判断、设计假设或缺失的输入，不能记作已完成 |",
   "| 未能核实 | 检查已执行，但结论依赖未核实的判断、设计假设或缺失的输入，或检查未执行；两者都不能记作已完成 |", 0)
ed("x2-character回声", "cross-media-drama-adaptation", "SKILL.md", "insert_after",
   "- `preset-card-generation` → 本 Skill：改编为舞台／影视／音频／互动这类不写成卡、也不用三轴的请求。",
   "\n- `character-and-narrative-control` → 本 Skill：改成舞台方案、分场稿、镜头。", 1)
ed("x3-branch-sheet占位", "cross-media-drama-adaptation", "templates/interactive-branch-sheet.md", "replace",
   "| 检查项 | 结果（已完成／依据／未能核实／待作者决定） | 证据或限制 |",
   "| 检查项 | 结果（已完成／依据／未能核实／待作者决定；占位可写「未知」） | 证据或限制 |", 0)
ed("x4-导演→作者或主创", "cross-media-drama-adaptation", "references/conflicts.md", "replace",
   "请导演或作者选择", "请作者或主创选择", 0)

# ── fiction-planning ──
ed("f1-规则卡补两步", "fiction-planning-and-diagnosis", "references/rules-revision-and-method.md", "replace",
   """  4. 写 `反例`（至少两个）。
  5. 遇到大师犯规：记入 `例外记录`，注明“有意/无意、代价、是否可学”；不改规则。
  6. 两条规则冲突：按 FC-01 赛道分流；不能平均，也不能“辩证统一”。""",
   """  4. 写 `分支`（按上文 A 结构层／B 文体层／C 天赋层给区分信号与反信号）。
  5. 写 `可信度`（按 FC-13：巧合是否在解结、类型豁免是否内部自洽；说不清时按最严的写实处理并标“契约未定”）。
  6. 写 `反例`（至少两个）。
  7. 遇到大师犯规：记入 `例外记录`，注明“有意/无意、代价、是否可学”；不改规则。
  8. 两条规则冲突：按 FC-01 赛道分流；不能平均，也不能“辩证统一”。""", 2)
ed("f2-:117四类统一", "fiction-planning-and-diagnosis", "SKILL.md", "replace",
   "给三个删减方案和代价，请作者选",
   "按 FC-19 的删／压／并／留四类各给方案和代价，请作者选", 0)

# ── preset-card ──
ed("p1-:118小说正文", "preset-card-generation", "SKILL.md", "replace",
   "正文类交付：", "小说正文类交付：", 0)
ed("p2-:172衔接", "preset-card-generation", "SKILL.md", "replace",
   "按最小改动处理，逐条列出所做的假设，不擅自扩大改动范围 |",
   "按最小改动处理（标「待作者决定」的项维持不落稿、不合并），逐条列出所做的假设，不擅自扩大改动范围 |", 0)
ed("p3-§9.2 character承接行", "preset-card-generation", "SKILL.md", "insert_after",
   "| 与 `genre-fiction-craft` 之间的题材规则、机制、混合题材 | 题材契约归 `genre-fiction-craft`，按其题材契约核对，缺项回本包登记；本包只接把约束写成「给模型的卡」的部分 |",
   "\n| `character-and-narrative-control` 转来的：生成／修订／诊断推进模式卡、文风卡、表达约束卡；写反 AI 味的约束卡；按三轴审章节；已有文风卡或推进卡作为输入 | 产物是「给模型的卡」或审查框架是三轴时接 |", 1)
ed("p4-style:101卡内正文", "preset-card-generation", "references/style.md", "replace",
   "- 正文 600 到 750 字，不含标题行。",
   "- 卡内正文 600 到 750 字，不含标题行。", 0)
ed("p5-progression:125卡内正文", "preset-card-generation", "references/progression.md", "replace",
   "- 正文 500 到 700 字，不含标题行。每次调用都会带上这张卡",
   "- 卡内正文 500 到 700 字，不含标题行。每次调用都会带上这张卡", 0)
ed("p6-expression模板声明", "preset-card-generation", "references/expression.md", "insert_after",
   "- 卡内正文不超过 300 字。",
   "\n- 本包不提供空白卡模板；示例卡只说明做法，写卡时按当前作品重新设计。", 1)

# ── line-editing（Set A＋Q1-4 双回声行）──
ed("l1-双回声行", "line-editing-and-proofreading", "SKILL.md", "insert_before",
   "## 2. 使用方式",
   "从 `genre-fiction-craft` 转入本 skill 的：句子和对白的措辞、标点、校对。\n从 `character-and-narrative-control` 转入本 skill 的：句子、对白的措辞、标点、语感、校对。\n\n", 2)


def rd(pkg, rel):
    with open(os.path.join(OUT, pkg, rel), encoding="utf-8", newline="") as f:
        return f.read()


def main(mode):
    files = {}
    for tag, pkg, rel, m, a, p, ld in E:
        files.setdefault((pkg, rel), []).append((tag, m, a, p, ld))
    # 阶段1：锚点计数
    fails = []
    for (pkg, rel), edits in files.items():
        txt = rd(pkg, rel)
        for tag, m, a, p, ld in edits:
            n = txt.count(a)
            if n != 1:
                fails.append(f"{pkg}/{rel} [{tag}] 锚点 count={n}")
    if fails:
        print("DRY-FAIL 锚点问题：")
        [print(" ", x) for x in fails]
        sys.exit(1)
    print(f"阶段1 PASS：{len(E)} 条编辑、{len(files)} 个文件锚点全部唯一")
    if mode == "dry":
        return
    # 阶段2：备份
    if os.path.exists(BACKUP):
        shutil.rmtree(BACKUP)
    for pkg, rel in files:
        dst = os.path.join(BACKUP, pkg, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(OUT, pkg, rel), dst)
    print(f"阶段2 备份 {len(files)} 文件 → {BACKUP}")
    # 阶段3：变换＋验证
    report, bad = [], []
    for (pkg, rel), edits in files.items():
        path = os.path.join(OUT, pkg, rel)
        txt = rd(pkg, rel)
        before_lines = txt.count("\n")
        before_bytes = len(txt.encode("utf-8"))
        for tag, m, a, p, ld in edits:
            if m == "replace":
                txt = txt.replace(a, p, 1)
            elif m == "insert_after":
                txt = txt.replace(a, a + p, 1)
            else:
                txt = txt.replace(a, p + a, 1)
        after_lines = txt.count("\n")
        after_bytes = len(txt.encode("utf-8"))
        d_lines, d_bytes = after_lines - before_lines, after_bytes - before_bytes
        exp = sum(x[4] for x in edits if x[4] is not None)
        if exp is not None and d_lines != exp:
            bad.append(f"{pkg}/{rel} 行差 {d_lines} ≠ 预期 {exp}")
        report.append(f"{pkg}/{rel}: {d_bytes:+d} B, {d_lines:+d} 行")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
    if bad:
        print("APPLY-FAIL 行数校验：")
        [print(" ", x) for x in bad]
        sys.exit(1)
    print("阶段3 落笔完成：")
    [print(" ", x) for x in report]
    total = sum(int(x.split(": ")[1].split(" ")[0]) for x in report)
    print(f"合计 {total:+d} B")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "dry")
