#Multiplication Table
a=int(input("Enter the first number of table"))
i=a
j=1
k=2
while i<(a*10):
	for j in range(1,10):
		f=i*j
		print("{0:3}".format(f),end=" ")
	print("\n")	
	i=a*k
	k+=1