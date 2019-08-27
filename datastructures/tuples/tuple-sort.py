#!/bin/python

# Sort list of tuples using second element in tuple

input_list = [(5,6), (4,2,3), (1,4)]

input_list.sort(key = lambda x: x[1])
print(input_list)