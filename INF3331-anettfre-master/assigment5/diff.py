#!/usr/bin/env python3

import argparse
        
def diff(original, modified):
    """
    Compares an original file as a list with a modified version of the same file and returns a dictionary with
    the differences between the two.
    :param original: The original file as a list
    :param modified: The second list
    :return: A dictionary with differences between list 1 and list 2

    If a line has not been changed it is a 0 in front of the line
    If a line has been added it is a + in front
    If a line has been deleted it is a - in front

    """

    dict = {}
    for i in original:
        if modified.__contains__(i):
            dict[i] = "0"
        else:
            dict[i] = "-"
    
    for j in modified:
        if not dict.__contains__(j):
            dict[j] = "+"

    return dict    


def print_correct(output):
    """
    Prints to terminal the added, deleted and unchanged lines

    :param output: A dictionary with the differences
    :return: a string with the differences
    """
    string = ""
    for i, j in output.items():
        print(j, i, end="")
        string = string + j + i
    return string


def write_to_file(output):
    """
    Writes to file
    :param output: A string to write
    :return: None

    """

    file3 = "outputfile_diff.txt"
    with open(file3, 'w') as file3:
        file3.write(output)
    

def parse_arg():

    """
    Argparser for this script.

    :return:
    """
    parser = argparse.ArgumentParser(description="Prints the difference between one file and another")
    parser.add_argument("file1",help = "File 1")
    parser.add_argument("file2", help= "File 2")

    args = parser.parse_args()
    with open(args.file1,'r') as file1:
        file1 = file1.readlines()
    with open(args.file2,'r') as file2:
        file2 = file2.readlines()

    output = diff(file1,file2)
    newoutput = print_correct(output)
    write_to_file(newoutput)

if __name__ == '__main__':
    parse_arg()