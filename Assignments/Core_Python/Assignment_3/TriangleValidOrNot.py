### Write a program to input angle of  triangle and check whether triangle is valid or not.
a= int(input('Enter first angle of triangle :'))
b= int(input('Enter second angle of triangle :'))
c = int(input('Enter third angle of triangle :'))
if (a+b+c == 180):
    print('Triangle is valid')
else:
    print('Triangle is not valid')

# a = int() --- IGNORE ---
# b = int() --- IGNORE ---  
# c = int() --- IGNORE ---