NUMBER_LENGTH = 5


def get_number():
    num = 0
    while not num:
        try:
            num = int(input('Введіть п`ятизначне число:'))
            if len(str(num)) == NUMBER_LENGTH:
                return num
            raise Exception
        except:
            print('Має бути п`ятизначне число')


user_number = get_number()
num_of_units = user_number % 10
num_of_tens = user_number % 100 // 10
num_of_hundreds = user_number % 1000 // 100
num_of_thousands = user_number % 10000 // 1000
num_of_tens_of_thousands = user_number // 10000
num_of_3 = user_number // 3
num_of_6 = user_number // 6

print(
    'одиниці:', num_of_units, '\n',
    'десятки:', num_of_tens, '\n',
    'сотні:', num_of_hundreds, '\n',
    'тисячі:', num_of_thousands, '\n',
    'десятки тисяч:', num_of_tens_of_thousands, '\n',
    'трійок у числі:', num_of_3, '\n',
    'шісток у числі:', num_of_6
)
