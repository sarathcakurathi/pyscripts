#!/bin/python

# Create a list of tuples from a given list having number and its cube in each tuple
# Can be done using list comprehension

input_list = [3,8,4,5]
tuples = [(x,x*x*x) for x in input_list]
print(tuples)