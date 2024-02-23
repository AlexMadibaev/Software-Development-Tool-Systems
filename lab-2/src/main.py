# src/main.py

def sort_lists():
    # Инициализация списков
    my_list = ["leaf", "cherry", "fish"]
    my_list1 = ["D", "C", "B", "A"]
    my_list2 = [3, 4, 5, 1, 2]

    # Сортировка списка my_list по возрастанию
    my_list.sort()

    # Сортировка списка my_list1 по возрастанию
    my_list1.sort()

    # Сортировка списка my_list2 по возрастанию
    my_list2.sort()

    # Возвращаем отсортированные копии списков
    return sorted(my_list), sorted(my_list1), sorted(my_list2)
