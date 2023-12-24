list_1 = ['a','b','c']
list_2 = [10, 20, 30]

def create_dict_from_two_lists(lst_1: list, lst_2: list):
    return dict(zip(lst_1, lst_2))

print(create_dict_from_two_lists(list_1, list_2))
