from unittest import TestCase
from src.polynome import Polynome

class PolynomeInitializationTests(TestCase):

    def test_successed_initialization(self):

        Polynome([1, 2, 3]);
        Polynome([0]);
        Polynome([-0]);

    def test_failed_initialization(self):

        self.assertRaises(Exception, Polynome, [])
        self.assertRaises(Exception, Polynome, ['a', 'b', 1, '2'])
        self.assertRaises(Exception, Polynome, ['1.1.1.1'])
        self.assertRaises(Exception, Polynome, ['&$%#@1!'])