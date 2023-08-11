#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    if size == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif size == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, sys.argv[i]))

