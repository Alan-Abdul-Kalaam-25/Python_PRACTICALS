# Remove the Given Items of a Set at Once

s = set(map(int, input("Enter elements of set: ").split()))

remove_items = set(map(int, input("Enter elements to remove: ").split()))

for i in remove_items:
    if i in s:
        s.remove(i)
print(s)
