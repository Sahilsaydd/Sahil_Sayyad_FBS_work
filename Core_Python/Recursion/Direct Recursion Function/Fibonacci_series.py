## Write a program to calculate the fibonacci series using the direct recursion.

def fibo(n,a,b):
    if(n>0):
        c=a+b
        print(c,end=" ")
        fibo(n-1,b,c)

n =11
fibo(n,-1,1)