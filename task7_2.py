import unittest
import random

numbers = []
n = random.randint(10, 50)
for i in range(n):
    numbers.append(random.random())
print(numbers)


class NumbersTest(unittest.TestCase):

    def test_compare(self):
        for i in range(len(numbers)):
            with self.subTest(i=i):
                self.assertGreaterEqual(numbers[i], 0.5)


if __name__ == '__main__':
    unittest.main()
