def vowels (s):
    counter = 0
    vov_max = 0
    res = []
    vovs = ['A', 'E', 'I', 'O', 'U', 'Y']
    l = list(s.split(' '))
    print l
    for i in l:
        for j in i:
            if j.upper() in vovs:
                counter += 1
                if counter >= vov_max:
                    vov_max = counter
        res.append(counter)
        counter = 0
    print res, 'Max:', vov_max

s1 = input()
vowels(s1)
