def flat (l):
    res = []
    for i in l:
        for k in i:
            res.append(k)
    print res

s = list(input())
flat(s)
