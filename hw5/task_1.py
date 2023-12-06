# test_list = [1,2,3,4,5,6,7,8,9]

# test_str = 'str'

def get_user_input():
    return input('Type a few characters:')


def handle_user_input(data):
    if data:
        new_data = multiple_string(data)
        return list(new_data)
    return ''


def reverse(lst):
    new_lst = lst[::-1]
    return new_lst


def get_last_elements(lst, num_of_last=5):
    return lst[-num_of_last::]


def get_even_idxs(lst):
    return lst[::2]


def multiple_string(string, length=15, times_to_multiple=2):
    while len(string) < length:
        string = string * times_to_multiple
    return string


def cut_start_end(lst, start=2, end=2):
    return lst[start:-end]


def show_results(data):
    print('initial list: ', data)
    print('reverse: ', reverse(data))
    print('last 5 elements: ', get_last_elements(data))
    print('even indexes: ', get_even_idxs(data))
    print('without 2 items from start and end: ', cut_start_end(data))


data = get_user_input()
lst = handle_user_input(data)
if lst:
    show_results(lst)
else:
    print('String is empty')
