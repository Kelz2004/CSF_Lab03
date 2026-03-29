# task 2. To check whether the given number is even or odd.

number = int(input("Enter a number:"))
if number % 2 == 0: # if the remainder when divided by 2 is 0, then it is even
    print("the number is even")
else: 
    print("the number is odd")