# Task 21: Function to calculate factorial of a number

def calculate_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter number: "))
print("Factorial =", calculate_factorial(num))