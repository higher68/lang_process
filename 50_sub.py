import re
fname = 'nlp.txt'

with open(fname) as lines:
    # 文切り出しの正規表現コンパイル
    pattern = re.compile(r'''
    (
    ^   # 行頭文字
    .*? # 任意の文字、最小マッチ最初の部分から、マッチを繰り返し続ける。それで、指定してる文字
    # ここだと「.」とかにぶつかったら止まる。なければマッチなんてしない。
    [\.|\:|\?|\!]  # 指定文字
    )
    \s  # 空白文字今まではここの部分が()ついてたからマッチしちまってた。
    (
    [A-Z].*  # 任意の英大文字以降の文字にマッチ最小ではないので、永遠にマッチを続ける。
    )
''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    i = 0
    for line in lines:
        i += 1
        print('-'*10)
        print('line', line)
        if i == 6:
            exit()
        line = line.strip()  # 前後の空白文字を削除
        # print(line)
        while len(line) > 0:

            # 行から1文を取得
            match = pattern.match(line)
            print('match', match)
            if match:

                # 切り出した文字を返す
                print('match.group(1)', match.group(1))  # 先頭の文
                print('match.group(2)', match.group(2))
                print(len(match.group(2)))
                line = match.group(2)  # 次の文以降
            else:

                # 区切りがないので、最後までが1文
                print('line2', line)
                line = ''
