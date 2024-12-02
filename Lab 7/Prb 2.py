class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}")

class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = graduationyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.graduationyear}")

class Teacher(Person):
    def __init__(self, fname, lname, joiningyear):
        super().__init__(fname, lname)
        self.joiningyear = joiningyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.joiningyear}")

class Admin(Person):
    def __init__(self, fname, lname, joiningyear):
        super().__init__(fname, lname)
        self.joiningyear = joiningyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.joiningyear}")





person1 = Person("Fahim", "Ferdous")
person1.display()

student1 = Student("Fahim", "Ferdous", 2026)
student1.display()

teacher1 = Teacher("Farabi", "Hasan", 2022)
teacher1.display()

admin1 = Admin("Faisal", "Rahman", 2020)
admin1.display()

