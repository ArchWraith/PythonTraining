import unittest
import name

class TestSubtractMethod(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(name.subtract(3,1), 2)

    def test_add(self):
        self.assertEqual(name.add(3,1), 4)


if __name__ == '__main__':
    unittest.main()