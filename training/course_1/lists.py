# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: List / Functions
# Date: 29 Aug 2021

friends = ["kevin", "Karen", "Jim"]
# indexpos    0        1       2
# how do we access each element in the list
# each element is assigned an index; first index is zero

print(friends[0] + " index position 0")
print(friends[1] + " index position 1")
print(friends[2] + " index position 2")

print(str(friends[1:]) + " listed friends from index 1")  # Me applying learnings

friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
#index pos   0          1       2       3       4
print(friends[1:])  # return all element from 1 onwards
print(friends[1:3])   # return 1 to 2 only
print(friends[:])  # list all elements
print(friends[:4]) # return the first 4 elements

# modify element
friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends)

# List functions
# functions to use on lists

lucky_numbers = [16, 42, 15, 4, 23, 8]
lucky_numbers.sort()
print(lucky_numbers, " sorted in ascending order")
friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends, "sorted in ascending order")
print(friends)
friends.extend(lucky_numbers)  # add two lists together
print(friends, " added two lists together")
friends.append("Creed")
print(friends, " appended another name on the end of the two lists")
friends.insert(1, "Kelly")
print(friends, " insert new name in index position 1")
friends.remove("Jim")
print(friends, "removes Jim from the list")
print(friends.index("kevin"), " identifies index position of Kevin")
friends.insert(3, "Oscar")
print(friends)
print(friends.count("Oscar"), "instances Oscar exists in this list")
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2, " demonstrates copy function for copying a list")
friends2.clear()
print(friends2, " cleared copied list labelled friends2")
#  print(friends.index("Mike"), " identifies error as Mike is not in the list



