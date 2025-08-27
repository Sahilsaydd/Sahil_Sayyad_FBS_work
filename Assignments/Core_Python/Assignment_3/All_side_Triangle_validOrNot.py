## Write a program to input all sides of triangle and check whether triangle is valid or not .
a= int(input('Enter first side :'))
b= int(input('enter second side :'))
c = int(input('enter third side :'))

if(a+b>c and b+c>a and c+a>b):
    print('Triangle is valid')
else:
    print('Triangle is not valid')
    