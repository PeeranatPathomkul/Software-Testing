from software_testing1.alternating.alternating import alternatingCharacters
import unittest

class Alter(unittest.TestCase):
    def alter_AAAA(self):
        text = 'AAAA'
        num_of_alter_char = alternatingCharacters(text)
        self.assertEqual(num_of_alter_char,3)