# Find Common Elements of Three Given Lists Using Sets

l1 = list(map(int, input("Enter elements of list1: ").split()))
l2 = list(map(int, input("Enter elements of list2: ").split()))
l3 = list(map(int, input("Enter elements of list3: ").split()))

common = list(set(l1) & set(l2) & set(l3))
print(common)
