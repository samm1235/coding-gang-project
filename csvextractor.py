import csv

data_dict = []

def clean_dict():
    with open('library.csv', newline = '', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter = ',')
        for row in reader:
            data_dict.append(dict(row))
    return data_dict

print(clean_dict())