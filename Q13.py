# Check if a Given Value Is Present in the Set or Not

s = set(map(int, input("Enter elements of set: ").split()))

val = int(input("Enter value to check: "))

if val in s:
    print("Present")
else:
    print("Not Present")
