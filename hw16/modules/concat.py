'''
This module contains functions for working with a users input
'''
def sum_or_concat():
    '''
    return sum or concat depends on velue type
    '''
    values = []
    while len(values) < 2:
        user_input = input('Enter a value: ')
        values.append(user_input)

    try:
        return sum(int(i) for i in values)
    except ValueError:
        result = ''
        for i in values:
            result += str(i)
        return result
