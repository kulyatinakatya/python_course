import json

with open('task3_2.json', 'w') as fout:
    with open('RomeoAndJuliet.json', 'r') as f:
        data = json.load(f)
        characters = []
        dic = {}

        for acts in data['acts']:
            for scenes in acts['scenes']:
                title = scenes['title']
                for action in scenes['action']:
                    for character in action:
                        if action['character'] not in characters:
                            characters.append(action['character'])
                key = title
                dic[key] = characters
                json_object = json.dumps(dic)
                fout.write(json_object)
                fout.write("\n")
                characters = []
                dic = {}
