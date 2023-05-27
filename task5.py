import csv
import json
from collections import Counter, defaultdict, OrderedDict


def def_value():
    return []


def split_to_words(filepath: str):
    results = []

    def _get_says(a_dict):
        try:
            results.append(a_dict['says'])
        except KeyError:
            pass
        return a_dict

    f = open(filepath, 'r')
    json.loads(f.read(), object_hook=_get_says)

    sentences = []
    for item in results:
        sentences += item

    words = []
    for sent in sentences:
        sent = sent.lower()
        punctuations = '@#!?+&*[]-%.:/();$=><|{}^,' + "'`" + '_'
        for p in punctuations:
            sent = sent.replace(p, '')
        words += sent.split()
    return words


def split_to_characters_and_says(filepath):
    results = defaultdict(def_value)

    def _get_chars_and_says(a_dict):
        try:
            for dialog in a_dict['action']:
                results[dialog["character"]] += dialog['says']
        except KeyError:
            pass
        return a_dict

    f = open(filepath, 'r')
    json.loads(f.read(), object_hook=_get_chars_and_says)

    return results


def split_to_characters(filepath):
    results = []

    def _get_chars(a_dict):
        try:
            results.append(a_dict['character'])
        except KeyError:
            pass
        return a_dict

    f = open(filepath, 'r')
    json.loads(f.read(), object_hook=_get_chars)

    return results


def first_task(filepath):
    words = split_to_words(filepath)
    cnt = Counter(words)
    sorted_cnt = sorted(dict(cnt).items(), key=lambda x: x[1], reverse=True)

    print('20 самых частых слов')
    for item in sorted_cnt[:20]:
        print(item[0], item[1])

    print('\n', '20 самых редких слов')
    for item in sorted_cnt[-20:]:
        print(item[0], item[1])


def second_task(filepath):
    with open('task5_2.json', 'w') as f:
        f.write(json.dumps(split_to_characters_and_says(filepath), indent=4))


def third_task(filepath):
    cnt = Counter(split_to_characters(filepath))
    sorted_cnt = sorted(dict(cnt).items(), key=lambda x: x[1], reverse=True)

    for character in sorted_cnt:
        print(character[0], character[1])


def fourth_task(filepath):
    path_to_new_file = 'fourth_task.csv'
    natural_order = 'natural_order_'
    reversed_order = 'reversed_order_'

    with open(filepath) as fd:
        data = [row for row in csv.DictReader(fd)]
        data.sort(key=lambda x: float(x['Price']))

        with open(natural_order + path_to_new_file, 'w') as wfile:
            writer = csv.writer(wfile)
            writer.writerow(['Id', 'Images', 'Title', 'Description', 'Price'])
            for dict in data:
                writer.writerow(dict.values())

        with open(reversed_order + path_to_new_file, 'w') as wfile:
            data = data[::-1]
            writer = csv.writer(wfile)
            writer.writerow(['Id', 'Images', 'Title', 'Description', 'Price'])
            for dict in data:
                writer.writerow(dict.values())


json_file = 'RomeoAndJuliet.json'
csv_file = 'stage3_test.csv'
#first_task(json_file)
#second_task(json_file)
#third_task(json_file)
fourth_task(csv_file)

