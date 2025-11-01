# Square the Elements of Set Using for Loop

s = set(map(int, input("Enter elements of set: ").split()))

squared = set()
for i in s:
    squared.add(i * i)
print(squared)
