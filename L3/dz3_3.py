s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.'

def reversall (s):
    letters = list()
    words = list()
    props = list()

    text = list(s.split('. '))
    text.reverse()
    for i in text:
        words.append(i.split(' '))
    for i in words:
        for j in i:
            letters.append(list(j))
    for i in letters:
        i.reverse()
    
    retext = ' '.join(text)
    print words, letters
     
reversall(s1)
