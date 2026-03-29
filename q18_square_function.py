# Task 18: Define a function that returns the square of a number

def get_square(n):
    return n * n  # This 'sends' the result back

num = int(input("Enter number: "))
result = get_square(num) # We catch the returned value here
print("Square =", result)