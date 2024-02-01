from funny_string.funny_string import funnyString
import unittest

class PrimeListTest(unittest.TestCase):
    def funnyString(self):
        text = 'acxz'
        emotion = funnyString(text)
        self.assertls(emotion,"Funny")
    
    def funnyString_bcxz(self):
        text = 'bcxz'
        emotion = funnyString(text)
        self.assertls(emotion,"Funny")