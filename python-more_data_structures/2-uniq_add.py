#!/usr/bin/python3
def uniq_add(my_list=[]):
    # On convertit la liste en ensemble (set) pour supprimer les doublons
    unique_values = set(my_list)
    # On additionne tous les éléments uniques
    return sum(unique_values)
