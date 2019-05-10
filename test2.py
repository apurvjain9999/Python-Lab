a=int(input("enter a levels "))
u=0
lis=[]
i=1
while i<=a:
    print("\n")
    d=a
    if(i==4):
        u=0
    if(i<=3):
       #k=i
       lis.append(i)
       u=i
    else:
        
        u=u+sum(lis)
    
    while d>=i:
        
        print(" ",end="\t")
        d=d-1

   
    for j in range(1,i+1):
        
        print(u,end="\t\t")
    i=i+1
    
   
