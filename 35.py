import MeCab
# MeCabの出力フォーマット
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'


def parse_neko():
    '''「我輩は猫である」を形態素解析
    「我輩は猫である」(neko.txt)を形態素解析してneko.txt.mecabに保存
    '''

    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        mecab = MeCab.Tagger()
        #  めかぶインスタンスの作成
        out_file.write(mecab.parse(data_file.read()))
        #  parse：解析結果を文字列として取得


def neco_lines():
    '''「吾輩は猫である」の形態素解析結果のジェネレータ
    「吾輩は猫である」の形態素解析結果を順次読み込んで、各形態素を
    http://www.nltk.org/book-jp/ch12.html
    ・表層形(surface)
    #表層形（活用や表記揺れなどを考慮した、文中において文字列として実際に出現する形式）
    ・基本形(base)
    見出し形（動詞の原形など、単語の基本的な形
    ・品詞(pos)
    ・品詞細分類1(pos)
    の４つをキーとする辞書に格納し、１文ずつ、この辞書のリストとして返す。

    戻り値：
    1文の形態素を辞書化したリスト
    '''
    with open(fname_parsed) as file_parsed:

        morphemes = []
        for line in file_parsed:
            # print('here1',line)
            # 表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            # print('here2',cols)
            if(len(cols) < 2):
                raise StopIteration  # 区切りがなければ終了
                # StopIterationでループを止められる。
                # raise：なんか例外を引き起こす
                # http://coilcyber.hatenablog.jp/entry/2013/12/10/101236

            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
            morpheme = {
                'surface': cols[0],  # 表層形
                'base': res_cols[6],  # 基本形
                'pos': res_cols[0],  # 品詞
                'pos1': res_cols[1]  # 品詞細分類
            }
            morphemes.append(morpheme)

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':
                yield morphemes
                # yieldは関数の処理を一旦停止し、値を返す。
                # もう一回呼び出したら普通に呼び出される。
                morphemes = []


parse_neko()

# 1文ずつ辞書のリストを取得し抽出
list_series_noun = []  # 出現リスト、重複あり
for line in neco_lines():
    nouns = []
    for morpheme in line:

        # 名詞ならnounsに追加
        if morpheme['pos'] == '名詞':
            nouns.append(morpheme['surface'])

        # 名詞以外なら、空までの連続する名詞をlist_series_nounに追加
        # このif文だけだと、line中のmorpheが名詞で終わった際に、それが追加されない
        else:
            if len(nouns) > 1:
                list_series_noun.append("".join(nouns))
                nouns = []

    # 名詞で終わる行があった場合は、最後の連続する名詞をlist_series_nounに追加
    if len(nouns) > 1:
        list_series_noun.append("".join(nouns))

# 重複除去
series_noun = set(list_series_noun)

# 確認しやすいようlist_series_nounを使って出現順にソートして表示
print(sorted(series_noun, key=list_series_noun.index))
