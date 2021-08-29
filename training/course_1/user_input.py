# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Input / Functions
# Date: 29 Aug 2021

print("test")

# User Input

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello " + user_name + "! You are " + user_age)

# Building a Basic Calculator
#  Note: where ever python takes input from user, it defaults to string data type

numb1 = input("Enter a number: ")
numb2 = input("Enter another number: ")
result = float(numb1) + float(numb2)
#  int or float to convert string data input into number data types

print(result)
