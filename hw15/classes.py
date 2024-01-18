import messages


class Triangle():

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_sides_as_list(self):
        return [self.__side_a, self.__side_b, self.__side_c]


class TriangleChecker(Triangle):

    def __is_numbers(self, sides):
        return all([isinstance(val, int) or isinstance(val, float) for val in sides])

    def __is_positive(self, sides):
        return all([float(val) > 0 for val in sides])

    def __is_triangel_possible(self, sides):
        return all([sum(sides) - val > val for val in sides])

    def is_triangle(self):
        sides = self.get_sides_as_list()
        if not self.__is_numbers(sides):
            print(messages.FAIL_NUMBERS_ONLY)
        elif not self.__is_positive(sides):
            print(messages.FAIL_POSITIVE_ONLY)
        elif not self.__is_triangel_possible(sides):
            print(messages.FAIL)
        else:
            print(messages.SUCCESS)


class ExtTriangle(TriangleChecker):
    pass
