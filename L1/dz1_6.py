a = input()
b = input()

if type(a) == str or type(b) == str:
    print 'string taken'
elif a == b:
    print 'equals'
elif a > b:
    print 'bigger'
elif a < b:
    print 'smaller'
