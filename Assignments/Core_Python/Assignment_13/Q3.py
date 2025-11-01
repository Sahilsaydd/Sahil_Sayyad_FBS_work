## Write a python to check if a given key already exists in a dictionary. or  not 
def check_key_exists(dictionary,key):
    if(key in dictionary):
        return True
    else:
        return False



my_dict = {"Id":101,"Name":"Sahil sayyad","Age":21}
print("The dictionary is :",my_dict)
keyToCheck = input("Enter the key to check :")
is_exists = check_key_exists(my_dict,keyToCheck)
if(is_exists):
    print(f'The key {keyToCheck} exists in the dictionary')
else:
    print(f'The key {keyToCheck} does not exist in the dictionary')


