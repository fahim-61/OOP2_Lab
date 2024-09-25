# 1. Print "Hello Python"
print("Hello Python")

# 2. Arithmetic operations
a, b = 5, 3
print(a + b, a - b, a * b, a / b)

# 3. Area of a triangle
b, h = 5, 10
area = 0.5 * b * h
print(area)

# 4. Solve quadratic equation
import cmath
a, b, c = 1, 5, 6
d = (b**2) - (4*a*c)
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)
print(sol1, sol2)

# 5. Swap two variables
a, b = 5, 10
a, b = b, a
print(a, b)

# 6. Generate a random number
import random
print(random.randint(1, 100))

# 7. Convert kilometers to miles
km = 5
miles = km * 0.621371
print(miles)

# 8. Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 9. Display calendar
import calendar
print(calendar.month(2023, 9))

# 10. Check if number is Positive, Negative, or Zero
num = -5
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 11. Check if number is Odd or Even
num = 4
print("Even" if num % 2 == 0 else "Odd")

# 12. Check Leap Year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 13. Check Prime Number
num = 29
is_prime = all(num % i != 0 for i in range(2, num))
print(is_prime)

# 14. Print all Prime Numbers in an Interval
for num in range(10, 20):
    if all(num % i != 0 for i in range(2, num)):
        print(num, end=" ")

# 15. Factorial of a number
import math
num = 5
print(math.factorial(num))

# 16. Multiplication Table
num = 5
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

# 17. Fibonacci sequence
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

# 18. Check Armstrong Number
num = 153
sum_of_cubes = sum(int(digit)**3 for digit in str(num))
print("Armstrong" if num == sum_of_cubes else "Not Armstrong")

# 19. Find Armstrong Numbers in an Interval
for num in range(100, 500):
    sum_of_cubes = sum(int(digit)**3 for digit in str(num))
    if num == sum_of_cubes:
        print(num)

# 20. Sum of Natural Numbers
n = 10
print(sum(range(1, n + 1)))

# 21. Reverse of a String
s = "Hello"
print(s[::-1])

# 22. Sum of First Ten Natural Numbers
print(sum(range(1, 11)))

# 23. Find LCM
def lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1
print(lcm(4, 6))

# 24. Find HCF
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x
print(hcf(12, 15))

# 25. Decimal to Binary, Octal, Hexadecimal
num = 10
print(bin(num), oct(num), hex(num))

# 26. ASCII value of a character
char = 'A'
print(ord(char))

# 27. Simple Calculator
a, b = 10, 5
print(a + b, a - b, a * b, a / b)

# 28. Fibonacci using Recursion
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i), end=" ")

# 29. Factorial using Recursion
def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)
print(factorial(5))

# 30. Power of a number
print(pow(2, 3))

# 31. Add Two Matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(C)

# 32. Multiply Two Matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(result)

# 33. Transpose a Matrix
A = [[1, 2], [3, 4]]
print([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])

# 34. Sort Words in Alphabetic Order
s = "python programming"
words = s.split()
words.sort()
print(" ".join(words))

# 35. Remove Punctuation from a String
s = "Hello!!! How are you?"
punctuations = '''!()-[]{};:,<>./?@#$%^&*_~'''
print("".join(ch for ch in s if ch not in punctuations))

# 36. Convert list to string
lst = ['Python', 'is', 'fun']
print(" ".join(lst))

# 37. Convert int to string
num = 123
print(str(num))

# 38. Concatenate two strings
s1, s2 = "Hello", "World"
print(s1 + s2)

# 39. Generate Random String
import string
print(''.join(random.choice(string.ascii_letters) for i in range(10)))

# 40. Check if string is palindrome
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 41. Convert lowercase to uppercase and vice versa
s = "Hello"
print(s.swapcase())

# 42. Occurrence of substring
s = "Hello Python"
print(s.count("o"))

# 43. Append element in list
lst = [1, 2, 3]
lst.append(4)
print(lst)

# 44. Compare two lists
lst1, lst2 = [1, 2, 3], [1, 2, 3]
print(lst1 == lst2)

# 45. Convert list to dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))

# 46. Remove element from list
lst = [1, 2, 3]
lst.remove(2)
print(lst)

# 47. Add two lists
lst1, lst2 = [1, 2, 3], [4, 5, 6]
print(lst1 + lst2)

# 48. Convert list to set
lst = [1, 2, 3, 2, 1]
print(set(lst))

# 49. Convert list to string
lst = ['Python', 'is', 'fun']
print("".join(lst))

# 50. Remove duplicates from list
lst = [1, 2, 2, 3, 4, 4]
print(list(set(lst)))