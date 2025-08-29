n =int(input('Enter the Number :'))

fact=1
while(n!=0):
    fact*=n
    n-=1
print(f'{fact} is a factorial of a {n}')