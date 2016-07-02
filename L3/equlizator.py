import main
from main import(s1,s2,s3)
ans = main.roots(s1,s2,s3)

def equalize(l):
    if l[0] > 0 and l[1] > 0:
        print('Roots is positive')
    elif (l[0] > 0 and  l[1] < 0) or (l[0] < 0 and l[1] > 0):
        print('One of roots is negative')
    else: print('Roots is negative')

equalize(ans)
