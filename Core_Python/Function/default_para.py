def add(num1,num2,num3=10,num4=0):
    return num1+num2+num3+num4

res=add(10,15,50,30)
## Whenever we  passing the parameter it not take from default value
ans =add(45,18)
## Whenever we dont't pass parameter it take from default value
print("Addition with passing parameter :",res)
print("Addition with without passing parameter",ans)

1 