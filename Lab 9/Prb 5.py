try:
    a = [5,10,15,20]
    for i in range(len(a)):
        print(a[i])
        try:
            b=int(input("Enter a number: "))
            print(a[i]/b)
        except ZeroDivisionError:
            print("Division by zero")

    print(a[6])

except IndexError:
    print("IndexError: Attempted to access an index that doesn't exist.")
except ValueError:
    print("ValueError: Please enter a valid integer.")
except NameError:
    print("NameError: A variable used is not defined.")
else:
    print("All operations completed successfully without errors.")
finally:
    print("Program execution finished.")
