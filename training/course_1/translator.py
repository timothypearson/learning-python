# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Build a translator - Giraffe Language
# Date: 31 Aug 2021

# if it's a vowel, we want to translate it to 'G' =  Giraffe Language
# a powerful structure

def translate(phase):
    translation = ""
    for letter in phase:
        if letter.lower() in "aeiou":
            translation += "G" if letter.isupper() else "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))

#  if letter in "AEIOUaeiou":