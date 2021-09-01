# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Classes & Objects
# Date: 01 Sep 2021

# Main Data types: String, Numbers & Boolean values
# Different structures to store data like lists and dictionaries
# Not all things can be represented by the main data types
# e.g cannot represent phone, computer, person all in a string or number

# Classes and object enable you to create your own data type
# Class is another data type
#  Very useful and used in all major programme languages

# Model a real world object specifically Student

# An OBJECT is an actual student..... the row within the class
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name, student1.major, student1.gpa, student1.is_on_probation)
print(student2.gpa)


