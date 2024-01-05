START = 5
END = 50


def is_prime_number(num: int):
    flag = False
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                flag = False
                break
        else:
            flag = True
    else:
        flag = False
    return flag


def generate_prime_numbers(start: int, end: int):
    for i in range(start, end + 1):
        if is_prime_number(i):
            yield i


if __name__ == '__main__':

    for i in generate_prime_numbers(START, END):
        print(i, end=' ')
    print()
