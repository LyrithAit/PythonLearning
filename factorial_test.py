#!/usr/bin/env python3
import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):

    def test_fact(self):
        res = fact(5)
        self.assertEqual(res, 120)


if __name__ == '__main__':
    unittest.main()