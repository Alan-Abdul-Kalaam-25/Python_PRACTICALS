# Check if a Set Is Superset Itself or Another Given Set

s1 = set(map(int, input("Enter elements of first set: ").split()))
s2 = set(map(int, input("Enter elements of second set: ").split()))

print(s1.issuperset(s2))
print(s1.issuperset(s1))
