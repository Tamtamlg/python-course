import random


matrix = []
MIN_LENGTH = 5
RANDOM_FROM = 1
RANDOM_TO = 100


def get_user_input(variable_name):
    user_input = ''
    while not user_input:
        try:
            user_input = input(f'Enter an integer > {MIN_LENGTH} ({variable_name}): ')
            if len(user_input) and int(user_input) > MIN_LENGTH:
                return int(user_input)
            raise ValueError
        except ValueError:
            print(f'It must be an integer > {MIN_LENGTH}')
            user_input = ''


def fill_matrix(matrix: list, row_length=MIN_LENGTH, col_length=MIN_LENGTH):
    for row in range(row_length):
        lst = []
        for col in range(col_length):
            lst.append(random.randint(RANDOM_FROM, RANDOM_TO))
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == 0:
                print('|', str(matrix[row][col]).rjust(3), end='  |')
            else:
                print(str(matrix[row][col]).rjust(4), end='  |')
        print()


def replace_column(matrix: list, col_1: int, col_2: int):
    for row in range(len(matrix)):
        matrix[row][col_1], matrix[row][col_2] = matrix[row][col_2], matrix[row][col_1]
    return matrix


matrix_row = get_user_input('N')
matrix_col = get_user_input('M')

fill_matrix(matrix, matrix_row, matrix_col)
print_matrix(matrix)
print()
replace_column(matrix, -1, -2)
print_matrix(matrix)
