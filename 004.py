a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = a.strip('.')
list1 = a.split(', ')
list2 = a.split('.')
list3 = a.split()
#辞書はappendでない
print(list3, len(list3))
#a[i,j,k]kは刻み、iはスタート、jは何個めまでか
#dictionaryへのついか方法は、dict[que] = keyword
sol_dex = {}
for i in range(len(list3)):
    if i+1 == 1 or (5 <= i+1 and i+1 <=9) or i+1 ==15 or i+1 == 16 or i+1 ==19:
        print(i, (list3[i])[0])
        sol_dex[list3[i][0]] = i+1
        print(sol_dex)
    else:
        print(i, (list3[i])[0:2])
        sol_dex[list3[i][0:2]] = i+1

print(sol_dex)
