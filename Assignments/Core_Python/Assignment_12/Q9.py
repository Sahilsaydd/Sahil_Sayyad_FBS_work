## Write a python program to calculate the Number of words and number of characters present in a string.

def count_words_and_characters(s):
    words = s.split()
    num_words = len(words)
    num_characters = len(s)
    return num_words,num_characters


string =input("Enter a String :")
words,characters = count_words_and_characters(string)
print("Number of words in the string :",words)
print("Number of characters in the string :",characters)