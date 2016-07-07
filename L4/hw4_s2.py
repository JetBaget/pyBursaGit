s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'
def hw4_solution2 (text, n):
    res = 0
    j = 1
    counter = 0
    slise = text[0:n]
    
    if slise[n-1] is '.':
        res = slise
        return res
    else:
        for i in slise:
            if i is ' ':
                counter += 1
            else:
                pass
        if counter > 1 and slise[n-1] != ' ':
            for letter in slise:
                if slise[n-1-j] is ' ':
                    res = slise[0:n-1-j] + '...'
                    break
                else:
                    j += 1
        elif counter > 1:
            res = slise[0:n-1] + '...'
        else:
            res = slise[0:n/2] + '...'
    return res
#n1 = int(raw_input('Enter the limit: '))
#print(hw4_solution2(s, n1))
