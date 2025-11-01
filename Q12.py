# Perform Intersection of Two Lists Using Set Methods

l1 = list(map(int, input("Enter elements of list1: ").split()))
l2 = list(map(int, input("Enter elements of list2: ").split()))

intersection = list(set(l1).intersection(set(l2)))
print(intersection)
