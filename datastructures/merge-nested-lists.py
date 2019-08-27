#!/bin/python

# Program to merge nested lists at all levels into a single list.

def merge_nested_lists(sublist, final_list):
    for element in sublist:
        if isinstance(element, list):
            merge_nested_lists(element, final_list)
        else:
            final_list.append(element)
    return final_list

# Input is a nested list
input_list = [1,[2,3,[4,5],[6,[7,8]]], [9,10,11,[12,[13,14],15]]]
final_list = [] 
final_list = merge_nested_lists(input_list, final_list)
print(final_list)