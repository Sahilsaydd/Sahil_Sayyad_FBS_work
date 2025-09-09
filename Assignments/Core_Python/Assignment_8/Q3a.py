## Write a program to find the sum of following series using the function :   
## a. 1+ 2 + 3 + 4+..... + n

def FirstNSum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

n = int(input("Enter The Number."))

res = FirstNSum(n)
print(f"{res} is a sum of first N Number")