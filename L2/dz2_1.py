def quadro(mas):
    res = []
    for i in mas:
        q = i*i
        res.append(q)
    print type(mas)(res)

s = input()
quadro(s)
