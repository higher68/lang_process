def n_gram(x, n):##x=文書、n=何グラムか
    x = x.strip('.')
    x = x.split()
    c_gram = [] ##単語gram
    w_gram = [] ##文字gram
    x1 = ''
    #print(x)
    ### 単語n-gram :単語を一かたまりと見て、bi-gramだと隣あう単語をひとかたまり
    if len(x) > n:
        for i in range(len(x)-n+1):
            x2 = ''
            #print('i', i,n)
            for j in range(i, i+n):
                #print('j',j, x[j])
                if j == i + n-1:
                    x2 += x[j]
                else:
                    x2 += x[j] + '-'
            c_gram.append(x2)
            #print(c_gram)
    else:
        c_gram += x
    for c in x:
        x1 += c
    print(x1)
    for i in range(len(x1)-n+1):
        x2 = ''
        for j in range(i, i+n):
            if j == i + n -1:
                x2 += x1[j]
            else:
                x2 += x1[j] + '-'
        w_gram.append(x2)
    return c_gram, w_gram


c = 'I am an NLPer'
x, y = n_gram(c, 2)
print(x)
print(y)
