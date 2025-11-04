# Write a function to find all duplicates in two different list.


def find_duplicates(a, b):
    dup = []
    for i in a:
        if i in b and i not in dup:
            dup.append(i)
    return dup


a = list(map(int, input("Enter elements of list 1: ").split()))
b = list(map(int, input("Enter elements of list 2: ").split()))
print("Duplicates are:", find_duplicates(a, b))
