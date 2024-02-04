from software_testing1.alternating.alternating import alternating_Characters
import unittest

class Alter(unittest.TestCase):
    def alter_AAAA(self):
        text = 'AAAA'
        num_of_alter_char = alternating_Characters(text)
        self.assertIs(num_of_alter_char,3)
    
    def alter_focus(self):
        text = 'focus'
        num_of_alter_char = alternating_Characters(text)
        self.assertIs(num_of_alter_char,3)