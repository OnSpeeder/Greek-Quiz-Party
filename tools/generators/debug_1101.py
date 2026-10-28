with open("tools/generators/tmp_sports_med_4.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(1095, 1105):
    print(f"{idx+1}: {ascii(lines[idx])}")
