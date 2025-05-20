#!/usr/bin/python3
def squre_matrix_map(matrix=[]):
    return matrix ** 2

matrix=[]

resultat = map(square_matrix_map, matrix)
print(list(resultat))
