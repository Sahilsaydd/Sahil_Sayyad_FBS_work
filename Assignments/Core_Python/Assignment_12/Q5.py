## write a python program to count the number of vowels in a string

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count


string = input("Enter a string :")
print("The original string is :",string)
cnt = count_vowels(string)
print("The number of vowels in the string is :",cnt)
