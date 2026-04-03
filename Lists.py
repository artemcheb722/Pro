def average_value(numbers):
    return sum(numbers) / len(numbers)


nums = input('Enter the numbers: ')
nums_list = list(map(int, nums.split()))

print(f'Average value: {average_value(nums_list)}')






def two_lists_in_one(list1, list2):
    return list1 + list2


l1 = input('Enter words1: ').split()
l2 = input('Enter words2: ').split()
print(two_lists_in_one(l1, l2))
