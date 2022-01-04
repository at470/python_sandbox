import task1_radians_to_degrees as task1
import task2_sort_list as task2
import task3_convert_decimal_to_binary as task3
import task4_count_vowels as task4
import task5_hide_card_number as task5
import task6_x_and_o as task6
import task7_calculator as task7
import task8_discount as task8
import task9_just_numbers_from_list as task9
import task10_repeat_char as task10

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

# Task 5
card_number = '4444111112341234'
print(task5.hide_card_number(card_number))

# Task 6
string = '1234'
print(task6.x_o_comparison(string))

# Task 7
a = 10
b = 5
operator = '/'
print(task7.calculator(a, operator, b))

# Task 8
full_price = 1000
discount = 50
print(task8.discounted_price(full_price, discount))

# Task 9
list = [1,'abc', 10, 'screw', 'foo', 3, 1000, 2, 'bar']
print(list, task9.only_numbers_from_list(list))

# Task 10
str = 'yo'
print(task10.repeat_char_in_string(str))
