# вариант №24
import math


def f13(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += (90 * i - math.pow(i, 8))

    sum2 = 0
    for i in range(1, n + 1):
        sum2 += (85 * i + math.log1p(i))

    return '%.2e' % (sum1 + sum2)
