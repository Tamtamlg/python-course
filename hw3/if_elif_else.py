def get_year():
    year = None
    while not year:
        try:
            year = int(input('Enter a year from 1900 to 1_000_000:'))
            if str(year):
                return year
            raise ValueError
        except ValueError:
            print('The year must be an integer')


def is_leap_year(year):
    if not year % 400:
        return True
    elif not year % 100:
        return False
    elif not year % 4:
        return True
    else:
        return False


def check_year(year):
    if 1900 < year < 1_000_000:
        if is_leap_year(year):
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print('The year must be between 1900 and 1_000_000')


checked_year = get_year()
check_year(checked_year)
