import unittest
from tests_hand_checker import TestHandChecker
from tests_card import TestCard
from tests_deck import TestStandardDeck


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestHandChecker))
    _suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestCard))
    _suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestStandardDeck))
    return _suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
