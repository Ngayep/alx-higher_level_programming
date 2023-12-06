#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = [word if word != search else replace for word in my_list]
    return new_list
