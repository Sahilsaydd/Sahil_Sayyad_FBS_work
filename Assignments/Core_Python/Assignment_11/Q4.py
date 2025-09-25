## Write a python program to find the second largest number in a list. using bubble sort 

def bubble_sort(li):
    for i in range(1,len(li)):
        for j in range(0,len(li)-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
    return li


li = [50,56,73,3,343,5,2,111,6,7,8,9]
second_largest = bubble_sort(li)[-2]
print("Second largest number is:",second_largest)
            