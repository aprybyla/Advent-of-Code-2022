# Advent of Code 2022 Day 1 part 2
# Solved: 05/12/2022
import numpy as np 
import pandas as pd
base_path = "C:/Users/alixa/OneDrive/Desktop/problems/"

#importing, opening, and reading my file 
my_file_path = base_path + "input_Day1.txt"

# when we use readlines, it tells the computer to read the 
# imported file as a list of strings separated by line breaks 
# as opposed to a single string 
my_file = open(my_file_path,"r")

# my_list is where I am saving my list in my script so that I can 
# work with it in my coding
my_list = my_file.readlines()

list_of_lists = []
new_list = []
num = 0

# this tells the computer to remove the /n (linebreak) from the 
# strings in the list, thus allowing us to create smaller lists 
for line in my_list: 
    # this is the assignment of the output replacing the old value,
    # meaning we have told the lines in my_list to remove the \n
    # and to refer to the lines without that \n
    line = line.strip('\n')
    #print(line.strip('\n'))
    if line == "": 
        # take what I've got so far, add it to the lists of lists
        list_of_lists.append(new_list)
        # create a new list, resetting so I can count/add again 
        new_list = []
    # this line tells the computer to add a numeric value to the 
    # previously created new list in our list of lists
    elif line.isnumeric() == True:
        line = int(line)
        new_list.append(line)

# first highest value
highest_value = 0
# create a list of summed nested lists
list_of_totals = []
# this for loop 
for list_of_numbers in list_of_lists: 
    total_calories = sum(list_of_numbers)
    highest_value = max(highest_value, total_calories)
    list_of_totals.append(total_calories)
print('First highest value: ',highest_value)
list_of_totals.remove(highest_value)

# second highest value 
highest_value = max(list_of_totals)
print('Second highest value: ',highest_value)
list_of_totals.remove(highest_value)

# third highest value 
highest_value = max(list_of_totals)
print('Third highest value: ',highest_value)


 
