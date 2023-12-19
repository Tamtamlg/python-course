from utils import get_data_from_file


data = get_data_from_file('data_3.csv')
rows = data.split('\n')
header = rows[0].split(',')
index = header.index('ship_mode')


def get_ship_mode_set(rows: list[str]):
    ship_mode_set = set()
    for idx, r in enumerate(rows):
        row = r.split(',')
        if idx:
            ship_mode_set.add(row[index])
    return ship_mode_set

ship_mode_set = get_ship_mode_set(rows)

def sort_by_key(rows):
    lst = []
    for i in ship_mode_set:
        temp = []
        for j in rows:
            if j.split(',')[index] == i:
                temp.append(j)
        lst.append(temp)
    return lst

sorted_list = sort_by_key(rows)


def calc_sum(lst):
    pass

print(sorted_list[0])
print()
print(sorted_list[1])
print()
print(sorted_list[2])
