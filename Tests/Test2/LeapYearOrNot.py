## Write a program to accept a year from user and check whether it is leap year or not.
year = int(input('Enter a year:'))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
 