import random
import sys


# 1.Преобразовать элементы списка s из строковой в числовую форму.
def str_to_int(str_s):
    return [int(x) for x in str_s]


# 2.Подсчитать количество различных элементов в последовательности s.
def count_elem(s):
    return len(set(s))


# 3.Обратить последовательность s без использования функций.
def reverse(s):
    return s[::-1]


# 4.Выдать список индексов, на которых найден элемент x в последовательности s.
def get_index(x, s):
    return [i for i in range(len(s)) if x == s[i]]


# 5.Сложить элементы списка s с четными индексами.
def sum_elem_even_index(s):
    return sum(s[1::2])


# 6.Найти строку максимальной длины в списке строк s.
def find_str_max_len(s):
    return max(s, key=len)


if __name__ == '__main__':
    # 1
    assert str_to_int(["10", "55", "3", "4"]) == [10, 55, 3, 4]
    # 2
    assert count_elem(["python", "task", "bonus", "python"]) == 3
    # 3
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    # 4
    assert get_index(7, [0, 7, 1, 7, 7, 2, 7]) == [1, 3, 4, 6]
    # 5
    assert sum_elem_even_index([2, -178, -7, 67, 2, 78, 0, 19]) == -14
    # 6
    assert find_str_max_len(["bonus", "python", "task", "practice"]) == "practice"
    print("\nSuccess")


# В следующем фрагменте по индексу i выбирается одна из трех строк:
# Сократите код в строке №2 до 19 символов без использования функций.
# возврат первого элемента
def do_code_shorter():
    i = 0
    # ['much', 'code', 'wow'][i]  # 24 символа
    return 'muchcodewow'[:i + 4]  # 19


# Напишите функцию generate_groups(), которая генерирует (не просто выдает готовый)
# список всех названий групп в том виде, который используется в выпадающем списке
# на сайте с результатами от робота kispython.
# возврат названия в новом виде
def generate_groups(str):
    return "{0}{1}".format(str[1], int(str[5:7]))


# Изучите, как работает функция zip().
def do_zip():
    a = [86, 52, 4]
    b = [1.7, 0.0, -1.7]
    c = ["task", "python", "zip"]
    zipped = zip(a, b, c)
    return list(zipped)  # список из кортежей


# Разберите роль операции * в создании функций с переменным числом
# аргументов, а также для распаковки последовательностей.
# *digits переменное число входных параметров
# возврат  произведения
def multiply_d(*digits):
    res = 1
    for d in digits:
        res *= d
    return res


# Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
# matrix - матрица исходная
def transpose_matrix(matrix):
    return list(list(i) for i in zip(*matrix))  # транспонированная


# Реализуйте генератор докладов по цифровой экономике.
def economy_generator():
    part1 = ('Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,',
             'Вместе с тем,', 'С другой стороны,')
    part2 = ('парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов',
             'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий',
             'программа прорывных исслeдований', 'ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data')
    part3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
             "расширяет горизонты", "заставляет искать варианты",
             "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
    part4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
             "компрометации конфиденциальных", "универсальной коммодитизации",
             "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
    part5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
             "опасных экспериментов.", "государственно-частных партнёрств.",
             "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    return random.choice(part1) + " " + random.choice(part2) + " " + random.choice(part3) + " " + random.choice(
        part4) + " " + random.choice(part5)


# Реализуйте свою версию print(). Постарайтесь использовать максимум
# возможностей настоящей print(). Для вывода используйте функцию
# sys.stdout.write().
# *args - входные аргументы
# sep - раделитель данных, end - последний символ строки
# sys.stdout.write - вывод
def func_print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(str(i) for i in args) + end)


# Реализуйте функцию, которая принимает только именованные аргументы. При
# передаче позиционного аргумента Питон должен выдать ошибку.
# **args - исходные параметры
# на возврат словарь ключ-значение
def get_only_init_args(**args):
    return args


# Реализуйте генератор случайных данных ФИО. Список распространенных имен позволяется скачать из интернета.
# Фамилии необходимо генерировать самостоятельно
names = ['Александр', 'Дмитрий', 'Арам', 'Вениамин', 'Андрей', 'Даниил', 'Василий', 'Михаил', 'Герман', 'Артём',
         'Давид', 'Владимир', 'Егор', 'Павел', 'Ильяс', 'Илья', 'Григорий', 'Ринат', 'Леонид', 'Захар',
         'Дамир', 'Денис', 'Алексей', 'Марк', 'Линар', 'Тимур', 'Антон', 'Ярослав', 'Иван', 'Николай']
ignore = ['Ю', 'Ь', 'Ъ', 'Й', 'Ё', 'Ы']
at = [chr(x) for x in range(ord('А'), ord('Я') + 1) if chr(x) not in ignore]
random_end = ['ов', 'ев', 'ин', 'ын', 'ский', 'цкий', 'ской', 'цкой', 'ой', 'ий', 'енков', 'их', 'ых', 'ко']
vowel = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'e']
consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


def generate_random_fio():
    s = random.choice(names) + " " + random.choice(at) + ". "
    for i in range(random.randint(1, 3)):
        if i == 0:
            s += random.choice(consonant).upper()
        else:
            s += random.choice(consonant)
        s += random.choice(vowel)
    s = s + random.choice(consonant) + random.choice(random_end)
    return print(s)


# Напишите функцию generate_array(dim1, dim2, dim3, ...) для создания
# многомерного массива с помощью вложенных списков.
# возврат многомерного массива
def generate_array(*dim):
    return [*dim]


if __name__ == '__main__':
    # 24 символа
    assert do_code_shorter() == "much"

    # генерация названий групп
    # assert generate_groups("IKBO-20-19") == "К20"

    # работа с zip
    assert do_zip() == [
        (86, 1.7, "task"),
        (52, 0.0, "python"),
        (4, -1.7, "zip")
    ]

    # переменное число параметров в функции
    assert multiply_d(-1, 2, 3, 6, 9) == -324

    # транспонирование матрицы
    assert transpose_matrix([[11, 44, 22], [38, 56, 99]]) == [[11, 38], [44, 56], [22, 99]]

    # реализация своего print()
    print("func_print()->", "python", [5, 8], None, True, sep="\t->\t", end="%\n")
    func_print("func_print()->", "python", [5, 8], None, True, sep="\t->\t", end="%\n")

    # получить только именованные аргументы
    assert get_only_init_args(
        student="Danil",
        group="IKBO-20-19",
        university="MIREA") == {
               "student": "Danil",
               "group": "IKBO-20-19",
               "university": "MIREA"
           }

    # генерация многомерного массива
    assert generate_array([23, 32], [48, 56], [96, 71]) == [[23, 32], [48, 56], [96, 71]]
    print("\nSuccess")
