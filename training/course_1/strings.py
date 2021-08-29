# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Strings / Variables / Functions
# Date: 28 Aug 2021

print("   /|")
print("  / |")
print(" /  |")
print("/   |")

# Define variables

character_name = "Tom" # string data type
character_age = 50  # number data types
is_Male = False  # True or false dat types

print("There once was a man named " + character_name + ", ")
print("He was 35 years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".\n")


print("Giraffe\nAcademy")  # new line
print("Giraffe\"Academy\n")  # backslash tells python to render quotation mark

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool")  # concatenation two spaces post code for comment

phrase = "Giraffe Academy"
print(phrase.lower()) # lower case
print(phrase.upper()) # upper case
print(phrase.lower().isupper())  # lowercase
print(phrase.upper().isupper())  # uppercase
print(phrase.lower().islower())  # lowercase
print(phrase.upper().isupper())   # uppercase

phrase = "Giraffe Academy"
print(len(phrase))  # length of string

phrase = "Giraffe Academy"
print(phrase[0])  # []index will return letter in specific position; string index starts at zero
print(phrase[3])

# Index function
print(phrase.index("a"))  # passing a parameter, tells position of the letter in the index
print(phrase.index("Acad"))  # note case senstive

print(phrase.replace("Giraffe","Elephant"))  # two values, old & new

