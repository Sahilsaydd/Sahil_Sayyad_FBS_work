## Write a python program to count number of lowercase characters in a string .

def count_lowercase(s):
    count = 0
    for char in s:
        if (char.islower()):
            count+=1
    return count


string = input("Enter a string :")
print("The original string is :",string)
print("Number of lowercase characters in the string is :",count_lowercase(string))