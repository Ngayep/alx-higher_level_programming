#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    num_args = len(argv) - 1
    if num_args == 0:
        print("{} arguments.".format(0))
    else:
        plural = 's' if num_args > 1 else ''
        print("{} argument{}:".format(num_args, plural))
        for i in range(1, len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
