# Python Basics Examples

# 1. Variables and Data Types
name = "Alice"  # String variable
age = 25         # Integer variable
height = 5.6     # Float variable
is_student = True # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# 2. Functions
def greet(person):
    """Function to greet a person."""
    print(f"Hello, {person}!")

greet(name)

# 3. Conditionals
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 4. Loops
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# 5. File I/O
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nWelcome to Python basics!")

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)

# 6. Lists
fruits = ["apple", "banana", "cherry"]
print("\nFruits list:")
for fruit in fruits:
    print(fruit)

