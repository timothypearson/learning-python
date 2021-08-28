# Date: 28 Aug 2021
# Mini Python - For Beginners Exercise by #TechwithTim known as Tim Ruscica
# Youtube link: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1933s
# Exercice: Rock, Paper, Scissors

# My Exercise Objectives
    # No.1 write out the code outlined by #TechwithTim exercise
    # No.2 to flag identify what I learnt from each exercise
    # No.3 add my own code commentary to start getting into good habits

# My learnings from Tim's Tutorial
    # No.1 - syntax is very sentive (e.g. _underscore twice changes variable names)
    # No.2 - use of a list
    # No.3 - when I add the comment sections it helps show the code logic flow

# Introduction / Variable Setup

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# Collect User Input

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue 

# Setup Computer Opponent

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

# Playing Scenarios - User vs Computer

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost")
        computer_wins += 1

# Summary of results when user exits program

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
