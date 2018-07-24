# coding: utf-8
import os
import subprocess
import xml.etree.ElementTree as ET

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'


def parse_nlp():
    '''nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
    すでに結果ファイルが存在する場合は実行しない
    '''
    if not os.path.exists(fname_parsed):

        # StanfordCoreNLP実行、標準エラーはparse.outへ出力
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,     # shellで実行
            check=True      # エラーチェックあり
        )


# nlp.txtを解析
parse_nlp()
# 解析結果のxmlをパース
root = ET.parse(fname_parsed)
# token = 字句 があって、その中にnerがあるそうです。さらにnerの中にpersonが格納されてる.
# tokenの抽出
# iterfind1~~タグ名または パス にマッチするすべての子要素を検索
for token in root.iterfind(
    './document/sentences/sentence/tokens/token[NER="PERSON"]'
):
    print(token.findtext('word'))
