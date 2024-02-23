## Общее описание решения

Проект представляет собой пример кода на Python для сортировки списков различных типов данных и вычисления среднего значения. Включает основной код программы, вспомогательные функции и модульные тесты.

### Описание функций

### Функция `sort_list(list_to_sort: list) -> None`

Сортирует переданный список `list_to_sort` по возрастанию.

**Пример использования:**
```python
my_list = ["leaf", "cherry", "fish"]
sort_list(my_list)
print(my_list)  # Результат: ['cherry', 'fish', 'leaf']
```

### Функция `sort_list_copy(list_to_sort: list) -> list`

Возвращает отсортированную копию переданного списка `list_to_sort` без изменения исходного.

**Пример использования:**
```python
my_list = ["D", "C", "B", "A"]
sorted_copy = sort_list_copy(my_list)
print(sorted_copy)  # Результат: ['A', 'B', 'C', 'D']
```

### Функция `calculate_average(numbers: list) -> float`

Вычисляет среднее арифметическое чисел в переданном списке `numbers`.

**Пример использования:**
```python
my_numbers = [3, 1, 4, 2]
average = calculate_average(my_numbers)
print(average)  # Результат: 2.5
```
