# 1. Define the math "recipes"
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Error! Division by zero."
    return a / b

# 2. Start the infinite loop
while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exiting...")
        break # This stops the calculator 

    # Get numbers for the calculation
    num1, num2 = map(float, input("Enter two numbers: ").split())

    # 3. Decision making
    if choice == 1:
        print("Sum =", add(num1, num2))
    elif choice == 2:
        print("Difference =", subtract(num1, num2))
    elif choice == 3:
        print("Product =", multiply(num1, num2))
    elif choice == 4:
        print("Result =", divide(num1, num2))
    else:
        print("Invalid choice, try again.")