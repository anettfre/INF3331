#!/usr/bin/env python3

import re
import argparse
import highlighter as hl
# Here I assume the program should take a filename and a regex. Not two filenames
def find_match(findfile,regex,highlight):

    with open(findfile,"r") as file:
        lines = file.readlines()
        for line in lines:
            match = re.search(r"{}".format(regex),line)
            if(match)
                if highlight:
                    line = hl.color_string(regex,line,"38;5;2")
                    print(line)
                else:
                    print(line)

def parse_arg():
    parser = argparse.ArgumentParser(description="Print lines where regex matches in a file")
    parser.add_argument("file",type=str, help="Input file") #changed so it doesnt come as a list
    parser.add_argument("--highlight", action="store_true", help="want to highlight?")
    parser.add_argument("regex", type=str,nargs="+", help="regexes to search for")
    args = parser.parse_args()

    findfile, highlight, regexes = [x[1] for x in args._get_kwargs()]

    for regex in regexes:
        find_match(findfile,regex,highlight)


if __name__ == '__main__':
    parse_arg()
