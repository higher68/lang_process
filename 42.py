# coding: utf-8
import CaboCha
# CabochaはSVM(Support Vector Machines) に基づく日本語係り受け解析器
# 文節間の「修飾する（係る）」「修飾される（受ける）」の関係を調べる事です。
# ex.綺麗な海
# ・「綺麗な」→「海」 #「綺麗な」が「海」を修飾する。
# https://qiita.com/nezuq/items/f481f07fc0576b38e81d
# svm：機械学習アルゴリズムの一つ。
# 係り先は、修飾先のことで、係り元は修飾元っぽいなあ。
import re

fname = 'neko.txt'
fname_parsed = 'neko.txt.cabocha'


def parse_neko():
    '''「吾輩は猫である」を係り受け解析
    「吾輩は猫である」(neko.txt)を係り受け解析して
    neko.txt.cabochaに保存する'''
    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        cabocha = CaboCha.Parser()
        # 構文解析を行う機構＝parser
        # https://ja.wikipedia.org/wiki/%E6%A7%8B%E6%96%87%E8%A7%A3%E6%9E%90
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
                # toString(CaboCha.FORMAT_LATTICE)   # 計算機に処理しやすいフォーマットで出力
                # http://mayo.hatenablog.com/entry/2014/09/12/113422
            )


class Morph:
    '''
    形態素クラス
    表層形(surface)、基本形(base)、品詞(pos)、品詞細分類１(pos1)を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    '''
    文節クラス
    形態素（Morphオブジェクト）のリスト（morphs）、係り先文節インデックス番号（dst）、
    係り元文節インデックス番号のリスト（srcs）をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        self.morphs = []  # 形態素オブジェクトのリスト
        self.srcs = []  # 係り元文節インデックス番号
        self.dst = -1  # 係り先インデックス番号

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

    def normalized_surface(self):
        '''句読点などの記号を除いた表層形'''
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                result += morph.surface
        return result


def neco_lines():
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで
    １文ずつChunkクラスのリストを返す

    戻り値：
    1文のChunkクラスのリスト
    '''
    with open(fname_parsed) as file_parsed:

        chunks = dict()  # idxをkeyにChunkを格納
        idx = -1

        for line in file_parsed:
            # print('line', line)

            # 1文の終了判定
            if line == 'EOS\n':
                # Chunkのリストを返す
                # print('len_chunks', len(chunks))
                # for _ in chunks:
                    # print('_', _)
                    # chunkは文節を表すそうです
                if len(chunks) > 0:
                    # print('chunks', chunks)
                    # chunksをkeyでソートし、valueのみ取り出し
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_tuple))[1]
                    chunks.clear()
                    # clear()　全ての要素を削除する。

                else:
                    yield []
                    # yield・・・一旦停止。再度呼んだらそこから再開

            elif line[0] == '*':
                # print('line', line)
                # Chunkのインデックス番号と係り先のインデックス番号取得
                cols = line.split(' ')
                idx = int(cols[1])
                dst = int(re.search(r'(.*?)D', cols[2]).group(1))
                # print('idx, dst', idx, dst)
                # groupはマッチした全体を返す
                # * 0 -1D 0/0 0.000000・・・・二つ目の数字がインデックス
                # Dにくっついてるのが、係り先のインデックス

                # Chunkを生成(なければ)し、係り先のインデックス番号セット
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先=dstのChunkを生成（なければ）し、係り元=srcsインデックス番号追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # それ以外の行は形態素解析結果なので、Morphを作りChunkに追加

            else:

                # 表層系はtab区切り、それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph(インスタンス)作成、リストに追加
                chunks[idx].morphs.append(
                    Morph(
                        cols[0],      # surface
                        res_cols[6],  # base
                        res_cols[0],  # pos
                        res_cols[1]   # pos1
                    )
                )

        raise StopIteration


# 係り受け解析
parse_neko()

# 1文ずつリスト作成
for chunks in neco_lines():
    # neco_linesを使うと、文節のリストが返ってくるのかあ
    # https://note.nkmk.me/python-enumerate-start/
    # enumerateを使うと、forループないで、リスト内の
    # オブジェクトの要素とインデックス番号を取得できる
    # enumerate(-, 1)でインデックスを1から開始
    # 3文目を表示
    # 係り先があるものを列挙
    for chunk in chunks:
        if chunk.dst != -1:
            # 記号を除いた表層形をチェック、空なら除外
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                print('{}\t{}'.format(src, dst))
