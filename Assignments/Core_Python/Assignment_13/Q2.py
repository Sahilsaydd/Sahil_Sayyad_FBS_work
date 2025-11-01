## Write a python program to concatenate two dictionaries. 
def concatenate_dicts(dict1,dict2):
    dict1.update(dict2)
    return dict1


dict_a = {"Id":101,"Name":"Sahil Sayyad"}
dict_b = {"Age":21,"salary":50000}
print("The first dictionary is :",dict_a)
print("The second dictionary is:",dict_b)
new_dict = concatenate_dicts(dict_a,dict_b)
print("The concatenated dictionary is :",new_dict)
