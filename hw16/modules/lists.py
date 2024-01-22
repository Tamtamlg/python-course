'''
This module contains functions for working with a lists
'''
import random

RANDOM_FROM = 1
RANDOM_TO = 100


def generate_list(list_length: int, random_from=RANDOM_FROM, random_to=RANDOM_TO):
    '''
    generate the list with random values
    '''
    return [random.randint(random_from, random_to) for _ in range(list_length)]


def reverse(lst: list):
    '''
    reverse the list
    '''
    new_lst = lst[::-1]
    return new_lst


def get_even_idxs(lst: list):
    '''
    get even indexes from the list
    '''
    return lst[::2]


def get_odd_idxs(lst: list):
    '''
    get odd indexes from the list
    '''
    return lst[::1]


if __name__ == '__main__':
    pass
