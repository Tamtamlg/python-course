RANGE_FROM = 3
RANGE_TO = 9


def get_user_input():
    try:
        user_input = input(f'Enter an integer from {RANGE_FROM} to {RANGE_TO}: ')
        if len(user_input) and int(user_input) in range(RANGE_FROM, RANGE_TO + 1):
            return int(user_input)
        raise ValueError
    except ValueError:
        return False


def print_left(data):
    counter = 1
    string = ''
    while counter <= data:
        print(string + str(counter) + string[::-1])
        string = string + str(counter)
        counter += 1


def get_center(data):
    return data * 2 - 1


def print_center(data):
    counter = 1
    string = ''
    center = get_center(data)
    while counter <= data:
        temp = string + str(counter) + string[::-1]
        print(temp.center(center))
        string = string + str(counter)
        counter += 1


def print_right(data):
    counter = 1
    string = ''
    center = get_center(data)
    while counter <= data:
        temp = string + str(counter) + string[::-1]
        print(temp.rjust(center))
        string = string + str(counter)
        counter += 1


data = get_user_input()
if data:
    print_left(data)
    print_right(data)
    print_center(data)
else:
    print(f'It must be an integer from {RANGE_FROM} to {RANGE_TO}')
