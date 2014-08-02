#!/usr/bin/env python3

import sys

def checkLength(line):
    if len(line) > 80:
        return False
    else:
        return True


def checkSpaces(line):
    if len(line) <= 1:
        return True
    if line[-2].isspace():
            return False
    else:
        return True


def checkfile(filename):
    fd = open(filename)

    passing = True

    i = 0
    for line in fd:
        i = i+1
        if not checkLength(line):
            print("Line too long: " + filename + ": line "+str(i))
            passing = False
        if not checkSpaces(line):
            print("Trailing whitespaces: "+ filename + ": line "+str(i))
            passing = False

    if passing:
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This command takes only one argument",file=sys.stderr)
        exit(1)

    filename = sys.argv[1]

    checkfile(filename)
