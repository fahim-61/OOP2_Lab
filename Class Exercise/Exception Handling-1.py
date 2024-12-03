class UnderageVoterException(Exception):
    pass

def verify_voter_age(age):
    if age < 18:
        raise UnderageVoterException("Voting eligibility requires age 18 or above.")
    else:
        print("You are eligible to vote.")

try:
    user_age = int(input("Enter your age: "))
    verify_voter_age(user_age)
except UnderageVoterException as e:
    print(e)
