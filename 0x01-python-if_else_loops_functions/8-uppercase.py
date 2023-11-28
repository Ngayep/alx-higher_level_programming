#!/usr/bin/python3
def uppercase(str):
    u_str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            u_str += chr(ord(char) - 32)
        else:
            u_str += char
    print("{}".format(u_str))
    print()
