def sort_lists():
    # Инициализация списков через ввод
    my_list = input("Введите элементы первого списка через пробел: ").split()
    my_list1 = input("Введите элементы второго списка через пробел: ").split()
    my_list2 = input("Введите элементы третьего списка через пробел: ").split()

    # Преобразование элементов списка my_list2 в целые числа
    my_list2 = [int(item) for item in my_list2]

    # Сортировка списка my_list по возрастанию
    my_list.sort()

    # Сортировка списка my_list1 по возрастанию
    my_list1.sort()

    # Сортировка списка my_list2 по возрастанию
    my_list2.sort()

    # Возвращаем отсортированные копии списков
    return sorted(my_list), sorted(my_list1), sorted(my_list2)