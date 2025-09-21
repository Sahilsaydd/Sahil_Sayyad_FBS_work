### Write a program to print all number which are divisible by m and n in the list

def DivisibleMN(li,m,n):
    for i in range(0,len(li)):
        if(li[i]%m==0 and li[i]%n==0):
            print(li[i],end=" ")
    else:
        None
        

li = [10,11,12,13,14,15,16,17,18,19,20]
m = int(input("Enter the value of the M :"))
n= int(input('Enter the value of n :'))
DivisibleMN(li,m,n)
