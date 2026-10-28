import ast
import glob
import os
import sys

# Add tools/generators to sys.path
sys.path.insert(0, os.path.abspath("tools/generators"))
from base_generator import validate_and_append, load_existing_db

scripts = [
    ("tools/generators/tmp_cinema_tv_hard_2.py", "cinema_tv", "hard", 5),
    ("tools/generators/tmp_gaming_med_4.py", "gaming", "medium", 3),
    ("tools/generators/tmp_geography_hard_2.py", "geography", "hard", 5),
    ("tools/generators/tmp_history_hard_2.py", "history", "hard", 5),
    ("tools/generators/tmp_logic_med_3.py", "logic", "medium", 3),
    ("tools/generators/tmp_pop_culture_med_2.py", "pop_culture", "medium", 3),
    ("tools/generators/tmp_science_med_4.py", "science", "medium", 3),
    ("tools/generators/tmp_sports_med_4.py", "sports", "medium", 3),
    ("tools/generators/tmp_technology_hard_2.py", "technology", "hard", 5),
    ("tools/generators/tmp_wtf_facts_med_2.py", "wtf_facts", "medium", 3),
]

for script_path, cat, diff_str, diff_num in scripts:
    print(f"\nProcessing {os.path.basename(script_path)} for {cat}_{diff_str}...")
    with open(script_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Find the list of questions in the file
    tree = ast.parse(code)
    questions = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ["QUESTIONS", "NEW_QUESTIONS", "BATCH_QUESTIONS", "questions"]:
                    questions = ast.literal_eval(node.value)
                    break
        if questions:
            break

    if not questions:
        print(f"ERROR: Could not find question list in {script_path}")
        continue

    # Filter to only the needed amount if exceeding 210
    import json
    target_file = f"content/questions/el-GR/{cat}_{diff_str}.json"
    with open(target_file, "r", encoding="utf-8") as fp:
        current_len = len(json.load(fp))
    
    needed = 210 - current_len
    if needed <= 0:
        print(f"File {target_file} already has {current_len} questions (target 210). Skipping.")
        continue

    to_add = questions[:needed]
    print(f"Found {len(questions)} questions. Current count: {current_len}. Adding {len(to_add)} questions to reach {current_len + len(to_add)}...")
    
    try:
        validate_and_append(cat, diff_str, diff_num, to_add)
        print(f"Successfully appended to {cat}_{diff_str}!")
    except Exception as e:
        print(f"FAILED validating {script_path}: {e}")

