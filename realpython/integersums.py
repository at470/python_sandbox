def add_it_up(input):
    if type(input) == int:
        loop = 0
        sum = 0
        while loop <= input:
            sum = sum + loop
            loop =+ 1
        return sum
    else:
        return 0
