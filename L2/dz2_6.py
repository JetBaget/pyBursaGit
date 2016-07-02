def classify(dic):
    Dict = dic.copy()
    d_type = 0
    counter = 0
    types1 = []
    types2 = []
    result = {}
    for i in Dict.values():
        types1.append(type(i))
        types2 = set(types1)
        for j in types2:
            counter = types1.count(j)
            result.update({j:counter})
    print result

s = dict(input())
classify(s)
