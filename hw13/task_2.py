import os


def get_text_as_list_from_file(filename):
    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, filename), 'r', encoding='UTF-8') as f:
        text_as_list = f.read().replace(' ', '\n').split('\n')
    return text_as_list


def get_max_length(lst: list[str]):
    lengths = [len(word) for word in lst]
    return max(lengths)


def longest_words(filename):
    results = []

    words = get_text_as_list_from_file(filename)

    max_length = get_max_length(words)

    for i in words:
        if len(i) == max_length:
            results.append(i)

    print(', '.join(results))


if __name__ == '__main__':
    longest_words('article.txt')
