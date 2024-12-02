class Person:
    def __init__(self, fname, lname):
        print("Person Constructor")
        self.fname = fname
        self.lname = lname
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}")

class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        print("Student Constructor")
        Person.__init__(self,fname, lname)
        self.graduationyear = graduationyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.graduationyear}")
class AlumniStudent(Student):
    def __init__(self, fname, lname, graduationyear, alumni_id):
        print("AlumniStudent Constructor")
        Student.__init__(self,fname, lname, graduationyear)
        self.alumni_id = alumni_id
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.graduationyear}, Alumni ID: {self.alumni_id}")
class CurrentStudent(Student):
    def __init__(self, fname, lname, graduationyear, student_id):
        print("CurrentStudent Constructor")
        Student.__init__(self, fname, lname, graduationyear)
        self.student_id = student_id
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.graduationyear}, Current Year: {self.student_id}")


class Teacher(Person):
    def __init__(self, fname, lname, joiningyear):
        print("Teacher Constructor")
        Person.__init__(self, fname, lname)
        self.joiningyear = joiningyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Joining Year: {self.joiningyear}")


class Admin(Person):
    def __init__(self, fname, lname, joiningyear):
        print("Admin Constructor")
        Person.__init__(self, fname, lname)
        self.joiningyear = joiningyear
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Joining Year: {self.joiningyear}")


class Employee(Teacher, Admin):
    def __init__(self, fname, lname, joiningyear, ID):
        print("Employee Constructor")
        super().__init__(fname, lname, joiningyear)
        self.ID = ID
    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, ID: {self.ID}, Joining Year: {self.joiningyear}")





person1 = Person("Fahim", "Ferdous")
person1.display()

student1 = Student("Fahim", "Ferdous", 2026)
student1.display()

alumni_student1 = AlumniStudent("Farabi", "Hasan", 2022, "A12345")
alumni_student1.display()

current_student1 = CurrentStudent("Fahad", "Rahman", 2026, "B12345")
current_student1.display()

teacher1 = Teacher("Farabi", "Hasan", 2022)
teacher1.display()

admin1 = Admin("Faisal", "Rahman", 2020)
admin1.display()

employee1 = Employee("Samanta", "JR", 2022, "C12345")
employee1.display()
