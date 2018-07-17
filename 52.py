# 語幹とは、語尾が変化する単語の、変化しない前方部分をさす
import re
import snowballstemmer

fname = 'nlp.txt'


def nlp_lines():
    '''nlp.txtを1文ずつ読み込むジェネレータ
    nlp.txtを順次読み込んで1文ずつ返す

    戻り値：
    1文の文字列
    '''
    with open(fname) as lines:
        # 文切り出しの正規表現コンパイル
        pattern = re.compile(r'''
            (
            ^   # 行頭文字
            .*? # 任意の文字
            [\.|\:|\?|\!]  # 指定文字
            )
            \s  # 空白文字
            (
            [A-Z].*  # 任意の英大文字以降の文字にマッチ
            )
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

        for line in lines:

            line = line.strip()  # 前後の空白文字を削除
            # print(line)
            while len(line) > 0:

                # 行から1文を取得
                match = pattern.match(line)
                if match:

                    # 切り出した文字を返す
                    yield match.group(1)  # 先頭の文
                    # yieldは戻り値を一旦返して処理を続ける.これ使えばプリントできる
                    line = match.group(2)  # 次の文以
                else:

                    # 区切りがないので、最後までが1文
                    yield line
                    line = ''


def nlp_words():
    '''nlp.txtを1単語ずつ返すジェネレータ
    文の終わりでは空行を返す

    戻り値
    1単語、ただし文の終わりでは空行
    '''
    for line in nlp_lines():
        # 空白で分解して、区切り文字を後から消した方が確実
        # 区切り文字は.だけではないので、splitからする必要
        for _ in line.split():
            yield _.strip('.,;:?!()-')  # ()に包まれた文字にも対応

        yield ''


# 読み込み
stemmer = snowballstemmer.stemmer('english')
for word in nlp_words():

    # 元の結果とステミング結果を出力
    print('{}\t{}'.format(word, stemmer.stemWord(word)))
