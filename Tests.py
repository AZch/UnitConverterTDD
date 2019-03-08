import unittest
import string
import random
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
        self.assertEqual("m", converter.getNames()[0], "zero elem should be m")

    def nameGenerator(self, sizeName=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(sizeName))

    def testCheckName100_Random_emptyList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            name = self.nameGenerator()
            converter.addQuantities(name, [])
            self.assertEqual(i + 1, len(converter.getNames()), "count name should be " + str(i + 1))
            self.assertEqual(name, converter.getNames()[i], "zero elem should be m")

    def testNormalQuantAddOneQuantites_m_emptyList(self):
        converter = Converter()
        converter.addQuantities("m", [])

        self.assertEqual(1, len(converter.getQuantities()), "count quantities matrix shoud be 1")
        self.assertEqual(1, converter.getQuantities()[0][0], "shoud be 1")

    def testCheckQunat100_RandomName_randomList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            name = self.nameGenerator()
            converter.addQuantities(name, [random.randint(0, 100)] * (i + 1))
            self.assertEqual(i + 1, len(converter.getNames()), "count name should be " + str(i + 1))
            self.assertEqual(name, converter.getNames()[i], "zero elem should be m")

            self.assertEqual(i + 1, len(converter.getQuantities()), "count quant should be " + str(i + 1))

            for k in range(i + 1):
                self.assertEqual(i + 1, len(converter.getQuantities()[k]))

    def testMainDiadQuant100_EmptyName_randomList(self):
        converter = Converter()
        size = 100
        for i in range(size):
            listAdd = [random.randint(0, 100)] * (i)
            converter.addQuantities("", listAdd)

            self.assertEqual(1, converter.getQuantities()[i][i], "quant diag should be 1")

    def testElemRelativeDiag100_EmptyName_randomLit(self, size = 100):
        converter = Converter()
        for i in range(size):
            listAdd = [random.randint(0, size)] * (i)
            converter.addQuantities("", listAdd)

            for k in range(i + 1):
                for m in range(i + 1):
                    if (k < m):
                        if (converter.getQuantities()[k][m] != 0):
                            self.assertAlmostEqual(1, converter.getQuantities()[k][m] * converter.getQuantities()[m][k], msg="elem relative diag should be 1", delta=0.0000001)
                        else:
                            self.assertEqual(0, converter.getQuantities()[k][m] * converter.getQuantities()[m][k], msg="elem relative diag should be 0")