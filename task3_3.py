import json
from collections import Counter


def phrases(list):
    count = Counter(list)
    return count.most_common(1)[0][0]


with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    dic = {}
    characters = []
    acts = data['acts']

    for line in acts:
        scene = line['scenes']
        for line in scene:
            action = line['action']
            for line in action:
                character = line['character']
                characters.append(character)

    print(phrases(characters))
