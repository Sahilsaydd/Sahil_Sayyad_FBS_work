## Write a python program to replace every blank space with hyphen(-) in a string.

def replace_space_with_hyphen(s):
    return s.replace(" ","_")



string = input('Enter a string :')
print('The original string is :',string)
print('After replacing space with hyphen the new string is :\n',replace_space_with_hyphen(string))
