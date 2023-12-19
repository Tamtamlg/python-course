from utils import get_data_from_file


GAP = 5


def get_items_length(res: list, lst: list):
    for idx, item in enumerate(lst):
        if len(item) > res[idx]:
            res[idx] = len(item)
    return res


def set_gap(lst: list):
    for idx, _ in enumerate(lst):
        if idx:
            lst[idx] += GAP


def get_max_items_length(rows: list[str]):
    max_items_length = [0] * len(rows[0].split(','))
    for r in rows:
        row = r.split(',')
        max_items_length = get_items_length(max_items_length, row)
    set_gap(max_items_length)
    return max_items_length


def print_data_as_table(rows: list[str], max_items_length):
    for r in rows:
        row = r.split(',')
        result_str = ''
        for i, item in enumerate(row):
            result_str += f'{item.rjust(max_items_length[i])}'
        print(result_str)


data = get_data_from_file('data_2.csv')
rows = data.split('\n')
max_items_length = get_max_items_length(rows)
print_data_as_table(rows, max_items_length)
