## With passing parameter (w/ input)
## With returning a value (w(output))
# perfect Number : 
#     6 = 1 2 3 4 5 
#     divisor are = 1 2 3 
#     sum of this = 1+2+3 = 6
#     6==6  perfect number

def checkPerfectNo(num):
    sum = 0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    return num == sum


num = int(input("Enter the Number to check perfect or not :"))
if checkPerfectNo(num):
    print(f'{num} is a perfect number .')
else:
    print(f'{num} is not a perfect number .')