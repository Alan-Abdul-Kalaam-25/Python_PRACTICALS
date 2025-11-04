# Write a program to perform binary search using recursion.


def binary_search(arr, l, r, x):
    if l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            return binary_search(arr, l, m - 1, x)
        else:
            return binary_search(arr, m + 1, r, x)
    return -1


arr = sorted(list(map(int, input("Enter elements: ").split())))
x = int(input("Enter element to search: "))
res = binary_search(arr, 0, len(arr) - 1, x)
if res != -1:
    print("Element found at position", res + 1)
else:
    print("Element not found")
