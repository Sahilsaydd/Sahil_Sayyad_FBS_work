### Write a program to print the fibonacci series using the recursion function 

def Fibonacci_Series(n, a,b):
    if(n>0):
        c=a+b
        print(c,end=" ")
        return Fibonacci_Series(n-1,b,c)
    

n=int(input('Enter the number : '))
a =-1
b=1
Fibonacci_Series(n,a,b)
