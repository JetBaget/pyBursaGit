from string import punctuation

result = []
result_dict = {}
res = []
counter = 0
str_len = 0
procent = 0
summ = 0
s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'
s = s.lower()
s1 = list(s.replace(' ', ''))
for letter in s1:
    if (letter in punctuation) or (letter == ' '):
        s1.remove(letter)

uniq = set(s1)
str_len = len(s1)
print str_len
for index in uniq:
    counter = s1.count(index)
    procent = float(counter) / float(str_len) * 100
    res.extend([index.lower(), round(procent, 1)])
    result.append(res)
    res = []
result_dict = dict(result)
print result_dict
for values in result_dict:
    summ += result_dict[values]
print summ
