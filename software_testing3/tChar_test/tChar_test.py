from software_testing3.two_Char.two_Char import alternate 
import unittest

class CaesarTest(unittest.TestCase):
    def test_2_char(self):
        text = 'beabeefeab'
        result = alternate(text)
        self.assertEqual(result,5)