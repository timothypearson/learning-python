# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: writing to files  # see employee.txt source file
# Date: 31 Aug 2021

employee_file = open("employees.txt", "r") # source file is in current working dir/
print(employee_file.read())
employee_file.close()

# append to file ("a")
employee_file = open("employees.txt", "a") # source file is in current working dir/
employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters
employee_file.close()

# write to file ("w"), means it will overwrite all existing records
employee_file = open("employees.txt", "w") # source file is in current working dir/
employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters
employee_file.close()

# write to file ("w"), create a new file by changing the name
employee_file = open("employees_1.txt", "w") # source file is in current working dir/
employee_file.write("\nKelly - Customer Service")  #\n new line knon as escape characters
employee_file.close()