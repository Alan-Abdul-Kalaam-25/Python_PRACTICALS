# Write a Python program that takes a text file as input and returns the number of words of a given text file.

fname = input("Enter file name: ")
f = open(fname, "r")
data = f.read()
print("Number of words:", len(data.split()))
f.close()
