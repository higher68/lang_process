col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')
col_m = open('col_m.txt', 'w')
col1_l = []
col2_l = []
for line in col1:
    col1_l.append(line.strip('\n'))
for line in col2:
    col2_l.append(line.strip('\n'))
for i in range(len(col1_l)) :
    col_m.write(col1_l[i] + '\t' + col2_l[i] + '\n')

col1.close()
col2.close()
col_m.close()
