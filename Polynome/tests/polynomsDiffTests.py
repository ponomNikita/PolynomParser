from unittest import TestCase
from src.polynome import Polynome


class PolynomesDiffTests(TestCase):
    def test_polynoms_diff_when_fisrt_lenght_bigger1(self):
        a = Polynome([1, 2])
        b = Polynome([2])
        c = a - b
        self.assertEqual("x", c.ToString())

    def test_polynoms_diff_when_fisrt_lenght_bigger2(self):
        a = Polynome([4, 3, 4, 5, 0])
        b = Polynome([-2, -0.0001])
        c = a - b
        self.assertEqual("4x^4 + 3x^3 + 4x^2 + 7x + 0.0001", c.ToString())

    def test_polynoms_diff_when_lenghts_are_equal1(self):
        a = Polynome([1, 2])
        b = Polynome([-1, -2])
        c = a - b
        self.assertEqual("2x + 4", c.ToString())

    def test_polynoms_diff_when_lenghts_are_equal2(self):
        a = Polynome([3, 6, 2])
        b = Polynome([-1, -2, -2])
        c = a - b
        self.assertEqual("4x^2 + 8x + 4", c.ToString())

    def test_polynoms_diff_when_second_lenght_bigger1(self):
        a = Polynome([1, 2])
        b = Polynome([2])
        c = b - a
        self.assertEqual("- x", c.ToString())

    def test_polynoms_diff_when_second_lenght_bigger2(self):
        a = Polynome([4, 3, 4, 5, 0])
        b = Polynome([-2, -0.0001])
        c = b - a
        self.assertEqual("- 4x^4 - 3x^3 - 4x^2 - 7x - 0.0001", c.ToString())
