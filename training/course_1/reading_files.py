# Learn python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw
# freeCodeCamp.org
# Course developed by Mike Dane.

# Exercise: reading files
# Date: 31 Aug 2021

# step 1 open file in python
    # open(insert relative pr absolute path or in the same file diretory)
    # open( file, mod = read (r), write (w), append (a), read/write (r+)
    # store file into variable
# step 2 check file is readeable
# step 3 close file when completed



employee_file = open("employees.txt", "r") # source file is in current working dir/
# print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# print(employee_file.readline() reads each line of the source file
# # print(employee_file.readlines()[] takes each line and puts it into an array
# print(employee_file.read())






