#!/usr/bin/python3
from sys import argv
import sys
import os.path

def count(i):
    """A function for counting words, lines, and char in the i-th file
    since * take all the files it can find in the directory and put the in the terminal as arguments, the while loop goes through all
    for any new file started on the lines, words and chars start at 0"""
    numbLines = 0
    numbWrods = 0
    numbChars = 0
    file = open(sys.argv[i], "r") #opens the file so it can be read
    for line in file.read().split('\n'): #reads the file and splits on eatch newline
        numbLines += 1
        numbWrods += len(line.split()) #splits on the spaces
        numbChars += len(line) #assuming that space is a character and new line is not a character
    print(numbLines, numbWrods, numbChars, argv[i])

"""Starts to see if the 1st argument given in terminal is a file, the while loop goes through all the arguments given in terminal.
Then checks if it is a file. If it is then it counts in the function count by calling it. If it is not a file then it will not be counted"""
i = 1
while i != len(sys.argv):
    if os.path.isfile(sys.argv[i]) == True:
        count(i)
    else:
        pass
    i += 1
