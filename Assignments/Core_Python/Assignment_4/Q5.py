## Write a program to print fibonacci number upto the n
n= int(input('Enter the number to print fibonacci series :'))
a=0
b=1
print(f'{a} {b} ',end=" ")
while(n!=0):
    c=a+b
    print(f'{c}',end=" ")
    a=b
    b=c
    n-=1

print('\n This is fibonacci series')