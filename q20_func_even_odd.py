# Task 20: Function to check whether a number is even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter number: "))
print("The number is", check_even_odd(num))