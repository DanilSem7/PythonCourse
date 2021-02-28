# вариант №24
import math


def f11(x):
    a = (53*math.pow((x*x*x+math.sin(x)), 8) + 85*x)
    b = -math.sqrt((x*x+69*math.pow(x, 5)/(35*x*x*x + x*x*x*x*x)))
    c = -((math.cos(x) - x*x+7)/(math.pow(math.e, x)-math.fabs(x)-6))
    result = a + b + c
    return '%.2e' % result

