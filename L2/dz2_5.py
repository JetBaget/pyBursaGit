def separator(l):
    even = []
    uneven = []
    res = []
    for i in l:
        if i%2 != 0:
            uneven.append(i)
        else: even.append(i)
    uneven.sort()
    even.sort()
    even.reverse()
    res = uneven + even
    print res
    print l is res

s = list(input())
separator(s)
