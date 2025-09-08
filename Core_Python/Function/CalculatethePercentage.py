def calculatePercentage():
    s1=int(input("Enter the Subject Marks 1 :"))
    s2=int(input("Enter the Subject Marks 2 :"))
    s3=int(input("Enter the Subject Marks 3  :"))
    s4=int(input("Enter the Subject Marks 4 :"))
    s5=int(input("Enter the Subject Marks 5 :"))
    total =s1+s2+s3+s4+s5
    percentage =(total/500)*100
    print(f"The percentage is : {percentage}")

calculatePercentage()