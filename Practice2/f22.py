def f22(x):
    f = x & 0x80000000
    e = x & 0x70000000
    d = x & 0x8000000
    c = x & 0x7FE0000
    b = x & 0x1FFC0
    a = x & 0x3F

    c <<= 5
    f >>= 10
    d >>= 6
    a <<= 14
    e >>= 17
    b >>= 6

    x = a + b + c + d + e + f
    return x

# print(hex(f22(0x1698850f)))
# = 0xd303ca14
# print(hex(f22(0x87574234)))
# = 0xeaed0508

