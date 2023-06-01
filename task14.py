import os
import math
import json
import pymorphy3
from collections import Counter


class TF_IDF:
    def __init__(self, files: list):
        self._texts = []
        self._idfs = {}

        for file in files:
            self._add_text(file)

        if os.path.exists('idfs.json'):
            with open('idfs.json', 'r', encoding='UTF-8') as f:
                self._idfs = json.load(f)
        else:
            for text in self._texts:
                self._count_idfs(text)

    def _add_text(self, file):
        self._texts.append(Counter(self._normalize(file)))

    def _normalize(self, file):
        ma = pymorphy3.MorphAnalyzer()
        with open(file, 'r', encoding='UTF-8') as f:
            text = f.read()

        for sym in '.,:;«»“”!?—"_()\n':
            text = text.replace(sym, ' ')
            words = [ma.parse(word)[0].normal_form for word in text.lower().split()]
        return words

    def _count_idfs(self, text):
        for word in text:
            numi = 0
            for text in self._texts:
                numi += (1 if word in text else 0)
            self._idfs[word] = math.log(abs(len(self._texts)) / abs(di))

        with open('idfs.json', 'w', encoding='UTF-8') as f:
            json.dump(self._idfs, f, ensure_ascii=False, indent=4)

    def get_texts(self):
        return self._texts

    def get_idfs(self):
        return self._idfs

    def count(self, file):
        words = self._normalize(file)
        words_count = Counter(words)

        tf_idfs = []
        for word in words:
            idf = self._idfs.get(word, 0)
            tf_idfs.append((word, (words_count[word] / len(words)) * idf))
        return tf_idfs