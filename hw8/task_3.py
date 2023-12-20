from utils import get_data_from_file_as_string


GAP = 10


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


def get_ship_mode_set(rows: list[str]):
    ship_mode_set = set()
    for idx, r in enumerate(rows):
        row = r.split(',')
        if idx:
            ship_mode_set.add(row[index_ship_mode])
    return ship_mode_set


def sort_by_key(rows: list[str]):
    lst = []
    for i in ship_mode_set:
        temp = []
        for j in rows:
            if j.split(',')[index_ship_mode] == i:
                temp.append(j)
        lst.append(temp)
    return lst


def print_data_as_table(rows: list[str], max_items_length):
    sum = calc_sum(rows)
    total = add_sum_to_table(f'Total: {sum}')
    rows.append(total)
    for r in rows:
        row = r.split(',')
        result_str = ''
        for i, item in enumerate(row):
            result_str += f'{item.rjust(max_items_length[i])}'
        print(result_str)


def print_header(header: list[str], max_items_length):
    result_str = ''
    for i, item in enumerate(header):
        result_str += f'{item.rjust(max_items_length[i])}'
    print(result_str)


def calc_sum(row: list[str]):
    counter = 0
    for _, item in enumerate(row):
        sales = float(item.split(',')[index_sales])
        counter += sales
    return round(counter, 2)


def add_sum_to_table(sum):
    row = []
    for i in range(index_sales + 1):
        if i == index_sales:
            row.append(str(sum))
        else:
            row.append(' ')
    return ','.join(row)


data = get_data_from_file_as_string('data_3.csv')
rows = data.split('\n')
max_items_length = get_max_items_length(rows)
header = rows[0].split(',')
index_ship_mode = header.index('ship_mode')
index_sales = header.index('sales')
ship_mode_set = get_ship_mode_set(rows)
sorted_list = sort_by_key(rows)

for row in sorted_list:
    print_header(header, max_items_length)
    print_data_as_table(row, max_items_length)
    print()
