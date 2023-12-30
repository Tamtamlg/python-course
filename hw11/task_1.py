side_x = [1, 2, 3, 4, 5, 6, 7]
side_y = [1, 2, 3, 4, 5, 6, 7]


def get_hypotenuse(*args):
    '''get hypotenuse by Pythagorean theorem'''
    print(list(map(lambda x, y=3: round(((x**2 + y**2) ** 0.5), 1), *args)))


if __name__ == '__main__':
    get_hypotenuse(side_x)
    get_hypotenuse(side_x, side_y)
