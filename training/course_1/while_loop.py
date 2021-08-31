# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: While Loop
# Date: 30 Aug 2021

# A while loop is a structure that allows code to be executed multiple times until condition is false
# a loop condition , loop guard, keep loop if true
# while loop a powerful structure

for i in range(1, 11):
    print(i)
print("Done with loop")

# Guessing Game - without limits

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")

# Guessing Game - introduce guess limits

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You win! Well Done!")

# Guessing Game - I was playing with shaping the code differently

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 4

while guess != secret_word and guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1

if guess_count < guess_limit:
        print("Out of Guesses, You Lose!")
else:
        print("You win! It took you " + str(guess_count) + " guesses. Well Done!")