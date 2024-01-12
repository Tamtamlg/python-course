import random


MIN_SIZE = 5
RANDOM_FROM = 1
RANDOM_TO = 50
GAP = 3


def get_matrix_size():
    matrix_size = ''
    while not matrix_size:
        try:
            matrix_size = input('Enter an integer: ')
            if len(matrix_size) and int(matrix_size) and int(matrix_size) > MIN_SIZE:
                return int(matrix_size)
            raise ValueError
        except ValueError:
            print(f'It must be an integer > {MIN_SIZE}')
            matrix_size = ''


def get_columns_sum(matrix: list):
    result = []
    for col in range(len(matrix)):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        result.append(sum(temp))
    return result


def fill_matrix(size):
    return [[random.randint(RANDOM_FROM, RANDOM_TO) for j in range(size)] for i in range(size)]


def print_matrix(matrix: list, columns_sum: list):
    matrix_copy = matrix.copy()
    matrix_copy.append(columns_sum)
    for row in range(len(matrix_copy)):
        for col in range(len(matrix_copy[row])):
            print(str(matrix_copy[row][col]).rjust(GAP), end='  ')
        print()


def bubble_sort(array, is_reversed=False):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if is_reversed:
                condition = array[j] < array[j + 1]
            else:
                condition = array[j] > array[j + 1]
            if condition:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def sort_matrix(matrix: list[list], columns_sum: list):
    auxiliary_list = []

    for i in range(len(columns_sum)):
        for j in range(0, len(columns_sum) - i - 1):
            if columns_sum[j] > columns_sum[j + 1]:
                columns_sum[j], columns_sum[j +
                                            1] = columns_sum[j + 1], columns_sum[j]
                for row in matrix:
                    row[j], row[j + 1] = row[j + 1], row[j]

    for c in range(len(matrix)):
        temp = []
        for r in range(len(matrix)):
            temp.append(matrix[r][c])
        if c % 2:
            auxiliary_list.append(bubble_sort(temp))
        else:
            auxiliary_list.append(bubble_sort(temp, True))

    matrix.clear()

    for c in range(len(auxiliary_list)):
        temp = []
        for r in range(len(auxiliary_list)):
            temp.append(auxiliary_list[r][c])
        matrix.append(temp)

    return matrix


def main():
    matrix_size = get_matrix_size()
    matrix = fill_matrix(matrix_size)
    columns_sum = get_columns_sum(matrix)
    print_matrix(matrix, columns_sum)
    print()
    matrix = sort_matrix(matrix, columns_sum)
    print_matrix(matrix, columns_sum)


if __name__ == '__main__':
    main()
