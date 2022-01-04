# make sure to run in python 3!!
# python3 four.py
def input_name():
    name = str(input("Enter your name: "))
    return name


def reverse_name():
    name = input_name()
    name = name.lower()
    reverse = name[::-1]
    if reverse == name:
        print(reverse.capitalize(), 'Palindrome!')
    else:
        print(reverse.capitalize())

reverse_name()
