## Write a program to create the new list from exiting list 
# which contains cube of each number of list

def CubeOfList(li):
    cubelist = []
    for i in li:
        cubelist.append(i ** 3)
    return cubelist


li =[10,20,30,40,50,60,70,80,90,100]

res = CubeOfList(li)
print("The new cube of list is :",res)