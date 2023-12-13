def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer: ')
            if len(user_input) and int(user_input):
                return int(user_input)
            raise ValueError
        except ValueError:
            print('It must be an integer > 0')
            user_input = ''


def print_data(digit):
    for i in range(digit):
        digit_length = len(str(digit))
        temp_num = str(i).rjust(digit_length)
        temp_str = '1' + '0' * i
        print(temp_num + ' ' + temp_str.rjust(digit))


digit = get_user_input()
print_data(digit)
