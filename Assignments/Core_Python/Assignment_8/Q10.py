## Write a program to check if entered year is leap year or not

def CheckLeapYear(n):
    
    if(n%400==0):
        print(f'{n} is a leap year')
    elif(n%100==0):
        print(f'{n} is not a leap year')
    elif(n%4==0):
        print(f'{n} is a leap year')
    
    
n = int(input('Enter the number to check whether the given number is leap year or not . :'))
CheckLeapYear(n)

          
        