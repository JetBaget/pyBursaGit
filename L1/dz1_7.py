counter = 0
current = 0

def dublicate_search(lis):
    result = []
    prior = set()
    for i in lis:
        if i in prior:
            continue
        prior.add(i)
        result.append(i)
    print list(prior)
    print result

l1 = list(raw_input())
dublicate_search(l1)
