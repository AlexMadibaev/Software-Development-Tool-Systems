def sort_list(list_to_sort):
    """Сортирует список по возрастанию."""
    list_to_sort.sort()

def sort_list_copy(list_to_sort):
    """Возвращает отсортированную копию списка."""
    return sorted(list_to_sort)

def calculate_average(numbers):
    """Вычисляет среднее арифметическое чисел в списке."""
    return sum(numbers) / len(numbers)

def initialize_list():
    """Инициализирует список через ввод пользователя."""
    user_input = input("Введите элементы списка через пробел: ")
    return user_input.split()
