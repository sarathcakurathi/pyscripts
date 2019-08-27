#!/bin/python

# This program will print occurrence of each distinct word in a file
fh = open("input.txt")

# fh.read() - Read content till end; returns a string
# fh.readlines() - Read file line by line; returns a list
lines = fh.readlines()
words = {}
for line in lines:
    line_words = line.rstrip().split(' ') # Remove trailing new line char and split in to list of words
    for word in line_words:
        if word in words:
           words[word] += 1
        else:
            words[word] = 1

print(words) # Print dict having word as key and value as occurrence 
print(words.values(), type(words.values())) # Type: dict_values()
print(sum(words.values()))