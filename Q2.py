# Check if a Given String Is Heterogram or Not

s = input("Enter a string: ")

if len(s) == len(set(s)):
    print("Heterogram")
else:
    print("Not Heterogram")
