def str_sym(d):
    s = list(d)
    if len(s)%2 == 0:
        s2 = s[len(s)/2:len(s)]
        ind1 = s[0:len(s)/2] == s2[::-1]
        print ind1
    else:
        s2 = s[len(s)/2+1:len(s)]
        ind2 = s[0:len(s)/2] == s2[::-1]
        print ind2

s1 = str(raw_input())
str_sym(s1)
