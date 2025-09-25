## Python program to take in two strings and display the larger string without using built-in functions.

def larger_string(s1,s2):
    len1 =0
    len2 =0
    for char in s1:
        len1+=1
    
    for char in s2:
        len2+=1
    
    if(len1>len2):
        return s1
    elif(len2>len1):
        return s2
    else:
        return "Both Strings are of equal length"
    

string1 = input("Enter first string :")
string2 = input("Enter second string :")
print("The larger string is :\n",larger_string(string1,string2))