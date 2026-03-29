# Task 13: Keep taking input until the user enters 0

while True:
    num = int(input("Enter number: "))
    
    if num == 0:
        break # This command jumps out of the loop immediately
        
print("Loop ended")