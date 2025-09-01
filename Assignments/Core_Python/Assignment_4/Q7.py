## Write a program to print all integers up to n that aren't divisible by 2 and 3
n= int(input('Enter the number upto which you want to print integers that are not divisible by 2 and 3 :'))
i=1
while(i<=n):
    if(i%2!=0 and i%3!=0):
        print(i,end=" ")
    i+=1
else:
    print('\n These are the numbers that are not divisible by 2 and 3')