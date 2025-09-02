n =int(input('Enter the number :'))
orginalNumber = n
sum=0

while(n!=0):
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact*=i
        
    sum+=fact
    n=n//10
if(orginalNumber==sum):
    print(f'{orginalNumber} is a Strong number  and is a sum of fact :{sum}')
else:
    print(f'{orginalNumber} is not a Strong Number')