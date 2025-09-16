def Sos(n):
    if(n==0):
        return 0
    else:
        return n+Sos(n-1)
    
n= 5 
res = Sos(n)
print(f"The Addition of sum of series {res}")