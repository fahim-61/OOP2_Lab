#Task 4
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# Taking input
num = int(input("Enter a number to check if it's prime: "))
print(f"{num} is {'a prime number' if is_prime(num) else 'not a prime number'}.")
