# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: Building a Multiple Choice Quiz
# Classes & Objects
# Date: 01 Sep 2021

# creation question data type
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
