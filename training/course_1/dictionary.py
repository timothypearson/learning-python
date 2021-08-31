# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Dictionary
# Date: 30 Aug 2021

# a special structure to store info in key value pairs
# dictionary - the definition associated with the word and word is the key and the definition is the value

# Exercise:  Jan convert to January or Mar to March | Jan -> January, Mar -> March
# This exercise is a good use case to use a dictionary
# All keys in the dictionary must be unique w

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Zero",
    1: "One",
}

print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions.get(0, "Not a valid key"))

# Dictionaries used to store different types of data
