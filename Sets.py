def two_sets_in_one(set1, set2):
    return set1 | set2

set1 = set(map(int, input("Enter your first set: ").split()))
set2 = set(map(int, input("Enter your second set: ").split()))

print(two_sets_in_one(set1, set2))



def is_subset(set1, set2):
    return set1.issubset(set2)

set1_ex = set(map(int, input("Enter your first set: ").split()))
set2_ex = set(map(int, input("Enter your second set: ").split()))

print(is_subset(set1_ex, set2_ex))
