## Write a program to calculate the m to the power of n 
def MNPower(m,n):
    if(n==0):
        return 1
    else:
        return m*MNPower(m,n-1)
    

m= int(input("Enter the M value :"))
n = int(input("Enter the N Value :"))
res=MNPower(m,n)
print(f'{m} to the power {n} is :{res}')