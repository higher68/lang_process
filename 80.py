import bz2

f_source = "enwiki-20150112-400-r10-105752.txt.bz2"
f_del = "del_list.txt"
f_result = "result.txt"
i = 0
with bz2.open(f_source, "rt") as data_file,\
 open(f_del, "r") as data_del,\
 open(f_result, "w") as data_result:
    for cols in data_file:
        i += 1
        # 空白分割
        cols = cols.split()
        # print(cols)
        # 末尾の文字削除
        for _ in data_del:
            del_list = _
        # print(del_list)
        col2s = []
        # strip()を作用させても、作用させた文字列は書き変わらないよ。
        for col in cols:
            # print(col)
            col2 = col.strip(del_list)
            if col2 != "":
                col2s.append(col2)
            # print(col)
        for col2 in col2s:
            print(col2, end=" ", file=data_result)
            # print(col2, end=" ")
        print("", file=data_result)
        # print("")
