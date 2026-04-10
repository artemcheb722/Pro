def string_length(s):
    return len(s)


print(string_length(input("Введи рядок: ")))


def foo1(str1, str2):
    return f'Цілий рядок: {str1 + str2}'


str1 = input('1str: ')
str2 = input('2str: ')

print(foo1(str1, str2))
