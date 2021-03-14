def f21(x):
    if x[2] == 2002:
        return 9
    elif x[2] == 1991:
        return 10
    elif x[2] == 1963:
        if x[1] == 'glyph':
            if x[0] == 'lua':
                return 0
            elif x[0] == 'nim':
                return 1
            elif x[0] == 'ada':
                return 2
        elif x[1] == 'nesc':
            if x[0] == 'lua':
                return 3
            elif x[0] == 'nim':
                return 4
            elif x[0] == 'ada':
                return 5
        elif x[1] == 'sas':
            if x[3] == 'tla':
                return 6
            elif x[3] == 'rdoc':
                return 7
            elif x[3] == 'oz':
                return 8



