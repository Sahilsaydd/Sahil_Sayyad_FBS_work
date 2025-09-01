## Write a program to take the input from user and check if the number is prime or not
num = int(input('Enter the number to check if it is prime or not :'))
i=2
while(i<num):
    if(num%i==0):
        print(f'{num} is not a prime number')
        break
    i+=1
else:
    print(f'{num} is a prime number')
    