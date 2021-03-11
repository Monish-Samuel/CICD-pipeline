
# This method is used to find the number of characters in a string without spaces
def word_length(sentence):
    r = sentence.replace(" ", "")
    size = len(r)
    return f'The number of characters in "{sentence}" is {size}'


# This method for finding matching statement
def matching_char(sentence, word):
    sentence = sentence
    word = word
    i = 0
    for char in sentence:
        if char == word:
            i += 1
    return f'No. of {word} in "{sentence}" is {i}'


# This method is to reverse the string
def reverse(sentence):
    sentence = sentence
    return 'The reverse of String: ' + sentence[::-1]


# This method is used to find whether the string is palindrome or not
def palindrome_or_not(sentence):
    r = sentence.replace(' ', '')
    if r[::-1].lower() == r.lower():
        return 'Its a Palindrome'
    else:
        return 'Its Not a Palindrome'


