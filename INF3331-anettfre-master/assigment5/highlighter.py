#!/usr/bin/env python3

import re
import argparse

def color_string(pattern, string, color):
    color_str = re.sub(r"({})".format(pattern),r"\033[{}m".format(color)+r"\1"+r"\033[0m",string)

    return color_str


def highlighter(regex_syntax, colors, filename):

    """
    Colors the words that matches a regex from regex file and color them according to the color file.

    :param regex_syntax: A file containing regular expressions
    :param colors: A file containing color codes
    :param filename: The name of the file to color
    :return: A string-copy of the input file with colored matches.

    Adds the regexes and colors from their respective files to two seperate lists.
    Replace the words that matches a regex from the inputfile and color them
    """

    
    with open(regex_syntax) as reg:
        regex_tofind = []
        for line in reg:
            pattern =  re.search(r"(?:\")(.*?)?(?:\"):(?<=:)(?:.*)",line) #matches everything on the line before colon
            name = re.search(r"\w*$",line)
            regex_tofind.append((pattern.group(1),name.group()))
            syntax = dict(regex_tofind)

    
    with open(colors) as color:
        color_words = []
        for line in color:
            code = re.search(r"(?<=:)(?:\s)(.*$)",line)
            name = re.search(r"\w*",line)
            color_words.append((name.group(),code.group()))
        colorstuff = dict(color_words)



    with open(filename) as file:
        read_file = file.read()

    for regex, key in syntax.items():
        read_file = color_string(regex,read_file,colorstuff[key])

    return read_file

def parse_arg():

    """
    A argparse for this script
    Prints the syntax highlighted input file.
    :return: None

    """

    parser = argparse.ArgumentParser(description="Makes a syntax highlighter based on a syntax- and theme-file.")
    parser.add_argument('syntax',help="A .syntax file containing regex expressions",metavar='[SYNTAX]')
    parser.add_argument('colors',help='A .theme file containing color schemes',metavar='[COLORS]')
    parser.add_argument('file',help="The file to syntax highlight", metavar ='[FILE]')
    args = parser.parse_args()


    highlighted = highlighter(args.syntax, args.colors, args.file)
    print(highlighted)

if __name__ == "__main__":
    parse_arg()
