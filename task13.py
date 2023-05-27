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

    def get_words(self):
        return self._words


class Corpus:

    def __init__(self, path_to_file):
        self.tree = etree.parse(path_to_file)
        self._sentences = []

    def load(self):
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

    def get_sentences(self):
        return self._sentences
