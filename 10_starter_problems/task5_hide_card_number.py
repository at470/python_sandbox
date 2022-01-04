def hide_card_number(number):
    if len(str(number)) == 16:
        return number[-4:]
    else:
        print('Enter a valid card number')
