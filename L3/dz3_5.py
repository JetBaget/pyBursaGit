from operator import add

def psevdosum (n):
    summ = 0
    s = str(n)
    for i in s:
        summ += int(i)
    print summ

def psevdo1 (n):
    digit_sum = 0
    for digit in list(str(n)):
        digit_sum = add(digit_sum, int(digit))
    return digit_sum

s1 = int(raw_input())
psevdosum(s1)
print(psevdo1(s1))
