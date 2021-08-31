# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: writing to files  # see employee.txt source file
# Date: 31 Aug 2021

with open("employees.txt", "r") as employee_file:
    print(employee_file.read())
with open("employees.txt", "a") as employee_file:
    employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters
with open("employees.txt", "w") as employee_file:
    employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters
with open("employees_1.txt", "w") as employee_file:
    employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters