## Write a program to find the largest and minimum number in a list

def LargestMinimum(li):
    max=0
    min =li[0]
    for i in range(0,len(li)):
        if(li[i]>max):
            max=li[i]
        elif(li[i]<min):
            min=li[i]
    return min,max



li=[100,20,30,40,50,60,70,80,90,1000]

num1,num2= LargestMinimum(li)

print("The Minimum number is :",num1)
print("The Maximum number is :",num2)