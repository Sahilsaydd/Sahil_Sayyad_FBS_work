## Write a program to check whether the given number is prime or not.

num = int(input('Enter the Number .'))

for i in range(2,num+1):
    if(num%i==0):
        print(f'{num} is not a prime number . ')
        break
    else:
      print(f'{num} is a prime number .')
      break