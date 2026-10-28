import json

path = 'content/questions/el-GR/cinema_tv_hard.json'
with open(path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if 'categoryId' not in q or not q['categoryId']:
        q['categoryId'] = 'cinema_tv'
    if 'difficulty' not in q or not q['difficulty']:
        q['difficulty'] = 5
    if 'locale' not in q or not q['locale']:
        q['locale'] = 'el-GR'
    if 'status' not in q or not q['status']:
        q['status'] = 'reviewed'
    if 'verifiedAt' not in q or not q['verifiedAt']:
        q['verifiedAt'] = '2026-10-25'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print('Fixed cinema_tv_hard.json successfully.')
