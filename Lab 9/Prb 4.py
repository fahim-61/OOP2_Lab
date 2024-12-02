class SalaryNotInRangeError(Exception):
    pass
class NameOutOfBoxError(Exception):
    pass
def employee(name, salary):
    if not (10000 <= salary <= 50000):
        raise SalaryNotInRangeError("Salary is not in the range")
    if name == "Khalid":
        raise NameOutOfBoxError("Khalid cannot get job here")

def displaySalary():
    try:
        name = input("Enter employee name: ")
        salary = float(input(f"Enter salary for {name}: "))
        employee(name, salary)
    except SalaryNotInRangeError as e:
        print(e)
    except NameOutOfBoxError as e:
        print(e)
    else:
        print("Salary is in the range and valid!")

displaySalary()
