# Create a function Pall_n to print all the palindrome numbers between two ranges.


def Pall_n(start, end):
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            print(i, end=" ")


a = int(input("Enter start: "))
b = int(input("Enter end: "))
Pall_n(a, b)
