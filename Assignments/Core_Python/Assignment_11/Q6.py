## Write a python program to find the union of two lists 

def union_of_lists(list1, list2):
    for i in range(len(list2)):
        if(list2[i] not in list1):
            list1.append(list2[i])
    return list1



list1 =[1,2,3,4,5]
list2 =[4,5,6,7,8]
print("List1 :",list1)
print("List2 :",list2)
result = union_of_lists(list1,list2)
print("The union of two lists is :",result)
    