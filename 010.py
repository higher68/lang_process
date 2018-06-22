sample_data = open('hightemp.txt', 'r')
#行数は横線が何本か
i=0
for line in sample_data:
    i+=1
    print(line)

sample_data.close()
print(str(i) + 'column exist.')
#確認用unix wc -l 'hightemp.txt'
