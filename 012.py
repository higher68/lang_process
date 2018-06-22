sample_data = open('hightemp.txt', 'r')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for line in sample_data:
    x = line.split()
    col1.write(x[0] + '\n')
    col2.write(x[1] + '\n')
##writeは改行が入らないらしい

col1.close()
col2.close()

col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')

for line in col1:
    print(line)
for line in col2:
    print(line)
