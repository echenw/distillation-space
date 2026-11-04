from pathlib import Path
import hashlib,json
spec={"PG2019":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/01-推理悬疑刑侦/PG2019-The-Bat/整本阅读版.txt","PG8778":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/12-异世界与穿越/PG8778-The-Water-of-the-Wondrous-Isles/整本阅读版.txt","PG11499":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/12-异世界与穿越/PG11499-An-Essence-of-the-Dusk-5th-Edition/整本阅读版.txt","PG69394":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/12-异世界与穿越/PG69394-The-dream-A-novel/整本阅读版.txt","PG79426":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/03-恐怖惊悚怪谈/PG79426-The-libertine-vol-2-of-4/整本阅读版.txt","PG79428":"/Users/aizou/Desktop/工作台/knowledge-distillation-workspace/archives/novel-craft-history/_source-store/novel-craft-reference-library-20261021-r12/分类/16-类型小说专项/03-恐怖惊悚怪谈/PG79428-The-libertine-vol-4-of-4/整本阅读版.txt"}
for pg,path in spec.items():
 p=Path(path);raw=p.read_bytes();ls=raw.decode('utf-8-sig').splitlines()
 print('# '+pg);print('source: '+path);print('sha256: '+hashlib.sha256(raw).hexdigest());print('total_lines: '+str(len(ls)));print('## Original L1-60')
 for n in range(1,min(60,len(ls))+1):print(str(n)+': '+ls[n-1])
 m=p.parent/'metadata.json'
 if m.is_file():
  data=json.loads(m.read_text());print('metadata_source: '+str(m));print('metadata_sha256: '+hashlib.sha256(m.read_bytes()).hexdigest());print('metadata_keys: '+json.dumps(list(data),ensure_ascii=False));print('identity_metadata: '+json.dumps({k:v for k,v in data.items() if any(s in k.lower() for s in ['title','author','creator','pg_id','ebook','gutenberg','publish','release','language','date'])},ensure_ascii=False))
 else:print('metadata_json_present: false')
 print('END '+pg)
