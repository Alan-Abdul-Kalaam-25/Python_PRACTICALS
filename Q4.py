# Get All the Subsets of a Given Size in a Set

from itertools import combinations

s = set(map(int, input("Enter elements of set separated by space: ").split()))

size = int(input("Enter the size of subsets: "))
subsets = list(combinations(s, size))
print(subsets)
