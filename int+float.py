def square_number(a):
    return a ** 2


number = int(input("Enter the number: "))
print(square_number(number))

###

def sum(a, b):
    return a + b


num1 = int(input('1number:'))
num2 = int(input('2number:'))

print(f'Sum: {sum(num1, num2)}')

###

def divmod(n1, n2):
    return f'Div: {n1 // n2}, Mod: {n1 % n2}'


a = int(input('a:'))
b = int(input('b:'))
print(divmod(a, b))


