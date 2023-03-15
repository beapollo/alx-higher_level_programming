#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp.append(matrix[i][j] * matrix[i][j])
        new_matrix.append(temp)
        temp = []
    return(new_matrix)
