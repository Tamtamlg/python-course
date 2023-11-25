def print_to_console(first_val, second_val):
    print('first variable:', first_val, ', second variable:', second_val, '\n')


def change_variables_value_by_buffer(first_val, second_val):
    print_to_console(first_val, second_val)
    buffer = first_val
    first_val = second_val
    second_val = buffer
    print_to_console(first_val, second_val)


def change_variables_value_by_python_prop(first_val, second_val):
    print_to_console(first_val, second_val)
    first_val, second_val = second_val, first_val
    print_to_console(first_val, second_val)


def change_variables_value_by_math(first_val, second_val):
    print_to_console(first_val, second_val)
    first_val = first_val + second_val
    second_val = first_val - second_val
    first_val = first_val - second_val
    print_to_console(first_val, second_val)


change_variables_value_by_buffer(1, 2.99)

change_variables_value_by_python_prop(3, 4.88)

change_variables_value_by_math(5, 6.77)
