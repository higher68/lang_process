import os
import subprocess
import xml.etree.ElementTree as ET  # XML データを解析および作成するシンプルかつ効率的な API

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'


def parse_nlp():
    '''nlp.txtをStanford Core NLPで解析、xmlファイルへ出力結果ファイルが
    すでに存在する時には実行しない
    '''

    if not os.path.exists(fname_parsed):
        'java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
        ' -Xmx2g'
        ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
        ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
        ' -file ' + fname + ' 2>parse.out',
        # StanfordCoreNLP実行、標準エラーparse.outに出力
        subprocess.run(
    # Xmx3gにしないとヒープ領域が足りなくなるよ
            shell=True,  # ,   # shell
            check=True      # エラーチェックあり   # エラーチェックあり
        )


# nlp.txtを解析
parse_nlp()
# 解析結果のxmlをパース
root = ET.parse(fname_parsed)
# print(type(root))
# wordのみ取り出し
# iter()イテレータオブジェクトを返す
for word in root.iter('word'):
    # 公式によると、'word'が現れるまで読み進めているらしい。上は
    exit()
    print(word.text)
