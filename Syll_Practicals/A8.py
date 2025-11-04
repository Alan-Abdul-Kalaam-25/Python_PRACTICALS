# Write a program to read a binary file having employee data in the form of list and search for the record of a particular employee entered by user.

import pickle

f = open("emp.dat", "wb")
n = int(input("Enter number of employees: "))
data = []
for i in range(n):
    name = input("Enter name: ")
    sal = int(input("Enter salary: "))
    data.append([name, sal])
pickle.dump(data, f)
f.close()
f = open("emp.dat", "rb")
records = pickle.load(f)
name = input("Enter name to search: ")
for r in records:
    if r[0] == name:
        print("Record found:", r)
        break
else:
    print("Not found")
f.close()
