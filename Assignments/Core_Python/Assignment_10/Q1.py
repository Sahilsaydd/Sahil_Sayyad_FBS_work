def SumOfList(li):
    sum = 0
    for i in li:
        sum=sum+i
    return sum


n = int(input("how many element you want in a list :"))
li = []
for i in range(0,n):
    ele = int(input(f"Enter the Element {i+1}"))
    li.append(ele)
    

res = SumOfList(li)
print(f'{res} is a sum of the list')