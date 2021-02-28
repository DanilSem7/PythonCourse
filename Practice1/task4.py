# вариант №24
import math


def f14(n):
    if n == 0:
        return 2
    else:
        return '%.2e' % (1 / 60 * (f14(math.pow(n - 1, 3))) - math.sin(f14(n - 1)))


