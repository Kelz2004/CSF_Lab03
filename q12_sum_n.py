# Task 12: Calculate sum from 1 to n using a while loop

n = int(input("Enter n: "))
total_sum = 0
i = 1

while i <= n:
    total_sum += i # This is a shortcut for total_sum = total_sum + i
    i += 1

print("Sum =", total_sum)