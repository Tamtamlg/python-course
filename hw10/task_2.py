import random


RANDOM_FROM = 0
RANDOM_TO = 200
DEFAULT_LENGTH = 5
MAX_LENGTH = len(str(RANDOM_TO))


def fill_matrix(height=DEFAULT_LENGTH, width=DEFAULT_LENGTH):
    '''create and fill matrix'''
    matrix = []
    for row in range(height):
        lst = []
        for col in range(width):
            lst.append(random.randint(RANDOM_FROM, RANDOM_TO))
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list):
    '''print matrix'''
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(str(matrix[row][col]).rjust(MAX_LENGTH), end='  ')
        print()
    print()


if __name__ == '__main__':
    matrix_1 = fill_matrix()
    matrix_2 = fill_matrix(3)
    matrix_3 = fill_matrix(3, 7)
    print_matrix(matrix_1)
    print_matrix(matrix_2)
    print_matrix(matrix_3)
