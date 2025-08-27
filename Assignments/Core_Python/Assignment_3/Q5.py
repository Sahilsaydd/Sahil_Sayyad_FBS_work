## Write a program to check whether the triangle is 
## equilateral, isosceles or scalene triangle.

a= int(input('Enter first side :'))
b= int(input('enter second side :'))
c =int(input('enter third side :'))

if(a==b and b==c):
    print('Triangle is Equilateral')
elif(a==b or b==c or c==a):
    print('Triangle is Isosceles')

else:
    print('Triangle is Scalene')