## Write a program to calculate percentage 
# of students based on marks any 5 subject

s1 =int(input("Enter marks of subject 1 :"))
s2 =int(input("Enter marks of subject 2 :"))
s3 =int(input("Enter marks of subject 3 :"))    
s4 =int(input("Enter marks of subject 4 :"))
s5 =int(input("Enter marks of subject 5 :"))
total = s1+s2+s3+s4+s5
percentage = (total/500)*100
print("Percentage of student is :",percentage)
