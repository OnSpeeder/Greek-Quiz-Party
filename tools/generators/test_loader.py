import runpy

def load_from_script(path):
    # Provide dummy environment
    env = {
        "append_questions": lambda *args: None,
        "verify_and_append": lambda *args: None,
    }
    # Execute file in env
    res = runpy.run_path(path, init_globals=env)
    for k in ["QUESTIONS", "NEW_QUESTIONS", "BATCH_QUESTIONS", "questions"]:
        if k in res and isinstance(res[k], list):
            return res[k]
    return None

for path in ["tools/generators/tmp_gaming_med_4.py", "tools/generators/tmp_sports_med_4.py", "tools/generators/tmp_technology_hard_2.py", "tools/generators/tmp_wtf_facts_med_2.py"]:
    qs = load_from_script(path)
    print(path, "loaded questions:", len(qs) if qs else "None")
