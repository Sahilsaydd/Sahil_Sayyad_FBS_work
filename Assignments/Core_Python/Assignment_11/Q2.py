def MergingList(l1,l2):
    mergesortlist = l1+l2
    n = len(mergesortlist)
    for i in range(n):
        for j in range(0,n-i-1):
            if(mergesortlist[j]>mergesortlist[j+1]):
                mergesortlist[j],mergesortlist[j+1]=mergesortlist[j+1],mergesortlist[j]
    return mergesortlist


l1 =[1,2,3,2,5]
l2=[6,7,8,9,10]
result = MergingList(l1,l2)
print("The l1 is :",l1)
print("The l2 is :",l2)

print("The Merging of this 2 list and sorted : ",result)