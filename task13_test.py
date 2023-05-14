from task13 import *
import unittest
import xml.etree.ElementTree as etree


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.test_corp = Corpus()
        self.test_corp.load("annot.opcorpora.no_ambig.xml")

    def test_instances(self): #тест, проверяющий, что все предложения являются объектами класса Sentence, а все слова – Wordform
        for sentence in self.test_corp._sentences:
            with self.subTest(sentence=sentence):
                self.assertTrue(isinstance(sentence, Sentence))

            for word in sentence._words:
                with self.subTest(word=word):
                    self.assertTrue(isinstance(word, Wordform))

    def test_gram(self): #тест, проверяющий, что для всех слов поставлены в соответствие верные граммемы
        tree = etree.parse("annot.opcorpora.no_ambig.xml")
        root = tree.getroot()
        for token, word in zip(root.find("text/paragraphs/paragraph/sentence/tokens"),
                               self.test_corp._sentences[0]._words):
            with self.subTest(token=token, word=word):
                grams = [gram.attrib['v'] for gram in token.findall('tfr/v/l/g')]
                test_grams = word._gram
                self.assertEqual(test_grams, grams)


if __name__ == '__main__':
    unittest.main()
