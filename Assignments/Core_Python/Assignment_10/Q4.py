## Write a program to reverse the list

def ReverseList(li):
    ReverseList = []
    for i in range(len(li)-1, -1, -1):
        ReverseList.append(li[i])
    return ReverseList




li = [10,20,30,40,50,60,70,80,90,100]
res = ReverseList(li)
print("The original list :",li)
print("The Reverse list :",res)