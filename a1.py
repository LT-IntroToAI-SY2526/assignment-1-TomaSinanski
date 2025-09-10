# Assignment 1: AI-Generated Python Problems
# Name: Toma Sinanski

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class. I have some experience with Java and a little bit of html/bootstrap. Can you create 7 practice problems that cover:
> - How ariables and basic data types work
> - if/else/elif
> - for and while loops
> - Functions
> - Basic list operations
> 
> Make sure each problem has clear instructions and example inputs/outputs."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
🐍 Python Practice Problems
1. Variables and Data Types: Favorite Number

Task:
Create a program that asks the user for their name and their favorite number. Print a sentence that combines both.

Example:

Input:
Name: Alice
Favorite number: 7

Output:
Hello Alice! Your favorite number is 7.

""" 
# Ask the user for their name
name = input("Name: ")
favorite_number = input("Favorite number: ")
print("Hello " + name + "! Your favorite number is " + favorite_number)

"""

2. Conditionals: Even or Odd

Task:
Write a program that asks the user for an integer and prints whether it’s even or odd.

Example:

Input: 12
Output: 12 is even.

Input: 9
Output: 9 is odd.
"""
num = input("Number: ")
if num % 2 == 0:
    print(num + "is even.")
else :
    print(num + "is odd.")
"""

3. Loops: Counting Down

Task:
Write a program that asks the user for a positive integer n and then prints a countdown from n to 1.

Example:

Input: 5
Output:
5
4
3
2
1
"""
start = input("Starting value: ")
while start > 0:
    print(start + "/n")
    start -= 1
"""

4. Functions: Temperature Converter

Task:
Write a function celsius_to_fahrenheit(c) that takes a temperature in Celsius and returns it in Fahrenheit.
Then ask the user for a Celsius value, call the function, and print the result.

Formula:

F = (C × 9/5) + 32


Example:

Input: 0
Output: 0°C is 32.0°F
"""
def celsius_to_fahrenheit(c: float)->float:
    return (c * 9/5) + 32
celsius = input("Temperature in celsius: ")
print(celsius + "°C is " + celsius_to_fahrenheit(celsius) + "°F")
"""

5. Lists: Average of Numbers

Task:
Ask the user to enter 5 numbers (one at a time) and store them in a list.
Then calculate and print the average.

Example:

Input: 3, 5, 8, 10, 4
Output: The average is 6.0
"""
num1 = input("Add number: ")
num2 = input("Add number: ")
num3 = input("Add number: ")
num4 = input("Add number: ")
num5 = input("Add number: ")
print("The average is " + (num1+num2+num3+num4+num5)/5)
"""

6. Loops + Conditionals: Multiplication Table

Task:
Ask the user for a number n. Print its multiplication table from 1 to 10.
(Hint: use a for loop).

Example:

Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""
num = input("Number: ")
print(num + " x 1 = " + num * 1)
print(num + " x 2 = " + num * 2)
print(num + " x 3 = " + num * 3)
print(num + " x 4 = " + num * 4)
print(num + " x 5 = " + num * 5)
print(num + " x 6 = " + num * 6)
print(num + " x 7 = " + num * 7)
print(num + " x 8 = " + num * 8)
print(num + " x 9 = " + num * 9)
print(num + " x 10 = " + num * 10)
"""

7. Functions + Lists + Loops: Find the Largest Number

Task:
Write a function find_max(numbers) that takes a list of numbers and returns the largest one.
Ask the user to enter numbers separated by spaces, store them in a list, and call your function.

Example:

Input: 10 4 25 7 15
Output: The largest number is 25
"""
def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
user_input = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in user_input.split()]
largest = find_max(numbers_list)
print("The largest number is", largest)


# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


