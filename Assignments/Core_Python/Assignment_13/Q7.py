## Python program to remove the given the key from dictionary.

def removeKey(d,key):
    
    if(key not in d):
        return "Key not found"
    else:
        del d[key]
        return d


d = {'a':1, 'b':2, 'c':3}
Key = 'b'
print(removeKey(d,Key))