### sum of all odd number between 1 to n

def sumOfOddNumber(n):  
    sum=0
    for i in range(1,n+1):
        if(i%2==0):
            continue
        else:
            sum+=i
    return sum

n = int(input("Enter the Numbers :"))
res = sumOfOddNumber(n)
print(f'The sum of odd number between 1 to {n} is : {res}')

## 1,3,5,7,9 9+7+5+3+1