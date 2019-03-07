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
        self.assertIsInstance(converter.getNames(), list, "name shoud have type list")

    def testQuantitiesNotNone(self):
        converter = Converter()
        self.assertIsNotNone(converter.getQuantities(), 'quantities cant be None')

    def testQuantitesIsArr(self):
        converter = Converter()
        self.assertIsInstance(converter.getQuantities(), list, "quantities shoud have type list")

    def testAddOneQuantites_m_emptyList(self):
        converter = Converter()
        converter.addQuantities("m", [])

        self.assertEqual(1, len(converter.getNames()), "count name should be 1")