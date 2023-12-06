#!/usr/bin/python3

Prototype: def search_replace(my_list, search, replace):

    new_list = [word if word != search else replace for word in my_list]

    return new_list
