# Task 15: Print 1-10 but skip 5

for i in range(1, 11):
    if i == 5:
        continue # This skips the print line below and goes to 6
    print(i)