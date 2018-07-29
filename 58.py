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


parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

for sentence in root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))

    # 語の辞書を作成
    dict_pred = {}  # {述語のidx, 述語のtext}
    dict_nsubj = {}  # {述語のidx, 述語とnsubj関係の子のtext=主語}
    dict_dobj = {}  # {述語のidx, 述語とdsubj関係の子のtext=目的語}
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        # 関係チェック
        dep_type = dep.get('type')
        if dep_type == 'dobj' or dep_type == 'nsubj':
            # 述語の辞書に追加
            govr = dep.find('./governor')
            idx = govr.get('idx')
            dict_pred[idx] = govr.text

            # 主語 or　目的語の辞書に追加
            if dep_type == 'nsubj':
                dict_nsubj[idx] = dep.find('./dependent').text
            else:
                dict_dobj[idx] = dep.find('./dependent').text

    # 述語を列挙、主語と目的語の両方を持つもののみ出力
    for idx, pred in sorted(dict_pred.items(), key=lambda x: x[0]):
        nsubj = dict_nsubj.get(idx)  # キーから値を出力できるメソッド
        dobj = dict_dobj.get(idx)
        if nsubj is not None and dobj is not None:
            print('{}\t{}\t{}'.format(nsubj, pred, dobj))
