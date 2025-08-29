g=input('Enter the Gender (M/F) :')
age = int(input("Enter The Age :"))

if(g=="M"):
    if(age>=21):
        print(f'{g} you are eligible for marriage')
    else:
        print(f'{g} You are not eligible for marraige')
else:
    if(age>17):
        print(f'{g} You are Eligible for marriage')
    else:
        print(f'{g} You are not eligible for marriage')