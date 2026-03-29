# Task 19: Define a function to add two numbers

def add_numbers(a, b):
    return a + b

# Input two numbers (using that map trick we learned!)
num1, num2 = map(int, input("Enter two numbers: ").split())

print("Sum =", add_numbers(num1, num2))