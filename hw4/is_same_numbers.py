def get_number():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer:')
            if len(user_input) and int(user_input):
                return user_input
            raise ValueError
        except ValueError:
            print('It must be an integer')
            user_input = ''


def find_same_numbers_by_loop(str):
    new_list = []
    for i in list(str):
        if i in new_list:
            return True
        else:
            new_list.append(i)
    return False


str_with_numbers = get_number()
print('It has duplicates:', find_same_numbers_by_loop(str_with_numbers))
