## write a program to calculate the total cost of painting . THe interior of building with four equal sized walls
size = int(input('enter the size'))
cost = int(input('enter the cost'))
area = 4*size*size
total_cost = area*cost
print(f'The total cost of painting the interior of building is {total_cost}')
