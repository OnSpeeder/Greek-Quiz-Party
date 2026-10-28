import glob
import os
import re

files = sorted(glob.glob("tools/generators/tmp_*.py"))
print(f"Total tmp files: {len(files)}")

# Check target json counts
content_files = glob.glob("content/questions/el-GR/*_*.json")
import json

db_counts = {}
for cf in content_files:
    cat_diff = os.path.basename(cf).replace(".json", "")
    with open(cf, "r", encoding="utf-8") as fp:
        db_counts[cat_diff] = len(json.load(fp))

print("Current counts in content/questions/el-GR:")
for k, v in sorted(db_counts.items()):
    if v < 210:
        print(f"  {k}: {v}/210")
