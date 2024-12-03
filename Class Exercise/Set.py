# Initialize the sets
a = {1, 3, 5, 8, 7}
b = {0, False, 1, 5}

# Set operations
a.add(10)  # Add an element
a.discard(8)  # Remove element 8

union_set = a | b  # Union
intersection_set = a & b  # Intersection
difference_set = a - b  # Difference
symmetric_difference_set = a ^ b  # Symmetric difference

# Print results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric difference:", symmetric_difference_set)
