import unittest
from src.main import sort_lists

class TestMain(unittest.TestCase):
    def test_sort_lists(self):
        my_list_sorted, my_list1_sorted, my_list2_sorted = sort_lists()

        # Проверяем сортировку списка my_list
        self.assertEqual(my_list_sorted, ['cherry', 'fish', 'leaf'])

        # Проверяем сортировку списка my_list1
        self.assertEqual(my_list1_sorted, ['A', 'B', 'C', 'D'])

        # Проверяем сортировку списка my_list2
        self.assertEqual(my_list2_sorted, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
