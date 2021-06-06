def f23(x):
    pretable = [[f"{date(i[0])}",
                 f"{name(i[2])}",
                 f"{done(i[2])}"
                 ] for i in x]

    table = []
    for i in pretable:
        if i not in table:
            table.append(i)

    def transpose(tab):
        return [list(row) for row in zip(*tab)]

    z = transpose(table)

    return z


def date(x):
    a = x[6] + x[7] + '/' + x[3] + x[4] + '/' + x[0] + x[1]
    return a


def done(x):
    sd = "!Да"
    if sd in x:
        return "Выполнено"
    else:
        return "Не выполнено"


def name(x):
    rez = ""
    rez = x.replace(',', '').split(".")[0]+'.'
    return rez
