class InvalidVoterError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be greater than or equal to 18.")

def Checker(age):
    if not isinstance(age, int) or age < 18:
        raise InvalidVoterError(age)
    print(f"Valid Voter: Age {age} is eligible for voting.")

try:
    user_age = int(input("Enter your age: "))
    Checker(user_age)

except ValueError:
    print("ValueError: Please enter a valid integer.")

finally:
    print("Age validation complete.")
