## Write a program to remove the nth index character from a non-empty string.
def removeCharAtIndex(str,n):
    firstpart = str[:n]
    secondpart = str[n+1:]
    return firstpart+secondpart

string = input("Enter a string :")
index = int(input("Enter the index of character to be removed :"))
print("The original string is :",string)
print("After removing the characte at  index ",index,"the new string is :\n",removeCharAtIndex(string,index))
