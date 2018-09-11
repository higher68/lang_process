# 最終目的＝複合語の置換
f_list = "Country_list.CSV"
f_corpus = "corpus80.py"
f_result = "corpus81.txt"
set_country = set()
dict_country = {}
with open(f_list, "r") as data_file:
    for _ in data_file:
        country = _.split()
        if len(country) > 1:

            # 集合に追加
            set_country.add(countri.strip())

            # 辞書に追加
            if country[0] in dict_country:
                lengths = dict_country[country[0]]
                if not len(country) in lengths:
                    # 未登録だったら、辞書から生成したリストに加え、そーと
                    lengths.append(len(country))
                    lengths.sort(reverse=True)
            else:
                dict_country[country[0]] = [len(country)]
# 1行ずつ処理
with open(f_corpus, "rt") as data_file, open(f_result, "wt") as out_file:
    for line in data_file:

        # 1語ずつチェック
        tokens = line.strip().split()
        result = []  # 結果のトークン配列
        skip = 0
        for i in range(len(tokens)):
            # 複合語の続きの場合はスキップ
            if skip > 0:
                skip -= 1
                continue

            # 1語目が辞書にあるか
            if tokens[i] in dict_country:
                # 後続の語数を切り取って集合にあるかチェック
                hit = False
                # 1語目の登録された単語数で全探索
                for length in dict_country[tokens[i]]:
                    # 文中の単語が複数後の単語に一致するかチェック
                    # なお、最長一致。
                    if " ".join(tokens[i:i + length]) in set_country:

                        # 複合語の国を発見。'_'で連結して、結果に追加
                        result.append('_'.join(tokens[i:i + length]))
                        # 区切り文字.joinでリストの連結ができる
                        skip = length - 1  # 残りの語はスキップ
                        hit = True
                        break
                if hit:
                    continue
            # 複合語の国ではないのでそのまま結果に追加
            result.append(tokens[i])
        print(*result, sep=' ', end="\n", file=out_file)
