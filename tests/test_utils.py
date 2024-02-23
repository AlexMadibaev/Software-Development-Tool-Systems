import unittest
from src.utils import sort_list, sort_list_copy, calculate_average, initialize_list

class TestUtils(unittest.TestCase):
    def test_sort_list(self):
        my_list = ["leaf", "cherry", "fish"]
        sort_list(my_list)
        self.assertEqual(my_list, ['cherry', 'fish', 'leaf'])
        print("Test for sort_list passed successfully.")

    def test_sort_list_copy(self):
        my_list = ["leaf", "cherry", "fish"]
        sorted_copy = sort_list_copy(my_list)
        self.assertEqual(sorted_copy, ['cherry', 'fish', 'leaf'])
        self.assertEqual(my_list, ["leaf", "cherry", "fish"])  # Проверяем, что исходный список не изменился
        print("Test for sort_list_copy passed successfully.")

    def test_calculate_average(self):
        numbers = [3, 1, 4, 2]
        average = calculate_average(numbers)
        self.assertEqual(average, 2.5)
        print("Test for calculate_average passed successfully.")

    def test_initialize_list(self):
        with unittest.mock.patch('builtins.input', side_effect=['1 2 3']):
            result = initialize_list()
        self.assertEqual(result, ['1', '2', '3'])
        print("Test for initialize_list passed successfully.")

if __name__ == '__main__':
    unittest.main()