class InvalidInput( Exception ):
    pass

def multiply(x):
    str_x = str(x)
    if len(str_x) < 3:
        print('This integer isn\'t long enough')
        raise InvalidInput
    else:
        max_loop_num = len(str_x)-1
        i = 0
        product = 1
        while i <= max_loop_num:
            product = int(str_x[i]) * product
            i += 1
        return product

def matching(x):
    unique_digits_from_multiply = set(int(i) for i in str(multiply(x)))
    unique_digits_from_x = set(int(i) for i in str(x))

    matching_digits = []
    for i in unique_digits_from_multiply:
        for j in unique_digits_from_x:
            if i == j:
                matching_digits.append(i)
    matching_digits.sort()
    if matching_digits == []:
        print('No shared digits!')
    return matching_digits
#

print(multiply(1468))

print(multiply(74))

print(multiply(123), matching(123))
