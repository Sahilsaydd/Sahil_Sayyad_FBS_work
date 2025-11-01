### Write a python program to add key-value pairs to a dictionary.
def add_key_value_pairs(dictionary,key,value):
    dictionary[key]=value
    return dictionary



my_dict = {"Id":101 ,'Name':"Sahil Sayyad"}
print("The original dictionary is :",my_dict)
newdict = add_key_value_pairs(my_dict,'Age',21)
print("The updated dictionary is :",newdict)
