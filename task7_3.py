import os
import unittest
import shutil

text = "This is a file for task 7_3"


def func(path):
    os.makedirs(path, exist_ok=True)
    with open('TestFile.txt', 'w') as f:
        f.write(text)


class Test(unittest.TestCase):

    def setUp(self):
        func('/Users/Katya/PycharmProjects/python_course/new_folder')

    def testmethod(self):
        with open('TestFile.txt', 'r') as f:
            self.assertFalse(os.stat('TestFile.txt').st_size == 0)
            self.assertTrue(text == f.read())

    def tearDown(self):
        shutil.rmtree('/Users/Katya/PycharmProjects/python_course/new_folder')


if __name__ == '__main__':
    unittest.main()
