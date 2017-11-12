from unittest import TestCase
from src.polynome import Polynome

class PolynomeToStringTests(TestCase):

    def test_toString_when_three_cooefs(self):
        polynom = Polynome([1, 2, 3])

        self.assertEqual("x^2 + 2x + 3", polynom.ToString())

    def test_toString_when_one_cooef_is_zero(self):
        polynom = Polynome([2, 0, -1])

        self.assertEqual("2x^2 - 1", polynom.ToString())