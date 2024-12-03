class Individual:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")


class Learner(Individual):
    def __init__(self, first_name, last_name, course_year):
        super().__init__(first_name, last_name)
        self.course_year = course_year

    def display(self):
        super().display()
        print(f"Course Year: {self.course_year}")


class Graduate(Learner):
    def __init__(self, first_name, last_name, course_year, completion_year):
        super().__init__(first_name, last_name, course_year)
        self.completion_year = completion_year

    def display(self):
        super().display()
        print(f"Completion Year: {self.completion_year}")


class CurrentLearner(Learner):
    def __init__(self, first_name, last_name, course_year, active_semester):
        super().__init__(first_name, last_name, course_year)
        self.active_semester = active_semester

    def display(self):
        super().display()
        print(f"Active Semester: {self.active_semester}")


class Mentor(Individual):
    def __init__(self, first_name, last_name, start_year):
        super().__init__(first_name, last_name)
        self.start_year = start_year

    def display(self):
        super().display()
        print(f"Start Year: {self.start_year}")


class Staff(Individual):
    def __init__(self, first_name, last_name, staff_id):
        super().__init__(first_name, last_name)
        self.staff_id = staff_id

    def display(self):
        super().display()
        print(f"Staff ID: {self.staff_id}")


# Create instances
graduate = Graduate("Eleanor", "Rigby", 2021, 2023)
current_learner = CurrentLearner("Mark", "Twain", 2024, 5)
mentor = Mentor("Isaac", "Newton", 2005)
staff = Staff("Albert", "Einstein", 112358)

# Display information
graduate.display()
current_learner.display()
mentor.display()
staff.display()
