import unittest
import random


def division(a, b):

    c = a / b
    return c


a = random.randint(1, 10)
b = random.randint(1, 10)


def new(arr):
    for i in range(random.randint(1, 10)):
        arr.append(random.randint(1, 10))
    arr.append(5)
    return(arr)


arr = []


def transform(array_1):
    return (array_1)


array_1 = []
for j in range(5):
    array_1.append(random.randint(1, 10))


class TestMethods(unittest.TestCase):

    def test_division(self):
        self.assertTrue(division(a, b) <= a)
        self.assertFalse(division(a, b) > a)

    def test_new(self):
        self.assertIn(5, new(arr))
        self.assertNotIn(0, new(arr))

    def test_greater(self):
        self.assertGreater(a, division(a, b))

    def test_less(self):
        self.assertLess(division(a, b), a)

    def test_equal(self):
        self.assertCountEqual(array_1, transform(array_1))


if __name__ == '__main__':
    unittest.main()

