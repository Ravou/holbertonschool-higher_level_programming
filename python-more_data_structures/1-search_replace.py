#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Crée une nouvelle liste avec remplacement des éléments
    return [replace if x == search else x for x in my_list]
