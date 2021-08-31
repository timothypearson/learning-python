
# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: For Loop
# Date: 31 Aug 2021
# common use case for a for loop is to move through a list / array

friends = ["Jim", "Karen", "Kevin"]
len(friends)  # identify the length of the list / array


for letter in "Giraffe Academy":
    print(letter)

for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

# loop through length of array
for friend_ in friends:
    print(friend_)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
