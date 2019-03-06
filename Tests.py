import unittest

class TestMainConvert(unittest.TestCase):
    def testMakeConverter(self):
        converter = Converter()
        self.assertIsNotNone(converter, "converter cant be None")