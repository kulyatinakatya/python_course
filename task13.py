import xml.etree.ElementTree as etree


class Wordform:
    def __init__(self, word_str, list_gr):
        self._word = word_str
        self._gram = list_gr

    def get_gr(self, i):
        return self._gram[i]

    def get_str_word(self):
        return self._word


class Sentence:
    def __init__(self, sent_str, words):
        self._sent = sent_str
        self._words = words

    def get_word(self, i):
        return self._words[i]

    def get_str_sent(self):
        return self._sent


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self, path_to_file):
        self.tree = etree.parse(path_to_file)
        root = self.tree.getroot()
        for sent in root.findall("text/paragraphs/paragraph/sentence"):
            words = []
            sent_str = sent.find('source').text
            for token in sent.find('tokens'):
                token_str = token.attrib['text']
                token_gr = []
                for gr in token.findall('tfr/v/l/g'):
                    token_gr.append(gr.attrib['v'])
                word = Wordform(token_str, token_gr)
                words.append(word)
            sentence = Sentence(sent_str, words)
            self._sentences.append(sentence)


a = Corpus()
a.load("annot.opcorpora.no_ambig.xml")


print(a._sentences[10].get_str_sent()) #выдаёт 11-ое предложение
print(a._sentences[10]._words[0].get_str_word()) #выдаёт 1-ое слово в 11-ом предложении
print(a._sentences[10]._words[0].get_gr(0)) #выдаёт 1-ую граммему 1-ого слова в 11-ом предложении