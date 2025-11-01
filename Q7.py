# Count Number of Vowels in a Given String Using Sets

s = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

count = 0
for ch in s.lower():
    if ch in vowels:
        count += 1
print(count)
