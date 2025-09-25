## Write a python program to count the  number of digits and letters in a string.
def count_digits_and_letters(s):
    num_digits = 0
    num_letters =0
    for char in s:
        if(char.isdigit()):
            num_digits+=1
        elif(char.isalpha()):
            num_letters+=1
    return num_digits,num_letters


string = input("Enter a string :")
digits,letters = count_digits_and_letters(string)
print("Number of digits in the string is :",digits)
print("Number of letters in the string is :",letters)
