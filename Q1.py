# Find the Differences Between Two Lists Using Sets

lst1 = []
lst2 = []

length = int(input("Enter the length of list 1: "))

for i in range(length):
    ele = input(f"ELE {i+1}: ")
    lst1.append(ele)

length = int(input("Enter the length of list 2: "))

for i in range(length):
    ele = input(f"ELE {i+1}: ")
    lst2.append(ele)

set1 = set(lst1)
set2 = set(lst2)

print(f"list 1 - list 2 = {set1 - set2}")
print(f"list 2 - list 1 = {set2 - set1}")