a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
##split()はリストを返す。
##strip()文字列の両端から指定文字を剥ぎ取る
print('1', a)
print('')
a = a.strip('.')
print('2', a)
print('')
list1 = a.split(', ')
print('3', list1)
print('')
list2 = a.split('.')
print('4', list2)
print('')
list3 = a.split()
print('5', list3)
print('')
#listは追加はappendで
list4 = []
for ch in list3:
    list4.append(len(ch))

print(list4)
