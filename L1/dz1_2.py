s = str(raw_input('Enter a string: '))
counter = 0

vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']

for i in s:
    for x in vowels_list:
        if i == x or i == x.upper():
            counter += 1
print 'Number of vowels in your string: ',counter
