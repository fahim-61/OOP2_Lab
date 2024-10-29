# Control flow
# Initial array of student grades
grades = [85, 78, 92, 45, 33, 67, 88, 41]

# Categorize each student's grade and display their grade category
def categorize_grades(grades):
    print("Grade Categories:")
    for score in grades:
        if score > 80:
            grade = 'A'
        elif 60 <= score <= 80:
            grade = 'B'
        elif 40 <= score < 60:
            grade = 'C'
        else:
            grade = 'F'
        print(f"Score: {score} - Grade: {grade}")

# Function to boost grades by 5% using map()
def boost_grades(grades):
    boosted_grades = list(map(lambda x: x * 1.05, grades))
    return boosted_grades

# Find boosted grades above 90 using a lambda function
def boosted_above_90(boosted_grades):
    above_90 = list(filter(lambda x: x > 90, boosted_grades))
    return above_90

# Call the functions to solve the tasks
categorize_grades(grades)

boosted_grades = boost_grades(grades)
print(f"Boosted Grades:\n{boosted_grades}")

above_90_grades = boosted_above_90(boosted_grades)
print(f"Boosted Grades Above 90:\n{above_90_grades}")
