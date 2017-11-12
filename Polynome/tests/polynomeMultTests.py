from unittest import TestCase
from src.polynome import Polynome

class PolynomesMultTests(TestCase):

    def test_mult_polynom_by_number(self):
        polynom = Polynome([1, 3, 4, 0]) * -1

        self.assertEqual("- x^3 - 3x^2 - 4x", polynom.ToString())

    def test_right_mult_polynom_by_number(self):
        polynom = -1 * Polynome([1, 3, 4, 0])

        self.assertEqual("- x^3 - 3x^2 - 4x", polynom.ToString())

    def test_mult_polynoms1(self):
        a = Polynome([1, 2])
        b = Polynome([2, 1])
        c = a * b

        self.assertEqual("2x^2 + 5x + 2", c.ToString())

    def test_mult_polynoms2(self):
        a = Polynome([4, 0, -3, -1])
        b = Polynome([2, -1, 1, 0])
        c = a * b

        self.assertEqual("8x^6 - 4x^5 - 2x^4 + x^3 - 2x^2 - x", c.ToString())
