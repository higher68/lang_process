import MeCab
fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'

def parse_neko():
    '''「我輩は猫である」を形態素解析
    「我輩は猫である」(neko.txt)を形態素解析してneko.txt.mecabに保存
    '''

    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        mecab = MeCab.Tagger()
        #めかぶインスタンスの作成
        out_file.write(mecab.parse(data_file.read()))
        #parse：解析結果を文字列として取得



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

            #表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration # 区切りがなければ終了
                #StopIterationでループを止められる。
                #raise：なんか例外を引き起こす
                #http://coilcyber.hatenablog.jp/entry/2013/12/10/101236

            res_cols = cols[1].split(',')

            #辞書作成、リストに追加
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                #yieldは関数の処理を一旦停止し、値を返す。
                #もう一回呼び出したら普通に呼び出される。
                morphemes = []

#形態素解析
parse_neko()

lines = neco_lines()
for line in lines:
    print(line)
