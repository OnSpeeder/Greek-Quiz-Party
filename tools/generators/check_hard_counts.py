import glob, json

for f in sorted(glob.glob('content/questions/el-GR/*_hard.json')):
    with open(f, encoding='utf-8') as fp:
        data = json.load(fp)
        cnt = len(data) if isinstance(data, list) else len(data.get('questions', []))
        print(f"{f}: {cnt}")

