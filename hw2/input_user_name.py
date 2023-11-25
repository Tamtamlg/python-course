MAX_AGE = 100


def get_user_data(str):
    user_data = None
    while not user_data:
        try:
            user_data = input(str)
            if len(user_data):
                return user_data
            raise Exception
        except:
            print('Це поле не може бути пустим')


def get_user_age():
    age = None
    while not age:
        try:
            age = int(input('Введіть ваш вік: '))
            return age
        except:
            print('Вік має бути цілим числом, спробуйте ще раз')


def calculate_remainder_up_100(age, max_age):
    return max_age - age


def print_result(name, surname, remainder_up_100):
    print('\n')
    print('Привіт,', surname)
    print(name, '- це гарне ім`я, мені подобається')
    print('до 100 років тобі залишилося жити', remainder_up_100, 'років')


user_name = get_user_data('Введіть ваше ім`я: ')
user_surname = get_user_data('Введіть ваше прізвище: ')
user_age = get_user_age()
user_remainder_up_100 = calculate_remainder_up_100(user_age, MAX_AGE)
print_result(user_name, user_surname, user_remainder_up_100)
