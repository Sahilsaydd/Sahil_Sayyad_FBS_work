## Write a program to print the first N Prime NUmber
num = int(input('Enter the number :'))
temp = 2

while(num!=0):
    for i in range(2,temp):
        if(temp%i==0):
            break
    else:
        print(temp, end=" ")
        num-=1
    temp+=1