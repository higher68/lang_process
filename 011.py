sample_data = open('hightemp.txt', 'r')
#replaceでできる。が。
for line in sample_data:
    print(line.replace('\t',' ' ))
##sed s/置換前/置換後/ catと使うときは cat 'ファイル名' | sed s/~/~/
sample_data.close()

print('----------------------------------')
##文字列はイミュータブル
sample_data = open('hightemp.txt', 'r')
#replaceでできる。が。
for line in sample_data:
    w1 =''
    for word in line:
        if word == '\t':
            w1 += ' '
        else:
            w1 += word
    print(w1)

sample_data.close()
