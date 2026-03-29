# Function to determine the label

def get_label(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
n = int(input("Enter n: "))

for i in range(1, n + 1):
    label = get_label(i)
    print(f"{i} -> {label}")