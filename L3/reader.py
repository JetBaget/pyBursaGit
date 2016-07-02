l = [i*i for i in range(10)]

wr = open('xfile.txt', 'w')
for j in l:
    wr.write(str(j) + '\n')

