## Write a program to check if a given number is perfect number or not
num=int(input('Enter the number to check if it is perfect number or not :'))
sum= 0
i=1
while(i<num):
    if(num%i==0):
        sum+=i
    i+=1
if(sum==num):
    print(f'{num} is a perfect number .')
else:
    print(f'{num} is not a perfect number .')