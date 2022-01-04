# 2. Sort a list
# Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
#
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.

def sort_list(list, order):
    if order == 'desc':
        list.sort(reverse=True)
        return list
    elif order == 'asc':
        list.sort()
        return list
    elif order == 'none':
        return list
    else:
        return 'unable to sort, check order parameter'

list = [10, 2, 45, 0, -1, 5]

print(list)

descending = sort_list(list, 'desc')
print(descending)

list = [10, 2, 45, 0, -1, 5]

ascending = sort_list(list, 'asc')
print(ascending)

list = [10, 2, 45, 0, -1, 5]

no_sort = sort_list(list, 'none')
print(no_sort)

list = [10, 2, 45, 0, -1, 5]

junk = sort_list(list, 'assdsfwer')
print(junk)
