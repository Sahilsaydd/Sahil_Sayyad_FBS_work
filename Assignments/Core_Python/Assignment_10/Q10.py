## Write a program to remove all the occurrences of a given element in a list

def RemoveOccurrences(ele,li):
    result = []
    for i in range(0,len(li)):
        if(ele!=li[i]):
            result.append(li[i])
    
    return result



li = [10,10,2030,20,20,30,40,50,50,50]
element = int(input("Enter the number to remove from the list :"))
res = RemoveOccurrences(element,li)

print(f"The original list : {li}")
print(f'After removing the given element { element} the list Is : {res}')