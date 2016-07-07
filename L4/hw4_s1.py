from string import punctuation

s = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'
 
def hw4_solution1 (text):
    text = text.lower()
    result = []
    result_dict = {}
    res = []
    counter = 0
    str_len = 0
    procent = 0
   
    s1 = list(text.replace(' ', ''))
    for letter in s1:
        if (letter in punctuation) or (letter == ' '):
            s1.remove(letter)

    uniq = set(s1)
    str_len = len(s1)
    for index in uniq:
        counter = s1.count(index)
        procent = float(counter) / float(str_len) * 100
        res.extend([index.lower(), round(procent, 1)])
        result.append(res)
        res = []
    result_dict = dict(result)
    return result_dict
