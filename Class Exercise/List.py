# Initialize the list
a = [1, 3, 5, 7, 9]

# List manipulations
a[-2], a[2] = a[2], a[-2]  # Swap values
a[3] = 50
a[2] = 19
a.append(100)  # Add 100 at the end
a.insert(2, 200)  # Add 200 at index 2
a.pop()  # Remove the last element
del a[1]  # Remove element at index 1
a.extend([2, 4, 6])  # Join new list

# Sort the list and find the maximum
sorted_a = sorted(a)
largest = max(a)

# Print details
print("Updated list:", a)
print("Sorted list:", sorted_a)
print("Largest number in list:", largest)

# Loop through and break on 5
print("Elements in list (stop at 5):")
for element in a:
    if element == 5:
        print(element)
        break
    print(element)
