a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
##split()はリストを返す。
##strip()文字列の両端から指定文字を剥ぎ取る
print('1', a)
print('')
a = a.strip('.')
print('2', a)
print('')
list1 = (((a.split(', ')).split('.')).split())
print('5', list1)
print('')
