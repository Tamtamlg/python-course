from modules.lists import generate_list
from modules.matrix import fill_matrix, print_matrix
from modules.concat import sum_or_concat


def main():
    # check lists module
    print(generate_list(10))
    print('-'*100)

    # check matrix module
    matrix = fill_matrix()
    print_matrix(matrix)
    print('-'*100)

    # check concat module 
    print(sum_or_concat())


if __name__ == '__main__':
    main()
