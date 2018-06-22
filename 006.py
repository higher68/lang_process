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
    #print(x1)
    for i in range(len(x1)-n+1):
        x2 = ''
        for j in range(i, i+n):
            if j == i + n -1:
                x2 += x1[j]
            else:
                x2 += x1[j] + '-'
        w_gram.append(x2)
    return w_gram
#print(n_gram('paraparaparadise', 2))
x = set(n_gram('paraparaparadise', 2))
y = set(n_gram('paragraph', 2))
#print(x)
#print(y)
union = x.union(y)#set型：集合を扱う型。ristとかではない|でも良い
intersec = x.intersection(y)#&でも良い
dif_set = x.difference(y)#-でも良い。
print(x)
print(y)
print(union)
print(intersec)
print(dif_set)
q = ['s-e']
q = set(q)
print(q)
print(q.issubset(x))
print(q.issubset(y))
