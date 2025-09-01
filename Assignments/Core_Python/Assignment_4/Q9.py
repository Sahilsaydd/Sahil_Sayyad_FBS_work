## Write a program to print all number divisible by given number in a range
n=int(input("Enter the number :"))
d = int(input("Enter the divisor :"))
i=1
while(i<=n):
    if(i%d==0):
        print(i,end=" ")
    i+=1
else:
    print(f'\n This are the number that divisible by a {d} given number')