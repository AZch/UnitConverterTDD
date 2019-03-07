import unittest
from Converter import Converter

class TestMainConvert(unittest.TestCase):
    def testConverterNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter, "converter cant be None")

    def testCheckQuantitiesNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter.getNames(), "names cant be None")