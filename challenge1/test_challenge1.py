import unittest 
from challenge_1 import increment_dictionary_values


class TestIncrementDictionaryValues(unittest.TestCase):
    """This class tests the increment_dictionary_values function."""
    def setUp(self):
        self.data = {'a': 5}
            
    def test_increment_dictionary_values(self):
        increment_dict = increment_dictionary_values(self.data, 5)
        self.assertEqual(increment_dict['a'], 10)
    
    def test_decrement_dictionary_values(self):
        increment_dict = increment_dictionary_values(self.data, -1)
        self.assertEqual(increment_dict['a'], 4)


if __name__ == '__main__':
    unittest.main()
