import os
import unittest
import shutil

text = "This is a file for task 7_3"


def func(path):
    os.makedirs(path, exist_ok=True)
    new_file = open("TestFile.txt", "w")
    new_file.write(text)
    new_file.close()


class Test(unittest.TestCase):

    def setUp(self):
        func('/Users/Katya/PycharmProjects/python_course/new_folder')

    def testmethod(self):
        new_file = open("TestFile.txt", "r")
        self.assertFalse(os.stat('TestFile.txt').st_size == 0)
        self.assertTrue(text == new_file.read())
        new_file.close()

    def tearDown(self):
        shutil.rmtree('/Users/Katya/PycharmProjects/python_course/new_folder')


if __name__ == '__main__':
    unittest.main()
