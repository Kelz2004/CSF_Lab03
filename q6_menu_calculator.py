#task6. menu-driven program for basic calculations

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
num1, num2 = map(int, input(" Enter two numbers:").split()) #asking two numbers at once, separated by a space

if choice == 1:
    print("Sum =", num1 + num2)
elif choice == 2:
    print("Difference =", num1 - num2)
elif choice == 3:
    print("Product =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice")
