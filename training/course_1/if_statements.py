# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: IF Statements
# Date: 30 Aug 2021

# If statement helping our code make decisions based on specific conditions / input received

print("A if statement using a boolean value")

# create a boolean variable
is_male = False

if is_male:  # is_male is a boolean value so the condition is implicit in IF statement
    print("You are a male\n")
    # you can put many lines of code here
else:
    print('You are not a male\n')
    # you can put many lines of code here

print("A if statement using a boolean value with a OR function")

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both\n")
else:
    print('You neither male or tall\n')

print("A if statement using a boolean value with AND function")
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male\n")
else:
    print('You either not male or not tall\n')

print("A if statement with elif using a boolean value with AND & NOT function")
# how to make a decision and respond to each potential scenario / combination
# Based on when changing the boolean values for each variable combination

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male\n")
elif is_male:
    print("You are a short male")
elif is_tall:
    print("You are either not a male but are tall")
else:
    print('You are not a male or not tall\n')


# Comparison Exercise
# Pass 3 parameters as input and print out the biggest number we give it
# >= , >=, ==, !=, <=, <= are examples of comparison operators

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Exercise: Building a calculator to show practical application of if Statement

print(max_num(3, 4, 5), "is the biggest number.")
print(max_num(300, 40, 5), "is the biggest number.\n")

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

#  Example to introduction If Statement tutorial
# I wake up
#   If I'm hungry
#      I eat breakfast

# I leave my house
#   if it's cloudy
#     I bring an umbrella
# otherwise
#     I bring sunglasses

# I'm at a restaurant
#  if I want meat
#    I order a steak
# otherwise if I want pasta
#   I order spaghetti & meatballs
# otherwise
#  I order salad
