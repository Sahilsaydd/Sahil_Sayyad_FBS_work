## Write program to reverse the number using recursive function

def ReversedFunction(n,rev=0):
    if(n==0):
        return rev
    else:
        digit =n % 10
        rev = rev * 10 + digit
        return ReversedFunction(n // 10, rev)
    

n = int(input('Enter the number :'))
res = ReversedFunction(n)
print(f'The original number is this : {n}')
print(f'The Reverse number is {res}')