'''
This module contains functions for working with a matrix
'''
import random

DEFAULT_LENGTH = 5
RANDOM_FROM = 10
RANDOM_TO = 99


def fill_matrix(num_row=DEFAULT_LENGTH, num_col=DEFAULT_LENGTH):
    '''
    generate the matrix with random values
    '''
    matrix = []
    for row in range(num_row):
        lst = []
        for col in range(num_col):
            lst.append(random.randint(RANDOM_FROM, RANDOM_TO))
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list):
    '''
    print the matrix
    '''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='  ')
        print()


if __name__ == '__main__':
    pass
