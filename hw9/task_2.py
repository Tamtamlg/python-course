import random
DICT_SIZE = 20


def generate_dict(size):
    new_dist = dict()
    for i in range(size):
        new_dist[f'element_{i}'] = random.randint(1, 3)
    return new_dist


def multiple(dct: dict):
    counter = 1
    for v in dct.values():
        counter = counter * v
    return counter


new_dict = generate_dict(DICT_SIZE)
print(new_dict)
print()
print(multiple(new_dict))
