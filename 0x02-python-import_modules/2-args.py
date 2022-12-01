#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        j = 1
        print("{} arguments:".format((len(sys.argv) - 1)))
        for i in range(len(sys.argv[1:])):
            print("{}: {:s}".format(j, sys.argv[j]))
            j = j + 1
