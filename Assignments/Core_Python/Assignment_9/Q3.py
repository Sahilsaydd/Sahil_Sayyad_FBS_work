## Write a program  to reverse the given number using the recursive function 
def ReverseNumber(n,rev=0):
    if(n==0):
        return rev
    else:
        digit = n%10
        rev =rev*10+digit
        return ReverseNumber( n//10 , rev)
    
    

n = int(input("Enter the number :"))
res = ReverseNumber(n)
print(f'The Original Number is : {n}')
print(f'The reversed number is : {res}')