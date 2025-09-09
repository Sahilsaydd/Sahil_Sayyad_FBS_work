## Write a program to find the sum of the following series .
## c. 1^1 + 2^2 + 3^3+ ...... n^n

def power(n):
    calculate_the_power =1
    for i in range(1,n+1):
        calculate_the_power = i**i
     
        
    return calculate_the_power 

n = int(input("Enter the number :"))
res =power(n)
print(f'{res} is power of {n}')