def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer: ')
            if len(user_input) and int(user_input):
                return int(user_input)
            raise ValueError
        except ValueError:
            print('It must be an integer')
            user_input = ''


def is_anthropomorphous(number):
    result = number * number
    return result % 10 ** len(str(number)) == number


def check_number(number):
    for i in range(1, number):
        if is_anthropomorphous(i):
            print(f'{i} * {i} = {i * i}')


checked_number = get_user_input()
check_number(checked_number)
