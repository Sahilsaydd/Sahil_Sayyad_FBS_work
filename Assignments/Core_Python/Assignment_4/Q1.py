## Write a program to print all even number until n  

n = int(input('Enter the number :'))
i=1
while(i<=n):
    if(i%2==0):
        print(f'{i} ',end=" ")
    i+=1


print('This is all Even Number')