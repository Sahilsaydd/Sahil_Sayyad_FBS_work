
def series(n): 
    if(n>0):
        print(n,end=" ") 
        series(n-1)
       
  
n=5      
series(n)