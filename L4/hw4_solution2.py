s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'
n = int(raw_input('Please, enter limit: '))
i = -1
res = 0
slise = s[0:n]

if ' ' not in slise:
    print slise[0:len(slise)/2]
elif s[n] != ' ':
    for letter in slise:
        if slise[i] is ' ':
            res = slise[0:n+i] + '...'
        else:
            i -= 1
    print res
else:
    print(s[0:n])
