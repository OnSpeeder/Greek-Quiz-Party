# -*- coding: utf-8 -*-
import sys
import os
import json
import random

sys.path.insert(0, os.path.abspath("tools/generators"))
import gen_cinema_tv_hard_4 as mod

questions = mod.QUESTIONS
random.seed(42)

for q in questions:
    correct_val = q['answers'][q['correctAnswerIndex']]
    opts = list(q['answers'])
    random.shuffle(opts)
    q['answers'] = opts
    q['correctAnswerIndex'] = opts.index(correct_val)

counts = {}
for q in questions:
    counts[q['correctAnswerIndex']] = counts.get(q['correctAnswerIndex'], 0) + 1
print("Distribution:", counts)

with open("tools/generators/gen_cinema_tv_hard_4.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\nimport sys\nimport os\nsys.path.insert(0, os.path.abspath('tools/generators'))\nfrom base_generator import validate_and_append\n\n")
    f.write("QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + "\n\n")
    f.write('if __name__ == "__main__":\n    print(f"Loaded {len(QUESTIONS)} questions for cinema_tv_hard.")\n    validate_and_append("cinema_tv", "hard", 5, QUESTIONS)\n')
