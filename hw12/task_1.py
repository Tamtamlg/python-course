import re


def password_decorator(fn):
    print('Enter min 8 characters, min 1 number, min 1 letter, min 1 special character:')

    def wrapper(*args, **kwargs):
        pattern = r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?[!@#$%^&*\(\)_+=\{\}\[\]]).{8,}"
        password = ''
        while not password:
            try:
                password = fn(*args, **kwargs)
                if password is None:
                    raise TypeError
                elif re.match(pattern, password):
                    print('the password is valid')
                    return password
                else:
                    raise ValueError
            except ValueError:
                print(
                    'min 8 characters, min 1 number, min 1 letter, min 1 special character')
                password = ''
            except TypeError:
                print('do not use space, tab and empty string, please')
                password = ''

    return wrapper


@password_decorator
def get_user_data():
    user_data = input()
    if len(user_data) == 0 or ' ' in user_data or '\t' in user_data:
        return None
    return user_data


if __name__ == '__main__':
    get_user_data()
