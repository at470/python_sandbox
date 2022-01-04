# Write a function multiply() that takes one parameter, an integer x. Check that x is an integer at least three characters long. If it is not, end the function and print a statement explaining why. If it is, return the product of x’s digits.
#
# Write another function matching() that takes an integer x as a parameter and “wraps” your multiply() function. Compare the results of the multiply() function on x with the original x parameter and return a sorted list of any shared digits between the two. If there are none, print “No shared digits!”


def multiply(x):
    str_x = str(x)
    if len(str_x) < 3:
        return print('This integer isn\'t long enough')
    else:
        max_loop_num = len(str_x)-1
        i = 0
        product = 1
        while i <= max_loop_num:
            product = int(str_x[i]) * product
            i += 1
        return product

print(multiply(1468))

print(multiply(74))
