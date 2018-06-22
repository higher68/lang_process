##学び listと文字列は違うのかー
a = 'パトカー'
print(a)
b = 'タクシー'
c = ''
print(b)
for i in range(len(a)):
    c += a[i] + b[i]

print(c)
