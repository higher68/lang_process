import CaboCha
import re
import pydot_ng as pydot

fname = 'nako.txt.tmp'
fname_parsed = 'neko.txt.cabocha.tmp'


def parse_neko():
    '''「吾輩は猫である」を係り受け解析
    「吾輩は猫である」(neko.txt)を係り受け解析してneko.txt.cabochaに保存する。
    '''
    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        cabocha = CaboCha.Parser()
        for line in data_file:
            out_file.write(
                cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
            )


class Morph:
    '''
    形態素クラス
    表層形(surface)、基本形(base)、品詞(pos)、品詞細分類1(pos1)を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''クラスのインスタンスにstr()が実行された時に呼び出され、
        文字列を返す
        '''
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    '''
    文節クラス
    形態素(Morphオブジェクト)のリスト(morphs)、係り受け文節インデックス番号(dst)、
    係り元文節インデックス番号のリスト(srcs)をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        self.morphs = []
        self.srcs = []
        self.dst = -1

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

    def chk_pos(self, pos):
        '''指定した品詞(pos)を含むかチェックする

        戻り値：
        品詞(pos)を含む場合はTrue
        '''
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False


def neco_lines():
    '''「吾輩は猫である」の係り受け解析結果のジェネレーター
    「吾輩は猫である」の係り受け解析結果を順次読み込んで、
    １文ずつChunkクラスのリストを返す

    戻り値：
    １文のChunkクラスのリスト
    '''
