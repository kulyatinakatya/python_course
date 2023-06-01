import json
import unittest
import pymorphy3
from collections import Counter

from task14 import TF_IDF

PATH_TO_FOLDER = './texts'
FILES = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt']
TEXTS = [f'{PATH_TO_FOLDER}/{file}' for file in FILES]


class TF_IDFTest(unittest.TestCase):
    def setUp(self):
        self.object = TF_IDF(TEXTS)
        self.tf_idfs = self.object.count('./texts/5.txt')
        self.no_tf_idfs = self.object.count('./texts/6.txt')

        ma = pymorphy3.MorphAnalyzer()
        with open('./texts/5.txt', 'r', encoding='UTF-8') as f:
            text = f.read()
        for sym in '.,:;«»“”!?—"_()\n':
            text = text.replace(sym, ' ')
            words = [ma.parse(word)[0].normal_form for word in text.lower().split()]

        self.words_count = Counter(words)

        with open('idfs.json', 'r', encoding='UTF-8') as f:
            self.idfs = json.load(f)

    def test_texts_len(self):
        self.assertEqual(sum(self.words_count.values()), len(self.tf_idfs))

    def test_no_idfs_in_file(self):
        for word_tf_idf_equal in self.no_tf_idfs:
            with self.subTest(word_tfidf_equal=word_tf_idf_equal):
                self.assertFalse(word_tf_idf_equal[-1])

    def test_idfs_loading(self):
        for word in self.idfs:
            with self.subTest(word=word):
                self.assertEqual(self.idfs[word], self.object.get_idfs()[word])


if __name__ == '__main__':
    unittest.main()
