## Write a program to  find the following fibonacci series using function 
## 1 1 2 3 5 8

def FibonacciSeries(num):
    a=-1
    b=1
    for i in range(1,num+1):
        
        c= a+b
        print(c,end=" ")
        a=b
        b=c


n = int(input("Enter the number :"))
FibonacciSeries(n)