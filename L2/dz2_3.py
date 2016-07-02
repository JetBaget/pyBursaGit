def trinity(l):
    d = dict()
    count = 0
    for i in l:
        k = (i%3 == 0)
        d[i] = k
        count += 1
    print d

s = list(input())
trinity(s)
