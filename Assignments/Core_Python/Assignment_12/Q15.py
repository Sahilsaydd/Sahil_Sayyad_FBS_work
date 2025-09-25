## Write a python program to find the largest string without using the built-in function.
def largest_string(s1,s2,s3):
    len1 =0
    len2 =0
    len3 =0
    for char in s1:
        len1+=1
    
    for char in s2:
        len2+=1
    
    for char in s3:
        len3+=1
    
    if(len1>=len2 and len1>=len3):
        return s1
    elif(len2>=len1 and len2>=len3):
        return s2
    else:
        return s3
    

string1 = input("Enter First String :")
string2 = input("Enter the second string :")
string3 = input("Enter the third string :")
print("The First String :",string1)
print("The Second String :",string2)
print("The Third String : ",string3)
print("The largest String Is : ",largest_string(string1,string2,string3))
