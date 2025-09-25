### Write a python program to replace all the occurences of 'a with '$' in a string.

def replace_a_with_dollar(str):
    for i in str:
        if(i=='a'):
            str=str.replace('a','$')
    return str


string = input("Enter a String :")
print("the original string is : ",string)
print("After replacing 'a' with '$' the new string is : \n",replace_a_with_dollar(string))
