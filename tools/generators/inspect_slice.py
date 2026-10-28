with open("tools/generators/tmp_sports_med_4.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("tools/generators/sports_slice.txt", "w", encoding="utf-8") as out:
    for i in range(max(0, 1090), min(len(lines), 1165)):
        out.write(f"{i+1}: {lines[i]}")

print("Wrote slice.")
