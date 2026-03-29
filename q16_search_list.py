# Task 16: Search for a number and stop when found

numbers = [2, 4, 6, 8, 10]
search_for = 8

for x in numbers:
    if x == search_for:
        print("Number found")
        break # We found it, so no need to keep looking at 10