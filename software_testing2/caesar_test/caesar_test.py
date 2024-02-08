from software_testing2.caesar_Cipher.caesar_Cipher import caesarCipher
import unittest

class CaesarTest(unittest.TestCase):
    def test_caesar_num(self):
        text = 'AAAA'
        num_k = 5
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'FFFF')