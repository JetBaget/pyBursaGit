s1 = 'Chupacabra Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.'

def max_len (s):
    i_len = []
    biggest = 0
    z = ['.', ',', '!', '?', ':', ';']
    lfs = list(s)
    for i in lfs:
        if i in z:
            lfs.remove(i)
    r = list((''.join(lfs)).split(' '))

    for i in r:
        i_len.append(len(i))
        biggest = max(i_len)
    for j in r:
        if len(j) >= biggest:
            print j, len(j)

max_len(s1)
