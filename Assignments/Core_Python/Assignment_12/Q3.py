## Write a python program to detect the two strings are anagrams or not
def areAnagrams(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
    

str1 = input("Enter the first string :")
str2 = input("Enter the second string :")

if(areAnagrams(str1,str2)):
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")
    
