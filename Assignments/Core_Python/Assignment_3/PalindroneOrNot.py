## Write a program to check whether a given string is a palindrome or not.
## Reverse a number without using loop or anything
num =int(input('Enter a number :')) 
n1 = num//100
n2 = (num//10)%10
n3 = num%10
rev = n3*100+n2*10+n1
if (num==rev):
    print(f'{num} is a palindrome number')
else:
    print(f'{num} is not a palindrome number')
       

