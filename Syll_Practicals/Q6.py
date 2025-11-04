# Write a Python program to demonstrate the use of List, Tuple, Dictionary.

# List demonstration
l = [10, 20, 30, 40, 50]
print("Original List:", l)
l.append(60)
print("After append(60):", l)
l.insert(2, 25)
print("After insert(2, 25):", l)
l.remove(40)
print("After remove(40):", l)
print("Index of 30:", l.index(30))
print("List length:", len(l))
print("List reversed:", list(reversed(l)))

# Tuple demonstration
t = (5, 10, 15, 20, 10)
print("\nOriginal Tuple:", t)
print("Count of 10:", t.count(10))
print("Index of 15:", t.index(15))
print("Tuple length:", len(t))
print("Tuple slicing (1:4):", t[1:4])

# Dictionary demonstration
d = {"name": "Alan", "age": 20, "course": "BCA"}
print("\nOriginal Dictionary:", d)
d["age"] = 21
print("After modifying age:", d)
d["city"] = "Delhi"
print("After adding new key (city):", d)
print("All Keys:", list(d.keys()))
print("All Values:", list(d.values()))
print("All Items:", list(d.items()))
d.pop("course")
print("After removing 'course':", d)
