#Task 1 and 2
# Function to calculate (a + b)^2
def calculate_formula(a, b):
    return (a + b)**2

# Lambda function for the same formula
lambda_formula = lambda a, b: (a + b)**2

# Taking input
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Output using both methods
print("Result using the function:", calculate_formula(a, b))
print("Result using lambda function:", lambda_formula(a, b))
