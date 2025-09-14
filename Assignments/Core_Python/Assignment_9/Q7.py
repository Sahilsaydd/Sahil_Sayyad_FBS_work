## Write a program to calculate the sum of the  digit

def SumOfDigit(n,sum=0):
    if(n == 0):
        return sum
    else:
        digit = n%10
        sum = sum+digit
        return  SumOfDigit(n//10,sum)
    

n = int(input('Enter the number :'))
res  = SumOfDigit(n)
print(f'The sum is :{res}')