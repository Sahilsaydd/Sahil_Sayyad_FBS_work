## write a python program to take in a string and replace every blank space with hyphen(-)

def replace_space_with_hyphen(s):
    return s.replace(' ', '-')

string  = input("Enter a string :")
print("The original string is :",string)
print("After replacing space with hyphen the new string is :\n",replace_space_with_hyphen(string))
