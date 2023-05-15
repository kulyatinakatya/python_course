import xml.etree.ElementTree as etree


def sentences(path):
    with open("sentences_file.txt", "w") as file:
        tree = etree.parse(path)
        root = tree.getroot()
        for tag in root.findall("text/paragraphs/paragraph/sentence/source"):
            file.write(tag.text + '\n')


def plural_nouns(path):
    with open("plural_nouns_file.txt", "w") as file:
        tree = etree.parse(path)
        root = tree.getroot()
        for token in root.iter('token'):
            grammems = []
            for g in token.iter('g'):
                grammems.append(g.attrib['v'])
                if ('NOUN' in grammems) and ('plur' in grammems):
                    file.write(token.attrib['text'] + '\n' + 'Начальная форма: ' + token.find('tfr/v/l').attrib['t'] + '\n'*2)
                    break


def ConjOrVerb(path):
    conj = 0
    verb = 0
    tree = etree.parse(path)
    root = tree.getroot()
    for token in root.iter('token'):
        if token.attrib['text'].lower() == 'может':
            grammems = []
            for g in token.iter('g'):
                grammems.append(g.attrib['v'])
            if 'CONJ' in grammems:
                conj += 1
            if 'VERB' in grammems:
                verb += 1
    print('Количество вхождений "может" в качестве союза: ', conj)
    print('Количество вхождений "может" в качестве глагола: ', verb)


sentences('annot.opcorpora.no_ambig.xml')
plural_nouns('annot.opcorpora.no_ambig.xml')
ConjOrVerb('annot.opcorpora.no_ambig.xml')
