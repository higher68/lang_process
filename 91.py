f_in = "question-words.txt"
f_out = "91_family.txt"

with open(f_in, "rt") as data_file, \
     open(f_out, "wt") as out_file:
    # 対象セクション(familyで始まる)内にいるか判定
    target = False
    # 全探索
    for line in data_file:
        # 対象セクションでない場合
        if target is False:
            if line.startswith(": family"):
                target = True
        # 対象セクションである場合
        elif target is True:
            # 次のセクションであり、familyでない場合。
            if line.startswith(": family ") is False:
                target = False
            # 同一セクション内の場合
            else:
                print(line.strip(), file=out_file)
