import glob
import json
import os

all_files = glob.glob("content/questions/el-GR/*_*.json")

diff_map = {
    "easy": 1,
    "medium": 3,
    "hard": 5
}

fixed_total = 0

for file_path in all_files:
    filename = os.path.basename(file_path).replace(".json", "")
    parts = filename.rsplit("_", 1)
    if len(parts) != 2:
        continue
    cat_id, diff_str = parts[0], parts[1]
    diff_num = diff_map.get(diff_str, 1)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for q in data:
        if q.get("categoryId") != cat_id:
            q["categoryId"] = cat_id
            changed = True
        if q.get("difficulty") != diff_num:
            q["difficulty"] = diff_num
            changed = True
        if q.get("locale") != "el-GR":
            q["locale"] = "el-GR"
            changed = True
        if q.get("status") != "reviewed":
            q["status"] = "reviewed"
            changed = True
        if not q.get("verifiedAt"):
            q["verifiedAt"] = "2026-10-25"
            changed = True
        if not q.get("tags"):
            q["tags"] = [cat_id]
            changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed metadata in {file_path}")
        fixed_total += 1

print(f"Total files updated: {fixed_total}")
