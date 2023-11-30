#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    total = 0
    for i in range(num_args):
        total += int(argv[i])
    print(total)
