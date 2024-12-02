class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname,self.lname)


class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = graduationyear


    def display(self):
        print(f"Full Name: {self.fname} {self.lname}, Graduation Year: {self.graduationyear}")


person1 = Person("Fahim", "Ferdous")
person1.display()

student1 = Student("Fahim", "Ferdous", 2026)
student1.display()
