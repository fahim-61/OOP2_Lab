import sys

try:
    b = int(input("Enter a number: "))
    a = [10 / b, 20 / b, 30 / b, 0 / b]

    for i in range(len(a)):
        print(f"Result of a[{i}] / b: {a[i] / b}")

except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed.")
except ValueError:
    print("ValueError: Please enter a valid integer.")
except NameError:
    print("NameError: A variable used is not defined.")
except IndexError:
    print("IndexError: Attempted to access an index that doesn't exist.")
except TypeError:
    print("TypeError: A variable used is not defined.")
except:
    print("Unexpected error:")
else:
    print("All operations completed successfully without errors.")
finally:
    print("Program execution finished.")
