# 最終目的＝複合語の置換
f_list = "Country_list.CSV"
f_corpus = "corpus80.py"
f_result = "corpus81.txt"
set_county = set()
dict_county = {}
with open(f_list, "r") as data_file:
    for _ in data_file:
        country = _[1].strip()
        country.replace(" ", "_")

with open(f_corpus, "rt") as data_file, open(f_result, "wt") as out_file:
    for line in data_file:
