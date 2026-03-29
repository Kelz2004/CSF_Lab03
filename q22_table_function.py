# Task 22: Function to print the multiplication table

def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter number: "))
print_table(num)