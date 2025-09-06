# a. 1! + 2! + 3! + 4! + .....n!
## Find the nth  factorial and sum it..

n = int(input('Enter the number :'))
sum =0
fact=1
for i in range(1,n+1):
    fact *=i
    sum+=fact

print(f'The sum of the {n} factorial is  {sum}')