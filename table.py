#Multiplication Table
a=int(input("Enter the first number of table"))
i=a
j=1
k=2
while i<(a*10):
	for j in range(1,10):
		f=i*j
		g=f
		count=0
		while g!=0:
			g=(int)(g/10)
			count+=1
		if count>=2 :
			print("  ",end="\t")
		else :
			print("   ",end="\t")
			
		print(f,end="\t")
	print("\n")	
	i=a*k
	k+=1
