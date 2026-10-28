import ast

for p in ["tools/generators/tmp_gaming_med_4.py", "tools/generators/tmp_sports_med_4.py"]:
    with open(p, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in ["BATCH_QUESTIONS", "NEW_QUESTIONS"]:
                    qs = ast.literal_eval(node.value)
                    print(p, "keys:", list(qs[0].keys()))
