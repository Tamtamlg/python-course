from text import text


def remove_punctuation(string: str):
    return string.replace('\n', ' ').replace(',', '').replace('.', '').replace('…', '')


def create_word_set(string: str):
    word_set = set()
    for i in string:
        word_set.add(i)
    return word_set


def generate_dict(keys: set, lst: list):
    return {k: lst.count(k) for k in keys}


def print_result(val):
    print(f'The word(s) occurs {val} time(s) in the text: ', ', '.join(
    [i for i in dct if dct[i] == val]))
    print()

text_without_punctuation = remove_punctuation(text)
list_from_text = text_without_punctuation.lower().split(' ')
word_set = create_word_set(list_from_text)
dct = generate_dict(word_set, list_from_text)
max_value = max(dct.values())
min_value = min(dct.values())

print_result(max_value)
print_result(min_value)
