### Write a program Calculate the sum of first N Number 

n=int(input('Enter the Number :'))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1

print(f'{sum} is a  sum of first {n} numbers')