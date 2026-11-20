"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Mahnoor Khan

 Save as  : yourname_task_01.py   (example: ali_task_01.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Your code here
print(7 / 2)          # 7/2 = 3.5
print(7 // 2)         # 7//2 = 3, round off figure
print("7" + "2")      # "7" + "2" = "72"
print(type(7.0))      # type(7.0) = <class 'float'>
print(2 + 3 * 4 ** 2)  # 2 + 3 * 16 = 2 + 48 = 50
print(bool("0"))      # bool("0") = True

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Your code here

# Line 2 has "Name Error" because the variable is 'Name' not 'name'. It should be:
name = input("Enter your name: ")
print("Hello!", name)

# Line 4 has "Type Error" as we cannot combine a string and an integer. It should be:
age = int(input("Enter your age: "))
print("Next year: ", age + 1)

# Line 7 has "Syntax Error" as the closing inverted comma is missing. It should be:
print("Done")

# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Your code here
bill = float(input("Enter bill amount: "))
split = int(input("Number of friends: "))
each_person = bill // split
leftover = bill % split

print("Each person pays:", each_person)
print("Leftover amount:", leftover)

# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------

# Your code here
name = "Mahnoor Khan"
age = 22
height = 1.73
is_student = True
# String variable for name
print("Name: Mahnoor Khan", type(name))
# Integer variable for age
print("Age:", age, type(age))
# Float variable for height
print("Height in metres:", height, type(height))
# Boolean variable for student status
print("Is student:", is_student, type(is_student))

# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------

# Your code here
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)

# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------

# Your code here
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)

# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------

# Your code here
savings = 1000
print("Starting savings:", savings)

savings += 500
print("After gift:", savings)

savings -= 300
print("After buying books:", savings)

savings *= 2
print("After doubling:", savings)

# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------

# Your code here
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_ok = marks >= 80
attendance_ok = attendance >= 75

print("Marks 80 or more:", marks_ok)
print("Attendance 75% or more:", attendance_ok)
print("Qualifies for scholarship:", marks_ok and attendance_ok)

# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_01.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
