RANGE_START = 1
RANGE_END = 10


def generate_dict(start, end):
    return {k:k**3 for k in range(start, end + 1)}


print(generate_dict(RANGE_START, RANGE_END))
