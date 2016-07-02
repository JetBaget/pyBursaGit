s = str(raw_input('Print a line for inverse: '))
s1 = ()
s2 = []
s3 = ()
s4 = ()
y = 0
#Make inversion of the line by 4 methods

#1-st method:
s1 = s
l = list(s1)
l.reverse()
s1 = ''.join(l)
print s1

#2-nd method:
for i in s:
    buf = i
    s2.insert(0,buf)
s2 = str(''.join(s2))
print s2

#3-rd method:
s3 = s
for j in s:
    

#4-th method:
s4 = s[::-1]
print s4
