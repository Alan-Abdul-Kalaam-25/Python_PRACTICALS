# Write a python program to create Class and Object.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter name: ")
age = int(input("Enter age: "))
s = Student(name, age)
s.display()
