## Write a program to check if given number is armstrong number or not using recursive function

def CountDigit(n):
    if(n==0):
        return 0
    else:
        return 1+CountDigit(n//10)
    
    
def armstrongsum(n,cnt):
    if(n==0):
        return 0
    else:
        digit = n%10
        return (digit**cnt)+armstrongsum(n//10,cnt)

n= int(input('Enter the number :'))
cnt = CountDigit(n)
sum = armstrongsum(n,cnt)

print(cnt)

if(n==sum):
    print(f'{n} is a armstrong number')
else:
    print(f'{n} is not a armstrong number')