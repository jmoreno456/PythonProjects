## unit testing in python is crucial
## write clean, testable code
## catch bugs before shipping
## work well in team environments and Cl pipelines


## unittest
## unit testing means writing tests for individual parts(units) of
## your code, usually functions or classes, to ensure they behave
## as expected


## basic example
# def add(a, b):
#  return a + b

# import unittest

# class TestMath(unittest.TestCase):

#  def test_add(self):
#     self.assertEqual(add(2, 3), 5)
#    self.assertEqual(add(-1, 1), 0)
#   self.assertEqual(add(0, 0), 0)

# if __name__ == "__main__":
#   unittest.main()

## unittest.TestCase: base class that provides assertion methods
## self.assertEqual(x, y): fails the test if x != y
## unittest.main(): runs the tests when the file is executed


## practice
## define a function multiply(a, b) that returns the product of
## two numbers
## create a unittest.testcase class to test multiply for:
## positive numbers, zero, negative numbers
# def multiply(a, b):
#  return a * b


# class TestMul(unittest.TestCase):

#  def test_mul(self):
#     self.assertEqual(multiply(2, 3), 6)
#    self.assertEqual(multiply(5, 0), 0)
#   self.assertEqual(multiply(8, -3), -24)


# if __name__ == "__main__":
#  unittest.main()


## bonus: write a function and test if a number is even
import unittest


def is_even(n):
    return n % 2 == 0


class TestEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(5))
        self.assertTrue(is_even(4))


if __name__ == "__main__":
    unittest.main()
## use self assert true when expecting true
## use self assert false when expecting false
