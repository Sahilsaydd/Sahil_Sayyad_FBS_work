## Named / keyword parameters / arguments
#1. Assigning value to the para in function call.
#2 . Flow of menioning from right to left.
#3. It skips positional para concept

def emp(id, name ,dept ,sal,address,age ):
    data = f'ID:{id}\nName:{name}\nDept:{dept}\nSalary:{sal}\nAge:{age}\nAddress:{address}\n'
    return data


print(emp(id=1 ,name='Sahil',dept="computer application" ,sal=35000,age=21,address="Ahmednagar"))
print(emp(id=2,name="sayyad",dept="computer application,", sal=45000,age=21, address="Ahmednagar"))