#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        i = len(matrix)
        for x in range(i):
            for y in range(len(matrix[x])):
                if y == len(matrix[x]) - 1:
                    print("{:d}".format(matrix[x][y]), end="$")
                else:
                    print("{:d}".format(matrix[x][y]), end=" ")
            print()
    else:
        print('$')
