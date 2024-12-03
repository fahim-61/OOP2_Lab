# Initialize the tuple
a = (1, 3, 5, 7, 4)

# Tuple manipulations
odd_sum = sum(x for x in a if x % 2 != 0)  # Sum of odd numbers
index_of_five = a.index(5)
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = len(a) - odd_count
extended_tuple = a + (2, 4, 6)
modified_tuple = a[:-1]  # Remove the last element

# Print details
print("Sum of odd numbers:", odd_sum)
print(f"Index of 5: {index_of_five}")
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)
print("Extended tuple:", extended_tuple)
print("Tuple after removing last element:", modified_tuple)
