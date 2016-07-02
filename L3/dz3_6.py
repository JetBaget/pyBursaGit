from math import sqrt

limit = 100

for number in xrange(1, limit + 1):
    for mult in xrange(2, int(sqrt(number)+1)):

        if number % mult == 0:
            break
    else:
        print number
