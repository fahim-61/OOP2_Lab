employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    45: {5, 6, True, 7, 1}
}

print("Original Dictionary:")
print(employee)

print("\nLength of dictionary:", len(employee))
print("Type of dictionary:", type(employee))
print("Dictionary:", employee)

developer_skills = employee["type"]["developer"]
print("\nDeveloper skills:", developer_skills)

employee["permanent"] = False
print("\nUpdated 'permanent' to False:", employee)

employee["gender"] = "male"
print("\nAdded 'gender' key with value 'male':", employee)

del employee["age"]
print("\nRemoved 'age' key:", employee)

keys = employee.keys()
values = employee.values()
items = employee.items()
print("\nKeys:", keys)
print("Values:", values)
print("Items:", items)

print("\nIterating through the dictionary:")
for key, value in employee.items():
    print(f"Key: {key}, Value: {value}")
