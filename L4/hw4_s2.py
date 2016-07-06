s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'
def hw4_solution2 (text, n):
    i = 1
    res = 0
    slise = text[0:n]

    if ' ' not in slise:
        return text[0:round(n/2+0.5)] + '...'
    elif text[n] != ' ':
        for letter in slise:
            if slise[i] is ' ':
                res = slise[0:n-i] + '...'
            else:
                i += 1
        return res
    else:
        return (text[0:n]) + '...'

print(hw4_solution2(s, 6))
