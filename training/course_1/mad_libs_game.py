# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Mad Libs Game
# Take a input of random words and make into a story
# Date: 29 Aug 2021

# Classic Poem
print("Classic Poem")
print("Roses are red")
print("Violet are blue")
print("I love you")

# Mix poem up - get user to put in random words

colour = input("Enter a colour: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + colour)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Homework - Make your own Mad libs game

container = input("Enter in a container ")
adjective1 = input("Enter in a adjective ")
adjective2 = input("Enter in another adjective ")
noun = input("Enter in a noun ")
animal = input("Enter in a type of animal ")
vegetable1 = input("Enter in a type of vegetable ")
vegetable2 = input("Enter in another type of vegetable ")
colour = input("Enter in a colour ")
adjective3 = input("Enter in another adjective ")

print("Make sure your lunch " + container + " is")
print("filled with nutritious " + adjective1 + " food. Do")
print("not go to the " + adjective2 + " food stand across")
print("the street from school. The hamburgers they")
print("serve are fried in " + noun + " and are made")
print("of " + animal + " meat. So take a sandwich made")
print("of " + vegetable1 + " or " + vegetable2 + " it's much")
print("healthier! Drink " + colour + " milk instead of")
print(adjective3 + " colas.")
