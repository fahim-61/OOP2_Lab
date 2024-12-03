#Task 3
# Function to calculate factorial recursively
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Taking input
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is:", factorial(n))
