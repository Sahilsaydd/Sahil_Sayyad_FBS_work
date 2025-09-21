## Write a program to create a duplicate of an exiting list.
## it should not point to same list 
## I can do this using slicing
def NotPointAddress(li):
    li2 = li[:]
    li2.append(60)
    return li2


li = [10,20,30,40,50]
res = NotPointAddress(li)
print("Original List :",li)
print("Copy the list :",res)