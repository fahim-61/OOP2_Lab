class InvalidSalaryException(Exception):
    pass

class Worker:
    def __init__(self, name, monthly_salary):
        if 20000 <= monthly_salary <= 60000:
            self.name = name
            self.salary = monthly_salary
        else:
            raise InvalidSalaryException("Salary must be between 20000 and 60000.")

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

try:
    worker = Worker("John", 15000)
except InvalidSalaryException as e:
    print(e)
