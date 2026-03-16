import unittest
from unit_math_tools import add


class TestMathTools(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 2), 5)


if __name__ == "__main__":
    unittest.main()
