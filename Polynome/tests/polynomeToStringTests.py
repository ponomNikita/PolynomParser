from unittest import TestCase
from src.polynome import Polynome

class PolynomeToStringTests(TestCase):

    def test_toString_when_three_cooefs(self):
        polynom = Polynome([1, 2, 3])

        self.assertEqual("x^2 + 2x + 3", polynom.ToString())

    def test_toString_when_one_cooef_is_zero(self):
        polynom = Polynome([2, 0, -1])

        self.assertEqual("2x^2 - 1", polynom.ToString())

    def test_toString_when_only_one_cooef_2(self):
        polynom = Polynome([2])

        self.assertEqual("2", polynom.ToString())

    def test_toString_when_only_one_cooef_1(self):
        polynom = Polynome([1])

        self.assertEqual("1", polynom.ToString())

    def test_toString_when_only_one_cooef_0(self):
        polynom = Polynome([0])

        self.assertEqual("0", polynom.ToString())

    def test_toString_when_cooefs_end_with_1(self):
        polynom = Polynome([2, 3, 1])

        self.assertEqual("2x^2 + 3x + 1", polynom.ToString())

    def test_toString_when_first_cooef_is_zero(self):
        polynom = Polynome([0, 3, 1])

        self.assertEqual("3x + 1", polynom.ToString())

    def test_toString_when_first_and_last_cooefs_are_zero(self):
        polynom = Polynome([0, 3, 0])

        self.assertEqual("3x", polynom.ToString())

    def test_toString_when_last_cooef_is_zero(self):
        polynom = Polynome([-4, 3, 0])

        self.assertEqual("- 4x^2 + 3x", polynom.ToString())

    def test_toString_when_all_cooefs_are_zero(self):
        polynom = Polynome([0, -0, 0])

        self.assertEqual("0", polynom.ToString())

    def test_toString_when_cooefs_with_floating_points(self):
        polynom = Polynome([0.102, -1.1, -4.5000, 0.00120])

        self.assertEqual("0.102x^3 - 1.1x^2 - 4.5x + 0.0012", polynom.ToString())