num =int(input('Enter the number :'))
cnt=0
temp =num
while(temp>0):
    d= temp%10
    cnt+=1
    temp =temp//10
    print(d)

print(f'The count is {cnt}')