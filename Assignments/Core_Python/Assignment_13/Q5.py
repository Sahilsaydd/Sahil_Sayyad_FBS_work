## Write a python program to sum all the items in a dictionary.

def sum_dict_items(dictionary):
    total = 0
    for value in dictionary.values():
        total+=value
    return total


my_dict = {'a':100,'b':200,'c':300,'d':400}

print("The dictionary is :",my_dict)
result = sum_dict_items(my_dict)
print("The sum of all the items in the dictionary is :",result)
# --- IGNORE ---