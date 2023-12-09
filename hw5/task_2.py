matrix = []


def fill_matrix(matrix: list, num_row=5, num_col=5):
    for row in range(num_row):
        lst = []
        for col in range(num_col):
            lst.append('**')
        matrix.append(lst)
    return matrix


def print_matrix(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end='  ')
        print()


def set_first_diagonal(matrix, counter_start):
    counter = counter_start
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == row:
                matrix[row][col] = counter
                counter += 1


def set_second_diagonal(matrix, counter_start):
    counter = counter_start
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == len(matrix) - 1 - row:
                matrix[row][col] = counter
                counter -= 1


fill_matrix(matrix)
set_first_diagonal(matrix, 10)
set_second_diagonal(matrix, 14)
print_matrix(matrix)