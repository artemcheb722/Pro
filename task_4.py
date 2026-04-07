def check(number):
    return "Парне" if number % 2 == 0 else "Не парне"
num = int(input("Введіть число: "))
print(check(num))



def check1(numbers):
 return [i for i in numbers if i % 2 == 0]

nums = list(map(int, input("Введіть числа: ").split()))
print(check1(nums))
