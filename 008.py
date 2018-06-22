def cipher(c):
    ##ord()ユニコード→整数
    ##chr()整数→ユニコード
    c = list(c)
    #print(c)
    for i in range(len(c)):
        ###str.islower()小文字ならtrue
        ###TypeError: 'str' object does not support item assignment
        ##pythonの文字列は、作成後に変更できない
        if c[i].islower():
            c[i] = chr(219 - ord(c[i]))
        else:
            pass
            ##strは数値を文字列にするだけ

    c1 = ''
    for i in range(len(c)):
        c1 += c[i]
    return c1
x = 'aiueoKoKKK'
print(x)
print(cipher(x))
