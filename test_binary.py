import unittest

from binary_search import binary_search

class TestBinarySort(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 4

        result = binary_search(array=array, x=find, low=0, high=len(array)-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()