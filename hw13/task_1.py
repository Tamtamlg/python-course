def get_user_input():
    user_input = input()
    if len(user_input) or user_input == '':
        return user_input


def write_to_file(string):
    with open('test.txt', 'w') as file:
        file.write(string)


def main():
    result_list = []

    while '' not in result_list:
        result_list.append(get_user_input())

    result_strng = '\n'.join(list(filter(None, result_list)))

    write_to_file(result_strng)


if __name__ == '__main__':
    main()
