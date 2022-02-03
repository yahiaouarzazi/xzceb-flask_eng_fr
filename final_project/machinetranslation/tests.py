import unittest

from translator import english_to_french, french_to_english

class TestMyfunctions(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), "Null input")
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), "Null input")
if __name__=='__main__':
    unittest.main()