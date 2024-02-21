# chore: Initialize lists
my_list = ["leaf", "cherry", "fish"]
my_list1 = ["D", "C", "B", "A"]
my_list2 = [3, 4, 5, 1, 2]

# chore: Sort my_list in ascending order
my_list.sort()
# Result: ['cherry', 'fish', 'leaf']

# chore: Sort my_list1 in ascending order
my_list1.sort()
# Result: ['A', 'B', 'C', 'D']

# chore: Sort my_list2 in ascending order
my_list2.sort()
# Result: [1, 2, 3, 4, 5]

# feat: Print sorted copies of lists
print(sorted(my_list))  # Returns a sorted copy of my_list without modifying the original.
# Result: ['cherry', 'fish', 'leaf']

print(sorted(my_list1))  # Returns a sorted copy of my_list1 without modifying the original.
# Result: ['A', 'B', 'C', 'D']

print(sorted(my_list2))  # Returns a sorted copy of my_list2 without modifying the original.
# Result: [1, 2, 3, 4, 5]
