s = 'sabrrtuwacaddabra'
prev = ''
result = ''
counter = 0

for ch in s:
    if ch > prev:
        result += ch
        counter += 1
    else:
        
        counter = 0
    prev = ch
print result

