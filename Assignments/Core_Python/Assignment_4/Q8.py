## Write a program to find which numbers are divisible by 7 and multiple of 5 in a given range
n = int(input('Enter the number upto which you want to find numbers that are divisible by 7 and multiple of 5 :'))
i=1
while(i<=n):
    if(i%7==0 and i%5==0):
        print(i,end=" ")
    i+=1
else:
    print('\n These are the numbers that are divisible by 7 and multiple of 5')