def discounted_price(full_price, discount_int):
    if discount_int > 100 or discount_int < 0:
        return 'invalid discount amount'
    else:
        return 0.01 * (100-discount_int) * full_price
