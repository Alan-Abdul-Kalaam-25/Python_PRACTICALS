# Write a program to print the sum of first n prime numbers.

n = int(input("Enter n: "))

count = 0
num = 2
sum = 0

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        sum += num
        count += 1
    num += 1

print("Sum of first", n, "prime numbers is", sum)
