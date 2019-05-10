a=int(input("enter number of transactions you want to have :\n"))
d={}
for i in range(a):
    b='T'+str(i+1)
    dd={}
    for j in range(a):
        if i!=j:
            c='T'+str(j+1)
            dd[c]=0
    
    d[b]=dd
            
    

print(d)
        
