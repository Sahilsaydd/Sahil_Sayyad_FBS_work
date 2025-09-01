## Write a program to print factorial of a number :

n= int(input('Enter the to display the factorial'))
fact=1

while(n!=0):
    fact*=n
    n-=1

print(f'The Factorial is {fact} ')