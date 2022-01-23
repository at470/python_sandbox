import unittest
import re

class TestCaesarCharCipher(unittest.TestCase):

    def test_when_a_shift_1(self):
        self.assertEqual(caesar_char('a',1), 'b')

    def test_when_b_shift_1(self):
        self.assertEqual(caesar_char('b',1), 'c')

    def test_when_b_shift_2(self):
        self.assertEqual(caesar_char('b',2), 'd')

    def test_when_a_shift_minus1(self):
        self.assertEqual(caesar_char('a',-1), 'z')

    def test_when_whitespace(self):
        self.assertEqual(caesar_char(' ',5), ' ')

    def test_when_punctuation(self):
        self.assertEqual(caesar_char('.',5), '.')

class TestCaesarCipher(unittest.TestCase):

    def test_when_ab_shift_1(self):
        self.assertEqual(caesar('ab',1), 'bc')

    def test_when_ab_shift_2(self):
        self.assertEqual(caesar('ab',2), 'cd')

    def test_when_multichar_with_whitespace_and_punctuation(self):
        self.assertEqual(caesar(' abc.',2), ' cde.')

if __name__ == '__main__':
    unittest.main()

def caesar_char(letter, shift):
    character = re.search(r'[a-zA-Z]', letter)
    if character == None:
        return letter
    else:
        return chr(ord(letter) + shift%26)

def caesar(letter, shift):
    returned_string = ''
    for i in letter:
        returned_string = returned_string + caesar_char(i, shift)
    return returned_string
