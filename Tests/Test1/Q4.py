#Calculate the cost of painting the following buildings walls (both interior and exterior )
# You need to accept the are (one wall) and cost of both interior and exterior wall
#(Note : 1. Below diagram is of two joint rooms)
# it is upper view of building 
# 2. You need to calculate the cost of painting both interior and exterior walls
area = int(input("Enter the area :"))
pi = int(input("Enter the interior Cost :"))
pe = int(input("Enter the exrior cost :"))
interiorCost = area* pi
exteriorCost = area * pe
print(f" the interior cost is : {interiorCost}")
print(f" the exterior cost is : {exteriorCost}")
totalCost = interiorCost + exteriorCost
print(f"the total cost is : {totalCost}")
