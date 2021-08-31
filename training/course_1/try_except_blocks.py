# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Try / Except
# Date: 31 Aug 2021

# Try / Except blocks  (to protect our program to catch invalid inputs)

# Below showing when use puts a string instead of a number
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

#  except is a broad all
#  also we can accept specific types of errors
# Best practice in python is to accept specific errors

# Below showing scenario when you put zero divison error
try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

