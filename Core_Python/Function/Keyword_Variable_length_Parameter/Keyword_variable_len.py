def emp(**data):
    for i , j in data.items():
        print(f'{i}:{j}')
        
emp(id="101",name="Rohit" ,sal=25000)
print("___________________________________________________________")
emp(id="102",name='rahul',address="pune",age="21",sal=45000 ,dept="computer scicence")