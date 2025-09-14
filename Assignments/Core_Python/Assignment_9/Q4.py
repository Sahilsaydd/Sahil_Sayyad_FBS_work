## Write program to calculate the sum of the n using the recursive function 
def SumOfNumber(n):
    if(n==0):
        return 0
    else:
        return n+SumOfNumber(n-1)
    

n = int(input('Enter the number :'))
res = SumOfNumber(n)
print(f'The sum of the series {res}')