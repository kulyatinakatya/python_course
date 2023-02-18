import json

with open('jul1.json', 'w') as outfile:

        with open('RomeoAndJuliet.json', 'r') as f:
            data = json.load(f)
        dic = {}
        characters = []
        acts = data['acts']

        for line in acts:
            scene = line['scenes']
            for line in scene:
                title = line['title']

                for line in scene:
                    action = line['action']
                    for line in action:
                        character = line['character']
                        if character not in characters:
                            characters.append(character)
                dic[title] = characters

        json_object = json.dumps(dic, indent=4)
        outfile.write(json_object)
