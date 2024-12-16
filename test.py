import unittest

from main import create_cards, check_zeros

class Test01(unittest.TestCase):
    def test_create_cards(self):
        '''
        Here we test the function create_cards with arg = 0
        '''
        data = {"b" : [0, 0, 0, 0, 0]}
        result = create_cards(0)
        self.assertEqual(data["b"], result["b"])

class Test02(unittest.TestCase):
    def test_create_deck(self):
        '''
        Here we test the function create_cards with arg = 1
        '''
        data = {"b" : 0, "i" : 0, "n" : 0, "g" : 0, "o" : 0}
        result = create_cards(1)
        self.assertEqual((data["b"], data["i"], data["n"], data["g"], data["o"]), (result["b"][0], result["i"][0], result["n"][0], result["g"][0], result["o"][0]))

class Test03(unittest.TestCase):
    def test_create_deck(self):
        '''
        Here we test the function create_ cards with arg = 2
        '''
        data = {"b" : [0, 1, 2, 3, 4], "i" : [1, 0, 2, 3, 4], "n" : [1, 2, 0, 3, 4], "g" : [1, 2, 3, 0, 4], "o" : [1, 2, 3, 4, 0]}
        result = create_cards(2)
        self.assertEqual((data["b"][0], data["i"][1], data["n"][2], data["g"][3], data["o"][4]), (result["b"][0], result["i"][1], result["n"][2], result["g"][3], result["o"][4]))

class Test04(unittest.TestCase):
    def test_create_deck(self):
        '''
        Here we test the function create_ cards with arg = 3
        '''
        data = {"b" : [0, 1, 2, 3, 4], "i" : [1, 0, 2, 3, 4], "n" : [1, 2, 0, 3, 4], "g" : [1, 2, 3, 4, 0], "o" : [1, 2, 3, 0, 4]}
        result = create_cards(3)
        self.assertEqual((data["b"][0], data["i"][1], data["n"][2], data["g"][4], data["o"][3]), (result["b"][0], result["i"][1], result["n"][2], result["g"][4], result["o"][3]))


class Test05(unittest.TestCase):
    def test_check_zeros(self):
        '''
        Here we test the check_zeros function
        '''
        result = check_zeros(create_cards(0))
        self.assertEqual(f"{True}, this is a winning card", result)


class Test06(unittest.TestCase):
    def test_check_zeros(self):
        '''
        Here we test the check_zeros function
        '''
        result = check_zeros(create_cards(1))
        self.assertEqual(f"{True}, this is a winning card", result)


class Test07(unittest.TestCase):
    def test_check_zeros(self):
        '''
        Here we test the check_zeros function
        '''
        result = check_zeros(create_cards(2))
        self.assertEqual(f"{True}, this is a winning card", result)

class Test08(unittest.TestCase):
    def test_check_zeros(self):
        '''
        Here we test the check_zeros function
        '''
        result = check_zeros(create_cards(3))
        self.assertEqual(f"{False}, this is ALMOST a winning card", result)
