import json

with open('wiki1.json', 'w') as f:
    data = [json.loads(line) for line in open('wikidata_1000.json', 'r')]
    dic = {}
    for line in data:
        word = line['label']['value']
        try:
            defin = line['description']['value']
        except KeyError:
            defin = None
        dic[word] = defin
    json.dump(dic, f, ensure_ascii=False, indent=4)
