# Save the paragraph below — from Alice’s Adventures in Wonderland — to a variable named text. Write two programs using “for” loops and/or list comprehensions to do the following:
#
# Create a single string that contains the second-to-last letter of each word in text, sorted alphabetically and in lowercase. Save it to a variable named letters and print. If a word is less than two letters in length, use the single character available.
# Find the average number of characters per word in text, rounded to the nearest hundredth. This value should exclude special characters, such as quotation marks and semicolons. Save it to a variable named avg_chars and print.

import re

text = "Alice was beginning to get very tired of sitting \
by her sister on the bank, and of having nothing to do: \
once or twice she had peeped into the book her sister \
was reading, but it had no pictures or conversations in \
it, ‘and what is the use of a book,’ thought Alice, \
‘without pictures or conversations?’"

# Part 1
list_text = text.split(' ') #create a list, delimiter is whitespace

stripped_list = [] #strip out punctuations from original string
for i in list_text:
    stripped_list.append(re.sub('[^A-Za-z0-9]+', '', i))

letters = []
for word in stripped_list:
    if len(word) > 1:
        letters.append(word[len(word) - 2].lower())
    else:
        letters.append(word[0].lower()) #if len == 1 then take the first character
letters.sort()
print(letters)

# End of part 1
####

# Part 2
