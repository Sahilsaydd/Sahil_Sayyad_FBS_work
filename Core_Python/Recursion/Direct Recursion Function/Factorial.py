## Write a program to calculate the factorial number using recursion

def fact(n):
    
    if(n==0):
        return 1
    else:
       return  n*fact(n-1)
        
        
n= 5
res = fact(n)
print(f'The factorial of {n} is a {res}')