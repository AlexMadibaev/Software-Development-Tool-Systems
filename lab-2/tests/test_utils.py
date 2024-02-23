import unittest
from src import utils

class TestUtils(unittest.TestCase):
    def test_sort_list(self):
        my_list = ["leaf", "cherry", "fish"]
        utils.sort_list(my_list)
        self.assertEqual(my_list, ['cherry', 'fish', 'leaf'])

    def test_sort_list_copy(self):
        my_list = ["leaf", "cherry", "fish"]
        sorted_copy = utils.sort_list_copy(my_list)
        self.assertEqual(sorted_copy, ['cherry', 'fish', 'leaf'])
        self.assertEqual(my_list, ["leaf", "cherry", "fish"])  # Проверяем, что исходный список не изменился

    def test_calculate_average(self):
        numbers = [3, 1, 4, 2]
        average = utils.calculate_average(numbers)
        self.assertEqual(average, 2.5)

if __name__ == '__main__':
    unittest.main()
