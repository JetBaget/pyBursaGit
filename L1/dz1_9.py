y = int(input('Var Y: '))
x = int(input('Var X: '))
z = int(input('Var Z: '))

def compare(X, Y, Z):
    res = min(max(max(min(X,Y),X),Y),Z)
    print res

compare(x, y, z)
