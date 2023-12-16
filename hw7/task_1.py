MONTH_PER_YEAR = 12


def get_user_input():
    user_input = ''
    while not user_input:
        try:
            user_input = input('Введіть суму кредиту: ')
            if len(user_input) and int(user_input):
                return int(user_input)
            raise ValueError
        except ValueError:
            print('Це має бути число > 0')
            user_input = ''


def get_rate(rate):
    return rate/100


def print_results(res):
    print(f'{"місяць":10} {"заборгованість":20} {"виплата":20} {"проценти":20} {"ставка,%":20}')
    for i in res:
        print(f'{i[0]:10} {i[1]:20} {i[2]:20} {i[3]:20} {i[4]:20}')


def calculate(amount: int, num_of_years: int):
    results = []
    interest_rate = 2
    num_of_month = num_of_years * MONTH_PER_YEAR
    remainder = amount
    month_payment_without_percents = amount/num_of_month

    for m in range(1, num_of_month + 1):
        if m > MONTH_PER_YEAR * 2:
            interest_rate = 4
        month_interest = remainder*get_rate(interest_rate)/MONTH_PER_YEAR
        month_payment = month_payment_without_percents + month_interest
        results.append((f'{m}', f'{remainder:.2f}',
                       f'{month_payment:.2f}', f'{month_interest:.2f}', f'{interest_rate}'))
        remainder = remainder - month_payment_without_percents
        num_of_month -= 1
    print_results(results)


amount = get_user_input()
calculate(amount, 1)
print('*' * 50)
calculate(amount, 5)
