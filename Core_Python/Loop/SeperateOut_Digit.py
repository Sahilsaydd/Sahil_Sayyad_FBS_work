num = int(input('Enter the number :'))
i=1
while(num>0):
    digit = num%10
    num = num // 10
    print(f'{digit} this is the {i}th digit')
    i+=1

print('Program executed successfully')
    
