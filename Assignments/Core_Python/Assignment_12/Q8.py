## Write a python program to remove the characters of odd index values in a string/

def remove_odd_index(s):
    result = ''
    for i in range(len(s)):
        if(i%2==0):
            result+=s[i]
    return result

string = input("Enter a string :")
print("After removing odd index characters the new string is : \n",remove_odd_index(string))

