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


def print_result(num):
    for i in range(num + 1):
        if 0 < i ** 2 <= num:
            print(i ** 2, end = " ")
    print()


number = get_user_input()
print_result(number)
