def only_numbers_from_list(list):
    result = []
    for i in list:
        if isinstance(i,int):
            result.append(i)
    return result
