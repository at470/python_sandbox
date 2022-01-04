# Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

# using bin
def decimal_to_binary(decimal):
    if decimal > 1024:
        return 'try a smaller number'
    else:
        binary = bin(decimal)
        binary = binary[2:]
        return binary

# without using bin
def decimal_to_binary_self(decimal):
    if decimal > 1024:
        return 'try a smaller number'
    else:
        binary = bin(decimal)
        binary = binary[2:]
        return binary


#
# from math import log
#
# string = '0000000000'
# print(string[-1])
# print(string[-2])
# print(string[-9])
#
# 2 --> string[-1]=1 --> 0000000001
