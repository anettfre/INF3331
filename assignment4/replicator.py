#!/usr/bin/python3

def repeat_bad(a):
    """Takes in a string, returns a different string
    Loops over alle the characters in string and counts how many times it have looped
    Asummes there is not an empty string
    """
    c = 0
    r = ""
    for i in a:
        r += i.upper()
        if c > 0:
            for j in range(c):
                r += i.lower()
        if c < len(a)-1:
            r += "-"
        c += 1

    print(r)
    return r

def repeat_good(someString):
        """Takes in a string, returns a different string
        Asummes there is not an empty string
        """
        counter = 0
        repeated = ""
        for i in someString:
            repeated += i.upper()
            if counter > 0:
                for j in range(counter):
                    repeated += i.lower()
            if counter < len(a)-1:
                repeated += "-"
            counter += 1

        print(repeated)
        return repeated

repeat_bad("hallo")
repeat_good("hallo")
