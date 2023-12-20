import csv
import os


def get_data_from_file_as_string(filename: str):
    rows = ''
    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, filename), 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            row_to_str = str(row)
            rows += row_to_str
    rows = rows.replace('][', '\n').replace('[', '').replace(
        ']', '').replace(', ', ',').replace("'", '').replace('"', '')
    return rows
