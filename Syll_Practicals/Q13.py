# Write a program illustrating load() and dump() in binary file.

import pickle

data = ["Alan", 20, "BCA"]
f = open("data.dat", "wb")
pickle.dump(data, f)
f.close()
f = open("data.dat", "rb")
print("Data read from binary file:", pickle.load(f))
f.close()
