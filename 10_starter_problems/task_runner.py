import task1_radians_to_degrees as task1
import task2_sort_list as task2
import task3_convert_decimal_to_binary as task3
import task4_count_vowels as task4

# Task 1
print(task1.radians_to_degrees(3.1))

# Task 2
list = [10, 2, 45, 0, -1, 5]
print(list)

descending = task2.sort_list(list, 'desc')
print(descending)

list = [10, 2, 45, 0, -1, 5]
ascending = task2.sort_list(list, 'asc')
print(ascending)

list = [10, 2, 45, 0, -1, 5]
no_sort = task2.sort_list(list, 'none')
print(no_sort)

list = [10, 2, 45, 0, -1, 5]
junk = task2.sort_list(list, 'assdsfwer')
print(junk)

# Task 3
decimal = 8
print(decimal, task3.decimal_to_binary(decimal))

# Task 4
word = 'sly'
print(task4.count_vowels_in_word(word))
