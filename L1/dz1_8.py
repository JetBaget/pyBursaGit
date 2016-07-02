counter = 0
result = []
k = 3
t1 = tuple(str(raw_input()).split(' '))
s1 = list(t1)

for i in s1:
    counter += 1
    if counter % k == 0:
        result.append(i)
res1 = tuple(result)
print res1
