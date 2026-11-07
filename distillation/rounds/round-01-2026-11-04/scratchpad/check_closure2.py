# -*- coding: utf-8 -*-
import re, os

ROOT = "/Users/aizou/Desktop/工作台/distillation-space/distill-release-chronology/distillation/rounds/round-01-2026-11-04"
c = open(os.path.join(ROOT, "notes/w4-closure-2026-11-05.md"), encoding="utf-8").read()
q = open(os.path.join(ROOT, "notes/w4-review-queue.md"), encoding="utf-8").read()

ids_q = sorted({int(m) for m in re.findall(r"W4-(\d+)", q)})
print("queue unique:", len(ids_q), "holes:", [i for i in range(1, max(ids_q)+1) if i not in ids_q])

sec1 = c.split("## 一、逐条定档")[1].split("## 二、净账")[0]
sec2 = c.split("## 二、净账")[1].split("## 三、")[0]

FIRST = {"已修": "已修", "已销": "已销", "B.2": "B2", "并入": "并入", "交作者": "作者", "未闭合": "未闭合"}
rows1 = {}
for m in re.finditer(r"^\| (W4-[\d／／、…]+) \| ([^|]+?) \|", sec1, re.M):
    ids_txt, label = m.group(1), m.group(2).strip()
    bucket = None
    for k, v in FIRST.items():
        if label.startswith(k):
            bucket = v
    if bucket is None:
        print("UNMAPPED LABEL:", ids_txt, "->", label[:40])
        continue
    for n in re.findall(r"W4-(\d+)", ids_txt):
        rows1.setdefault(int(n), []).append(bucket)

dup1 = {k: v for k, v in rows1.items() if len(v) > 1}
print("section1 rows cover:", len(rows1), "duplicated assignments:", sorted(dup1))

bucket2 = {}
for name, n, body in re.findall(r"\|\s*([^|]+?)\s*\|\s*\*\*(\d+)\*\*\s*\|([^|]+)\|", sec2):
    body2 = re.sub(r"W4-", " ", body)
    nums = sorted({int(x) for x in re.findall(r"(?<![\d])(\d{1,3})(?![\d])", body2)})
    key = None
    for k, v in FIRST.items():
        if name.strip().startswith(k):
            key = v
    bucket2[key] = nums
    print("%-8s claim=%3d actual=%3d %s" % (key, int(n), len(nums), "OK" if int(n) == len(nums) else "MISMATCH"))

total = sum(len(v) for v in bucket2.values())
allids = sorted(set(x for v in bucket2.values() for x in v))
print("bucket total:", total, "unique:", len(set(allids)), "== queue:", len(ids_q))
print("not bucketed:", [i for i in ids_q if i not in set(allids)])
print("not in section1:", [i for i in ids_q if i not in rows1])

# cross-check section1 label vs section2 membership
conf = []
for i, bs in sorted(rows1.items()):
    b2 = [k for k, v in bucket2.items() if i in v]
    if sorted(set(bs)) != sorted(b2):
        conf.append((i, bs, b2))
print("label/membership mismatches:", len(conf))
for x in conf[:20]:
    print("   ", x)
