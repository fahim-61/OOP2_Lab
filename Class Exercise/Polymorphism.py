class Division:
    def __init__(self, division_name):
        self.division_name = division_name

    def display_name(self):
        print(f"Division Name: {self.division_name}")


class Instructor(Division):
    def __init__(self, division_name, class_schedule):
        super().__init__(division_name)
        self.class_schedule = class_schedule

    def schedule_class(self):
        print(f"Class Scheduled: {self.class_schedule}")

    def grade_students(self):
        print("Grading Assignments...")

    def display_name(self):
        super().display_name()
        print("Role: Instructor")


class ContentCreator(Division):
    def __init__(self, division_name):
        super().__init__(division_name)

    def write_content(self):
        print("Drafting Content...")

    def publish_material(self):
        print("Publishing Learning Materials...")


class InstructorCreator(Instructor, ContentCreator):
    def __init__(self, division_name, class_schedule):
        super().__init__(division_name, class_schedule)

    def display_name(self):
        super().display_name()
        print("Role: Instructor and Content Creator")


# Create an instance of InstructorCreator
instructor_creator = InstructorCreator("Mathematics", "Monday 10 AM")

# Access methods
instructor_creator.schedule_class()
instructor_creator.grade_students()
instructor_creator.write_content()
instructor_creator.publish_material()
instructor_creator.display_name()
