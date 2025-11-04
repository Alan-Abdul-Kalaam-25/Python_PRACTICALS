# Write a function to print the sum of numbers in list having 3 at their units place.


def sum_of_numbers_with_3(lst):
    s = 0
    for num in lst:
        if num % 10 == 3:
            s += num
    return s


n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter number: ")))

result = sum_of_numbers_with_3(numbers)
print("Sum of numbers with 3 at their units place:", result)
