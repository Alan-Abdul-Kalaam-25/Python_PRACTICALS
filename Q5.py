# Determine if Two Sets Are Disjoint or Not Without In-built Methods

s1 = set(map(int, input("Enter elements of first set: ").split()))
s2 = set(map(int, input("Enter elements of second set: ").split()))

disjoint = True
for i in s1:
    if i in s2:
        disjoint = False
        break
print(disjoint)
