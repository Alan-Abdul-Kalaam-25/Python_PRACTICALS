# Write a Python program to demonstrate the use of recursion.


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter number: "))
print("Factorial:", fact(n))
