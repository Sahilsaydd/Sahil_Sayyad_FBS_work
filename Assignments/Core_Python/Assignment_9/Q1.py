## Write a program to find the sum of series using recursive function
## i. 1! + 2! + 3! + 4! +..... + n!

def Fact(n):
    if(n==0):
        return 1
    else:
        return n*Fact(n-1)
    

def sumOfSeries(n):
    if(n==1):
        return Fact(1)
    else:
        return Fact(n)+sumOfSeries(n-1)

n = int(input("Enter the Number to calculate the factorial :"))
res =Fact(n)
sum= sumOfSeries(n)
print(f'{res} is a factorial of {n} number and the sum is {sum}')