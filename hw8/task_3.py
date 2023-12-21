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
    max_items_length = [0] * len(rows[0])
    for r in rows:
        max_items_length = get_items_length(max_items_length, r)
    set_gap(max_items_length)
    return max_items_length


def get_ship_mode_set(rows: list[str]):
    ship_mode_set = []
    for idx, r in enumerate(rows):
        row = r.split(',')
        if idx and not row[index_ship_mode] in ship_mode_set:
            ship_mode_set.append(row[index_ship_mode])
    return ship_mode_set


def sort_by_key(rows: list[str], ship_mode_set: set):
    lst = []
    for i in ship_mode_set:
        temp = []
        for j in rows:
            if j.split(',')[index_ship_mode] == i:
                temp.append(j)
        lst.append(temp)
    return lst


def print_data_as_table(rows: list[str], max_items_length):
    for r in rows:
        result_str = ''
        for i, item in enumerate(r):
            result_str += f'{item.rjust(max_items_length[i])}'
        print(result_str)



def calc_sum(row: list[str]):
    counter = 0
    for _, item in enumerate(row):
        sales = float(item.split(',')[index_sales])
        counter += sales
    return round(counter, 2)


def generate_total_table(rows: list[str], ship_mode_set: set):
    total = [[],[]]
    for j in rows:
        sum = calc_sum(j)
        for idx, i in enumerate(ship_mode_set):
            key = j[idx].split(',')[index_ship_mode]
            if key == i:
                total[0].append(key)
                total[1].append(str(sum))
    return total


data = get_data_from_file_as_string('data_3.csv')
rows = data.split('\n')
header = rows[0].split(',')
index_ship_mode = header.index('ship_mode')
index_sales = header.index('sales')
ship_mode_set = get_ship_mode_set(rows)
sorted_list = sort_by_key(rows, ship_mode_set)
total = generate_total_table(sorted_list, ship_mode_set)
max_items_length = get_max_items_length(total)
print_data_as_table(total, max_items_length)
