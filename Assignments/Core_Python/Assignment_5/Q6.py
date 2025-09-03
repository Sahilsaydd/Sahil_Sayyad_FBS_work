### write a program to print number between 1 to 100 prime number

for i in (range(1,101)):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print( i , end=" ")
        



print(" \n This are all Prime number from 1  to 100")