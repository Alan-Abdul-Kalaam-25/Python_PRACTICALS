# Write a Python program to copy the contents of a file to another file in a text file.

import os

base_path = os.path.dirname(os.path.abspath(__file__))
src = input("Enter source file name: ")
dst = input("Enter destination file name: ")

src_path = os.path.join(base_path, src)
dst_path = os.path.join(base_path, dst)

f1 = open(src_path, "r")
f2 = open(dst_path, "w")
f2.write(f1.read())
f1.close()
f2.close()

print("File copied successfully from", src, "to", dst)
