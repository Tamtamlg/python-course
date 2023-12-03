result_list = []


def calculate(lst: list):
    print()
    print('sum:', get_sum(lst))
    print('arithmetic mean: ', get_arithmetic_mean(lst))
    print('min: ', get_min(lst))
    print('max: ', get_max(lst))
    print('number of even: ', get_number_of_even(lst))
    print('umber of odd: ', get_number_of_odd(lst))


def remove_zero_from_list(lst: list):
    for i in lst:
        if i == 0:
            lst.remove(i)
    return lst


def get_sum(lst: list):
    result = 0
    for i in lst:
        result += i
    return result


def get_arithmetic_mean(lst: list):
    try:
        return get_sum(lst)/len(lst)
    except:
        return 0


def get_min(lst: list):
    try:
        min_value = lst[0]
        for i in lst:
            if i < min_value:
                min_value = i
        return min_value
    except:
        return 0


def get_max(lst: list):
    try:
        max_value = lst[0]
        for i in lst:
            if i > max_value:
                max_value = i
        return max_value
    except:
        return 0


def get_number_of_even(lst: list):
    try:
        counter = 0
        for i in lst:
            if not i % 2:
                counter += 1
        return counter
    except:
        return 0


def get_number_of_odd(lst: list):
    try:
        counter = 0
        for i in lst:
            if i % 2:
                counter += 1
        return counter
    except:
        return 0


def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer: ')
            if user_input == '0' or len(user_input) and int(user_input):
                return int(user_input)
            raise ValueError
        except ValueError:
            print('It must be an integer')
            user_input = ''


while not 0 in result_list:
    result_list.append(get_user_input())


calculate(remove_zero_from_list(result_list))
