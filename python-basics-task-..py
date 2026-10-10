"""Task 1: Python basics.

Covers data types, string concatenation, user input, f-strings,
arithmetic and logical operators, string methods, and lists.
"""

# ---------- 1. Data types ----------
x = 5
y = "java"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# ---------- 2. String concatenation ----------
word1 = "python "
word2 = "is "
word3 = "awesome"
print(word1 + word2 + word3)

# ---------- 3. Sum and average of two numbers ----------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
average = total / 2
print("sum =", total)
print("average =", average)

# ---------- 4. Formatted output ----------
pi = 3.14159
# The f prefix makes this an f-string, so expressions inside {} are evaluated.
# {pi:.2f} formats pi to two decimal places.
print(f"value of pi is approximately {pi:.2f}")

# ---------- 5. Arithmetic operators ----------
a = 10
b = 3
print(f"addition : {a + b}")
print(f"subtraction : {a - b}")
print(f"multiplication : {a * b}")
print(f"division : {a / b}")  # float division
print(f"floor division : {a // b}")  # integer division
print(f"modulus : {a % b}")  # remainder
print(f"exponentiation : {a ** b}")

# ---------- 6. Logical operators ----------
is_sunny = True
is_warm = False
print(f"sunny and warm : {is_sunny and is_warm}")
print(f"sunny or warm : {is_sunny or is_warm}")
print(f"not sunny : {not is_sunny}")

# ---------- 7. String methods ----------
text = "Hello, world!"
print(len(text))
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("H", "J"))

# ---------- 8. Lists ----------
fruits = ["apple", "banana", "cherry"]
print(f"fruits : {fruits}")
print(f"first fruit : {fruits[0]}")  # indexing
print(f"last fruit : {fruits[-1]}")  # negative indexing
print(f"slice fruits : {fruits[:2]}")  # slicing
fruits[1] = "orange"  # lists are mutable
print(f"modified fruits : {fruits}")
