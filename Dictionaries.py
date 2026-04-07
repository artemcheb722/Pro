def keys(dictionary):
    for k in dictionary:
        print(k)

example = input("Enter the dict: ")
ex_dict = eval(example)

keys(ex_dict)


def two_dicts_in_one(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = input("Enter first dict: ")
dict1_ex = eval(dict1)
dict2 = input("Enter second dict: ")
dict2_ex = eval(dict2)

print(two_dicts_in_one(dict1_ex, dict2_ex))
