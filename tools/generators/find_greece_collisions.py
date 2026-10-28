with open("tools/generators/tmp_greece_hard_1.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "σκυριανά" in l or "Θησαυρό" in l:
        print(f"Line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+20)):
            print(f"  {j+1}: {ascii(lines[j].strip())}")
