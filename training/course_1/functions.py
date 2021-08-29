# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Functions
# Date: 29 Aug 2021

# A function is a collection of code that performs a specific task
# Functions help organise your code into manageable pieces
# functions are a core concept in coding and python

# def is a key word, this person wants to use a function
# all code that comes after function pass to it we need to indent it with colon
#  Code to be passed to function must be indented

# In this function, it needs no data elements
def say_hi():
    print("Hello User")
# if you run this code, nothing will happen. You need to specific execution of function by calling it

print("Top")
say_hi()  # want to execute this function, it go to defined function above and then back
print("Bottom")

# a parameter is data that is passed to the function. Give the function information

# In this function, it needs one data elements
def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

# In this function, it needs two data elements
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")

# RETURN Statement - allow return data from a function

def cube(num):
    num*num*num

# call function and when run nothing happens
cube(3)

# print the call and it returns None
print(cube(3), "is result of calling the cube function is")

# RETURN gives a value back to whatever called the function

def cube(num):
    return num*num*num

print(cube(3), "is the result of calling the cube function.")

def cube(num):
    return num*num*num
# cannot put any code after the return statement, if you do it will not work
# return breaks out of the function

result = cube(4)
# defined function is called and 4 is the input that is passed to the function
# output from the called function is stored in variable named result

print(result, "is the result of calling the cube function.")