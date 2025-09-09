### Write a program to reverse of a number

def ReverseNumber(n):
    rev =0
    while(n!=0):
        d = n%10
        rev = rev*10+d
        n=n//10
    return rev


n = int(input('Enter the Number :'))
res = ReverseNumber(n)
print(f'The original Numbers : {n}')
print(f'The Reverse Number is : {res}')