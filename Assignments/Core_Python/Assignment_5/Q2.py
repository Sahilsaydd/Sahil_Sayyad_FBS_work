##Enter the number of student from user.
## for those many student accept marks of 5 subjects 
## marks from user and calculate percentage .
## Display all percentage and average percentage of students
n= int(input('Enter number of students :'))
total_percentage =0
for i in range(n+1):
    print(f'Enter marks of student {i} :')
    total =0
    for j in range(1,6):
        marks =int(input(f'Enter marks of subject {j}:'))
        total += marks    
    
percentage = total/5
total_percentage += percentage

print(f'Percentage of student {i} is {percentage}%')
         
    