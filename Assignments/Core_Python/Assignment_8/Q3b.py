## Write a program to find the sum of following series using function 
## b. 1!+ 2! + 3! + 4!+..... + n!

def FactorialFistN(n):
    fact =1 
    for i in range(1,n+1):
        fact*=i
    return fact

n = int(input("Enter the Number to Calculate the first N number Factorials :"))
res = FactorialFistN(n)
print(f"{res} is a Factorials of first {n} numbers.")