# Write a program to demonstrate the use of different operators in python.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n===== ARITHMETIC OPERATORS =====")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print("\n===== COMPARISON OPERATORS =====")
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} > {b} → {a > b}")
print(f"{a} < {b} → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")

print("\n===== LOGICAL OPERATORS =====")
print(f"({a} > 0) and ({b} > 0) → {(a > 0) and (b > 0)}")
print(f"({a} > 0) or ({b} > 0) → {(a > 0) or (b > 0)}")
print(f"not({a} > 0) → {not(a > 0)}")

print("\n===== BITWISE OPERATORS =====")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"{a} ^ {b} = {a ^ b}")
print(f"~{a} = {~a}")
print(f"{a} << 1 = {a << 1}")
print(f"{a} >> 1 = {a >> 1}")

print("\n===== ASSIGNMENT OPERATORS =====")
x = a
print(f"x = {x}")
x += b
print(f"x += {b} → {x}")
x -= b
print(f"x -= {b} → {x}")
x *= b
print(f"x *= {b} → {x}")
x /= b
print(f"x /= {b} → {x}")
x //= b
print(f"x //= {b} → {x}")
x %= b
print(f"x %= {b} → {x}")
x **= b
print(f"x **= {b} → {x}")

print("\n===== IDENTITY OPERATORS =====")
print(f"a is b → {a is b}")
print(f"a is not b → {a is not b}")

print("\n===== MEMBERSHIP OPERATORS =====")
lst = [1, 2, 3, 4, 5]
print(f"List = {lst}")
print(f"{a} in list → {a in lst}")
print(f"{b} not in list → {b not in lst}")
