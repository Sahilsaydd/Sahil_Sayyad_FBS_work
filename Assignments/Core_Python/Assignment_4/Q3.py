## Write a program to print the sum of series upto n

n =int(input('Enter the number to print the sum of series :'))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1

print(f'{sum} is a sum of series upto {n}')
    