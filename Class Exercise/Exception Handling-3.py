numbers = [12, 24, 36, 48]
divisor = int(input("Enter a divisor: "))

try:
    for number in numbers:
        result = number / divisor
        print(f"{number} divided by {divisor} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
