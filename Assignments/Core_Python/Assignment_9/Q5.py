## Write a program to find the factorial using the recursion function

def Factorial(n):
    if(n==0):
        return 1
    else:
        return n*Factorial(n-1)

n = int(input("Enter the Number to find the factorial :"))
res = Factorial(n)
print(f'The factorial of the {n} is a {res}')