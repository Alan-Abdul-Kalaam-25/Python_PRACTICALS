# Write a program illustrating various functions of mathematical library in python.

import math

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

print("\n===== BASIC FUNCTIONS =====")
print(f"Absolute value of {x}: {math.fabs(x)}")
print(f"Ceiling of {x}: {math.ceil(x)}")
print(f"Floor of {x}: {math.floor(x)}")
print(f"Factorial of {int(x)}: {math.factorial(int(x))}")
print(f"Square root of {x}: {math.sqrt(x)}")
print(f"Power ({x}^{y}): {math.pow(x, y)}")

print("\n===== TRIGONOMETRIC FUNCTIONS =====")
print(f"sin({x}) = {math.sin(math.radians(x))}")
print(f"cos({x}) = {math.cos(math.radians(x))}")
print(f"tan({x}) = {math.tan(math.radians(x))}")
print(f"asin(0.5) = {math.degrees(math.asin(0.5))}")
print(f"acos(0.5) = {math.degrees(math.acos(0.5))}")
print(f"atan(1) = {math.degrees(math.atan(1))}")

print("\n===== EXPONENTIAL & LOGARITHMIC FUNCTIONS =====")
print(f"Exponential of {x}: {math.exp(x)}")
print(f"Natural log (ln) of {y}: {math.log(y)}")
print(f"Base-10 log of {y}: {math.log10(y)}")

print("\n===== ANGLE CONVERSIONS =====")
print(f"{x} degrees in radians: {math.radians(x)}")
print(f"{x} radians in degrees: {math.degrees(x)}")

print("\n===== CONSTANTS =====")
print(f"Pi value: {math.pi}")
print(f"Euler’s number (e): {math.e}")
print(f"Tau (2π): {math.tau}")
print(f"Infinity: {math.inf}")
print(f"NaN (Not a Number): {math.nan}")

print("\n===== ADVANCED FUNCTIONS =====")
print(f"GCD of {int(x)} and {int(y)}: {math.gcd(int(x), int(y))}")
print(f"LCM of {int(x)} and {int(y)}: {math.lcm(int(x), int(y))}")
print(f"Modf of {x} (fractional, integer): {math.modf(x)}")
print(f"Trunc of {x}: {math.trunc(x)}")
print(f"Copysign of {x} with sign of {y}: {math.copysign(x, y)}")
print(f"Hypotenuse of ({x}, {y}): {math.hypot(x, y)}")
print(f"fmod({x}, {y}) = {math.fmod(x, y)}")
print(f"isfinite({x}) = {math.isfinite(x)}")
print(f"isinf({x}) = {math.isinf(x)}")
print(f"isnan({x}) = {math.isnan(x)}")

print("\n===== SPECIAL FUNCTIONS =====")
print(f"Degrees to radians (example 180°): {math.radians(180)}")
print(f"Radians to degrees (example π): {math.degrees(math.pi)}")
print(f"Next power of 2 greater than {x}: {math.nextafter(x, math.inf)}")
print(f"Comb(5,2): {math.comb(5, 2)}")
print(f"Perm(5,2): {math.perm(5, 2)}")
print(f"Isqrt(25): {math.isqrt(25)}")
