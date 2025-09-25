## Write a python program to count the occurrences of each word in a given string/paragraph.  

def count_word_occurrences(s):
    words = s.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if(word in word_count):
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count


string = input("Enter a string :")
word_cnt = count_word_occurrences(string)
print("Occurrences of each word in the string is :",word_cnt)
