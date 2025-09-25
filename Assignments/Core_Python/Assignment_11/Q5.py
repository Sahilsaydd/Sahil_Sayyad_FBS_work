## Write a python program to sort a list According to the length of the elements within the list.

def sort_by_length(li):
    return sorted(li, key =len)




li = ['apple','banana','kiwi','cherry','mango','blueberry','strawberry']
sorted_list = sort_by_length(li)
print("Original list:",li)
print("Sorted list by length of elements:",sorted_list)