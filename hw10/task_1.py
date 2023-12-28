TEST_LIST_1 = [5, 4, 3, 2, 1]
TEST_LIST_2 = [10, 20, 30]
SUM_1 = 2
SUM_2 = 40


def find_sum_in_list(list_of_num: list, result: int):
    '''find sum of each 2 elements in list end compare with result'''
    for i in range(len(list_of_num)):
        for j in range(i + 1, len(list_of_num)):
            if list_of_num[i] + list_of_num[j] == result:
                return True
    return False


if __name__ == '__main__':
    print(find_sum_in_list(TEST_LIST_1, SUM_1))
    print(find_sum_in_list(TEST_LIST_2, SUM_2))
