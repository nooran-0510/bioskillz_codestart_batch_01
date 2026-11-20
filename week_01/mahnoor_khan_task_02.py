"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : Mahnoor Khan

 Save as  : yourname_task_02.py   (example: ali_task_02.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Tip: These tasks also use what you learned in Session 01,
 such as input(), typecasting and operators.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 02 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 02 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Your code here

# Slicing [1:4] takes positions 1,2 and 3 (the end is excluded),so yth
print("Python"[1:4])
print("banana".count("an"))      # "banana" contains “an” twice, so 2
print("Hello"[-1])              # -1 means the last character
# Strings compare by character code, and uppercase letters come before lowercase ones, so "Z" < "a" is True
print("Zebra" < "apple")
print(5 > 3 and 2 > 4)          # and needs both sides true, and 2 > 4 is false
# An empty string counts as False, so not "" is True
print(not "")

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Your code here

# Bug 1: SyntaxError, line 2. The if line is missing a colon (:).
# Bug 2: IndentationError, line 5. print("Fail") must be indented under else.
# Bug 3 (bonus): No error, but typing "Yes" with a capital Y does nothing,
# because "Yes" != "yes".

marks = int(input("Marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

answer = input("Again? ").lower()
if answer == "yes":
    print("Restarting...")


# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Your code here

# strip removes extra spaces, title capitalises each word
name = input("Student name: ").strip().title()
marks_text = input("Marks (0-100): ").strip()

if marks_text.isdigit():
    marks = int(marks_text)

    if marks > 100:
        print("Marks must be 0-100")
    else:
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{name} scored {marks}/100 → Grade {grade}")
else:
    print("Please enter a valid number.")


# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
#
# Ask the user to enter their full name. Then print:
#   - the name in uppercase          (use upper())
#   - the name in lowercase          (use lower())
#   - the name in title case         (use title())
#   - the total number of characters, including spaces (use len())
#   - how many times the letter "a" appears (use count())
#
# Example output:
#   Enter your full name: ayesha khan
#   Uppercase: AYESHA KHAN
#   Lowercase: ayesha khan
#   Title case: Ayesha Khan
#   Total characters: 11
#   Number of 'a': 3
# --------------------------------------------------------------

# Your code here

name = input("Enter your full name: ")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title case:", name.title())
print("Total characters:", len(name))
print("Number of 'a':", name.count('a'))


# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
#
# Ask the user to enter an email address. Then print:
#   - the first character               (use indexing)
#   - the last character                (use negative indexing)
#   - the position of "@"               (use find())
#   - the username, the part before "@" (use slicing)
#   - the domain, the part after "@"    (use slicing)
#   - whether it is a Gmail address     (use endswith())
#
# Hint: Save the position of "@" in a variable first, then use
# it inside your slices.
#
# Example output:
#   Enter your email: ali.khan@gmail.com
#   First character: a
#   Last character: m
#   Position of @: 8
#   Username: ali.khan
#   Domain: gmail.com
#   Gmail address: True
# --------------------------------------------------------------

# Your code here

email = input("Enter your email: ")
print("First character:", email[0])
print("Last character:", email[-1])
position = email.find("@")
print("Position of @:", position)
username = email[:position]
domain = email[position + 1:]
print("Username:", username)
print("Domain:", domain)
print("Gmail address:", email.endswith("@gmail.com"))

# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
#
# Ask the user for their name and their marks in three
# subjects, each out of 100. Convert the marks to floats.
# Calculate the total and the percentage, then print a short
# report using f-strings. Show the percentage with exactly
# 2 decimal places.
#
#   Percentage = (Total / 300) * 100
#
# Hint: {percentage:.2f} shows a number with 2 decimal places.
#
# Example output:
#   Enter your name: Sara
#   Enter marks for Subject 1: 78
#   Enter marks for Subject 2: 85.5
#   Enter marks for Subject 3: 90
#   ----- Report Card -----
#   Name: Sara
#   Total: 253.5 out of 300
#   Percentage: 84.50%
# --------------------------------------------------------------

# Your code here

name = input("Enter your name: ")
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

print("----- Report Card -----")
print("Name:", name)
print("Total:", total, "out of 300")
print(f"Percentage: {percentage:.2}%")

# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
#
# Ask the user to enter their marks (0 to 100) and convert them
# to an integer. Print their grade using this scale:
#
#   85 to 100  ->  A
#   70 to 84   ->  B
#   55 to 69   ->  C
#   40 to 54   ->  D
#   0 to 39    ->  F
#
# If the marks are below 0 or above 100, print "Invalid marks".
#
# Hint: Check for invalid marks first.
#
# Example output 1:
#   Enter your marks: 72
#   Grade: B
#
# Example output 2:
#   Enter your marks: 105
#   Invalid marks
# --------------------------------------------------------------

# Your code here

subject = int(input("Enter marks for the subject: "))
if subject < 0 or subject > 100:
    print("Invalid marks!")
else:
    if subject >= 85:
        grade = "A"
    elif subject >= 70:
        grade = "B"
    elif subject >= 55:
        grade = "C"
    elif subject >= 40:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)

# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
#
# The correct login details are:
#   username: codestart
#   password: python123
#
# Ask the user for a username and a password.
#   - The username should NOT be case-sensitive, and extra
#     spaces should be ignored. (Use strip() and lower().)
#   - The password IS case-sensitive.
#
# Use a nested if statement:
#   - If the username is correct, check the password:
#       correct password -> "Login successful. Welcome to CodeStart!"
#       wrong password   -> "Incorrect password. Please try again."
#   - If the username is wrong -> "Username not found."
#
# Example output 1:
#   Enter username:   CodeStart
#   Enter password: python123
#   Login successful. Welcome to CodeStart!
#
# Example output 2:
#   Enter username: codestart
#   Enter password: Python123
#   Incorrect password. Please try again.
#
# Example output 3:
#   Enter username: student
#   Enter password: python123
#   Username not found.
# --------------------------------------------------------------

# Your code here

correct_username = "codestart"
correct_password = "python123"

username = input("Enter username: ").strip(
).lower()   # ignore spaces and capitals
password = input("Enter password: ")                   # case-sensitive

if username == correct_username:
    # Username is right, so now check the password (nested if)
    if password == correct_password:
        print("Login successful. Welcome to CodeStart!")
    elif password != correct_password:
        print("Incorrect password. Please try again.")
else:
    print("Username not found.")


# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_02.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
