# Write a program to find the second largest element in the list

def SecondLargestElement(li):
    max =0
    secondMax =0
    for i in range(0,len(li)):
        if(li[i]>max  ):
            secondMax =max
            max=li[i]
        elif(li[i]>secondMax and li[i]!=max):
            secondMax =li[i]
    return max,secondMax


li = [10,20,30,40,50,60,70,80,90,1000]

num1,num2 =SecondLargestElement(li) 
print("The Largest Element is ",num1)
print("The Second Largest Element is ",num2)