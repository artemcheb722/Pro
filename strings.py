def foo():
    string = input("Введіть рядок: ")
    return f'Кількість символів: {len(string)}'


print(foo())


def foo1():
    str1 = input('1str: ')
    str2 = input('2str: ')
    return f'Цілий рядок: {str1 + str2}'


print(foo1())
