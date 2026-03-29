#Task 10: Multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(1, 11): # range(1, 11) starts at 1 and stops before 11
   
    print(f"{num} x {i} = {num * i}")  # This prints the math problem and the answer