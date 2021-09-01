# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Building a Multiple Choice Quiz
# Classes & Objects
# Date: 01 Sep 2021

from Question import Question

# List / array
question_prompt = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n (c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# an array of questions to ask on the test
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]

# write function to run quiz test

def run_test(questions):   # take a list of question objects as core parameter
    score = 0
    for question in questions:   # for each question object within the questions array I want to do something
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions)) + " Correct")

#  call function
run_test(questions)