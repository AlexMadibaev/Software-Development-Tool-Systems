import unittest
from unittest.mock import patch
from src.main import sort_lists

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['leaf cherry fish', 'D C B A', '3 4 5 1 2'])
    def test_sort_lists(self, mock_input):
        my_list_sorted, my_list1_sorted, my_list2_sorted = sort_lists()

        # Проверяем сортировку списка my_list
        self.assertEqual(my_list_sorted, ['cherry', 'fish', 'leaf'])
        print("Test for sorting my_list passed successfully.")

        # Проверяем сортировку списка my_list1
        self.assertEqual(my_list1_sorted, ['A', 'B', 'C', 'D'])
        print("Test for sorting my_list1 passed successfully.")

        # Проверяем сортировку списка my_list2
        self.assertEqual(my_list2_sorted, [1, 2, 3, 4, 5])
        print("Test for sorting my_list2 passed successfully.")

if __name__ == '__main__':
    unittest.main()
