# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged 

def exchange_first_last_char(s):
    if(len(s)<=1):
        return s
    else:
        return s[-1]+s[1:-1]+s[0]
    


string = input("Enter a string :")
print("The original string is :",string)
print("After exchanging the first and last character the new string is : \n",exchange_first_last_char(string))
