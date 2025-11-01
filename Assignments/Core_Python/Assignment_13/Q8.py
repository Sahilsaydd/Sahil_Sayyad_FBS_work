## Write a python program to count the frequency of words appearing in a string using dictionary.

def wordFrequency(s):
    words = s.split()
    freq ={}
    for word in words:
        if(word in freq):
            freq[word] +=1
        else:
            freq[word]=1
    return freq


s = "hello world hello"
print(wordFrequency(s))
