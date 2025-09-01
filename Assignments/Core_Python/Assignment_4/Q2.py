## Write a program to all odd number until n

n= int(input('Enter the Number to check odd or not :'))
i=1
while(i<=n):
    if(i%2!=0):
        print(f'{i} ',end="")
    i+=1

print("\n This is all odd number")