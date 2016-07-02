def evener(l):
    if len(l)%2 == 0:
        for i in l:
            if i%2 != 0:
                l.remove(i)
        print l
    else:
        for i in l:
            if i%2 == 0:
                l.remove(i)
        print l

s = list(input())
evener(s)
