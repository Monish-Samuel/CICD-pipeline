import Alphabet


def run(sentence, character):
    print(Alphabet.word_length(sentence))
    print(Alphabet.matching_char(sentence, character))
    print(Alphabet.palindrome_or_not(sentence))
    print(Alphabet.reverse(sentence))


a = "Welcome to TCS"
b = "T"
run(a, b)
