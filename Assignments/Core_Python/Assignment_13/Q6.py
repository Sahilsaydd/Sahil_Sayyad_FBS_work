## Write a python program to multiply all the items in a dictionary. 

def multiply_dict_items(dictionary):
    result = 1
    for value in dictionary.values():
        result*=value
    return  result


my_dict = {'a':100,'b':200,'c':300, 'd':400}

print("The dictionary is :",my_dict)
result = multiply_dict_items(my_dict)
print("The multiplication of all the items in the dictionary is :",result)