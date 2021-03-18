import Alphabet


# Method to print Output
def run(sentence, character):
    """this method imports the methods from the Alphabet file and prints the output for the input given in this
    method"""
    print(Alphabet.word_length(sentence))
    print(Alphabet.matching_char(sentence, character))
    print(Alphabet.palindrome_or_not(sentence))
    print(Alphabet.reverse(sentence))


a = "Welcome to TCS"
b = "T"
run(a, b)
