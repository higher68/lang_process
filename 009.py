def sort1(x, l):
    import random
    #print(x)
    x = list(x)
    if len(x) > 4:
        for i in range(1,len(x)-1):
            r = random.randint(1,len(x)-2)
            ##randintは整数で乱数を生成。どういうアルゴリズム？
            #print(r)
            tmp = x[i]
            x[i] = x[r]
            x[r] = tmp
    else:
        pass
    result = ''
    for c in x:
        result += c
    return result



s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(s)
s = s.strip('.').split()
#split(' ')にすると、空白が最後に残ってしまう。
#print(s)
l=len(s)
#print('hoge',l)
for i in range(l):
    s[i] = sort1(s[i], l)
result = ''
for i in range(l):
    result += s[i] + ' '
result +='.'
print(result)
