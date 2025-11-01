## Write a python to find elements in a given set that are not in another set.

def find_difference(set1,set2):
    return set1 - set2



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(find_difference(set1, set2)) # output {1, 2, 3}