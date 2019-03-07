import unittest
from Converter import Converter

class TestMainConvert(unittest.TestCase):
    def testConverterNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter, "converter cant be None")

    def testCheckNamesNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter.getNames(), "names cant be None")

    def testNamesIsArr(self):
        converter = Converter()
        self.assertIsInstance(converter.getNames(), list, "name shoud be type list")