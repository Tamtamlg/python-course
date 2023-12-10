import random


matrix = []


def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer: ')
            if len(user_input) and int(user_input):
                return int(user_input)
            raise ValueError
        except ValueError:
            print('It must be an integer > 0')
            user_input = ''


def fill_matrix(matrix: list, size=5):
    for row in range(size):
        lst = []
        for col in range(size):
            lst.append(random.randint(10, 99))
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='  ')
        print()


def calc_first_diagonal(matrix):
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == row:
                counter += matrix[row][col]
    return counter


def calc_second_diagonal(matrix):
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == len(matrix) - 1 - row:
                counter += matrix[row][col]
    return counter


def get_center(matrix):
    if len(matrix) % 2:
        center = len(matrix) // 2
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col == center and row == center:
                    return matrix[row][col]
    else:
        return 'The matrix has no digit in center'


matrix_length = get_user_input()
fill_matrix(matrix, matrix_length)
print_matrix(matrix)
print('first diagonal: ', calc_first_diagonal(matrix))
print('second diagonal: ', calc_second_diagonal(matrix))
print('center: ', get_center(matrix))
