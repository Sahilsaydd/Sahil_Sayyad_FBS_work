### Write a program to prompt user to enter userid and password after verifying userid and password 
## Display a four digit random number and ask user to enter that number if user enters correct number 
## then display succeflly login otherwise display incorrect captcha
import random
userId  = input("Enter the UserId :")
Password  = input("Enter the password :")

if(userId == "Sahil" and Password == "Sahil@124"):
    captcha = random.randint(1000,9999)
    print(f"OTP is :{captcha}")
    userCaptcha = int(input("Enter the Otp :"))
    if(captcha == userCaptcha):
        print("Successfully login")
    else:
     print("Incorrect Captcha")
else:
    print("Incorrect UserId Or Password")