import unittest

class TestAddItUp(unittest.TestCase):

    def test_when_input_is_1(self):
        self.assertEqual(add_it_up(1), 1)

    def test_when_input_is_2(self):
        self.assertEqual(add_it_up(2), 3)

    def test_when_input_is_negative(self):
        self.assertEqual(add_it_up(-5), 0)

    def test_when_input_is_not_an_int(self):
        self.assertEqual(add_it_up("Pooch"), 'pal', msg='it\'s not working')


if __name__ == '__main__':
    unittest.main()

def add_it_up(input):
    loop = 0
    sum = 0
    if type(input) == int:
        while loop < input:
            loop = loop + 1
            sum = sum + loop
    return sum
