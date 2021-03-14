import math


def f12(x):
    if x < 179:
        result = math.pow(math.pow(x, 7) - 4 * math.pow(x, 6), 4) + 93 * math.pow(x, 8)
        return result
    elif 179 <= x < 229:
        result = math.log1p((58 * x * x * x + math.pow(x, 8)/94)) - math.cos(math.tan(x) + 12 * x * x * x)
        return result
    else:
        result = x * x + 24 * x * x * x - 88
        return result
