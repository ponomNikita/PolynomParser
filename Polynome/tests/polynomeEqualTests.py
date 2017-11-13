from unittest import TestCase
from src.polynome import Polynome


class PolynomesEqualityTests(TestCase):

    def test_polynomeA_equals_polynomeB(self):
        a = Polynome([1, 2, 3, 4])
        b = Polynome([1, 2, 3, 4])

        self.assertTrue(a == b)

    def test_polynomeA_not_equal_polynomeB_when_they_have_different_length(self):
        a = Polynome([1, 2])
        b = Polynome([1])

        self.assertTrue(a != b)

    def test_polynomeA_not_equal_polynomeB_when_they_have_same_length(self):
        a = Polynome([1, 2])
        b = Polynome([1, 3])

        self.assertTrue(a != b)

    def test_polynomeA_not_equal_to_character(self):
        a = Polynome([1, 2])

        self.assertTrue(a != "b")

    def test_polynomeA_not_equal_to_character2(self):
        a = Polynome([1, 2])

        self.assertFalse(a == "b")

    def test_polynomeA_not_equal_to_number(self):
        a = Polynome([1, 2])

        self.assertTrue(a != 2)

    def test_polynomeA_not_equal_to_list(self):
        a = Polynome([1, 2])

        self.assertTrue(a != [1, 2])
