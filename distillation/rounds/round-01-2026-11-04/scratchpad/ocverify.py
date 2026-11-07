#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""operations-contract 行锚点通用核验：抽出全部 `file:N` / `file:N–M` 引用，
解析到包内真实文件（basename 匹配，必要时按给定子目录优先），断言在行数范围内。
用法：python3 ocverify.py <contract.md> <pkg_dir>"""
import os, re, sys

contract, pkg = sys.argv[1], sys.argv[2]

index = {}
for root, dirs, files in os.walk(pkg):
    for f in files:
        if f.endswith((".md", ".yaml", ".json")):
            index.setdefault(f, []).append(os.path.join(root, f))

txt = open(contract, encoding="utf-8").read()
CIT = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|yaml|json)):([0-9]+)(?:\u2013([0-9]+))?`")
rows = CIT.findall(txt)
print("引用数:", len(rows))
cache, bad = {}, []
for path, a, b in rows:
    base = path.split("/")[-1]
    cands = index.get(base, [])
    if "/" in path:
        cands = [c for c in cands if c.replace(pkg + "/", "").startswith(path) or c.endswith(path)]
    if not cands:
        bad.append(("NOFILE", path, a)); continue
    p = sorted(cands, key=lambda c: (pkg not in c, len(c)))[0]
    n = cache.setdefault(p, sum(1 for _ in open(p, encoding="utf-8")))
    hi = int(b) if b else int(a)
    if hi > n or int(a) < 1 or int(a) > hi:
        bad.append(("OUT_OF_RANGE", os.path.relpath(p, pkg), a, b, n))
uniq = {}
for path, a, b in rows:
    uniq.setdefault(path.split("/")[-1], 0)
    uniq[path.split("/")[-1]] += 1
print("被引文件分布:", uniq)
if bad:
    for x in bad:
        print("  BAD", x)
    sys.exit(1)
print("全部行锚点在范围内: OK")
