for path in ["tools/generators/tmp_gaming_med_4.py", "tools/generators/tmp_sports_med_4.py"]:
    print(f"=== {path} ===")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("First 5 lines:")
        for l in lines[:5]:
            print(" ", l.strip())
        print("Last 10 lines:")
        for l in lines[-10:]:
            print(" ", l.strip())
