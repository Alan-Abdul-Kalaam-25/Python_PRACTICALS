# Write a program to perform Linear Search.

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
x = int(input("Enter element to search: "))
for i in range(n):
    if arr[i] == x:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")
