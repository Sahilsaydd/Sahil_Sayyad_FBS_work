gender =input('Enter the Gender Male (M) / Female (F) : ')
age = int(input('Enter the age :'))
if(gender == 'M'):
    if(age>=21):
        print(f'{gender} You are eligible for marriage') 
    else:
        print(f'{gender} You are not eligible for marriage')
else:
    if(age>=18):
        print(f'{gender} You are not eligible for marriage')
    else:
        print(f'{gender} You are not eligible for marriage')