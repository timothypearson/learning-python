# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Classes & Objects
# Date: 01 Seo 2021

# Main Data types: String, Numbers & Boolean values
# Different structures to store data like lists and dictionaries
# Not all things can be represented by the main data types
# e.g cannot represent phone, computer, person all in a string or number

# Classes and object enable you to create your own data type
# Class is another data type
#  Very useful and used in all major programme languages

# Model a real world object specifically Student

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# in the initialise function (within the brackets map out the attributes you want to describe student data type
# it defines the student data type
# NOW you can represent a student data type within your program