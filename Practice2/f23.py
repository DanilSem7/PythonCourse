def f23(x):
    preTable = [[f"{i[0].replace('‐', ' ').split()[2]} {i[0].replace('‐', ' ').split()[1]} {i[0].replace('‐', ' ').split()[0]}".replace(' ', '/'),
                 f"{i[2].replace(',', '').split('.')[0]+'.'}",
                 f"{i[2].split('!')[1].replace('Нет','Не выполнено').replace('Да','Выполнено')}",
                 ] for i in x]
    table = []
    for i in preTable:
        if i not in table:
            table.append(i)
    table = list(map(list, zip(*table)))
    return table


print(f23([['17‐02‐99', 'None', 'Горий, М.Ц.!Нет'], ['11‐11‐01', 'None', 'Тудук, С.Е.!Нет'], ['11‐11‐01', 'None', 'Тудук, С.Е.!Нет'], ['03‐02‐99', 'None', 'Лувберг, М.Ч.!Да']]))
print(f23([['20‐03‐03', 'None', 'Рекман, Ф.Г.!Нет'], ['27‐03‐00', 'None', 'Ватишли, П.З.!Нет'], ['27‐03‐00', 'None', 'Ватишли, П.З.!Нет'], ['22‐02‐99', 'None', 'Мемман, Б.Ш.!Нет']]))
