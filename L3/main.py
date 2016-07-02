def main(s1,s2,s3):    
    if discrim(s1,s2,s3) > 0:
        print(roots(s1, s2, discrim(s1,s2,s3)))
    elif discrim(s1,s2,s3) == 0:
        print('Discrim is zero')
        print(roots(s1, s2, discrim(s1,s2,s3)))
    else: print('Discrim is negative, no roots')

def discrim(a, b, c):
    D = b**2 - 4*a*c
    return D

def roots(a, b, D):
    ans = []
    if D == 0:
        x1 = x2 = -b/(2*a)
        ans.append(x1)
        ans.append(x2)
    else:
        x1 = -b + D**(1/2.0) / 2*a
        x2 = -b - D**(-1/2.0) / 2*a
        ans.append(x1)
        ans.append(x2)
    return ans

s1 = int(input())
s2 = int(input())
s3 = int(input())
main(s1,s2,s3)
