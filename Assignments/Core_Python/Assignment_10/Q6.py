##write a program to remove duplicates from a list

def DeleteDuplicates(li):
    uniqueList = []
    for item in li:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList


li = [10,20,30,40,40,40,70,80,90,100]
print("The original List : ",li)
print("The unique list :",DeleteDuplicates(li))