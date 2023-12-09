def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Enter an integer: ')
            if len(user_input) and int(user_input):
                return user_input
            raise ValueError
        except ValueError:
            print('It must be an integer')
            user_input = ''


def generate_list(number):
    lst = []
    for i in range(int(number)):
        if i % 2:
            lst.append(i)
    return lst


number = get_user_input()
lst = generate_list(number)
print(lst[::-1])
