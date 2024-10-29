# Define the students' data
students_data = {
    "Alice": {"scores": [85, 86, 78], "favorites": {"Math", "Physics", "Art of living"}},
    "Bob": {"scores": [75, 87, 70], "favorites": {"Math", "English", "OOP"}},
    "Charlie": {"scores": [55, 88, 91], "favorites": {"OOP", "Chemistry", "Math"}},
    "David": {"scores": [78, 42, 85], "favorites": {"Physics", "Chemistry", "Math"}},
    "Eve": {"scores": [90, 45, 87], "favorites": {"Art of living", "Math", "English"}},
}

# Task 1: Highest and Lowest Scores
def find_highest_lowest_scores(data):
    all_scores = [score for student in data.values() for score in student['scores']]
    return max(all_scores), min(all_scores)

# Task 2: Average Scores for Each Student
def calculate_average_scores(data):
    average_scores = {student: sum(info['scores']) / len(info['scores']) for student, info in data.items()}
    return average_scores

# Task 3: Unique Favorite Subjects
def unique_favorite_subjects(data):
    all_subjects = set()
    for student in data.values():
        all_subjects.update(student['favorites'])
    return all_subjects

# Task 4: Common Favorite Subjects
def common_favorite_subjects(students_data):
    common_subjects = set.intersection(*[data["favorites"] for data in students_data.values()])
    return common_subjects

# Execute the functions
highest_lowest_scores = find_highest_lowest_scores(students_data)
average_scores = calculate_average_scores(students_data)
unique_subjects = unique_favorite_subjects(students_data)
common_subjects = common_favorite_subjects(students_data)

# Results
print(highest_lowest_scores)
print(average_scores)
print(unique_subjects)
print(common_subjects)
