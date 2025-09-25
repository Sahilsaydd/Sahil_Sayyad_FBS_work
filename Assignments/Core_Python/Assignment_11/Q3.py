##write a program to sort the list according to the second element  in sublist 

# Define a function to return the second element of a sublist
def takeSecond(li):
    return li[1]


li = [[1,2],[3,1],[5,0],[5,3],[4,4]]

sorted_list = sorted(li, key = takeSecond)
print('Original List :',li)
print('Sorted List :',sorted_list)