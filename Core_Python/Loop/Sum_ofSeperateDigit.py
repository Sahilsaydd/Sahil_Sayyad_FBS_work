num =int(input('Enter number :'))
temp=num
sum=0
while(temp>0):
    d= temp%10
    sum = sum+d
    temp=temp//10
    print(f'{d}')

print(f'The sum is {sum}')
