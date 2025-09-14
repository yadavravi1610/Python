n = int(input("Enter a positive integer: "))

# Initialize sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total += i

# Print the result
print(f"The sum of the first {n} natural numbers is: {total}")