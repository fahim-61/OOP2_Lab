# Dictionary
def manage_courses():
    # Create the dictionary with the initial courses
    courses = {
        "CSE101": {"Course Name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course Name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course Name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"}
    }

    # Update the instructor's name for CSE102 to "Dr. Bob Jr."
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."

    # Add a new course CSE104
    courses["CSE104"] = {"Course Name": "Algorithms", "Credits": 4, "Instructor": "Dr. Dave"}

    # Remove the course CSE101
    courses.pop("CSE101", None)

    # Loop through the dictionary and print the course code along with its details
    for course_code, details in courses.items():
        print(f"Course Code: {course_code}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()  # Print a new line

# Call the function to manage and display courses
manage_courses()
