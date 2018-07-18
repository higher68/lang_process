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

        # StanfordCoreNLP実行、標準エラーparse.outに出力
        subprocess.run(
            'java -cp "/Users/junya/Library/stanford-corenlp-full-2018-02-27/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,  # ,   # shell
            check=True      # エラーチェックあり
        )


# nlp.txtを解析
parse_nlp()
print('hoge')
print('hoge2')
# 解析結果のxmlをパース
root = ET.parse(fname_parsed)
print('hoge3')

# wordのみ取り出し
for word in root.iter('word'):
    exit()
    print(word.text)
