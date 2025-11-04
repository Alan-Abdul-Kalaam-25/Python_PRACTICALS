# Write a python program to insert data into CSV file and display it.

import csv

f = open("students.csv", "w", newline="")
w = csv.writer(f)
n = int(input("Enter number of records: "))
for i in range(n):
    name = input("Enter name: ")
    age = input("Enter age: ")
    w.writerow([name, age])
f.close()
f = open("students.csv", "r")
r = csv.reader(f)
for row in r:
    print(row)
f.close()
