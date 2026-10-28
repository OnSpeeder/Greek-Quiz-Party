import glob
import os
import re

files = sorted(glob.glob("tools/generators/tmp_*.py"))

# For each file, check if it executes validate_and_append or what it does
info = []
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    # search for validate_and_append call
    match = re.search(r'validate_and_append\s*\(\s*["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']\s*,\s*(\d+)', content)
    # search for question IDs
    ids = re.findall(r'["\']id["\']\s*:\s*["\']([^"\']+)["\']', content)
    if match:
        cat, diff_str, diff_num = match.groups()
        info.append((f, cat, diff_str, int(diff_num), len(ids), ids[:2], ids[-1:]))
    else:
        info.append((f, None, None, None, len(ids), ids[:2], ids[-1:]))

# Check existing IDs in content
import json
content_files = glob.glob("content/questions/el-GR/*_*.json")
existing_ids = set()
for cf in content_files:
    with open(cf, "r", encoding="utf-8") as fp:
        for q in json.load(fp):
            existing_ids.add(q["id"])

print(f"Total existing questions in DB: {len(existing_ids)}")
unapplied = []
for f, cat, diff_str, diff_num, count, id_start, id_end in info:
    if not id_start:
        continue
    first_id = id_start[0]
    last_id = id_end[0] if id_end else ""
    first_in = first_id in existing_ids
    last_in = last_id in existing_ids
    if not first_in:
        unapplied.append((f, cat, diff_str, diff_num, count, first_id, last_id))

print(f"\nUnapplied tmp scripts: {len(unapplied)}")
for item in unapplied:
    print(f"  {os.path.basename(item[0])} -> {item[1]}_{item[2]} ({item[4]} questions: {item[5]}..{item[6]})")
