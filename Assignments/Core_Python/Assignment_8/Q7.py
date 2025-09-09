### Write a program to find the sum of digit of a number 

def sumOfDigit(n):
    sum =0
    while(n!=0):
        d = n%10
        sum +=d
        n = n//10
    return sum


n = int(input("Enter the number to Sum of its digit :  "))
res=sumOfDigit(n)
print(f'The sum {n} its digit  : {res}')
        