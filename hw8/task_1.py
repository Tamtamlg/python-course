import random

LIST_LENGTH = 15


def generate_list(list_length):
    return [random.randint(1, 100) for _ in range(list_length)]


def calculate_even_and_odd_sum(lst):
    odd_sum = 0
    even_sum = 0

    for i in lst:
        if i % 2:
            odd_sum += i
        else:
            even_sum += i
    return (odd_sum, even_sum)


def compare_sum(tpl):
    return tpl[0] > tpl[1]


random_list = generate_list(LIST_LENGTH)
sum_tuple = calculate_even_and_odd_sum(random_list)
compare_result = compare_sum(sum_tuple)


print(random_list)
print('odd > even: ', compare_result)
