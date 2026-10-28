with open("tools/generators/tmp_sports_med_4.py", "r", encoding="utf-8") as f:
    text = f.read()

import ast
tree = ast.parse(text)
for node in tree.body:
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name):
                print(f"Assign to {t.id} at line {node.lineno}")
