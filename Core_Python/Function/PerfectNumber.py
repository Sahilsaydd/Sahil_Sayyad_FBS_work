def perfectNumber():
    num =153
    temp = num
    sum =0
    for i in range(1,temp+1):
        if(temp%i==0):
            sum+=i
   
    if(sum==num):
        print(f'{num} is a perfect number ')
    else:
        print(f'{num} is not a perfect number')
perfectNumber()