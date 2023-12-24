data = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'


def remove_spaces(string: str):
    return string.replace(' ','')


def get_char_set(string: str):
    char_set = set()
    for i in string:
        char_set.add(i)
    return char_set


def generate_dict(keys: set, string: str):
    return {k: string.count(k) for k in keys}


data_without_spaces = remove_spaces(data).lower()
char_set = get_char_set(data_without_spaces)
print(generate_dict(char_set, data_without_spaces))
