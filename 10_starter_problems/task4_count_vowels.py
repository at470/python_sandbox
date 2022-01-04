def count_vowels_in_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count
